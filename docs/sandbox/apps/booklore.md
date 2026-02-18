---
icon: material/docker
hide:
  - tags
tags:
  - booklore
  - ebooks
  - reading
saltbox_automation:
  app_links:
    - name: Manual
      url: https://booklore.org/docs/getting-started
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/booklore/booklore/tags
      type: docker
    - name: Community
      url: https://discord.gg/Ee5hd458Uz
      type: discord
  project_description:
    name: Booklore
    summary: |-
      a powerful, self-hosted web application designed to organize and manage your personal book collection with elegance and ease. Build your dream library with an intuitive interface, robust metadata management, and seamless multi-user support.
    link: https://booklore.org
    categories:
      - Content Delivery Apps > Reader
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Booklore

## Overview

[Booklore](https://booklore.org) is a powerful, self-hosted web application designed to organize and manage your personal book collection with elegance and ease. Build your dream library with an intuitive interface, robust metadata management, and seamless multi-user support.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://booklore.org/docs/getting-started){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/booklore/booklore/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/Ee5hd458Uz){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

The *Bookdrop* location is managed by the role and defaults to `/mnt/unionfs/downloads/bookdrop` (based on your [downloads root](../../reference/accounts.md#__tabbed_2_2)), where other apps have access to place downloads in.

To rename the subdirectory, you can use `booklore_role_bookdrop_subfolder`, detailed in the Settings tab below.

## Deployment

```shell
sb install sandbox-booklore
```

## Usage

Visit <https://booklore.iYOUR_DOMAIN_NAMEi>.

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
        booklore_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `booklore_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `booklore_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`booklore_name`"

        ```yaml
        # Type: string
        booklore_name: booklore
        ```

=== "Settings"

    ??? variable string "`booklore_role_media_subfolder`"

        ```yaml
        # Name of a subdirectory to be created in /mnt/unionfs/Media/
        # Opt out with a falsy value (e.g. "")
        # Type: string
        booklore_role_media_subfolder: "Books"
        ```

    ??? variable string "`booklore_role_bookdrop_subfolder`"

        ```yaml
        # Name of the Bookdrop subdirectory
        # Will be placed in the downloads root: usually /mnt/unionfs/downloads/
        # Type: string
        booklore_role_bookdrop_subfolder: "bookdrop"
        ```

    ??? variable string "`booklore_role_mariadb_name`"

        ```yaml
        # Type: string
        booklore_role_mariadb_name: "{{ booklore_name }}-mariadb"
        ```

    ??? variable string "`booklore_role_mariadb_paths_folder`"

        ```yaml
        # Type: string
        booklore_role_mariadb_paths_folder: "{{ booklore_name }}"
        ```

    ??? variable string "`booklore_role_mariadb_paths_location`"

        ```yaml
        # Type: string
        booklore_role_mariadb_paths_location: "{{ server_appdata_path }}/{{ booklore_role_mariadb_paths_folder }}/mariadb"
        ```

    ??? variable string "`booklore_role_mariadb_docker_image_tag`"

        ```yaml
        # Type: string
        booklore_role_mariadb_docker_image_tag: "11.4"
        ```

    ??? variable string "`booklore_role_mariadb_docker_env_db`"

        ```yaml
        # Type: string
        booklore_role_mariadb_docker_env_db: "{{ booklore_name }}-mariadb"
        ```

=== "Web"

    ??? variable string "`booklore_role_web_subdomain`"

        ```yaml
        # Type: string
        booklore_role_web_subdomain: "{{ booklore_name }}"
        ```

    ??? variable string "`booklore_role_web_domain`"

        ```yaml
        # Type: string
        booklore_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`booklore_role_web_port`"

        ```yaml
        # Type: string
        booklore_role_web_port: "6060"
        ```

    ??? variable string "`booklore_role_web_url`"

        ```yaml
        # Type: string
        booklore_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='booklore') + '.' + lookup('role_var', '_web_domain', role='booklore')
                                if (lookup('role_var', '_web_subdomain', role='booklore') | length > 0)
                                else lookup('role_var', '_web_domain', role='booklore')) }}"
        ```

=== "DNS"

    ??? variable string "`booklore_role_dns_record`"

        ```yaml
        # Type: string
        booklore_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='booklore') }}"
        ```

    ??? variable string "`booklore_role_dns_zone`"

        ```yaml
        # Type: string
        booklore_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='booklore') }}"
        ```

    ??? variable bool "`booklore_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_dns_proxy: "{{ dns.proxied }}"
        ```

=== "Traefik"

    ??? variable string "`booklore_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        booklore_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`booklore_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        booklore_role_traefik_middleware_default: "{{ traefik_default_middleware }},booklore-kobo-sync-headers"
        ```

    ??? variable string "`booklore_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        booklore_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`booklore_role_traefik_certresolver`"

        ```yaml
        # Type: string
        booklore_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`booklore_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`booklore_role_docker_container`"

        ```yaml
        # Type: string
        booklore_role_docker_container: "{{ booklore_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`booklore_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_image_pull: true
        ```

    ??? variable string "`booklore_role_docker_image_tag`"

        ```yaml
        # Type: string
        booklore_role_docker_image_tag: "latest"
        ```

    ??? variable string "`booklore_role_docker_image_repo`"

        ```yaml
        # Type: string
        booklore_role_docker_image_repo: "booklore/booklore"
        ```

    ??? variable string "`booklore_role_docker_image`"

        ```yaml
        # Type: string
        booklore_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='booklore') }}:{{ lookup('role_var', '_docker_image_tag', role='booklore') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`booklore_role_docker_envs_default`"

        ```yaml
        # Type: dict
        booklore_role_docker_envs_default:
          TZ: "{{ tz }}"
          USER_ID: "{{ uid }}"
          GROUP_ID: "{{ gid }}"
          DATABASE_URL: "jdbc:mariadb://{{ booklore_name }}-mariadb:3306/{{ lookup('role_var', '_mariadb_docker_env_db', role='booklore') }}"
          DATABASE_USERNAME: "root"
          DATABASE_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          APP_BOOKDROP_FOLDER: "{{ lookup('role_var', '_paths_bookdrop_location', role='booklore') }}"
        ```

    ??? variable dict "`booklore_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        booklore_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`booklore_role_docker_volumes_default`"

        ```yaml
        # Type: list
        booklore_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='booklore') }}/data:/app/data"
        ```

    ??? variable list "`booklore_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        booklore_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`booklore_role_docker_labels_default`"

        ```yaml
        # Type: dict
        booklore_role_docker_labels_default:
          traefik.http.middlewares.booklore-kobo-sync-headers.headers.customrequestheaders.X-Scheme: "https"
        ```

    ??? variable dict "`booklore_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        booklore_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`booklore_role_docker_hostname`"

        ```yaml
        # Type: string
        booklore_role_docker_hostname: "{{ booklore_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`booklore_role_docker_networks_alias`"

        ```yaml
        # Type: string
        booklore_role_docker_networks_alias: "{{ booklore_name }}"
        ```

    ??? variable list "`booklore_role_docker_networks_default`"

        ```yaml
        # Type: list
        booklore_role_docker_networks_default: []
        ```

    ??? variable list "`booklore_role_docker_networks_custom`"

        ```yaml
        # Type: list
        booklore_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`booklore_role_docker_restart_policy`"

        ```yaml
        # Type: string
        booklore_role_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`booklore_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        booklore_role_docker_stop_timeout: 10
        ```

    <h5>State</h5>

    ??? variable string "`booklore_role_docker_state`"

        ```yaml
        # Type: string
        booklore_role_docker_state: started
        ```

    <h5>Healthcheck</h5>

    ??? variable dict "`booklore_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        booklore_role_docker_healthcheck:
          test: wget -q -O - http://localhost:6060/api/v1/healthcheck
          interval: 60s
          retries: 5
          start_period: 60s
          timeout: 10s
        ```

    <h5>Dependencies</h5>

    ??? variable string "`booklore_role_depends_on`"

        ```yaml
        # Type: string
        booklore_role_depends_on: "{{ booklore_name }}-mariadb"
        ```

    ??? variable string "`booklore_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        booklore_role_depends_on_delay: "0"
        ```

    ??? variable string "`booklore_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        booklore_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`booklore_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        booklore_role_docker_blkio_weight:
        ```

    ??? variable int "`booklore_role_docker_cpu_period`"

        ```yaml
        # Type: int
        booklore_role_docker_cpu_period:
        ```

    ??? variable int "`booklore_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        booklore_role_docker_cpu_quota:
        ```

    ??? variable int "`booklore_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        booklore_role_docker_cpu_shares:
        ```

    ??? variable string "`booklore_role_docker_cpus`"

        ```yaml
        # Type: string
        booklore_role_docker_cpus:
        ```

    ??? variable string "`booklore_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        booklore_role_docker_cpuset_cpus:
        ```

    ??? variable string "`booklore_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        booklore_role_docker_cpuset_mems:
        ```

    ??? variable string "`booklore_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        booklore_role_docker_kernel_memory:
        ```

    ??? variable string "`booklore_role_docker_memory`"

        ```yaml
        # Type: string
        booklore_role_docker_memory:
        ```

    ??? variable string "`booklore_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        booklore_role_docker_memory_reservation:
        ```

    ??? variable string "`booklore_role_docker_memory_swap`"

        ```yaml
        # Type: string
        booklore_role_docker_memory_swap:
        ```

    ??? variable int "`booklore_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        booklore_role_docker_memory_swappiness:
        ```

    ??? variable string "`booklore_role_docker_shm_size`"

        ```yaml
        # Type: string
        booklore_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`booklore_role_docker_cap_drop`"

        ```yaml
        # Type: list
        booklore_role_docker_cap_drop:
        ```

    ??? variable string "`booklore_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        booklore_role_docker_cgroupns_mode:
        ```

    ??? variable list "`booklore_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        booklore_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`booklore_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        booklore_role_docker_device_read_bps:
        ```

    ??? variable list "`booklore_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        booklore_role_docker_device_read_iops:
        ```

    ??? variable list "`booklore_role_docker_device_requests`"

        ```yaml
        # Type: list
        booklore_role_docker_device_requests:
        ```

    ??? variable list "`booklore_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        booklore_role_docker_device_write_bps:
        ```

    ??? variable list "`booklore_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        booklore_role_docker_device_write_iops:
        ```

    ??? variable list "`booklore_role_docker_devices`"

        ```yaml
        # Type: list
        booklore_role_docker_devices:
        ```

    ??? variable list "`booklore_role_docker_groups`"

        ```yaml
        # Type: list
        booklore_role_docker_groups:
        ```

    ??? variable bool "`booklore_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_privileged:
        ```

    ??? variable list "`booklore_role_docker_security_opts`"

        ```yaml
        # Type: list
        booklore_role_docker_security_opts:
        ```

    ??? variable string "`booklore_role_docker_user`"

        ```yaml
        # Type: string
        booklore_role_docker_user:
        ```

    ??? variable string "`booklore_role_docker_userns_mode`"

        ```yaml
        # Type: string
        booklore_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`booklore_role_docker_dns_opts`"

        ```yaml
        # Type: list
        booklore_role_docker_dns_opts:
        ```

    ??? variable list "`booklore_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        booklore_role_docker_dns_search_domains:
        ```

    ??? variable list "`booklore_role_docker_dns_servers`"

        ```yaml
        # Type: list
        booklore_role_docker_dns_servers:
        ```

    ??? variable string "`booklore_role_docker_domainname`"

        ```yaml
        # Type: string
        booklore_role_docker_domainname:
        ```

    ??? variable list "`booklore_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        booklore_role_docker_exposed_ports:
        ```

    ??? variable dict "`booklore_role_docker_hosts`"

        ```yaml
        # Type: dict
        booklore_role_docker_hosts:
        ```

    ??? variable bool "`booklore_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_hosts_use_common:
        ```

    ??? variable string "`booklore_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        booklore_role_docker_ipc_mode:
        ```

    ??? variable list "`booklore_role_docker_links`"

        ```yaml
        # Type: list
        booklore_role_docker_links:
        ```

    ??? variable string "`booklore_role_docker_network_mode`"

        ```yaml
        # Type: string
        booklore_role_docker_network_mode:
        ```

    ??? variable string "`booklore_role_docker_pid_mode`"

        ```yaml
        # Type: string
        booklore_role_docker_pid_mode:
        ```

    ??? variable list "`booklore_role_docker_ports`"

        ```yaml
        # Type: list
        booklore_role_docker_ports:
        ```

    ??? variable string "`booklore_role_docker_uts`"

        ```yaml
        # Type: string
        booklore_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`booklore_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_keep_volumes:
        ```

    ??? variable list "`booklore_role_docker_mounts`"

        ```yaml
        # Type: list
        booklore_role_docker_mounts:
        ```

    ??? variable dict "`booklore_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        booklore_role_docker_storage_opts:
        ```

    ??? variable list "`booklore_role_docker_tmpfs`"

        ```yaml
        # Type: list
        booklore_role_docker_tmpfs:
        ```

    ??? variable string "`booklore_role_docker_volume_driver`"

        ```yaml
        # Type: string
        booklore_role_docker_volume_driver:
        ```

    ??? variable list "`booklore_role_docker_volumes_from`"

        ```yaml
        # Type: list
        booklore_role_docker_volumes_from:
        ```

    ??? variable bool "`booklore_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_volumes_global:
        ```

    ??? variable string "`booklore_role_docker_working_dir`"

        ```yaml
        # Type: string
        booklore_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`booklore_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_auto_remove:
        ```

    ??? variable bool "`booklore_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_cleanup:
        ```

    ??? variable string "`booklore_role_docker_force_kill`"

        ```yaml
        # Type: string
        booklore_role_docker_force_kill:
        ```

    ??? variable int "`booklore_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        booklore_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`booklore_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_init:
        ```

    ??? variable string "`booklore_role_docker_kill_signal`"

        ```yaml
        # Type: string
        booklore_role_docker_kill_signal:
        ```

    ??? variable string "`booklore_role_docker_log_driver`"

        ```yaml
        # Type: string
        booklore_role_docker_log_driver:
        ```

    ??? variable dict "`booklore_role_docker_log_options`"

        ```yaml
        # Type: dict
        booklore_role_docker_log_options:
        ```

    ??? variable bool "`booklore_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_oom_killer:
        ```

    ??? variable int "`booklore_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        booklore_role_docker_oom_score_adj:
        ```

    ??? variable bool "`booklore_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_output_logs:
        ```

    ??? variable bool "`booklore_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_paused:
        ```

    ??? variable bool "`booklore_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_recreate:
        ```

    ??? variable int "`booklore_role_docker_restart_retries`"

        ```yaml
        # Type: int
        booklore_role_docker_restart_retries:
        ```

    ??? variable string "`booklore_role_docker_stop_signal`"

        ```yaml
        # Type: string
        booklore_role_docker_stop_signal:
        ```

    <h5>Other Options</h5>

    ??? variable list "`booklore_role_docker_capabilities`"

        ```yaml
        # Type: list
        booklore_role_docker_capabilities:
        ```

    ??? variable string "`booklore_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        booklore_role_docker_cgroup_parent:
        ```

    ??? variable list "`booklore_role_docker_commands`"

        ```yaml
        # Type: list
        booklore_role_docker_commands:
        ```

    ??? variable int "`booklore_role_docker_create_timeout`"

        ```yaml
        # Type: int
        booklore_role_docker_create_timeout:
        ```

    ??? variable string "`booklore_role_docker_entrypoint`"

        ```yaml
        # Type: string
        booklore_role_docker_entrypoint:
        ```

    ??? variable string "`booklore_role_docker_env_file`"

        ```yaml
        # Type: string
        booklore_role_docker_env_file:
        ```

    ??? variable bool "`booklore_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_labels_use_common:
        ```

    ??? variable bool "`booklore_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_read_only:
        ```

    ??? variable string "`booklore_role_docker_runtime`"

        ```yaml
        # Type: string
        booklore_role_docker_runtime:
        ```

    ??? variable list "`booklore_role_docker_sysctls`"

        ```yaml
        # Type: list
        booklore_role_docker_sysctls:
        ```

    ??? variable list "`booklore_role_docker_ulimits`"

        ```yaml
        # Type: list
        booklore_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`booklore_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        booklore_role_autoheal_enabled: true
        ```

    ??? variable bool "`booklore_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        booklore_role_diun_enabled: true
        ```

    ??? variable bool "`booklore_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        booklore_role_dns_enabled: true
        ```

    ??? variable bool "`booklore_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        booklore_role_docker_controller: true
        ```

    ??? variable list "`booklore_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        booklore_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`booklore_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_docker_volumes_download:
        ```

    ??? variable string "`booklore_role_themepark_addons`"

        ```yaml
        # Type: string
        booklore_role_themepark_addons:
        ```

    ??? variable string "`booklore_role_themepark_app`"

        ```yaml
        # Type: string
        booklore_role_themepark_app:
        ```

    ??? variable string "`booklore_role_themepark_theme`"

        ```yaml
        # Type: string
        booklore_role_themepark_theme:
        ```

    ??? variable dict "`booklore_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        booklore_role_traefik_api_endpoint:
        ```

    ??? variable string "`booklore_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        booklore_role_traefik_api_middleware:
        ```

    ??? variable string "`booklore_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        booklore_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`booklore_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        booklore_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`booklore_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        booklore_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`booklore_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        booklore_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`booklore_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        booklore_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`booklore_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        booklore_role_traefik_middleware_http:
        ```

    ??? variable bool "`booklore_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`booklore_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        booklore_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`booklore_role_traefik_priority`"

        ```yaml
        # Type: string
        booklore_role_traefik_priority:
        ```

    ??? variable bool "`booklore_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        booklore_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`booklore_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        booklore_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`booklore_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        booklore_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`booklore_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        booklore_role_web_api_http_port:
        ```

    ??? variable string "`booklore_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        booklore_role_web_api_http_scheme:
        ```

    ??? variable dict "`booklore_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        booklore_role_web_api_http_serverstransport:
        ```

    ??? variable string "`booklore_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        booklore_role_web_api_port:
        ```

    ??? variable string "`booklore_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        booklore_role_web_api_scheme:
        ```

    ??? variable dict "`booklore_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        booklore_role_web_api_serverstransport:
        ```

    ??? variable list "`booklore_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        booklore_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            booklore_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "booklore2.{{ user.domain }}"
              - "booklore.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`booklore_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        booklore_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            booklore_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'booklore2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`booklore_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        booklore_role_web_http_port:
        ```

    ??? variable string "`booklore_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        booklore_role_web_http_scheme:
        ```

    ??? variable dict "`booklore_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        booklore_role_web_http_serverstransport:
        ```

    ??? variable string "`booklore_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        booklore_role_web_scheme:
        ```

    ??? variable dict "`booklore_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        booklore_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
