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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        plextraktsync_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    plextraktsync_name: plextraktsync

    ```

??? example "Paths"

    ```yaml
    # Type: string
    plextraktsync_role_paths_folder: "{{ plextraktsync_name }}"

    # Type: string
    plextraktsync_role_paths_location: "{{ server_appdata_path }}/{{ plextraktsync_role_paths_folder }}"

    # Type: string
    plextraktsync_role_paths_env: "{{ plextraktsync_role_paths_location }}/.env"

    # Type: string
    plextraktsync_role_paths_log: "{{ plextraktsync_role_paths_location }}/plextraktsync.log"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    plextraktsync_role_docker_container: "{{ plextraktsync_name }}"

    # Image
    # Type: bool (true/false)
    plextraktsync_role_docker_image_pull: true

    # Type: string
    plextraktsync_role_docker_image_tag: "latest"

    # Type: string
    plextraktsync_role_docker_image_repo: "ghcr.io/taxel/plextraktsync"

    # Type: string
    plextraktsync_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plextraktsync') }}:{{ lookup('role_var', '_docker_image_tag', role='plextraktsync') }}"

    # Envs
    # Type: dict
    plextraktsync_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    plextraktsync_role_docker_envs_custom: {}

    # Commands
    # Type: list
    plextraktsync_role_docker_commands_default: 
      - watch

    # Type: list
    plextraktsync_role_docker_commands_custom: []

    # Volumes
    # Type: list
    plextraktsync_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='plextraktsync') }}:/app/config"

    # Type: list
    plextraktsync_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    plextraktsync_role_docker_hostname: "{{ plextraktsync_name }}"

    # Networks
    # Type: string
    plextraktsync_role_docker_networks_alias: "{{ plextraktsync_name }}"

    # Type: list
    plextraktsync_role_docker_networks_default: []

    # Type: list
    plextraktsync_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    plextraktsync_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    plextraktsync_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    plextraktsync_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    plextraktsync_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    plextraktsync_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    plextraktsync_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    plextraktsync_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    plextraktsync_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    plextraktsync_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    plextraktsync_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    plextraktsync_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    plextraktsync_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    plextraktsync_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    plextraktsync_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    plextraktsync_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    plextraktsync_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    plextraktsync_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    plextraktsync_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    plextraktsync_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        plextraktsync_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "plextraktsync2.{{ user.domain }}"
          - "plextraktsync.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        plextraktsync_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plextraktsync2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
