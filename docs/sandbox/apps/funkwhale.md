---
hide:
  - tags
tags:
  - funkwhale
  - media
  - music
---

# Funkwhale

## What is it?

[Funkwhale](https://funkwhale.audio/) is a modern, self-hosted, free and open-source music server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://funkwhale.audio/){: .header-icons } | [:octicons-link-16: Docs](https://docs.funkwhale.audio/){: .header-icons } | [:octicons-mark-github-16: Github](https://dev.funkwhale.audio/funkwhale){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/funkwhale/all-in-one){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-funkwhale

```

### 2. URL

- To access Funkwhale, visit `https://funkwhale.xDOMAIN_NAMEx`

### 3. Setup

- First create the superuser

- `docker exec -it funkwhale manage createsuperuser` <br />
   (for ease of access, set it as your Saltbox user and password.)
- enter the `exit` command when finished to return to your server's shell.

- Now configure these settings via the web GUI

- Access Funkwhale, visit `https://funkwhale.xDOMAIN_NAMEx` and log in with the user and password you just created.
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

``` { .shell }
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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        funkwhale_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `funkwhale_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `funkwhale_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    funkwhale_name: funkwhale

    ```

??? example "Paths"

    ```yaml
    # Type: string
    funkwhale_role_paths_folder: "{{ funkwhale_name }}"

    # Type: string
    funkwhale_role_paths_location: "{{ server_appdata_path }}/{{ funkwhale_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    funkwhale_role_web_subdomain: "{{ funkwhale_name }}"

    # Type: string
    funkwhale_role_web_domain: "{{ user.domain }}"

    # Type: string
    funkwhale_role_web_port: "80"

    # Type: string
    funkwhale_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='funkwhale') + '.' + lookup('role_var', '_web_domain', role='funkwhale')
                             if (lookup('role_var', '_web_subdomain', role='funkwhale') | length > 0)
                             else lookup('role_var', '_web_domain', role='funkwhale')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    funkwhale_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='funkwhale') }}"

    # Type: string
    funkwhale_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='funkwhale') }}"

    # Type: bool (true/false)
    funkwhale_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    funkwhale_role_traefik_sso_middleware: ""

    # Type: string
    funkwhale_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    funkwhale_role_traefik_middleware_custom: ""

    # Type: string
    funkwhale_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    funkwhale_role_traefik_enabled: true

    # Type: bool (true/false)
    funkwhale_role_traefik_api_enabled: false

    # Type: string
    funkwhale_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    funkwhale_role_docker_container: "{{ funkwhale_name }}"

    # Image
    # Type: bool (true/false)
    funkwhale_role_docker_image_pull: true

    # Type: string
    funkwhale_role_docker_image_repo: "funkwhale/all-in-one"

    # Type: string
    funkwhale_role_docker_image_tag: "latest"

    # Type: string
    funkwhale_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='funkwhale') }}:{{ lookup('role_var', '_docker_image_tag', role='funkwhale') }}"

    # Envs
    # Type: dict
    funkwhale_role_docker_envs_default: 
      FUNKWHALE_HOSTNAME: "{{ lookup('role_var', '_web_subdomain', role='funkwhale') + '.' + lookup('role_var', '_web_domain', role='funkwhale') }}"
      NESTED_PROXY: "1"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    funkwhale_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    funkwhale_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='funkwhale') }}/data:/data"
      - "/mnt/unionfs:/music:ro"

    # Type: list
    funkwhale_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    funkwhale_role_docker_hostname: "{{ funkwhale_name }}"

    # Networks
    # Type: string
    funkwhale_role_docker_networks_alias: "{{ funkwhale_name }}"

    # Type: list
    funkwhale_role_docker_networks_default: []

    # Type: list
    funkwhale_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    funkwhale_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    funkwhale_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    funkwhale_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    funkwhale_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    funkwhale_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    funkwhale_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    funkwhale_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    funkwhale_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    funkwhale_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    funkwhale_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    funkwhale_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    funkwhale_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    funkwhale_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    funkwhale_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    funkwhale_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    funkwhale_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    funkwhale_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    funkwhale_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    funkwhale_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        funkwhale_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "funkwhale2.{{ user.domain }}"
          - "funkwhale.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        funkwhale_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'funkwhale2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
