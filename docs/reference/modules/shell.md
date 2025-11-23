---
icon: material/cogs
status: WIP
---

# Shell

## Overview

Installs and configures a user's shell (Bash or Zsh) with tools like z for directory jumping, argcomplete for tab completion, Oh My Zsh and optional Oh My Posh theming.

---

## Deployment

Saltbox dependency.

```shell
sb install shell
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    shell_type: "custom_value"
    ```

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

=== "Global Override Options"

    ??? variable bool "`shell_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        shell_role_autoheal_enabled: true
        ```

    ??? variable string "`shell_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        shell_role_depends_on: ""
        ```

    ??? variable string "`shell_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        shell_role_depends_on_delay: "0"
        ```

    ??? variable string "`shell_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        shell_role_depends_on_healthchecks:
        ```

    ??? variable bool "`shell_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        shell_role_diun_enabled: true
        ```

    ??? variable bool "`shell_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        shell_role_dns_enabled: true
        ```

    ??? variable bool "`shell_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        shell_role_docker_controller: true
        ```

    ??? variable bool "`shell_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        shell_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`shell_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        shell_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`shell_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        shell_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`shell_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        shell_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`shell_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        shell_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`shell_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        shell_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`shell_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        shell_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`shell_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        shell_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`shell_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        shell_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`shell_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        shell_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            shell_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "shell2.{{ user.domain }}"
              - "shell.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`shell_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        shell_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            shell_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'shell2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`shell_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        shell_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->