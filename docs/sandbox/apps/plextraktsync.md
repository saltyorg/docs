---
hide:
  - tags
tags:
  - plextraktsync
  - trakt.tv
---

# PlexTraktSync

Self-hosted application that adds a two-way-sync between trakt.tv and Plex Media Server. It requires a trakt.tv account but no Plex premium and no Trakt VIP subscriptions, unlike the Plex app provided by Trakt.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://github.com/Taxel/PlexTraktSync){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/Taxel/PlexTraktSync/blob/main/README.md#setup){ .md-button .md-button--stretch }

[:octicons-container-16: Releases&nbsp;&nbsp;](https://github.com/taxel/PlexTraktSync/pkgs/container/plextraktsync){ .md-button .md-button--stretch }

[:fontawesome-brands-github: Community&nbsp;&nbsp;](https://github.com/Taxel/PlexTraktSync/discussions){ .md-button .md-button--stretch }

</div>

---

## Deployment

``` shell
sb install sandbox-plextraktsync
```

## Configuration

Sync preferences are available to customize in `/opt/plextraktsync/config.yml`.

The following command will launch an interactive script prompting you for missing credentials (use this to set up Trakt.tv):

```shell
docker exec -it plextraktsync plextraktsync login
```

???+ info "Plex"
    The target Plex server is initially set to your main Plex Saltbox instance using the owner account. To reset these credentials:
    ```shell
    docker exec -it plextraktsync plextraktsync plex-login
    ```

## Usage

### Daemon

Once configured, the selected Plex user's streaming activity is automatically scrobbled.

### CLI

To perform a one-time sync of the data you have specified in the configuration file:

```shell
docker exec plextraktsync plextraktsync sync
```

To get a list of available commands:

```shell
docker exec plextraktsync plextraktsync --help
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    plextraktsync_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `plextraktsync_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `plextraktsync_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`plextraktsync_name`"

        ```yaml
        # Type: string
        plextraktsync_name: plextraktsync
        ```

=== "Paths"

    ??? variable string "`plextraktsync_role_paths_folder`"

        ```yaml
        # Type: string
        plextraktsync_role_paths_folder: "{{ plextraktsync_name }}"
        ```

    ??? variable string "`plextraktsync_role_paths_location`"

        ```yaml
        # Type: string
        plextraktsync_role_paths_location: "{{ server_appdata_path }}/{{ plextraktsync_role_paths_folder }}"
        ```

    ??? variable string "`plextraktsync_role_paths_env`"

        ```yaml
        # Type: string
        plextraktsync_role_paths_env: "{{ plextraktsync_role_paths_location }}/.env"
        ```

    ??? variable string "`plextraktsync_role_paths_log`"

        ```yaml
        # Type: string
        plextraktsync_role_paths_log: "{{ plextraktsync_role_paths_location }}/plextraktsync.log"
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`plextraktsync_role_docker_container`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_container: "{{ plextraktsync_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`plextraktsync_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_image_pull: true
        ```

    ??? variable string "`plextraktsync_role_docker_image_tag`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_image_tag: "latest"
        ```

    ??? variable string "`plextraktsync_role_docker_image_repo`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_image_repo: "ghcr.io/taxel/plextraktsync"
        ```

    ??? variable string "`plextraktsync_role_docker_image`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plextraktsync') }}:{{ lookup('role_var', '_docker_image_tag', role='plextraktsync') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`plextraktsync_role_docker_envs_default`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`plextraktsync_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_envs_custom: {}
        ```

    Commands
    { .sb-h5 }

    ??? variable list "`plextraktsync_role_docker_commands_default`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_commands_default: 
          - watch
        ```

    ??? variable list "`plextraktsync_role_docker_commands_custom`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_commands_custom: []
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`plextraktsync_role_docker_volumes_default`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='plextraktsync') }}:/app/config"
        ```

    ??? variable list "`plextraktsync_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`plextraktsync_role_docker_hostname`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_hostname: "{{ plextraktsync_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`plextraktsync_role_docker_networks_alias`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_networks_alias: "{{ plextraktsync_name }}"
        ```

    ??? variable list "`plextraktsync_role_docker_networks_default`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_networks_default: []
        ```

    ??? variable list "`plextraktsync_role_docker_networks_custom`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`plextraktsync_role_docker_restart_policy`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`plextraktsync_role_docker_state`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`plextraktsync_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plextraktsync_role_autoheal_enabled: true
        ```

    ??? variable string "`plextraktsync_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plextraktsync_role_depends_on: ""
        ```

    ??? variable string "`plextraktsync_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plextraktsync_role_depends_on_delay: "0"
        ```

    ??? variable string "`plextraktsync_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plextraktsync_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plextraktsync_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plextraktsync_role_diun_enabled: true
        ```

    ??? variable bool "`plextraktsync_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        plextraktsync_role_dns_enabled: true
        ```

    ??? variable bool "`plextraktsync_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plextraktsync_role_docker_controller: true
        ```

    ??? variable bool "`plextraktsync_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        plextraktsync_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`plextraktsync_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        plextraktsync_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`plextraktsync_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        plextraktsync_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`plextraktsync_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        plextraktsync_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`plextraktsync_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`plextraktsync_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`plextraktsync_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        plextraktsync_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`plextraktsync_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        plextraktsync_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`plextraktsync_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        plextraktsync_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`plextraktsync_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        plextraktsync_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            plextraktsync_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plextraktsync2.{{ user.domain }}"
              - "plextraktsync.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`plextraktsync_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        plextraktsync_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            plextraktsync_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plextraktsync2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`plextraktsync_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        plextraktsync_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->