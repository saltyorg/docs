---
icon: material/docker
title: NZBHydra2
hide:
  - tags
tags:
  - nzbhydra
  - nzbhydra2
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.linuxserver.io/general/container-customization
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/nzbhydra2/tags
      type: docker
    - name: Community
      url: https://linuxserver.io/discord
      type: discord
  project_description:
    name: NZBHydra2
    summary: |-
      a meta search tool designed to aggregate results from various Usenet indexers and torrent trackers into a single, unified interface.
    link: https://github.com/theotherp/nzbhydra2
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# NZBHydra2

## Overview

[NZBHydra2](https://github.com/theotherp/nzbhydra2) is a meta search tool designed to aggregate results from various Usenet indexers and torrent trackers into a single, unified interface.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.linuxserver.io/general/container-customization){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/nzbhydra2/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! abstract cta "Saltbox Setup Process"

    <div data-search-exclude>

    <div>

    Opting for another indexer manager?

    <div>

    [**Explore alternatives**:material-shuffle-variant:](index.md#indexer-management){ .md-button }

    [**Skip to qBittorrent**:material-fast-forward:](qbittorrent.md){ .md-button }

    </div>

    </div>

    </div>

## Deployment

```shell
sb install nzbydra2
```

## Usage

Visit <https://nzbhydra2.iYOUR_DOMAIN_NAMEi>.

## Basics

!!! tip "Three ways to setup NZB indexers with Sonarr/Radarr/Lidarr"

    - Skip this page and add all your NZB Indexers directly into Sonarr/Radarr/Lidarr. Benefit from the seeing indexer sources during manual lookups in Sonarr/Radarr/Lidarr. This method is also useful when diagnosing issues with indexers during failed searches;

    - Add all your NZB Indexers directly into Sonarr/Radarr/Lidarr, but also add them in NZBHydra2, so it could be used a tool for manual downloads; or

    - Add all your NZB indexers in NZBHydra2 and then just add the one NZBHydra2 "indexer" into Sonarr/Radarr/Lidarr. This is the most popular choice among users.

1.  Enter setup by clicking on "Config" at the top.

1.  Main: Under 'Security', click the icon next to the 'API key *' field to generate an API key. Click 'Save'.

1.  Authorization: Login settings are preset out of the box (`user` / `passwd` as set in [accounts.yml](../reference/accounts.md)).

1.  Indexers: Add your indexers. Click "Save".

1.  Downloaders: NZBGet settings are preset out of the box.

1.  API Key: To find the NZBHydra2 API Key, go to "Config" --> "Main". This will be used later in [Sonarr](sonarr.md) and [Radarr](radarr.md).

## Next

<div class="sb-cta" markdown>

Are you setting Saltbox up for the first time?

<div markdown>

[**Continue to qBittorrent**:material-forward:](qbittorrent.md){ .md-button }

</div>

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        nzbhydra2_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `nzbhydra2_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `nzbhydra2_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`nzbhydra2_name`"

        ```yaml
        # Type: string
        nzbhydra2_name: nzbhydra2
        ```

=== "Web"

    ??? variable string "`nzbhydra2_role_web_subdomain`"

        ```yaml
        # Type: string
        nzbhydra2_role_web_subdomain: "{{ nzbhydra2_name }}"
        ```

    ??? variable string "`nzbhydra2_role_web_domain`"

        ```yaml
        # Type: string
        nzbhydra2_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`nzbhydra2_role_web_port`"

        ```yaml
        # Type: string
        nzbhydra2_role_web_port: "5076"
        ```

    ??? variable string "`nzbhydra2_role_web_url`"

        ```yaml
        # Type: string
        nzbhydra2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nzbhydra2') + '.' + lookup('role_var', '_web_domain', role='nzbhydra2')
                                 if (lookup('role_var', '_web_subdomain', role='nzbhydra2') | length > 0)
                                 else lookup('role_var', '_web_domain', role='nzbhydra2')) }}"
        ```

=== "DNS"

    ??? variable string "`nzbhydra2_role_dns_record`"

        ```yaml
        # Type: string
        nzbhydra2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nzbhydra2') }}"
        ```

    ??? variable string "`nzbhydra2_role_dns_zone`"

        ```yaml
        # Type: string
        nzbhydra2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nzbhydra2') }}"
        ```

    ??? variable bool "`nzbhydra2_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`nzbhydra2_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`nzbhydra2_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                       + (',themepark-' + nzbhydra2_name
                                                         if (lookup('role_var', '_themepark_enabled', role='nzbhydra2') and global_themepark_plugin_enabled)
                                                         else '') }}"
        ```

    ??? variable string "`nzbhydra2_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`nzbhydra2_role_traefik_certresolver`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`nzbhydra2_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_traefik_enabled: true
        ```

    ??? variable bool "`nzbhydra2_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_traefik_api_enabled: true
        ```

    ??? variable string "`nzbhydra2_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/getnzb`) || PathPrefix(`/gettorrent`) || PathPrefix(`/rss`) || PathPrefix(`/torznab/api`)"
        ```

=== "Theme"

    ??? variable bool "`nzbhydra2_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        nzbhydra2_role_themepark_enabled: false
        ```

    ??? variable string "`nzbhydra2_role_themepark_app`"

        ```yaml
        # Type: string
        nzbhydra2_role_themepark_app: "nzbhydra2"
        ```

    ??? variable string "`nzbhydra2_role_themepark_theme`"

        ```yaml
        # Type: string
        nzbhydra2_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`nzbhydra2_role_themepark_domain`"

        ```yaml
        # Type: string
        nzbhydra2_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`nzbhydra2_role_themepark_addons`"

        ```yaml
        # Type: list
        nzbhydra2_role_themepark_addons: []
        ```

=== "Config"

    ??? variable string "`nzbhydra2_role_config_settings_jvm_memory`"

        ```yaml
        # Type: string
        nzbhydra2_role_config_settings_jvm_memory: "{{ ((ansible_facts['memory_mb']['real']['total'] / 1024)
                                                       | round(0, 'ceil') | int >= 8)
                                                       | ternary('512', '256') }}"
        ```

    ??? variable string "`nzbhydra2_role_config_settings_default`"

        ```yaml
        # Type: string
        nzbhydra2_role_config_settings_default:
          # NZBGet
          - del(.downloading.downloaders)
          - .downloading.downloaders[0].apiKey = "{{ nzbhydra2_sabnzbd_api_lookup | default('not-found') }}"
          - .downloading.downloaders[0].defaultCategory = null
          - .downloading.downloaders[0].downloadType = "NZB" | .downloading.downloaders[0].downloadType style="double"
          - .downloading.downloaders[0].enabled = true
          - .downloading.downloaders[0].iconCssClass = ""
          - .downloading.downloaders[0].name = "SABnzbd" | .downloading.downloaders[0].name style="double"
          - .downloading.downloaders[0].nzbAddingType = "UPLOAD" | .downloading.downloaders[0].nzbAddingType style="double"
          - .downloading.downloaders[0].downloaderType = "SABNZBD" | .downloading.downloaders[0].downloaderType style="double"
          - .downloading.downloaders[0].url = "http://{{ lookup('role_var', '_docker_networks_alias', role='sabnzbd') }}:{{ lookup('role_var', '_web_port', role='sabnzbd') }}" | .downloading.downloaders[0].url style="double"
          - .downloading.downloaders[0].username = null
          - .downloading.downloaders[0].password = null
          - .downloading.downloaders[0].addPaused = false
          # JVM Memory. If RAM >= 8GB, set XMX to 512, else 256.
          - .main.xmx = {{ lookup('role_var', '_config_settings_jvm_memory', role='nzbhydra2') }}
        ```

    ??? variable list "`nzbhydra2_role_config_settings_custom`"

        ```yaml
        # Type: list
        nzbhydra2_role_config_settings_custom: []
        ```

    ??? variable string "`nzbhydra2_role_config_settings_list`"

        ```yaml
        # Type: string
        nzbhydra2_role_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='nzbhydra2')
                                                 + lookup('role_var', '_config_settings_custom', role='nzbhydra2') }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`nzbhydra2_role_docker_container`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_container: "{{ nzbhydra2_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`nzbhydra2_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_image_pull: true
        ```

    ??? variable string "`nzbhydra2_role_docker_image_repo`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_image_repo: "lscr.io/linuxserver/nzbhydra2"
        ```

    ??? variable string "`nzbhydra2_role_docker_image_tag`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_image_tag: "latest"
        ```

    ??? variable string "`nzbhydra2_role_docker_image`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nzbhydra2') }}:{{ lookup('role_var', '_docker_image_tag', role='nzbhydra2') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`nzbhydra2_role_docker_envs_default`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`nzbhydra2_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`nzbhydra2_role_docker_volumes_default`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_volumes_default:
          - "{{ nzbhydra2_role_paths_location }}:/config"
        ```

    ??? variable list "`nzbhydra2_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`nzbhydra2_role_docker_labels_default`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_labels_default: {}
        ```

    ??? variable dict "`nzbhydra2_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`nzbhydra2_role_docker_hostname`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_hostname: "{{ nzbhydra2_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`nzbhydra2_role_docker_networks_alias`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_networks_alias: "{{ nzbhydra2_name }}"
        ```

    ??? variable list "`nzbhydra2_role_docker_networks_default`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_networks_default: []
        ```

    ??? variable list "`nzbhydra2_role_docker_networks_custom`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`nzbhydra2_role_docker_restart_policy`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`nzbhydra2_role_docker_state`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`nzbhydra2_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_blkio_weight:
        ```

    ??? variable int "`nzbhydra2_role_docker_cpu_period`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_cpu_period:
        ```

    ??? variable int "`nzbhydra2_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_cpu_quota:
        ```

    ??? variable int "`nzbhydra2_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_cpu_shares:
        ```

    ??? variable string "`nzbhydra2_role_docker_cpus`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_cpus:
        ```

    ??? variable string "`nzbhydra2_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_cpuset_cpus:
        ```

    ??? variable string "`nzbhydra2_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_cpuset_mems:
        ```

    ??? variable string "`nzbhydra2_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_kernel_memory:
        ```

    ??? variable string "`nzbhydra2_role_docker_memory`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_memory:
        ```

    ??? variable string "`nzbhydra2_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_memory_reservation:
        ```

    ??? variable string "`nzbhydra2_role_docker_memory_swap`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_memory_swap:
        ```

    ??? variable int "`nzbhydra2_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_memory_swappiness:
        ```

    ??? variable string "`nzbhydra2_role_docker_shm_size`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`nzbhydra2_role_docker_cap_drop`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_cap_drop:
        ```

    ??? variable string "`nzbhydra2_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_cgroupns_mode:
        ```

    ??? variable list "`nzbhydra2_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`nzbhydra2_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_device_read_bps:
        ```

    ??? variable list "`nzbhydra2_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_device_read_iops:
        ```

    ??? variable list "`nzbhydra2_role_docker_device_requests`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_device_requests:
        ```

    ??? variable list "`nzbhydra2_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_device_write_bps:
        ```

    ??? variable list "`nzbhydra2_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_device_write_iops:
        ```

    ??? variable list "`nzbhydra2_role_docker_devices`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_devices:
        ```

    ??? variable list "`nzbhydra2_role_docker_groups`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_groups:
        ```

    ??? variable bool "`nzbhydra2_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_privileged:
        ```

    ??? variable list "`nzbhydra2_role_docker_security_opts`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_security_opts:
        ```

    ??? variable string "`nzbhydra2_role_docker_user`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_user:
        ```

    ??? variable string "`nzbhydra2_role_docker_userns_mode`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`nzbhydra2_role_docker_dns_opts`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_dns_opts:
        ```

    ??? variable list "`nzbhydra2_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_dns_search_domains:
        ```

    ??? variable list "`nzbhydra2_role_docker_dns_servers`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_dns_servers:
        ```

    ??? variable string "`nzbhydra2_role_docker_domainname`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_domainname:
        ```

    ??? variable list "`nzbhydra2_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_exposed_ports:
        ```

    ??? variable dict "`nzbhydra2_role_docker_hosts`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_hosts:
        ```

    ??? variable bool "`nzbhydra2_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_hosts_use_common:
        ```

    ??? variable string "`nzbhydra2_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_ipc_mode:
        ```

    ??? variable list "`nzbhydra2_role_docker_links`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_links:
        ```

    ??? variable string "`nzbhydra2_role_docker_network_mode`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_network_mode:
        ```

    ??? variable string "`nzbhydra2_role_docker_pid_mode`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_pid_mode:
        ```

    ??? variable list "`nzbhydra2_role_docker_ports`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_ports:
        ```

    ??? variable string "`nzbhydra2_role_docker_uts`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`nzbhydra2_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_keep_volumes:
        ```

    ??? variable list "`nzbhydra2_role_docker_mounts`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_mounts:
        ```

    ??? variable dict "`nzbhydra2_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_storage_opts:
        ```

    ??? variable list "`nzbhydra2_role_docker_tmpfs`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_tmpfs:
        ```

    ??? variable string "`nzbhydra2_role_docker_volume_driver`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_volume_driver:
        ```

    ??? variable list "`nzbhydra2_role_docker_volumes_from`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_volumes_from:
        ```

    ??? variable bool "`nzbhydra2_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_volumes_global:
        ```

    ??? variable string "`nzbhydra2_role_docker_working_dir`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`nzbhydra2_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_auto_remove:
        ```

    ??? variable bool "`nzbhydra2_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_cleanup:
        ```

    ??? variable string "`nzbhydra2_role_docker_force_kill`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_force_kill:
        ```

    ??? variable dict "`nzbhydra2_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_healthcheck:
        ```

    ??? variable int "`nzbhydra2_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`nzbhydra2_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_init:
        ```

    ??? variable string "`nzbhydra2_role_docker_kill_signal`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_kill_signal:
        ```

    ??? variable string "`nzbhydra2_role_docker_log_driver`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_log_driver:
        ```

    ??? variable dict "`nzbhydra2_role_docker_log_options`"

        ```yaml
        # Type: dict
        nzbhydra2_role_docker_log_options:
        ```

    ??? variable bool "`nzbhydra2_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_oom_killer:
        ```

    ??? variable int "`nzbhydra2_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_oom_score_adj:
        ```

    ??? variable bool "`nzbhydra2_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_output_logs:
        ```

    ??? variable bool "`nzbhydra2_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_paused:
        ```

    ??? variable bool "`nzbhydra2_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_recreate:
        ```

    ??? variable int "`nzbhydra2_role_docker_restart_retries`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_restart_retries:
        ```

    ??? variable string "`nzbhydra2_role_docker_stop_signal`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_stop_signal:
        ```

    ??? variable int "`nzbhydra2_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`nzbhydra2_role_docker_capabilities`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_capabilities:
        ```

    ??? variable string "`nzbhydra2_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_cgroup_parent:
        ```

    ??? variable list "`nzbhydra2_role_docker_commands`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_commands:
        ```

    ??? variable int "`nzbhydra2_role_docker_create_timeout`"

        ```yaml
        # Type: int
        nzbhydra2_role_docker_create_timeout:
        ```

    ??? variable string "`nzbhydra2_role_docker_dev_dri`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_dev_dri:
        ```

    ??? variable string "`nzbhydra2_role_docker_entrypoint`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_entrypoint:
        ```

    ??? variable string "`nzbhydra2_role_docker_env_file`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_env_file:
        ```

    ??? variable bool "`nzbhydra2_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_labels_use_common:
        ```

    ??? variable bool "`nzbhydra2_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_read_only:
        ```

    ??? variable string "`nzbhydra2_role_docker_runtime`"

        ```yaml
        # Type: string
        nzbhydra2_role_docker_runtime:
        ```

    ??? variable list "`nzbhydra2_role_docker_sysctls`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_sysctls:
        ```

    ??? variable list "`nzbhydra2_role_docker_ulimits`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`nzbhydra2_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nzbhydra2_role_autoheal_enabled: true
        ```

    ??? variable string "`nzbhydra2_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        nzbhydra2_role_depends_on: ""
        ```

    ??? variable string "`nzbhydra2_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nzbhydra2_role_depends_on_delay: "0"
        ```

    ??? variable string "`nzbhydra2_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nzbhydra2_role_depends_on_healthchecks:
        ```

    ??? variable bool "`nzbhydra2_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nzbhydra2_role_diun_enabled: true
        ```

    ??? variable bool "`nzbhydra2_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        nzbhydra2_role_dns_enabled: true
        ```

    ??? variable bool "`nzbhydra2_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nzbhydra2_role_docker_controller: true
        ```

    ??? variable list "`nzbhydra2_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        nzbhydra2_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`nzbhydra2_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_docker_volumes_download:
        ```

    ??? variable string "`nzbhydra2_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_api_middleware:
        ```

    ??? variable string "`nzbhydra2_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`nzbhydra2_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        nzbhydra2_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`nzbhydra2_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        nzbhydra2_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`nzbhydra2_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        nzbhydra2_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`nzbhydra2_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        nzbhydra2_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`nzbhydra2_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_middleware_http:
        ```

    ??? variable bool "`nzbhydra2_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`nzbhydra2_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        nzbhydra2_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`nzbhydra2_role_traefik_priority`"

        ```yaml
        # Type: string
        nzbhydra2_role_traefik_priority:
        ```

    ??? variable bool "`nzbhydra2_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        nzbhydra2_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`nzbhydra2_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        nzbhydra2_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`nzbhydra2_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        nzbhydra2_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`nzbhydra2_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        nzbhydra2_role_web_api_http_port:
        ```

    ??? variable string "`nzbhydra2_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        nzbhydra2_role_web_api_http_scheme:
        ```

    ??? variable dict "`nzbhydra2_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbhydra2_role_web_api_http_serverstransport:
        ```

    ??? variable string "`nzbhydra2_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        nzbhydra2_role_web_api_port:
        ```

    ??? variable string "`nzbhydra2_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        nzbhydra2_role_web_api_scheme:
        ```

    ??? variable dict "`nzbhydra2_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbhydra2_role_web_api_serverstransport:
        ```

    ??? variable list "`nzbhydra2_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        nzbhydra2_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            nzbhydra2_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nzbhydra22.{{ user.domain }}"
              - "nzbhydra2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`nzbhydra2_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        nzbhydra2_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            nzbhydra2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nzbhydra22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`nzbhydra2_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        nzbhydra2_role_web_http_port:
        ```

    ??? variable string "`nzbhydra2_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        nzbhydra2_role_web_http_scheme:
        ```

    ??? variable dict "`nzbhydra2_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbhydra2_role_web_http_serverstransport:
        ```

    ??? variable string "`nzbhydra2_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        nzbhydra2_role_web_scheme:
        ```

    ??? variable dict "`nzbhydra2_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        nzbhydra2_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
