---
hide:
  - tags
tags:
  - deluge
---

# Deluge

## What is it?

[Deluge](https://deluge-torrent.org/) is a torrent client that can be used as an alternative to qbittorrent.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://deluge-torrent.org/){: .header-icons } | [:octicons-link-16: Docs](https://dev.deluge-torrent.org/wiki/UserGuide){: .header-icons } | [:octicons-mark-github-16: Github](https://git.deluge-torrent.org/deluge){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/linuxserver/deluge){: .header-icons }|

### 1. Installation

``` { .shell }

sb install deluge

```

### 2. URL

- To access Deluge, visit `https://deluge.xDOMAIN_NAMEx`

!!! info
    **default login**

```yaml
        user: admin
    password: deluge
```

### 3. Setup

- Change login password.

- Click Preferences in the top bar and on the Downloads section enter the following paths: <br />
  - Download to: <br />
    `/mnt/unionfs/downloads/torrents/deluge/incoming`
  - Move completed to: <br />
    `/mnt/unionfs/downloads/torrents/deluge/completed`
  - Autoadd `.torrent files` from: <br />
    `/mnt/unionfs/downloads/torrents/deluge/watched`

- Click the `Plugins` section
  - enable the `labels` plugin.
  - enable and the `Extractor` plugin. <br />
      In order for Sonarr or Radarr to import media packaged within .rar files, they will have to be extracted.
  - After clicking `"Apply"`, select the `Extractor`  plugin on the left. <br />
      Make sure the directory points to the `completed` folder within your Deluge data directory.  <br />
      `/mnt/unionfs/downloads/torrents/deluge/completed` <br />
      Also, make sure that the Create torrent name sub-folder setting is checked.

### 4. Adding to Sonarr/Radarr

To add Deluge as a download client in Sonarr/Radarr use the following settings. Both are able to remove completed torrents after they have finished seeding.

  ![](../images/community/deluge_add_to_arr.png)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `deluge_instances`.

    === "Role-level Override"

        Applies to all instances of deluge:

        ```yaml
        deluge_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `deluge2`):

        ```yaml
        deluge2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `deluge_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `deluge_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        deluge_instances: ["deluge"]

        ```

    === "Example"

        ```yaml
        # Type: list
        deluge_instances: ["deluge", "deluge2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        deluge_role_paths_folder: "{{ deluge_name }}"

        # Type: string
        deluge_role_paths_location: "{{ server_appdata_path }}/{{ deluge_role_paths_folder }}"

        # Type: string
        deluge_role_paths_conf: "{{ deluge_role_paths_location }}/core.conf"

        # Type: string
        deluge_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ deluge_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        deluge2_paths_folder: "{{ deluge_name }}"

        # Type: string
        deluge2_paths_location: "{{ server_appdata_path }}/{{ deluge_role_paths_folder }}"

        # Type: string
        deluge2_paths_conf: "{{ deluge_role_paths_location }}/core.conf"

        # Type: string
        deluge2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ deluge_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        deluge_role_web_subdomain: "{{ deluge_name }}"

        # Type: string
        deluge_role_web_domain: "{{ user.domain }}"

        # Type: string
        deluge_role_web_port: "8112"

        # Type: string
        deluge_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='deluge') + '.' + lookup('role_var', '_web_domain', role='deluge')
                              if (lookup('role_var', '_web_subdomain', role='deluge') | length > 0)
                              else lookup('role_var', '_web_domain', role='deluge')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        deluge2_web_subdomain: "{{ deluge_name }}"

        # Type: string
        deluge2_web_domain: "{{ user.domain }}"

        # Type: string
        deluge2_web_port: "8112"

        # Type: string
        deluge2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='deluge') + '.' + lookup('role_var', '_web_domain', role='deluge')
                          if (lookup('role_var', '_web_subdomain', role='deluge') | length > 0)
                          else lookup('role_var', '_web_domain', role='deluge')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        deluge_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='deluge') }}"

        # Type: string
        deluge_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='deluge') }}"

        # Type: bool (true/false)
        deluge_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        deluge2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='deluge') }}"

        # Type: string
        deluge2_dns_zone: "{{ lookup('role_var', '_web_domain', role='deluge') }}"

        # Type: bool (true/false)
        deluge2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        deluge_role_traefik_sso_middleware: ""

        # Type: string
        deluge_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',themepark-' + deluge_name
                                                      if (lookup('role_var', '_themepark_enabled', role='deluge') and global_themepark_plugin_enabled)
                                                      else '') }}"

        # Type: string
        deluge_role_traefik_middleware_custom: ""

        # Type: string
        deluge_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        deluge_role_traefik_enabled: true

        # Type: bool (true/false)
        deluge_role_traefik_api_enabled: false

        # Type: string
        deluge_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        deluge2_traefik_sso_middleware: ""

        # Type: string
        deluge2_traefik_middleware_default: "{{ traefik_default_middleware
                                                + (',themepark-' + deluge_name
                                                  if (lookup('role_var', '_themepark_enabled', role='deluge') and global_themepark_plugin_enabled)
                                                  else '') }}"

        # Type: string
        deluge2_traefik_middleware_custom: ""

        # Type: string
        deluge2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        deluge2_traefik_enabled: true

        # Type: bool (true/false)
        deluge2_traefik_api_enabled: false

        # Type: string
        deluge2_traefik_api_endpoint: ""

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        deluge_role_themepark_enabled: false

        # Type: string
        deluge_role_themepark_app: "deluge"

        # Type: string
        deluge_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        deluge_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        deluge_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        deluge2_themepark_enabled: false

        # Type: string
        deluge2_themepark_app: "deluge"

        # Type: string
        deluge2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        deluge2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        deluge2_themepark_addons: []

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        deluge_role_docker_container: "{{ deluge_name }}"

        # Image
        # Type: bool (true/false)
        deluge_role_docker_image_pull: true

        # Type: string
        deluge_role_docker_image_repo: "lscr.io/linuxserver/deluge"

        # Type: string
        deluge_role_docker_image_tag: "latest"

        # Type: string
        deluge_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='deluge') }}:{{ lookup('role_var', '_docker_image_tag', role='deluge') }}"

        # Ports
        # Type: string
        deluge_role_docker_ports_58112: "{{ port_lookup_58112.meta.port
                                         if (port_lookup_58112.meta.port is defined) and (port_lookup_58112.meta.port | trim | length > 0)
                                         else '58112' }}"

        # Type: list
        deluge_role_docker_ports_default: 
          - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}"
          - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}/udp"

        # Type: list
        deluge_role_docker_ports_custom: []

        # Envs
        # Type: dict
        deluge_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"

        # Type: dict
        deluge_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        deluge_role_docker_volumes_default: 
          - "{{ deluge_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        deluge_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        deluge_role_docker_labels_default: {}

        # Type: dict
        deluge_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        deluge_role_docker_hostname: "{{ deluge_name }}"

        # Networks
        # Type: string
        deluge_role_docker_networks_alias: "{{ deluge_name }}"

        # Type: list
        deluge_role_docker_networks_default: []

        # Type: list
        deluge_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        deluge_role_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        deluge_role_docker_stop_timeout: 900

        # State
        # Type: string
        deluge_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        deluge_role_docker_blkio_weight:

        # Type: int
        deluge_role_docker_cpu_period:

        # Type: int
        deluge_role_docker_cpu_quota:

        # Type: int
        deluge_role_docker_cpu_shares:

        # Type: string
        deluge_role_docker_cpus:

        # Type: string
        deluge_role_docker_cpuset_cpus:

        # Type: string
        deluge_role_docker_cpuset_mems:

        # Type: string
        deluge_role_docker_kernel_memory:

        # Type: string
        deluge_role_docker_memory:

        # Type: string
        deluge_role_docker_memory_reservation:

        # Type: string
        deluge_role_docker_memory_swap:

        # Type: int
        deluge_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        deluge_role_docker_cap_drop:

        # Type: list
        deluge_role_docker_device_cgroup_rules:

        # Type: list
        deluge_role_docker_device_read_bps:

        # Type: list
        deluge_role_docker_device_read_iops:

        # Type: list
        deluge_role_docker_device_requests:

        # Type: list
        deluge_role_docker_device_write_bps:

        # Type: list
        deluge_role_docker_device_write_iops:

        # Type: list
        deluge_role_docker_devices:

        # Type: string
        deluge_role_docker_devices_default:

        # Type: bool (true/false)
        deluge_role_docker_privileged:

        # Type: list
        deluge_role_docker_security_opts:

        # Networking
        # Type: list
        deluge_role_docker_dns_opts:

        # Type: list
        deluge_role_docker_dns_search_domains:

        # Type: list
        deluge_role_docker_dns_servers:

        # Type: dict
        deluge_role_docker_hosts:

        # Type: string
        deluge_role_docker_hosts_use_common:

        # Type: string
        deluge_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        deluge_role_docker_keep_volumes:

        # Type: list
        deluge_role_docker_mounts:

        # Type: string
        deluge_role_docker_volume_driver:

        # Type: list
        deluge_role_docker_volumes_from:

        # Type: string
        deluge_role_docker_volumes_global:

        # Type: string
        deluge_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        deluge_role_docker_healthcheck:

        # Type: bool (true/false)
        deluge_role_docker_init:

        # Type: string
        deluge_role_docker_log_driver:

        # Type: dict
        deluge_role_docker_log_options:

        # Type: bool (true/false)
        deluge_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        deluge_role_docker_auto_remove:

        # Type: list
        deluge_role_docker_capabilities:

        # Type: string
        deluge_role_docker_cgroup_parent:

        # Type: string
        deluge_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        deluge_role_docker_cleanup:

        # Type: list
        deluge_role_docker_commands:

        # Type: string
        deluge_role_docker_create_timeout:

        # Type: string
        deluge_role_docker_domainname:

        # Type: string
        deluge_role_docker_entrypoint:

        # Type: string
        deluge_role_docker_env_file:

        # Type: list
        deluge_role_docker_exposed_ports:

        # Type: string
        deluge_role_docker_force_kill:

        # Type: list
        deluge_role_docker_groups:

        # Type: int
        deluge_role_docker_healthy_wait_timeout:

        # Type: string
        deluge_role_docker_ipc_mode:

        # Type: string
        deluge_role_docker_kill_signal:

        # Type: string
        deluge_role_docker_labels_use_common:

        # Type: list
        deluge_role_docker_links:

        # Type: bool (true/false)
        deluge_role_docker_oom_killer:

        # Type: int
        deluge_role_docker_oom_score_adj:

        # Type: bool (true/false)
        deluge_role_docker_paused:

        # Type: string
        deluge_role_docker_pid_mode:

        # Type: bool (true/false)
        deluge_role_docker_read_only:

        # Type: bool (true/false)
        deluge_role_docker_recreate:

        # Type: int
        deluge_role_docker_restart_retries:

        # Type: string
        deluge_role_docker_runtime:

        # Type: string
        deluge_role_docker_shm_size:

        # Type: dict
        deluge_role_docker_storage_opts:

        # Type: list
        deluge_role_docker_sysctls:

        # Type: list
        deluge_role_docker_tmpfs:

        # Type: list
        deluge_role_docker_ulimits:

        # Type: string
        deluge_role_docker_user:

        # Type: string
        deluge_role_docker_userns_mode:

        # Type: string
        deluge_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        deluge2_docker_container: "{{ deluge_name }}"

        # Image
        # Type: bool (true/false)
        deluge2_docker_image_pull: true

        # Type: string
        deluge2_docker_image_repo: "lscr.io/linuxserver/deluge"

        # Type: string
        deluge2_docker_image_tag: "latest"

        # Type: string
        deluge2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='deluge') }}:{{ lookup('role_var', '_docker_image_tag', role='deluge') }}"

        # Ports
        # Type: string
        deluge2_docker_ports_58112: "{{ port_lookup_58112.meta.port
                                     if (port_lookup_58112.meta.port is defined) and (port_lookup_58112.meta.port | trim | length > 0)
                                     else '58112' }}"

        # Type: list
        deluge2_docker_ports_default: 
          - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}"
          - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}/udp"

        # Type: list
        deluge2_docker_ports_custom: []

        # Envs
        # Type: dict
        deluge2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"

        # Type: dict
        deluge2_docker_envs_custom: {}

        # Volumes
        # Type: list
        deluge2_docker_volumes_default: 
          - "{{ deluge_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        deluge2_docker_volumes_custom: []

        # Labels
        # Type: dict
        deluge2_docker_labels_default: {}

        # Type: dict
        deluge2_docker_labels_custom: {}

        # Hostname
        # Type: string
        deluge2_docker_hostname: "{{ deluge_name }}"

        # Networks
        # Type: string
        deluge2_docker_networks_alias: "{{ deluge_name }}"

        # Type: list
        deluge2_docker_networks_default: []

        # Type: list
        deluge2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        deluge2_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        deluge2_docker_stop_timeout: 900

        # State
        # Type: string
        deluge2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        deluge2_docker_blkio_weight:
        # Type: int
        deluge2_docker_cpu_period:
        # Type: int
        deluge2_docker_cpu_quota:
        # Type: int
        deluge2_docker_cpu_shares:
        # Type: string
        deluge2_docker_cpus:
        # Type: string
        deluge2_docker_cpuset_cpus:
        # Type: string
        deluge2_docker_cpuset_mems:
        # Type: string
        deluge2_docker_kernel_memory:
        # Type: string
        deluge2_docker_memory:
        # Type: string
        deluge2_docker_memory_reservation:
        # Type: string
        deluge2_docker_memory_swap:
        # Type: int
        deluge2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        deluge2_docker_cap_drop:
        # Type: list
        deluge2_docker_device_cgroup_rules:
        # Type: list
        deluge2_docker_device_read_bps:
        # Type: list
        deluge2_docker_device_read_iops:
        # Type: list
        deluge2_docker_device_requests:
        # Type: list
        deluge2_docker_device_write_bps:
        # Type: list
        deluge2_docker_device_write_iops:
        # Type: list
        deluge2_docker_devices:
        # Type: string
        deluge2_docker_devices_default:
        # Type: bool (true/false)
        deluge2_docker_privileged:
        # Type: list
        deluge2_docker_security_opts:

        # Networking
        # Type: list
        deluge2_docker_dns_opts:
        # Type: list
        deluge2_docker_dns_search_domains:
        # Type: list
        deluge2_docker_dns_servers:
        # Type: dict
        deluge2_docker_hosts:
        # Type: string
        deluge2_docker_hosts_use_common:
        # Type: string
        deluge2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        deluge2_docker_keep_volumes:
        # Type: list
        deluge2_docker_mounts:
        # Type: string
        deluge2_docker_volume_driver:
        # Type: list
        deluge2_docker_volumes_from:
        # Type: string
        deluge2_docker_volumes_global:
        # Type: string
        deluge2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        deluge2_docker_healthcheck:
        # Type: bool (true/false)
        deluge2_docker_init:
        # Type: string
        deluge2_docker_log_driver:
        # Type: dict
        deluge2_docker_log_options:
        # Type: bool (true/false)
        deluge2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        deluge2_docker_auto_remove:
        # Type: list
        deluge2_docker_capabilities:
        # Type: string
        deluge2_docker_cgroup_parent:
        # Type: string
        deluge2_docker_cgroupns_mode:
        # Type: bool (true/false)
        deluge2_docker_cleanup:
        # Type: list
        deluge2_docker_commands:
        # Type: string
        deluge2_docker_create_timeout:
        # Type: string
        deluge2_docker_domainname:
        # Type: string
        deluge2_docker_entrypoint:
        # Type: string
        deluge2_docker_env_file:
        # Type: list
        deluge2_docker_exposed_ports:
        # Type: string
        deluge2_docker_force_kill:
        # Type: list
        deluge2_docker_groups:
        # Type: int
        deluge2_docker_healthy_wait_timeout:
        # Type: string
        deluge2_docker_ipc_mode:
        # Type: string
        deluge2_docker_kill_signal:
        # Type: string
        deluge2_docker_labels_use_common:
        # Type: list
        deluge2_docker_links:
        # Type: bool (true/false)
        deluge2_docker_oom_killer:
        # Type: int
        deluge2_docker_oom_score_adj:
        # Type: bool (true/false)
        deluge2_docker_paused:
        # Type: string
        deluge2_docker_pid_mode:
        # Type: bool (true/false)
        deluge2_docker_read_only:
        # Type: bool (true/false)
        deluge2_docker_recreate:
        # Type: int
        deluge2_docker_restart_retries:
        # Type: string
        deluge2_docker_runtime:
        # Type: string
        deluge2_docker_shm_size:
        # Type: dict
        deluge2_docker_storage_opts:
        # Type: list
        deluge2_docker_sysctls:
        # Type: list
        deluge2_docker_tmpfs:
        # Type: list
        deluge2_docker_ulimits:
        # Type: string
        deluge2_docker_user:
        # Type: string
        deluge2_docker_userns_mode:
        # Type: string
        deluge2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        deluge_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        deluge_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        deluge_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        deluge_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        deluge_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        deluge_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        deluge_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        deluge_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        deluge_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        deluge_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        deluge_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        deluge_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        deluge_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        deluge_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        deluge_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        deluge_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        deluge_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            deluge_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "deluge2.{{ user.domain }}"
              - "deluge.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            deluge_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'deluge2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `deluge2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        deluge2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        deluge2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        deluge2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        deluge2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        deluge2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        deluge2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        deluge2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        deluge2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        deluge2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        deluge2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        deluge2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        deluge2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        deluge2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        deluge2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        deluge2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        deluge2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        deluge2_web_scheme:

        ```

        1.  Example:

            ```yaml
            deluge2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "deluge2.{{ user.domain }}"
              - "deluge.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            deluge2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'deluge2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
