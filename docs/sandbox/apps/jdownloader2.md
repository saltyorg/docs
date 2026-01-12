---
icon: material/docker
title: JDownloader
hide:
  - tags
tags:
  - jdownloader2
  - download
  - tools
saltbox_automation:
  app_links:
    - name: Manual
      url: https://beta.jdownloader.org/support
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/jlesage/jdownloader-2/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: JDownloader
    summary: |
      a free download-manager that makes downloading as easy, fast and automated as it should be. It's like your personal internet robot that does all the work for you. He will download whole photo albums, playlists or just about anything else with just one click. Go ahead and try it!.
    link: https://beta.jdownloader.org/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# JDownloader

## Overview

[JDownloader](https://beta.jdownloader.org/) is a free download-manager that makes downloading as easy, fast and automated as it should be. It's like your personal internet robot that does all the work for you. He will download whole photo albums, playlists or just about anything else with just one click. Go ahead and try it!.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://beta.jdownloader.org/support){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/jlesage/jdownloader-2/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-jdownloader2
```

## Usage

Visit <https://jdownloader2.iYOUR_DOMAIN_NAMEi>.

## Basics

1. The configured password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

2. Configure your myjdownloader account (Create at <https://my.jdownloader.org/> if needed) and name your instance so you can connect via web or browser extensions. Use clipboard for two step copy and paste if needed. Note that some settings are only accessible via `jdownloader2.xYOUR_DOMAIN_NAMEx`. Premium accounts such as mega.nz can be added via web interface.

3. Use manual import from sonarr / radarr and navigate to `/mnt/local/downloads/myjdownloader/output/` to import your files, note they must be already added as wanted media for import to recognise and identify your downloaded media.

4. See <https://my.jdownloader.org/> for browser extensions and phone apps as desired.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        jdownloader2_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `jdownloader2_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `jdownloader2_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`jdownloader2_name`"

        ```yaml
        # Type: string
        jdownloader2_name: jdownloader2
        ```

=== "Web"

    ??? variable string "`jdownloader2_role_web_subdomain`"

        ```yaml
        # Type: string
        jdownloader2_role_web_subdomain: "{{ jdownloader2_name }}"
        ```

    ??? variable string "`jdownloader2_role_web_domain`"

        ```yaml
        # Type: string
        jdownloader2_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`jdownloader2_role_web_port`"

        ```yaml
        # Type: string
        jdownloader2_role_web_port: "5800"
        ```

    ??? variable string "`jdownloader2_role_web_url`"

        ```yaml
        # Type: string
        jdownloader2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jdownloader2') + '.' + lookup('role_var', '_web_domain', role='jdownloader2')
                                    if (lookup('role_var', '_web_subdomain', role='jdownloader2') | length > 0)
                                    else lookup('role_var', '_web_domain', role='jdownloader2')) }}"
        ```

=== "DNS"

    ??? variable string "`jdownloader2_role_dns_record`"

        ```yaml
        # Type: string
        jdownloader2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jdownloader2') }}"
        ```

    ??? variable string "`jdownloader2_role_dns_zone`"

        ```yaml
        # Type: string
        jdownloader2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jdownloader2') }}"
        ```

    ??? variable bool "`jdownloader2_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`jdownloader2_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`jdownloader2_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`jdownloader2_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`jdownloader2_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`jdownloader2_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_api_enabled: false
        ```

    ??? variable string "`jdownloader2_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`jdownloader2_role_docker_container`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_container: "{{ jdownloader2_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`jdownloader2_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_image_pull: true
        ```

    ??? variable string "`jdownloader2_role_docker_image_repo`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image_repo: "jlesage/jdownloader-2"
        ```

    ??? variable string "`jdownloader2_role_docker_image_tag`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image_tag: "latest"
        ```

    ??? variable string "`jdownloader2_role_docker_image`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jdownloader2') }}:{{ lookup('role_var', '_docker_image_tag', role='jdownloader2') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`jdownloader2_role_docker_envs_default`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_envs_default:
          USER_ID: "{{ uid }}"
          GROUP_ID: "{{ gid }}"
          TZ: "{{ tz }}"
          DISPLAY_WIDTH: "1280"
          DISPLAY_HEIGHT: "768"
          VNC_PASSWORD: "{{ user.pass }}"
          CLEAN_TMP_DIR: "1"
          UMASK: "000"
          ENABLE_CJK_FONT: "1"
        ```

    ??? variable dict "`jdownloader2_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`jdownloader2_role_docker_volumes_default`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='jdownloader2') }}/config:/config"
          - "{{ lookup('role_var', '_paths_downloads_location', role='jdownloader2') }}:/output"
        ```

    ??? variable list "`jdownloader2_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`jdownloader2_role_docker_hostname`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_hostname: "{{ jdownloader2_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`jdownloader2_role_docker_networks_alias`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_networks_alias: "{{ jdownloader2_name }}"
        ```

    ??? variable list "`jdownloader2_role_docker_networks_default`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_networks_default: []
        ```

    ??? variable list "`jdownloader2_role_docker_networks_custom`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`jdownloader2_role_docker_restart_policy`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`jdownloader2_role_docker_state`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`jdownloader2_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_blkio_weight:
        ```

    ??? variable int "`jdownloader2_role_docker_cpu_period`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_cpu_period:
        ```

    ??? variable int "`jdownloader2_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_cpu_quota:
        ```

    ??? variable int "`jdownloader2_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_cpu_shares:
        ```

    ??? variable string "`jdownloader2_role_docker_cpus`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_cpus:
        ```

    ??? variable string "`jdownloader2_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_cpuset_cpus:
        ```

    ??? variable string "`jdownloader2_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_cpuset_mems:
        ```

    ??? variable string "`jdownloader2_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_kernel_memory:
        ```

    ??? variable string "`jdownloader2_role_docker_memory`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_memory:
        ```

    ??? variable string "`jdownloader2_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_memory_reservation:
        ```

    ??? variable string "`jdownloader2_role_docker_memory_swap`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_memory_swap:
        ```

    ??? variable int "`jdownloader2_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_memory_swappiness:
        ```

    ??? variable string "`jdownloader2_role_docker_shm_size`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`jdownloader2_role_docker_cap_drop`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_cap_drop:
        ```

    ??? variable string "`jdownloader2_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_cgroupns_mode:
        ```

    ??? variable list "`jdownloader2_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`jdownloader2_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_device_read_bps:
        ```

    ??? variable list "`jdownloader2_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_device_read_iops:
        ```

    ??? variable list "`jdownloader2_role_docker_device_requests`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_device_requests:
        ```

    ??? variable list "`jdownloader2_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_device_write_bps:
        ```

    ??? variable list "`jdownloader2_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_device_write_iops:
        ```

    ??? variable list "`jdownloader2_role_docker_devices`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_devices:
        ```

    ??? variable string "`jdownloader2_role_docker_devices_default`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_devices_default:
        ```

    ??? variable list "`jdownloader2_role_docker_groups`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_groups:
        ```

    ??? variable bool "`jdownloader2_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_privileged:
        ```

    ??? variable list "`jdownloader2_role_docker_security_opts`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_security_opts:
        ```

    ??? variable string "`jdownloader2_role_docker_user`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_user:
        ```

    ??? variable string "`jdownloader2_role_docker_userns_mode`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`jdownloader2_role_docker_dns_opts`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_dns_opts:
        ```

    ??? variable list "`jdownloader2_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_dns_search_domains:
        ```

    ??? variable list "`jdownloader2_role_docker_dns_servers`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_dns_servers:
        ```

    ??? variable string "`jdownloader2_role_docker_domainname`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_domainname:
        ```

    ??? variable list "`jdownloader2_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_exposed_ports:
        ```

    ??? variable dict "`jdownloader2_role_docker_hosts`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_hosts:
        ```

    ??? variable bool "`jdownloader2_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_hosts_use_common:
        ```

    ??? variable string "`jdownloader2_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_ipc_mode:
        ```

    ??? variable list "`jdownloader2_role_docker_links`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_links:
        ```

    ??? variable string "`jdownloader2_role_docker_network_mode`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_network_mode:
        ```

    ??? variable string "`jdownloader2_role_docker_pid_mode`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_pid_mode:
        ```

    ??? variable list "`jdownloader2_role_docker_ports`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_ports:
        ```

    ??? variable string "`jdownloader2_role_docker_uts`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`jdownloader2_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_keep_volumes:
        ```

    ??? variable list "`jdownloader2_role_docker_mounts`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_mounts:
        ```

    ??? variable dict "`jdownloader2_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_storage_opts:
        ```

    ??? variable list "`jdownloader2_role_docker_tmpfs`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_tmpfs:
        ```

    ??? variable string "`jdownloader2_role_docker_volume_driver`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_volume_driver:
        ```

    ??? variable list "`jdownloader2_role_docker_volumes_from`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_volumes_from:
        ```

    ??? variable bool "`jdownloader2_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_volumes_global:
        ```

    ??? variable string "`jdownloader2_role_docker_working_dir`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`jdownloader2_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_auto_remove:
        ```

    ??? variable bool "`jdownloader2_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_cleanup:
        ```

    ??? variable string "`jdownloader2_role_docker_force_kill`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_force_kill:
        ```

    ??? variable dict "`jdownloader2_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_healthcheck:
        ```

    ??? variable int "`jdownloader2_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`jdownloader2_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_init:
        ```

    ??? variable string "`jdownloader2_role_docker_kill_signal`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_kill_signal:
        ```

    ??? variable string "`jdownloader2_role_docker_log_driver`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_log_driver:
        ```

    ??? variable dict "`jdownloader2_role_docker_log_options`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_log_options:
        ```

    ??? variable bool "`jdownloader2_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_oom_killer:
        ```

    ??? variable int "`jdownloader2_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_oom_score_adj:
        ```

    ??? variable bool "`jdownloader2_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_output_logs:
        ```

    ??? variable bool "`jdownloader2_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_paused:
        ```

    ??? variable bool "`jdownloader2_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_recreate:
        ```

    ??? variable int "`jdownloader2_role_docker_restart_retries`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_restart_retries:
        ```

    ??? variable int "`jdownloader2_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`jdownloader2_role_docker_capabilities`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_capabilities:
        ```

    ??? variable string "`jdownloader2_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_cgroup_parent:
        ```

    ??? variable list "`jdownloader2_role_docker_commands`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_commands:
        ```

    ??? variable int "`jdownloader2_role_docker_create_timeout`"

        ```yaml
        # Type: int
        jdownloader2_role_docker_create_timeout:
        ```

    ??? variable string "`jdownloader2_role_docker_entrypoint`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_entrypoint:
        ```

    ??? variable string "`jdownloader2_role_docker_env_file`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_env_file:
        ```

    ??? variable dict "`jdownloader2_role_docker_labels`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_labels:
        ```

    ??? variable bool "`jdownloader2_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_labels_use_common:
        ```

    ??? variable bool "`jdownloader2_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_read_only:
        ```

    ??? variable string "`jdownloader2_role_docker_runtime`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_runtime:
        ```

    ??? variable list "`jdownloader2_role_docker_sysctls`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_sysctls:
        ```

    ??? variable list "`jdownloader2_role_docker_ulimits`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`jdownloader2_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jdownloader2_role_autoheal_enabled: true
        ```

    ??? variable string "`jdownloader2_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        jdownloader2_role_depends_on: ""
        ```

    ??? variable string "`jdownloader2_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        jdownloader2_role_depends_on_delay: "0"
        ```

    ??? variable string "`jdownloader2_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jdownloader2_role_depends_on_healthchecks:
        ```

    ??? variable bool "`jdownloader2_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jdownloader2_role_diun_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jdownloader2_role_dns_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jdownloader2_role_docker_controller: true
        ```

    ??? variable string "`jdownloader2_role_docker_image_repo`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image_repo:
        ```

    ??? variable string "`jdownloader2_role_docker_image_tag`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image_tag:
        ```

    ??? variable bool "`jdownloader2_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_volumes_download:
        ```

    ??? variable string "`jdownloader2_role_paths_downloads_location`"

        ```yaml
        # Type: string
        jdownloader2_role_paths_downloads_location:
        ```

    ??? variable string "`jdownloader2_role_paths_location`"

        ```yaml
        # Type: string
        jdownloader2_role_paths_location:
        ```

    ??? variable string "`jdownloader2_role_themepark_addons`"

        ```yaml
        # Type: string
        jdownloader2_role_themepark_addons:
        ```

    ??? variable string "`jdownloader2_role_themepark_app`"

        ```yaml
        # Type: string
        jdownloader2_role_themepark_app:
        ```

    ??? variable string "`jdownloader2_role_themepark_theme`"

        ```yaml
        # Type: string
        jdownloader2_role_themepark_theme:
        ```

    ??? variable dict "`jdownloader2_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        jdownloader2_role_traefik_api_endpoint:
        ```

    ??? variable string "`jdownloader2_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_api_middleware:
        ```

    ??? variable string "`jdownloader2_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`jdownloader2_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`jdownloader2_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_certresolver:
        ```

    ??? variable bool "`jdownloader2_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`jdownloader2_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_middleware_http:
        ```

    ??? variable bool "`jdownloader2_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`jdownloader2_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`jdownloader2_role_traefik_priority`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_priority:
        ```

    ??? variable bool "`jdownloader2_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`jdownloader2_role_web_domain`"

        ```yaml
        # Type: string
        jdownloader2_role_web_domain:
        ```

    ??? variable list "`jdownloader2_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jdownloader2_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            jdownloader2_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jdownloader22.{{ user.domain }}"
              - "jdownloader2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`jdownloader2_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        jdownloader2_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            jdownloader2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jdownloader22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`jdownloader2_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        jdownloader2_role_web_http_port:
        ```

    ??? variable string "`jdownloader2_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        jdownloader2_role_web_http_scheme:
        ```

    ??? variable dict "`jdownloader2_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        jdownloader2_role_web_http_serverstransport:
        ```

    ??? variable string "`jdownloader2_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jdownloader2_role_web_scheme:
        ```

    ??? variable dict "`jdownloader2_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        jdownloader2_role_web_serverstransport:
        ```

    ??? variable string "`jdownloader2_role_web_subdomain`"

        ```yaml
        # Type: string
        jdownloader2_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->