---
hide:
  - tags
tags:
  - dashdot
  - dashboard
  - monitoring
---

# Dashdot

## What is it?

[Dashdot](https://getdashdot.com/) is a simple, modern server dashboard designed with glassmorphism aesthetics, primarily intended for smaller VPS and private servers. It provides real-time system monitoring and beautiful visualizations.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://getdashdot.com/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/MauriceNino/dashdot){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/mauricenino/dashdot){: .header-icons } | [:material-eye: Demo](https://dash.mauz.dev/){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-dashdot
```

### 2. URL

- To access Dashdot, visit `https://dashdot._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    dashdot_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `dashdot_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `dashdot_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`dashdot_name`"

        ```yaml
        # Type: string
        dashdot_name: dashdot
        ```

=== "Settings"

    ??? variable string "`dashdot_role_show_host`"

        ```yaml
        # Type: string
        dashdot_role_show_host: "false"
        ```

    ??? variable string "`dashdot_role_cpu_temps`"

        ```yaml
        # Type: string
        dashdot_role_cpu_temps: "false"
        ```

    ??? variable string "`dashdot_role_imperial`"

        ```yaml
        # Type: string
        dashdot_role_imperial: "false"
        ```

    ??? variable string "`dashdot_role_always_show_percentages`"

        ```yaml
        # Type: string
        dashdot_role_always_show_percentages: "false"
        ```

    ??? variable string "`dashdot_role_title`"

        ```yaml
        # Type: string
        dashdot_role_title: "dash."
        ```

    ??? variable string "`dashdot_role_widget_list`"

        ```yaml
        # Type: string
        dashdot_role_widget_list: "os,cpu,storage,ram,network"
        ```

    ??? variable string "`dashdot_role_os_label_list`"

        ```yaml
        # Type: string
        dashdot_role_os_label_list: "os,arch,up_since"
        ```

    ??? variable string "`dashdot_role_cpu_label_list`"

        ```yaml
        # Type: string
        dashdot_role_cpu_label_list: "brand,model,cores,threads,frequency"
        ```

    ??? variable string "`dashdot_role_storage_label_list`"

        ```yaml
        # Type: string
        dashdot_role_storage_label_list: "brand,size,type"
        ```

    ??? variable string "`dashdot_role_ram_label_list`"

        ```yaml
        # Type: string
        dashdot_role_ram_label_list: "brand,size,type,frequency"
        ```

    ??? variable string "`dashdot_role_network_label_list`"

        ```yaml
        # Type: string
        dashdot_role_network_label_list: "type,speed_up,speed_down,interface_speed"
        ```

    ??? variable string "`dashdot_role_gpu_label_list`"

        ```yaml
        # Type: string
        dashdot_role_gpu_label_list: "brand,model,memory"
        ```

=== "Paths"

    ??? variable string "`dashdot_role_paths_folder`"

        ```yaml
        # Type: string
        dashdot_role_paths_folder: "{{ dashdot_name }}"
        ```

    ??? variable string "`dashdot_role_paths_location`"

        ```yaml
        # Type: string
        dashdot_role_paths_location: "{{ server_appdata_path }}/{{ dashdot_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`dashdot_role_web_subdomain`"

        ```yaml
        # Type: string
        dashdot_role_web_subdomain: "{{ dashdot_name }}"
        ```

    ??? variable string "`dashdot_role_web_domain`"

        ```yaml
        # Type: string
        dashdot_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`dashdot_role_web_port`"

        ```yaml
        # Type: string
        dashdot_role_web_port: "3001"
        ```

    ??? variable string "`dashdot_role_web_url`"

        ```yaml
        # Type: string
        dashdot_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='dashdot') + '.' + lookup('role_var', '_web_domain', role='dashdot')
                               if (lookup('role_var', '_web_subdomain', role='dashdot') | length > 0)
                               else lookup('role_var', '_web_domain', role='dashdot')) }}"
        ```

=== "DNS"

    ??? variable string "`dashdot_role_dns_record`"

        ```yaml
        # Type: string
        dashdot_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dashdot') }}"
        ```

    ??? variable string "`dashdot_role_dns_zone`"

        ```yaml
        # Type: string
        dashdot_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dashdot') }}"
        ```

    ??? variable bool "`dashdot_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`dashdot_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        dashdot_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`dashdot_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        dashdot_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`dashdot_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        dashdot_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`dashdot_role_traefik_certresolver`"

        ```yaml
        # Type: string
        dashdot_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`dashdot_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_enabled: true
        ```

    ??? variable bool "`dashdot_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_api_enabled: false
        ```

    ??? variable string "`dashdot_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        dashdot_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`dashdot_role_docker_container`"

        ```yaml
        # Type: string
        dashdot_role_docker_container: "{{ dashdot_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`dashdot_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_image_pull: true
        ```

    ??? variable string "`dashdot_role_docker_image_repo`"

        ```yaml
        # Type: string
        dashdot_role_docker_image_repo: "mauricenino/dashdot"
        ```

    ??? variable string "`dashdot_role_docker_image_tag`"

        ```yaml
        # Type: string
        dashdot_role_docker_image_tag: "latest"
        ```

    ??? variable string "`dashdot_role_docker_image`"

        ```yaml
        # Type: string
        dashdot_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dashdot') }}:{{ lookup('role_var', '_docker_image_tag', role='dashdot') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`dashdot_role_docker_envs_default`"

        ```yaml
        # Type: dict
        dashdot_role_docker_envs_default: 
          DASHDOT_SHOW_HOST: "{{ lookup('role_var', '_show_host', role='dashdot') }}"
          DASHDOT_CUSTOM_HOST: "{{ lookup('role_var', '_web_subdomain', role='dashdot') + '.' + lookup('role_var', '_web_domain', role='dashdot') }}"
          DASHDOT_ENABLE_CPU_TEMPS: "{{ lookup('role_var', '_cpu_temps', role='dashdot') }}"
          DASHDOT_USE_IMPERIAL: "{{ lookup('role_var', '_imperial', role='dashdot') }}"
          DASHDOT_ALWAYS_SHOW_PERCENTAGES: "{{ lookup('role_var', '_always_show_percentages', role='dashdot') }}"
          DASHDOT_PAGE_TITLE: "{{ lookup('role_var', '_title', role='dashdot') }}"
          DASHDOT_WIDGET_LIST: "{{ lookup('role_var', '_widget_list', role='dashdot') }}"
          DASHDOT_OS_LABEL_LIST: "{{ lookup('role_var', '_os_label_list', role='dashdot') }}"
          DASHDOT_CPU_LABEL_LIST: "{{ lookup('role_var', '_cpu_label_list', role='dashdot') }}"
          DASHDOT_STORAGE_LABEL_LIST: "{{ lookup('role_var', '_storage_label_list', role='dashdot') }}"
          DASHDOT_RAM_LABEL_LIST: "{{ lookup('role_var', '_ram_label_list', role='dashdot') }}"
          DASHDOT_NETWORK_LABEL_LIST: "{{ lookup('role_var', '_network_label_list', role='dashdot') }}"
          DASHDOT_GPU_LABEL_LIST: "{{ lookup('role_var', '_gpu_label_list', role='dashdot') }}"
          DASHDOT_ACCEPT_OOKLA_EULA: "true"
        ```

    ??? variable dict "`dashdot_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        dashdot_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`dashdot_role_docker_volumes_default`"

        ```yaml
        # Type: list
        dashdot_role_docker_volumes_default: 
          - "/:/mnt/host:ro"
        ```

    ??? variable list "`dashdot_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        dashdot_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`dashdot_role_docker_hostname`"

        ```yaml
        # Type: string
        dashdot_role_docker_hostname: "{{ dashdot_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`dashdot_role_docker_networks_alias`"

        ```yaml
        # Type: string
        dashdot_role_docker_networks_alias: "{{ dashdot_name }}"
        ```

    ??? variable list "`dashdot_role_docker_networks_default`"

        ```yaml
        # Type: list
        dashdot_role_docker_networks_default: []
        ```

    ??? variable list "`dashdot_role_docker_networks_custom`"

        ```yaml
        # Type: list
        dashdot_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`dashdot_role_docker_restart_policy`"

        ```yaml
        # Type: string
        dashdot_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`dashdot_role_docker_state`"

        ```yaml
        # Type: string
        dashdot_role_docker_state: started
        ```

    Privileged
    { .sb-h5 }

    ??? variable bool "`dashdot_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_privileged: true
        ```

=== "Global Override Options"

    ??? variable bool "`dashdot_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        dashdot_role_autoheal_enabled: true
        ```

    ??? variable string "`dashdot_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        dashdot_role_depends_on: ""
        ```

    ??? variable string "`dashdot_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        dashdot_role_depends_on_delay: "0"
        ```

    ??? variable string "`dashdot_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        dashdot_role_depends_on_healthchecks:
        ```

    ??? variable bool "`dashdot_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        dashdot_role_diun_enabled: true
        ```

    ??? variable bool "`dashdot_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        dashdot_role_dns_enabled: true
        ```

    ??? variable bool "`dashdot_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        dashdot_role_docker_controller: true
        ```

    ??? variable bool "`dashdot_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`dashdot_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`dashdot_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`dashdot_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        dashdot_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        dashdot_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`dashdot_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        dashdot_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            dashdot_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "dashdot2.{{ user.domain }}"
              - "dashdot.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`dashdot_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        dashdot_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            dashdot_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dashdot2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`dashdot_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        dashdot_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->