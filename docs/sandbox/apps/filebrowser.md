---
hide:
  - tags
tags:
  - filebrowser
  - file-management
  - admin
---

# File Browser

## What is it?

[File Browser](https://filebrowser.org/) is is a create-your-own-cloud-kind of software where you can install it on a server, direct it to a path and then access your files through a nice web interface. You have many available features!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://filebrowser.org/){: .header-icons } | [:octicons-link-16: Docs](https://filebrowser.org/features){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/filebrowser/filebrowser){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/filebrowser/filebrowser){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-filebrowser

```

### 2. URL

- To access File Browser, visit `https://filebrowser._yourdomain.com_`

!!! info
    The initial `admin` user has a randomly generated password. You may retrieve this password in the container logs via `docker logs filebrowser`. We recommend changing the credentials promptly upon deployment.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        filebrowser_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `filebrowser_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `filebrowser_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`filebrowser_name`"

        ```yaml
        # Type: string
        filebrowser_name: filebrowser
        ```

=== "Paths"

    ??? variable string "`filebrowser_role_paths_folder`"

        ```yaml
        # Type: string
        filebrowser_role_paths_folder: "{{ filebrowser_name }}"
        ```

    ??? variable string "`filebrowser_role_paths_location`"

        ```yaml
        # Type: string
        filebrowser_role_paths_location: "{{ server_appdata_path }}/{{ filebrowser_role_paths_folder }}"
        ```

    ??? variable string "`filebrowser_role_paths_config_location`"

        ```yaml
        # Type: string
        filebrowser_role_paths_config_location: "{{ filebrowser_role_paths_location }}/filebrowser.json"
        ```

    ??? variable string "`filebrowser_role_paths_config_folder`"

        ```yaml
        # Type: string
        filebrowser_role_paths_config_folder: "{{ filebrowser_role_paths_location }}/config"
        ```

    ??? variable string "`filebrowser_role_paths_db_location`"

        ```yaml
        # Type: string
        filebrowser_role_paths_db_location: "{{ filebrowser_role_paths_location }}/filebrowser.db"
        ```

    ??? variable string "`filebrowser_role_paths_db_folder`"

        ```yaml
        # Type: string
        filebrowser_role_paths_db_folder: "{{ filebrowser_role_paths_location }}/database"
        ```

=== "Web"

    ??? variable string "`filebrowser_role_web_subdomain`"

        ```yaml
        # Type: string
        filebrowser_role_web_subdomain: "{{ filebrowser_name }}"
        ```

    ??? variable string "`filebrowser_role_web_domain`"

        ```yaml
        # Type: string
        filebrowser_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`filebrowser_role_web_port`"

        ```yaml
        # Type: string
        filebrowser_role_web_port: "80"
        ```

    ??? variable string "`filebrowser_role_web_url`"

        ```yaml
        # Type: string
        filebrowser_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='filebrowser') + '.' + lookup('role_var', '_web_domain', role='filebrowser')
                                   if (lookup('role_var', '_web_subdomain', role='filebrowser') | length > 0)
                                   else lookup('role_var', '_web_domain', role='filebrowser')) }}"
        ```

=== "DNS"

    ??? variable string "`filebrowser_role_dns_record`"

        ```yaml
        # Type: string
        filebrowser_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='filebrowser') }}"
        ```

    ??? variable string "`filebrowser_role_dns_zone`"

        ```yaml
        # Type: string
        filebrowser_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='filebrowser') }}"
        ```

    ??? variable bool "`filebrowser_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        filebrowser_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`filebrowser_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        filebrowser_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`filebrowser_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        filebrowser_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`filebrowser_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        filebrowser_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`filebrowser_role_traefik_certresolver`"

        ```yaml
        # Type: string
        filebrowser_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`filebrowser_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        filebrowser_role_traefik_enabled: true
        ```

    ??? variable bool "`filebrowser_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        filebrowser_role_traefik_api_enabled: true
        ```

    ??? variable string "`filebrowser_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        filebrowser_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/share`) || PathPrefix(`/static`) || PathPrefix(`/api/public`)"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`filebrowser_role_docker_container`"

        ```yaml
        # Type: string
        filebrowser_role_docker_container: "{{ filebrowser_name }}"
        ```

    ##### Image

    ??? variable bool "`filebrowser_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        filebrowser_role_docker_image_pull: true
        ```

    ??? variable string "`filebrowser_role_docker_image_repo`"

        ```yaml
        # Type: string
        filebrowser_role_docker_image_repo: "filebrowser/filebrowser"
        ```

    ??? variable string "`filebrowser_role_docker_image_tag`"

        ```yaml
        # Type: string
        filebrowser_role_docker_image_tag: "latest"
        ```

    ??? variable string "`filebrowser_role_docker_image`"

        ```yaml
        # Type: string
        filebrowser_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='filebrowser') }}:{{ lookup('role_var', '_docker_image_tag', role='filebrowser') }}"
        ```

    ##### Envs

    ??? variable dict "`filebrowser_role_docker_envs_default`"

        ```yaml
        # Type: dict
        filebrowser_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`filebrowser_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        filebrowser_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`filebrowser_role_docker_volumes_default`"

        ```yaml
        # Type: list
        filebrowser_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_db_folder', role='filebrowser') }}:/database"
          - "{{ lookup('role_var', '_paths_config_folder', role='filebrowser') }}:/config"
          - "/mnt/unionfs:/srv:rslave"
        ```

    ??? variable list "`filebrowser_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        filebrowser_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`filebrowser_role_docker_hostname`"

        ```yaml
        # Type: string
        filebrowser_role_docker_hostname: "{{ filebrowser_name }}"
        ```

    ##### Networks

    ??? variable string "`filebrowser_role_docker_networks_alias`"

        ```yaml
        # Type: string
        filebrowser_role_docker_networks_alias: "{{ filebrowser_name }}"
        ```

    ??? variable list "`filebrowser_role_docker_networks_default`"

        ```yaml
        # Type: list
        filebrowser_role_docker_networks_default: []
        ```

    ??? variable list "`filebrowser_role_docker_networks_custom`"

        ```yaml
        # Type: list
        filebrowser_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`filebrowser_role_docker_restart_policy`"

        ```yaml
        # Type: string
        filebrowser_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`filebrowser_role_docker_state`"

        ```yaml
        # Type: string
        filebrowser_role_docker_state: started
        ```

    ##### User

    ??? variable string "`filebrowser_role_docker_user`"

        ```yaml
        # Type: string
        filebrowser_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`filebrowser_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        filebrowser_role_autoheal_enabled: true
        ```

    ??? variable string "`filebrowser_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        filebrowser_role_depends_on: ""
        ```

    ??? variable string "`filebrowser_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        filebrowser_role_depends_on_delay: "0"
        ```

    ??? variable string "`filebrowser_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        filebrowser_role_depends_on_healthchecks:
        ```

    ??? variable bool "`filebrowser_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        filebrowser_role_diun_enabled: true
        ```

    ??? variable bool "`filebrowser_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        filebrowser_role_dns_enabled: true
        ```

    ??? variable bool "`filebrowser_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        filebrowser_role_docker_controller: true
        ```

    ??? variable bool "`filebrowser_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        filebrowser_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`filebrowser_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        filebrowser_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`filebrowser_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        filebrowser_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`filebrowser_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        filebrowser_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`filebrowser_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        filebrowser_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`filebrowser_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        filebrowser_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`filebrowser_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        filebrowser_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`filebrowser_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        filebrowser_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`filebrowser_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        filebrowser_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`filebrowser_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        filebrowser_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            filebrowser_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "filebrowser2.{{ user.domain }}"
              - "filebrowser.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`filebrowser_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        filebrowser_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            filebrowser_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'filebrowser2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`filebrowser_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        filebrowser_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->