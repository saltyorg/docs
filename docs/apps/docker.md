---
icon: material/server-network-outline
status: wip
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
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
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
        # Supported formats:
        # "28"      - Major version (installs latest 28.x.x, auto-updates within 28.x)
        # "28.5"    - Major.minor version (installs latest 28.5.x, auto-updates within 28.5.x)
        # "28.5.2"  - Exact version (installs exactly 28.5.2, no auto-updates)
        # Type: string
        docker_version: "28"
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
        docker_ce_package: "docker-ce={{ docker_ce_resolved_version }}"
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
        docker_ce_cli_package: "docker-ce-cli={{ docker_ce_cli_resolved_version }}"
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

    ??? variable bool "`put_docker_dpkg_into_hold`"

        ```yaml
        # Misc
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

    ??? variable string "`docker_controller_binary_path`"

        ```yaml
        # Type: string
        docker_controller_binary_path: "/usr/local/bin/sdc"
        ```

    ??? variable string "`docker_controller_releases_url`"

        ```yaml
        # Type: string
        docker_controller_releases_url: "{{ svm }}https://api.github.com/repos/saltyorg/sdc/releases/latest"
        ```

    ??? variable string "`docker_controller_releases_download_url`"

        ```yaml
        # Type: string
        docker_controller_releases_download_url: https://github.com/saltyorg/sdc/releases/download
        ```

    ??? variable string "`docker_controller_release_lookup_command`"

        ```yaml
        # Type: string
        docker_controller_release_lookup_command: |
          curl -s {{ docker_controller_releases_url }} \
            | jq -r ".assets[] | select(.name == \"sdc_linux_amd64\") \
            | .browser_download_url"
        ```

    ??? variable string "`docker_controller_venv_path`"

        ```yaml
        # Legacy
        # Type: string
        docker_controller_venv_path: "/srv/docker-controller/venv"
        ```

=== "Docker DNS"

    ??? variable string "`docker_dns_binary_path`"

        ```yaml
        # Type: string
        docker_dns_binary_path: "/usr/local/bin/sdhm"
        ```

    ??? variable string "`docker_dns_releases_url`"

        ```yaml
        # Type: string
        docker_dns_releases_url: "{{ svm }}https://api.github.com/repos/saltyorg/sdhm/releases/latest"
        ```

    ??? variable string "`docker_dns_releases_download_url`"

        ```yaml
        # Type: string
        docker_dns_releases_download_url: https://github.com/saltyorg/sdhm/releases/download
        ```

    ??? variable string "`docker_dns_release_lookup_command`"

        ```yaml
        # Type: string
        docker_dns_release_lookup_command: |
          curl -s {{ docker_dns_releases_url }} \
            | jq -r ".assets[] | select(.name == \"sdhm_linux_amd64\") \
            | .browser_download_url"
        ```

    ??? variable string "`docker_dns_ports_8090`"

        ```yaml
        # Type: string
        docker_dns_ports_8090: "{{ port_lookup_8090.meta.port
                                if (port_lookup_8090.meta.port is defined) and (port_lookup_8090.meta.port | trim | length > 0)
                                else '8090' }}"
        ```

    ??? variable list "`docker_dns_networks`"

        ```yaml
        # Type: list
        docker_dns_networks:
          - "saltbox"
        ```

    ??? variable string "`docker_dns_periodic_validation`"

        ```yaml
        # Type: string
        docker_dns_periodic_validation: "5m"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`docker_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        docker_role_docker_blkio_weight:
        ```

    ??? variable int "`docker_role_docker_cpu_period`"

        ```yaml
        # Type: int
        docker_role_docker_cpu_period:
        ```

    ??? variable int "`docker_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        docker_role_docker_cpu_quota:
        ```

    ??? variable int "`docker_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        docker_role_docker_cpu_shares:
        ```

    ??? variable string "`docker_role_docker_cpus`"

        ```yaml
        # Type: string
        docker_role_docker_cpus:
        ```

    ??? variable string "`docker_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        docker_role_docker_cpuset_cpus:
        ```

    ??? variable string "`docker_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        docker_role_docker_cpuset_mems:
        ```

    ??? variable string "`docker_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        docker_role_docker_kernel_memory:
        ```

    ??? variable string "`docker_role_docker_memory`"

        ```yaml
        # Type: string
        docker_role_docker_memory:
        ```

    ??? variable string "`docker_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        docker_role_docker_memory_reservation:
        ```

    ??? variable string "`docker_role_docker_memory_swap`"

        ```yaml
        # Type: string
        docker_role_docker_memory_swap:
        ```

    ??? variable int "`docker_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        docker_role_docker_memory_swappiness:
        ```

    ??? variable string "`docker_role_docker_shm_size`"

        ```yaml
        # Type: string
        docker_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`docker_role_docker_cap_drop`"

        ```yaml
        # Type: list
        docker_role_docker_cap_drop:
        ```

    ??? variable string "`docker_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        docker_role_docker_cgroupns_mode:
        ```

    ??? variable list "`docker_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        docker_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`docker_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        docker_role_docker_device_read_bps:
        ```

    ??? variable list "`docker_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        docker_role_docker_device_read_iops:
        ```

    ??? variable list "`docker_role_docker_device_requests`"

        ```yaml
        # Type: list
        docker_role_docker_device_requests:
        ```

    ??? variable list "`docker_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        docker_role_docker_device_write_bps:
        ```

    ??? variable list "`docker_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        docker_role_docker_device_write_iops:
        ```

    ??? variable list "`docker_role_docker_devices`"

        ```yaml
        # Type: list
        docker_role_docker_devices:
        ```

    ??? variable string "`docker_role_docker_devices_default`"

        ```yaml
        # Type: string
        docker_role_docker_devices_default:
        ```

    ??? variable list "`docker_role_docker_groups`"

        ```yaml
        # Type: list
        docker_role_docker_groups:
        ```

    ??? variable bool "`docker_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_privileged:
        ```

    ??? variable list "`docker_role_docker_security_opts`"

        ```yaml
        # Type: list
        docker_role_docker_security_opts:
        ```

    ??? variable string "`docker_role_docker_user`"

        ```yaml
        # Type: string
        docker_role_docker_user:
        ```

    ??? variable string "`docker_role_docker_userns_mode`"

        ```yaml
        # Type: string
        docker_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`docker_role_docker_dns_opts`"

        ```yaml
        # Type: list
        docker_role_docker_dns_opts:
        ```

    ??? variable list "`docker_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        docker_role_docker_dns_search_domains:
        ```

    ??? variable list "`docker_role_docker_dns_servers`"

        ```yaml
        # Type: list
        docker_role_docker_dns_servers:
        ```

    ??? variable string "`docker_role_docker_domainname`"

        ```yaml
        # Type: string
        docker_role_docker_domainname:
        ```

    ??? variable list "`docker_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        docker_role_docker_exposed_ports:
        ```

    ??? variable string "`docker_role_docker_hostname`"

        ```yaml
        # Type: string
        docker_role_docker_hostname:
        ```

    ??? variable dict "`docker_role_docker_hosts`"

        ```yaml
        # Type: dict
        docker_role_docker_hosts:
        ```

    ??? variable bool "`docker_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_hosts_use_common:
        ```

    ??? variable string "`docker_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        docker_role_docker_ipc_mode:
        ```

    ??? variable list "`docker_role_docker_links`"

        ```yaml
        # Type: list
        docker_role_docker_links:
        ```

    ??? variable string "`docker_role_docker_network_mode`"

        ```yaml
        # Type: string
        docker_role_docker_network_mode:
        ```

    ??? variable list "`docker_role_docker_networks`"

        ```yaml
        # Type: list
        docker_role_docker_networks:
        ```

    ??? variable string "`docker_role_docker_pid_mode`"

        ```yaml
        # Type: string
        docker_role_docker_pid_mode:
        ```

    ??? variable list "`docker_role_docker_ports`"

        ```yaml
        # Type: list
        docker_role_docker_ports:
        ```

    ??? variable string "`docker_role_docker_uts`"

        ```yaml
        # Type: string
        docker_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`docker_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_keep_volumes:
        ```

    ??? variable list "`docker_role_docker_mounts`"

        ```yaml
        # Type: list
        docker_role_docker_mounts:
        ```

    ??? variable dict "`docker_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        docker_role_docker_storage_opts:
        ```

    ??? variable list "`docker_role_docker_tmpfs`"

        ```yaml
        # Type: list
        docker_role_docker_tmpfs:
        ```

    ??? variable string "`docker_role_docker_volume_driver`"

        ```yaml
        # Type: string
        docker_role_docker_volume_driver:
        ```

    ??? variable list "`docker_role_docker_volumes`"

        ```yaml
        # Type: list
        docker_role_docker_volumes:
        ```

    ??? variable list "`docker_role_docker_volumes_from`"

        ```yaml
        # Type: list
        docker_role_docker_volumes_from:
        ```

    ??? variable bool "`docker_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_volumes_global:
        ```

    ??? variable string "`docker_role_docker_working_dir`"

        ```yaml
        # Type: string
        docker_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`docker_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_auto_remove:
        ```

    ??? variable bool "`docker_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_cleanup:
        ```

    ??? variable string "`docker_role_docker_force_kill`"

        ```yaml
        # Type: string
        docker_role_docker_force_kill:
        ```

    ??? variable dict "`docker_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        docker_role_docker_healthcheck:
        ```

    ??? variable int "`docker_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        docker_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`docker_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_init:
        ```

    ??? variable string "`docker_role_docker_kill_signal`"

        ```yaml
        # Type: string
        docker_role_docker_kill_signal:
        ```

    ??? variable string "`docker_role_docker_log_driver`"

        ```yaml
        # Type: string
        docker_role_docker_log_driver:
        ```

    ??? variable dict "`docker_role_docker_log_options`"

        ```yaml
        # Type: dict
        docker_role_docker_log_options:
        ```

    ??? variable bool "`docker_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_oom_killer:
        ```

    ??? variable int "`docker_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        docker_role_docker_oom_score_adj:
        ```

    ??? variable bool "`docker_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_output_logs:
        ```

    ??? variable bool "`docker_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_paused:
        ```

    ??? variable bool "`docker_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_recreate:
        ```

    ??? variable string "`docker_role_docker_restart_policy`"

        ```yaml
        # Type: string
        docker_role_docker_restart_policy:
        ```

    ??? variable int "`docker_role_docker_restart_retries`"

        ```yaml
        # Type: int
        docker_role_docker_restart_retries:
        ```

    ??? variable int "`docker_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        docker_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`docker_role_docker_capabilities`"

        ```yaml
        # Type: list
        docker_role_docker_capabilities:
        ```

    ??? variable string "`docker_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        docker_role_docker_cgroup_parent:
        ```

    ??? variable list "`docker_role_docker_commands`"

        ```yaml
        # Type: list
        docker_role_docker_commands:
        ```

    ??? variable string "`docker_role_docker_container`"

        ```yaml
        # Type: string
        docker_role_docker_container:
        ```

    ??? variable int "`docker_role_docker_create_timeout`"

        ```yaml
        # Type: int
        docker_role_docker_create_timeout:
        ```

    ??? variable string "`docker_role_docker_entrypoint`"

        ```yaml
        # Type: string
        docker_role_docker_entrypoint:
        ```

    ??? variable string "`docker_role_docker_env_file`"

        ```yaml
        # Type: string
        docker_role_docker_env_file:
        ```

    ??? variable dict "`docker_role_docker_envs`"

        ```yaml
        # Type: dict
        docker_role_docker_envs:
        ```

    ??? variable string "`docker_role_docker_image`"

        ```yaml
        # Type: string
        docker_role_docker_image:
        ```

    ??? variable bool "`docker_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_image_pull:
        ```

    ??? variable dict "`docker_role_docker_labels`"

        ```yaml
        # Type: dict
        docker_role_docker_labels:
        ```

    ??? variable bool "`docker_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_labels_use_common:
        ```

    ??? variable bool "`docker_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_read_only:
        ```

    ??? variable string "`docker_role_docker_runtime`"

        ```yaml
        # Type: string
        docker_role_docker_runtime:
        ```

    ??? variable list "`docker_role_docker_sysctls`"

        ```yaml
        # Type: list
        docker_role_docker_sysctls:
        ```

    ??? variable list "`docker_role_docker_ulimits`"

        ```yaml
        # Type: list
        docker_role_docker_ulimits:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->