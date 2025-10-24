---
hide:
  - tags
tags:
  - reposilite
  - development
  - repository
---

# reposilite

## What is it?

[reposilite](https://reposilite.com/) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://reposilite.com/){: .header-icons } | [:octicons-link-16: Docs](https://reposilite.com/guide/about){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/dzikoysk/reposilite){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/dzikoysk/reposilite){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-reposilite

```

### 2. URL

- To access reposilite, visit `https://reposilite._yourdomain.com_`

### 3. Usage

- Consult [the doc](https://reposilite.com/guide/docker)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    reposilite_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `reposilite_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `reposilite_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`reposilite_name`"

        ```yaml
        # Type: string
        reposilite_name: reposilite
        ```

=== "Paths"

    ??? variable string "`reposilite_role_paths_folder`"

        ```yaml
        # Type: string
        reposilite_role_paths_folder: "{{ reposilite_name }}"
        ```

    ??? variable string "`reposilite_role_paths_location`"

        ```yaml
        # Type: string
        reposilite_role_paths_location: "{{ server_appdata_path }}/{{ reposilite_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`reposilite_role_web_subdomain`"

        ```yaml
        # Type: string
        reposilite_role_web_subdomain: "{{ reposilite_name }}"
        ```

    ??? variable string "`reposilite_role_web_domain`"

        ```yaml
        # Type: string
        reposilite_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`reposilite_role_web_port`"

        ```yaml
        # Type: string
        reposilite_role_web_port: "8080"
        ```

    ??? variable string "`reposilite_role_web_url`"

        ```yaml
        # Type: string
        reposilite_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='reposilite') + '.' + lookup('role_var', '_web_domain', role='reposilite')
                                  if (lookup('role_var', '_web_subdomain', role='reposilite') | length > 0)
                                  else lookup('role_var', '_web_domain', role='reposilite')) }}"
        ```

=== "DNS"

    ??? variable string "`reposilite_role_dns_record`"

        ```yaml
        # Type: string
        reposilite_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='reposilite') }}"
        ```

    ??? variable string "`reposilite_role_dns_zone`"

        ```yaml
        # Type: string
        reposilite_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='reposilite') }}"
        ```

    ??? variable bool "`reposilite_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`reposilite_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        reposilite_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`reposilite_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        reposilite_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`reposilite_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        reposilite_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`reposilite_role_traefik_certresolver`"

        ```yaml
        # Type: string
        reposilite_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`reposilite_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_enabled: true
        ```

    ??? variable bool "`reposilite_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_api_enabled: true
        ```

    ??? variable string "`reposilite_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        reposilite_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`reposilite_role_docker_container`"

        ```yaml
        # Type: string
        reposilite_role_docker_container: "{{ reposilite_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`reposilite_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_image_pull: true
        ```

    ??? variable string "`reposilite_role_docker_image_repo`"

        ```yaml
        # Type: string
        reposilite_role_docker_image_repo: "ghcr.io/dzikoysk/reposilite"
        ```

    ??? variable string "`reposilite_role_docker_image_tag`"

        ```yaml
        # Type: string
        reposilite_role_docker_image_tag: "latest"
        ```

    ??? variable string "`reposilite_role_docker_image`"

        ```yaml
        # Type: string
        reposilite_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='reposilite') }}:{{ lookup('role_var', '_docker_image_tag', role='reposilite') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`reposilite_role_docker_envs_default`"

        ```yaml
        # Type: dict
        reposilite_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          REPOSILITE_OPTS: "--token {{ user.name }}:{{ user.pass }}"
        ```

    ??? variable dict "`reposilite_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        reposilite_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`reposilite_role_docker_volumes_default`"

        ```yaml
        # Type: list
        reposilite_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='reposilite') }}:/app/data"
        ```

    ??? variable list "`reposilite_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        reposilite_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`reposilite_role_docker_hostname`"

        ```yaml
        # Type: string
        reposilite_role_docker_hostname: "{{ reposilite_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`reposilite_role_docker_networks_alias`"

        ```yaml
        # Type: string
        reposilite_role_docker_networks_alias: "{{ reposilite_name }}"
        ```

    ??? variable list "`reposilite_role_docker_networks_default`"

        ```yaml
        # Type: list
        reposilite_role_docker_networks_default: []
        ```

    ??? variable list "`reposilite_role_docker_networks_custom`"

        ```yaml
        # Type: list
        reposilite_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`reposilite_role_docker_restart_policy`"

        ```yaml
        # Type: string
        reposilite_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`reposilite_role_docker_state`"

        ```yaml
        # Type: string
        reposilite_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`reposilite_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        reposilite_role_autoheal_enabled: true
        ```

    ??? variable string "`reposilite_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        reposilite_role_depends_on: ""
        ```

    ??? variable string "`reposilite_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        reposilite_role_depends_on_delay: "0"
        ```

    ??? variable string "`reposilite_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        reposilite_role_depends_on_healthchecks:
        ```

    ??? variable bool "`reposilite_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        reposilite_role_diun_enabled: true
        ```

    ??? variable bool "`reposilite_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        reposilite_role_dns_enabled: true
        ```

    ??? variable bool "`reposilite_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        reposilite_role_docker_controller: true
        ```

    ??? variable bool "`reposilite_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`reposilite_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`reposilite_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`reposilite_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        reposilite_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        reposilite_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`reposilite_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        reposilite_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            reposilite_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "reposilite2.{{ user.domain }}"
              - "reposilite.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`reposilite_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        reposilite_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            reposilite_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'reposilite2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`reposilite_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        reposilite_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->