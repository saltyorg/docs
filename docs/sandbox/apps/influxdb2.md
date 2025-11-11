---
icon: material/docker
hide:
  - tags
tags:
  - influxdb2
  - database
  - timeseries
---

# InfluxDB2

## Overview

[InfluxDB2](https://www.influxdata.com/products/influxdb/) is an open source time series database for recording metrics, events, and analytics.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.influxdata.com/products/influxdb/){: .header-icons } | [:octicons-link-16: Docs](https://docs.influxdata.com/influxdb/latest/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/influxdata/influxdata-docker){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/influxdb){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-influxdb2

```

### 2. URL

- To access InfluxDB2, visit <https://influxdb2.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- To setup the initial admin user, token and bucket, visit the UI at the URL above.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `influxdb2_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of influxdb2:" }
    influxdb2_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `influxdb22`):" }
    influxdb22_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `influxdb2_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `influxdb2_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`influxdb2_instances`"

        ```yaml
        # Type: list
        influxdb2_instances: ["influxdb2"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            influxdb2_instances: ["influxdb2", "influxdb22"]
            ```

=== "Paths"

    ??? variable string "`influxdb2_role_paths_folder`{ .sb-show-on-unchecked }`influxdb22_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_paths_folder: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_paths_folder: "{{ influxdb2_name }}"
        ```

    ??? variable string "`influxdb2_role_paths_location`{ .sb-show-on-unchecked }`influxdb22_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`influxdb2_role_web_subdomain`{ .sb-show-on-unchecked }`influxdb22_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_subdomain: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_subdomain: "{{ influxdb2_name }}"
        ```

    ??? variable string "`influxdb2_role_web_domain`{ .sb-show-on-unchecked }`influxdb22_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`influxdb2_role_web_port`{ .sb-show-on-unchecked }`influxdb22_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_port: "8086"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_port: "8086"
        ```

    ??? variable string "`influxdb2_role_web_url`{ .sb-show-on-unchecked }`influxdb22_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                                 if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                                 else lookup('role_var', '_web_domain', role='influxdb2')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                             if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                             else lookup('role_var', '_web_domain', role='influxdb2')) }}"
        ```

=== "DNS"

    ??? variable string "`influxdb2_role_dns_record`{ .sb-show-on-unchecked }`influxdb22_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"
        ```

    ??? variable string "`influxdb2_role_dns_zone`{ .sb-show-on-unchecked }`influxdb22_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"
        ```

    ??? variable bool "`influxdb2_role_dns_proxy`{ .sb-show-on-unchecked }`influxdb22_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`influxdb2_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`influxdb22_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`influxdb2_role_traefik_middleware_default`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`influxdb2_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_middleware_custom: ""
        ```

    ??? variable string "`influxdb2_role_traefik_certresolver`{ .sb-show-on-unchecked }`influxdb22_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`influxdb2_role_traefik_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_enabled: true
        ```

    ??? variable bool "`influxdb2_role_traefik_api_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_api_enabled: false
        ```

    ??? variable string "`influxdb2_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`influxdb22_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`influxdb2_role_docker_container`{ .sb-show-on-unchecked }`influxdb22_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_container: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_container: "{{ influxdb2_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`influxdb2_role_docker_image_pull`{ .sb-show-on-unchecked }`influxdb22_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_image_pull: true
        ```

    ??? variable string "`influxdb2_role_docker_image_tag`{ .sb-show-on-unchecked }`influxdb22_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image_tag: "2-alpine"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image_tag: "2-alpine"
        ```

    ??? variable string "`influxdb2_role_docker_image_repo`{ .sb-show-on-unchecked }`influxdb22_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image_repo: "influxdb"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image_repo: "influxdb"
        ```

    ??? variable string "`influxdb2_role_docker_image`{ .sb-show-on-unchecked }`influxdb22_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`influxdb2_role_docker_volumes_default`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"
        ```

    ??? variable list "`influxdb2_role_docker_volumes_custom`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`influxdb2_role_docker_hostname`{ .sb-show-on-unchecked }`influxdb22_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_hostname: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_hostname: "{{ influxdb2_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`influxdb2_role_docker_networks_alias`{ .sb-show-on-unchecked }`influxdb22_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_networks_alias: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_networks_alias: "{{ influxdb2_name }}"
        ```

    ??? variable list "`influxdb2_role_docker_networks_default`{ .sb-show-on-unchecked }`influxdb22_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_networks_default: []
        ```

    ??? variable list "`influxdb2_role_docker_networks_custom`{ .sb-show-on-unchecked }`influxdb22_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`influxdb2_role_docker_restart_policy`{ .sb-show-on-unchecked }`influxdb22_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`influxdb2_role_docker_state`{ .sb-show-on-unchecked }`influxdb22_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`influxdb2_role_autoheal_enabled`{ .sb-show-on-unchecked }`influxdb22_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        influxdb2_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        influxdb22_autoheal_enabled: true
        ```

    ??? variable string "`influxdb2_role_depends_on`{ .sb-show-on-unchecked }`influxdb22_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        influxdb2_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        influxdb22_depends_on: ""
        ```

    ??? variable string "`influxdb2_role_depends_on_delay`{ .sb-show-on-unchecked }`influxdb22_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        influxdb2_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        influxdb22_depends_on_delay: "0"
        ```

    ??? variable string "`influxdb2_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`influxdb22_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb2_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb22_depends_on_healthchecks:
        ```

    ??? variable bool "`influxdb2_role_diun_enabled`{ .sb-show-on-unchecked }`influxdb22_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        influxdb2_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        influxdb22_diun_enabled: true
        ```

    ??? variable bool "`influxdb2_role_dns_enabled`{ .sb-show-on-unchecked }`influxdb22_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        influxdb2_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        influxdb22_dns_enabled: true
        ```

    ??? variable bool "`influxdb2_role_docker_controller`{ .sb-show-on-unchecked }`influxdb22_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        influxdb2_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        influxdb22_docker_controller: true
        ```

    ??? variable bool "`influxdb2_role_docker_volumes_download`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_volumes_download:
        ```

    ??? variable bool "`influxdb2_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_gzip_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`influxdb2_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`influxdb2_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_robot_enabled: true
        ```

    ??? variable bool "`influxdb2_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        influxdb22_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        influxdb22_traefik_wildcard_enabled: true
        ```

    ??? variable list "`influxdb2_role_web_fqdn_override`{ .sb-show-on-unchecked }`influxdb22_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        influxdb2_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        influxdb22_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            influxdb2_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "influxdb22.{{ user.domain }}"
              - "influxdb2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            influxdb22_web_fqdn_override:
              - "{{ traefik_host }}"
              - "influxdb22.{{ user.domain }}"
              - "influxdb2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`influxdb2_role_web_host_override`{ .sb-show-on-unchecked }`influxdb22_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        influxdb2_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        influxdb22_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            influxdb2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            influxdb22_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`influxdb2_role_web_scheme`{ .sb-show-on-unchecked }`influxdb22_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        influxdb2_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        influxdb22_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->