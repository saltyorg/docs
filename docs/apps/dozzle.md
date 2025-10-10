---
hide:
  - tags
tags:
  - dozzle
---

# Dozzle

## What is it?

[Dozzle](https://dozzle.dev/) is a small lightweight application with a web based interface to monitor Docker logs. It doesn’t store any log files. It is for live monitoring of your container logs only. Dozzle can only access logs written to stdout or stderr which is the same functionality as the `docker logs` command. See below for more info on that.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://dozzle.dev/){: .header-icons } | [:octicons-link-16: Docs](https://dozzle.dev/guide/what-is-dozzle){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/amir20/dozzle){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/amir20/dozzle){: .header-icons }|

### 1. Installation

``` shell

sb install dozzle

```

### 2. URL

- To access Dozzle, visit `https://dozzle._yourdomain.com_`

### 3. Setup

To view log files that are NOT written to stdout or stderr, use the following to setup a basic Alpine Linux container via Docker Compose that just tails a mounted log file (in this case, Cloudplow) which then exposes it to Dozzle. Adjust as needed for your circumstances.

``` yaml
  tail-cloudplow: # (1)!
    container_name: tail-cloudplow # (2)!
    image: alpine
    volumes:
      - /opt/cloudplow/cloudplow.log:/opt/cloudplow/cloudplow.log:ro # (3)!
    command:
      - tail
      - -F
      - /opt/cloudplow/cloudplow.log # (4)!
    network_mode: none
    restart: unless-stopped
    user: 1000:1000 # (5)!
```

1. You can pick any name for the container, but it is recommended to pick a memorable name that you will recognize in the Dozzle menu.
2. You can pick any name for the container, but it is recommended to pick a memorable name that you will recognize in the Dozzle menu.
3. The volume mount for the log file. This takes the format of `/host/path/to.log:/container/path/to.log:ro`. The `:ro` suffix is optional but recommended to give this container only read-only access to the log file.
4. The path inside of the container where the log file is accessible. This must be the same in the `volumes` section above and this `command` section. Matching the annotation example, this would be `/container/path/to.log`.
5. Provide your `uid:gid` if they are different. You can check these values by running the `id` command.

???+ note
    To get the container running, follow our docs on starting a docker container here; [Your Own Containers](../advanced/your-own-containers.md#creating-and-running-the-container).

### 4. Adding Additional Hosts

You can add additional hosts to Dozzle using the `dozzle_additional_hosts` inventory variable. This will append the additional host(s) to the default entry. You can review the upstream documentation [here](https://dozzle.dev/guide/remote-hosts) for the proper syntax. The initiai `,` will be added after the default entry, you must comma separate the hosts if you are adding multiple entries such as:

```yaml
dozzle_additional_hosts: "tcp://otherserver:2375|otherserver,tcp://thirdserver:2375|thirdserver"
```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        dozzle_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    dozzle_name: dozzle

    ```

??? example "Docker Socket Proxy"

    ```yaml
    # Type: dict
    dozzle_docker_socket_proxy_envs: 
      CONTAINERS: "1"
      INFO: "1"

    ```

??? example "Settings"

    ```yaml
    # Type: string
    dozzle_role_additional_hosts: ""

    # Type: string
    dozzle_role_agent_hosts: ""

    # Type: bool (true/false)
    dozzle_role_agent_mode: false

    ```

??? example "Paths"

    ```yaml
    # Type: string
    dozzle_role_paths_folder: "{{ dozzle_name }}"

    # Type: string
    dozzle_role_paths_location: "{{ server_appdata_path }}/{{ dozzle_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    dozzle_role_web_subdomain: "{{ dozzle_name }}"

    # Type: string
    dozzle_role_web_domain: "{{ user.domain }}"

    # Type: string
    dozzle_role_web_port: "8080"

    # Type: string
    dozzle_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='dozzle') + '.' + lookup('role_var', '_web_domain', role='dozzle')
                          if (lookup('role_var', '_web_subdomain', role='dozzle') | length > 0)
                          else lookup('role_var', '_web_domain', role='dozzle')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    dozzle_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dozzle') }}"

    # Type: string
    dozzle_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dozzle') }}"

    # Type: bool (true/false)
    dozzle_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    dozzle_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    dozzle_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                + (',dropsecurityheaders@file,themepark-' + dozzle_name
                                                  if (lookup('role_var', '_themepark_enabled', role='dozzle') and global_themepark_plugin_enabled)
                                                  else '') }}"

    # Type: string
    dozzle_role_traefik_middleware_custom: ""

    # Type: string
    dozzle_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    dozzle_role_traefik_enabled: true

    # Type: bool (true/false)
    dozzle_role_traefik_api_enabled: false

    # Type: string
    dozzle_role_traefik_api_endpoint: ""

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    dozzle_role_themepark_enabled: false

    # Type: string
    dozzle_role_themepark_app: "dozzle"

    # Type: string
    dozzle_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    dozzle_role_themepark_domain: "{{ global_themepark_domain }}"

    # Type: list
    dozzle_role_themepark_addons: []

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    dozzle_role_docker_container: "{{ dozzle_name }}"

    # Image
    # Type: bool (true/false)
    dozzle_role_docker_image_pull: true

    # Type: string
    dozzle_role_docker_image_repo: "amir20/dozzle"

    # Type: string
    dozzle_role_docker_image_tag: "latest"

    # Type: string
    dozzle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dozzle') }}:{{ lookup('role_var', '_docker_image_tag', role='dozzle') }}"

    # Envs
    # Type: dict
    dozzle_role_docker_envs_default: 
      DOZZLE_AUTH_PROVIDER: "{{ 'forward-proxy' if (lookup('role_var', '_traefik_sso_middleware', role='dozzle') | length > 0) else omit }}"
      DOZZLE_REMOTE_AGENT: "{{ lookup('role_var', '_agent_hosts', role='dozzle') if (lookup('role_var', '_additional_hosts', role='dozzle') | length > 0) else omit }}"
      DOZZLE_REMOTE_HOST: "{{ 'tcp://' + dozzle_name + '-docker-socket-proxy:2375|' + traefik_host + ',' + lookup('role_var', '_additional_hosts', role='dozzle')
                           if (lookup('role_var', '_additional_hosts', role='dozzle') | length > 0)
                           else 'tcp://' + dozzle_name + '-docker-socket-proxy:2375|' + traefik_host }}"
      DOZZLE_AUTH_HEADER_USER: "{{ 'X-authentik-username' if 'authentik' in lookup('role_var', '_traefik_sso_middleware', role='dozzle') else omit }}"
      DOZZLE_AUTH_HEADER_EMAIL: "{{ 'X-authentik-email' if 'authentik' in lookup('role_var', '_traefik_sso_middleware', role='dozzle') else omit }}"
      DOZZLE_AUTH_HEADER_NAME: "{{ 'X-authentik-name' if 'authentik' in lookup('role_var', '_traefik_sso_middleware', role='dozzle') else omit }}"

    # Type: dict
    dozzle_role_docker_envs_custom: {}

    # Commands
    # Type: string
    dozzle_role_docker_commands_agent: "agent"

    # Type: list
    dozzle_role_docker_commands_default: []

    # Type: list
    dozzle_role_docker_commands_custom: []

    # Labels
    # Type: dict
    dozzle_role_docker_labels_default: {}

    # Type: dict
    dozzle_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    dozzle_role_docker_hostname: "{{ dozzle_name }}"

    # Networks
    # Type: string
    dozzle_role_docker_networks_alias: "{{ dozzle_name }}"

    # Type: list
    dozzle_role_docker_networks_default: []

    # Type: list
    dozzle_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    dozzle_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    dozzle_role_docker_state: started

    # Dependencies
    # Type: string
    dozzle_role_depends_on: "{{ dozzle_name }}-docker-socket-proxy"

    # Type: string
    dozzle_role_depends_on_delay: "0"

    # Type: string
    dozzle_role_depends_on_healthchecks: "false"


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    dozzle_role_docker_blkio_weight:

    # Type: int
    dozzle_role_docker_cpu_period:

    # Type: int
    dozzle_role_docker_cpu_quota:

    # Type: int
    dozzle_role_docker_cpu_shares:

    # Type: string
    dozzle_role_docker_cpus:

    # Type: string
    dozzle_role_docker_cpuset_cpus:

    # Type: string
    dozzle_role_docker_cpuset_mems:

    # Type: string
    dozzle_role_docker_kernel_memory:

    # Type: string
    dozzle_role_docker_memory:

    # Type: string
    dozzle_role_docker_memory_reservation:

    # Type: string
    dozzle_role_docker_memory_swap:

    # Type: int
    dozzle_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    dozzle_role_docker_cap_drop:

    # Type: list
    dozzle_role_docker_device_cgroup_rules:

    # Type: list
    dozzle_role_docker_device_read_bps:

    # Type: list
    dozzle_role_docker_device_read_iops:

    # Type: list
    dozzle_role_docker_device_requests:

    # Type: list
    dozzle_role_docker_device_write_bps:

    # Type: list
    dozzle_role_docker_device_write_iops:

    # Type: list
    dozzle_role_docker_devices:

    # Type: string
    dozzle_role_docker_devices_default:

    # Type: bool (true/false)
    dozzle_role_docker_privileged:

    # Type: list
    dozzle_role_docker_security_opts:


    # Networking
    # Type: list
    dozzle_role_docker_dns_opts:

    # Type: list
    dozzle_role_docker_dns_search_domains:

    # Type: list
    dozzle_role_docker_dns_servers:

    # Type: dict
    dozzle_role_docker_hosts:

    # Type: string
    dozzle_role_docker_hosts_use_common:

    # Type: string
    dozzle_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    dozzle_role_docker_keep_volumes:

    # Type: list
    dozzle_role_docker_mounts:

    # Type: string
    dozzle_role_docker_volume_driver:

    # Type: list
    dozzle_role_docker_volumes:

    # Type: list
    dozzle_role_docker_volumes_from:

    # Type: string
    dozzle_role_docker_volumes_global:

    # Type: string
    dozzle_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    dozzle_role_docker_healthcheck:

    # Type: bool (true/false)
    dozzle_role_docker_init:

    # Type: string
    dozzle_role_docker_log_driver:

    # Type: dict
    dozzle_role_docker_log_options:

    # Type: bool (true/false)
    dozzle_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    dozzle_role_docker_auto_remove:

    # Type: list
    dozzle_role_docker_capabilities:

    # Type: string
    dozzle_role_docker_cgroup_parent:

    # Type: string
    dozzle_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    dozzle_role_docker_cleanup:

    # Type: string
    dozzle_role_docker_create_timeout:

    # Type: string
    dozzle_role_docker_domainname:

    # Type: string
    dozzle_role_docker_entrypoint:

    # Type: string
    dozzle_role_docker_env_file:

    # Type: list
    dozzle_role_docker_exposed_ports:

    # Type: string
    dozzle_role_docker_force_kill:

    # Type: list
    dozzle_role_docker_groups:

    # Type: int
    dozzle_role_docker_healthy_wait_timeout:

    # Type: string
    dozzle_role_docker_ipc_mode:

    # Type: string
    dozzle_role_docker_kill_signal:

    # Type: string
    dozzle_role_docker_labels_use_common:

    # Type: list
    dozzle_role_docker_links:

    # Type: bool (true/false)
    dozzle_role_docker_oom_killer:

    # Type: int
    dozzle_role_docker_oom_score_adj:

    # Type: bool (true/false)
    dozzle_role_docker_paused:

    # Type: string
    dozzle_role_docker_pid_mode:

    # Type: list
    dozzle_role_docker_ports:

    # Type: bool (true/false)
    dozzle_role_docker_read_only:

    # Type: bool (true/false)
    dozzle_role_docker_recreate:

    # Type: int
    dozzle_role_docker_restart_retries:

    # Type: string
    dozzle_role_docker_runtime:

    # Type: string
    dozzle_role_docker_shm_size:

    # Type: int
    dozzle_role_docker_stop_timeout:

    # Type: dict
    dozzle_role_docker_storage_opts:

    # Type: list
    dozzle_role_docker_sysctls:

    # Type: list
    dozzle_role_docker_tmpfs:

    # Type: list
    dozzle_role_docker_ulimits:

    # Type: string
    dozzle_role_docker_user:

    # Type: string
    dozzle_role_docker_userns_mode:

    # Type: string
    dozzle_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    dozzle_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    dozzle_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    dozzle_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    dozzle_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    dozzle_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    dozzle_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    dozzle_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    dozzle_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    dozzle_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    dozzle_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    dozzle_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    dozzle_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    dozzle_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    dozzle_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    dozzle_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    dozzle_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    dozzle_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        dozzle_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "dozzle2.{{ user.domain }}"
          - "dozzle.otherdomain.tld"
        ```
        
        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
        

    2.  Example:

        ```yaml
        dozzle_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dozzle2.' + user.domain }}`)"
        ```
        
        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
        

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
