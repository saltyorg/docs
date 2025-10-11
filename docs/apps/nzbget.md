---
hide:
  - tags
tags:
  - nzbget
---

# NZBGet

# What is it?

[NZBGet](https://nzbget.net/) (by Andrey Prygunkov aka hugbug) is a very efficient, cross-platform usenet downloader.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://nzbget.net){: .header-icons } | [:octicons-link-16: Docs](https://nzbget.net/documentation){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nzbget/nzbget){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/nzbget){: .header-icons }|

## 1. Accessing NZBGet

- To access NZBGet, visit `https://nzbget._yourdomain.com_`

## 2. Settings

### Paths

- Download paths have already been specified, no need to change those.

### News-Servers

- Add your [news servers](../reference/usenet-torrent.md).

### Security

- Login settings are preset out of the box (`user` / `passwd` as set in [accounts.yml](../reference/accounts.md)).

### Download Queue

- Disk Space

  - By default, minimum disk space is set at _100000_ (i.e. 100GB). When space goes lower than this, NZBGet will pause the queue. If you have a smaller hard drive, you will need to lower this setting.

### Connection

- DailyQuota

  - If you are using Google Drive and set up the 300 [service accounts in Rclone](../reference/rclone-manual.md) you can ignore this.
  - Otherwise, if you are using Google Drive, it's recommended you set this to `750000` (i.e. 750GB), to coincide with the Google Drive daily upload limit.

## 3. Extensions

- Location on server: `/opt/scripts/nzbget`.

- Location within NZBGet: `/scripts/nzbget`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        nzbget_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    nzbget_name: nzbget

    ```

??? example "Paths"

    ```yaml
    # Type: string
    nzbget_role_paths_folder: "{{ nzbget_name }}"

    # Type: string
    nzbget_role_paths_location: "{{ server_appdata_path }}/{{ nzbget_role_paths_folder }}"

    # Type: string
    nzbget_role_paths_downloads_location: "{{ downloads_usenet_path }}/{{ nzbget_role_paths_folder }}"

    # Type: string
    nzbget_role_paths_config_location: "{{ nzbget_role_paths_location }}/nzbget.conf"

    ```

??? example "Web"

    ```yaml
    # Type: string
    nzbget_role_web_subdomain: "{{ nzbget_name }}"

    # Type: string
    nzbget_role_web_domain: "{{ user.domain }}"

    # Type: string
    nzbget_role_web_port: "6789"

    # Type: string
    nzbget_role_web_login: "{{ user.name }}:{{ user.pass }}"

    # Type: string
    nzbget_role_web_url_with_login: "{{ 'https://' + lookup('role_var', '_web_login', role='nzbget') + '@' + lookup('role_var', '_web_subdomain', role='nzbget') + '.' + lookup('role_var', '_web_domain', role='nzbget') }}"

    # Type: string
    nzbget_role_web_local_url_web_login: "{{ 'http://' + lookup('role_var', '_web_login', role='nzbget') + '@' + nzbget_name + ':' + lookup('role_var', '_web_port', role='nzbget') }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    nzbget_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nzbget') }}"

    # Type: string
    nzbget_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nzbget') }}"

    # Type: bool (true/false)
    nzbget_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    nzbget_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    nzbget_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                + (',themepark-' + nzbget_name
                                                  if (lookup('role_var', '_themepark_enabled', role='nzbget') and global_themepark_plugin_enabled)
                                                  else '') }}"

    # Type: string
    nzbget_role_traefik_middleware_custom: ""

    # Type: string
    nzbget_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    nzbget_role_traefik_enabled: true

    # Type: bool (true/false)
    nzbget_role_traefik_api_enabled: true

    # Type: string
    nzbget_role_traefik_api_endpoint: "PathRegexp(`^/[A-Za-z0-9]+:[A-Za-z0-9]+/(xml|json|jsonp)rpc`) || PathRegexp(`^/(xml|json|jsonp)rpc`)"

    ```

??? example "Config"

    ```yaml
    # Type: list
    nzbget_role_config_new_installs_settings_default: 
      # Authentication
      - { regexp: '^ControlUsername\s?=.*', line: "ControlUsername={{ user.name }}" }
      - { regexp: '^ControlPassword\s?=.*', line: "ControlPassword={{ user.pass }}" }
      - { regexp: '^FormAuth\s?=.*', line: 'FormAuth=yes' }
      # Paths
      - { regexp: '^MainDir\s?=.*', line: 'MainDir=/mnt/unionfs/downloads/nzbs/{{ nzbget_name }}' }
      - { regexp: '^QueueDir\s?=.*', line: "QueueDir=${MainDir}/queue" }
      - { regexp: '^TempDir\s?=.*', line: "TempDir=${MainDir}/tmp" }
      - { regexp: '^ScriptDir\s?=.*', line: 'ScriptDir=/scripts/nzbget' }
      - { regexp: '^LockFile\s?=.*', line: 'LockFile=config/nzbget.lock' }
      - { regexp: '^LogFile\s?=.*', line: "LogFile=${MainDir}/nzbget.log" }
      # Default Categories
      - { regexp: '^Category1\.Name\s?=.*', line: 'Category1.Name=movies' }
      - { regexp: '^Category1\.Aliases\s?=.*', line: 'Category1.Aliases=movies*, Movies*' }
      - { regexp: '^Category2\.Name\s?=.*', line: 'Category2.Name=series' }
      - { regexp: '^Category2\.Aliases\s?=.*', line: 'Category2.Aliases=TV - HD, TV - SD, TV*' }
      - { regexp: '^Category3\.Name\s?=.*', line: 'Category3.Name=music' }
      - { regexp: '^Category3\.Aliases\s?=.*', line: 'Category3.Aliases=audio*' }
      - { regexp: '^Category4\.Name\s?=.*', line: 'Category4.Name=apps' }
      - { regexp: '^Category4\.Aliases\s?=.*', line: 'Category4.Aliases=apps*, pc*' }
      # New Categories
      - { regexp: '^Category5\.Name\s?=.*', line: 'Category5.Name=sonarr' }
      - { regexp: '^Category6\.Name\s?=.*', line: 'Category6.Name=radarr' }
      - { regexp: '^Category7\.Name\s?=.*', line: 'Category7.Name=lidarr' }
      # Logging
      - { regexp: '^WriteLog\s?=.*', line: 'WriteLog=rotate' }
      - { regexp: '^RotateLog\s?=.*', line: 'RotateLog=3' }
      # Min Disk Space = 100GB
      - { regexp: '^DiskSpace\s?=.*', line: 'DiskSpace=100000' }
      # HealthCheck
      - { regexp: '^HealthCheck\s?=.*', line: 'HealthCheck=Delete' }
      # Unpauser task
      - { regexp: '^#?Task1\.Time\s?=.*', line: 'Task1.Time=*,*:00,*:15,*:30,*:45' }
      - { regexp: '^#?Task1\.WeekDays\s?=.*', line: 'Task1.WeekDays=1-7' }
      - { regexp: '^#?Task1\.Command\s?=.*', line: 'Task1.Command=UnpauseDownload' }
      - { regexp: '^#?Task1\.Param\s?=.*', line: 'Task1.Param=' }
      # Scripts
      - { regexp: '^ShellOverride\s?=.*', line: 'ShellOverride=.py=/usr/bin/python3' }
      - { regexp: '^Extensions\s?=.*', line: 'Extensions=nzbgetpp/unzip.py, flatten.py, DeleteSamples.py, HashRenamer.py, reverse_name.py' }
      - { regexp: '^ScriptOrder\s?=.*', line: 'ScriptOrder=nzbgetpp/unzip.py, flatten.py, DeleteSamples.py, HashRenamer.py, reverse_name.py' }
      # Unpacking
      - { regexp: '^UnrarCmd\s?=.*', line: 'UnrarCmd=ionice -c3 /usr/bin/unrar' }
      - { regexp: '^SevenZipCmd\s?=.*', line: 'SevenZipCmd=ionice -c3 /usr/bin/7z' }
      - { regexp: '^ParIgnoreExt\s?=.*', line: 'ParIgnoreExt=.sfv, .nzb, .nfo, .srr, .1.rar' }
      - { regexp: '^ExtCleanupDisk\s?=.*', line: 'ExtCleanupDisk=.nzb, .par2, .sfv, .sfv.*, .rar.*,
                                                                  .htm, .html, _brokenlog.txt, .srr,
                                                                  .duplicate1.rar, .srs, .info, .txt,
                                                                  .com, .md5, .png, .1, .url, .jpg,
                                                                  .xxx, .rev, .iso, .img, .ifo, .vob' }

    # Type: list
    nzbget_role_config_new_installs_settings_custom: []

    # Type: string
    nzbget_role_config_new_installs_settings_list: "{{ lookup('role_var', '_config_new_installs_settings_default', role='nzbget')
                                                       + lookup('role_var', '_config_new_installs_settings_custom', role='nzbget') }}"

    # Type: list
    nzbget_role_config_existing_installs_settings_default: 
      # Logging
      - { regexp: '^WriteLog\s?=.*', line: 'WriteLog=rotate' }
      - { regexp: '^RotateLog\s?=.*', line: 'RotateLog=3' }
      # Scripts
      - { regexp: '^ShellOverride\s?=.*', line: 'ShellOverride=.py=/usr/bin/python3' }
      # Unpacking
      - { regexp: '^UnrarCmd\s?=.*', line: 'UnrarCmd=ionice -c3 /usr/bin/unrar' }
      - { regexp: '^SevenZipCmd\s?=.*', line: 'SevenZipCmd=ionice -c3 /usr/bin/7z' }

    # Type: list
    nzbget_role_config_existing_installs_settings_custom: []

    # Type: string
    nzbget_role_config_existing_installs_settings_list: "{{ lookup('role_var', '_config_existing_installs_settings_default', role='nzbget')
                                                            + lookup('role_var', '_config_existing_installs_settings_custom', role='nzbget') }}"

    ```

??? example "Scripts"

    ```yaml
    # Paths
    # Default nzbget_scripts_paths_location = /opt/scripts/nzbget
    # Type: string
    nzbget_role_scripts_paths_location: "{{ server_appdata_path }}/scripts/{{ nzbget_role_paths_folder }}"

    # Type: string
    nzbget_role_scripts_paths_rarfile_py_location: "{{ nzbget_role_scripts_paths_location }}/nzbgetpp/rarfile/rarfile.py"

    # Repos Downloaded
    # Type: list
    nzbget_role_scripts_repos_default: 
      - 'https://github.com/Prinz23/nzbgetpp.git'

    # Type: list
    nzbget_role_scripts_repos_custom: []

    # Type: string
    nzbget_role_scripts_repos_list: "{{ lookup('role_var', '_scripts_repos_default', role='nzbget') + lookup('role_var', '_scripts_repos_custom', role='nzbget') }}"

    # URLs Downloaded
    # Type: list
    nzbget_role_scripts_direct_downloads_default: 
      - "https://raw.githubusercontent.com/clinton-hall/GetScripts/master/flatten.py"
      - "https://raw.githubusercontent.com/clinton-hall/GetScripts/master/DeleteSamples.py"
      - "https://raw.githubusercontent.com/Prinz23/nzbget-pp-reverse/master/reverse_name.py"
      - "https://raw.githubusercontent.com/l3uddz/nzbgetScripts/master/HashRenamer.py"

    # Type: list
    nzbget_role_scripts_direct_downloads_custom: []

    # Type: string
    nzbget_role_scripts_direct_downloads_list: "{{ lookup('role_var', '_scripts_direct_downloads_default', role='nzbget')
                                                   + lookup('role_var', '_scripts_direct_downloads_custom', role='nzbget') }}"

    # Locally Copied
    # Type: list
    nzbget_role_scripts_local_copy_default: []

    # Type: list
    nzbget_role_scripts_local_copy_custom: []

    # Type: string
    nzbget_role_scripts_local_copy_list: "{{ lookup('role_var', '_scripts_local_copy_default', role='nzbget')
                                             + lookup('role_var', '_scripts_local_copy_custom', role='nzbget') }}"

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    nzbget_role_themepark_enabled: false

    # Type: string
    nzbget_role_themepark_app: "nzbget"

    # Type: string
    nzbget_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    nzbget_role_themepark_domain: "{{ global_themepark_domain }}"

    # Type: list
    nzbget_role_themepark_addons: []

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    nzbget_role_docker_container: "{{ nzbget_name }}"

    # Image
    # Type: bool (true/false)
    nzbget_role_docker_image_pull: true

    # Type: string
    nzbget_role_docker_image_repo: "ghcr.io/hotio/nzbget"

    # Type: string
    nzbget_role_docker_image_tag: "release"

    # Type: string
    nzbget_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nzbget') }}:{{ lookup('role_var', '_docker_image_tag', role='nzbget') }}"

    # Envs
    # Type: dict
    nzbget_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      UMASK: "002"
      TZ: "{{ tz }}"
      LC_ALL: "C"

    # Type: dict
    nzbget_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    nzbget_role_docker_volumes_default: 
      - "{{ nzbget_role_paths_location }}:/config"
      - "{{ server_appdata_path }}/scripts:/scripts"

    # Type: list
    nzbget_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    nzbget_role_docker_labels_default: {}

    # Type: dict
    nzbget_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    nzbget_role_docker_hostname: "{{ nzbget_name }}"

    # Networks
    # Type: string
    nzbget_role_docker_networks_alias: "{{ nzbget_name }}"

    # Type: list
    nzbget_role_docker_networks_default: []

    # Type: list
    nzbget_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    nzbget_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    nzbget_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    nzbget_role_docker_blkio_weight:

    # Type: int
    nzbget_role_docker_cpu_period:

    # Type: int
    nzbget_role_docker_cpu_quota:

    # Type: int
    nzbget_role_docker_cpu_shares:

    # Type: string
    nzbget_role_docker_cpus:

    # Type: string
    nzbget_role_docker_cpuset_cpus:

    # Type: string
    nzbget_role_docker_cpuset_mems:

    # Type: string
    nzbget_role_docker_kernel_memory:

    # Type: string
    nzbget_role_docker_memory:

    # Type: string
    nzbget_role_docker_memory_reservation:

    # Type: string
    nzbget_role_docker_memory_swap:

    # Type: int
    nzbget_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    nzbget_role_docker_cap_drop:

    # Type: list
    nzbget_role_docker_device_cgroup_rules:

    # Type: list
    nzbget_role_docker_device_read_bps:

    # Type: list
    nzbget_role_docker_device_read_iops:

    # Type: list
    nzbget_role_docker_device_requests:

    # Type: list
    nzbget_role_docker_device_write_bps:

    # Type: list
    nzbget_role_docker_device_write_iops:

    # Type: list
    nzbget_role_docker_devices:

    # Type: string
    nzbget_role_docker_devices_default:

    # Type: bool (true/false)
    nzbget_role_docker_privileged:

    # Type: list
    nzbget_role_docker_security_opts:


    # Networking
    # Type: list
    nzbget_role_docker_dns_opts:

    # Type: list
    nzbget_role_docker_dns_search_domains:

    # Type: list
    nzbget_role_docker_dns_servers:

    # Type: dict
    nzbget_role_docker_hosts:

    # Type: string
    nzbget_role_docker_hosts_use_common:

    # Type: string
    nzbget_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    nzbget_role_docker_keep_volumes:

    # Type: list
    nzbget_role_docker_mounts:

    # Type: string
    nzbget_role_docker_volume_driver:

    # Type: list
    nzbget_role_docker_volumes_from:

    # Type: string
    nzbget_role_docker_volumes_global:

    # Type: string
    nzbget_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    nzbget_role_docker_healthcheck:

    # Type: bool (true/false)
    nzbget_role_docker_init:

    # Type: string
    nzbget_role_docker_log_driver:

    # Type: dict
    nzbget_role_docker_log_options:

    # Type: bool (true/false)
    nzbget_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    nzbget_role_docker_auto_remove:

    # Type: list
    nzbget_role_docker_capabilities:

    # Type: string
    nzbget_role_docker_cgroup_parent:

    # Type: string
    nzbget_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    nzbget_role_docker_cleanup:

    # Type: list
    nzbget_role_docker_commands:

    # Type: string
    nzbget_role_docker_create_timeout:

    # Type: string
    nzbget_role_docker_domainname:

    # Type: string
    nzbget_role_docker_entrypoint:

    # Type: string
    nzbget_role_docker_env_file:

    # Type: list
    nzbget_role_docker_exposed_ports:

    # Type: string
    nzbget_role_docker_force_kill:

    # Type: list
    nzbget_role_docker_groups:

    # Type: int
    nzbget_role_docker_healthy_wait_timeout:

    # Type: string
    nzbget_role_docker_ipc_mode:

    # Type: string
    nzbget_role_docker_kill_signal:

    # Type: string
    nzbget_role_docker_labels_use_common:

    # Type: list
    nzbget_role_docker_links:

    # Type: bool (true/false)
    nzbget_role_docker_oom_killer:

    # Type: int
    nzbget_role_docker_oom_score_adj:

    # Type: bool (true/false)
    nzbget_role_docker_paused:

    # Type: string
    nzbget_role_docker_pid_mode:

    # Type: list
    nzbget_role_docker_ports:

    # Type: bool (true/false)
    nzbget_role_docker_read_only:

    # Type: bool (true/false)
    nzbget_role_docker_recreate:

    # Type: int
    nzbget_role_docker_restart_retries:

    # Type: string
    nzbget_role_docker_runtime:

    # Type: string
    nzbget_role_docker_shm_size:

    # Type: int
    nzbget_role_docker_stop_timeout:

    # Type: dict
    nzbget_role_docker_storage_opts:

    # Type: list
    nzbget_role_docker_sysctls:

    # Type: list
    nzbget_role_docker_tmpfs:

    # Type: list
    nzbget_role_docker_ulimits:

    # Type: string
    nzbget_role_docker_user:

    # Type: string
    nzbget_role_docker_userns_mode:

    # Type: string
    nzbget_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    nzbget_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    nzbget_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    nzbget_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    nzbget_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    nzbget_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    nzbget_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    nzbget_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    nzbget_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    nzbget_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    nzbget_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    nzbget_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    nzbget_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    nzbget_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    nzbget_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    nzbget_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    nzbget_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    nzbget_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        nzbget_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "nzbget2.{{ user.domain }}"
          - "nzbget.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        nzbget_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nzbget2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
