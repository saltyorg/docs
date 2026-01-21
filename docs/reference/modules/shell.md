---
icon: material/cogs
status: draft
saltbox_automation:
  project_description:
    name: Shell
    summary: |-
      a Saltbox module that installs and configures a user's shell (Bash or Zsh) with tools like z for directory jumping, argcomplete for tab completion, Oh My Zsh and optional Oh My Posh theming.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Shell

## Overview

Shell is a Saltbox module that installs and configures a user's shell (Bash or Zsh) with tools like z for directory jumping, argcomplete for tab completion, Oh My Zsh and optional Oh My Posh theming.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Core Saltbox role.

```shell
sb install shell
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        shell_type: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `shell_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `shell_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`shell_type`"

        ```yaml
        # Type: string
        shell_type: "{{ shell | default('zsh') }}"
        ```

    ??? variable string "`shell_editor`"

        ```yaml
        # Type: string
        shell_editor: "nano"
        ```

=== "Misc"

    ??? variable string "`shell_misc_argcomplete_pip_package`"

        ```yaml
        # Type: string
        shell_misc_argcomplete_pip_package: argcomplete
        ```

    ??? variable string "`shell_misc_argcomplete_command`"

        ```yaml
        # Type: string
        shell_misc_argcomplete_command: "activate-global-python-argcomplete"
        ```

=== "z (jump around)"

    ??? variable string "`shell_z_git_repo_url`"

        ```yaml
        # Type: string
        shell_z_git_repo_url: "https://github.com/rupa/z.git"
        ```

    ??? variable string "`shell_z_git_repo_dest`"

        ```yaml
        # Type: string
        shell_z_git_repo_dest: "{{ server_appdata_path }}/z"
        ```

=== "Bash"

    ??? variable string "`shell_bash_bashrc_path`"

        ```yaml
        # Type: string
        shell_bash_bashrc_path: "/home/{{ user.name }}/.bashrc"
        ```

    ??? variable string "`shell_bash_bashrc_block_content`"

        ```yaml
        # Type: string
        shell_bash_bashrc_block_content: |
          # Editor
          export EDITOR={{ shell_editor }}
          # Include Z
          . {{ shell_z_git_repo_dest }}/z.sh
          # Aliases
          alias lso="ls -alG | awk '{k=0;for(i=0;i<=8;i++)k+=((substr(\$1,i+2,1)~/[rwx]/)*2^(8-i));if(k)printf(\" %0o \",k);print}'"
          # OSC 1337 - Set current directory
          export PS1="$PS1\[\e]1337;CurrentDir="'$(pwd)\a\]'
        ```

    ??? variable string "`shell_bash_bashrc_block_custom`"

        ```yaml
        # Type: string
        shell_bash_bashrc_block_custom: ""
        ```

    ??? variable string "`shell_bash_binary_path`"

        ```yaml
        # Type: string
        shell_bash_binary_path: "/bin/bash"
        ```

=== "Zsh"

    ??? variable list "`shell_zsh_apt_packages_list`"

        ```yaml
        # Type: list
        shell_zsh_apt_packages_list:
          - zsh
        ```

    ??? variable string "`shell_zsh_omzsh_git_repo_url`"

        ```yaml
        # Type: string
        shell_zsh_omzsh_git_repo_url: https://github.com/robbyrussell/oh-my-zsh.git
        ```

    ??? variable string "`shell_zsh_omzsh_git_repo_dest`"

        ```yaml
        # Type: string
        shell_zsh_omzsh_git_repo_dest: "/home/{{ user.name }}/.oh-my-zsh"
        ```

    ??? variable string "`shell_zsh_zshrc_template_path`"

        ```yaml
        # Type: string
        shell_zsh_zshrc_template_path: "/home/{{ user.name }}/.oh-my-zsh/templates/zshrc.zsh-template"
        ```

    ??? variable string "`shell_zsh_zshrc_path`"

        ```yaml
        # Type: string
        shell_zsh_zshrc_path: "/home/{{ user.name }}/.zshrc"
        ```

    ??? variable string "`shell_zsh_zshrc_block_content1`"

        ```yaml
        # Type: string
        shell_zsh_zshrc_block_content1: |
          # Oh-my-zsh - auto update zsh without prompt
          DISABLE_UPDATE_PROMPT=true
        ```

    ??? variable string "`shell_zsh_zshrc_block_content2`"

        ```yaml
        # Type: string
        shell_zsh_zshrc_block_content2: |
          # zsh - allows commands to run with the un-expanded glob
          unsetopt nomatch
          # zsh - set TIMEFMT
          export TIMEFMT=$'
          real	%E
          user	%U
          sys	%S'
          # Editor
          export EDITOR={{ shell_editor }}
          # Include Z
          . {{ shell_z_git_repo_dest }}/z.sh
          # Aliases
          alias lso="ls -alG | awk '{k=0;for(i=0;i<=8;i++)k+=((substr(\$1,i+2,1)~/[rwx]/)*2^(8-i));if(k)printf(\" %0o \",k);print}'"
          # Load compinit and bashcompinit
          autoload -U +X compinit && compinit
          autoload -U +X bashcompinit && bashcompinit
          # OSC 1337 - Set current directory
          precmd () { echo -n "\x1b]1337;CurrentDir=$(pwd)\x07" }
        ```

    ??? variable string "`shell_zsh_zshrc_block_custom`"

        ```yaml
        # Type: string
        shell_zsh_zshrc_block_custom: ""
        ```

    ??? variable string "`shell_zsh_plugins`"

        ```yaml
        # Type: string
        shell_zsh_plugins: "(git docker docker-compose ansible)"
        ```

    ??? variable string "`shell_zsh_binary_previous_path`"

        ```yaml
        # Type: string
        shell_zsh_binary_previous_path: "/bin/zsh5"
        ```

    ??? variable string "`shell_zsh_binary_path`"

        ```yaml
        # Type: string
        shell_zsh_binary_path: "/bin/zsh"
        ```

=== "Oh My Posh"

    ??? variable bool "`shell_ohmyposh_enabled`"

        ```yaml
        # Type: bool (true/false)
        shell_ohmyposh_enabled: false
        ```

    ??? variable string "`shell_ohmyposh_config`"

        ```yaml
        # Takes a file path or url to a config file
        # Type: string
        shell_ohmyposh_config: ""
        ```

    ??? variable string "`shell_zsh_zshrc_oh_my_posh`"

        ```yaml
        # Type: string
        shell_zsh_zshrc_oh_my_posh: |
          # Oh My Posh
          eval "$(oh-my-posh init zsh{{ ' --config ' + shell_ohmyposh_config if shell_ohmyposh_config | length > 0 else '' }})"
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
