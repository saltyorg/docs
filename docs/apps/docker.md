---
icon: material/server-network-outline
status: WIP
---

# Docker

## Overview

Saltbox dependency.

Docker is an open-source platform that enables developers to build, ship, and run applications using containers.

---

## Deployment

```sh
sb install docker
```

## Usage

```sh
docker
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    docker_dns: ["item1", "item2"]
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `docker_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `docker_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Settings"

    ??? variable list "`docker_dns`"

        ```yaml
        # Format is ["8.8.8.8", "8.8.4.4"]
        # Type: list
        docker_dns: []
        ```

    ??? variable dict "`docker_config_custom`"

        ```yaml
        # YAML Dictionary that gets combined with the defaults and later converted to json
        # Example of how to remove an option:
        # docker_config_custom:
        # log-opts: "{{ omit }}"
        # Example of how to add options:
        # docker_config_custom:
        # debug: "true"
        # Type: dict
        docker_config_custom: {}
        ```

    ??? variable string "`docker_cpus_default`"

        ```yaml
        # CPU and Memory defaults
        # Type: string
        docker_cpus_default: ""
        ```

    ??? variable string "`docker_memory_default`"

        ```yaml
        # Type: string
        docker_memory_default: ""
        ```

    ??? variable string "`docker_skip_start_during_meta_tag`"

        ```yaml
        # Skip Container startup during core, saltbox, mediabox or feederbox
        # If the kernel has been updated and a reboot will happen
        # Type: string
        docker_skip_start_during_meta_tag: "{{ saltbox_auto_reboot }}"
        ```

    ??? variable bool "`docker_create_image_prune`"

        ```yaml
        # Toggles pruning of dangling images after container creation.
        # Type: bool (true/false)
        docker_create_image_prune: true
        ```

    ??? variable bool "`docker_create_image_prune_delay`"

        ```yaml
        # Type: bool (true/false)
        docker_create_image_prune_delay: true
        ```

    ??? variable int "`docker_create_image_prune_delay_timeout`"

        ```yaml
        # Type: int
        docker_create_image_prune_delay_timeout: 10
        ```

=== "Lookup"

    ??? variable string "`docker_start_containers_check`"

        ```yaml
        # Type: string
        docker_start_containers_check: "{{ true if (('docker' in ansible_run_tags) or (not docker_skip_start_during_meta_tag)) else (not docker_reboot_required_file.stat.exists) }}"
        ```

=== "Docker APT Key"

    ??? variable string "`docker_apt_key_id`"

        ```yaml
        # Type: string
        docker_apt_key_id: 0EBFCD88
        ```

    ??? variable string "`docker_apt_key_url`"

        ```yaml
        # Type: string
        docker_apt_key_url: https://download.docker.com/linux/ubuntu/gpg
        ```

=== "Docker APT Repository"

    ??? variable string "`docker_apt_repo_version`"

        ```yaml
        # Type: string
        docker_apt_repo_version: stable
        ```

    ??? variable string "`docker_apt_repo_url`"

        ```yaml
        # Type: string
        docker_apt_repo_url: "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/{{ ansible_facts['distribution'] | lower }} {{ ansible_facts['distribution_release'] | lower }} {{ docker_apt_repo_version }}"  # noqa line-length
        ```

    ??? variable string "`docker_apt_repo_filename`"

        ```yaml
        # Type: string
        docker_apt_repo_filename: docker
        ```

=== "Docker APT Package"

    ??? variable string "`docker_version`"

        ```yaml
        # Version
        # Type: string
        docker_version: "latest"
        ```

    ??? variable string "`docker_ce_name`"

        ```yaml
        # Docker CE
        # Type: string
        docker_ce_name: "Docker CE"
        ```

    ??? variable string "`docker_ce_package`"

        ```yaml
        # Type: string
        docker_ce_package: "{{ 'docker-ce'
                            if (docker_version is defined and docker_version | lower == 'latest')
                            else 'docker-ce=*' + docker_version + '*~' + ansible_facts['distribution'] | lower + '.' + ansible_facts['distribution_version'] + '~' + ansible_facts['distribution_release'] | lower }}"
        ```

    ??? variable string "`docker_ce_filepath`"

        ```yaml
        # Type: string
        docker_ce_filepath: "/usr/bin/dockerd"
        ```

    ??? variable string "`docker_ce_dpkg`"

        ```yaml
        # Type: string
        docker_ce_dpkg: "docker-ce"
        ```

    ??? variable string "`docker_ce_cli_name`"

        ```yaml
        # Docker CE CLI
        # Type: string
        docker_ce_cli_name: "Docker CE CLI"
        ```

    ??? variable string "`docker_ce_cli_package`"

        ```yaml
        # Type: string
        docker_ce_cli_package: "{{ 'docker-ce-cli'
                                if (docker_version is defined and docker_version | lower == 'latest')
                                else 'docker-ce-cli=*' + docker_version + '*~' + ansible_facts['distribution'] | lower + '.' + ansible_facts['distribution_version'] + '~' + ansible_facts['distribution_release'] | lower }}"
        ```

    ??? variable string "`docker_ce_cli_filepath`"

        ```yaml
        # Type: string
        docker_ce_cli_filepath: "/usr/bin/docker"
        ```

    ??? variable string "`docker_ce_cli_dpkg`"

        ```yaml
        # Type: string
        docker_ce_cli_dpkg: "docker-ce-cli"
        ```

    ??? variable string "`containerd_io_name`"

        ```yaml
        # Containerd
        # Type: string
        containerd_io_name: "Containerd"
        ```

    ??? variable string "`containerd_io_package`"

        ```yaml
        # Type: string
        containerd_io_package: "containerd.io"
        ```

    ??? variable string "`containerd_io_filepath`"

        ```yaml
        # Type: string
        containerd_io_filepath: "/usr/bin/containerd"
        ```

    ??? variable string "`containerd_io_dpkg`"

        ```yaml
        # Type: string
        containerd_io_dpkg: "containerd.io"
        ```

    ??? variable string "`compose_cli_name`"

        ```yaml
        # Docker Compose
        # Type: string
        compose_cli_name: "Docker Compose"
        ```

    ??? variable string "`compose_cli_package`"

        ```yaml
        # Type: string
        compose_cli_package: "docker-compose-plugin"
        ```

    ??? variable string "`compose_cli_filepath`"

        ```yaml
        # Type: string
        compose_cli_filepath: "docker compose"
        ```

    ??? variable string "`compose_cli_dpkg`"

        ```yaml
        # Type: string
        compose_cli_dpkg: "docker-compose-plugin"
        ```

    ??? variable string "`docker_rootless_name`"

        ```yaml
        # Docker Rootless Extras
        # Type: string
        docker_rootless_name: "Docker Rootless Extras"
        ```

    ??? variable string "`docker_rootless_package`"

        ```yaml
        # Type: string
        docker_rootless_package: "docker-ce-rootless-extras"
        ```

    ??? variable string "`docker_rootless_filepath`"

        ```yaml
        # Type: string
        docker_rootless_filepath: "/usr/bin/rootlesskit"
        ```

    ??? variable string "`docker_rootless_dpkg`"

        ```yaml
        # Type: string
        docker_rootless_dpkg: "docker-ce-rootless-extras"
        ```

    ??? variable string "`docker_package_state`"

        ```yaml
        # Misc
        # Type: string
        docker_package_state: "{{ 'latest'
                               if (docker_version is defined and docker_version | lower == 'latest')
                               else 'present' }}"
        ```

    ??? variable bool "`put_docker_dpkg_into_hold`"

        ```yaml
        # Type: bool (true/false)
        put_docker_dpkg_into_hold: true
        ```

    ??? variable string "`docker_filesystem_path`"

        ```yaml
        # Type: string
        docker_filesystem_path: "/media/docker-volume.img"
        ```

    ??? variable string "`docker_filesystem_size`"

        ```yaml
        # Type: string
        docker_filesystem_size: "20G"
        ```

    ??? variable string "`docker_ipv6`"

        ```yaml
        # Type: string
        docker_ipv6: "{{ dns_ipv6_enabled }}"
        ```

    ??? variable string "`docker_service_after`"

        ```yaml
        # Service
        # Type: string
        docker_service_after: "{{ mergerfs_service_name }}"
        ```

    ??? variable string "`docker_service_sleep`"

        ```yaml
        # Type: string
        docker_service_sleep: "{{ 0
                               if continuous_integration or (not use_remote)
                               else 120 }}"
        ```

    ??? variable bool "`docker_service_force`"

        ```yaml
        # Type: bool (true/false)
        docker_service_force: true
        ```

    ??? variable string "`docker_service_check`"

        ```yaml
        # Type: string
        docker_service_check: "{{ docker_binary.stat.exists and (docker_service_running or ((remote_docker_service_running is defined) and remote_docker_service_running) or ((unionfs_docker_service_running is defined) and unionfs_docker_service_running)) }}"
        ```

    ??? variable string "`docker_service_check_mounts`"

        ```yaml
        # Type: string
        docker_service_check_mounts: "{{ docker_binary.stat.exists and (((remote_docker_service_running is defined) and remote_docker_service_running) or ((unionfs_docker_service_running is defined) and unionfs_docker_service_running)) }}"
        ```

    ??? variable string "`docker_update_hosts_service_runtime_max`"

        ```yaml
        # Type: string
        docker_update_hosts_service_runtime_max: "3600s"
        ```

    ??? variable string "`docker_daemon_storage_driver`"

        ```yaml
        # Type: string
        docker_daemon_storage_driver: "{{ ('zfs' in var_lib_file_system.stdout) | ternary('zfs', 'overlay2') }}"
        ```

    ??? variable bool "`docker_daemon_template_force`"

        ```yaml
        # Type: bool (true/false)
        docker_daemon_template_force: true
        ```

=== "Docker Compose"

    ??? variable string "`compose_cleanup_switch`"

        ```yaml
        # Type: string
        compose_cleanup_switch: "{{ compose_install_switch | default(true) }}"
        ```

=== "Docker Controller"

    ??? variable string "`docker_controller_python_version`"

        ```yaml
        # Type: string
        docker_controller_python_version: "3.10"
        ```

    ??? variable string "`docker_controller_venv_path`"

        ```yaml
        # Type: string
        docker_controller_venv_path: "/srv/docker-controller/venv"
        ```

=== "Docker DNS"

    ??? variable string "`docker_dns_python_version`"

        ```yaml
        # Type: string
        docker_dns_python_version: "3.10"
        ```

=== "Global Override Options"

    ??? variable bool "`docker_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        docker_role_autoheal_enabled: true
        ```

    ??? variable string "`docker_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        docker_role_depends_on: ""
        ```

    ??? variable string "`docker_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        docker_role_depends_on_delay: "0"
        ```

    ??? variable string "`docker_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        docker_role_depends_on_healthchecks:
        ```

    ??? variable bool "`docker_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        docker_role_diun_enabled: true
        ```

    ??? variable bool "`docker_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        docker_role_dns_enabled: true
        ```

    ??? variable bool "`docker_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        docker_role_docker_controller: true
        ```

    ??? variable bool "`docker_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        docker_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`docker_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        docker_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`docker_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        docker_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`docker_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        docker_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`docker_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        docker_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`docker_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        docker_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`docker_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        docker_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`docker_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        docker_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`docker_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        docker_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`docker_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        docker_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            docker_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "docker2.{{ user.domain }}"
              - "docker.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`docker_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        docker_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            docker_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'docker2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`docker_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        docker_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->