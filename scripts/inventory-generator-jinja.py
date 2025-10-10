#!/srv/ansible/venv/bin/python3
import sys
import yaml
import re
from pathlib import Path
from collections import defaultdict, OrderedDict
from dataclasses import dataclass
from typing import Dict, List, Set, Any, Optional

# Compiled regex patterns for performance
SECTION_PATTERN = re.compile(r'^#+\s*$')
VAR_PATTERN = re.compile(r'^([a-z_][a-z0-9_]*)\s*:\s*(.*)$')
DOCKER_VAR_LOOKUP_PATTERN = re.compile(r"lookup\('docker_var',\s*'([^']+)'")
ROLE_VAR_LOOKUP_PATTERN = re.compile(r"lookup\('role_var',\s*'([^']+)'[^)]*\)")
COMMENT_IGNORE_PATTERN = re.compile(r'^(Title:|Author|https?://)')
VALID_ROLE_NAME_PATTERN = re.compile(r'^[a-z][a-z0-9_-]*$')

@dataclass
class Variable:
    name: str
    default_value: Any
    var_type: str
    section: str
    comment: Optional[str] = None

# Maximum number of lines to look ahead when checking if a comment belongs to a variable
LOOKAHEAD_LINES = 10

# Maximum length for value strings before truncation in display output
MAX_VALUE_DISPLAY_LENGTH = 60

# Type overrides for variables where dynamic type detection fails
# Format: 'variable_suffix': 'type'
# This will match any variable ending with the suffix
TYPE_OVERRIDES = {
    '_dns_proxy': 'bool',
    '_dns_record': 'string',
    '_dns_zone': 'string',
}

# Global inventory path - set via command line or default
INVENTORY_PATH = Path('/srv/git/saltbox/inventories/group_vars/all.yml')

# Type inference rules for role_var lookups
# Each rule is a tuple of (check_function, type_name)
# Rules are checked in order, first match wins
TYPE_INFERENCE_RULES = [
    # Exact matches first
    (lambda suffix, line: suffix == "_depends_on_healthchecks", "string (true/false)"),
    (lambda suffix, line: suffix == "_depends_on_delay", "string (number)"),
    (lambda suffix, line: suffix == "_depends_on", "string"),
    # Pattern matches
    (lambda suffix, line: "_scheme" in suffix, "string (http/https)"),
    (lambda suffix, line: "_enabled" in suffix or "_proxy" in suffix, "bool"),
    (lambda suffix, line: "_domain" in suffix or "_subdomain" in suffix or "_url" in suffix, "string"),
    (lambda suffix, line: "_port" in suffix or "_timeout" in suffix, "string/int"),
    # Line context checks
    (lambda suffix, line: "| bool" in line, "bool"),
    (lambda suffix, line: re.search(r"default=['\"]", line) is not None, "string"),
    (lambda suffix, line: re.search(r"default=(false|true)\b", line, re.IGNORECASE) is not None, "bool"),
    (lambda suffix, line: "default={}" in line or "default=omit" in line, "dict/omit"),
    (lambda suffix, line: "default=[]" in line, "list"),
]

# Load role_var configuration from YAML file
def load_role_var_config():
    """Load role_var descriptions, examples, defaults, and ignore list from YAML config file"""
    config_file = Path(__file__).parent / 'global_override_options.yml'
    try:
        with open(config_file) as f:
            config = yaml.safe_load(f) or {}

        descriptions = {}
        defaults = {}
        ignore_suffixes = set(config.get('ignore_suffixes', []))

        for suffix, data in config.items():
            if suffix == 'ignore_suffixes':
                continue
            if isinstance(data, dict):
                descriptions[suffix] = data
                defaults[suffix] = data.get('default')

        return descriptions, defaults, ignore_suffixes
    except FileNotFoundError:
        print(f"Warning: Config file not found: {config_file}", file=sys.stderr)
        return {}, {}, set()
    except yaml.YAMLError as e:
        print(f"Warning: Invalid YAML in config file: {e}", file=sys.stderr)
        return {}, {}, set()

def load_role_var_examples():
    """Load role-specific variable example overrides from YAML config file"""
    config_file = Path(__file__).parent / 'role_var_examples.yml'
    try:
        with open(config_file) as f:
            config = yaml.safe_load(f) or {}
        return config
    except FileNotFoundError:
        # File is optional, return empty dict
        return {}
    except yaml.YAMLError as e:
        print(f"Warning: Invalid YAML in role var examples file: {e}", file=sys.stderr)
        return {}

# Load configuration at module level
ROLE_VAR_DESCRIPTIONS, ROLE_VAR_DEFAULTS, IGNORE_ROLE_VAR_SUFFIXES = load_role_var_config()
ROLE_VAR_EXAMPLE_OVERRIDES = load_role_var_examples()

class RoleVariableParser:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.roles_path = repo_path / 'roles'
        self.resources_path = repo_path / 'resources'
        # Caches for expensive lookups
        self._docker_vars_cache = None
        self._role_var_lookups_cache = None

    def get_type(self, value: Any, var_name: str = "") -> str:
        """Determine the type of a variable

        Args:
            value: The variable value
            var_name: The variable name (for checking overrides)
        """
        # Check type overrides first
        for suffix, override_type in TYPE_OVERRIDES.items():
            if var_name.endswith(suffix):
                return override_type

        # Dynamic type detection
        if value is None:
            return "null"
        elif isinstance(value, bool):
            return "bool"
        elif isinstance(value, int):
            return "int"
        elif isinstance(value, str):
            return "string"
        elif isinstance(value, list):
            return "list"
        elif isinstance(value, dict):
            return "dict"
        else:
            return "unknown"

    def format_value(self, value: Any) -> str:
        """Format a value for display in terminal output

        Args:
            value: The value to format (any type)

        Returns:
            String representation suitable for terminal display
        """
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    def get_raw_value(self, var_name: str) -> str:
        """Get the raw value as it appears in the YAML file

        Args:
            var_name: The variable name to look up

        Returns:
            Raw value string from YAML file, or empty string if not found
        """
        if hasattr(self, '_raw_lines') and var_name in self._raw_lines:
            return self._raw_lines[var_name]
        # Fallback to empty string if not found
        return ""

    def format_type_comment(self, var_type: str, indent: str = "    ") -> str:
        """Format a type annotation comment with user-friendly format

        Args:
            var_type: The variable type
            indent: The indentation string to prepend

        Returns:
            Formatted type comment string
        """
        if var_type == "bool":
            return f"{indent}# Type: bool (true/false)"
        elif var_type == "string":
            return f"{indent}# Type: string"
        elif var_type == "list":
            return f"{indent}# Type: list"
        elif var_type == "dict":
            return f"{indent}# Type: dict"
        elif var_type == "string (true/false)":
            return f"{indent}# Type: string (\"true\"/\"false\")"
        elif var_type == "string (number)":
            return f"{indent}# Type: string (quoted number)"
        elif var_type == "string (http/https)":
            return f"{indent}# Type: string (\"http\"/\"https\")"
        else:
            return f"{indent}# Type: {var_type}"

    def get_docker_var_type_comment(self, var_suffix: str, indent: str = "    ") -> str:
        """Get type comment for docker variable based on suffix

        Args:
            var_suffix: The docker variable suffix (e.g., 'auto_remove', 'cpu_shares')
            indent: The indentation string to prepend

        Returns:
            Formatted type comment string

        Reference: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html
        """
        if var_suffix in ['auto_remove', 'cleanup', 'detach', 'init', 'keep_volumes', 'oom_killer',
                          'output_logs', 'paused', 'privileged', 'read_only', 'recreate']:
            return f"{indent}# Type: bool (true/false)"
        elif var_suffix in ['blkio_weight', 'cpu_period', 'cpu_quota', 'cpu_shares', 'healthy_wait_timeout',
                            'memory_swappiness', 'oom_score_adj', 'restart_retries', 'stop_timeout']:
            return f"{indent}# Type: int"
        elif var_suffix in ['capabilities', 'cap_drop', 'commands', 'device_cgroup_rules', 'device_read_bps',
                            'device_read_iops', 'device_requests', 'device_write_bps', 'device_write_iops',
                            'devices', 'dns_opts', 'dns_search_domains', 'dns_servers', 'exposed_ports',
                            'groups', 'links', 'mounts', 'networks', 'ports', 'security_opts', 'sysctls',
                            'tmpfs', 'ulimits', 'volumes', 'volumes_from']:
            return f"{indent}# Type: list"
        elif var_suffix in ['envs', 'healthcheck', 'hosts', 'labels', 'log_options', 'storage_opts']:
            return f"{indent}# Type: dict"
        else:
            # Everything else is string: cpus, cpuset_cpus, cpuset_mems, domainname, entrypoint, etc.
            return f"{indent}# Type: string"

    def adjust_multiline_indentation(self, value_lines: List[str], original_var_name: str,
                                     new_var_name: str, output_indent: str) -> List[str]:
        """Adjust indentation of multi-line YAML values when variable name changes

        When a variable name changes (e.g., sonarr_role_var -> sonarr2_var), multi-line
        values that are aligned with the original value position need to be re-aligned.

        Args:
            value_lines: Lines of the multi-line value (first line already split from var name)
            original_var_name: Original variable name
            new_var_name: New variable name
            output_indent: Base indentation for output lines

        Returns:
            List of formatted lines ready to append to output
        """
        result = []
        result.append(f"{output_indent}{new_var_name}: {value_lines[0]}")

        # Calculate indentation adjustment based on variable name length change
        # Format: "var_name: " = name + ": " = len(name) + 2
        original_indent = len(original_var_name) + 2
        new_indent = len(new_var_name) + 2
        indent_diff = original_indent - new_indent

        for continuation_line in value_lines[1:]:
            # Only adjust indentation for lines that appear to be indented
            # to align with the first line's value position
            if continuation_line and continuation_line[0] == ' ':
                # Count leading spaces
                leading_spaces = len(continuation_line) - len(continuation_line.lstrip(' '))

                # Only adjust if the indentation matches the original alignment
                # (this preserves dict/list structure indentation)
                if leading_spaces >= original_indent:
                    # This looks like an aligned continuation line
                    if indent_diff > 0:
                        # New var is shorter, remove spaces
                        adjusted_line = ' ' * (leading_spaces - indent_diff) + continuation_line.lstrip(' ')
                    elif indent_diff < 0:
                        # New var is longer, add spaces
                        adjusted_line = ' ' * (leading_spaces + abs(indent_diff)) + continuation_line.lstrip(' ')
                    else:
                        adjusted_line = continuation_line
                else:
                    # This is structural indentation (dict/list), keep as-is
                    adjusted_line = continuation_line
            else:
                # No leading space, keep as-is
                adjusted_line = continuation_line
            result.append(f"{output_indent}{adjusted_line}")

        return result

    def parse_yaml_with_sections(self, file_path: Path) -> Dict:
        """Parse YAML and extract section headers and comments for variables

        Returns an OrderedDict to preserve file order
        """
        variables = OrderedDict()
        current_section = None
        pending_comments = []

        # Store raw lines for later reference
        self._raw_lines = {}

        try:
            with open(file_path) as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            return OrderedDict()
        except PermissionError:
            print(f"Error: Permission denied reading: {file_path}", file=sys.stderr)
            return OrderedDict()
        except IOError as e:
            print(f"Error: Failed to read file {file_path}: {e}", file=sys.stderr)
            return OrderedDict()

        for i, line in enumerate(lines):
            stripped = line.strip()

            # Check if this is a section header block (#### lines)
            if SECTION_PATTERN.match(stripped):
                # Check if next line has content and line after that is also ####
                if i < len(lines) - 1:
                    next_line = lines[i + 1].strip()
                    if next_line.startswith('#') and not SECTION_PATTERN.match(next_line):
                        # Extract section name
                        if i < len(lines) - 2 and SECTION_PATTERN.match(lines[i + 2].strip()):
                            # This is a section header
                            section_text = next_line.lstrip('#').strip()
                            if section_text:
                                current_section = section_text
                                pending_comments = []
                                continue

            # Track comments that appear right before variables (not section headers)
            # Skip indented comments as they are part of multi-line values (lists/dicts)
            if stripped.startswith('#') and not SECTION_PATTERN.match(stripped) and not line.startswith(' '):
                # Check if this looks like a variable comment (not URL, Title, Author, etc.)
                comment_text = stripped.lstrip('#').strip()
                if comment_text and not COMMENT_IGNORE_PATTERN.match(comment_text):
                    # Check if the next non-comment line is a variable
                    is_var_comment = False
                    for j in range(i + 1, min(i + 1 + LOOKAHEAD_LINES, len(lines))):
                        next_line = lines[j].strip()
                        if not next_line.startswith('#') and next_line:
                            if ':' in next_line and not next_line.startswith('---'):
                                is_var_comment = True
                            break

                    if is_var_comment:
                        pending_comments.append(comment_text)
            # Clear pending comments if we hit a blank line
            elif not stripped:
                # Don't clear if next line is a variable (blank lines between comment and var are ok)
                if i < len(lines) - 1:
                    next_line = lines[i + 1].strip()
                    if not (':' in next_line and not next_line.startswith('#')):
                        pending_comments = []

            # Parse variable definitions
            if ':' in line and not stripped.startswith('#') and not stripped.startswith('---'):
                var_match = VAR_PATTERN.match(line)
                if var_match:
                    var_name = var_match.group(1)
                    raw_value = var_match.group(2).rstrip()

                    # Check for continuation lines (multi-line values or lists)
                    j = i + 1
                    while j < len(lines):
                        next_line = lines[j]
                        stripped_next = next_line.strip()

                        # Skip blank lines (but not indented comments)
                        if not stripped_next:
                            j += 1
                            continue

                        # Check if this is a new top-level variable (starts at column 0)
                        if re.match(r'^[a-z_][a-z0-9_]*\s*:', next_line):
                            # This is a new variable, stop
                            break

                        # If line starts with any indentation (including indented comments), it's a continuation
                        if next_line.startswith(' '):
                            raw_value += '\n' + next_line.rstrip()
                            j += 1
                            continue

                        # Hit a non-indented line that's not a variable, stop
                        break

                    # Store the raw line value for later use
                    self._raw_lines[var_name] = raw_value

                    # Join multi-line comments
                    full_comment = '\n'.join(pending_comments) if pending_comments else None
                    variables[var_name] = {
                        'line': i + 1,  # Convert to 1-based line number for display
                        'section': current_section or 'General',
                        'comment': full_comment
                    }
                    pending_comments = []

        return variables

    def find_docker_var_lookups(self) -> Set[str]:
        """Find all docker_var lookup variables from resources/tasks/docker/*.yml

        Scans docker task files for lookup('docker_var', 'suffix') patterns and
        extracts the variable suffixes. Results are cached for performance.

        Returns:
            Set of docker variable suffixes found in task files
        """
        # Return cached result if available
        if self._docker_vars_cache is not None:
            return self._docker_vars_cache

        docker_vars = set()
        docker_tasks_path = self.resources_path / 'tasks' / 'docker'

        if not docker_tasks_path.exists():
            self._docker_vars_cache = docker_vars
            return docker_vars

        for yml_file in docker_tasks_path.glob('*.yml'):
            try:
                with open(yml_file) as f:
                    content = f.read()
                    for match in DOCKER_VAR_LOOKUP_PATTERN.finditer(content):
                        var_suffix = match.group(1)
                        # Strip the leading _docker_ prefix if present
                        if var_suffix.startswith('_docker_'):
                            var_suffix = var_suffix[8:]  # len('_docker_') = 8
                        docker_vars.add(var_suffix)
            except (FileNotFoundError, PermissionError, IOError) as e:
                print(f"Warning: Failed to read {yml_file}: {e}", file=sys.stderr)
                continue

        self._docker_vars_cache = docker_vars
        return docker_vars

    def find_role_var_lookups(self) -> Dict[str, str]:
        """Find all role_var lookup variables from inventories/group_vars/all.yml with types

        Scans the inventory file for lookup('role_var', 'suffix') patterns and infers
        variable types from context (naming patterns and usage). Results are cached.

        Returns:
            Dictionary mapping variable suffixes to their inferred types
        """
        # Return cached result if available
        if self._role_var_lookups_cache is not None:
            return self._role_var_lookups_cache

        lookups = {}  # suffix -> inferred type

        if not INVENTORY_PATH.exists():
            self._role_var_lookups_cache = lookups
            return lookups

        try:
            with open(INVENTORY_PATH) as f:
                lines = f.readlines()

            # Find all lookup('role_var', 'suffix') patterns with context
            for line in lines:
                for match in ROLE_VAR_LOOKUP_PATTERN.finditer(line):
                    var_suffix = match.group(1)

                    # Skip ignored suffixes
                    if var_suffix in IGNORE_ROLE_VAR_SUFFIXES:
                        continue

                    # Try to infer type from context using rule-based system
                    inferred_type = "unknown"
                    for check_func, type_name in TYPE_INFERENCE_RULES:
                        if check_func(var_suffix, line):
                            inferred_type = type_name
                            break

                    # Store or update (keep more specific type if already exists)
                    if var_suffix not in lookups or inferred_type != "unknown":
                        lookups[var_suffix] = inferred_type

        except FileNotFoundError:
            # File doesn't exist, return empty lookups
            pass
        except PermissionError:
            print(f"Warning: Permission denied reading {INVENTORY_PATH}", file=sys.stderr)
        except Exception as e:
            print(f"Warning: Error parsing role_var lookups from {INVENTORY_PATH}: {e}", file=sys.stderr)

        self._role_var_lookups_cache = lookups
        return lookups

    def parse_role(self, role_name: str) -> tuple[Dict[str, Variable], OrderedDict[str, Dict[str, Any]]]:
        """Parse a role's defaults/main.yml

        Returns: (variables dict, parsed OrderedDict for preserving order)
        """
        defaults_file = self.roles_path / role_name / 'defaults' / 'main.yml'

        if not defaults_file.exists():
            return {}, OrderedDict()

        variables = {}
        parsed = self.parse_yaml_with_sections(defaults_file)

        # Load actual values with error handling
        try:
            with open(defaults_file) as f:
                yaml_data = yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            print(f"Error: Invalid YAML in {defaults_file}: {e}", file=sys.stderr)
            return {}, OrderedDict()
        except FileNotFoundError:
            print(f"Error: File not found: {defaults_file}", file=sys.stderr)
            return {}, OrderedDict()
        except PermissionError:
            print(f"Error: Permission denied reading: {defaults_file}", file=sys.stderr)
            return {}, OrderedDict()
        except IOError as e:
            print(f"Error: Failed to read file {defaults_file}: {e}", file=sys.stderr)
            return {}, OrderedDict()

        for var_name, meta in parsed.items():
            value = yaml_data.get(var_name)
            variables[var_name] = Variable(
                name=var_name,
                default_value=value,
                var_type=self.get_type(value, var_name),
                section=meta['section'],
                comment=meta.get('comment')
            )

        return variables, parsed


    def extract_instance_name_var(self, role_name: str, role_vars: Dict[str, Variable]) -> Optional[str]:
        """Try to find the instances variable for this role

        Args:
            role_name: Name of the role
            role_vars: Dictionary of role variables

        Returns:
            The instances variable name if found, None otherwise
        """
        instances_var = f"{role_name}_instances"
        if instances_var in role_vars:
            return instances_var
        return None

    def display_role_analysis(self, role_name: str):
        """Display formatted analysis for a role to terminal

        Outputs a comprehensive analysis including:
        - Role variables from defaults/main.yml
        - Override instructions
        - Docker container options
        - Global override options

        Args:
            role_name: Name of the role to analyze
        """
        role_vars, parsed = self.parse_role(role_name)
        docker_vars = self.find_docker_var_lookups()
        role_var_lookups = self.find_role_var_lookups()

        instances_var = self.extract_instance_name_var(role_name, role_vars)

        print(f"\n{'='*80}")
        print(f"ROLE: {role_name}")
        print(f"{'='*80}\n")

        # Section 1: Role Variables
        print(f"1. ROLE VARIABLES")
        print(f"   Source: roles/{role_name}/defaults/main.yml\n")

        if not role_vars:
            print("   No variables found.\n")
        else:
            # Identify variables that have _default/_custom variants to hide base vars
            has_default_custom = set()
            for var_name in role_vars.keys():
                if var_name.endswith('_default') or var_name.endswith('_custom'):
                    base_name = var_name.rsplit('_', 1)[0]
                    if base_name in role_vars:
                        has_default_custom.add(base_name)

            # Group by section, preserving order from file
            sections = defaultdict(list)
            section_order = []

            for var_name in parsed.keys():  # parsed maintains file order
                var = role_vars.get(var_name)
                if var and var.name not in has_default_custom:
                    sections[var.section].append(var)
                    # Track section order as they first appear
                    if var.section not in section_order:
                        section_order.append(var.section)

            for section in section_order:
                if section not in sections:
                    continue
                vars_list = sections[section]
                print(f"   [{section}]")
                first_in_section = True
                for var in vars_list:
                    # Show comment if exists
                    if var.comment:
                        # Only add blank line if not the first item in section
                        if not first_in_section:
                            print()
                        # Handle multi-line comments
                        for comment_line in var.comment.split('\n'):
                            print(f"   # {comment_line}")

                    # Format value preview
                    value_str = self.format_value(var.default_value)
                    if len(value_str) > MAX_VALUE_DISPLAY_LENGTH:
                        value_str = value_str[:MAX_VALUE_DISPLAY_LENGTH - 3] + "..."

                    print(f"   {var.name:<45} {var.var_type:<8} {value_str}")
                    first_in_section = False
                print()

        # Section 2: How to Override Variables
        print(f"2. HOW TO OVERRIDE")
        print(f"   All variables from section 1 can be overridden in:")
        print(f"   - /srv/git/saltbox/inventories/host_vars/localhost.yml\n")

        if instances_var:
            print(f"   Instance Support:")
            print(f"   This role supports multiple instances via '{instances_var}'.")
            print(f"   You can override per instance by removing '_role' from the variable name:\n")
            print(f"   Role-level:     {role_name}_role_web_subdomain: \"sonarr\"")
            print(f"   Instance-level: sonarr4k_web_subdomain: \"sonarr4k\"\n")
        else:
            print(f"   Simply set any variable from section 1 with your desired value.\n")

        # Mark base variables as shown so they don't appear elsewhere
        has_default_custom = set()
        for var_name in role_vars.keys():
            if var_name.endswith('_default') or var_name.endswith('_custom'):
                base_name = var_name.rsplit('_', 1)[0]
                if base_name in role_vars:
                    has_default_custom.add(base_name)
        shown_vars = set(has_default_custom)

        # Section 3: Docker Variables (if role uses docker)
        all_docker_role_vars = [v for v in role_vars.keys() if '_docker_' in v]
        docker_role_vars_not_shown = [v for v in all_docker_role_vars if v not in shown_vars]

        # Dynamic section counter
        section_counter = 3

        # Check if role uses docker
        if all_docker_role_vars:
            # Get suffixes of all docker vars defined in role
            role_docker_vars_suffixes = set()
            for var_name in all_docker_role_vars:
                match = re.match(f'^{role_name}_role_docker_(.+)$', var_name)
                if match:
                    role_docker_vars_suffixes.add(match.group(1))

            # Find additional docker vars from resources
            additional_docker_vars = []
            for docker_var in sorted(docker_vars):
                if docker_var not in role_docker_vars_suffixes:
                    additional_docker_vars.append(docker_var)

            # Only show docker section if there are unshown role vars or additional vars
            if docker_role_vars_not_shown or additional_docker_vars:
                print(f"{section_counter}. DOCKER CONTAINER OPTIONS")
                section_counter += 1
                print(f"   This role creates a Docker container. The following docker options")
                print(f"   are available via the resources/tasks/docker/create_docker_container.yml task.")
                print(f"   For type/format information, see:")
                print(f"   https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html\n")

                print(f"   You can override these using:")
                print(f"   - {role_name}_role_docker_<option>")
                if instances_var:
                    print(f"   - <instance_name>_docker_<option>  (for specific instances)")
                print()

                if additional_docker_vars:
                    print(f"   Additional docker options available (not defined in role, but supported):")
                    for var_suffix in additional_docker_vars:
                        var_name = f"{role_name}_role_docker_{var_suffix}"
                        print(f"   {var_name}")
                    print()

        # Global Override Options (role_var lookups)
        if role_var_lookups:
            print(f"{section_counter}. GLOBAL OVERRIDE OPTIONS")
            section_counter += 1
            print(f"   These options are available for ANY role via /srv/git/saltbox/inventories/host_vars/localhost.yml")
            print(f"   They are defined in /srv/git/saltbox/inventories/group_vars/all.yml using lookup('role_var', ...)\n")

            print(f"   You can override these using:")
            print(f"   - {role_name}_role<suffix>")
            if instances_var:
                print(f"   - <instance_name><suffix>  (for specific instances)")
            print()

            for suffix in sorted(role_var_lookups.keys()):
                var_type = role_var_lookups[suffix]
                role_var_name = f"{role_name}_role{suffix}"
                print(f"   {role_var_name:<50} {var_type}")
            print()

        print(f"{'='*80}\n")

def format_default_value_filter(value, var_type):
    """Filter to format default values with proper quoting"""
    if var_type.startswith("string"):
        if not (value.startswith('"') or value.startswith("'") or value in ['[]', '{}']):
            if value == '':
                return '""'
            else:
                return f'"{value}"'
    return value

def get_example_value_for_type(var_type):
    """Generate an appropriate example value based on variable type"""
    if var_type == "bool":
        return "true"
    elif var_type == "int":
        return "42"
    elif var_type == "string":
        return '"custom_value"'
    elif var_type == "list":
        return '["item1", "item2"]'
    elif var_type == "dict":
        return '{"key": "value"}'
    elif var_type == "string (true/false)":
        return '"true"'
    elif var_type == "string (number)":
        return '"30"'
    elif var_type == "string (http/https)":
        return '"https"'
    elif var_type == "string/int":
        return "8080"
    else:
        return '"custom_value"'

def prepare_template_context(role_name, role_vars, parsed, instances_var, role_var_lookups, parser):
    """Prepare context dictionary for Jinja2 template"""

    # Filter out variables with _default/_custom patterns
    has_default_custom = set()
    for var_name in role_vars.keys():
        if var_name.endswith('_default') or var_name.endswith('_custom'):
            base_name = var_name.rsplit('_', 1)[0]
            if base_name in role_vars:
                has_default_custom.add(base_name)

    # Ignore variables
    ignored_vars = set()
    for var_name, var in role_vars.items():
        if var.comment:
            if 'Do not edit or override using the inventory' in var.comment or 'Skip docs' in var.comment:
                ignored_vars.add(var_name)
        if '_paths_folders_list' in var_name:
            ignored_vars.add(var_name)

    # Group variables by section
    sections = OrderedDict()
    section_order = []

    for var_name in parsed.keys():
        var = role_vars.get(var_name)
        if var and var.name not in has_default_custom and var.name not in ignored_vars:
            raw_value = parser.get_raw_value(var.name)
            # Create variable dict for template
            var_dict = {
                'name': var.name,
                'var_type': var.var_type,
                'raw_value': raw_value,
                'comment': var.comment,
                'comment_lines': var.comment.split('\n') if var.comment else [],
                'has_inline_comments': '\n' in raw_value and any(
                    line.strip().startswith('#') for line in raw_value.split('\n')
                ),
                'is_multiline': '\n' in raw_value,
                'value_lines': raw_value.split('\n') if '\n' in raw_value else [raw_value],
                'instance_name': var.name.replace(f'{role_name}_role_', f'{role_name}2_'),
                'section': var.section
            }

            if var.section not in sections:
                sections[var.section] = []
                section_order.append(var.section)

            sections[var.section].append(var_dict)

    # Find example variable
    example_var = None
    example_var_type = "string"
    example_var_value = None

    # Check if there's an override for any variable in this role
    for var_name in role_vars.keys():
        if var_name in ROLE_VAR_EXAMPLE_OVERRIDES:
            example_var = var_name
            example_var_type = role_vars[var_name].var_type
            example_var_value = ROLE_VAR_EXAMPLE_OVERRIDES[var_name]
            break

    # If no override found, use default logic
    if not example_var:
        for var_name in list(role_vars.keys())[:5]:
            if '_docker_image_tag' in var_name:
                example_var = var_name
                example_var_type = role_vars[var_name].var_type
                break
        if not example_var:
            first_var_name = list(role_vars.keys())[0] if role_vars else f"{role_name}_example_var"
            example_var = first_var_name
            if first_var_name in role_vars:
                example_var_type = role_vars[first_var_name].var_type

    # Find docker vars if needed
    docker_info = None
    all_docker_role_vars = [v for v in role_vars.keys() if '_docker_' in v]
    if all_docker_role_vars:
        docker_vars = parser.find_docker_var_lookups()

        # Get suffixes of all docker vars defined in role
        role_docker_vars_suffixes = set()
        for var_name in all_docker_role_vars:
            match = re.match(f'^{role_name}_role_docker_(.+)$', var_name)
            if match:
                role_docker_vars_suffixes.add(match.group(1))

        # Find additional docker vars from resources
        additional_docker_vars = []
        for docker_var in sorted(docker_vars):
            if docker_var not in role_docker_vars_suffixes:
                additional_docker_vars.append(docker_var)

        if additional_docker_vars:
            # Group by category based on variable name
            categories = defaultdict(list)
            for var_suffix in additional_docker_vars:
                if any(x in var_suffix for x in ['cpu', 'memory', 'blkio']):
                    categories['Resource Limits'].append(var_suffix)
                elif any(x in var_suffix for x in ['device', 'cap_', 'privileged', 'security']):
                    categories['Security & Devices'].append(var_suffix)
                elif any(x in var_suffix for x in ['network', 'dns', 'hostname', 'hosts']):
                    categories['Networking'].append(var_suffix)
                elif any(x in var_suffix for x in ['volume', 'mount', 'working_dir']):
                    categories['Storage'].append(var_suffix)
                elif any(x in var_suffix for x in ['log', 'healthcheck', 'init']):
                    categories['Monitoring & Lifecycle'].append(var_suffix)
                else:
                    categories['Other Options'].append(var_suffix)

            docker_info = {
                'additional_vars': additional_docker_vars,
                'categories': dict(categories),
                'category_order': ['Resource Limits', 'Security & Devices', 'Networking', 'Storage', 'Monitoring & Lifecycle', 'Other Options']
            }

    return {
        'role_name': role_name,
        'instances_var': instances_var,
        'sections': sections,
        'role_var_lookups': role_var_lookups,
        'role_var_descriptions': ROLE_VAR_DESCRIPTIONS,
        'role_var_defaults': ROLE_VAR_DEFAULTS,
        'example_var': example_var,
        'example_var_type': example_var_type,
        'example_var_value': example_var_value,
        'docker_info': docker_info,
        'parser': parser,
    }

def generate_docs_section(role_name: str, repo_path: Path, is_sandbox: bool = False) -> str:
    """Generate a markdown documentation section using Jinja2 template"""

    # Create parser
    parser = RoleVariableParser(repo_path)
    if is_sandbox:
        parser.roles_path = repo_path / 'roles'

    # Get role data
    role_vars, parsed = parser.parse_role(role_name)
    role_var_lookups = parser.find_role_var_lookups()
    instances_var = parser.extract_instance_name_var(role_name, role_vars)

    if not role_vars:
        return f"No variables found for role '{role_name}'"

    # Prepare data for template
    context = prepare_template_context(
        role_name, role_vars, parsed, instances_var,
        role_var_lookups, parser
    )

    # Load and render template
    from jinja2 import Environment, FileSystemLoader
    template_dir = Path(__file__).parent / 'templates'
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Add custom global functions (callable in templates)
    # These return comment text without indentation - the template handles spacing
    env.globals['format_type_comment'] = lambda var_type: parser.format_type_comment(var_type, "")
    env.globals['get_docker_var_type_comment'] = lambda var_suffix: parser.get_docker_var_type_comment(var_suffix, "")
    env.globals['adjust_multiline_indentation'] = lambda value_lines, orig_name, new_name, indent: parser.adjust_multiline_indentation(value_lines, orig_name, new_name, indent)
    env.globals['format_default_value'] = format_default_value_filter
    env.globals['get_example_value'] = get_example_value_for_type

    template = env.get_template('role_docs.md.j2')
    return template.render(**context)

def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser(
        description='Analyze Saltbox role variables and generate documentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python3 test.py sonarr
  python3 test.py sandbox-myapp
  python3 test.py plex --write-docs /opt/git/docs/docs/apps/plex.md
  python3 test.py plex --saltbox-repo /custom/path --write-docs docs.md
        '''
    )

    parser.add_argument('role_name', help='Role name (or sandbox-<name> for sandbox roles)')
    parser.add_argument('--write-docs', metavar='PATH', help='Write documentation to specified markdown file')
    parser.add_argument('--saltbox-repo', metavar='PATH', default='/srv/git/saltbox',
                        help='Path to Saltbox repository (default: /srv/git/saltbox)')
    parser.add_argument('--sandbox-repo', metavar='PATH', default='/opt/sandbox',
                        help='Path to Sandbox repository (default: /opt/sandbox)')
    parser.add_argument('--inventory-path', metavar='PATH',
                        help='Path to inventory all.yml file (default: /srv/git/saltbox/inventories/group_vars/all.yml)')

    # Show available roles if no arguments
    if len(sys.argv) == 1:
        parser.print_help()
        print("\nAvailable roles:")
        default_repo = Path(__file__).parent
        roles_path = default_repo / 'roles'
        if roles_path.exists():
            roles = sorted([r.name for r in roles_path.iterdir() if r.is_dir()])
            for i in range(0, min(30, len(roles)), 3):
                row = roles[i:i+3]
                print(f"  {row[0]:<25} {row[1] if len(row) > 1 else '':<25} {row[2] if len(row) > 2 else '':<25}")
            if len(roles) > 30:
                print(f"\n  ... and {len(roles) - 30} more")

        # Check for sandbox roles
        sandbox_path = Path('/opt/sandbox') / 'roles'
        if sandbox_path.exists():
            sandbox_roles = sorted([r.name for r in sandbox_path.iterdir() if r.is_dir()])
            if sandbox_roles:
                print("\nSandbox roles (use sandbox-<name>):")
                for i in range(0, min(20, len(sandbox_roles)), 3):
                    row = sandbox_roles[i:i+3]
                    print(f"  sandbox-{row[0]:<20} {('sandbox-' + row[1]) if len(row) > 1 else '':<25} {('sandbox-' + row[2]) if len(row) > 2 else '':<25}")
                if len(sandbox_roles) > 20:
                    print(f"\n  ... and {len(sandbox_roles) - 20} more")
        print()
        sys.exit(1)

    args = parser.parse_args()

    # Determine repository paths
    repo_path = Path(args.saltbox_repo)
    sandbox_repo_path = Path(args.sandbox_repo)

    # Check if this is a sandbox role
    role_input = args.role_name
    is_sandbox = role_input.startswith('sandbox-')
    if is_sandbox:
        role_name = role_input[8:]  # Remove 'sandbox-' prefix
    else:
        role_name = role_input

    # Validate role name
    if not VALID_ROLE_NAME_PATTERN.match(role_name):
        print(f"fatal: Invalid role name '{role_name}'. Role names must start with a lowercase letter and contain only lowercase letters, numbers, hyphens, and underscores.", file=sys.stderr)
        sys.exit(1)

    if is_sandbox:
        sandbox_roles_path = sandbox_repo_path / 'roles'
        role_path = sandbox_roles_path / role_name
        if not role_path.exists():
            print(f"fatal: Sandbox role '{role_name}' not found at {role_path}", file=sys.stderr)
            sys.exit(1)
        defaults_file = role_path / 'defaults' / 'main.yml'
        if not defaults_file.exists():
            print(f"fatal: Role '{role_name}' has no defaults file at {defaults_file}", file=sys.stderr)
            sys.exit(1)
    else:
        role_path = repo_path / 'roles' / role_name
        if not role_path.exists():
            print(f"fatal: Role '{role_name}' not found at {role_path}", file=sys.stderr)
            sys.exit(1)
        defaults_file = role_path / 'defaults' / 'main.yml'
        if not defaults_file.exists():
            print(f"fatal: Role '{role_name}' has no defaults file at {defaults_file}", file=sys.stderr)
            sys.exit(1)

    # Set global inventory path
    global INVENTORY_PATH
    if args.inventory_path:
        INVENTORY_PATH = Path(args.inventory_path)

    # Handle documentation generation
    if args.write_docs:
        docs_path = Path(args.write_docs)
        if not docs_path.exists():
            print(f"fatal: Documentation file not found: {docs_path}", file=sys.stderr)
            sys.exit(1)

        # Read existing docs
        with open(docs_path) as f:
            original_content = f.read()

        # Check if managed section exists
        if '<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->' not in original_content:
            print(f"fatal: Documentation file does not contain managed section markers", file=sys.stderr)
            sys.exit(1)

        # Generate new section - pass sandbox_repo_path for sandbox roles
        if is_sandbox:
            new_section = generate_docs_section(role_name, sandbox_repo_path, is_sandbox)
        else:
            new_section = generate_docs_section(role_name, repo_path, is_sandbox)

        # Replace the managed section
        import re
        pattern = r'<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->.*?<!-- END SALTBOX MANAGED VARIABLES SECTION -->'
        replacement = f'<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->\n<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->{new_section}\n<!-- END SALTBOX MANAGED VARIABLES SECTION -->'
        new_content = re.sub(pattern, replacement, original_content, flags=re.DOTALL)

        # Generate diff
        import difflib
        diff = difflib.unified_diff(
            original_content.splitlines(keepends=True),
            new_content.splitlines(keepends=True),
            fromfile=str(docs_path),
            tofile=str(docs_path),
            lineterm=''
        )

        # Write updated docs
        with open(docs_path, 'w') as f:
            f.write(new_content)

        # Print diff
        print(''.join(diff), end='')
        sys.exit(0)

    # Normal display mode
    if is_sandbox:
        # Create a custom parser that uses sandbox roles but Saltbox inventory
        role_parser = RoleVariableParser(repo_path)
        # Override the roles_path to point to sandbox
        role_parser.roles_path = sandbox_repo_path / 'roles'
        role_parser.display_role_analysis(role_name)
    else:
        role_parser = RoleVariableParser(repo_path)
        role_parser.display_role_analysis(role_name)

if __name__ == '__main__':
    main()
