---
icon: material/cogs
title: MOTD
status: draft
saltbox_automation:
  project_description:
    name: MOTD
    summary: |-
      a Saltbox module that enhances the Message of the Day (MOTD) displayed upon user login to provide personalized information.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# MOTD

## Overview

MOTD is a Saltbox module that enhances the Message of the Day (MOTD) displayed upon user login to provide personalized information.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->


## Deployment

```shell
sb install motd
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        motd_install: true
        ```

=== "Basics"

    ??? variable bool "`motd_install`"

        ```yaml
        # Setting this to false will skip the motd management and you can manage it manually
        # Type: bool (true/false)
        motd_install: true
        ```

    ??? variable bool "`motd_use_python`"

        ```yaml
        # Setting this to true will switch back to the old python motd
        # Type: bool (true/false)
        motd_use_python: false
        ```

    ??? variable string "`motd_cli_path`"

        ```yaml
        # Type: string
        motd_cli_path: "/usr/local/bin/sb"
        ```

    ??? variable string "`motd_cli_flags`"

        ```yaml
        # Run sb motd --help to view what you can customize in terms of flags
        # Type: string
        motd_cli_flags: "--all --title 'Saltbox' --font ivrit --type parchment"
        ```

=== "Service Definitions"

    ??? variable list "`motd_services`"

        ```yaml
        # Service types:
        # - multi_instance_apikey: Multiple instances with API key (sonarr, radarr, lidarr, readarr, overseerr)
        # - multi_instance_token: Multiple instances with token (plex)
        # - single_instance_apikey: Single instance with API key (sabnzbd)
        # - single_instance_userpass: Single instance with username/password (nzbget)
        # - multi_instance_userpass: Multiple instances with username/password (qbittorrent)
        # - disabled: Statically disabled services (jellyfin, emby, rtorrent)
        # Type: list
        motd_services:
          - name: colors
            type: colors
          - name: emby
            type: multi_instance_token
            check_field: token
            output_field: token
          - name: jellyfin
            type: multi_instance_token
            check_field: token
            output_field: token
          - name: lidarr
            type: multi_instance_apikey
            check_field: api_key
            output_field: apikey
          - name: nzbget
            type: single_instance_userpass
            check_field: username
          - name: plex
            type: multi_instance_token
            check_field: token
            output_field: token
          - name: qbittorrent
            type: multi_instance_userpass_info
            check_field: username
          - name: radarr
            type: multi_instance_apikey
            check_field: api_key
            output_field: apikey
          - name: sabnzbd
            type: single_instance_apikey
            check_field: api_key
            output_field: apikey
          - name: sonarr
            type: multi_instance_apikey
            check_field: api_key
            output_field: apikey
          - name: systemd
            type: systemd
        ```

    ??? variable dict "`motd_colors`"

        ```yaml
        # Type: dict
        motd_colors:
          text:
            label: "#FF79D0"
            value: "#12C78F"
            app_name: "#BF976F"
          status:
            warning: "#F5EF34"
            success: "#12C78F"
            error: "#EB4268"
          progress_bar:
            low: "#A8CC8C"
            high: "#DBAB79"
            critical: "#E88388"
        ```

    ??? variable dict "`motd_systemd`"

        ```yaml
        # Type: dict
        motd_systemd:
          enabled: true
          additional_services: []
          display_names: {}
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
