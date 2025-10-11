---
hide:
  - tags
tags:
  - mkvtoolnix
  - media
  - tools
---

# MKVToolNix

## What is it?

[MKVToolNix](https://mkvtoolnix.download) is a set of tools to create, alter and inspect Matroska files.

You can use MKVToolNix to create, split, edit, mux, demux, merge, extract or inspect Matroska files. The program will also work with other video formats (AVI, MPEG, MP4, MPEG, Ogg/OGM, RealVideo, MPEG1/2, h264/AVC, Dirac, VC1) including some video codecs (such as VP9 video codec support - reading from IVF/Matroska/WebM files, extract to IVF files). Audio formats (AAC, FLAC, MP2, MP3, (E)AC3, DTS/DTS-HD, Vorbis, RealAudio) and also most subtitle formats (SRT, PGS/SUP, VobSub, ASS, SSA, etc.).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://mkvtoolnix.download){: .header-icons } | [:octicons-link-16: Docs](https://mkvtoolnix.download/docs.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jlesage/docker-mkvtoolnix){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/mkvtoolnix){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-mkvtoolnix

```

### 2. URL

- To access MKVToolNix, visit `https://mkvtoolnix._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        mkvtoolnix_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    mkvtoolnix_name: mkvtoolnix

    ```

??? example "Paths"

    ```yaml
    # Type: string
    mkvtoolnix_role_paths_folder: "{{ mkvtoolnix_name }}"

    # Type: string
    mkvtoolnix_role_paths_location: "{{ server_appdata_path }}/{{ mkvtoolnix_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    mkvtoolnix_role_web_subdomain: "{{ mkvtoolnix_name }}"

    # Type: string
    mkvtoolnix_role_web_domain: "{{ user.domain }}"

    # Type: string
    mkvtoolnix_role_web_port: "5800"

    # Type: string
    mkvtoolnix_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='mkvtoolnix') + '.' + lookup('role_var', '_web_domain', role='mkvtoolnix')
                              if (lookup('role_var', '_web_subdomain', role='mkvtoolnix') | length > 0)
                              else lookup('role_var', '_web_domain', role='mkvtoolnix')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    mkvtoolnix_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='mkvtoolnix') }}"

    # Type: string
    mkvtoolnix_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='mkvtoolnix') }}"

    # Type: bool (true/false)
    mkvtoolnix_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    mkvtoolnix_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    mkvtoolnix_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    mkvtoolnix_role_traefik_middleware_custom: ""

    # Type: string
    mkvtoolnix_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    mkvtoolnix_role_traefik_enabled: true

    # Type: bool (true/false)
    mkvtoolnix_role_traefik_api_enabled: false

    # Type: string
    mkvtoolnix_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    mkvtoolnix_role_docker_container: "{{ mkvtoolnix_name }}"

    # Image
    # Type: bool (true/false)
    mkvtoolnix_role_docker_image_pull: true

    # Type: string
    mkvtoolnix_role_docker_image_tag: "latest"

    # Type: string
    mkvtoolnix_role_docker_image_repo: "jlesage/mkvtoolnix"

    # Type: string
    mkvtoolnix_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mkvtoolnix') }}:{{ lookup('role_var', '_docker_image_tag', role='mkvtoolnix') }}"

    # Envs
    # Type: dict
    mkvtoolnix_role_docker_envs_default: 
      USER_ID: "{{ uid }}"
      GROUP_ID: "{{ gid }}"
      TZ: "{{ tz }}"
      DISPLAY_WIDTH: "1280"
      DISPLAY_HEIGHT: "768"
      CLEAN_TMP_DIR: "1"
      UMASK: "000"
      ENABLE_CJK_FONT: "1"

    # Type: dict
    mkvtoolnix_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    mkvtoolnix_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='mkvtoolnix') }}:/config"
      - "/mnt/unionfs:/storage"

    # Type: list
    mkvtoolnix_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    mkvtoolnix_role_docker_hostname: "{{ mkvtoolnix_name }}"

    # Networks
    # Type: string
    mkvtoolnix_role_docker_networks_alias: "{{ mkvtoolnix_name }}"

    # Type: list
    mkvtoolnix_role_docker_networks_default: []

    # Type: list
    mkvtoolnix_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    mkvtoolnix_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    mkvtoolnix_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    mkvtoolnix_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    mkvtoolnix_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    mkvtoolnix_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    mkvtoolnix_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    mkvtoolnix_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    mkvtoolnix_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    mkvtoolnix_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    mkvtoolnix_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    mkvtoolnix_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    mkvtoolnix_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    mkvtoolnix_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    mkvtoolnix_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    mkvtoolnix_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    mkvtoolnix_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    mkvtoolnix_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    mkvtoolnix_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    mkvtoolnix_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        mkvtoolnix_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "mkvtoolnix2.{{ user.domain }}"
          - "mkvtoolnix.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        mkvtoolnix_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mkvtoolnix2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
