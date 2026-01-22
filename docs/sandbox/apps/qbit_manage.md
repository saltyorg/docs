---
icon: material/docker
title: qBit Manage
hide:
  - tags
tags:
  - qbit-manage
  - torrent
  - automation
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://github.com/hotio/qbitmanage/pkgs/container/qbitmanage
      type: github
    - name: Community
      url: https://hotio.dev/discord
      type: discord
  project_description:
    name: qBit Manage
    summary: |-
      a program used to manage your qBittorrent instance.
    link: https://github.com/StuffAnThings/qbit_manage
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# qBit Manage

## Overview

[qBit Manage](https://github.com/StuffAnThings/qbit_manage) is a program used to manage your qBittorrent instance.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/hotio/qbitmanage/pkgs/container/qbitmanage){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://hotio.dev/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

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

## Deployment

Before installing qBit Manage, you should have a **[qBittorrent](../../apps/qbittorrent.md)** instance running on your local machine.

```shell
sb install sandbox-qbit-manage
```

## Usage

Visit <https://qbit-manage.iYOUR_DOMAIN_NAMEi>.

## Basics

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

```shell
sb install sandbox-qbit-manage
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        qbit_manage_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `qbit_manage_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `qbit_manage_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`qbit_manage_name`"

        ```yaml
        # Type: string
        qbit_manage_name: qbit-manage
        ```

=== "Settings"

    ??? variable string "`qbit_manage_role_qbt_run`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_run: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_schedule`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_schedule: "30"
        ```

    ??? variable string "`qbit_manage_role_qbt_config`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_config: "config.yml"
        ```

    ??? variable string "`qbit_manage_role_qbt_logfile`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_logfile: "activity.log"
        ```

    ??? variable string "`qbit_manage_role_qbt_cross_seed`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_cross_seed: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_recheck`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_recheck: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_cat_update`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_cat_update: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_tag_update`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_tag_update: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_rem_unregistered`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_rem_unregistered: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_rem_orphaned`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_rem_orphaned: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_tag_nohardlinks`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_tag_nohardlinks: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_skip_recycle`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_skip_recycle: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_dry_run`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_dry_run: "true"
        ```

    ??? variable string "`qbit_manage_role_qbt_log_level`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_log_level: "INFO"
        ```

    ??? variable string "`qbit_manage_role_qbt_divider`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_divider: "="
        ```

    ??? variable string "`qbit_manage_role_qbt_width`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_width: "100"
        ```

    ??? variable string "`qbit_manage_role_qbt_debug`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_debug: "false"
        ```

    ??? variable string "`qbit_manage_role_qbt_trace`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_trace: "false"
        ```

=== "Web"

    ??? variable string "`qbit_manage_role_web_subdomain`"

        ```yaml
        # Type: string
        qbit_manage_role_web_subdomain: "{{ qbit_manage_name }}"
        ```

    ??? variable string "`qbit_manage_role_web_domain`"

        ```yaml
        # Type: string
        qbit_manage_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`qbit_manage_role_web_port`"

        ```yaml
        # Type: string
        qbit_manage_role_web_port: "8080"
        ```

    ??? variable string "`qbit_manage_role_web_url`"

        ```yaml
        # Type: string
        qbit_manage_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbit_manage') + '.' + lookup('role_var', '_web_domain', role='qbit_manage')
                                   if (lookup('role_var', '_web_subdomain', role='qbit_manage') | length > 0)
                                   else lookup('role_var', '_web_domain', role='qbit_manage')) }}"
        ```

=== "DNS"

    ??? variable string "`qbit_manage_role_dns_record`"

        ```yaml
        # Type: string
        qbit_manage_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbit_manage') }}"
        ```

    ??? variable string "`qbit_manage_role_dns_zone`"

        ```yaml
        # Type: string
        qbit_manage_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbit_manage') }}"
        ```

    ??? variable bool "`qbit_manage_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`qbit_manage_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`qbit_manage_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`qbit_manage_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`qbit_manage_role_traefik_certresolver`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`qbit_manage_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_traefik_enabled: true
        ```

    ??? variable bool "`qbit_manage_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_traefik_api_enabled: true
        ```

    ??? variable string "`qbit_manage_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`qbit_manage_role_docker_container`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_container: "{{ qbit_manage_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`qbit_manage_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_image_pull: true
        ```

    ??? variable string "`qbit_manage_role_docker_image_repo`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_image_repo: "ghcr.io/hotio/qbitmanage"
        ```

    ??? variable string "`qbit_manage_role_docker_image_tag`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_image_tag: "release"
        ```

    ??? variable string "`qbit_manage_role_docker_image`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbit_manage') }}:{{ lookup('role_var', '_docker_image_tag', role='qbit_manage') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`qbit_manage_role_docker_ports_default`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_ports_default: []
        ```

    ??? variable list "`qbit_manage_role_docker_ports_custom`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`qbit_manage_role_docker_envs_default`"

        ```yaml
        # Type: dict
        qbit_manage_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"
          QBT_WEB_SERVER: "true"
          QBT_RUN: "{{ lookup('role_var', '_qbt_run', role='qbit_manage') }}"
          QBT_SCHEDULE: "{{ lookup('role_var', '_qbt_schedule', role='qbit_manage') }}"
          QBT_CONFIG: "{{ lookup('role_var', '_qbt_config', role='qbit_manage') }}"
          QBT_LOGFILE: "{{ lookup('role_var', '_qbt_logfile', role='qbit_manage') }}"
          QBT_CROSS_SEED: "{{ lookup('role_var', '_qbt_cross_seed', role='qbit_manage') }}"
          QBT_RECHECK: "{{ lookup('role_var', '_qbt_recheck', role='qbit_manage') }}"
          QBT_CAT_UPDATE: "{{ lookup('role_var', '_qbt_cat_update', role='qbit_manage') }}"
          QBT_TAG_UPDATE: "{{ lookup('role_var', '_qbt_tag_update', role='qbit_manage') }}"
          QBT_REM_UNREGISTERED: "{{ lookup('role_var', '_qbt_rem_unregistered', role='qbit_manage') }}"
          QBT_REM_ORPHANED: "{{ lookup('role_var', '_qbt_rem_orphaned', role='qbit_manage') }}"
          QBT_TAG_NOHARDLINKS: "{{ lookup('role_var', '_qbt_tag_nohardlinks', role='qbit_manage') }}"
          QBT_SKIP_RECYCLE: "{{ lookup('role_var', '_qbt_skip_recycle', role='qbit_manage') }}"
          QBT_DRY_RUN: "{{ lookup('role_var', '_qbt_dry_run', role='qbit_manage') }}"
          QBT_LOG_LEVEL: "{{ lookup('role_var', '_qbt_log_level', role='qbit_manage') }}"
          QBT_DIVIDER: "{{ lookup('role_var', '_qbt_divider', role='qbit_manage') }}"
          QBT_WIDTH: "{{ lookup('role_var', '_qbt_width', role='qbit_manage') }}"
          QBT_DEBUG: "{{ lookup('role_var', '_qbt_debug', role='qbit_manage') }}"
          QBT_TRACE: "{{ lookup('role_var', '_qbt_trace', role='qbit_manage') }}"
        ```

    ??? variable dict "`qbit_manage_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        qbit_manage_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`qbit_manage_role_docker_volumes_default`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='qbit_manage') }}:/config"
        ```

    ??? variable list "`qbit_manage_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`qbit_manage_role_docker_hostname`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_hostname: "{{ qbit_manage_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`qbit_manage_role_docker_networks_alias`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_networks_alias: "{{ qbit_manage_name }}"
        ```

    ??? variable list "`qbit_manage_role_docker_networks_default`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_networks_default: []
        ```

    ??? variable list "`qbit_manage_role_docker_networks_custom`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`qbit_manage_role_docker_restart_policy`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_restart_policy: on-failure
        ```

    ??? variable int "`qbit_manage_role_docker_restart_retries`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_restart_retries: 3
        ```

    <h5>State</h5>

    ??? variable string "`qbit_manage_role_docker_state`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`qbit_manage_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_blkio_weight:
        ```

    ??? variable int "`qbit_manage_role_docker_cpu_period`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_cpu_period:
        ```

    ??? variable int "`qbit_manage_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_cpu_quota:
        ```

    ??? variable int "`qbit_manage_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_cpu_shares:
        ```

    ??? variable string "`qbit_manage_role_docker_cpus`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_cpus:
        ```

    ??? variable string "`qbit_manage_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_cpuset_cpus:
        ```

    ??? variable string "`qbit_manage_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_cpuset_mems:
        ```

    ??? variable string "`qbit_manage_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_kernel_memory:
        ```

    ??? variable string "`qbit_manage_role_docker_memory`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_memory:
        ```

    ??? variable string "`qbit_manage_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_memory_reservation:
        ```

    ??? variable string "`qbit_manage_role_docker_memory_swap`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_memory_swap:
        ```

    ??? variable int "`qbit_manage_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_memory_swappiness:
        ```

    ??? variable string "`qbit_manage_role_docker_shm_size`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`qbit_manage_role_docker_cap_drop`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_cap_drop:
        ```

    ??? variable string "`qbit_manage_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_cgroupns_mode:
        ```

    ??? variable list "`qbit_manage_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`qbit_manage_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_device_read_bps:
        ```

    ??? variable list "`qbit_manage_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_device_read_iops:
        ```

    ??? variable list "`qbit_manage_role_docker_device_requests`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_device_requests:
        ```

    ??? variable list "`qbit_manage_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_device_write_bps:
        ```

    ??? variable list "`qbit_manage_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_device_write_iops:
        ```

    ??? variable list "`qbit_manage_role_docker_devices`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_devices:
        ```

    ??? variable string "`qbit_manage_role_docker_devices_default`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_devices_default:
        ```

    ??? variable list "`qbit_manage_role_docker_groups`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_groups:
        ```

    ??? variable bool "`qbit_manage_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_privileged:
        ```

    ??? variable list "`qbit_manage_role_docker_security_opts`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_security_opts:
        ```

    ??? variable string "`qbit_manage_role_docker_user`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_user:
        ```

    ??? variable string "`qbit_manage_role_docker_userns_mode`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`qbit_manage_role_docker_dns_opts`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_dns_opts:
        ```

    ??? variable list "`qbit_manage_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_dns_search_domains:
        ```

    ??? variable list "`qbit_manage_role_docker_dns_servers`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_dns_servers:
        ```

    ??? variable string "`qbit_manage_role_docker_domainname`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_domainname:
        ```

    ??? variable list "`qbit_manage_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_exposed_ports:
        ```

    ??? variable dict "`qbit_manage_role_docker_hosts`"

        ```yaml
        # Type: dict
        qbit_manage_role_docker_hosts:
        ```

    ??? variable bool "`qbit_manage_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_hosts_use_common:
        ```

    ??? variable string "`qbit_manage_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_ipc_mode:
        ```

    ??? variable list "`qbit_manage_role_docker_links`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_links:
        ```

    ??? variable string "`qbit_manage_role_docker_network_mode`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_network_mode:
        ```

    ??? variable string "`qbit_manage_role_docker_pid_mode`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_pid_mode:
        ```

    ??? variable string "`qbit_manage_role_docker_uts`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`qbit_manage_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_keep_volumes:
        ```

    ??? variable list "`qbit_manage_role_docker_mounts`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_mounts:
        ```

    ??? variable dict "`qbit_manage_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        qbit_manage_role_docker_storage_opts:
        ```

    ??? variable list "`qbit_manage_role_docker_tmpfs`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_tmpfs:
        ```

    ??? variable string "`qbit_manage_role_docker_volume_driver`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_volume_driver:
        ```

    ??? variable list "`qbit_manage_role_docker_volumes_from`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_volumes_from:
        ```

    ??? variable bool "`qbit_manage_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_volumes_global:
        ```

    ??? variable string "`qbit_manage_role_docker_working_dir`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`qbit_manage_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_auto_remove:
        ```

    ??? variable bool "`qbit_manage_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_cleanup:
        ```

    ??? variable string "`qbit_manage_role_docker_force_kill`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_force_kill:
        ```

    ??? variable dict "`qbit_manage_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        qbit_manage_role_docker_healthcheck:
        ```

    ??? variable int "`qbit_manage_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`qbit_manage_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_init:
        ```

    ??? variable string "`qbit_manage_role_docker_kill_signal`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_kill_signal:
        ```

    ??? variable string "`qbit_manage_role_docker_log_driver`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_log_driver:
        ```

    ??? variable dict "`qbit_manage_role_docker_log_options`"

        ```yaml
        # Type: dict
        qbit_manage_role_docker_log_options:
        ```

    ??? variable bool "`qbit_manage_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_oom_killer:
        ```

    ??? variable int "`qbit_manage_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_oom_score_adj:
        ```

    ??? variable bool "`qbit_manage_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_output_logs:
        ```

    ??? variable bool "`qbit_manage_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_paused:
        ```

    ??? variable bool "`qbit_manage_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_recreate:
        ```

    ??? variable int "`qbit_manage_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`qbit_manage_role_docker_capabilities`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_capabilities:
        ```

    ??? variable string "`qbit_manage_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_cgroup_parent:
        ```

    ??? variable list "`qbit_manage_role_docker_commands`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_commands:
        ```

    ??? variable int "`qbit_manage_role_docker_create_timeout`"

        ```yaml
        # Type: int
        qbit_manage_role_docker_create_timeout:
        ```

    ??? variable string "`qbit_manage_role_docker_entrypoint`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_entrypoint:
        ```

    ??? variable string "`qbit_manage_role_docker_env_file`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_env_file:
        ```

    ??? variable dict "`qbit_manage_role_docker_labels`"

        ```yaml
        # Type: dict
        qbit_manage_role_docker_labels:
        ```

    ??? variable bool "`qbit_manage_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_labels_use_common:
        ```

    ??? variable bool "`qbit_manage_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_read_only:
        ```

    ??? variable string "`qbit_manage_role_docker_runtime`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_runtime:
        ```

    ??? variable list "`qbit_manage_role_docker_sysctls`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_sysctls:
        ```

    ??? variable list "`qbit_manage_role_docker_ulimits`"

        ```yaml
        # Type: list
        qbit_manage_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`qbit_manage_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        qbit_manage_role_autoheal_enabled: true
        ```

    ??? variable string "`qbit_manage_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        qbit_manage_role_depends_on: ""
        ```

    ??? variable string "`qbit_manage_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        qbit_manage_role_depends_on_delay: "0"
        ```

    ??? variable string "`qbit_manage_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbit_manage_role_depends_on_healthchecks:
        ```

    ??? variable bool "`qbit_manage_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        qbit_manage_role_diun_enabled: true
        ```

    ??? variable bool "`qbit_manage_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        qbit_manage_role_dns_enabled: true
        ```

    ??? variable bool "`qbit_manage_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        qbit_manage_role_docker_controller: true
        ```

    ??? variable string "`qbit_manage_role_docker_image_repo`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_image_repo:
        ```

    ??? variable string "`qbit_manage_role_docker_image_tag`"

        ```yaml
        # Type: string
        qbit_manage_role_docker_image_tag:
        ```

    ??? variable bool "`qbit_manage_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_docker_volumes_download:
        ```

    ??? variable string "`qbit_manage_role_paths_location`"

        ```yaml
        # Type: string
        qbit_manage_role_paths_location:
        ```

    ??? variable string "`qbit_manage_role_qbt_cat_update`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_cat_update:
        ```

    ??? variable string "`qbit_manage_role_qbt_config`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_config:
        ```

    ??? variable string "`qbit_manage_role_qbt_cross_seed`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_cross_seed:
        ```

    ??? variable string "`qbit_manage_role_qbt_debug`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_debug:
        ```

    ??? variable string "`qbit_manage_role_qbt_divider`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_divider:
        ```

    ??? variable string "`qbit_manage_role_qbt_dry_run`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_dry_run:
        ```

    ??? variable string "`qbit_manage_role_qbt_log_level`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_log_level:
        ```

    ??? variable string "`qbit_manage_role_qbt_logfile`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_logfile:
        ```

    ??? variable string "`qbit_manage_role_qbt_recheck`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_recheck:
        ```

    ??? variable string "`qbit_manage_role_qbt_rem_orphaned`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_rem_orphaned:
        ```

    ??? variable string "`qbit_manage_role_qbt_rem_unregistered`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_rem_unregistered:
        ```

    ??? variable string "`qbit_manage_role_qbt_run`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_run:
        ```

    ??? variable string "`qbit_manage_role_qbt_schedule`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_schedule:
        ```

    ??? variable string "`qbit_manage_role_qbt_skip_recycle`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_skip_recycle:
        ```

    ??? variable string "`qbit_manage_role_qbt_tag_nohardlinks`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_tag_nohardlinks:
        ```

    ??? variable string "`qbit_manage_role_qbt_tag_update`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_tag_update:
        ```

    ??? variable string "`qbit_manage_role_qbt_trace`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_trace:
        ```

    ??? variable string "`qbit_manage_role_qbt_width`"

        ```yaml
        # Type: string
        qbit_manage_role_qbt_width:
        ```

    ??? variable string "`qbit_manage_role_themepark_addons`"

        ```yaml
        # Type: string
        qbit_manage_role_themepark_addons:
        ```

    ??? variable string "`qbit_manage_role_themepark_app`"

        ```yaml
        # Type: string
        qbit_manage_role_themepark_app:
        ```

    ??? variable string "`qbit_manage_role_themepark_theme`"

        ```yaml
        # Type: string
        qbit_manage_role_themepark_theme:
        ```

    ??? variable dict "`qbit_manage_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        qbit_manage_role_traefik_api_endpoint:
        ```

    ??? variable string "`qbit_manage_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_api_middleware:
        ```

    ??? variable string "`qbit_manage_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`qbit_manage_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        qbit_manage_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`qbit_manage_role_traefik_certresolver`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_certresolver:
        ```

    ??? variable bool "`qbit_manage_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        qbit_manage_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`qbit_manage_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        qbit_manage_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`qbit_manage_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        qbit_manage_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`qbit_manage_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_middleware_http:
        ```

    ??? variable bool "`qbit_manage_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`qbit_manage_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        qbit_manage_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`qbit_manage_role_traefik_priority`"

        ```yaml
        # Type: string
        qbit_manage_role_traefik_priority:
        ```

    ??? variable bool "`qbit_manage_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        qbit_manage_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`qbit_manage_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        qbit_manage_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`qbit_manage_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        qbit_manage_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`qbit_manage_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        qbit_manage_role_web_api_http_port:
        ```

    ??? variable string "`qbit_manage_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        qbit_manage_role_web_api_http_scheme:
        ```

    ??? variable dict "`qbit_manage_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        qbit_manage_role_web_api_http_serverstransport:
        ```

    ??? variable string "`qbit_manage_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        qbit_manage_role_web_api_port:
        ```

    ??? variable string "`qbit_manage_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        qbit_manage_role_web_api_scheme:
        ```

    ??? variable dict "`qbit_manage_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        qbit_manage_role_web_api_serverstransport:
        ```

    ??? variable string "`qbit_manage_role_web_domain`"

        ```yaml
        # Type: string
        qbit_manage_role_web_domain:
        ```

    ??? variable list "`qbit_manage_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        qbit_manage_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            qbit_manage_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbit_manage2.{{ user.domain }}"
              - "qbit_manage.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`qbit_manage_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        qbit_manage_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            qbit_manage_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbit_manage2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`qbit_manage_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        qbit_manage_role_web_http_port:
        ```

    ??? variable string "`qbit_manage_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        qbit_manage_role_web_http_scheme:
        ```

    ??? variable dict "`qbit_manage_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        qbit_manage_role_web_http_serverstransport:
        ```

    ??? variable string "`qbit_manage_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        qbit_manage_role_web_scheme:
        ```

    ??? variable dict "`qbit_manage_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        qbit_manage_role_web_serverstransport:
        ```

    ??? variable string "`qbit_manage_role_web_subdomain`"

        ```yaml
        # Type: string
        qbit_manage_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
