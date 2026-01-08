---
icon: material/docker
hide:
  - tags
tags:
  - linkwarden
  - bookmarks
  - collaboration
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
      url: https://docs.linkwarden.app
      type: documentation
    - name: Releases
      url: https://github.com/linkwarden/linkwarden/pkgs/container/linkwarden
      type: github
    - name: Community
      url: https://discord.gg/CtuYV47nuJ
      type: discord
  project_description:
    name: LinkWarden
    summary: |
      a self-hosted collaborative bookmark manager designed to collect, read, annotate, and fully preserve web content. It automatically captures screenshots, PDFs, and HTML files of bookmarked pages to prevent link rot.
    link: https://linkwarden.app
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# LinkWarden

## Overview

[LinkWarden](https://linkwarden.app) is a self-hosted collaborative bookmark manager designed to collect, read, annotate, and fully preserve web content. It automatically captures screenshots, PDFs, and HTML files of bookmarked pages to prevent link rot.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.linkwarden.app){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/linkwarden/linkwarden/pkgs/container/linkwarden){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/CtuYV47nuJ){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-linkwarden
```

## Usage

Visit <https://linkwarden.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        linkwarden_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `linkwarden_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `linkwarden_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`linkwarden_name`"

        ```yaml
        # Type: string
        linkwarden_name: linkwarden
        ```

=== "Settings"

    ??? variable bool "`linkwarden_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_postgres_deploy: true
        ```

    ??? variable string "`linkwarden_role_postgres_name`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_name: "{{ linkwarden_name }}-postgres"
        ```

    ??? variable string "`linkwarden_role_postgres_user`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_user: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_password`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_password: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_docker_env_db: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_docker_image_tag: "16-alpine"
        ```

    ??? variable string "`linkwarden_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`linkwarden_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        linkwarden_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='linkwarden') }} -U {{ lookup('role_var', '_postgres_user', role='linkwarden') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`linkwarden_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_paths_folder: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_paths_location`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_paths_location: "{{ server_appdata_path }}/{{ linkwarden_role_postgres_paths_folder }}/postgres"
        ```

=== "Web"

    ??? variable string "`linkwarden_role_web_subdomain`"

        ```yaml
        # Type: string
        linkwarden_role_web_subdomain: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_web_domain`"

        ```yaml
        # Type: string
        linkwarden_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`linkwarden_role_web_port`"

        ```yaml
        # Type: string
        linkwarden_role_web_port: "3000"
        ```

    ??? variable string "`linkwarden_role_web_url`"

        ```yaml
        # Type: string
        linkwarden_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='linkwarden') + '.' + lookup('role_var', '_web_domain', role='linkwarden')
                                  if (lookup('role_var', '_web_subdomain', role='linkwarden') | length > 0)
                                  else lookup('role_var', '_web_domain', role='linkwarden')) }}"
        ```

=== "DNS"

    ??? variable string "`linkwarden_role_dns_record`"

        ```yaml
        # Type: string
        linkwarden_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='linkwarden') }}"
        ```

    ??? variable string "`linkwarden_role_dns_zone`"

        ```yaml
        # Type: string
        linkwarden_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='linkwarden') }}"
        ```

    ??? variable bool "`linkwarden_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`linkwarden_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`linkwarden_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`linkwarden_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`linkwarden_role_traefik_certresolver`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`linkwarden_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_traefik_enabled: true
        ```

    ??? variable bool "`linkwarden_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_traefik_api_enabled: true
        ```

    ??? variable string "`linkwarden_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`linkwarden_role_docker_container`"

        ```yaml
        # Type: string
        linkwarden_role_docker_container: "{{ linkwarden_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`linkwarden_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_image_pull: true
        ```

    ??? variable string "`linkwarden_role_docker_image_tag`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image_tag: "latest"
        ```

    ??? variable string "`linkwarden_role_docker_image_repo`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image_repo: "ghcr.io/linkwarden/linkwarden"
        ```

    ??? variable string "`linkwarden_role_docker_image`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='linkwarden') }}:{{ lookup('role_var', '_docker_image_tag', role='linkwarden') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`linkwarden_role_docker_envs_default`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_envs_default:
          TZ: "{{ tz }}"
          NEXT_PUBLIC_CREDENTIALS_ENABLED: "true"
          STORAGE_FOLDER: "/data"
          NEXTAUTH_SECRET: "{{ linkwarden_secret_key.stdout }}"
          NEXTAUTH_URL: "{{ lookup('role_var', '_web_url', role='linkwarden') }}/api/v1/auth"
          DATABASE_URL: "postgresql://{{ lookup('role_var', '_postgres_user', role='linkwarden') }}:{{ lookup('role_var', '_postgres_password', role='linkwarden') }}@{{ lookup('role_var', '_postgres_name', role='linkwarden') }}:5432/{{ lookup('role_var', '_postgres_docker_env_db', role='linkwarden') }}"
        ```

    ??? variable dict "`linkwarden_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`linkwarden_role_docker_volumes_default`"

        ```yaml
        # Type: list
        linkwarden_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='linkwarden') }}:/data/data"
        ```

    ??? variable list "`linkwarden_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        linkwarden_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`linkwarden_role_docker_hostname`"

        ```yaml
        # Type: string
        linkwarden_role_docker_hostname: "{{ linkwarden_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`linkwarden_role_docker_networks_alias`"

        ```yaml
        # Type: string
        linkwarden_role_docker_networks_alias: "{{ linkwarden_name }}"
        ```

    ??? variable list "`linkwarden_role_docker_networks_default`"

        ```yaml
        # Type: list
        linkwarden_role_docker_networks_default: []
        ```

    ??? variable list "`linkwarden_role_docker_networks_custom`"

        ```yaml
        # Type: list
        linkwarden_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`linkwarden_role_docker_restart_policy`"

        ```yaml
        # Type: string
        linkwarden_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`linkwarden_role_docker_state`"

        ```yaml
        # Type: string
        linkwarden_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`linkwarden_role_depends_on`"

        ```yaml
        # Type: string
        linkwarden_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='linkwarden') }}"
        ```

    ??? variable string "`linkwarden_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        linkwarden_role_depends_on_delay: "0"
        ```

    ??? variable string "`linkwarden_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        linkwarden_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`linkwarden_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        linkwarden_role_docker_blkio_weight:
        ```

    ??? variable int "`linkwarden_role_docker_cpu_period`"

        ```yaml
        # Type: int
        linkwarden_role_docker_cpu_period:
        ```

    ??? variable int "`linkwarden_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        linkwarden_role_docker_cpu_quota:
        ```

    ??? variable int "`linkwarden_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        linkwarden_role_docker_cpu_shares:
        ```

    ??? variable string "`linkwarden_role_docker_cpus`"

        ```yaml
        # Type: string
        linkwarden_role_docker_cpus:
        ```

    ??? variable string "`linkwarden_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        linkwarden_role_docker_cpuset_cpus:
        ```

    ??? variable string "`linkwarden_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        linkwarden_role_docker_cpuset_mems:
        ```

    ??? variable string "`linkwarden_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        linkwarden_role_docker_kernel_memory:
        ```

    ??? variable string "`linkwarden_role_docker_memory`"

        ```yaml
        # Type: string
        linkwarden_role_docker_memory:
        ```

    ??? variable string "`linkwarden_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        linkwarden_role_docker_memory_reservation:
        ```

    ??? variable string "`linkwarden_role_docker_memory_swap`"

        ```yaml
        # Type: string
        linkwarden_role_docker_memory_swap:
        ```

    ??? variable int "`linkwarden_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        linkwarden_role_docker_memory_swappiness:
        ```

    ??? variable string "`linkwarden_role_docker_shm_size`"

        ```yaml
        # Type: string
        linkwarden_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`linkwarden_role_docker_cap_drop`"

        ```yaml
        # Type: list
        linkwarden_role_docker_cap_drop:
        ```

    ??? variable string "`linkwarden_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        linkwarden_role_docker_cgroupns_mode:
        ```

    ??? variable list "`linkwarden_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        linkwarden_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`linkwarden_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        linkwarden_role_docker_device_read_bps:
        ```

    ??? variable list "`linkwarden_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        linkwarden_role_docker_device_read_iops:
        ```

    ??? variable list "`linkwarden_role_docker_device_requests`"

        ```yaml
        # Type: list
        linkwarden_role_docker_device_requests:
        ```

    ??? variable list "`linkwarden_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        linkwarden_role_docker_device_write_bps:
        ```

    ??? variable list "`linkwarden_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        linkwarden_role_docker_device_write_iops:
        ```

    ??? variable list "`linkwarden_role_docker_devices`"

        ```yaml
        # Type: list
        linkwarden_role_docker_devices:
        ```

    ??? variable string "`linkwarden_role_docker_devices_default`"

        ```yaml
        # Type: string
        linkwarden_role_docker_devices_default:
        ```

    ??? variable list "`linkwarden_role_docker_groups`"

        ```yaml
        # Type: list
        linkwarden_role_docker_groups:
        ```

    ??? variable bool "`linkwarden_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_privileged:
        ```

    ??? variable list "`linkwarden_role_docker_security_opts`"

        ```yaml
        # Type: list
        linkwarden_role_docker_security_opts:
        ```

    ??? variable string "`linkwarden_role_docker_user`"

        ```yaml
        # Type: string
        linkwarden_role_docker_user:
        ```

    ??? variable string "`linkwarden_role_docker_userns_mode`"

        ```yaml
        # Type: string
        linkwarden_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`linkwarden_role_docker_dns_opts`"

        ```yaml
        # Type: list
        linkwarden_role_docker_dns_opts:
        ```

    ??? variable list "`linkwarden_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        linkwarden_role_docker_dns_search_domains:
        ```

    ??? variable list "`linkwarden_role_docker_dns_servers`"

        ```yaml
        # Type: list
        linkwarden_role_docker_dns_servers:
        ```

    ??? variable string "`linkwarden_role_docker_domainname`"

        ```yaml
        # Type: string
        linkwarden_role_docker_domainname:
        ```

    ??? variable list "`linkwarden_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        linkwarden_role_docker_exposed_ports:
        ```

    ??? variable dict "`linkwarden_role_docker_hosts`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_hosts:
        ```

    ??? variable bool "`linkwarden_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_hosts_use_common:
        ```

    ??? variable string "`linkwarden_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        linkwarden_role_docker_ipc_mode:
        ```

    ??? variable list "`linkwarden_role_docker_links`"

        ```yaml
        # Type: list
        linkwarden_role_docker_links:
        ```

    ??? variable string "`linkwarden_role_docker_network_mode`"

        ```yaml
        # Type: string
        linkwarden_role_docker_network_mode:
        ```

    ??? variable string "`linkwarden_role_docker_pid_mode`"

        ```yaml
        # Type: string
        linkwarden_role_docker_pid_mode:
        ```

    ??? variable list "`linkwarden_role_docker_ports`"

        ```yaml
        # Type: list
        linkwarden_role_docker_ports:
        ```

    ??? variable string "`linkwarden_role_docker_uts`"

        ```yaml
        # Type: string
        linkwarden_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`linkwarden_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_keep_volumes:
        ```

    ??? variable list "`linkwarden_role_docker_mounts`"

        ```yaml
        # Type: list
        linkwarden_role_docker_mounts:
        ```

    ??? variable dict "`linkwarden_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_storage_opts:
        ```

    ??? variable list "`linkwarden_role_docker_tmpfs`"

        ```yaml
        # Type: list
        linkwarden_role_docker_tmpfs:
        ```

    ??? variable string "`linkwarden_role_docker_volume_driver`"

        ```yaml
        # Type: string
        linkwarden_role_docker_volume_driver:
        ```

    ??? variable list "`linkwarden_role_docker_volumes_from`"

        ```yaml
        # Type: list
        linkwarden_role_docker_volumes_from:
        ```

    ??? variable bool "`linkwarden_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_volumes_global:
        ```

    ??? variable string "`linkwarden_role_docker_working_dir`"

        ```yaml
        # Type: string
        linkwarden_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`linkwarden_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_auto_remove:
        ```

    ??? variable bool "`linkwarden_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_cleanup:
        ```

    ??? variable string "`linkwarden_role_docker_force_kill`"

        ```yaml
        # Type: string
        linkwarden_role_docker_force_kill:
        ```

    ??? variable dict "`linkwarden_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_healthcheck:
        ```

    ??? variable int "`linkwarden_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        linkwarden_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`linkwarden_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_init:
        ```

    ??? variable string "`linkwarden_role_docker_kill_signal`"

        ```yaml
        # Type: string
        linkwarden_role_docker_kill_signal:
        ```

    ??? variable string "`linkwarden_role_docker_log_driver`"

        ```yaml
        # Type: string
        linkwarden_role_docker_log_driver:
        ```

    ??? variable dict "`linkwarden_role_docker_log_options`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_log_options:
        ```

    ??? variable bool "`linkwarden_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_oom_killer:
        ```

    ??? variable int "`linkwarden_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        linkwarden_role_docker_oom_score_adj:
        ```

    ??? variable bool "`linkwarden_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_output_logs:
        ```

    ??? variable bool "`linkwarden_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_paused:
        ```

    ??? variable bool "`linkwarden_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_recreate:
        ```

    ??? variable int "`linkwarden_role_docker_restart_retries`"

        ```yaml
        # Type: int
        linkwarden_role_docker_restart_retries:
        ```

    ??? variable int "`linkwarden_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        linkwarden_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`linkwarden_role_docker_capabilities`"

        ```yaml
        # Type: list
        linkwarden_role_docker_capabilities:
        ```

    ??? variable string "`linkwarden_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        linkwarden_role_docker_cgroup_parent:
        ```

    ??? variable list "`linkwarden_role_docker_commands`"

        ```yaml
        # Type: list
        linkwarden_role_docker_commands:
        ```

    ??? variable int "`linkwarden_role_docker_create_timeout`"

        ```yaml
        # Type: int
        linkwarden_role_docker_create_timeout:
        ```

    ??? variable string "`linkwarden_role_docker_entrypoint`"

        ```yaml
        # Type: string
        linkwarden_role_docker_entrypoint:
        ```

    ??? variable string "`linkwarden_role_docker_env_file`"

        ```yaml
        # Type: string
        linkwarden_role_docker_env_file:
        ```

    ??? variable dict "`linkwarden_role_docker_labels`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_labels:
        ```

    ??? variable bool "`linkwarden_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_labels_use_common:
        ```

    ??? variable bool "`linkwarden_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_read_only:
        ```

    ??? variable string "`linkwarden_role_docker_runtime`"

        ```yaml
        # Type: string
        linkwarden_role_docker_runtime:
        ```

    ??? variable list "`linkwarden_role_docker_sysctls`"

        ```yaml
        # Type: list
        linkwarden_role_docker_sysctls:
        ```

    ??? variable list "`linkwarden_role_docker_ulimits`"

        ```yaml
        # Type: list
        linkwarden_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`linkwarden_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        linkwarden_role_autoheal_enabled: true
        ```

    ??? variable string "`linkwarden_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        linkwarden_role_depends_on: ""
        ```

    ??? variable string "`linkwarden_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        linkwarden_role_depends_on_delay: "0"
        ```

    ??? variable string "`linkwarden_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        linkwarden_role_depends_on_healthchecks:
        ```

    ??? variable bool "`linkwarden_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        linkwarden_role_diun_enabled: true
        ```

    ??? variable bool "`linkwarden_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        linkwarden_role_dns_enabled: true
        ```

    ??? variable bool "`linkwarden_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        linkwarden_role_docker_controller: true
        ```

    ??? variable string "`linkwarden_role_docker_image_repo`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image_repo:
        ```

    ??? variable string "`linkwarden_role_docker_image_tag`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image_tag:
        ```

    ??? variable bool "`linkwarden_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_volumes_download:
        ```

    ??? variable string "`linkwarden_role_paths_location`"

        ```yaml
        # Type: string
        linkwarden_role_paths_location:
        ```

    ??? variable string "`linkwarden_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_docker_env_db:
        ```

    ??? variable string "`linkwarden_role_postgres_name`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_name:
        ```

    ??? variable string "`linkwarden_role_postgres_password`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_password:
        ```

    ??? variable string "`linkwarden_role_postgres_user`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_user:
        ```

    ??? variable string "`linkwarden_role_themepark_addons`"

        ```yaml
        # Type: string
        linkwarden_role_themepark_addons:
        ```

    ??? variable string "`linkwarden_role_themepark_app`"

        ```yaml
        # Type: string
        linkwarden_role_themepark_app:
        ```

    ??? variable string "`linkwarden_role_themepark_theme`"

        ```yaml
        # Type: string
        linkwarden_role_themepark_theme:
        ```

    ??? variable dict "`linkwarden_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        linkwarden_role_traefik_api_endpoint:
        ```

    ??? variable string "`linkwarden_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_api_middleware:
        ```

    ??? variable string "`linkwarden_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`linkwarden_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`linkwarden_role_traefik_certresolver`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_certresolver:
        ```

    ??? variable bool "`linkwarden_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`linkwarden_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_middleware_http:
        ```

    ??? variable bool "`linkwarden_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`linkwarden_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`linkwarden_role_traefik_priority`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_priority:
        ```

    ??? variable bool "`linkwarden_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`linkwarden_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`linkwarden_role_web_domain`"

        ```yaml
        # Type: string
        linkwarden_role_web_domain:
        ```

    ??? variable list "`linkwarden_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        linkwarden_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            linkwarden_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "linkwarden2.{{ user.domain }}"
              - "linkwarden.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`linkwarden_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        linkwarden_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            linkwarden_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'linkwarden2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`linkwarden_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        linkwarden_role_web_http_port:
        ```

    ??? variable string "`linkwarden_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        linkwarden_role_web_http_scheme:
        ```

    ??? variable dict "`linkwarden_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        linkwarden_role_web_http_serverstransport:
        ```

    ??? variable string "`linkwarden_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        linkwarden_role_web_scheme:
        ```

    ??? variable dict "`linkwarden_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        linkwarden_role_web_serverstransport:
        ```

    ??? variable string "`linkwarden_role_web_subdomain`"

        ```yaml
        # Type: string
        linkwarden_role_web_subdomain:
        ```

    ??? variable string "`linkwarden_role_web_url`"

        ```yaml
        # Type: string
        linkwarden_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
