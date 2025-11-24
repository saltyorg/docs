---
icon: material/docker
hide:
  - tags
tags:
  - telegraf
  - monitoring
  - metrics
---

# Telegraf

## Overview

[Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) is a plugin-driven server agent for collecting and sending metrics and events from databases, systems, and IoT sensors.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.influxdata.com/time-series-platform/telegraf/){: .header-icons } | [:octicons-link-16: Docs](https://docs.influxdata.com/telegraf/v1.20/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/influxdata/telegraf){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/telegraf){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-telegraf
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `telegraf_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of telegraf:" }
    telegraf_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `telegraf2`):" }
    telegraf2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `telegraf_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `telegraf_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`telegraf_instances`"

        ```yaml
        # Type: list
        telegraf_instances: ["telegraf"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            telegraf_instances: ["telegraf", "telegraf2"]
            ```

=== "Paths"

    ??? variable string "`telegraf_role_paths_folder`{ .sb-show-on-unchecked }`telegraf2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_paths_folder: "telegraf"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_paths_folder: "telegraf"
        ```

    ??? variable string "`telegraf_role_paths_location`{ .sb-show-on-unchecked }`telegraf2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_paths_location: "{{ server_appdata_path }}/{{ telegraf_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_paths_location: "{{ server_appdata_path }}/{{ telegraf_role_paths_folder }}"
        ```

    ??? variable bool "`telegraf_role_paths_recursive`{ .sb-show-on-unchecked }`telegraf2_paths_recursive`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_paths_recursive: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_paths_recursive: true
        ```

=== "Web"

    ??? variable string "`telegraf_role_web_subdomain`{ .sb-show-on-unchecked }`telegraf2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_web_subdomain: "{{ telegraf_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_web_subdomain: "{{ telegraf_name }}"
        ```

    ??? variable string "`telegraf_role_web_domain`{ .sb-show-on-unchecked }`telegraf2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_web_domain: "{{ user.domain }}"
        ```

=== "DNS"

    ??? variable string "`telegraf_role_dns_record`{ .sb-show-on-unchecked }`telegraf2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='telegraf') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='telegraf') }}"
        ```

    ??? variable string "`telegraf_role_dns_zone`{ .sb-show-on-unchecked }`telegraf2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='telegraf') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_dns_zone: "{{ lookup('role_var', '_web_domain', role='telegraf') }}"
        ```

    ??? variable bool "`telegraf_role_dns_proxy`{ .sb-show-on-unchecked }`telegraf2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_dns_proxy: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_dns_proxy: false
        ```

=== "Traefik"

    ??? variable string "`telegraf_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`telegraf2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`telegraf_role_traefik_middleware_default`{ .sb-show-on-unchecked }`telegraf2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`telegraf_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`telegraf2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_traefik_middleware_custom: ""
        ```

    ??? variable string "`telegraf_role_traefik_certresolver`{ .sb-show-on-unchecked }`telegraf2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`telegraf_role_traefik_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_traefik_enabled: true
        ```

    ??? variable bool "`telegraf_role_traefik_api_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_traefik_api_enabled: false
        ```

    ??? variable string "`telegraf_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`telegraf2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`telegraf_role_docker_container`{ .sb-show-on-unchecked }`telegraf2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_container: "{{ telegraf_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_container: "{{ telegraf_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`telegraf_role_docker_image_pull`{ .sb-show-on-unchecked }`telegraf2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_docker_image_pull: true
        ```

    ??? variable string "`telegraf_role_docker_image_repo`{ .sb-show-on-unchecked }`telegraf2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_image_repo: "telegraf"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_image_repo: "telegraf"
        ```

    ??? variable string "`telegraf_role_docker_image_tag`{ .sb-show-on-unchecked }`telegraf2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_image_tag: "latest"
        ```

    ??? variable string "`telegraf_role_docker_image`{ .sb-show-on-unchecked }`telegraf2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='telegraf') }}:{{ lookup('role_var', '_docker_image_tag', role='telegraf') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='telegraf') }}:{{ lookup('role_var', '_docker_image_tag', role='telegraf') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`telegraf_role_docker_envs_default`{ .sb-show-on-unchecked }`telegraf2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        telegraf_role_docker_envs_default:
          TZ: "{{ tz }}"
          EULA: "TRUE"
          UID: "{{ uid }}"
          GID: "{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        telegraf2_docker_envs_default:
          TZ: "{{ tz }}"
          EULA: "TRUE"
          UID: "{{ uid }}"
          GID: "{{ gid }}"
        ```

    ??? variable dict "`telegraf_role_docker_envs_custom`{ .sb-show-on-unchecked }`telegraf2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        telegraf_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        telegraf2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`telegraf_role_docker_volumes_default`{ .sb-show-on-unchecked }`telegraf2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        telegraf_role_docker_volumes_default:
          - "{{ server_appdata_path }}/telegraf/{{ telegraf_name }}:/etc/telegraf:ro"
          - "/var/run/docker.sock:/var/run/docker.sock:ro"
          - "/var/run/utmp:/var/run/utmp"
          - "/:/host:ro"
          - "/sys:/host/sys:ro"
          - "/proc:/host/proc:ro"
          - "/etc:/host/etc:ro"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        telegraf2_docker_volumes_default:
          - "{{ server_appdata_path }}/telegraf/{{ telegraf_name }}:/etc/telegraf:ro"
          - "/var/run/docker.sock:/var/run/docker.sock:ro"
          - "/var/run/utmp:/var/run/utmp"
          - "/:/host:ro"
          - "/sys:/host/sys:ro"
          - "/proc:/host/proc:ro"
          - "/etc:/host/etc:ro"
        ```

    ??? variable list "`telegraf_role_docker_volumes_custom`{ .sb-show-on-unchecked }`telegraf2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        telegraf_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        telegraf2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`telegraf_role_docker_hostname`{ .sb-show-on-unchecked }`telegraf2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_hostname: "{{ telegraf_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_hostname: "{{ telegraf_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`telegraf_role_docker_networks_alias`{ .sb-show-on-unchecked }`telegraf2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_networks_alias: "{{ telegraf_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_networks_alias: "{{ telegraf_name }}"
        ```

    ??? variable list "`telegraf_role_docker_networks_default`{ .sb-show-on-unchecked }`telegraf2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        telegraf_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        telegraf2_docker_networks_default: []
        ```

    ??? variable list "`telegraf_role_docker_networks_custom`{ .sb-show-on-unchecked }`telegraf2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        telegraf_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        telegraf2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`telegraf_role_docker_restart_policy`{ .sb-show-on-unchecked }`telegraf2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`telegraf_role_docker_state`{ .sb-show-on-unchecked }`telegraf2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        telegraf_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        telegraf2_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`telegraf_role_autoheal_enabled`{ .sb-show-on-unchecked }`telegraf2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        telegraf_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        telegraf2_autoheal_enabled: true
        ```

    ??? variable string "`telegraf_role_depends_on`{ .sb-show-on-unchecked }`telegraf2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        telegraf_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        telegraf2_depends_on: ""
        ```

    ??? variable string "`telegraf_role_depends_on_delay`{ .sb-show-on-unchecked }`telegraf2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        telegraf_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        telegraf2_depends_on_delay: "0"
        ```

    ??? variable string "`telegraf_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`telegraf2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        telegraf_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        telegraf2_depends_on_healthchecks:
        ```

    ??? variable bool "`telegraf_role_diun_enabled`{ .sb-show-on-unchecked }`telegraf2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        telegraf_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        telegraf2_diun_enabled: true
        ```

    ??? variable bool "`telegraf_role_dns_enabled`{ .sb-show-on-unchecked }`telegraf2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        telegraf_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        telegraf2_dns_enabled: true
        ```

    ??? variable bool "`telegraf_role_docker_controller`{ .sb-show-on-unchecked }`telegraf2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        telegraf_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        telegraf2_docker_controller: true
        ```

    ??? variable bool "`telegraf_role_docker_volumes_download`{ .sb-show-on-unchecked }`telegraf2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_docker_volumes_download:
        ```

    ??? variable bool "`telegraf_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        telegraf2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`telegraf_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        telegraf2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`telegraf_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        telegraf2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`telegraf_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        telegraf2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`telegraf_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`telegraf2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`telegraf_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`telegraf2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        telegraf_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        telegraf2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`telegraf_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        telegraf2_traefik_robot_enabled: true
        ```

    ??? variable bool "`telegraf_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        telegraf_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        telegraf2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`telegraf_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`telegraf2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        telegraf_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        telegraf2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`telegraf_role_web_fqdn_override`{ .sb-show-on-unchecked }`telegraf2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        telegraf_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        telegraf2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            telegraf_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "telegraf2.{{ user.domain }}"
              - "telegraf.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            telegraf2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "telegraf2.{{ user.domain }}"
              - "telegraf.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`telegraf_role_web_host_override`{ .sb-show-on-unchecked }`telegraf2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        telegraf_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        telegraf2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            telegraf_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'telegraf2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            telegraf2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'telegraf2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`telegraf_role_web_scheme`{ .sb-show-on-unchecked }`telegraf2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        telegraf_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        telegraf2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->