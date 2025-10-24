---
hide:
  - tags
tags:
  - archivebox
  - archiving
  - web
---

# ArchiveBox

## What is it?

[ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) is a powerful, self-hosted internet archiving solution to collect, save, and view sites you want to preserve offline.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/ArchiveBox/ArchiveBox){: .header-icons } | [:octicons-link-16: Docs](https://github.com/ArchiveBox/ArchiveBox/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ArchiveBox/ArchiveBox){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/archivebox/archivebox){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-archivebox

```

### 2. URL

- To access ArchiveBox, visit `https://archivebox._yourdomain.com_`

### 3. Setup

Initial setup guide thanks to `erisheaded` on CB discord.

1. Run tag:

    ``` { .shell }
    sb install sandbox-archivebox
    ```

2. Connect to container:

   ``` { .shell }
   docker exec -it archivebox /bin/bash
   ```

   - NOTE: (This drops you in the /data folder. DO NOT switch to /data/archive directory)
3. Switch to `archivebox` user for config:

   ``` { .shell }
   su archivebox
   ```

4. Initialize with setup to create a web admin:

   ``` { .shell }
   archivebox init --setup
   ```

5. Enter username, email, and password
6. Load URL and test login

By default, your new installation has a publicly accessible web index, snapshots, and archive addition access. You may not want this for a host of security reasons, so it's recommended to review the [ArchiveBox Security Overview](https://docs.archivebox.io/en/latest/Security-Overview.html){: .header-icons } and tailoring these settings to your preference when setting up.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    archivebox_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `archivebox_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `archivebox_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`archivebox_name`"

        ```yaml
        # Type: string
        archivebox_name: archivebox
        ```

=== "Paths"

    ??? variable string "`archivebox_role_paths_folder`"

        ```yaml
        # Type: string
        archivebox_role_paths_folder: "{{ archivebox_name }}"
        ```

    ??? variable string "`archivebox_role_paths_location`"

        ```yaml
        # Type: string
        archivebox_role_paths_location: "{{ server_appdata_path }}/{{ archivebox_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`archivebox_role_web_subdomain`"

        ```yaml
        # Type: string
        archivebox_role_web_subdomain: "{{ archivebox_name }}"
        ```

    ??? variable string "`archivebox_role_web_domain`"

        ```yaml
        # Type: string
        archivebox_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`archivebox_role_web_port`"

        ```yaml
        # Type: string
        archivebox_role_web_port: "8000"
        ```

    ??? variable string "`archivebox_role_web_url`"

        ```yaml
        # Type: string
        archivebox_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='archivebox') + '.' + lookup('role_var', '_web_domain', role='archivebox')
                                  if (lookup('role_var', '_web_subdomain', role='archivebox') | length > 0)
                                  else lookup('role_var', '_web_domain', role='archivebox')) }}"
        ```

=== "DNS"

    ??? variable string "`archivebox_role_dns_record`"

        ```yaml
        # Type: string
        archivebox_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='archivebox') }}"
        ```

    ??? variable string "`archivebox_role_dns_zone`"

        ```yaml
        # Type: string
        archivebox_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='archivebox') }}"
        ```

    ??? variable bool "`archivebox_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        archivebox_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`archivebox_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        archivebox_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`archivebox_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        archivebox_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`archivebox_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        archivebox_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`archivebox_role_traefik_certresolver`"

        ```yaml
        # Type: string
        archivebox_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`archivebox_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        archivebox_role_traefik_enabled: true
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`archivebox_role_docker_container`"

        ```yaml
        # Type: string
        archivebox_role_docker_container: "{{ archivebox_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`archivebox_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        archivebox_role_docker_image_pull: true
        ```

    ??? variable string "`archivebox_role_docker_image_repo`"

        ```yaml
        # Type: string
        archivebox_role_docker_image_repo: "archivebox/archivebox"
        ```

    ??? variable string "`archivebox_role_docker_image_tag`"

        ```yaml
        # Type: string
        archivebox_role_docker_image_tag: "latest"
        ```

    ??? variable string "`archivebox_role_docker_image`"

        ```yaml
        # Type: string
        archivebox_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='archivebox') }}:{{ lookup('role_var', '_docker_image_tag', role='archivebox') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`archivebox_role_docker_envs_default`"

        ```yaml
        # Type: dict
        archivebox_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`archivebox_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        archivebox_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`archivebox_role_docker_volumes_default`"

        ```yaml
        # Type: list
        archivebox_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='archivebox') }}:/data"
        ```

    ??? variable list "`archivebox_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        archivebox_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`archivebox_role_docker_hostname`"

        ```yaml
        # Type: string
        archivebox_role_docker_hostname: "{{ archivebox_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`archivebox_role_docker_networks_alias`"

        ```yaml
        # Type: string
        archivebox_role_docker_networks_alias: "{{ archivebox_name }}"
        ```

    ??? variable list "`archivebox_role_docker_networks_default`"

        ```yaml
        # Type: list
        archivebox_role_docker_networks_default: []
        ```

    ??? variable list "`archivebox_role_docker_networks_custom`"

        ```yaml
        # Type: list
        archivebox_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`archivebox_role_docker_restart_policy`"

        ```yaml
        # Type: string
        archivebox_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`archivebox_role_docker_state`"

        ```yaml
        # Type: string
        archivebox_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`archivebox_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        archivebox_role_autoheal_enabled: true
        ```

    ??? variable string "`archivebox_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        archivebox_role_depends_on: ""
        ```

    ??? variable string "`archivebox_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        archivebox_role_depends_on_delay: "0"
        ```

    ??? variable string "`archivebox_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        archivebox_role_depends_on_healthchecks:
        ```

    ??? variable bool "`archivebox_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        archivebox_role_diun_enabled: true
        ```

    ??? variable bool "`archivebox_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        archivebox_role_dns_enabled: true
        ```

    ??? variable bool "`archivebox_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        archivebox_role_docker_controller: true
        ```

    ??? variable bool "`archivebox_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        archivebox_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`archivebox_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        archivebox_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`archivebox_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        archivebox_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`archivebox_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        archivebox_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`archivebox_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        archivebox_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`archivebox_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        archivebox_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`archivebox_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        archivebox_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`archivebox_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        archivebox_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`archivebox_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        archivebox_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`archivebox_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        archivebox_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            archivebox_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "archivebox2.{{ user.domain }}"
              - "archivebox.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`archivebox_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        archivebox_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            archivebox_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'archivebox2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`archivebox_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        archivebox_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->