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

[tqm](https://github.com/autobrr/tqm) is a CLI (Command Line Interface) tool designed to manage torrent client queues, with a primary focus on automatically removing torrents that meet specific user-defined criteria.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/autobrr/tqm/blob/main/README.md){ .md-button .md-button--stretch }

[:material-tag:**Releases**](https://github.com/autobrr/tqm/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.autobrr.com){ .md-button .md-button--stretch }

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
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
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
<!-- END SALTBOX MANAGED VARIABLES SECTION -->