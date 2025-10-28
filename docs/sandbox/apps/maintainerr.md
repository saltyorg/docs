---
hide:
  - tags
tags:
  - maintainerr
  - maintenance
  - automation
---

# Maintainerr

# What is it?

[Maintainerr](https://docs.maintainerr.info/) allows you to set a variety of rules and actions mostly around identifying and deleting little-watched media.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.maintainerr.info/){: .header-icons } | [:octicons-link-16: Docs](https://docs.maintainerr.info/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jorenn92/Maintainerr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jorenn92/maintainerr){: .header-icons }|

## 1. URL

- To access maintainerr, visit <https://maintainerr.iYOUR_DOMAIN_NAMEi>

## 2. Settings

This setup needs to take place **AFTER** you've set up Plex, Radarr, and Sonarr, since it involves connections to all three of those.

You will need your API Keys from both Radarr and Sonarr.

1. Log into your maintainerr url and the inital page will be the plex settings

2. Authenticate into plex

3. Click the refresh button to have maintainer find all plex servers

4. Click on the drop down and choose manual

5. Name it whatever you want

6. Hostname or IP is the name of your container. Default is plex

7. Port of plex server. Default is 32400

8. Leave SSL unchecked

9. Save Changes and Test changes

10. Navigate to Overseerr tab

11. Hostname of overseerr container. Default is overseerr

12. Port of container. Default is 5055

13. API key from overseerr

14. Save and test changes

15. Navigate to Sonarr tab

16. Hostname of sonarr container. Default is sonarr

17. Port of sonarr container. Default is 8989

18. API key from sonarr

19. Save and test changes

20. Navigate to Radarr tab

21. Hostname of radarr container. Default is radarr

22. Port of radarr container. Default is 7878

23. API key from radarr

24. Save and test changes

25. Once Overseerr, Plex, Sonarr, Radarr configurations are in place, you can use the app to you preferences.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `maintainerr_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of maintainerr:" }
    maintainerr_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `maintainerr2`):" }
    maintainerr2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `maintainerr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `maintainerr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`maintainerr_instances`"

        ```yaml
        # Type: list
        maintainerr_instances: ["maintainerr"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            maintainerr_instances: ["maintainerr", "maintainerr2"]
            ```

=== "Paths"

    ??? variable string "`maintainerr_role_paths_folder`{ .sb-show-on-unchecked }`maintainerr2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_paths_folder: "{{ maintainerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_paths_folder: "{{ maintainerr_name }}"
        ```

    ??? variable string "`maintainerr_role_paths_location`{ .sb-show-on-unchecked }`maintainerr2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_paths_location: "{{ server_appdata_path }}/{{ maintainerr_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_paths_location: "{{ server_appdata_path }}/{{ maintainerr_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`maintainerr_role_web_subdomain`{ .sb-show-on-unchecked }`maintainerr2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_web_subdomain: "{{ maintainerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_web_subdomain: "{{ maintainerr_name }}"
        ```

    ??? variable string "`maintainerr_role_web_domain`{ .sb-show-on-unchecked }`maintainerr2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`maintainerr_role_web_port`{ .sb-show-on-unchecked }`maintainerr2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_web_port: "6246"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_web_port: "6246"
        ```

    ??? variable string "`maintainerr_role_web_url`{ .sb-show-on-unchecked }`maintainerr2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='maintainerr') + '.' + lookup('role_var', '_web_domain', role='maintainerr')
                                   if (lookup('role_var', '_web_subdomain', role='maintainerr') | length > 0)
                                   else lookup('role_var', '_web_domain', role='maintainerr')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='maintainerr') + '.' + lookup('role_var', '_web_domain', role='maintainerr')
                               if (lookup('role_var', '_web_subdomain', role='maintainerr') | length > 0)
                               else lookup('role_var', '_web_domain', role='maintainerr')) }}"
        ```

=== "DNS"

    ??? variable string "`maintainerr_role_dns_record`{ .sb-show-on-unchecked }`maintainerr2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='maintainerr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='maintainerr') }}"
        ```

    ??? variable string "`maintainerr_role_dns_zone`{ .sb-show-on-unchecked }`maintainerr2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='maintainerr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='maintainerr') }}"
        ```

    ??? variable bool "`maintainerr_role_dns_proxy`{ .sb-show-on-unchecked }`maintainerr2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        maintainerr_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        maintainerr2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`maintainerr_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`maintainerr2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`maintainerr_role_traefik_middleware_default`{ .sb-show-on-unchecked }`maintainerr2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`maintainerr_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`maintainerr2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_traefik_middleware_custom: ""
        ```

    ??? variable string "`maintainerr_role_traefik_certresolver`{ .sb-show-on-unchecked }`maintainerr2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`maintainerr_role_traefik_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        maintainerr_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        maintainerr2_traefik_enabled: true
        ```

    ??? variable bool "`maintainerr_role_traefik_api_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        maintainerr_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        maintainerr2_traefik_api_enabled: false
        ```

    ??? variable string "`maintainerr_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`maintainerr2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`maintainerr_role_docker_container`{ .sb-show-on-unchecked }`maintainerr2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_container: "{{ maintainerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_container: "{{ maintainerr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`maintainerr_role_docker_image_pull`{ .sb-show-on-unchecked }`maintainerr2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        maintainerr_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        maintainerr2_docker_image_pull: true
        ```

    ??? variable string "`maintainerr_role_docker_image_repo`{ .sb-show-on-unchecked }`maintainerr2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_image_repo: "jorenn92/maintainerr"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_image_repo: "jorenn92/maintainerr"
        ```

    ??? variable string "`maintainerr_role_docker_image_tag`{ .sb-show-on-unchecked }`maintainerr2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_image_tag: "latest"
        ```

    ??? variable string "`maintainerr_role_docker_image`{ .sb-show-on-unchecked }`maintainerr2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='maintainerr') }}:{{ lookup('role_var', '_docker_image_tag', role='maintainerr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='maintainerr') }}:{{ lookup('role_var', '_docker_image_tag', role='maintainerr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`maintainerr_role_docker_envs_default`{ .sb-show-on-unchecked }`maintainerr2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        maintainerr_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        maintainerr2_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`maintainerr_role_docker_envs_custom`{ .sb-show-on-unchecked }`maintainerr2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        maintainerr_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        maintainerr2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`maintainerr_role_docker_volumes_default`{ .sb-show-on-unchecked }`maintainerr2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        maintainerr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='maintainerr') }}:/opt/data"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        maintainerr2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='maintainerr') }}:/opt/data"
        ```

    ??? variable list "`maintainerr_role_docker_volumes_custom`{ .sb-show-on-unchecked }`maintainerr2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        maintainerr_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        maintainerr2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`maintainerr_role_docker_hostname`{ .sb-show-on-unchecked }`maintainerr2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_hostname: "{{ maintainerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_hostname: "{{ maintainerr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`maintainerr_role_docker_networks_alias`{ .sb-show-on-unchecked }`maintainerr2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_networks_alias: "{{ maintainerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_networks_alias: "{{ maintainerr_name }}"
        ```

    ??? variable list "`maintainerr_role_docker_networks_default`{ .sb-show-on-unchecked }`maintainerr2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        maintainerr_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        maintainerr2_docker_networks_default: []
        ```

    ??? variable list "`maintainerr_role_docker_networks_custom`{ .sb-show-on-unchecked }`maintainerr2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        maintainerr_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        maintainerr2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`maintainerr_role_docker_restart_policy`{ .sb-show-on-unchecked }`maintainerr2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`maintainerr_role_docker_state`{ .sb-show-on-unchecked }`maintainerr2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`maintainerr_role_docker_user`{ .sb-show-on-unchecked }`maintainerr2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        maintainerr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        maintainerr2_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`maintainerr_role_autoheal_enabled`{ .sb-show-on-unchecked }`maintainerr2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        maintainerr_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        maintainerr2_autoheal_enabled: true
        ```

    ??? variable string "`maintainerr_role_depends_on`{ .sb-show-on-unchecked }`maintainerr2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        maintainerr_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        maintainerr2_depends_on: ""
        ```

    ??? variable string "`maintainerr_role_depends_on_delay`{ .sb-show-on-unchecked }`maintainerr2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        maintainerr_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        maintainerr2_depends_on_delay: "0"
        ```

    ??? variable string "`maintainerr_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`maintainerr2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        maintainerr_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        maintainerr2_depends_on_healthchecks:
        ```

    ??? variable bool "`maintainerr_role_diun_enabled`{ .sb-show-on-unchecked }`maintainerr2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        maintainerr_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        maintainerr2_diun_enabled: true
        ```

    ??? variable bool "`maintainerr_role_dns_enabled`{ .sb-show-on-unchecked }`maintainerr2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        maintainerr_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        maintainerr2_dns_enabled: true
        ```

    ??? variable bool "`maintainerr_role_docker_controller`{ .sb-show-on-unchecked }`maintainerr2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        maintainerr_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        maintainerr2_docker_controller: true
        ```

    ??? variable bool "`maintainerr_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        maintainerr_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        maintainerr2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`maintainerr_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        maintainerr_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        maintainerr2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`maintainerr_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        maintainerr_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        maintainerr2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`maintainerr_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        maintainerr_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        maintainerr2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`maintainerr_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`maintainerr2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        maintainerr_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        maintainerr2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`maintainerr_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`maintainerr2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        maintainerr_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        maintainerr2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`maintainerr_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        maintainerr_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        maintainerr2_traefik_robot_enabled: true
        ```

    ??? variable bool "`maintainerr_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        maintainerr_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        maintainerr2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`maintainerr_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`maintainerr2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        maintainerr_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        maintainerr2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`maintainerr_role_web_fqdn_override`{ .sb-show-on-unchecked }`maintainerr2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        maintainerr_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        maintainerr2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            maintainerr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "maintainerr2.{{ user.domain }}"
              - "maintainerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            maintainerr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "maintainerr2.{{ user.domain }}"
              - "maintainerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`maintainerr_role_web_host_override`{ .sb-show-on-unchecked }`maintainerr2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        maintainerr_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        maintainerr2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            maintainerr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'maintainerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            maintainerr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'maintainerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`maintainerr_role_web_scheme`{ .sb-show-on-unchecked }`maintainerr2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        maintainerr_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        maintainerr2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->