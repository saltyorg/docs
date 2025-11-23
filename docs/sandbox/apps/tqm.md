---
icon: material/server-network-outline
hide:
  - tags
tags:
  - tqm
  - torrent
  - automation
---

# tqm

## Overview

> [tqm](https://github.com/autobrr/tqm) is a CLI (Command Line Interface) tool designed to manage torrent client queues, with a primary focus on automatically removing torrents that meet specific user-defined criteria.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-home:**Homepage**](https://autobrr.com/3rd-party-tools/manage-torrents#tqm){ .md-button .md-button--stretch }

[:material-bookshelf:**Manual**](https://github.com/autobrr/tqm/blob/main/README.md){ .md-button .md-button--stretch }

[:material-tag:**Releases**](https://github.com/autobrr/tqm/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.autobrr.com/){ .md-button .md-button--stretch }

</div>

---

???+ warning "Sandbox `settings.yml` Deprecation"

    As of ***role-refactor***, `settings.yml` is no longer used to configure Sandbox roles. Values currently set in `/opt/sandbox/settings.yml` must be migrated to their Inventory form. See [Role Defaults](#role-defaults) for the expected syntax.

## Configuration

1.  Set your download client via the Inventory override.

1.  Edit `/opt/tqm/config.yaml`.  

Use Saltbox paths (`/mnt/unionfs/downloads/...`) for `download_path` as per [Saltbox media paths](../../saltbox/basics/paths.md#media).

**Example client config:**

```yaml
deluge:
  enabled: false
  download_path: /mnt/unionfs/downloads/torrents/deluge
  free_space_path: /mnt/local/downloads/torrents/deluge
  download_path_mapping:
    /downloads/torrents/deluge: /mnt/unionfs/downloads/torrents/deluge
  host: deluge
  login: localclient
  password: password-from-/opt/deluge/auth
  port: 58846
  type: deluge
  v2: true
qbt:
  enabled: true
  download_path: /mnt/unionfs/downloads/torrents/qbittorrent/completed
  free_space_path: /mnt/local/downloads/torrents/qbittorrent/completed
  download_path_mapping:
    /mnt/unionfs/downloads/torrents/qbittorrent/completed: /mnt/unionfs/downloads/torrents/qbittorrent/completed
  type: qbittorrent
  url: http://qbittorrent:8080
  user: seed
  password: super_strong_password
```

See the [main documentation](https://github.com/autobrr/tqm#example-configuration) for full configuration and filter options.

## Deployment

```shell
sb install sandbox-tqm
```

## Usage

Check service status:

```shell
sudo systemctl status tqm.service
```

View logs:

```shell
tail -f /opt/tqm/activity.log
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    tqm_name: "custom_value"
    ```

=== "Basics"

    ??? variable string "`tqm_name`"

        ```yaml
        # Type: string
        tqm_name: tqm
        ```

=== "Paths"

    ??? variable string "`tqm_role_paths_folder`"

        ```yaml
        # Type: string
        tqm_role_paths_folder: "{{ tqm_name }}"
        ```

    ??? variable string "`tqm_role_paths_location`"

        ```yaml
        # Type: string
        tqm_role_paths_location: "{{ server_appdata_path }}/{{ tqm_role_paths_folder }}"
        ```

    ??? variable string "`tqm_role_paths_config_location`"

        ```yaml
        # Type: string
        tqm_role_paths_config_location: "{{ tqm_role_paths_location }}/config.yaml"
        ```

    ??? variable string "`tqm_role_paths_service_location`"

        ```yaml
        # Type: string
        tqm_role_paths_service_location: "/etc/systemd/system/tqm.service"
        ```

    ??? variable string "`tqm_role_paths_timer_location`"

        ```yaml
        # Type: string
        tqm_role_paths_timer_location: "/etc/systemd/system/tqm.timer"
        ```

=== "Global Override Options"

    ??? variable bool "`tqm_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tqm_role_autoheal_enabled: true
        ```

    ??? variable string "`tqm_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tqm_role_depends_on: ""
        ```

    ??? variable string "`tqm_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tqm_role_depends_on_delay: "0"
        ```

    ??? variable string "`tqm_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tqm_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tqm_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tqm_role_diun_enabled: true
        ```

    ??? variable bool "`tqm_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tqm_role_dns_enabled: true
        ```

    ??? variable bool "`tqm_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tqm_role_docker_controller: true
        ```

    ??? variable bool "`tqm_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        tqm_role_docker_volumes_download:
        ```

    ??? variable bool "`tqm_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tqm_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`tqm_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tqm_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tqm_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tqm_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tqm_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tqm_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`tqm_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tqm_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tqm_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tqm_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`tqm_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tqm_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tqm_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tqm_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tqm_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tqm_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`tqm_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tqm_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            tqm_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tqm2.{{ user.domain }}"
              - "tqm.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`tqm_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tqm_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            tqm_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tqm2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`tqm_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tqm_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->