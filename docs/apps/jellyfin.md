---
hide:
  - tags
tags:
  - jellyfin
---

# Jellyfin

## What is it?

[Jellyfin](https://jellyfin.org/) is the volunteer-built media solution that puts you in control of your media. Stream to any device from your own server, with no strings attached. Your media, your server, your way.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://jellyfin.org/){: .header-icons } | [:octicons-link-16: Docs](https://docs.jellyfin.org/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jellyfin/jellyfin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/jellyfin){: .header-icons }|

### 1. Installation

``` shell

sb install jellyfin

```

### 2. URL

- To access Jellyfin, visit `https://jellyfin.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `jellyfin_instances`.

    === "Role-level Override"

        Applies to all instances of jellyfin:

        ```yaml
        jellyfin_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `jellyfin2`):

        ```yaml
        jellyfin2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `jellyfin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jellyfin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        jellyfin_instances: ["jellyfin"]

        ```

    === "Example"

        ```yaml
        # Type: list
        jellyfin_instances: ["jellyfin", "jellyfin2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        jellyfin_role_paths_folder: "{{ jellyfin_name }}"

        # Type: string
        jellyfin_role_paths_location: "{{ server_appdata_path }}/{{ jellyfin_role_paths_folder }}"

        # Type: string
        jellyfin_role_paths_transcodes_location: "{{ transcodes_path }}/{{ jellyfin_role_paths_folder }}"

        # Type: string
        jellyfin_role_paths_dlna_location: "{{ jellyfin_role_paths_location }}/dlna.xml"

        # Type: string
        jellyfin_role_paths_sys_xml_location: "{{ jellyfin_role_paths_location }}/system.xml"

        # Type: string
        jellyfin_role_paths_net_xml_location: "{{ jellyfin_role_paths_location }}/network.xml"

        # Type: string
        jellyfin_role_paths_xml_location_old: "{{ jellyfin_role_paths_location }}/app/config/system.xml"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyfin2_paths_folder: "{{ jellyfin_name }}"

        # Type: string
        jellyfin2_paths_location: "{{ server_appdata_path }}/{{ jellyfin_role_paths_folder }}"

        # Type: string
        jellyfin2_paths_transcodes_location: "{{ transcodes_path }}/{{ jellyfin_role_paths_folder }}"

        # Type: string
        jellyfin2_paths_dlna_location: "{{ jellyfin_role_paths_location }}/dlna.xml"

        # Type: string
        jellyfin2_paths_sys_xml_location: "{{ jellyfin_role_paths_location }}/system.xml"

        # Type: string
        jellyfin2_paths_net_xml_location: "{{ jellyfin_role_paths_location }}/network.xml"

        # Type: string
        jellyfin2_paths_xml_location_old: "{{ jellyfin_role_paths_location }}/app/config/system.xml"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        jellyfin_role_web_subdomain: "{{ jellyfin_name }}"

        # Type: string
        jellyfin_role_web_domain: "{{ user.domain }}"

        # Type: string
        jellyfin_role_web_port: "8096"

        # Type: string
        jellyfin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyfin') + '.' + lookup('role_var', '_web_domain', role='jellyfin')
                                if (lookup('role_var', '_web_subdomain', role='jellyfin') | length > 0)
                                else lookup('role_var', '_web_domain', role='jellyfin')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyfin2_web_subdomain: "{{ jellyfin_name }}"

        # Type: string
        jellyfin2_web_domain: "{{ user.domain }}"

        # Type: string
        jellyfin2_web_port: "8096"

        # Type: string
        jellyfin2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyfin') + '.' + lookup('role_var', '_web_domain', role='jellyfin')
                            if (lookup('role_var', '_web_subdomain', role='jellyfin') | length > 0)
                            else lookup('role_var', '_web_domain', role='jellyfin')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        jellyfin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyfin') }}"

        # Type: string
        jellyfin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyfin') }}"

        # Type: bool (true/false)
        jellyfin_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyfin2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyfin') }}"

        # Type: string
        jellyfin2_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyfin') }}"

        # Type: bool (true/false)
        jellyfin2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        jellyfin_role_traefik_sso_middleware: ""

        # Type: string
        jellyfin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        jellyfin_role_traefik_middleware_custom: ""

        # Type: string
        jellyfin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        jellyfin_role_traefik_enabled: true

        # Type: bool (true/false)
        jellyfin_role_traefik_api_enabled: false

        # Type: string
        jellyfin_role_traefik_api_endpoint: ""

        # Type: bool (true/false)
        jellyfin_role_traefik_gzip_enabled: false

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyfin2_traefik_sso_middleware: ""

        # Type: string
        jellyfin2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        jellyfin2_traefik_middleware_custom: ""

        # Type: string
        jellyfin2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        jellyfin2_traefik_enabled: true

        # Type: bool (true/false)
        jellyfin2_traefik_api_enabled: false

        # Type: string
        jellyfin2_traefik_api_endpoint: ""

        # Type: bool (true/false)
        jellyfin2_traefik_gzip_enabled: false

        ```

??? example "Config"

    === "Role-level"

        ```yaml
        # System
        # Type: list
        jellyfin_role_system_settings_default: 
          - { xpath: 'PublicPort', value: '80' }
          - { xpath: 'PublicHttpsPort', value: '443' }
          - { xpath: 'EnableFolderView', value: 'true' }
          - { xpath: 'QuickConnectAvailable', value: 'true' }
          - { xpath: 'EnableRemoteAccess', value: 'true' }
          - { xpath: 'ServerName', value: 'saltbox' }

        # Type: list
        jellyfin_role_system_settings_custom: []

        # Type: string
        jellyfin_role_system_settings_list: "{{ lookup('role_var', '_system_settings_default', role='jellyfin') + lookup('role_var', '_system_settings_custom', role='jellyfin') }}"

        # Network
        # Type: list
        jellyfin_role_network_settings_default: 
          - { xpath: 'PublicPort', value: '80' }
          - { xpath: 'PublicHttpsPort', value: '443' }
          - { xpath: 'PublishedServerUriBySubnet/string', value: 'external={{ lookup("role_var", "_web_url", role="jellyfin") }}:443' }

        # Type: list
        jellyfin_role_network_settings_custom: []

        # Type: string
        jellyfin_role_network_settings_list: "{{ lookup('role_var', '_network_settings_default', role='jellyfin') + lookup('role_var', '_network_settings_custom', role='jellyfin') }}"

        ```

    === "Instance-level"

        ```yaml
        # System
        # Type: list
        jellyfin2_system_settings_default: 
          - { xpath: 'PublicPort', value: '80' }
          - { xpath: 'PublicHttpsPort', value: '443' }
          - { xpath: 'EnableFolderView', value: 'true' }
          - { xpath: 'QuickConnectAvailable', value: 'true' }
          - { xpath: 'EnableRemoteAccess', value: 'true' }
          - { xpath: 'ServerName', value: 'saltbox' }

        # Type: list
        jellyfin2_system_settings_custom: []

        # Type: string
        jellyfin2_system_settings_list: "{{ lookup('role_var', '_system_settings_default', role='jellyfin') + lookup('role_var', '_system_settings_custom', role='jellyfin') }}"

        # Network
        # Type: list
        jellyfin2_network_settings_default: 
          - { xpath: 'PublicPort', value: '80' }
          - { xpath: 'PublicHttpsPort', value: '443' }
          - { xpath: 'PublishedServerUriBySubnet/string', value: 'external={{ lookup("role_var", "_web_url", role="jellyfin") }}:443' }

        # Type: list
        jellyfin2_network_settings_custom: []

        # Type: string
        jellyfin2_network_settings_list: "{{ lookup('role_var', '_network_settings_default', role='jellyfin') + lookup('role_var', '_network_settings_custom', role='jellyfin') }}"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        jellyfin_role_docker_container: "{{ jellyfin_name }}"

        # Image
        # Type: bool (true/false)
        jellyfin_role_docker_image_pull: true

        # Type: string
        jellyfin_role_docker_image_repo: "ghcr.io/hotio/jellyfin"

        # Type: string
        jellyfin_role_docker_image_tag: "release"

        # Type: string
        jellyfin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyfin') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyfin') }}"

        # Envs
        # Type: dict
        jellyfin_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          DOTNET_USE_POLLING_FILE_WATCHER: "1"

        # Type: dict
        jellyfin_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        jellyfin_role_docker_volumes_default: 
          - "{{ jellyfin_role_paths_location }}:/config:rw"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ jellyfin_role_paths_transcodes_location }}:/transcode"

        # Type: list
        jellyfin_role_docker_volumes_legacy: 
          - "/mnt/unionfs/Media:/data"

        # Type: list
        jellyfin_role_docker_volumes_custom: []

        # Mounts
        # Type: list
        jellyfin_role_docker_mounts_default: 
          - target: /tmp
            type: tmpfs

        # Type: list
        jellyfin_role_docker_mounts_custom: []

        # Hostname
        # Type: string
        jellyfin_role_docker_hostname: "{{ jellyfin_name }}"

        # Networks
        # Type: string
        jellyfin_role_docker_networks_alias: "{{ jellyfin_name }}"

        # Type: list
        jellyfin_role_docker_networks_default: []

        # Type: list
        jellyfin_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        jellyfin_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        jellyfin_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        jellyfin_role_docker_blkio_weight:

        # Type: int
        jellyfin_role_docker_cpu_period:

        # Type: int
        jellyfin_role_docker_cpu_quota:

        # Type: int
        jellyfin_role_docker_cpu_shares:

        # Type: string
        jellyfin_role_docker_cpus:

        # Type: string
        jellyfin_role_docker_cpuset_cpus:

        # Type: string
        jellyfin_role_docker_cpuset_mems:

        # Type: string
        jellyfin_role_docker_kernel_memory:

        # Type: string
        jellyfin_role_docker_memory:

        # Type: string
        jellyfin_role_docker_memory_reservation:

        # Type: string
        jellyfin_role_docker_memory_swap:

        # Type: int
        jellyfin_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        jellyfin_role_docker_cap_drop:

        # Type: list
        jellyfin_role_docker_device_cgroup_rules:

        # Type: list
        jellyfin_role_docker_device_read_bps:

        # Type: list
        jellyfin_role_docker_device_read_iops:

        # Type: list
        jellyfin_role_docker_device_requests:

        # Type: list
        jellyfin_role_docker_device_write_bps:

        # Type: list
        jellyfin_role_docker_device_write_iops:

        # Type: list
        jellyfin_role_docker_devices:

        # Type: string
        jellyfin_role_docker_devices_default:

        # Type: bool (true/false)
        jellyfin_role_docker_privileged:

        # Type: list
        jellyfin_role_docker_security_opts:

        # Networking
        # Type: list
        jellyfin_role_docker_dns_opts:

        # Type: list
        jellyfin_role_docker_dns_search_domains:

        # Type: list
        jellyfin_role_docker_dns_servers:

        # Type: dict
        jellyfin_role_docker_hosts:

        # Type: string
        jellyfin_role_docker_hosts_use_common:

        # Type: string
        jellyfin_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        jellyfin_role_docker_keep_volumes:

        # Type: string
        jellyfin_role_docker_volume_driver:

        # Type: list
        jellyfin_role_docker_volumes_from:

        # Type: string
        jellyfin_role_docker_volumes_global:

        # Type: string
        jellyfin_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        jellyfin_role_docker_healthcheck:

        # Type: bool (true/false)
        jellyfin_role_docker_init:

        # Type: string
        jellyfin_role_docker_log_driver:

        # Type: dict
        jellyfin_role_docker_log_options:

        # Type: bool (true/false)
        jellyfin_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        jellyfin_role_docker_auto_remove:

        # Type: list
        jellyfin_role_docker_capabilities:

        # Type: string
        jellyfin_role_docker_cgroup_parent:

        # Type: string
        jellyfin_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        jellyfin_role_docker_cleanup:

        # Type: list
        jellyfin_role_docker_commands:

        # Type: string
        jellyfin_role_docker_create_timeout:

        # Type: string
        jellyfin_role_docker_domainname:

        # Type: string
        jellyfin_role_docker_entrypoint:

        # Type: string
        jellyfin_role_docker_env_file:

        # Type: list
        jellyfin_role_docker_exposed_ports:

        # Type: string
        jellyfin_role_docker_force_kill:

        # Type: list
        jellyfin_role_docker_groups:

        # Type: int
        jellyfin_role_docker_healthy_wait_timeout:

        # Type: string
        jellyfin_role_docker_ipc_mode:

        # Type: string
        jellyfin_role_docker_kill_signal:

        # Type: dict
        jellyfin_role_docker_labels:

        # Type: string
        jellyfin_role_docker_labels_use_common:

        # Type: list
        jellyfin_role_docker_links:

        # Type: bool (true/false)
        jellyfin_role_docker_oom_killer:

        # Type: int
        jellyfin_role_docker_oom_score_adj:

        # Type: bool (true/false)
        jellyfin_role_docker_paused:

        # Type: string
        jellyfin_role_docker_pid_mode:

        # Type: list
        jellyfin_role_docker_ports:

        # Type: bool (true/false)
        jellyfin_role_docker_read_only:

        # Type: bool (true/false)
        jellyfin_role_docker_recreate:

        # Type: int
        jellyfin_role_docker_restart_retries:

        # Type: string
        jellyfin_role_docker_runtime:

        # Type: string
        jellyfin_role_docker_shm_size:

        # Type: int
        jellyfin_role_docker_stop_timeout:

        # Type: dict
        jellyfin_role_docker_storage_opts:

        # Type: list
        jellyfin_role_docker_sysctls:

        # Type: list
        jellyfin_role_docker_tmpfs:

        # Type: list
        jellyfin_role_docker_ulimits:

        # Type: string
        jellyfin_role_docker_user:

        # Type: string
        jellyfin_role_docker_userns_mode:

        # Type: string
        jellyfin_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        jellyfin2_docker_container: "{{ jellyfin_name }}"

        # Image
        # Type: bool (true/false)
        jellyfin2_docker_image_pull: true

        # Type: string
        jellyfin2_docker_image_repo: "ghcr.io/hotio/jellyfin"

        # Type: string
        jellyfin2_docker_image_tag: "release"

        # Type: string
        jellyfin2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyfin') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyfin') }}"

        # Envs
        # Type: dict
        jellyfin2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          DOTNET_USE_POLLING_FILE_WATCHER: "1"

        # Type: dict
        jellyfin2_docker_envs_custom: {}

        # Volumes
        # Type: list
        jellyfin2_docker_volumes_default: 
          - "{{ jellyfin_role_paths_location }}:/config:rw"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ jellyfin_role_paths_transcodes_location }}:/transcode"

        # Type: list
        jellyfin2_docker_volumes_legacy: 
          - "/mnt/unionfs/Media:/data"

        # Type: list
        jellyfin2_docker_volumes_custom: []

        # Mounts
        # Type: list
        jellyfin2_docker_mounts_default: 
          - target: /tmp
            type: tmpfs

        # Type: list
        jellyfin2_docker_mounts_custom: []

        # Hostname
        # Type: string
        jellyfin2_docker_hostname: "{{ jellyfin_name }}"

        # Networks
        # Type: string
        jellyfin2_docker_networks_alias: "{{ jellyfin_name }}"

        # Type: list
        jellyfin2_docker_networks_default: []

        # Type: list
        jellyfin2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        jellyfin2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        jellyfin2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        jellyfin2_docker_blkio_weight:
        # Type: int
        jellyfin2_docker_cpu_period:
        # Type: int
        jellyfin2_docker_cpu_quota:
        # Type: int
        jellyfin2_docker_cpu_shares:
        # Type: string
        jellyfin2_docker_cpus:
        # Type: string
        jellyfin2_docker_cpuset_cpus:
        # Type: string
        jellyfin2_docker_cpuset_mems:
        # Type: string
        jellyfin2_docker_kernel_memory:
        # Type: string
        jellyfin2_docker_memory:
        # Type: string
        jellyfin2_docker_memory_reservation:
        # Type: string
        jellyfin2_docker_memory_swap:
        # Type: int
        jellyfin2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        jellyfin2_docker_cap_drop:
        # Type: list
        jellyfin2_docker_device_cgroup_rules:
        # Type: list
        jellyfin2_docker_device_read_bps:
        # Type: list
        jellyfin2_docker_device_read_iops:
        # Type: list
        jellyfin2_docker_device_requests:
        # Type: list
        jellyfin2_docker_device_write_bps:
        # Type: list
        jellyfin2_docker_device_write_iops:
        # Type: list
        jellyfin2_docker_devices:
        # Type: string
        jellyfin2_docker_devices_default:
        # Type: bool (true/false)
        jellyfin2_docker_privileged:
        # Type: list
        jellyfin2_docker_security_opts:

        # Networking
        # Type: list
        jellyfin2_docker_dns_opts:
        # Type: list
        jellyfin2_docker_dns_search_domains:
        # Type: list
        jellyfin2_docker_dns_servers:
        # Type: dict
        jellyfin2_docker_hosts:
        # Type: string
        jellyfin2_docker_hosts_use_common:
        # Type: string
        jellyfin2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        jellyfin2_docker_keep_volumes:
        # Type: string
        jellyfin2_docker_volume_driver:
        # Type: list
        jellyfin2_docker_volumes_from:
        # Type: string
        jellyfin2_docker_volumes_global:
        # Type: string
        jellyfin2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        jellyfin2_docker_healthcheck:
        # Type: bool (true/false)
        jellyfin2_docker_init:
        # Type: string
        jellyfin2_docker_log_driver:
        # Type: dict
        jellyfin2_docker_log_options:
        # Type: bool (true/false)
        jellyfin2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        jellyfin2_docker_auto_remove:
        # Type: list
        jellyfin2_docker_capabilities:
        # Type: string
        jellyfin2_docker_cgroup_parent:
        # Type: string
        jellyfin2_docker_cgroupns_mode:
        # Type: bool (true/false)
        jellyfin2_docker_cleanup:
        # Type: list
        jellyfin2_docker_commands:
        # Type: string
        jellyfin2_docker_create_timeout:
        # Type: string
        jellyfin2_docker_domainname:
        # Type: string
        jellyfin2_docker_entrypoint:
        # Type: string
        jellyfin2_docker_env_file:
        # Type: list
        jellyfin2_docker_exposed_ports:
        # Type: string
        jellyfin2_docker_force_kill:
        # Type: list
        jellyfin2_docker_groups:
        # Type: int
        jellyfin2_docker_healthy_wait_timeout:
        # Type: string
        jellyfin2_docker_ipc_mode:
        # Type: string
        jellyfin2_docker_kill_signal:
        # Type: dict
        jellyfin2_docker_labels:
        # Type: string
        jellyfin2_docker_labels_use_common:
        # Type: list
        jellyfin2_docker_links:
        # Type: bool (true/false)
        jellyfin2_docker_oom_killer:
        # Type: int
        jellyfin2_docker_oom_score_adj:
        # Type: bool (true/false)
        jellyfin2_docker_paused:
        # Type: string
        jellyfin2_docker_pid_mode:
        # Type: list
        jellyfin2_docker_ports:
        # Type: bool (true/false)
        jellyfin2_docker_read_only:
        # Type: bool (true/false)
        jellyfin2_docker_recreate:
        # Type: int
        jellyfin2_docker_restart_retries:
        # Type: string
        jellyfin2_docker_runtime:
        # Type: string
        jellyfin2_docker_shm_size:
        # Type: int
        jellyfin2_docker_stop_timeout:
        # Type: dict
        jellyfin2_docker_storage_opts:
        # Type: list
        jellyfin2_docker_sysctls:
        # Type: list
        jellyfin2_docker_tmpfs:
        # Type: list
        jellyfin2_docker_ulimits:
        # Type: string
        jellyfin2_docker_user:
        # Type: string
        jellyfin2_docker_userns_mode:
        # Type: string
        jellyfin2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        jellyfin_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        jellyfin_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        jellyfin_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jellyfin_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        jellyfin_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        jellyfin_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        jellyfin_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        jellyfin_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        jellyfin_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        jellyfin_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        jellyfin_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        jellyfin_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        jellyfin_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        jellyfin_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        jellyfin_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        jellyfin_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        jellyfin_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            jellyfin_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellyfin2.{{ user.domain }}"
              - "jellyfin.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            jellyfin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyfin2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `jellyfin2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jellyfin2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        jellyfin2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        jellyfin2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jellyfin2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jellyfin2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jellyfin2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jellyfin2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jellyfin2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jellyfin2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jellyfin2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jellyfin2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jellyfin2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jellyfin2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jellyfin2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jellyfin2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        jellyfin2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jellyfin2_web_scheme:

        ```

        1.  Example:

            ```yaml
            jellyfin2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellyfin2.{{ user.domain }}"
              - "jellyfin.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            jellyfin2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyfin2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
