---
icon: material/docker
title: NZBGet
hide:
  - tags
tags:
  - nzbget
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://github.com/hotio/nzbget/pkgs/container/nzbget
      type: github
    - name: Community
      url: https://hotio.dev/discord
      type: discord
  project_description:
    name: NZBGet
    summary: |-
      a very efficient, cross-platform usenet downloader.
    link: https://nzbget.net
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# NZBGet

## Overview

[NZBGet](https://nzbget.net) is a very efficient, cross-platform usenet downloader.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/hotio/nzbget/pkgs/container/nzbget){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://hotio.dev/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install nzbget
```

## Usage

Visit <https://nzbget.iYOUR_DOMAIN_NAMEi>.

## Basics

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

### Extensions

- Location on server: `/opt/scripts/nzbget`.

- Location within NZBGet: `/scripts/nzbget`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        nzbget_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `nzbget_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `nzbget_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`nzbget_name`"

        ```yaml
        # Type: string
        nzbget_name: nzbget
        ```

=== "Web"

    ??? variable string "`nzbget_role_web_subdomain`"

        ```yaml
        # Type: string
        nzbget_role_web_subdomain: "{{ nzbget_name }}"
        ```

    ??? variable string "`nzbget_role_web_domain`"

        ```yaml
        # Type: string
        nzbget_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`nzbget_role_web_port`"

        ```yaml
        # Type: string
        nzbget_role_web_port: "6789"
        ```

    ??? variable string "`nzbget_role_web_url`"

        ```yaml
        # Type: string
        nzbget_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nzbget') + '.' + lookup('role_var', '_web_domain', role='nzbget')
                              if (lookup('role_var', '_web_subdomain', role='nzbget') | length > 0)
                              else lookup('role_var', '_web_domain', role='nzbget')) }}"
        ```

    ??? variable string "`nzbget_role_web_login`"

        ```yaml
        # Type: string
        nzbget_role_web_login: "{{ user.name }}:{{ user.pass }}"
        ```

    ??? variable string "`nzbget_role_web_url_with_login`"

        ```yaml
        # Type: string
        nzbget_role_web_url_with_login: "{{ 'https://' + lookup('role_var', '_web_login', role='nzbget') + '@' + lookup('role_var', '_web_subdomain', role='nzbget') + '.' + lookup('role_var', '_web_domain', role='nzbget') }}"
        ```

    ??? variable string "`nzbget_role_web_local_url`"

        ```yaml
        # Type: string
        nzbget_role_web_local_url: "{{ 'http://' + nzbget_name + ':' + lookup('role_var', '_web_port', role='nzbget') }}"
        ```

    ??? variable string "`nzbget_role_web_local_url_web_login`"

        ```yaml
        # Type: string
        nzbget_role_web_local_url_web_login: "{{ 'http://' + lookup('role_var', '_web_login', role='nzbget') + '@' + nzbget_name + ':' + lookup('role_var', '_web_port', role='nzbget') }}"
        ```

=== "DNS"

    ??? variable string "`nzbget_role_dns_record`"

        ```yaml
        # Type: string
        nzbget_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nzbget') }}"
        ```

    ??? variable string "`nzbget_role_dns_zone`"

        ```yaml
        # Type: string
        nzbget_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nzbget') }}"
        ```

    ??? variable bool "`nzbget_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`nzbget_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        nzbget_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`nzbget_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        nzbget_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',themepark-' + nzbget_name
                                                      if (lookup('role_var', '_themepark_enabled', role='nzbget') and global_themepark_plugin_enabled)
                                                      else '') }}"
        ```

    ??? variable string "`nzbget_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        nzbget_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`nzbget_role_traefik_certresolver`"

        ```yaml
        # Type: string
        nzbget_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`nzbget_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_traefik_enabled: true
        ```

    ??? variable bool "`nzbget_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_traefik_api_enabled: true
        ```

    ??? variable string "`nzbget_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        nzbget_role_traefik_api_endpoint: "PathRegexp(`^/[A-Za-z0-9]+:[A-Za-z0-9]+/(xml|json|jsonp)rpc`) || PathRegexp(`^/(xml|json|jsonp)rpc`)"
        ```

=== "Config"

    ??? variable string "`nzbget_role_config_new_installs_settings_default`"

        ```yaml
        # New Installs
        # Type: string
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
          - { regexp: '^UnrarCmd\s?=.*', line: 'UnrarCmd=/usr/bin/unrar' }
          - { regexp: '^SevenZipCmd\s?=.*', line: 'SevenZipCmd=/usr/bin/7z' }
          - { regexp: '^ParIgnoreExt\s?=.*', line: 'ParIgnoreExt=.sfv, .nzb, .nfo, .srr, .1.rar' }
          - { regexp: '^ExtCleanupDisk\s?=.*', line: 'ExtCleanupDisk=.nzb, .par2, .sfv, .sfv.*, .rar.*,
                                                                      .htm, .html, _brokenlog.txt, .srr,
                                                                      .duplicate1.rar, .srs, .info, .txt,
                                                                      .com, .md5, .png, .1, .url, .jpg,
                                                                      .xxx, .rev, .iso, .img, .ifo, .vob' }
        ```

    ??? variable list "`nzbget_role_config_new_installs_settings_custom`"

        ```yaml
        # Type: list
        nzbget_role_config_new_installs_settings_custom: []
        ```

    ??? variable string "`nzbget_role_config_new_installs_settings_list`"

        ```yaml
        # Type: string
        nzbget_role_config_new_installs_settings_list: "{{ lookup('role_var', '_config_new_installs_settings_default', role='nzbget')
                                                           + lookup('role_var', '_config_new_installs_settings_custom', role='nzbget') }}"
        ```

    ??? variable string "`nzbget_role_config_existing_installs_settings_default`"

        ```yaml
        # Existing Installs
        # Type: string
        nzbget_role_config_existing_installs_settings_default:
          # Logging
          - { regexp: '^WriteLog\s?=.*', line: 'WriteLog=rotate' }
          - { regexp: '^RotateLog\s?=.*', line: 'RotateLog=3' }
          # Scripts
          - { regexp: '^ShellOverride\s?=.*', line: 'ShellOverride=.py=/usr/bin/python3' }
          # Unpacking
          - { regexp: '^UnrarCmd\s?=.*', line: 'UnrarCmd=ionice -c3 /usr/bin/unrar' }
          - { regexp: '^SevenZipCmd\s?=.*', line: 'SevenZipCmd=ionice -c3 /usr/bin/7z' }
        ```

    ??? variable list "`nzbget_role_config_existing_installs_settings_custom`"

        ```yaml
        # Type: list
        nzbget_role_config_existing_installs_settings_custom: []
        ```

    ??? variable string "`nzbget_role_config_existing_installs_settings_list`"

        ```yaml
        # Type: string
        nzbget_role_config_existing_installs_settings_list: "{{ lookup('role_var', '_config_existing_installs_settings_default', role='nzbget')
                                                                + lookup('role_var', '_config_existing_installs_settings_custom', role='nzbget') }}"
        ```

=== "Scripts"

    ??? variable string "`nzbget_role_scripts_paths_location`"

        ```yaml
        # Paths
        # Default nzbget_scripts_paths_location = /opt/scripts/nzbget
        # Type: string
        nzbget_role_scripts_paths_location: "{{ server_appdata_path }}/scripts/{{ nzbget_role_paths_folder }}"
        ```

    ??? variable list "`nzbget_role_scripts_paths_folders_list`"

        ```yaml
        # Type: list
        nzbget_role_scripts_paths_folders_list:
          - "{{ nzbget_role_scripts_paths_location }}"
          - "{{ nzbget_role_scripts_paths_location }}/nzbgetpp"
        ```

    ??? variable string "`nzbget_role_scripts_paths_rarfile_py_location`"

        ```yaml
        # Type: string
        nzbget_role_scripts_paths_rarfile_py_location: "{{ nzbget_role_scripts_paths_location }}/nzbgetpp/rarfile/rarfile.py"
        ```

    ??? variable list "`nzbget_role_scripts_repos_default`"

        ```yaml
        # Repos Downloaded
        # Type: list
        nzbget_role_scripts_repos_default:
          - 'https://github.com/Prinz23/nzbgetpp.git'
        ```

    ??? variable list "`nzbget_role_scripts_repos_custom`"

        ```yaml
        # Type: list
        nzbget_role_scripts_repos_custom: []
        ```

    ??? variable string "`nzbget_role_scripts_repos_list`"

        ```yaml
        # Type: string
        nzbget_role_scripts_repos_list: "{{ lookup('role_var', '_scripts_repos_default', role='nzbget') + lookup('role_var', '_scripts_repos_custom', role='nzbget') }}"
        ```

    ??? variable list "`nzbget_role_scripts_direct_downloads_default`"

        ```yaml
        # URLs Downloaded
        # Type: list
        nzbget_role_scripts_direct_downloads_default:
          - "https://raw.githubusercontent.com/clinton-hall/GetScripts/master/flatten.py"
          - "https://raw.githubusercontent.com/clinton-hall/GetScripts/master/DeleteSamples.py"
          - "https://raw.githubusercontent.com/Prinz23/nzbget-pp-reverse/master/reverse_name.py"
          - "https://raw.githubusercontent.com/l3uddz/nzbgetScripts/master/HashRenamer.py"
        ```

    ??? variable list "`nzbget_role_scripts_direct_downloads_custom`"

        ```yaml
        # Type: list
        nzbget_role_scripts_direct_downloads_custom: []
        ```

    ??? variable string "`nzbget_role_scripts_direct_downloads_list`"

        ```yaml
        # Type: string
        nzbget_role_scripts_direct_downloads_list: "{{ lookup('role_var', '_scripts_direct_downloads_default', role='nzbget')
                                                       + lookup('role_var', '_scripts_direct_downloads_custom', role='nzbget') }}"
        ```

    ??? variable list "`nzbget_role_scripts_local_copy_default`"

        ```yaml
        # Locally Copied
        # Type: list
        nzbget_role_scripts_local_copy_default: []
        ```

    ??? variable list "`nzbget_role_scripts_local_copy_custom`"

        ```yaml
        # Type: list
        nzbget_role_scripts_local_copy_custom: []
        ```

    ??? variable string "`nzbget_role_scripts_local_copy_list`"

        ```yaml
        # Type: string
        nzbget_role_scripts_local_copy_list: "{{ lookup('role_var', '_scripts_local_copy_default', role='nzbget')
                                                 + lookup('role_var', '_scripts_local_copy_custom', role='nzbget') }}"
        ```

=== "Theme"

    ??? variable bool "`nzbget_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        nzbget_role_themepark_enabled: false
        ```

    ??? variable string "`nzbget_role_themepark_app`"

        ```yaml
        # Type: string
        nzbget_role_themepark_app: "nzbget"
        ```

    ??? variable string "`nzbget_role_themepark_theme`"

        ```yaml
        # Type: string
        nzbget_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`nzbget_role_themepark_domain`"

        ```yaml
        # Type: string
        nzbget_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`nzbget_role_themepark_addons`"

        ```yaml
        # Type: list
        nzbget_role_themepark_addons: []
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`nzbget_role_docker_container`"

        ```yaml
        # Type: string
        nzbget_role_docker_container: "{{ nzbget_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`nzbget_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_image_pull: true
        ```

    ??? variable string "`nzbget_role_docker_image_repo`"

        ```yaml
        # Type: string
        nzbget_role_docker_image_repo: "ghcr.io/hotio/nzbget"
        ```

    ??? variable string "`nzbget_role_docker_image_tag`"

        ```yaml
        # Type: string
        nzbget_role_docker_image_tag: "release"
        ```

    ??? variable string "`nzbget_role_docker_image`"

        ```yaml
        # Type: string
        nzbget_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nzbget') }}:{{ lookup('role_var', '_docker_image_tag', role='nzbget') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`nzbget_role_docker_envs_default`"

        ```yaml
        # Type: dict
        nzbget_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"
          LC_ALL: "C"
        ```

    ??? variable dict "`nzbget_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        nzbget_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`nzbget_role_docker_volumes_default`"

        ```yaml
        # Type: list
        nzbget_role_docker_volumes_default:
          - "{{ nzbget_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`nzbget_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        nzbget_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`nzbget_role_docker_labels_default`"

        ```yaml
        # Type: dict
        nzbget_role_docker_labels_default: {}
        ```

    ??? variable dict "`nzbget_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        nzbget_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`nzbget_role_docker_hostname`"

        ```yaml
        # Type: string
        nzbget_role_docker_hostname: "{{ nzbget_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`nzbget_role_docker_networks_alias`"

        ```yaml
        # Type: string
        nzbget_role_docker_networks_alias: "{{ nzbget_name }}"
        ```

    ??? variable list "`nzbget_role_docker_networks_default`"

        ```yaml
        # Type: list
        nzbget_role_docker_networks_default: []
        ```

    ??? variable list "`nzbget_role_docker_networks_custom`"

        ```yaml
        # Type: list
        nzbget_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`nzbget_role_docker_restart_policy`"

        ```yaml
        # Type: string
        nzbget_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`nzbget_role_docker_state`"

        ```yaml
        # Type: string
        nzbget_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`nzbget_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        nzbget_role_docker_blkio_weight:
        ```

    ??? variable int "`nzbget_role_docker_cpu_period`"

        ```yaml
        # Type: int
        nzbget_role_docker_cpu_period:
        ```

    ??? variable int "`nzbget_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        nzbget_role_docker_cpu_quota:
        ```

    ??? variable int "`nzbget_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        nzbget_role_docker_cpu_shares:
        ```

    ??? variable string "`nzbget_role_docker_cpus`"

        ```yaml
        # Type: string
        nzbget_role_docker_cpus:
        ```

    ??? variable string "`nzbget_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        nzbget_role_docker_cpuset_cpus:
        ```

    ??? variable string "`nzbget_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        nzbget_role_docker_cpuset_mems:
        ```

    ??? variable string "`nzbget_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        nzbget_role_docker_kernel_memory:
        ```

    ??? variable string "`nzbget_role_docker_memory`"

        ```yaml
        # Type: string
        nzbget_role_docker_memory:
        ```

    ??? variable string "`nzbget_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        nzbget_role_docker_memory_reservation:
        ```

    ??? variable string "`nzbget_role_docker_memory_swap`"

        ```yaml
        # Type: string
        nzbget_role_docker_memory_swap:
        ```

    ??? variable int "`nzbget_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        nzbget_role_docker_memory_swappiness:
        ```

    ??? variable string "`nzbget_role_docker_shm_size`"

        ```yaml
        # Type: string
        nzbget_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`nzbget_role_docker_cap_drop`"

        ```yaml
        # Type: list
        nzbget_role_docker_cap_drop:
        ```

    ??? variable string "`nzbget_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        nzbget_role_docker_cgroupns_mode:
        ```

    ??? variable list "`nzbget_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        nzbget_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`nzbget_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        nzbget_role_docker_device_read_bps:
        ```

    ??? variable list "`nzbget_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        nzbget_role_docker_device_read_iops:
        ```

    ??? variable list "`nzbget_role_docker_device_requests`"

        ```yaml
        # Type: list
        nzbget_role_docker_device_requests:
        ```

    ??? variable list "`nzbget_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        nzbget_role_docker_device_write_bps:
        ```

    ??? variable list "`nzbget_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        nzbget_role_docker_device_write_iops:
        ```

    ??? variable list "`nzbget_role_docker_devices`"

        ```yaml
        # Type: list
        nzbget_role_docker_devices:
        ```

    ??? variable string "`nzbget_role_docker_devices_default`"

        ```yaml
        # Type: string
        nzbget_role_docker_devices_default:
        ```

    ??? variable list "`nzbget_role_docker_groups`"

        ```yaml
        # Type: list
        nzbget_role_docker_groups:
        ```

    ??? variable bool "`nzbget_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_privileged:
        ```

    ??? variable list "`nzbget_role_docker_security_opts`"

        ```yaml
        # Type: list
        nzbget_role_docker_security_opts:
        ```

    ??? variable string "`nzbget_role_docker_user`"

        ```yaml
        # Type: string
        nzbget_role_docker_user:
        ```

    ??? variable string "`nzbget_role_docker_userns_mode`"

        ```yaml
        # Type: string
        nzbget_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`nzbget_role_docker_dns_opts`"

        ```yaml
        # Type: list
        nzbget_role_docker_dns_opts:
        ```

    ??? variable list "`nzbget_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        nzbget_role_docker_dns_search_domains:
        ```

    ??? variable list "`nzbget_role_docker_dns_servers`"

        ```yaml
        # Type: list
        nzbget_role_docker_dns_servers:
        ```

    ??? variable string "`nzbget_role_docker_domainname`"

        ```yaml
        # Type: string
        nzbget_role_docker_domainname:
        ```

    ??? variable list "`nzbget_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        nzbget_role_docker_exposed_ports:
        ```

    ??? variable dict "`nzbget_role_docker_hosts`"

        ```yaml
        # Type: dict
        nzbget_role_docker_hosts:
        ```

    ??? variable bool "`nzbget_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_hosts_use_common:
        ```

    ??? variable string "`nzbget_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        nzbget_role_docker_ipc_mode:
        ```

    ??? variable list "`nzbget_role_docker_links`"

        ```yaml
        # Type: list
        nzbget_role_docker_links:
        ```

    ??? variable string "`nzbget_role_docker_network_mode`"

        ```yaml
        # Type: string
        nzbget_role_docker_network_mode:
        ```

    ??? variable string "`nzbget_role_docker_pid_mode`"

        ```yaml
        # Type: string
        nzbget_role_docker_pid_mode:
        ```

    ??? variable list "`nzbget_role_docker_ports`"

        ```yaml
        # Type: list
        nzbget_role_docker_ports:
        ```

    ??? variable string "`nzbget_role_docker_uts`"

        ```yaml
        # Type: string
        nzbget_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`nzbget_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_keep_volumes:
        ```

    ??? variable list "`nzbget_role_docker_mounts`"

        ```yaml
        # Type: list
        nzbget_role_docker_mounts:
        ```

    ??? variable dict "`nzbget_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        nzbget_role_docker_storage_opts:
        ```

    ??? variable list "`nzbget_role_docker_tmpfs`"

        ```yaml
        # Type: list
        nzbget_role_docker_tmpfs:
        ```

    ??? variable string "`nzbget_role_docker_volume_driver`"

        ```yaml
        # Type: string
        nzbget_role_docker_volume_driver:
        ```

    ??? variable list "`nzbget_role_docker_volumes_from`"

        ```yaml
        # Type: list
        nzbget_role_docker_volumes_from:
        ```

    ??? variable bool "`nzbget_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_volumes_global:
        ```

    ??? variable string "`nzbget_role_docker_working_dir`"

        ```yaml
        # Type: string
        nzbget_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`nzbget_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_auto_remove:
        ```

    ??? variable bool "`nzbget_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_cleanup:
        ```

    ??? variable string "`nzbget_role_docker_force_kill`"

        ```yaml
        # Type: string
        nzbget_role_docker_force_kill:
        ```

    ??? variable dict "`nzbget_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        nzbget_role_docker_healthcheck:
        ```

    ??? variable int "`nzbget_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        nzbget_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`nzbget_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_init:
        ```

    ??? variable string "`nzbget_role_docker_kill_signal`"

        ```yaml
        # Type: string
        nzbget_role_docker_kill_signal:
        ```

    ??? variable string "`nzbget_role_docker_log_driver`"

        ```yaml
        # Type: string
        nzbget_role_docker_log_driver:
        ```

    ??? variable dict "`nzbget_role_docker_log_options`"

        ```yaml
        # Type: dict
        nzbget_role_docker_log_options:
        ```

    ??? variable bool "`nzbget_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_oom_killer:
        ```

    ??? variable int "`nzbget_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        nzbget_role_docker_oom_score_adj:
        ```

    ??? variable bool "`nzbget_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_output_logs:
        ```

    ??? variable bool "`nzbget_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_paused:
        ```

    ??? variable bool "`nzbget_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_recreate:
        ```

    ??? variable int "`nzbget_role_docker_restart_retries`"

        ```yaml
        # Type: int
        nzbget_role_docker_restart_retries:
        ```

    ??? variable int "`nzbget_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        nzbget_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`nzbget_role_docker_capabilities`"

        ```yaml
        # Type: list
        nzbget_role_docker_capabilities:
        ```

    ??? variable string "`nzbget_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        nzbget_role_docker_cgroup_parent:
        ```

    ??? variable list "`nzbget_role_docker_commands`"

        ```yaml
        # Type: list
        nzbget_role_docker_commands:
        ```

    ??? variable int "`nzbget_role_docker_create_timeout`"

        ```yaml
        # Type: int
        nzbget_role_docker_create_timeout:
        ```

    ??? variable string "`nzbget_role_docker_entrypoint`"

        ```yaml
        # Type: string
        nzbget_role_docker_entrypoint:
        ```

    ??? variable string "`nzbget_role_docker_env_file`"

        ```yaml
        # Type: string
        nzbget_role_docker_env_file:
        ```

    ??? variable bool "`nzbget_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_labels_use_common:
        ```

    ??? variable bool "`nzbget_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_read_only:
        ```

    ??? variable string "`nzbget_role_docker_runtime`"

        ```yaml
        # Type: string
        nzbget_role_docker_runtime:
        ```

    ??? variable list "`nzbget_role_docker_sysctls`"

        ```yaml
        # Type: list
        nzbget_role_docker_sysctls:
        ```

    ??? variable list "`nzbget_role_docker_ulimits`"

        ```yaml
        # Type: list
        nzbget_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`nzbget_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nzbget_role_autoheal_enabled: true
        ```

    ??? variable string "`nzbget_role_config_existing_installs_settings_custom`"

        ```yaml
        # Type: string
        nzbget_role_config_existing_installs_settings_custom:
        ```

    ??? variable string "`nzbget_role_config_existing_installs_settings_default`"

        ```yaml
        # Type: string
        nzbget_role_config_existing_installs_settings_default:
        ```

    ??? variable string "`nzbget_role_config_new_installs_settings_custom`"

        ```yaml
        # Type: string
        nzbget_role_config_new_installs_settings_custom:
        ```

    ??? variable string "`nzbget_role_config_new_installs_settings_default`"

        ```yaml
        # Type: string
        nzbget_role_config_new_installs_settings_default:
        ```

    ??? variable string "`nzbget_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        nzbget_role_depends_on: ""
        ```

    ??? variable string "`nzbget_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nzbget_role_depends_on_delay: "0"
        ```

    ??? variable string "`nzbget_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nzbget_role_depends_on_healthchecks:
        ```

    ??? variable bool "`nzbget_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nzbget_role_diun_enabled: true
        ```

    ??? variable bool "`nzbget_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        nzbget_role_dns_enabled: true
        ```

    ??? variable bool "`nzbget_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nzbget_role_docker_controller: true
        ```

    ??? variable string "`nzbget_role_docker_image_repo`"

        ```yaml
        # Type: string
        nzbget_role_docker_image_repo:
        ```

    ??? variable string "`nzbget_role_docker_image_tag`"

        ```yaml
        # Type: string
        nzbget_role_docker_image_tag:
        ```

    ??? variable bool "`nzbget_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_docker_volumes_download:
        ```

    ??? variable string "`nzbget_role_scripts_direct_downloads_custom`"

        ```yaml
        # Type: string
        nzbget_role_scripts_direct_downloads_custom:
        ```

    ??? variable string "`nzbget_role_scripts_direct_downloads_default`"

        ```yaml
        # Type: string
        nzbget_role_scripts_direct_downloads_default:
        ```

    ??? variable string "`nzbget_role_scripts_local_copy_custom`"

        ```yaml
        # Type: string
        nzbget_role_scripts_local_copy_custom:
        ```

    ??? variable string "`nzbget_role_scripts_local_copy_default`"

        ```yaml
        # Type: string
        nzbget_role_scripts_local_copy_default:
        ```

    ??? variable string "`nzbget_role_scripts_repos_custom`"

        ```yaml
        # Type: string
        nzbget_role_scripts_repos_custom:
        ```

    ??? variable string "`nzbget_role_scripts_repos_default`"

        ```yaml
        # Type: string
        nzbget_role_scripts_repos_default:
        ```

    ??? variable string "`nzbget_role_themepark_addons`"

        ```yaml
        # Type: string
        nzbget_role_themepark_addons:
        ```

    ??? variable string "`nzbget_role_themepark_app`"

        ```yaml
        # Type: string
        nzbget_role_themepark_app:
        ```

    ??? variable bool "`nzbget_role_themepark_enabled`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_themepark_enabled:
        ```

    ??? variable string "`nzbget_role_themepark_theme`"

        ```yaml
        # Type: string
        nzbget_role_themepark_theme:
        ```

    ??? variable dict "`nzbget_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        nzbget_role_traefik_api_endpoint:
        ```

    ??? variable string "`nzbget_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        nzbget_role_traefik_api_middleware:
        ```

    ??? variable string "`nzbget_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        nzbget_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`nzbget_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        nzbget_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`nzbget_role_traefik_certresolver`"

        ```yaml
        # Type: string
        nzbget_role_traefik_certresolver:
        ```

    ??? variable bool "`nzbget_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        nzbget_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`nzbget_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        nzbget_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`nzbget_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        nzbget_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`nzbget_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        nzbget_role_traefik_middleware_http:
        ```

    ??? variable bool "`nzbget_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`nzbget_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        nzbget_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`nzbget_role_traefik_priority`"

        ```yaml
        # Type: string
        nzbget_role_traefik_priority:
        ```

    ??? variable bool "`nzbget_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        nzbget_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`nzbget_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        nzbget_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`nzbget_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        nzbget_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`nzbget_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        nzbget_role_web_api_http_port:
        ```

    ??? variable string "`nzbget_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        nzbget_role_web_api_http_scheme:
        ```

    ??? variable dict "`nzbget_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbget_role_web_api_http_serverstransport:
        ```

    ??? variable string "`nzbget_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        nzbget_role_web_api_port:
        ```

    ??? variable string "`nzbget_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        nzbget_role_web_api_scheme:
        ```

    ??? variable dict "`nzbget_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbget_role_web_api_serverstransport:
        ```

    ??? variable string "`nzbget_role_web_domain`"

        ```yaml
        # Type: string
        nzbget_role_web_domain:
        ```

    ??? variable list "`nzbget_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        nzbget_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            nzbget_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nzbget2.{{ user.domain }}"
              - "nzbget.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`nzbget_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        nzbget_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            nzbget_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nzbget2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`nzbget_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        nzbget_role_web_http_port:
        ```

    ??? variable string "`nzbget_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        nzbget_role_web_http_scheme:
        ```

    ??? variable dict "`nzbget_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbget_role_web_http_serverstransport:
        ```

    ??? variable string "`nzbget_role_web_login`"

        ```yaml
        # Type: string
        nzbget_role_web_login:
        ```

    ??? variable string "`nzbget_role_web_port`"

        ```yaml
        # Type: string (quoted number)
        nzbget_role_web_port:
        ```

    ??? variable string "`nzbget_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        nzbget_role_web_scheme:
        ```

    ??? variable dict "`nzbget_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbget_role_web_serverstransport:
        ```

    ??? variable string "`nzbget_role_web_subdomain`"

        ```yaml
        # Type: string
        nzbget_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
