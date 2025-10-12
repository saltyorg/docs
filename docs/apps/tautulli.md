---
hide:
  - tags
tags:
  - tautulli
---

# Tautulli

# What is it?

[Tautulli](http://tautulli.com/) (Tautulli), by JonnyWong16, is a web-based application runs alongside the Plex Media Server to monitor activity and track various statistics (eg most watched media).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://tautulli.com){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Tautulli/Tautulli/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Tautulli/Tautulli){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/tautulli){: .header-icons }|

## 2. URL

To access Tautulli, visit `https://tautulli._yourdomain_.com`

## 3. Setup Wizard

1. First time you go to the Tautulli site, you will be presented with the "Tautulli Setup Wizard". Click `Next`.

    ![](../images/tautulli/01-tautulli-wizard.png)

2. On the "Plex Authentication" page, sign in with your Plex username and password, and click `Authenticate`. When you see the "Authentication successful." message, click `Next`.

    ![](../images/tautulli/02-tautulli-plex-auth.png)

3. On the "Plex Media Server" page, set the following:

    - "Plex IP or Hostname": `plex`
    - "Port Number": `32400`
    - "Use SSL": disabled
    - "Remote Server": disabled

     Click `Verify`. When you see the "Server found!" message, click `Next`.

     ![](../images/tautulli/03-tautulli-plex-media.png)

4. On the "Activity Logging" page, select your preferences (default is OK) and click `Next`.

    ![](../images/tautulli/04-tautulli-activity.png)

5. On the "Notifications" page, simply click `Next`.

    ![](../images/tautulli/05-tautulli-notifications.png)

6. On the "Database Import" page, click `Finish` to complete the setup.

    ![](../images/tautulli/06-tautulli-database.png)

## 4. Settings

1. Once the Tautulli page comes up, go to "Settings".

    ![](../images/tautulli/07-tautulli-settings.png)

2. Click "Web Interface" on the left. Fill in "HTTP Username" and "HTTP Password (this will be the login for your Tautulli site), but don't click `Save` yet.

    ![](../images/tautulli/08-tautulli-web.png)

3. On the "Restart" popup window, click `Restart`.

    ![](../images/tautulli/10-tautulli-reboot.png)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `tautulli_instances`.

    === "Role-level Override"

        Applies to all instances of tautulli:

        ```yaml
        tautulli_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `tautulli2`):

        ```yaml
        tautulli2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `tautulli_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tautulli_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        tautulli_instances: ["tautulli"]

        ```

    === "Example"

        ```yaml
        # Type: list
        tautulli_instances: ["tautulli", "tautulli2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        tautulli_role_paths_folder: "{{ tautulli_name }}"

        # Type: string
        tautulli_role_paths_location: "{{ server_appdata_path }}/{{ tautulli_role_paths_folder }}"

        # Type: string
        tautulli_role_paths_scripts_location: "{{ server_appdata_path }}/scripts/tautulli"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        tautulli2_paths_folder: "{{ tautulli_name }}"

        # Type: string
        tautulli2_paths_location: "{{ server_appdata_path }}/{{ tautulli_role_paths_folder }}"

        # Type: string
        tautulli2_paths_scripts_location: "{{ server_appdata_path }}/scripts/tautulli"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        tautulli_role_web_subdomain: "{{ tautulli_name }}"

        # Type: string
        tautulli_role_web_domain: "{{ user.domain }}"

        # Type: string
        tautulli_role_web_port: "8181"

        # Type: string
        tautulli_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tautulli') + '.' + lookup('role_var', '_web_domain', role='tautulli')
                                if (lookup('role_var', '_web_subdomain', role='tautulli') | length > 0)
                                else lookup('role_var', '_web_domain', role='tautulli')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        tautulli2_web_subdomain: "{{ tautulli_name }}"

        # Type: string
        tautulli2_web_domain: "{{ user.domain }}"

        # Type: string
        tautulli2_web_port: "8181"

        # Type: string
        tautulli2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tautulli') + '.' + lookup('role_var', '_web_domain', role='tautulli')
                            if (lookup('role_var', '_web_subdomain', role='tautulli') | length > 0)
                            else lookup('role_var', '_web_domain', role='tautulli')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        tautulli_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tautulli') }}"

        # Type: string
        tautulli_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tautulli') }}"

        # Type: bool (true/false)
        tautulli_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        tautulli2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tautulli') }}"

        # Type: string
        tautulli2_dns_zone: "{{ lookup('role_var', '_web_domain', role='tautulli') }}"

        # Type: bool (true/false)
        tautulli2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        tautulli_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        tautulli_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                      + (',themepark-' + tautulli_name
                                                        if (lookup('role_var', '_themepark_enabled', role='tautulli') and global_themepark_plugin_enabled)
                                                        else '') }}"

        # Type: string
        tautulli_role_traefik_middleware_custom: ""

        # Type: string
        tautulli_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        tautulli_role_traefik_enabled: true

        # Type: bool (true/false)
        tautulli_role_traefik_api_enabled: true

        # Type: string
        tautulli_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/newsletter`) || PathPrefix(`/image`) || PathPrefix(`/pms_image_proxy`)"

        # Type: bool (true/false)
        tautulli_role_traefik_gzip_enabled: false

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        tautulli2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        tautulli2_traefik_middleware_default: "{{ traefik_default_middleware
                                                  + (',themepark-' + tautulli_name
                                                    if (lookup('role_var', '_themepark_enabled', role='tautulli') and global_themepark_plugin_enabled)
                                                    else '') }}"

        # Type: string
        tautulli2_traefik_middleware_custom: ""

        # Type: string
        tautulli2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        tautulli2_traefik_enabled: true

        # Type: bool (true/false)
        tautulli2_traefik_api_enabled: true

        # Type: string
        tautulli2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/newsletter`) || PathPrefix(`/image`) || PathPrefix(`/pms_image_proxy`)"

        # Type: bool (true/false)
        tautulli2_traefik_gzip_enabled: false

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        tautulli_role_themepark_enabled: false

        # Type: string
        tautulli_role_themepark_app: "tautulli"

        # Type: string
        tautulli_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        tautulli_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        tautulli_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        tautulli2_themepark_enabled: false

        # Type: string
        tautulli2_themepark_app: "tautulli"

        # Type: string
        tautulli2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        tautulli2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        tautulli2_themepark_addons: []

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        tautulli_role_docker_container: "{{ tautulli_name }}"

        # Image
        # Type: bool (true/false)
        tautulli_role_docker_image_pull: true

        # Type: string
        tautulli_role_docker_image_repo: "ghcr.io/hotio/tautulli"

        # Type: string
        tautulli_role_docker_image_tag: "release"

        # Type: string
        tautulli_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tautulli') }}:{{ lookup('role_var', '_docker_image_tag', role='tautulli') }}"

        # Envs
        # Type: dict
        tautulli_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        tautulli_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        tautulli_role_docker_volumes_default: 
          - "{{ tautulli_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        tautulli_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        tautulli_role_docker_labels_default: {}

        # Type: dict
        tautulli_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        tautulli_role_docker_hostname: "{{ tautulli_name }}"

        # Networks
        # Type: string
        tautulli_role_docker_networks_alias: "{{ tautulli_name }}"

        # Type: list
        tautulli_role_docker_networks_default: []

        # Type: list
        tautulli_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        tautulli_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        tautulli_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        tautulli_role_docker_blkio_weight:

        # Type: int
        tautulli_role_docker_cpu_period:

        # Type: int
        tautulli_role_docker_cpu_quota:

        # Type: int
        tautulli_role_docker_cpu_shares:

        # Type: string
        tautulli_role_docker_cpus:

        # Type: string
        tautulli_role_docker_cpuset_cpus:

        # Type: string
        tautulli_role_docker_cpuset_mems:

        # Type: string
        tautulli_role_docker_kernel_memory:

        # Type: string
        tautulli_role_docker_memory:

        # Type: string
        tautulli_role_docker_memory_reservation:

        # Type: string
        tautulli_role_docker_memory_swap:

        # Type: int
        tautulli_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        tautulli_role_docker_cap_drop:

        # Type: list
        tautulli_role_docker_device_cgroup_rules:

        # Type: list
        tautulli_role_docker_device_read_bps:

        # Type: list
        tautulli_role_docker_device_read_iops:

        # Type: list
        tautulli_role_docker_device_requests:

        # Type: list
        tautulli_role_docker_device_write_bps:

        # Type: list
        tautulli_role_docker_device_write_iops:

        # Type: list
        tautulli_role_docker_devices:

        # Type: string
        tautulli_role_docker_devices_default:

        # Type: bool (true/false)
        tautulli_role_docker_privileged:

        # Type: list
        tautulli_role_docker_security_opts:

        # Networking
        # Type: list
        tautulli_role_docker_dns_opts:

        # Type: list
        tautulli_role_docker_dns_search_domains:

        # Type: list
        tautulli_role_docker_dns_servers:

        # Type: dict
        tautulli_role_docker_hosts:

        # Type: string
        tautulli_role_docker_hosts_use_common:

        # Type: string
        tautulli_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        tautulli_role_docker_keep_volumes:

        # Type: list
        tautulli_role_docker_mounts:

        # Type: string
        tautulli_role_docker_volume_driver:

        # Type: list
        tautulli_role_docker_volumes_from:

        # Type: string
        tautulli_role_docker_volumes_global:

        # Type: string
        tautulli_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        tautulli_role_docker_healthcheck:

        # Type: bool (true/false)
        tautulli_role_docker_init:

        # Type: string
        tautulli_role_docker_log_driver:

        # Type: dict
        tautulli_role_docker_log_options:

        # Type: bool (true/false)
        tautulli_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        tautulli_role_docker_auto_remove:

        # Type: list
        tautulli_role_docker_capabilities:

        # Type: string
        tautulli_role_docker_cgroup_parent:

        # Type: string
        tautulli_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        tautulli_role_docker_cleanup:

        # Type: list
        tautulli_role_docker_commands:

        # Type: string
        tautulli_role_docker_create_timeout:

        # Type: string
        tautulli_role_docker_domainname:

        # Type: string
        tautulli_role_docker_entrypoint:

        # Type: string
        tautulli_role_docker_env_file:

        # Type: list
        tautulli_role_docker_exposed_ports:

        # Type: string
        tautulli_role_docker_force_kill:

        # Type: list
        tautulli_role_docker_groups:

        # Type: int
        tautulli_role_docker_healthy_wait_timeout:

        # Type: string
        tautulli_role_docker_ipc_mode:

        # Type: string
        tautulli_role_docker_kill_signal:

        # Type: string
        tautulli_role_docker_labels_use_common:

        # Type: list
        tautulli_role_docker_links:

        # Type: bool (true/false)
        tautulli_role_docker_oom_killer:

        # Type: int
        tautulli_role_docker_oom_score_adj:

        # Type: bool (true/false)
        tautulli_role_docker_paused:

        # Type: string
        tautulli_role_docker_pid_mode:

        # Type: list
        tautulli_role_docker_ports:

        # Type: bool (true/false)
        tautulli_role_docker_read_only:

        # Type: bool (true/false)
        tautulli_role_docker_recreate:

        # Type: int
        tautulli_role_docker_restart_retries:

        # Type: string
        tautulli_role_docker_runtime:

        # Type: string
        tautulli_role_docker_shm_size:

        # Type: int
        tautulli_role_docker_stop_timeout:

        # Type: dict
        tautulli_role_docker_storage_opts:

        # Type: list
        tautulli_role_docker_sysctls:

        # Type: list
        tautulli_role_docker_tmpfs:

        # Type: list
        tautulli_role_docker_ulimits:

        # Type: string
        tautulli_role_docker_user:

        # Type: string
        tautulli_role_docker_userns_mode:

        # Type: string
        tautulli_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        tautulli2_docker_container: "{{ tautulli_name }}"

        # Image
        # Type: bool (true/false)
        tautulli2_docker_image_pull: true

        # Type: string
        tautulli2_docker_image_repo: "ghcr.io/hotio/tautulli"

        # Type: string
        tautulli2_docker_image_tag: "release"

        # Type: string
        tautulli2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tautulli') }}:{{ lookup('role_var', '_docker_image_tag', role='tautulli') }}"

        # Envs
        # Type: dict
        tautulli2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        tautulli2_docker_envs_custom: {}

        # Volumes
        # Type: list
        tautulli2_docker_volumes_default: 
          - "{{ tautulli_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        tautulli2_docker_volumes_custom: []

        # Labels
        # Type: dict
        tautulli2_docker_labels_default: {}

        # Type: dict
        tautulli2_docker_labels_custom: {}

        # Hostname
        # Type: string
        tautulli2_docker_hostname: "{{ tautulli_name }}"

        # Networks
        # Type: string
        tautulli2_docker_networks_alias: "{{ tautulli_name }}"

        # Type: list
        tautulli2_docker_networks_default: []

        # Type: list
        tautulli2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        tautulli2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        tautulli2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        tautulli2_docker_blkio_weight:
        # Type: int
        tautulli2_docker_cpu_period:
        # Type: int
        tautulli2_docker_cpu_quota:
        # Type: int
        tautulli2_docker_cpu_shares:
        # Type: string
        tautulli2_docker_cpus:
        # Type: string
        tautulli2_docker_cpuset_cpus:
        # Type: string
        tautulli2_docker_cpuset_mems:
        # Type: string
        tautulli2_docker_kernel_memory:
        # Type: string
        tautulli2_docker_memory:
        # Type: string
        tautulli2_docker_memory_reservation:
        # Type: string
        tautulli2_docker_memory_swap:
        # Type: int
        tautulli2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        tautulli2_docker_cap_drop:
        # Type: list
        tautulli2_docker_device_cgroup_rules:
        # Type: list
        tautulli2_docker_device_read_bps:
        # Type: list
        tautulli2_docker_device_read_iops:
        # Type: list
        tautulli2_docker_device_requests:
        # Type: list
        tautulli2_docker_device_write_bps:
        # Type: list
        tautulli2_docker_device_write_iops:
        # Type: list
        tautulli2_docker_devices:
        # Type: string
        tautulli2_docker_devices_default:
        # Type: bool (true/false)
        tautulli2_docker_privileged:
        # Type: list
        tautulli2_docker_security_opts:

        # Networking
        # Type: list
        tautulli2_docker_dns_opts:
        # Type: list
        tautulli2_docker_dns_search_domains:
        # Type: list
        tautulli2_docker_dns_servers:
        # Type: dict
        tautulli2_docker_hosts:
        # Type: string
        tautulli2_docker_hosts_use_common:
        # Type: string
        tautulli2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        tautulli2_docker_keep_volumes:
        # Type: list
        tautulli2_docker_mounts:
        # Type: string
        tautulli2_docker_volume_driver:
        # Type: list
        tautulli2_docker_volumes_from:
        # Type: string
        tautulli2_docker_volumes_global:
        # Type: string
        tautulli2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        tautulli2_docker_healthcheck:
        # Type: bool (true/false)
        tautulli2_docker_init:
        # Type: string
        tautulli2_docker_log_driver:
        # Type: dict
        tautulli2_docker_log_options:
        # Type: bool (true/false)
        tautulli2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        tautulli2_docker_auto_remove:
        # Type: list
        tautulli2_docker_capabilities:
        # Type: string
        tautulli2_docker_cgroup_parent:
        # Type: string
        tautulli2_docker_cgroupns_mode:
        # Type: bool (true/false)
        tautulli2_docker_cleanup:
        # Type: list
        tautulli2_docker_commands:
        # Type: string
        tautulli2_docker_create_timeout:
        # Type: string
        tautulli2_docker_domainname:
        # Type: string
        tautulli2_docker_entrypoint:
        # Type: string
        tautulli2_docker_env_file:
        # Type: list
        tautulli2_docker_exposed_ports:
        # Type: string
        tautulli2_docker_force_kill:
        # Type: list
        tautulli2_docker_groups:
        # Type: int
        tautulli2_docker_healthy_wait_timeout:
        # Type: string
        tautulli2_docker_ipc_mode:
        # Type: string
        tautulli2_docker_kill_signal:
        # Type: string
        tautulli2_docker_labels_use_common:
        # Type: list
        tautulli2_docker_links:
        # Type: bool (true/false)
        tautulli2_docker_oom_killer:
        # Type: int
        tautulli2_docker_oom_score_adj:
        # Type: bool (true/false)
        tautulli2_docker_paused:
        # Type: string
        tautulli2_docker_pid_mode:
        # Type: list
        tautulli2_docker_ports:
        # Type: bool (true/false)
        tautulli2_docker_read_only:
        # Type: bool (true/false)
        tautulli2_docker_recreate:
        # Type: int
        tautulli2_docker_restart_retries:
        # Type: string
        tautulli2_docker_runtime:
        # Type: string
        tautulli2_docker_shm_size:
        # Type: int
        tautulli2_docker_stop_timeout:
        # Type: dict
        tautulli2_docker_storage_opts:
        # Type: list
        tautulli2_docker_sysctls:
        # Type: list
        tautulli2_docker_tmpfs:
        # Type: list
        tautulli2_docker_ulimits:
        # Type: string
        tautulli2_docker_user:
        # Type: string
        tautulli2_docker_userns_mode:
        # Type: string
        tautulli2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        tautulli_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        tautulli_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        tautulli_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tautulli_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        tautulli_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        tautulli_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        tautulli_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        tautulli_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        tautulli_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        tautulli_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        tautulli_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        tautulli_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        tautulli_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        tautulli_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        tautulli_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        tautulli_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        tautulli_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            tautulli_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tautulli2.{{ user.domain }}"
              - "tautulli.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            tautulli_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tautulli2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `tautulli2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tautulli2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        tautulli2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tautulli2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tautulli2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tautulli2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tautulli2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tautulli2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tautulli2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tautulli2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tautulli2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tautulli2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tautulli2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tautulli2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tautulli2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tautulli2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        tautulli2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tautulli2_web_scheme:

        ```

        1.  Example:

            ```yaml
            tautulli2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tautulli2.{{ user.domain }}"
              - "tautulli.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            tautulli2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tautulli2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Overseerr](overseerr.md).
