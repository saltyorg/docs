---
hide:
  - tags
tags:
  - portainer
---

# Portainer

THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

# What is it?

[Portainer](https://portainer.io/) is an open-source lightweight management UI which allows you to easily manage your Docker containers, images, networks and volumes.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://portainer.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.portainer.io//){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/portainer/portainer/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/portainer/portainer-ce){: .header-icons }|

## 2. URL

To access Portainer, visit  `https://portainer._yourdomain.com_`

## 3. Initial Setup

1. The first time you go to the Portainer page, you will be presented with the message "Please create the initial administrator user.". Fill in your preferred admin username and password. Click `Create User`.

    ![](../images/portainer/portainer-01.png)

2. On this first visit when you set up the admin user, you will be logged in automagically. On future visits, you will be asked to log in with your username and password.

    ![](../images/portainer/portainer-02.png)

3. On the "Connect Portainer to the Docker environment you want to manage." screen, select `Local: Manage the local Docker environment` and click `Connect`.

    _Note: Don't be confused by "local" in this context. It is referring to the relationship between the Docker instance you're managing on your Saltbox server and this instance of Portainer. These things are local to each other on your Saltbox server, wherever that is. They may be remote from you, but they are local to each other.  Pay no mind to what looks like a warning at the bottom. Saltbox has already taken care of that._

    ![](../images/portainer/portainer-03.png)

4. Portainer is now set up.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        portainer_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    portainer_name: portainer

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    portainer_role_business_edition: false

    ```

??? example "Paths"

    ```yaml
    # Type: string
    portainer_role_paths_folder: "{{ portainer_name }}"

    # Type: string
    portainer_role_paths_location: "{{ server_appdata_path }}/{{ portainer_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    portainer_role_web_subdomain: "{{ portainer_name }}"

    # Type: string
    portainer_role_web_domain: "{{ user.domain }}"

    # Type: string
    portainer_role_web_port: "9000"

    # Type: string
    portainer_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='portainer') + '.' + lookup('role_var', '_web_domain', role='portainer')
                             if (lookup('role_var', '_web_subdomain', role='portainer') | length > 0)
                             else lookup('role_var', '_web_domain', role='portainer')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    portainer_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='portainer') }}"

    # Type: string
    portainer_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='portainer') }}"

    # Type: bool (true/false)
    portainer_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    portainer_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    portainer_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                   + (',themepark-' + portainer_name
                                                     if (lookup('role_var', '_themepark_enabled', role='portainer') and global_themepark_plugin_enabled)
                                                     else '') }}"

    # Type: string
    portainer_role_traefik_middleware_custom: ""

    # Type: string
    portainer_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    portainer_role_traefik_enabled: true

    # Type: bool (true/false)
    portainer_role_traefik_api_enabled: true

    # Type: string
    portainer_role_traefik_api_endpoint: "PathPrefix(`/api/websocket/`)"

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    portainer_role_themepark_enabled: false

    # Type: string
    portainer_role_themepark_theme: "{{ global_themepark_theme }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    portainer_role_docker_container: "{{ portainer_name }}"

    # Image
    # Type: bool (true/false)
    portainer_role_docker_image_pull: true

    # Type: string
    portainer_role_docker_image_tag: "latest"

    # Type: string
    portainer_role_docker_image_repo: "{{ 'portainer/portainer-ee'
                                       if lookup('role_var', '_business_edition', role='portainer')
                                       else 'portainer/portainer-ce' }}"

    # Type: string
    portainer_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='portainer') }}:{{ lookup('role_var', '_docker_image_tag', role='portainer') }}"

    # Envs
    # Type: dict
    portainer_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    portainer_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    portainer_role_docker_volumes_default: 
      - "{{ portainer_role_paths_location }}:/data"
      - "/var/run/docker.sock:/var/run/docker.sock"

    # Type: list
    portainer_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    portainer_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    portainer_role_docker_hostname: "{{ portainer_name }}"

    # Networks
    # Type: string
    portainer_role_docker_networks_alias: "{{ portainer_name }}"

    # Type: list
    portainer_role_docker_networks_default: []

    # Type: list
    portainer_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    portainer_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    portainer_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    portainer_role_docker_blkio_weight:

    # Type: int
    portainer_role_docker_cpu_period:

    # Type: int
    portainer_role_docker_cpu_quota:

    # Type: int
    portainer_role_docker_cpu_shares:

    # Type: string
    portainer_role_docker_cpus:

    # Type: string
    portainer_role_docker_cpuset_cpus:

    # Type: string
    portainer_role_docker_cpuset_mems:

    # Type: string
    portainer_role_docker_kernel_memory:

    # Type: string
    portainer_role_docker_memory:

    # Type: string
    portainer_role_docker_memory_reservation:

    # Type: string
    portainer_role_docker_memory_swap:

    # Type: int
    portainer_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    portainer_role_docker_cap_drop:

    # Type: list
    portainer_role_docker_device_cgroup_rules:

    # Type: list
    portainer_role_docker_device_read_bps:

    # Type: list
    portainer_role_docker_device_read_iops:

    # Type: list
    portainer_role_docker_device_requests:

    # Type: list
    portainer_role_docker_device_write_bps:

    # Type: list
    portainer_role_docker_device_write_iops:

    # Type: list
    portainer_role_docker_devices:

    # Type: string
    portainer_role_docker_devices_default:

    # Type: bool (true/false)
    portainer_role_docker_privileged:

    # Type: list
    portainer_role_docker_security_opts:


    # Networking
    # Type: list
    portainer_role_docker_dns_opts:

    # Type: list
    portainer_role_docker_dns_search_domains:

    # Type: list
    portainer_role_docker_dns_servers:

    # Type: dict
    portainer_role_docker_hosts:

    # Type: string
    portainer_role_docker_hosts_use_common:

    # Type: string
    portainer_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    portainer_role_docker_keep_volumes:

    # Type: list
    portainer_role_docker_mounts:

    # Type: string
    portainer_role_docker_volume_driver:

    # Type: list
    portainer_role_docker_volumes_from:

    # Type: string
    portainer_role_docker_volumes_global:

    # Type: string
    portainer_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    portainer_role_docker_healthcheck:

    # Type: bool (true/false)
    portainer_role_docker_init:

    # Type: string
    portainer_role_docker_log_driver:

    # Type: dict
    portainer_role_docker_log_options:

    # Type: bool (true/false)
    portainer_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    portainer_role_docker_auto_remove:

    # Type: list
    portainer_role_docker_capabilities:

    # Type: string
    portainer_role_docker_cgroup_parent:

    # Type: string
    portainer_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    portainer_role_docker_cleanup:

    # Type: list
    portainer_role_docker_commands:

    # Type: string
    portainer_role_docker_create_timeout:

    # Type: string
    portainer_role_docker_domainname:

    # Type: string
    portainer_role_docker_entrypoint:

    # Type: string
    portainer_role_docker_env_file:

    # Type: list
    portainer_role_docker_exposed_ports:

    # Type: string
    portainer_role_docker_force_kill:

    # Type: list
    portainer_role_docker_groups:

    # Type: int
    portainer_role_docker_healthy_wait_timeout:

    # Type: string
    portainer_role_docker_ipc_mode:

    # Type: string
    portainer_role_docker_kill_signal:

    # Type: string
    portainer_role_docker_labels_use_common:

    # Type: list
    portainer_role_docker_links:

    # Type: bool (true/false)
    portainer_role_docker_oom_killer:

    # Type: int
    portainer_role_docker_oom_score_adj:

    # Type: bool (true/false)
    portainer_role_docker_paused:

    # Type: string
    portainer_role_docker_pid_mode:

    # Type: list
    portainer_role_docker_ports:

    # Type: bool (true/false)
    portainer_role_docker_read_only:

    # Type: bool (true/false)
    portainer_role_docker_recreate:

    # Type: int
    portainer_role_docker_restart_retries:

    # Type: string
    portainer_role_docker_runtime:

    # Type: string
    portainer_role_docker_shm_size:

    # Type: int
    portainer_role_docker_stop_timeout:

    # Type: dict
    portainer_role_docker_storage_opts:

    # Type: list
    portainer_role_docker_sysctls:

    # Type: list
    portainer_role_docker_tmpfs:

    # Type: list
    portainer_role_docker_ulimits:

    # Type: string
    portainer_role_docker_user:

    # Type: string
    portainer_role_docker_userns_mode:

    # Type: string
    portainer_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    portainer_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    portainer_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    portainer_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    portainer_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    portainer_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    portainer_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    portainer_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    portainer_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    portainer_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    portainer_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    portainer_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    portainer_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    portainer_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    portainer_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    portainer_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    portainer_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    portainer_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        portainer_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "portainer2.{{ user.domain }}"
          - "portainer.otherdomain.tld"
        ```
        
        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
        

    2.  Example:

        ```yaml
        portainer_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'portainer2.' + user.domain }}`)"
        ```
        
        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
        

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Organizr](organizr.md).
