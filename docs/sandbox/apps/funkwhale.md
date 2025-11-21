---
icon: material/docker
hide:
  - tags
tags:
  - funkwhale
  - media
  - music
---

# Funkwhale

## Overview

[Funkwhale](https://funkwhale.audio/) is a modern, self-hosted, free and open-source music server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://funkwhale.audio/){: .header-icons } | [:octicons-link-16: Docs](https://docs.funkwhale.audio/){: .header-icons } | [:octicons-mark-github-16: Github](https://dev.funkwhale.audio/funkwhale){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/funkwhale/all-in-one){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-funkwhale
```

### 2. URL

- To access Funkwhale, visit <https://funkwhale.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- First create the superuser

- `docker exec -it funkwhale manage createsuperuser` <br />
   (for ease of access, set it as your Saltbox user and password.)
- enter the `exit` command when finished to return to your server's shell.

- Now configure these settings via the web GUI

- Access Funkwhale, visit <https://funkwhale.iYOUR_DOMAIN_NAMEi> and log in with the user and password you just created.
- Enter `Music->Add Content->Create a new Library` and fill out the information.
- Enter your new Library and Details. There will be a sharing link such as:
  `https://funkwhale.domain.com/federation/music/libraries/da8bd97b-3c3f-4e7b-92cb-6ba45721837b`
- Copy out the last portion: `da8bd97b-3c3f-4e7b-92cb-6ba45721837b`

- Return to the shell session to import music library

- `docker exec -it funkwhale /usr/bin/python3 /app/api/manage.py import_files da8bd97b-3c3f-4e7b-92cb-6ba45721837b "/music/Media/Audio/Music/**/**/*.flac" --in-place --async --recursive`

The above line explained:

- `docker exec -it funkwhale /usr/bin/python3 /app/api/manage.py import_files` tells funkwhale to import music.
- `da8bd97b-3c3f-4e7b-92cb-6ba45721837b` is your library id
- `"/music/Media/Audio/Music/**/**/*.flac"` is the path to your media.
- `--in-place` means do not copy the media into Funkwhale and leave it where it is.
- `--async` means it will import the music first and then pull the metadata`
- `--recursive` will recursively scan the folders

If everything goes as planned you'll get prompted like this:

```shell
> Checking imported paths against settings.MUSIC_DIRECTORY_PATH
> Import summary:
> - 149828 files found matching this pattern: ['/music/Media/Audio/Music/**/**/*.flac']

> - 0 files already found in database
> - 149828 new files
> Selected options: in place
> Are you sure you want to do this?
> Type 'yes' to continue, or 'no' to cancel:
```

- Answer yes at the prompt and the import will begin.

!!! info
    Useful URLs <br />
    Libraries URL: `https://funkwhale.domain.com/content/libraries/` <br />
    Admin Account Edit Page: `https://funkwhale.domain.com/api/admin/users/user/1/change/` <br />

!!! info
    If you want to use subsonic clients then you'll need to set a password here:  <br />
    `https://funkwhale.domain.com/settings`
    (subsonic protocol requires storing password in cleartext, so to avoid compromising your Funkwhale account, we use a different password).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    funkwhale_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `funkwhale_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `funkwhale_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`funkwhale_name`"

        ```yaml
        # Type: string
        funkwhale_name: funkwhale
        ```

=== "Paths"

    ??? variable string "`funkwhale_role_paths_folder`"

        ```yaml
        # Type: string
        funkwhale_role_paths_folder: "{{ funkwhale_name }}"
        ```

    ??? variable string "`funkwhale_role_paths_location`"

        ```yaml
        # Type: string
        funkwhale_role_paths_location: "{{ server_appdata_path }}/{{ funkwhale_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`funkwhale_role_web_subdomain`"

        ```yaml
        # Type: string
        funkwhale_role_web_subdomain: "{{ funkwhale_name }}"
        ```

    ??? variable string "`funkwhale_role_web_domain`"

        ```yaml
        # Type: string
        funkwhale_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`funkwhale_role_web_port`"

        ```yaml
        # Type: string
        funkwhale_role_web_port: "80"
        ```

    ??? variable string "`funkwhale_role_web_url`"

        ```yaml
        # Type: string
        funkwhale_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='funkwhale') + '.' + lookup('role_var', '_web_domain', role='funkwhale')
                                 if (lookup('role_var', '_web_subdomain', role='funkwhale') | length > 0)
                                 else lookup('role_var', '_web_domain', role='funkwhale')) }}"
        ```

=== "DNS"

    ??? variable string "`funkwhale_role_dns_record`"

        ```yaml
        # Type: string
        funkwhale_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='funkwhale') }}"
        ```

    ??? variable string "`funkwhale_role_dns_zone`"

        ```yaml
        # Type: string
        funkwhale_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='funkwhale') }}"
        ```

    ??? variable bool "`funkwhale_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`funkwhale_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`funkwhale_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`funkwhale_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`funkwhale_role_traefik_certresolver`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`funkwhale_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_enabled: true
        ```

    ??? variable bool "`funkwhale_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_api_enabled: false
        ```

    ??? variable string "`funkwhale_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`funkwhale_role_docker_container`"

        ```yaml
        # Type: string
        funkwhale_role_docker_container: "{{ funkwhale_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`funkwhale_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_image_pull: true
        ```

    ??? variable string "`funkwhale_role_docker_image_repo`"

        ```yaml
        # Type: string
        funkwhale_role_docker_image_repo: "funkwhale/all-in-one"
        ```

    ??? variable string "`funkwhale_role_docker_image_tag`"

        ```yaml
        # Type: string
        funkwhale_role_docker_image_tag: "latest"
        ```

    ??? variable string "`funkwhale_role_docker_image`"

        ```yaml
        # Type: string
        funkwhale_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='funkwhale') }}:{{ lookup('role_var', '_docker_image_tag', role='funkwhale') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`funkwhale_role_docker_envs_default`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_envs_default:
          FUNKWHALE_HOSTNAME: "{{ lookup('role_var', '_web_subdomain', role='funkwhale') + '.' + lookup('role_var', '_web_domain', role='funkwhale') }}"
          NESTED_PROXY: "1"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`funkwhale_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`funkwhale_role_docker_volumes_default`"

        ```yaml
        # Type: list
        funkwhale_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='funkwhale') }}/data:/data"
          - "/mnt/unionfs:/music:ro"
        ```

    ??? variable list "`funkwhale_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        funkwhale_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`funkwhale_role_docker_hostname`"

        ```yaml
        # Type: string
        funkwhale_role_docker_hostname: "{{ funkwhale_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`funkwhale_role_docker_networks_alias`"

        ```yaml
        # Type: string
        funkwhale_role_docker_networks_alias: "{{ funkwhale_name }}"
        ```

    ??? variable list "`funkwhale_role_docker_networks_default`"

        ```yaml
        # Type: list
        funkwhale_role_docker_networks_default: []
        ```

    ??? variable list "`funkwhale_role_docker_networks_custom`"

        ```yaml
        # Type: list
        funkwhale_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`funkwhale_role_docker_restart_policy`"

        ```yaml
        # Type: string
        funkwhale_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`funkwhale_role_docker_state`"

        ```yaml
        # Type: string
        funkwhale_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`funkwhale_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        funkwhale_role_autoheal_enabled: true
        ```

    ??? variable string "`funkwhale_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        funkwhale_role_depends_on: ""
        ```

    ??? variable string "`funkwhale_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        funkwhale_role_depends_on_delay: "0"
        ```

    ??? variable string "`funkwhale_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        funkwhale_role_depends_on_healthchecks:
        ```

    ??? variable bool "`funkwhale_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        funkwhale_role_diun_enabled: true
        ```

    ??? variable bool "`funkwhale_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        funkwhale_role_dns_enabled: true
        ```

    ??? variable bool "`funkwhale_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        funkwhale_role_docker_controller: true
        ```

    ??? variable bool "`funkwhale_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_volumes_download:
        ```

    ??? variable bool "`funkwhale_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`funkwhale_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`funkwhale_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`funkwhale_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`funkwhale_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        funkwhale_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            funkwhale_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "funkwhale2.{{ user.domain }}"
              - "funkwhale.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`funkwhale_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        funkwhale_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            funkwhale_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'funkwhale2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`funkwhale_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        funkwhale_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->