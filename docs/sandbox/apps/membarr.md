---
hide:
  - tags
tags:
  - membarr
  - discord
  - automation
---

# Membarr

## What is it?

[Membarr](https://github.com/Yoruio/Membarr) is a fork of Invitarr that invites discord users to Plex and Jellyfin. You can also automate this bot to invite discord users to a media server once a certain role is given to a user or the user can also be added manually.

***Features*** are:

- Ability to invite users to Plex and Jellyfin from discord
- Fully automatic invites using roles
- Ability to kick users from plex if they leave the discord server or if their role is taken away.
- Ability to view the database in discord and to edit it.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Yoruio/Membarr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Yoruio/Membarr){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Yoruio/Membarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/yoruio/membarr){: .header-icons }|

## Setup Membarr

### 1. Create Discord bot

1. Create the Discord server that your users will get member roles or use an existing discord that you can assign roles from.
2. Log into the [Discord Developer Portal] and click 'New Application'
3. Add a short description and an icon for the bot. Save changes. *(Optional)*
4. Go to **Bot** section in the side menu.
5. Uncheck 'Public Bot' under **Authorization Flow**
6. Check all 3 boxes under Privileged Gateway Intents: **Presence Intent**, **Server Members Intent**, and **Message Content Intent**. Save changes.
7. Copy the token under the username or reset it to copy. This is the token used in the docker image.
8. Go to **OAuth2** section in the side menu, then click **URL Generator**.
9. Under **Scopes**, check **bot** and **applications.commands**.
10. Copy the **Generated URL** and paste into your browser and add it to your discord server from Step 1.
11. The bot will come online after the docker container is running with the correct Bot Token.

  [Discord Developer Portal]: https://discord.com/developers/applications

### 2. Installation

``` shell

sb install sandbox-membarr

```

### 3. Set up Plex parameters

When you install the role, it will create 2 files, an `app.db` file and `config.ini`. You will need to edit the `config.ini` file with your preferred editing program. (ie `nano` or `vim` etc) Add your Plex credentials like so:

``` toml
[bot_envs]
plex_user =
plex_pass =
plex_server_name = ServerFriendlyName
plex_roles =
plex_token = token
plex_base_url = https://plex.xYOUR_DOMAIN_NAMEx
plex_enabled = True
```

Now restart the Membarr container `docker restart membarr`.

???+ Success "Plex Token"
    To get the Plex token, you will run the following command: `sb install plex-auth-token`
    Look for the **Display Plex Auth Token** task in the log.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    membarr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `membarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `membarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`membarr_name`"

        ```yaml
        # Type: string
        membarr_name: membarr
        ```

=== "Paths"

    ??? variable string "`membarr_role_paths_folder`"

        ```yaml
        # Type: string
        membarr_role_paths_folder: "{{ membarr_name }}"
        ```

    ??? variable string "`membarr_role_paths_location`"

        ```yaml
        # Type: string
        membarr_role_paths_location: "{{ server_appdata_path }}/{{ membarr_role_paths_folder }}"
        ```

    ??? variable bool "`membarr_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_paths_recursive: true
        ```

    ??? variable string "`membarr_role_paths_config_location`"

        ```yaml
        # Type: string
        membarr_role_paths_config_location: "{{ membarr_role_paths_location }}/config.ini"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`membarr_role_docker_container`"

        ```yaml
        # Type: string
        membarr_role_docker_container: "{{ membarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`membarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_image_pull: true
        ```

    ??? variable string "`membarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        membarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`membarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        membarr_role_docker_image_repo: "yoruio/membarr"
        ```

    ??? variable string "`membarr_role_docker_image`"

        ```yaml
        # Type: string
        membarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='membarr') }}:{{ lookup('role_var', '_docker_image_tag', role='membarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`membarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        membarr_role_docker_envs_default: 
          TZ: "{{ tz }}"
          token: "{{ membarr.discord_token }}"
        ```

    ??? variable dict "`membarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        membarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`membarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        membarr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='membarr') }}:/app/app/config"
        ```

    ??? variable list "`membarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        membarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`membarr_role_docker_hostname`"

        ```yaml
        # Type: string
        membarr_role_docker_hostname: "{{ membarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`membarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        membarr_role_docker_networks_alias: "{{ membarr_name }}"
        ```

    ??? variable list "`membarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        membarr_role_docker_networks_default: []
        ```

    ??? variable list "`membarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        membarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`membarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        membarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`membarr_role_docker_state`"

        ```yaml
        # Type: string
        membarr_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`membarr_role_docker_user`"

        ```yaml
        # Type: string
        membarr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`membarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        membarr_role_autoheal_enabled: true
        ```

    ??? variable string "`membarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        membarr_role_depends_on: ""
        ```

    ??? variable string "`membarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        membarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`membarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        membarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`membarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        membarr_role_diun_enabled: true
        ```

    ??? variable bool "`membarr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        membarr_role_dns_enabled: true
        ```

    ??? variable bool "`membarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        membarr_role_docker_controller: true
        ```

    ??? variable bool "`membarr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        membarr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`membarr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        membarr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`membarr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        membarr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`membarr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        membarr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`membarr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`membarr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`membarr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        membarr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`membarr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        membarr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`membarr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        membarr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`membarr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        membarr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            membarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "membarr2.{{ user.domain }}"
              - "membarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`membarr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        membarr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            membarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'membarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`membarr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        membarr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->