---
hide:
  - tags
tags:
  - mylar3
  - media
  - comics
---

# Mylar3

## What is it?

[Mylar3](https://github.com/mylar3/mylar3) is an automated Comic Book downloader (cbr/cbz) for use with SABnzbd, NZBGet and torrents. Also provides an OPDS server distribution.

Mylar allows you to create a watchlist of series that it monitors for various things (new issues, updated information, etc). It will grab, sort, and rename downloaded issues. It will also allow you to monitor weekly pull-lists for items belonging to said watchlisted series to download, as well as being able to monitor and maintain story-arcs.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/mylar3/mylar3){: .header-icons } | [:octicons-link-16: Docs](https://github.com/mylar3/mylar3/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/mylar3/mylar3){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/mylar3){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-mylar3

```

### 2. URL

- To access Mylar3, visit `https://mylar3._yourdomain.com_`

### 3. Setup

1. It's highly unlikely your mylar install is up to date. <br />
  Press the Update link on the dialog in the bottom right hand corner. Mylar3 will update and then restart.

2. Enable some authentication. Add a `username` and `password` and set your preferred `login method`.

3. Make sure `Launch Browser on startup` is disabled.

4. You'll need a [ComicVine API](https://comicvine.gamespot.com/api/) Key for Mylar to be useful. [Create an account](https://comicvine.gamespot.com/login-signup/), and your key will be at [the top of this page](https://comicvine.gamespot.com/api/).

5. Set the Comic Location path to `/comics`. It will already be mounted.

6. Uncheck `enforce permissions`

7. _Optional_: Enable `Series-Annual Integration`

8. Save and then restart the app

!!! note
      If you enable to OPDS server, DO NOT ENABLE `OPDS Fetch MetaInfo`. It queries the file system.

### Download settings

(These instructions are for NZBGet. Adapt for other Download Apps)

#### Configure NZBGet

1. Log into `https://nzbget._youdomain_.com`

2. Go to `Settings > Categories`

3. Scroll to bottom, click `Add Another Category`

4. Name it `mylar`

#### Configure Mylar

1. Set Usenet client to NZBGet

1. Fill in the server stuff like it would be in sonarr / radarr / etc

1. Set values:

   1. Host: `nzbget`

   1. Port: `6789`

   1. Username:  `Your NZBGet Username`

   1. Password:  `Your NZBGet Password`

   1. Category: `mylar`

   1. Use SSL: `No`

   1. NZBGet Download Directory: Leave Blank

   1. Enable Completed Download Handling: `X`

### Search Providers

1. Click Add Indexer (`+`).

1. Select "Newznab".

1. Add the following:

      1. Use Newznab: `X`

      2. NewzNab Name: `NZBHydra2`

      3. NewzNab Host: `http://nzbhydra2:5076`

      4. Verify SSL: `Disabled`

      5. API Key: `Your NZBHydra2 API Key`

      6. Enabled: `X`

### Quality and Post Processing

1. Enable Failed Download Handling: `X`

1. Enable Automatic-Retry for Failed Downloads: `X`

1. Enable Post-Processing: `X`

1. When Post-Processing `move` the files

### Advanced Settings

These settings are up to the user

1. Rename Files: `X`

1. Folder Format: `$Series ($Year)` _(My recommendation)_

1. File Format: `$Series $Annual $Issue ($Year)` _(My recommendation)_

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        mylar3_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    mylar3_name: mylar3

    ```

??? example "Paths"

    ```yaml
    # Type: string
    mylar3_role_paths_folder: "{{ mylar3_name }}"

    # Type: string
    mylar3_role_paths_location: "{{ server_appdata_path }}/{{ mylar3_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    mylar3_role_web_subdomain: "{{ mylar3_name }}"

    # Type: string
    mylar3_role_web_domain: "{{ user.domain }}"

    # Type: string
    mylar3_role_web_port: "8090"

    # Type: string
    mylar3_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='mylar3') + '.' + lookup('role_var', '_web_domain', role='mylar3')
                          if (lookup('role_var', '_web_subdomain', role='mylar3') | length > 0)
                          else lookup('role_var', '_web_domain', role='mylar3')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    mylar3_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='mylar3') }}"

    # Type: string
    mylar3_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='mylar3') }}"

    # Type: bool (true/false)
    mylar3_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    mylar3_role_traefik_sso_middleware: ""

    # Type: string
    mylar3_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    mylar3_role_traefik_middleware_custom: ""

    # Type: string
    mylar3_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    mylar3_role_traefik_enabled: true

    # Type: bool (true/false)
    mylar3_role_traefik_api_enabled: false

    # Type: string
    mylar3_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    mylar3_role_docker_container: "{{ mylar3_name }}"

    # Image
    # Type: bool (true/false)
    mylar3_role_docker_image_pull: true

    # Type: string
    mylar3_role_docker_image_tag: "latest"

    # Type: string
    mylar3_role_docker_image_repo: "lscr.io/linuxserver/mylar3"

    # Type: string
    mylar3_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mylar3') }}:{{ lookup('role_var', '_docker_image_tag', role='mylar3') }}"

    # Envs
    # Type: dict
    mylar3_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    mylar3_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    mylar3_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='mylar3') }}:/config"
      - "/mnt/unionfs/Media/Comics:/comics"

    # Type: list
    mylar3_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    mylar3_role_docker_hostname: "{{ mylar3_name }}"

    # Networks
    # Type: string
    mylar3_role_docker_networks_alias: "{{ mylar3_name }}"

    # Type: list
    mylar3_role_docker_networks_default: []

    # Type: list
    mylar3_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    mylar3_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    mylar3_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    mylar3_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    mylar3_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    mylar3_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    mylar3_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    mylar3_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    mylar3_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    mylar3_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    mylar3_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    mylar3_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    mylar3_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    mylar3_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    mylar3_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    mylar3_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    mylar3_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    mylar3_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    mylar3_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    mylar3_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        mylar3_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "mylar32.{{ user.domain }}"
          - "mylar3.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        mylar3_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mylar32.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
