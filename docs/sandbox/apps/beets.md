---
hide:
  - tags
tags:
  - beets
  - music
  - metadata
---

# Beets

## What is it?

[Beets](https://beets.io/) catalogs your collection, automatically improving its metadata as it goes using the MusicBrainz database. Then it provides a bouquet of tools for manipulating and accessing your music.

Beets is a music library manager and not, for the most part, a music player. It does include a simple player plugin and an experimental Web-based player, but it generally leaves actual sound-reproduction to specialized tools.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://beets.io/){: .header-icons } | [:octicons-link-16: Docs](http://beets.readthedocs.org/){: .header-icons } | [:octicons-mark-github-16: Github](http://github.com/beetbox/beets){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/beets){: .header-icons }|

### 1. Installation

```  { .shell }

sb install sandbox-beets

```

### 2. URL

- To access Beets, visit `https://beets._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`
- When the role is run, a cron job is set to automatically import any music found at `/mnt/local/downloads/music` every hour.  <br />
  If a match is under 95% beets will skip the file and it will need manual importing.
- To run a manual import (which will help correct any matches under 95%) run the following command:

    ``` { .shell }
    rm /opt/beets/state.pickle && docker exec -it beets /bin/bash -c 'beet import /downloads'
    ```

- If you want to change the folder structure you should do so in the config file located at  <br />
  `/opt/beets/config.yaml` <br />
  [This link details the allowed options](https://beets.readthedocs.io/en/v1.4.7/reference/config.html#path-format-configuration)

    If you already have imported music you will need to run an import using the following command:

    ``` { .shell }
    docker exec -it beets /bin/bash -c 'beet import /music'
    ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    beets_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `beets_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `beets_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`beets_name`"

        ```yaml
        # Type: string
        beets_name: beets
        ```

=== "Paths"

    ??? variable string "`beets_role_paths_folder`"

        ```yaml
        # Type: string
        beets_role_paths_folder: "{{ beets_name }}"
        ```

    ??? variable string "`beets_role_paths_location`"

        ```yaml
        # Type: string
        beets_role_paths_location: "{{ server_appdata_path }}/{{ beets_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`beets_role_web_subdomain`"

        ```yaml
        # Type: string
        beets_role_web_subdomain: "{{ beets_name }}"
        ```

    ??? variable string "`beets_role_web_domain`"

        ```yaml
        # Type: string
        beets_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`beets_role_web_port`"

        ```yaml
        # Type: string
        beets_role_web_port: "8337"
        ```

    ??? variable string "`beets_role_web_url`"

        ```yaml
        # Type: string
        beets_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='beets') + '.' + lookup('role_var', '_web_domain', role='beets')
                             if (lookup('role_var', '_web_subdomain', role='beets') | length > 0)
                             else lookup('role_var', '_web_domain', role='beets')) }}"
        ```

=== "DNS"

    ??? variable string "`beets_role_dns_record`"

        ```yaml
        # Type: string
        beets_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='beets') }}"
        ```

    ??? variable string "`beets_role_dns_zone`"

        ```yaml
        # Type: string
        beets_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='beets') }}"
        ```

    ??? variable bool "`beets_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        beets_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`beets_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        beets_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`beets_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        beets_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`beets_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        beets_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`beets_role_traefik_certresolver`"

        ```yaml
        # Type: string
        beets_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`beets_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        beets_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`beets_role_docker_container`"

        ```yaml
        # Type: string
        beets_role_docker_container: "{{ beets_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`beets_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        beets_role_docker_image_pull: true
        ```

    ??? variable string "`beets_role_docker_image_repo`"

        ```yaml
        # Type: string
        beets_role_docker_image_repo: "lscr.io/linuxserver/beets"
        ```

    ??? variable string "`beets_role_docker_image_tag`"

        ```yaml
        # Type: string
        beets_role_docker_image_tag: "latest"
        ```

    ??? variable string "`beets_role_docker_image`"

        ```yaml
        # Type: string
        beets_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='beets') }}:{{ lookup('role_var', '_docker_image_tag', role='beets') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`beets_role_docker_envs_default`"

        ```yaml
        # Type: dict
        beets_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`beets_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        beets_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`beets_role_docker_volumes_default`"

        ```yaml
        # Type: list
        beets_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='beets') }}:/config"
          - "/mnt/unionfs/Media/Music:/music"
        ```

    ??? variable list "`beets_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        beets_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`beets_role_docker_hostname`"

        ```yaml
        # Type: string
        beets_role_docker_hostname: "{{ beets_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`beets_role_docker_networks_alias`"

        ```yaml
        # Type: string
        beets_role_docker_networks_alias: "{{ beets_name }}"
        ```

    ??? variable list "`beets_role_docker_networks_default`"

        ```yaml
        # Type: list
        beets_role_docker_networks_default: []
        ```

    ??? variable list "`beets_role_docker_networks_custom`"

        ```yaml
        # Type: list
        beets_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`beets_role_docker_restart_policy`"

        ```yaml
        # Type: string
        beets_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`beets_role_docker_state`"

        ```yaml
        # Type: string
        beets_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`beets_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        beets_role_autoheal_enabled: true
        ```

    ??? variable string "`beets_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        beets_role_depends_on: ""
        ```

    ??? variable string "`beets_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        beets_role_depends_on_delay: "0"
        ```

    ??? variable string "`beets_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        beets_role_depends_on_healthchecks:
        ```

    ??? variable bool "`beets_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        beets_role_diun_enabled: true
        ```

    ??? variable bool "`beets_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        beets_role_dns_enabled: true
        ```

    ??? variable bool "`beets_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        beets_role_docker_controller: true
        ```

    ??? variable bool "`beets_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        beets_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`beets_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        beets_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`beets_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        beets_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`beets_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        beets_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`beets_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        beets_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`beets_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        beets_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`beets_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        beets_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`beets_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        beets_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`beets_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        beets_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`beets_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        beets_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            beets_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "beets2.{{ user.domain }}"
              - "beets.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`beets_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        beets_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            beets_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'beets2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`beets_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        beets_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->