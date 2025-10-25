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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    mkvtoolnix_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `mkvtoolnix_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `mkvtoolnix_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`mkvtoolnix_name`"

        ```yaml
        # Type: string
        mkvtoolnix_name: mkvtoolnix
        ```

=== "Paths"

    ??? variable string "`mkvtoolnix_role_paths_folder`"

        ```yaml
        # Type: string
        mkvtoolnix_role_paths_folder: "{{ mkvtoolnix_name }}"
        ```

    ??? variable string "`mkvtoolnix_role_paths_location`"

        ```yaml
        # Type: string
        mkvtoolnix_role_paths_location: "{{ server_appdata_path }}/{{ mkvtoolnix_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`mkvtoolnix_role_web_subdomain`"

        ```yaml
        # Type: string
        mkvtoolnix_role_web_subdomain: "{{ mkvtoolnix_name }}"
        ```

    ??? variable string "`mkvtoolnix_role_web_domain`"

        ```yaml
        # Type: string
        mkvtoolnix_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`mkvtoolnix_role_web_port`"

        ```yaml
        # Type: string
        mkvtoolnix_role_web_port: "5800"
        ```

    ??? variable string "`mkvtoolnix_role_web_url`"

        ```yaml
        # Type: string
        mkvtoolnix_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='mkvtoolnix') + '.' + lookup('role_var', '_web_domain', role='mkvtoolnix')
                                  if (lookup('role_var', '_web_subdomain', role='mkvtoolnix') | length > 0)
                                  else lookup('role_var', '_web_domain', role='mkvtoolnix')) }}"
        ```

=== "DNS"

    ??? variable string "`mkvtoolnix_role_dns_record`"

        ```yaml
        # Type: string
        mkvtoolnix_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='mkvtoolnix') }}"
        ```

    ??? variable string "`mkvtoolnix_role_dns_zone`"

        ```yaml
        # Type: string
        mkvtoolnix_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='mkvtoolnix') }}"
        ```

    ??? variable bool "`mkvtoolnix_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        mkvtoolnix_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`mkvtoolnix_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        mkvtoolnix_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`mkvtoolnix_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        mkvtoolnix_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`mkvtoolnix_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        mkvtoolnix_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`mkvtoolnix_role_traefik_certresolver`"

        ```yaml
        # Type: string
        mkvtoolnix_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_enabled: true
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_api_enabled: false
        ```

    ??? variable string "`mkvtoolnix_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        mkvtoolnix_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`mkvtoolnix_role_docker_container`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_container: "{{ mkvtoolnix_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`mkvtoolnix_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        mkvtoolnix_role_docker_image_pull: true
        ```

    ??? variable string "`mkvtoolnix_role_docker_image_tag`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_image_tag: "latest"
        ```

    ??? variable string "`mkvtoolnix_role_docker_image_repo`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_image_repo: "jlesage/mkvtoolnix"
        ```

    ??? variable string "`mkvtoolnix_role_docker_image`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mkvtoolnix') }}:{{ lookup('role_var', '_docker_image_tag', role='mkvtoolnix') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`mkvtoolnix_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`mkvtoolnix_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        mkvtoolnix_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`mkvtoolnix_role_docker_volumes_default`"

        ```yaml
        # Type: list
        mkvtoolnix_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='mkvtoolnix') }}:/config"
          - "/mnt/unionfs:/storage"
        ```

    ??? variable list "`mkvtoolnix_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        mkvtoolnix_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`mkvtoolnix_role_docker_hostname`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_hostname: "{{ mkvtoolnix_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`mkvtoolnix_role_docker_networks_alias`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_networks_alias: "{{ mkvtoolnix_name }}"
        ```

    ??? variable list "`mkvtoolnix_role_docker_networks_default`"

        ```yaml
        # Type: list
        mkvtoolnix_role_docker_networks_default: []
        ```

    ??? variable list "`mkvtoolnix_role_docker_networks_custom`"

        ```yaml
        # Type: list
        mkvtoolnix_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`mkvtoolnix_role_docker_restart_policy`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`mkvtoolnix_role_docker_state`"

        ```yaml
        # Type: string
        mkvtoolnix_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`mkvtoolnix_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        mkvtoolnix_role_autoheal_enabled: true
        ```

    ??? variable string "`mkvtoolnix_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        mkvtoolnix_role_depends_on: ""
        ```

    ??? variable string "`mkvtoolnix_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        mkvtoolnix_role_depends_on_delay: "0"
        ```

    ??? variable string "`mkvtoolnix_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mkvtoolnix_role_depends_on_healthchecks:
        ```

    ??? variable bool "`mkvtoolnix_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        mkvtoolnix_role_diun_enabled: true
        ```

    ??? variable bool "`mkvtoolnix_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        mkvtoolnix_role_dns_enabled: true
        ```

    ??? variable bool "`mkvtoolnix_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        mkvtoolnix_role_docker_controller: true
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`mkvtoolnix_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        mkvtoolnix_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`mkvtoolnix_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        mkvtoolnix_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            mkvtoolnix_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mkvtoolnix2.{{ user.domain }}"
              - "mkvtoolnix.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`mkvtoolnix_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        mkvtoolnix_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            mkvtoolnix_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mkvtoolnix2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`mkvtoolnix_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        mkvtoolnix_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->