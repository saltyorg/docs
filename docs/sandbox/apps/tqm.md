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

[tqm](https://github.com/autobrr/tqm) is a CLI tool to manage your torrent client queues. Primary focus is on removing torrents that meet specific criteria.

- The tqm binary is downloaded and a service and timer file created when the config is identified.

!!! note
      📢 You will need to have `config.yaml` in place (`/opt/tqm/`) for the role to run successfully. [Here](https://github.com/autobrr/tqm#example-configuration) is an example config you can grab and fill in with your own details.

| Details     |
|-------------|
| [:octicons-mark-github-16: Github](https://github.com/autobrr/tqm){: .header-icons }|

Recommended install types: Feederbox, Saltbox, Core

### 1. Setup

Edit in your favorite code editor  (with yaml highlighting) or even a unix editor like nano.

```shell
nano /opt/tqm/config.yaml
```

### Modify "Client" section

!!! note
      📢 As setup for Saltbox, tqm uses this path to find your downloaded files:  `/mnt/unionfs/downloads/...` (see [Paths](../../saltbox/basics/paths.md#media))

Client Example:

```yaml
...
  deluge:
    enabled: false
    filter: default
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
    download_path: /mnt/unionfs/downloads/torrents/qbittorrent/completed
    free_space_path: /mnt/local/downloads/torrents/qbittorrent/completed
    download_path_mapping:
      /mnt/unionfs/downloads/torrents/qbittorrent/completed: /mnt/unionfs/downloads/torrents/qbittorrent/completed
    enabled: true
    filter: default
    type: qbittorrent
    url: http://qbittorrent:8080
    user: seed
    password: super_strong_password
...
```

`download_path:` Where your downloaded files are stored.

`free_space_path:` Typically the local mergerfs path to show available space.

`enabled:` Set to boolean value (true, false) depending on the client you use.

`url:` Set to the examples equivalent of your client.

`user:` your default user from **accounts.yml**

`password:` your default password from **accounts.yml**

### Modify "Filter" section

Filter Example:

```yaml
...
filters:
  default:
    ignore:
      - TrackerName contains "sportscult"
      - TrackerStatus contains "Tracker is down"
      - Label contains "upload"
      - Downloaded == false && !IsUnregistered()
    remove:
      - IsUnregistered()
      - Label contains "-imported" && TrackerName contains "avistaz.to" && (Ratio > 2.0 || SeedingDays >= 21.0)
      - Label contains "-imported" && TrackerName contains "nebulance.io" && SeedingDays >= 6.0
      - Label in ["lidarr-imported"] && (Ratio > 5.0 || SeedingDays >= 25.0)
      - Label in ["autoremove-btn"] && (Ratio > 3.0 || SeedingDays >= 15.0)
...
```

`ignore:` Instructs **tqm** to ignore anything defined.

`remove:` Instructs **tqm** what files to delete based on what is defined in the **filter**.

Note: There are many ways to do the same thing. Check the **language definitions** for an explanation [here](https://github.com/antonmedv/expr/blob/586b86b462d22497d442adbc924bfb701db3075d/docs/Language-Definition.md){: .header-icons }

### Modify "Label" section

Label Example:

```yaml
...
    label:
      # Permaseed Animebytes torrents (all must evaluate to true)
      - name: permaseed-AB
        update:
          - SeedingSeconds > 1000.0
          - Label contains "-imported"
          - TrackerName contains "animebytes.tv"
      # cleanup btn season packs to autoremove-btn (all must evaluate to true)
      - name: autoremove-btn
        update:
          - Label == "sonarr-imported"
          - TrackerName == "landof.tv"
          - not (Name contains "1080p")
          - len(Files) >= 3
...
```

!!! note
      📢 tqm will not create a category for you, so be sure to create the category first. If you
      want the file moved as well, you will need to set **Default Torrent Management Mode: Automatic**.

`name:` The category (label) you want the torrent changed to.

`update:` Define what is to be moved by tqm.

### Modify the "Settings" file

You can edit the **settings.yml** file in `/opt/sandbox/`. The default is `qbt`, for qbittorrent. If you want to use deluge, change that entry. Once you set your download client, run the role again and it will update the service.

Shortened example of **settings.yml**:

```yaml
...
tandoor:
  secret_key:
tqm:
  download_client: "qbt" # Change this to deluge or whatever you specify in config.yaml
transmissionvpn:
  vpn_user:
  vpn_pass:
  vpn_prov:
...
```

### 2. Installation

```shell
sb install sandbox-tqm
```

To check the status of the service, you can run:

```shell
sudo systemctl status tqm.service
```

You can also follow the logs with:

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