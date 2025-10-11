---
hide:
  - tags
tags:
  - qbit-manage
  - torrent
  - automation
---

# qBit Manage

## What is it?

[qBit Manage](https://github.com/StuffAnThings/qbit_manage) is a program used to manage your qBittorrent instance.

### Features

- Tag torrents based on tracker and then set seed goals/limit upload speed by tag
- Update categories based on save directory
- Remove unregistered torrents (delete data & torrent if it is not being cross-seeded, otherwise it will just remove the torrent)
- Automatically add cross-seed torrents in paused state (*Note: cross-seed now allows for torrent injections directly to qBit, making this feature obsolete*)
- Recheck paused torrents sorted by lowest size and resume if completed
- Remove orphaned files from your root directory that are not referenced by qBittorrent
- Tag any torrents that have no hard links and allows optional cleanup to delete these torrents and contents based on maximum ratio and/or time seeded
- RecycleBin function to move files into a RecycleBin folder instead of deleting the data directly when deleting a torrent
- Built-in scheduler to run the script every x minutes (Can use --run command to run without the scheduler)
- Webhook notifications with Notifiarr and Apprise API integration
- Web interface for monitoring and management

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/StuffAnThings/qbit_manage){: .header-icons } | [:octicons-link-16: Docs](https://github.com/StuffAnThings/qbit_manage/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/StuffAnThings/qbit_manage){: .header-icons } | [:material-docker: Docker](https://hotio.dev/containers/qbitmanage/){: .header-icons } |

### 1. Installation

Before installing qBit Manage, you should have a **[qBittorrent](../../apps/qbittorrent.md)** instance running on your local machine.

``` shell

sb install sandbox-qbit-manage

```

### 2. URL

- To access qBit Manage, visit `https://qbit-manage._yourdomain.com_`

### 3. Setup

After installation has finished, stop the qbit-manage docker container and edit the config file that will have been created at `/opt/qbit-manage/config.yml`

```shell
docker stop qbit-manage
```

Minimally you will need to change the following items in order to connect with your qBittorrent instance:-

```yaml
    qbt:
      host: "qbittorrent:8080"
      user: "qbittorrent_username"
      pass: "qbittorrent_password"

    directory:
      cross_seed: "/your/path/here/"
      root_dir: "/mnt/unionfs/downloads/torrents/qbittorrent/completed/"
      remote_dir: "/mnt/unionfs/torrents/your/path/here/"
```

An indepth explanation of the config file settings can [be found here.](https://github.com/StuffAnThings/qbit_manage/wiki/Config-Setup#config-file)

The config file is full of examples that more than likely will not work for you, sections you aren't using can be safely commented out or left blank. An up to date example configuration file [can be found here](https://github.com/StuffAnThings/qbit_manage/blob/master/config/config.yml.sample) when you wish to add newer features or restore a self mangled section. YAML spacing matters.

After making adjustments to the config file, you can start the docker container again.

```shell
docker start qbit-manage
```

Either tail the log ( `tail -f "/opt/qbit-manage/logs/activity.log"` ) or open the log file after a few minutes to check for any errors or behaviour that may have been unexpected. The container has been deliberately set to **DRY RUN MODE** initially so you can see what the script will do without actually moving deleting, tagging, or categorising anything.. Once you are happy your life's work will not be destroyed and any errors have been resolved you can edit the qbit_manage variables in the sandbox settings.yml file and then run the role again. Set `qbt_dry_run: false` to run in live mode. This will delete and move files according to your settings.

Apply the changes to the sandbox settings file with:

``` shell

sb install sandbox-qbit-manage

```

### 4. Configuration

The following variables are available to set in the sandbox settings.yml file. An explanation of [these settings can be found here](https://github.com/StuffAnThings/qbit_manage/wiki/Docker-Installation).

```yaml
qbit_manage:
  qbt_run: "false" # Default is "false"
  qbt_schedule: "30" # Default is "30"
  qbt_config: "config.yml" # Default is "config.yml"
  qbt_logfile: "activity.log" # Default is "activity.log"
  qbt_cross_seed: "false" # Default is "false"
  qbt_recheck: "false" # Default is "false"
  qbt_cat_update: "false" # Default is "false"
  qbt_tag_update: "false" # Default is "false"
  qbt_rem_unregistered: "false" # Default is "false"
  qbt_rem_orphaned: "false" # Default is "false"
  qbt_tag_nohardlinks: "false" # Default is "false"
  qbt_skip_recycle: "false" # Default is "false"
  qbt_dry_run: "true" # Default is "false"
  qbt_log_level: "INFO" # Default is "INFO"
  qbt_divider: "=" # Default is "="
  qbt_width: "100" # Default is "100"
```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        qbit_manage_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    qbit_manage_name: qbit-manage

    ```

??? example "Paths"

    ```yaml
    # Type: string
    qbit_manage_role_paths_folder: "{{ qbit_manage_name }}"

    # Type: string
    qbit_manage_role_paths_location: "{{ server_appdata_path }}/{{ qbit_manage_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    qbit_manage_role_web_subdomain: "{{ qbit_manage_name }}"

    # Type: string
    qbit_manage_role_web_domain: "{{ user.domain }}"

    # Type: string
    qbit_manage_role_web_port: "8080"

    # Type: string
    qbit_manage_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbit_manage') + '.' + lookup('role_var', '_web_domain', role='qbit_manage')
                               if (lookup('role_var', '_web_subdomain', role='qbit_manage') | length > 0)
                               else lookup('role_var', '_web_domain', role='qbit_manage')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    qbit_manage_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbit_manage') }}"

    # Type: string
    qbit_manage_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbit_manage') }}"

    # Type: bool (true/false)
    qbit_manage_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    qbit_manage_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    qbit_manage_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    qbit_manage_role_traefik_middleware_custom: ""

    # Type: string
    qbit_manage_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    qbit_manage_role_traefik_enabled: true

    # Type: bool (true/false)
    qbit_manage_role_traefik_api_enabled: true

    # Type: string
    qbit_manage_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    qbit_manage_role_docker_container: "{{ qbit_manage_name }}"

    # Image
    # Type: bool (true/false)
    qbit_manage_role_docker_image_pull: true

    # Type: string
    qbit_manage_role_docker_image_repo: "ghcr.io/hotio/qbitmanage"

    # Type: string
    qbit_manage_role_docker_image_tag: "release"

    # Type: string
    qbit_manage_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbit_manage') }}:{{ lookup('role_var', '_docker_image_tag', role='qbit_manage') }}"

    # Ports
    # Type: list
    qbit_manage_role_docker_ports_defaults: []

    # Type: list
    qbit_manage_role_docker_ports_custom: []

    # Envs
    # Type: dict
    qbit_manage_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      UMASK: "002"
      TZ: "{{ tz }}"
      QBT_WEB_SERVER: "true"
      QBT_RUN: "{{ qbit_manage.qbt_run }}"
      QBT_SCHEDULE: "{{ qbit_manage.qbt_schedule }}"
      QBT_CONFIG: "{{ qbit_manage.qbt_config }}"
      QBT_LOGFILE: "{{ qbit_manage.qbt_logfile }}"
      QBT_CROSS_SEED: "{{ qbit_manage.qbt_cross_seed }}"
      QBT_RECHECK: "{{ qbit_manage.qbt_recheck }}"
      QBT_CAT_UPDATE: "{{ qbit_manage.qbt_cat_update }}"
      QBT_TAG_UPDATE: "{{ qbit_manage.qbt_tag_update }}"
      QBT_REM_UNREGISTERED: "{{ qbit_manage.qbt_rem_unregistered }}"
      QBT_REM_ORPHANED: "{{ qbit_manage.qbt_rem_orphaned }}"
      QBT_TAG_NOHARDLINKS: "{{ qbit_manage.qbt_tag_nohardlinks }}"
      QBT_SKIP_RECYCLE: "{{ qbit_manage.qbt_skip_recycle }}"
      QBT_DRY_RUN: "{{ qbit_manage.qbt_dry_run }}"
      QBT_LOG_LEVEL: "{{ qbit_manage.qbt_log_level }}"
      QBT_DIVIDER: "{{ qbit_manage.qbt_divider }}"
      QBT_WIDTH: "{{ qbit_manage.qbt_width }}"
      QBT_DEBUG: "{{ qbit_manage.qbt_debug }}"
      QBT_TRACE: "{{ qbit_manage.qbt_trace }}"

    # Type: dict
    qbit_manage_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    qbit_manage_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='qbit_manage') }}:/config"

    # Type: list
    qbit_manage_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    qbit_manage_role_docker_hostname: "{{ qbit_manage_name }}"

    # Networks
    # Type: string
    qbit_manage_role_docker_networks_alias: "{{ qbit_manage_name }}"

    # Type: list
    qbit_manage_role_docker_networks_default: []

    # Type: list
    qbit_manage_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    qbit_manage_role_docker_restart_policy: on-failure

    # Type: int
    qbit_manage_role_docker_restart_retries: 3

    # State
    # Type: string
    qbit_manage_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    qbit_manage_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    qbit_manage_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    qbit_manage_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    qbit_manage_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    qbit_manage_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    qbit_manage_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    qbit_manage_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    qbit_manage_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    qbit_manage_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    qbit_manage_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    qbit_manage_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    qbit_manage_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    qbit_manage_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    qbit_manage_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    qbit_manage_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    qbit_manage_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    qbit_manage_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        qbit_manage_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "qbit_manage2.{{ user.domain }}"
          - "qbit_manage.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        qbit_manage_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbit_manage2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
