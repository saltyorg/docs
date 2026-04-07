---
icon: material/docker
hide:
  - tags
tags:
  - booklore
  - ebooks
  - grimmory
  - reading
saltbox_automation:
  app_links:
    - name: Manual
      url: https://grimmory.org/docs/getting-started
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/grimmory/grimmory/tags
      type: docker
    - name: Community
      url: https://discord.gg/9YJ7HB4n8T
      type: discord
  project_description:
    name: Grimmory
    summary: |-
      a self-hosted application designed to manage your entire book collection in one place.
    link: https://grimmory.org
    categories:
      - Content Delivery Apps > Reader
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Grimmory

## Overview

[Grimmory](https://grimmory.org) is a self-hosted application designed to manage your entire book collection in one place.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://grimmory.org/docs/getting-started){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/grimmory/grimmory/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/FwqHeFWk){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

???+ warning "Migration notice for Booklore users"

    1. Remove the existing container and rename the existing directory.

        ```shell
        docker rm -f booklore booklore-mariadb
        mv /opt/booklore /opt/grimmory
        ```

    1. Add the following to your inventory to reuse the existing database.

        ```yaml
        grimmory_role_mariadb_docker_env_db: "booklore-mariadb"
        ```

    1.  [Deploy Grimmory :material-arrow-down-bold:](#deployment)

## Configuration

The [Bookdrop](https://grimmory.org/docs/bookdrop) location is managed by the role and defaults to `/mnt/unionfs/downloads/bookdrop` (based on your [downloads root](../../reference/accounts.md#__tabbed_2_2)), where other apps have access to place downloads in.

To rename the subdirectory, you can use `grimmory_role_bookdrop_subfolder`, detailed in the Settings tab below.

## Deployment

```shell
sb install sandbox-grimmory
```

## Usage

Visit <https://grimmory.iYOUR_DOMAIN_NAMEi>.

-   On your first visit you must create an admin user account.

-   After logging back in with the admin user account, create your first library.

-   Create a directory for your book files (e.g. `/mnt/unionfs/Media/Books`) or use an existing directory.

    Select that path when creating your library.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        grimmory_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `grimmory_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `grimmory_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`grimmory_name`"

        ```yaml
        # Type: string
        grimmory_name: grimmory
        ```

=== "Settings"

    ??? variable string "`grimmory_role_media_subfolder`"

        ```yaml
        # Name of a subdirectory to be created in /mnt/unionfs/Media/
        # Opt out with a falsy value (e.g. "")
        # Type: string
        grimmory_role_media_subfolder: "Books"
        ```

    ??? variable string "`grimmory_role_bookdrop_subfolder`"

        ```yaml
        # Name of the Bookdrop subdirectory
        # Will be placed in the downloads root: usually /mnt/unionfs/downloads/
        # Type: string
        grimmory_role_bookdrop_subfolder: "bookdrop"
        ```

    ??? variable string "`grimmory_role_mariadb_name`"

        ```yaml
        # Type: string
        grimmory_role_mariadb_name: "{{ grimmory_name }}-mariadb"
        ```

    ??? variable string "`grimmory_role_mariadb_paths_folder`"

        ```yaml
        # Type: string
        grimmory_role_mariadb_paths_folder: "{{ grimmory_name }}"
        ```

    ??? variable string "`grimmory_role_mariadb_paths_location`"

        ```yaml
        # Type: string
        grimmory_role_mariadb_paths_location: "{{ server_appdata_path }}/{{ grimmory_role_mariadb_paths_folder }}/mariadb"
        ```

    ??? variable string "`grimmory_role_mariadb_docker_image_tag`"

        ```yaml
        # Type: string
        grimmory_role_mariadb_docker_image_tag: "11.4"
        ```

    ??? variable string "`grimmory_role_mariadb_docker_env_db`"

        ```yaml
        # Type: string
        grimmory_role_mariadb_docker_env_db: "{{ grimmory_name }}-mariadb"
        ```

=== "Web"

    ??? variable string "`grimmory_role_web_subdomain`"

        ```yaml
        # Type: string
        grimmory_role_web_subdomain: "{{ grimmory_name }}"
        ```

    ??? variable string "`grimmory_role_web_domain`"

        ```yaml
        # Type: string
        grimmory_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`grimmory_role_web_port`"

        ```yaml
        # Type: string
        grimmory_role_web_port: "6060"
        ```

    ??? variable string "`grimmory_role_web_url`"

        ```yaml
        # Type: string
        grimmory_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='grimmory') + '.' + lookup('role_var', '_web_domain', role='grimmory')
                                if (lookup('role_var', '_web_subdomain', role='grimmory') | length > 0)
                                else lookup('role_var', '_web_domain', role='grimmory')) }}"
        ```

=== "DNS"

    ??? variable string "`grimmory_role_dns_record`"

        ```yaml
        # Type: string
        grimmory_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='grimmory') }}"
        ```

    ??? variable string "`grimmory_role_dns_zone`"

        ```yaml
        # Type: string
        grimmory_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='grimmory') }}"
        ```

    ??? variable bool "`grimmory_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_dns_proxy: "{{ dns.proxied }}"
        ```

=== "Traefik"

    ??? variable string "`grimmory_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        grimmory_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`grimmory_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        grimmory_role_traefik_middleware_default: "{{ traefik_default_middleware }},grimmory-kobo-sync-headers"
        ```

    ??? variable string "`grimmory_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        grimmory_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`grimmory_role_traefik_certresolver`"

        ```yaml
        # Type: string
        grimmory_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`grimmory_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`grimmory_role_docker_container`"

        ```yaml
        # Type: string
        grimmory_role_docker_container: "{{ grimmory_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`grimmory_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_image_pull: true
        ```

    ??? variable string "`grimmory_role_docker_image_tag`"

        ```yaml
        # Type: string
        grimmory_role_docker_image_tag: "latest"
        ```

    ??? variable string "`grimmory_role_docker_image_repo`"

        ```yaml
        # Type: string
        grimmory_role_docker_image_repo: "grimmory/grimmory"
        ```

    ??? variable string "`grimmory_role_docker_image`"

        ```yaml
        # Type: string
        grimmory_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='grimmory') }}:{{ lookup('role_var', '_docker_image_tag', role='grimmory') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`grimmory_role_docker_envs_default`"

        ```yaml
        # Type: dict
        grimmory_role_docker_envs_default:
          TZ: "{{ tz }}"
          USER_ID: "{{ uid }}"
          GROUP_ID: "{{ gid }}"
          DATABASE_URL: "jdbc:mariadb://{{ grimmory_name }}-mariadb:3306/{{ lookup('role_var', '_mariadb_docker_env_db', role='grimmory') }}"
          DATABASE_USERNAME: "root"
          DATABASE_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          APP_BOOKDROP_FOLDER: "{{ lookup('role_var', '_paths_bookdrop_location', role='grimmory') }}"
        ```

    ??? variable dict "`grimmory_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        grimmory_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`grimmory_role_docker_volumes_default`"

        ```yaml
        # Type: list
        grimmory_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='grimmory') }}/data:/app/data"
        ```

    ??? variable list "`grimmory_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        grimmory_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`grimmory_role_docker_labels_default`"

        ```yaml
        # Type: dict
        grimmory_role_docker_labels_default:
          traefik.http.middlewares.grimmory-kobo-sync-headers.headers.customrequestheaders.X-Scheme: "https"
        ```

    ??? variable dict "`grimmory_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        grimmory_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`grimmory_role_docker_hostname`"

        ```yaml
        # Type: string
        grimmory_role_docker_hostname: "{{ grimmory_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`grimmory_role_docker_networks_alias`"

        ```yaml
        # Type: string
        grimmory_role_docker_networks_alias: "{{ grimmory_name }}"
        ```

    ??? variable list "`grimmory_role_docker_networks_default`"

        ```yaml
        # Type: list
        grimmory_role_docker_networks_default: []
        ```

    ??? variable list "`grimmory_role_docker_networks_custom`"

        ```yaml
        # Type: list
        grimmory_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`grimmory_role_docker_restart_policy`"

        ```yaml
        # Type: string
        grimmory_role_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`grimmory_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        grimmory_role_docker_stop_timeout: 10
        ```

    <h5>State</h5>

    ??? variable string "`grimmory_role_docker_state`"

        ```yaml
        # Type: string
        grimmory_role_docker_state: started
        ```

    <h5>Healthcheck</h5>

    ??? variable dict "`grimmory_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        grimmory_role_docker_healthcheck:
          test: wget -q -O - http://localhost:6060/api/v1/healthcheck
          interval: 60s
          retries: 5
          start_period: 60s
          timeout: 10s
        ```

    <h5>Dependencies</h5>

    ??? variable string "`grimmory_role_depends_on`"

        ```yaml
        # Type: string
        grimmory_role_depends_on: "{{ grimmory_name }}-mariadb"
        ```

    ??? variable string "`grimmory_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        grimmory_role_depends_on_delay: "0"
        ```

    ??? variable string "`grimmory_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        grimmory_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`grimmory_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        grimmory_role_docker_blkio_weight:
        ```

    ??? variable int "`grimmory_role_docker_cpu_period`"

        ```yaml
        # Type: int
        grimmory_role_docker_cpu_period:
        ```

    ??? variable int "`grimmory_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        grimmory_role_docker_cpu_quota:
        ```

    ??? variable int "`grimmory_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        grimmory_role_docker_cpu_shares:
        ```

    ??? variable string "`grimmory_role_docker_cpus`"

        ```yaml
        # Type: string
        grimmory_role_docker_cpus:
        ```

    ??? variable string "`grimmory_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        grimmory_role_docker_cpuset_cpus:
        ```

    ??? variable string "`grimmory_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        grimmory_role_docker_cpuset_mems:
        ```

    ??? variable string "`grimmory_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        grimmory_role_docker_kernel_memory:
        ```

    ??? variable string "`grimmory_role_docker_memory`"

        ```yaml
        # Type: string
        grimmory_role_docker_memory:
        ```

    ??? variable string "`grimmory_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        grimmory_role_docker_memory_reservation:
        ```

    ??? variable string "`grimmory_role_docker_memory_swap`"

        ```yaml
        # Type: string
        grimmory_role_docker_memory_swap:
        ```

    ??? variable int "`grimmory_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        grimmory_role_docker_memory_swappiness:
        ```

    ??? variable string "`grimmory_role_docker_shm_size`"

        ```yaml
        # Type: string
        grimmory_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`grimmory_role_docker_cap_drop`"

        ```yaml
        # Type: list
        grimmory_role_docker_cap_drop:
        ```

    ??? variable string "`grimmory_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        grimmory_role_docker_cgroupns_mode:
        ```

    ??? variable list "`grimmory_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        grimmory_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`grimmory_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        grimmory_role_docker_device_read_bps:
        ```

    ??? variable list "`grimmory_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        grimmory_role_docker_device_read_iops:
        ```

    ??? variable list "`grimmory_role_docker_device_requests`"

        ```yaml
        # Type: list
        grimmory_role_docker_device_requests:
        ```

    ??? variable list "`grimmory_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        grimmory_role_docker_device_write_bps:
        ```

    ??? variable list "`grimmory_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        grimmory_role_docker_device_write_iops:
        ```

    ??? variable list "`grimmory_role_docker_devices`"

        ```yaml
        # Type: list
        grimmory_role_docker_devices:
        ```

    ??? variable list "`grimmory_role_docker_groups`"

        ```yaml
        # Type: list
        grimmory_role_docker_groups:
        ```

    ??? variable bool "`grimmory_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_privileged:
        ```

    ??? variable list "`grimmory_role_docker_security_opts`"

        ```yaml
        # Type: list
        grimmory_role_docker_security_opts:
        ```

    ??? variable string "`grimmory_role_docker_user`"

        ```yaml
        # Type: string
        grimmory_role_docker_user:
        ```

    ??? variable string "`grimmory_role_docker_userns_mode`"

        ```yaml
        # Type: string
        grimmory_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`grimmory_role_docker_dns_opts`"

        ```yaml
        # Type: list
        grimmory_role_docker_dns_opts:
        ```

    ??? variable list "`grimmory_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        grimmory_role_docker_dns_search_domains:
        ```

    ??? variable list "`grimmory_role_docker_dns_servers`"

        ```yaml
        # Type: list
        grimmory_role_docker_dns_servers:
        ```

    ??? variable string "`grimmory_role_docker_domainname`"

        ```yaml
        # Type: string
        grimmory_role_docker_domainname:
        ```

    ??? variable list "`grimmory_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        grimmory_role_docker_exposed_ports:
        ```

    ??? variable dict "`grimmory_role_docker_hosts`"

        ```yaml
        # Type: dict
        grimmory_role_docker_hosts:
        ```

    ??? variable bool "`grimmory_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_hosts_use_common:
        ```

    ??? variable string "`grimmory_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        grimmory_role_docker_ipc_mode:
        ```

    ??? variable list "`grimmory_role_docker_links`"

        ```yaml
        # Type: list
        grimmory_role_docker_links:
        ```

    ??? variable string "`grimmory_role_docker_network_mode`"

        ```yaml
        # Type: string
        grimmory_role_docker_network_mode:
        ```

    ??? variable string "`grimmory_role_docker_pid_mode`"

        ```yaml
        # Type: string
        grimmory_role_docker_pid_mode:
        ```

    ??? variable list "`grimmory_role_docker_ports`"

        ```yaml
        # Type: list
        grimmory_role_docker_ports:
        ```

    ??? variable string "`grimmory_role_docker_uts`"

        ```yaml
        # Type: string
        grimmory_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`grimmory_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_keep_volumes:
        ```

    ??? variable list "`grimmory_role_docker_mounts`"

        ```yaml
        # Type: list
        grimmory_role_docker_mounts:
        ```

    ??? variable dict "`grimmory_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        grimmory_role_docker_storage_opts:
        ```

    ??? variable list "`grimmory_role_docker_tmpfs`"

        ```yaml
        # Type: list
        grimmory_role_docker_tmpfs:
        ```

    ??? variable string "`grimmory_role_docker_volume_driver`"

        ```yaml
        # Type: string
        grimmory_role_docker_volume_driver:
        ```

    ??? variable list "`grimmory_role_docker_volumes_from`"

        ```yaml
        # Type: list
        grimmory_role_docker_volumes_from:
        ```

    ??? variable bool "`grimmory_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_volumes_global:
        ```

    ??? variable string "`grimmory_role_docker_working_dir`"

        ```yaml
        # Type: string
        grimmory_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`grimmory_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_auto_remove:
        ```

    ??? variable bool "`grimmory_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_cleanup:
        ```

    ??? variable string "`grimmory_role_docker_force_kill`"

        ```yaml
        # Type: string
        grimmory_role_docker_force_kill:
        ```

    ??? variable int "`grimmory_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        grimmory_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`grimmory_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_init:
        ```

    ??? variable string "`grimmory_role_docker_kill_signal`"

        ```yaml
        # Type: string
        grimmory_role_docker_kill_signal:
        ```

    ??? variable string "`grimmory_role_docker_log_driver`"

        ```yaml
        # Type: string
        grimmory_role_docker_log_driver:
        ```

    ??? variable dict "`grimmory_role_docker_log_options`"

        ```yaml
        # Type: dict
        grimmory_role_docker_log_options:
        ```

    ??? variable bool "`grimmory_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_oom_killer:
        ```

    ??? variable int "`grimmory_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        grimmory_role_docker_oom_score_adj:
        ```

    ??? variable bool "`grimmory_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_output_logs:
        ```

    ??? variable bool "`grimmory_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_paused:
        ```

    ??? variable bool "`grimmory_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_recreate:
        ```

    ??? variable int "`grimmory_role_docker_restart_retries`"

        ```yaml
        # Type: int
        grimmory_role_docker_restart_retries:
        ```

    ??? variable string "`grimmory_role_docker_stop_signal`"

        ```yaml
        # Type: string
        grimmory_role_docker_stop_signal:
        ```

    <h5>Other Options</h5>

    ??? variable list "`grimmory_role_docker_capabilities`"

        ```yaml
        # Type: list
        grimmory_role_docker_capabilities:
        ```

    ??? variable string "`grimmory_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        grimmory_role_docker_cgroup_parent:
        ```

    ??? variable list "`grimmory_role_docker_commands`"

        ```yaml
        # Type: list
        grimmory_role_docker_commands:
        ```

    ??? variable int "`grimmory_role_docker_create_timeout`"

        ```yaml
        # Type: int
        grimmory_role_docker_create_timeout:
        ```

    ??? variable string "`grimmory_role_docker_entrypoint`"

        ```yaml
        # Type: string
        grimmory_role_docker_entrypoint:
        ```

    ??? variable string "`grimmory_role_docker_env_file`"

        ```yaml
        # Type: string
        grimmory_role_docker_env_file:
        ```

    ??? variable bool "`grimmory_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_labels_use_common:
        ```

    ??? variable bool "`grimmory_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_read_only:
        ```

    ??? variable string "`grimmory_role_docker_runtime`"

        ```yaml
        # Type: string
        grimmory_role_docker_runtime:
        ```

    ??? variable list "`grimmory_role_docker_sysctls`"

        ```yaml
        # Type: list
        grimmory_role_docker_sysctls:
        ```

    ??? variable list "`grimmory_role_docker_ulimits`"

        ```yaml
        # Type: list
        grimmory_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`grimmory_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        grimmory_role_autoheal_enabled: true
        ```

    ??? variable bool "`grimmory_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        grimmory_role_diun_enabled: true
        ```

    ??? variable bool "`grimmory_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        grimmory_role_dns_enabled: true
        ```

    ??? variable bool "`grimmory_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        grimmory_role_docker_controller: true
        ```

    ??? variable list "`grimmory_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        grimmory_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`grimmory_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_docker_volumes_download:
        ```

    ??? variable string "`grimmory_role_themepark_addons`"

        ```yaml
        # Type: string
        grimmory_role_themepark_addons:
        ```

    ??? variable string "`grimmory_role_themepark_app`"

        ```yaml
        # Type: string
        grimmory_role_themepark_app:
        ```

    ??? variable string "`grimmory_role_themepark_theme`"

        ```yaml
        # Type: string
        grimmory_role_themepark_theme:
        ```

    ??? variable dict "`grimmory_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        grimmory_role_traefik_api_endpoint:
        ```

    ??? variable string "`grimmory_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        grimmory_role_traefik_api_middleware:
        ```

    ??? variable string "`grimmory_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        grimmory_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`grimmory_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        grimmory_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`grimmory_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        grimmory_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`grimmory_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        grimmory_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`grimmory_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        grimmory_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`grimmory_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        grimmory_role_traefik_middleware_http:
        ```

    ??? variable bool "`grimmory_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`grimmory_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        grimmory_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`grimmory_role_traefik_priority`"

        ```yaml
        # Type: string
        grimmory_role_traefik_priority:
        ```

    ??? variable bool "`grimmory_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        grimmory_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`grimmory_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        grimmory_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`grimmory_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        grimmory_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`grimmory_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        grimmory_role_web_api_http_port:
        ```

    ??? variable string "`grimmory_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        grimmory_role_web_api_http_scheme:
        ```

    ??? variable dict "`grimmory_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        grimmory_role_web_api_http_serverstransport:
        ```

    ??? variable string "`grimmory_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        grimmory_role_web_api_port:
        ```

    ??? variable string "`grimmory_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        grimmory_role_web_api_scheme:
        ```

    ??? variable dict "`grimmory_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        grimmory_role_web_api_serverstransport:
        ```

    ??? variable list "`grimmory_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        grimmory_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            grimmory_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "grimmory2.{{ user.domain }}"
              - "grimmory.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`grimmory_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        grimmory_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            grimmory_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'grimmory2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`grimmory_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        grimmory_role_web_http_port:
        ```

    ??? variable string "`grimmory_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        grimmory_role_web_http_scheme:
        ```

    ??? variable dict "`grimmory_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        grimmory_role_web_http_serverstransport:
        ```

    ??? variable string "`grimmory_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        grimmory_role_web_scheme:
        ```

    ??? variable dict "`grimmory_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        grimmory_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
