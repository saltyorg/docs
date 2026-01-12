---
icon: material/server-network-outline
title: tqm
hide:
  - tags
tags:
  - tqm
  - torrent
  - automation 
saltbox_automation:
  app_links:
  - name: Manual
    url: https://autobrr.com/3rd-party-tools/manage-torrents#tqm
    type: documentation
  - name: Releases
    url: https://github.com/autobrr/tqm/tags
    type: github
  - name: Community
    url: https://discord.autobrr.com
    type: discord
  project_description:
    name: tqm
    summary: |
      a command-line tool designed to manage torrent client queues, with a primary focus on automatically removing torrents that meet specific user-defined criteria.
    link: https://github.com/autobrr/tqm
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# tqm

## Overview

[tqm](https://github.com/autobrr/tqm) is a command-line tool designed to manage torrent client queues, with a primary focus on automatically removing torrents that meet specific user-defined criteria.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://autobrr.com/3rd-party-tools/manage-torrents#tqm){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/autobrr/tqm/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.autobrr.com){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

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

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        tqm_name: "custom_value"
        ```

=== "Basics"

    ??? variable string "`tqm_name`"

        ```yaml
        # Type: string
        tqm_name: tqm
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->