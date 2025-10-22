---
hide:
  - tags
tags:
  - doplarr
  - media
  - discord
---

# Doplarr

## What is it?

[Doplarr](https://kiranshila.github.io/Doplarr/#/) is a chatbot used to simplify using services like Sonarr/Radarr/Overseer via the use of chat. Current platform is Discord only.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://kiranshila.github.io/Doplarr/#/){: .header-icons } | [:octicons-link-16: Docs](https://kiranshila.github.io/Doplarr/#/configuration){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/kiranshila/doplarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/doplarr){: .header-icons }|

## Setup Doplarr

### 1. Create Discord bot

1. Create a new [Application](https://discord.com/developers/applications) in Discord
2. Go to the Bot tab and add a new bot
3. Copy the token and paste it in `/opt/sandbox/settings.yml` in the `doplarr.discord_token` field:

    ```yaml hl_lines="3" title="/opt/sandbox/settings.yml"
    ...
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ...
    ```

4. Go to OAuth2 and under "OAuth2 URL Generator", enable `applications.commands` and `bot`
5. Copy the resulting URL and open it in your browser in order to invite your bot to your discord channel.

### 2. Set up overseer parameters

1. In `/opt/sandbox/settings.yml` : set up the overseer url in the corresponding field `doplarr.overseerr_url` according to your setings. If you have not customize saltbox settings, the default url `http://overseerr:5055` should be correct:

    ```yaml hl_lines="4" title="/opt/sandbox/settings.yml"
    ...
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ...
    ```

2. In `/opt/sandbox/settings.yml` : set up the overseer API key in the corresponding field `doplarr.overseerr_api` according to your overseer settings.
You can get your api keys in your main setting page in overseer: `https://overseerr.xDOMAIN_NAMEx/settings`:

    ```yaml hl_lines="5" title="/opt/sandbox/settings.yml"
    ...
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ...
    ```

### 3. Installation

``` shell

sb install sandbox-doplarr

```

!!! note
      📢 You may also override the default setting of Doplarr working with overseer, to work with Sonarr and Radarr.
      The recommended way to customize these parameters is to use the [inventory](../../saltbox/inventory/index.md). You should edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section.

    ``` yaml title="Inventory"
    doplarr_docker_envs_defaults:
      SONARR__URL: # (1)!
      RADARR__URL: # (2)!
      SONARR__API: # (3)!
      RADARR__API: # (4)!
      DISCORD__TOKEN: # (5)!
    ```

    1. This line will set the Sonarr URL. Saltbox defaults to `"http://sonarr:8989"`.
    2. This line will set the Radarr URL. Saltbox defaults to `"http://radarr:7878"`.
    3. This line will set the Sonarr API key. Place your API key here. Wrap it in quotes.
    4. This line will set the Radarr API key. Place your API key here. Wrap it in quotes.
    5. This line will set the Discord token. Place your token here. Wrap it in quotes.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        doplarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `doplarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `doplarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    doplarr_name: doplarr

    ```

??? example "Settings"

    ```yaml
    # Type: string
    doplarr_role_discord_token: ""

    # Type: string
    doplarr_role_overseerr_url: ""

    # Type: string
    doplarr_role_overseerr_api: ""

    # Type: string
    doplarr_role_radarr_api: ""

    # Type: string
    doplarr_role_radarr_url: ""

    # Type: string
    doplarr_role_sonarr_api: ""

    # Type: string
    doplarr_role_sonarr_url: ""

    # Type: string
    doplarr_role_discord_max_results: "25"

    # Type: string
    doplarr_role_discord_role_id: ""

    # Type: string
    doplarr_role_discord_requested_msg_style: ":plain"

    # Type: string
    doplarr_role_sonarr_quality_profile: ""

    # Type: string
    doplarr_role_radarr_quality_profile: ""

    # Type: string
    doplarr_role_sonarr_language_profile: ""

    # Type: string
    doplarr_role_overseer_default_id: ""

    # Type: string
    doplarr_role_partial_seasons: "true"

    # Type: string
    doplarr_role_log_level: ":info"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    doplarr_role_docker_container: "{{ doplarr_name }}"

    # Image
    # Type: bool (true/false)
    doplarr_role_docker_image_pull: true

    # Type: string
    doplarr_role_docker_image_repo: "lscr.io/linuxserver/doplarr"

    # Type: string
    doplarr_role_docker_image_tag: "latest"

    # Type: string
    doplarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='doplarr') }}:{{ lookup('role_var', '_docker_image_tag', role='doplarr') }}"

    # Envs
    # Type: dict
    doplarr_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      DISCORD__TOKEN: "{{ lookup('role_var', '_discord_token', role='doplarr') }}"
      OVERSEERR__URL: "{{ lookup('role_var', '_overseerr_url', role='doplarr') }}"
      OVERSEERR__API: "{{ lookup('role_var', '_overseerr_api', role='doplarr') }}"
      RADARR__API: "{{ lookup('role_var', '_radarr_api', role='doplarr') }}"
      RADARR__URL: "{{ lookup('role_var', '_radarr_url', role='doplarr') }}"
      SONARR__API: "{{ lookup('role_var', '_sonarr_api', role='doplarr') }}"
      SONARR__URL: "{{ lookup('role_var', '_sonarr_url', role='doplarr') }}"
      DISCORD__MAX_RESULTS: "{{ lookup('role_var', '_discord_max_results', role='doplarr') }}"
      DISCORD__ROLE_ID: "{{ lookup('role_var', '_discord_role_id', role='doplarr') }}"
      DISCORD__REQUESTED_MSG_STYLE: "{{ lookup('role_var', '_discord_requested_msg_style', role='doplarr') }}"
      SONARR__QUALITY_PROFILE: "{{ lookup('role_var', '_sonarr_quality_profile', role='doplarr') }}"
      RADARR__QUALITY_PROFILE: "{{ lookup('role_var', '_radarr_quality_profile', role='doplarr') }}"
      SONARR__LANGUAGE_PROFILE: "{{ lookup('role_var', '_sonarr_language_profile', role='doplarr') }}"
      OVERSEERR__DEFAULT_ID: "{{ lookup('role_var', '_overseer_default_id', role='doplarr') }}"
      PARTIAL_SEASONS: "{{ lookup('role_var', '_partial_seasons', role='doplarr') }}"
      LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='doplarr') }}"

    # Type: list
    doplarr_role_docker_envs_custom: []

    # Hostname
    # Type: string
    doplarr_role_docker_hostname: "{{ doplarr_name }}"

    # Networks
    # Type: string
    doplarr_role_docker_networks_alias: "{{ doplarr_name }}"

    # Type: list
    doplarr_role_docker_networks_default: []

    # Type: list
    doplarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    doplarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    doplarr_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    doplarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    doplarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    doplarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    doplarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    doplarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    doplarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    doplarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    doplarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    doplarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    doplarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    doplarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    doplarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    doplarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    doplarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    doplarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    doplarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    doplarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        doplarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "doplarr2.{{ user.domain }}"
          - "doplarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        doplarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'doplarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
