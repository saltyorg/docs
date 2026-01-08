---
icon: material/docker
hide:
  - tags
tags:
  - mylar3
  - media
  - comics
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url: https://mylarcomics.com/docs/category/guides
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/mylar3/tags
      type: docker
    - name: Community
      url: https://forum.mylarcomics.com
      type: community
  project_description:
    name: Mylar3
    summary: |
      an automated Comic Book downloader (cbr/cbz) for use with NZB and torrents written in python. It supports SABnzbd, NZBGET, and many torrent clients in addition to DDL.
    link: https://mylarcomics.com
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Mylar3

## Overview

[Mylar3](https://mylarcomics.com) is an automated Comic Book downloader (cbr/cbz) for use with NZB and torrents written in python. It supports SABnzbd, NZBGET, and many torrent clients in addition to DDL.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://mylarcomics.com/docs/category/guides){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/mylar3/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://forum.mylarcomics.com){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-mylar3
```

## Usage

Visit <https://mylar3.iYOUR_DOMAIN_NAMEi>.

## Basics

1. It's highly unlikely your mylar install is up to date. <br />
  Press the Update link on the dialog in the bottom right hand corner. Mylar3 will update and then restart.

2. Enable some authentication. Add a `username` and `password` and set your preferred `login method`.

3. Make sure `Launch Browser on startup` is disabled.

4. You'll need a [ComicVine API](https://comicvine.gamespot.com/api/) Key for Mylar to be useful. [Create an account](https://comicvine.gamespot.com/login-signup/), and your key will be at [the top of this page](https://comicvine.gamespot.com/api/).

5. Set the Comic Location path to `/comics`. It will already be mounted.

6. Uncheck `enforce permissions`

7. _Optional_: Enable `Series-Annual Integration`

8. Save and then restart the app

!!! note
      If you enable to OPDS server, DO NOT ENABLE `OPDS Fetch MetaInfo`. It queries the file system.

### Download settings

(These instructions are for NZBGet. Adapt for other Download Apps)

#### Configure NZBGet

1. Log into <https://nzbget.iYOUR_DOMAIN_NAMEi>

2. Go to `Settings > Categories`

3. Scroll to bottom, click `Add Another Category`

4. Name it `mylar`

#### Configure Mylar

1. Set Usenet client to NZBGet

1. Fill in the server stuff like it would be in sonarr / radarr / etc

1. Set values:

   1. Host: `nzbget`

   1. Port: `6789`

   1. Username:  `Your NZBGet Username`

   1. Password:  `Your NZBGet Password`

   1. Category: `mylar`

   1. Use SSL: `No`

   1. NZBGet Download Directory: Leave Blank

   1. Enable Completed Download Handling: `X`

### Search Providers

1. Click Add Indexer (`+`).

1. Select "Newznab".

1. Add the following:

      1. Use Newznab: `X`

      2. NewzNab Name: `NZBHydra2`

      3. NewzNab Host: `http://nzbhydra2:5076`

      4. Verify SSL: `Disabled`

      5. API Key: `Your NZBHydra2 API Key`

      6. Enabled: `X`

### Quality and Post Processing

1. Enable Failed Download Handling: `X`

1. Enable Automatic-Retry for Failed Downloads: `X`

1. Enable Post-Processing: `X`

1. When Post-Processing `move` the files

### Advanced Settings

These settings are up to the user

1. Rename Files: `X`

1. Folder Format: `$Series ($Year)` _(My recommendation)_

1. File Format: `$Series $Annual $Issue ($Year)` _(My recommendation)_

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        mylar3_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `mylar3_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `mylar3_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`mylar3_name`"

        ```yaml
        # Type: string
        mylar3_name: mylar3
        ```

=== "Web"

    ??? variable string "`mylar3_role_web_subdomain`"

        ```yaml
        # Type: string
        mylar3_role_web_subdomain: "{{ mylar3_name }}"
        ```

    ??? variable string "`mylar3_role_web_domain`"

        ```yaml
        # Type: string
        mylar3_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`mylar3_role_web_port`"

        ```yaml
        # Type: string
        mylar3_role_web_port: "8090"
        ```

    ??? variable string "`mylar3_role_web_url`"

        ```yaml
        # Type: string
        mylar3_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='mylar3') + '.' + lookup('role_var', '_web_domain', role='mylar3')
                              if (lookup('role_var', '_web_subdomain', role='mylar3') | length > 0)
                              else lookup('role_var', '_web_domain', role='mylar3')) }}"
        ```

=== "DNS"

    ??? variable string "`mylar3_role_dns_record`"

        ```yaml
        # Type: string
        mylar3_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='mylar3') }}"
        ```

    ??? variable string "`mylar3_role_dns_zone`"

        ```yaml
        # Type: string
        mylar3_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='mylar3') }}"
        ```

    ??? variable bool "`mylar3_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`mylar3_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        mylar3_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`mylar3_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        mylar3_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`mylar3_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        mylar3_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`mylar3_role_traefik_certresolver`"

        ```yaml
        # Type: string
        mylar3_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`mylar3_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_traefik_enabled: true
        ```

    ??? variable bool "`mylar3_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_traefik_api_enabled: false
        ```

    ??? variable string "`mylar3_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        mylar3_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`mylar3_role_docker_container`"

        ```yaml
        # Type: string
        mylar3_role_docker_container: "{{ mylar3_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`mylar3_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_image_pull: true
        ```

    ??? variable string "`mylar3_role_docker_image_tag`"

        ```yaml
        # Type: string
        mylar3_role_docker_image_tag: "latest"
        ```

    ??? variable string "`mylar3_role_docker_image_repo`"

        ```yaml
        # Type: string
        mylar3_role_docker_image_repo: "lscr.io/linuxserver/mylar3"
        ```

    ??? variable string "`mylar3_role_docker_image`"

        ```yaml
        # Type: string
        mylar3_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mylar3') }}:{{ lookup('role_var', '_docker_image_tag', role='mylar3') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`mylar3_role_docker_envs_default`"

        ```yaml
        # Type: dict
        mylar3_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`mylar3_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        mylar3_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`mylar3_role_docker_volumes_default`"

        ```yaml
        # Type: list
        mylar3_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='mylar3') }}:/config"
          - "/mnt/unionfs/Media/Comics:/comics"
        ```

    ??? variable list "`mylar3_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        mylar3_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`mylar3_role_docker_hostname`"

        ```yaml
        # Type: string
        mylar3_role_docker_hostname: "{{ mylar3_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`mylar3_role_docker_networks_alias`"

        ```yaml
        # Type: string
        mylar3_role_docker_networks_alias: "{{ mylar3_name }}"
        ```

    ??? variable list "`mylar3_role_docker_networks_default`"

        ```yaml
        # Type: list
        mylar3_role_docker_networks_default: []
        ```

    ??? variable list "`mylar3_role_docker_networks_custom`"

        ```yaml
        # Type: list
        mylar3_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`mylar3_role_docker_restart_policy`"

        ```yaml
        # Type: string
        mylar3_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`mylar3_role_docker_state`"

        ```yaml
        # Type: string
        mylar3_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`mylar3_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        mylar3_role_docker_blkio_weight:
        ```

    ??? variable int "`mylar3_role_docker_cpu_period`"

        ```yaml
        # Type: int
        mylar3_role_docker_cpu_period:
        ```

    ??? variable int "`mylar3_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        mylar3_role_docker_cpu_quota:
        ```

    ??? variable int "`mylar3_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        mylar3_role_docker_cpu_shares:
        ```

    ??? variable string "`mylar3_role_docker_cpus`"

        ```yaml
        # Type: string
        mylar3_role_docker_cpus:
        ```

    ??? variable string "`mylar3_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        mylar3_role_docker_cpuset_cpus:
        ```

    ??? variable string "`mylar3_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        mylar3_role_docker_cpuset_mems:
        ```

    ??? variable string "`mylar3_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        mylar3_role_docker_kernel_memory:
        ```

    ??? variable string "`mylar3_role_docker_memory`"

        ```yaml
        # Type: string
        mylar3_role_docker_memory:
        ```

    ??? variable string "`mylar3_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        mylar3_role_docker_memory_reservation:
        ```

    ??? variable string "`mylar3_role_docker_memory_swap`"

        ```yaml
        # Type: string
        mylar3_role_docker_memory_swap:
        ```

    ??? variable int "`mylar3_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        mylar3_role_docker_memory_swappiness:
        ```

    ??? variable string "`mylar3_role_docker_shm_size`"

        ```yaml
        # Type: string
        mylar3_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`mylar3_role_docker_cap_drop`"

        ```yaml
        # Type: list
        mylar3_role_docker_cap_drop:
        ```

    ??? variable string "`mylar3_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        mylar3_role_docker_cgroupns_mode:
        ```

    ??? variable list "`mylar3_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        mylar3_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`mylar3_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        mylar3_role_docker_device_read_bps:
        ```

    ??? variable list "`mylar3_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        mylar3_role_docker_device_read_iops:
        ```

    ??? variable list "`mylar3_role_docker_device_requests`"

        ```yaml
        # Type: list
        mylar3_role_docker_device_requests:
        ```

    ??? variable list "`mylar3_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        mylar3_role_docker_device_write_bps:
        ```

    ??? variable list "`mylar3_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        mylar3_role_docker_device_write_iops:
        ```

    ??? variable list "`mylar3_role_docker_devices`"

        ```yaml
        # Type: list
        mylar3_role_docker_devices:
        ```

    ??? variable string "`mylar3_role_docker_devices_default`"

        ```yaml
        # Type: string
        mylar3_role_docker_devices_default:
        ```

    ??? variable list "`mylar3_role_docker_groups`"

        ```yaml
        # Type: list
        mylar3_role_docker_groups:
        ```

    ??? variable bool "`mylar3_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_privileged:
        ```

    ??? variable list "`mylar3_role_docker_security_opts`"

        ```yaml
        # Type: list
        mylar3_role_docker_security_opts:
        ```

    ??? variable string "`mylar3_role_docker_user`"

        ```yaml
        # Type: string
        mylar3_role_docker_user:
        ```

    ??? variable string "`mylar3_role_docker_userns_mode`"

        ```yaml
        # Type: string
        mylar3_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`mylar3_role_docker_dns_opts`"

        ```yaml
        # Type: list
        mylar3_role_docker_dns_opts:
        ```

    ??? variable list "`mylar3_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        mylar3_role_docker_dns_search_domains:
        ```

    ??? variable list "`mylar3_role_docker_dns_servers`"

        ```yaml
        # Type: list
        mylar3_role_docker_dns_servers:
        ```

    ??? variable string "`mylar3_role_docker_domainname`"

        ```yaml
        # Type: string
        mylar3_role_docker_domainname:
        ```

    ??? variable list "`mylar3_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        mylar3_role_docker_exposed_ports:
        ```

    ??? variable dict "`mylar3_role_docker_hosts`"

        ```yaml
        # Type: dict
        mylar3_role_docker_hosts:
        ```

    ??? variable bool "`mylar3_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_hosts_use_common:
        ```

    ??? variable string "`mylar3_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        mylar3_role_docker_ipc_mode:
        ```

    ??? variable list "`mylar3_role_docker_links`"

        ```yaml
        # Type: list
        mylar3_role_docker_links:
        ```

    ??? variable string "`mylar3_role_docker_network_mode`"

        ```yaml
        # Type: string
        mylar3_role_docker_network_mode:
        ```

    ??? variable string "`mylar3_role_docker_pid_mode`"

        ```yaml
        # Type: string
        mylar3_role_docker_pid_mode:
        ```

    ??? variable list "`mylar3_role_docker_ports`"

        ```yaml
        # Type: list
        mylar3_role_docker_ports:
        ```

    ??? variable string "`mylar3_role_docker_uts`"

        ```yaml
        # Type: string
        mylar3_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`mylar3_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_keep_volumes:
        ```

    ??? variable list "`mylar3_role_docker_mounts`"

        ```yaml
        # Type: list
        mylar3_role_docker_mounts:
        ```

    ??? variable dict "`mylar3_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        mylar3_role_docker_storage_opts:
        ```

    ??? variable list "`mylar3_role_docker_tmpfs`"

        ```yaml
        # Type: list
        mylar3_role_docker_tmpfs:
        ```

    ??? variable string "`mylar3_role_docker_volume_driver`"

        ```yaml
        # Type: string
        mylar3_role_docker_volume_driver:
        ```

    ??? variable list "`mylar3_role_docker_volumes_from`"

        ```yaml
        # Type: list
        mylar3_role_docker_volumes_from:
        ```

    ??? variable bool "`mylar3_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_volumes_global:
        ```

    ??? variable string "`mylar3_role_docker_working_dir`"

        ```yaml
        # Type: string
        mylar3_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`mylar3_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_auto_remove:
        ```

    ??? variable bool "`mylar3_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_cleanup:
        ```

    ??? variable string "`mylar3_role_docker_force_kill`"

        ```yaml
        # Type: string
        mylar3_role_docker_force_kill:
        ```

    ??? variable dict "`mylar3_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        mylar3_role_docker_healthcheck:
        ```

    ??? variable int "`mylar3_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        mylar3_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`mylar3_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_init:
        ```

    ??? variable string "`mylar3_role_docker_kill_signal`"

        ```yaml
        # Type: string
        mylar3_role_docker_kill_signal:
        ```

    ??? variable string "`mylar3_role_docker_log_driver`"

        ```yaml
        # Type: string
        mylar3_role_docker_log_driver:
        ```

    ??? variable dict "`mylar3_role_docker_log_options`"

        ```yaml
        # Type: dict
        mylar3_role_docker_log_options:
        ```

    ??? variable bool "`mylar3_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_oom_killer:
        ```

    ??? variable int "`mylar3_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        mylar3_role_docker_oom_score_adj:
        ```

    ??? variable bool "`mylar3_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_output_logs:
        ```

    ??? variable bool "`mylar3_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_paused:
        ```

    ??? variable bool "`mylar3_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_recreate:
        ```

    ??? variable int "`mylar3_role_docker_restart_retries`"

        ```yaml
        # Type: int
        mylar3_role_docker_restart_retries:
        ```

    ??? variable int "`mylar3_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        mylar3_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`mylar3_role_docker_capabilities`"

        ```yaml
        # Type: list
        mylar3_role_docker_capabilities:
        ```

    ??? variable string "`mylar3_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        mylar3_role_docker_cgroup_parent:
        ```

    ??? variable list "`mylar3_role_docker_commands`"

        ```yaml
        # Type: list
        mylar3_role_docker_commands:
        ```

    ??? variable int "`mylar3_role_docker_create_timeout`"

        ```yaml
        # Type: int
        mylar3_role_docker_create_timeout:
        ```

    ??? variable string "`mylar3_role_docker_entrypoint`"

        ```yaml
        # Type: string
        mylar3_role_docker_entrypoint:
        ```

    ??? variable string "`mylar3_role_docker_env_file`"

        ```yaml
        # Type: string
        mylar3_role_docker_env_file:
        ```

    ??? variable dict "`mylar3_role_docker_labels`"

        ```yaml
        # Type: dict
        mylar3_role_docker_labels:
        ```

    ??? variable bool "`mylar3_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_labels_use_common:
        ```

    ??? variable bool "`mylar3_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_read_only:
        ```

    ??? variable string "`mylar3_role_docker_runtime`"

        ```yaml
        # Type: string
        mylar3_role_docker_runtime:
        ```

    ??? variable list "`mylar3_role_docker_sysctls`"

        ```yaml
        # Type: list
        mylar3_role_docker_sysctls:
        ```

    ??? variable list "`mylar3_role_docker_ulimits`"

        ```yaml
        # Type: list
        mylar3_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`mylar3_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        mylar3_role_autoheal_enabled: true
        ```

    ??? variable string "`mylar3_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        mylar3_role_depends_on: ""
        ```

    ??? variable string "`mylar3_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        mylar3_role_depends_on_delay: "0"
        ```

    ??? variable string "`mylar3_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mylar3_role_depends_on_healthchecks:
        ```

    ??? variable bool "`mylar3_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        mylar3_role_diun_enabled: true
        ```

    ??? variable bool "`mylar3_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        mylar3_role_dns_enabled: true
        ```

    ??? variable bool "`mylar3_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        mylar3_role_docker_controller: true
        ```

    ??? variable string "`mylar3_role_docker_image_repo`"

        ```yaml
        # Type: string
        mylar3_role_docker_image_repo:
        ```

    ??? variable string "`mylar3_role_docker_image_tag`"

        ```yaml
        # Type: string
        mylar3_role_docker_image_tag:
        ```

    ??? variable bool "`mylar3_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_docker_volumes_download:
        ```

    ??? variable string "`mylar3_role_paths_location`"

        ```yaml
        # Type: string
        mylar3_role_paths_location:
        ```

    ??? variable string "`mylar3_role_themepark_addons`"

        ```yaml
        # Type: string
        mylar3_role_themepark_addons:
        ```

    ??? variable string "`mylar3_role_themepark_app`"

        ```yaml
        # Type: string
        mylar3_role_themepark_app:
        ```

    ??? variable string "`mylar3_role_themepark_theme`"

        ```yaml
        # Type: string
        mylar3_role_themepark_theme:
        ```

    ??? variable dict "`mylar3_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        mylar3_role_traefik_api_endpoint:
        ```

    ??? variable string "`mylar3_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        mylar3_role_traefik_api_middleware:
        ```

    ??? variable string "`mylar3_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        mylar3_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`mylar3_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        mylar3_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`mylar3_role_traefik_certresolver`"

        ```yaml
        # Type: string
        mylar3_role_traefik_certresolver:
        ```

    ??? variable bool "`mylar3_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        mylar3_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`mylar3_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        mylar3_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`mylar3_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        mylar3_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`mylar3_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        mylar3_role_traefik_middleware_http:
        ```

    ??? variable bool "`mylar3_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`mylar3_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        mylar3_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`mylar3_role_traefik_priority`"

        ```yaml
        # Type: string
        mylar3_role_traefik_priority:
        ```

    ??? variable bool "`mylar3_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        mylar3_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`mylar3_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        mylar3_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`mylar3_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        mylar3_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`mylar3_role_web_domain`"

        ```yaml
        # Type: string
        mylar3_role_web_domain:
        ```

    ??? variable list "`mylar3_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        mylar3_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            mylar3_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mylar32.{{ user.domain }}"
              - "mylar3.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`mylar3_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        mylar3_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            mylar3_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mylar32.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`mylar3_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        mylar3_role_web_http_port:
        ```

    ??? variable string "`mylar3_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        mylar3_role_web_http_scheme:
        ```

    ??? variable dict "`mylar3_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        mylar3_role_web_http_serverstransport:
        ```

    ??? variable string "`mylar3_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        mylar3_role_web_scheme:
        ```

    ??? variable dict "`mylar3_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        mylar3_role_web_serverstransport:
        ```

    ??? variable string "`mylar3_role_web_subdomain`"

        ```yaml
        # Type: string
        mylar3_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->