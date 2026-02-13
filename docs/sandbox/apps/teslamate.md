---
icon: material/docker
hide:
  - tags
tags:
  - teslamate
  - tesla
  - monitoring
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/teslamate-org/teslamate
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/teslamate/teslamate/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Teslamate
    summary: |-
      a powerful, self-hosted data logger for your Tesla.
    link: https://github.com/teslamate-org/teslamate
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Teslamate

## Overview

[Teslamate](https://github.com/teslamate-org/teslamate) is a powerful, self-hosted data logger for your Tesla.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/teslamate-org/teslamate){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/teslamate/teslamate/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-teslamate
```

## Usage

Visit <https://teslamate.iYOUR_DOMAIN_NAMEi>.

## Basics

- [:octicons-link-16: Documentation: Teslamate Docs](https://docs.teslamate.org/docs/installation/docker){: .header-icons }

To use a custom subdomain, add a custom value for `teslamate_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

### Grafana Setup

Once installation is finished, you will need to add the teslamate data source in grafana under connections.

Host URL: This is based upon the `{{ teslamate_name }}-postgres` variable. Default is `teslamate-postgres:5432`
Table: `teslamate`

Authentication for Postgres: Run the command below to have saltbox output the DB password.

```shell
sb install sandbox-teslamate-postgres-password
```

Save and Test

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        teslamate_secret_key: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `teslamate_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `teslamate_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Settings"

    ??? variable string "`teslamate_secret_key`"

        ```yaml
        # Type: string
        teslamate_secret_key: "{{ teslamate_saltbox_facts.facts.secret_key }}"
        ```

    ??? variable bool "`teslamate_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_postgres_deploy: true
        ```

    ??? variable string "`teslamate_role_postgres_name`"

        ```yaml
        # Type: string
        teslamate_role_postgres_name: "{{ teslamate_name }}-postgres"
        ```

    ??? variable string "`teslamate_role_postgres_user`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        teslamate_role_postgres_user: ""
        ```

    ??? variable string "`teslamate_role_postgres_password`"

        ```yaml
        # Type: string
        teslamate_role_postgres_password: "{{ teslamate_saltbox_facts.facts.postgres_password }}"
        ```

    ??? variable string "`teslamate_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        teslamate_role_postgres_docker_env_db: "{{ teslamate_name }}"
        ```

    ??? variable string "`teslamate_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        teslamate_role_postgres_docker_image_tag: "18"
        ```

    ??? variable string "`teslamate_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        teslamate_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`teslamate_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        teslamate_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='teslamate') }} -U {{ lookup('role_var', '_postgres_user', role='teslamate') if (lookup('role_var', '_postgres_user', role='teslamate') | length > 0) else lookup('role_var', '_docker_env_user', role='postgres') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`teslamate_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        teslamate_role_postgres_paths_folder: "{{ teslamate_name }}"
        ```

    ??? variable string "`teslamate_role_postgres_paths_location`"

        ```yaml
        # Type: string
        teslamate_role_postgres_paths_location: "{{ server_appdata_path }}/{{ teslamate_role_postgres_paths_folder }}/postgres"
        ```

=== "Web"

    ??? variable string "`teslamate_role_web_subdomain`"

        ```yaml
        # Type: string
        teslamate_role_web_subdomain: "{{ teslamate_name }}"
        ```

    ??? variable string "`teslamate_role_web_domain`"

        ```yaml
        # Type: string
        teslamate_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`teslamate_role_web_port`"

        ```yaml
        # Type: string
        teslamate_role_web_port: "4000"
        ```

    ??? variable string "`teslamate_role_web_url`"

        ```yaml
        # Type: string
        teslamate_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='teslamate') + '.' + lookup('role_var', '_web_domain', role='teslamate')
                                 if (lookup('role_var', '_web_subdomain', role='teslamate') | length > 0)
                                 else lookup('role_var', '_web_domain', role='teslamate')) }}"
        ```

=== "DNS"

    ??? variable string "`teslamate_role_dns_record`"

        ```yaml
        # Type: string
        teslamate_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='teslamate') }}"
        ```

    ??? variable string "`teslamate_role_dns_zone`"

        ```yaml
        # Type: string
        teslamate_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='teslamate') }}"
        ```

    ??? variable bool "`teslamate_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`teslamate_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        teslamate_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`teslamate_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        teslamate_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`teslamate_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        teslamate_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`teslamate_role_traefik_certresolver`"

        ```yaml
        # Type: string
        teslamate_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`teslamate_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_enabled: true
        ```

    ??? variable bool "`teslamate_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_api_enabled: false
        ```

    ??? variable string "`teslamate_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        teslamate_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`teslamate_role_docker_container`"

        ```yaml
        # Type: string
        teslamate_role_docker_container: "{{ teslamate_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`teslamate_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_image_pull: true
        ```

    ??? variable string "`teslamate_role_docker_image_tag`"

        ```yaml
        # Type: string
        teslamate_role_docker_image_tag: "latest"
        ```

    ??? variable string "`teslamate_role_docker_image_repo`"

        ```yaml
        # Type: string
        teslamate_role_docker_image_repo: "teslamate/teslamate"
        ```

    ??? variable string "`teslamate_role_docker_image`"

        ```yaml
        # Type: string
        teslamate_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='teslamate') }}:{{ lookup('role_var', '_docker_image_tag', role='teslamate') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`teslamate_role_docker_envs_default`"

        ```yaml
        # Type: dict
        teslamate_role_docker_envs_default:
          DATABASE_USER: "{{ lookup('role_var', '_postgres_user', role='teslamate')
                          if (lookup('role_var', '_postgres_user', role='teslamate') | length > 0)
                          else lookup('role_var', '_docker_env_user', role='postgres') }}"
          DATABASE_PASS: "{{ lookup('role_var', '_postgres_password', role='teslamate')
                          if (lookup('role_var', '_postgres_password', role='teslamate') | length > 0)
                          else lookup('role_var', '_docker_env_password', role='postgres') }}"
          DATABASE_NAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='teslamate') }}"
          ENCRYPTION_KEY: "{{ teslamate_secret_key }}"
          DATABASE_HOST: "{{ lookup('role_var', '_postgres_name', role='teslamate') }}"
          DATABASE_PORT: "5432"
          MQTT_HOST: "mqtt"
          CHECK_ORIGIN: "false"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`teslamate_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        teslamate_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`teslamate_role_docker_volumes_default`"

        ```yaml
        # Type: list
        teslamate_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='teslamate') }}:/opt/app/import"
        ```

    ??? variable list "`teslamate_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        teslamate_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`teslamate_role_docker_hostname`"

        ```yaml
        # Type: string
        teslamate_role_docker_hostname: "{{ teslamate_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`teslamate_role_docker_networks_alias`"

        ```yaml
        # Type: string
        teslamate_role_docker_networks_alias: "{{ teslamate_name }}"
        ```

    ??? variable list "`teslamate_role_docker_networks_default`"

        ```yaml
        # Type: list
        teslamate_role_docker_networks_default: []
        ```

    ??? variable list "`teslamate_role_docker_networks_custom`"

        ```yaml
        # Type: list
        teslamate_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`teslamate_role_docker_restart_policy`"

        ```yaml
        # Type: string
        teslamate_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`teslamate_role_docker_state`"

        ```yaml
        # Type: string
        teslamate_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`teslamate_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        teslamate_role_docker_blkio_weight:
        ```

    ??? variable int "`teslamate_role_docker_cpu_period`"

        ```yaml
        # Type: int
        teslamate_role_docker_cpu_period:
        ```

    ??? variable int "`teslamate_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        teslamate_role_docker_cpu_quota:
        ```

    ??? variable int "`teslamate_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        teslamate_role_docker_cpu_shares:
        ```

    ??? variable string "`teslamate_role_docker_cpus`"

        ```yaml
        # Type: string
        teslamate_role_docker_cpus:
        ```

    ??? variable string "`teslamate_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        teslamate_role_docker_cpuset_cpus:
        ```

    ??? variable string "`teslamate_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        teslamate_role_docker_cpuset_mems:
        ```

    ??? variable string "`teslamate_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        teslamate_role_docker_kernel_memory:
        ```

    ??? variable string "`teslamate_role_docker_memory`"

        ```yaml
        # Type: string
        teslamate_role_docker_memory:
        ```

    ??? variable string "`teslamate_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        teslamate_role_docker_memory_reservation:
        ```

    ??? variable string "`teslamate_role_docker_memory_swap`"

        ```yaml
        # Type: string
        teslamate_role_docker_memory_swap:
        ```

    ??? variable int "`teslamate_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        teslamate_role_docker_memory_swappiness:
        ```

    ??? variable string "`teslamate_role_docker_shm_size`"

        ```yaml
        # Type: string
        teslamate_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`teslamate_role_docker_cap_drop`"

        ```yaml
        # Type: list
        teslamate_role_docker_cap_drop:
        ```

    ??? variable string "`teslamate_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        teslamate_role_docker_cgroupns_mode:
        ```

    ??? variable list "`teslamate_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        teslamate_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`teslamate_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        teslamate_role_docker_device_read_bps:
        ```

    ??? variable list "`teslamate_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        teslamate_role_docker_device_read_iops:
        ```

    ??? variable list "`teslamate_role_docker_device_requests`"

        ```yaml
        # Type: list
        teslamate_role_docker_device_requests:
        ```

    ??? variable list "`teslamate_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        teslamate_role_docker_device_write_bps:
        ```

    ??? variable list "`teslamate_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        teslamate_role_docker_device_write_iops:
        ```

    ??? variable list "`teslamate_role_docker_devices`"

        ```yaml
        # Type: list
        teslamate_role_docker_devices:
        ```

    ??? variable list "`teslamate_role_docker_groups`"

        ```yaml
        # Type: list
        teslamate_role_docker_groups:
        ```

    ??? variable bool "`teslamate_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_privileged:
        ```

    ??? variable list "`teslamate_role_docker_security_opts`"

        ```yaml
        # Type: list
        teslamate_role_docker_security_opts:
        ```

    ??? variable string "`teslamate_role_docker_user`"

        ```yaml
        # Type: string
        teslamate_role_docker_user:
        ```

    ??? variable string "`teslamate_role_docker_userns_mode`"

        ```yaml
        # Type: string
        teslamate_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`teslamate_role_docker_dns_opts`"

        ```yaml
        # Type: list
        teslamate_role_docker_dns_opts:
        ```

    ??? variable list "`teslamate_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        teslamate_role_docker_dns_search_domains:
        ```

    ??? variable list "`teslamate_role_docker_dns_servers`"

        ```yaml
        # Type: list
        teslamate_role_docker_dns_servers:
        ```

    ??? variable string "`teslamate_role_docker_domainname`"

        ```yaml
        # Type: string
        teslamate_role_docker_domainname:
        ```

    ??? variable list "`teslamate_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        teslamate_role_docker_exposed_ports:
        ```

    ??? variable dict "`teslamate_role_docker_hosts`"

        ```yaml
        # Type: dict
        teslamate_role_docker_hosts:
        ```

    ??? variable bool "`teslamate_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_hosts_use_common:
        ```

    ??? variable string "`teslamate_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        teslamate_role_docker_ipc_mode:
        ```

    ??? variable list "`teslamate_role_docker_links`"

        ```yaml
        # Type: list
        teslamate_role_docker_links:
        ```

    ??? variable string "`teslamate_role_docker_network_mode`"

        ```yaml
        # Type: string
        teslamate_role_docker_network_mode:
        ```

    ??? variable string "`teslamate_role_docker_pid_mode`"

        ```yaml
        # Type: string
        teslamate_role_docker_pid_mode:
        ```

    ??? variable list "`teslamate_role_docker_ports`"

        ```yaml
        # Type: list
        teslamate_role_docker_ports:
        ```

    ??? variable string "`teslamate_role_docker_uts`"

        ```yaml
        # Type: string
        teslamate_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`teslamate_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_keep_volumes:
        ```

    ??? variable list "`teslamate_role_docker_mounts`"

        ```yaml
        # Type: list
        teslamate_role_docker_mounts:
        ```

    ??? variable dict "`teslamate_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        teslamate_role_docker_storage_opts:
        ```

    ??? variable list "`teslamate_role_docker_tmpfs`"

        ```yaml
        # Type: list
        teslamate_role_docker_tmpfs:
        ```

    ??? variable string "`teslamate_role_docker_volume_driver`"

        ```yaml
        # Type: string
        teslamate_role_docker_volume_driver:
        ```

    ??? variable list "`teslamate_role_docker_volumes_from`"

        ```yaml
        # Type: list
        teslamate_role_docker_volumes_from:
        ```

    ??? variable bool "`teslamate_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_volumes_global:
        ```

    ??? variable string "`teslamate_role_docker_working_dir`"

        ```yaml
        # Type: string
        teslamate_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`teslamate_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_auto_remove:
        ```

    ??? variable bool "`teslamate_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_cleanup:
        ```

    ??? variable string "`teslamate_role_docker_force_kill`"

        ```yaml
        # Type: string
        teslamate_role_docker_force_kill:
        ```

    ??? variable dict "`teslamate_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        teslamate_role_docker_healthcheck:
        ```

    ??? variable int "`teslamate_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        teslamate_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`teslamate_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_init:
        ```

    ??? variable string "`teslamate_role_docker_kill_signal`"

        ```yaml
        # Type: string
        teslamate_role_docker_kill_signal:
        ```

    ??? variable string "`teslamate_role_docker_log_driver`"

        ```yaml
        # Type: string
        teslamate_role_docker_log_driver:
        ```

    ??? variable dict "`teslamate_role_docker_log_options`"

        ```yaml
        # Type: dict
        teslamate_role_docker_log_options:
        ```

    ??? variable bool "`teslamate_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_oom_killer:
        ```

    ??? variable int "`teslamate_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        teslamate_role_docker_oom_score_adj:
        ```

    ??? variable bool "`teslamate_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_output_logs:
        ```

    ??? variable bool "`teslamate_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_paused:
        ```

    ??? variable bool "`teslamate_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_recreate:
        ```

    ??? variable int "`teslamate_role_docker_restart_retries`"

        ```yaml
        # Type: int
        teslamate_role_docker_restart_retries:
        ```

    ??? variable string "`teslamate_role_docker_stop_signal`"

        ```yaml
        # Type: string
        teslamate_role_docker_stop_signal:
        ```

    ??? variable int "`teslamate_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        teslamate_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`teslamate_role_docker_capabilities`"

        ```yaml
        # Type: list
        teslamate_role_docker_capabilities:
        ```

    ??? variable string "`teslamate_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        teslamate_role_docker_cgroup_parent:
        ```

    ??? variable list "`teslamate_role_docker_commands`"

        ```yaml
        # Type: list
        teslamate_role_docker_commands:
        ```

    ??? variable int "`teslamate_role_docker_create_timeout`"

        ```yaml
        # Type: int
        teslamate_role_docker_create_timeout:
        ```

    ??? variable string "`teslamate_role_docker_entrypoint`"

        ```yaml
        # Type: string
        teslamate_role_docker_entrypoint:
        ```

    ??? variable string "`teslamate_role_docker_env_file`"

        ```yaml
        # Type: string
        teslamate_role_docker_env_file:
        ```

    ??? variable dict "`teslamate_role_docker_labels`"

        ```yaml
        # Type: dict
        teslamate_role_docker_labels:
        ```

    ??? variable bool "`teslamate_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_labels_use_common:
        ```

    ??? variable bool "`teslamate_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_read_only:
        ```

    ??? variable string "`teslamate_role_docker_runtime`"

        ```yaml
        # Type: string
        teslamate_role_docker_runtime:
        ```

    ??? variable list "`teslamate_role_docker_sysctls`"

        ```yaml
        # Type: list
        teslamate_role_docker_sysctls:
        ```

    ??? variable list "`teslamate_role_docker_ulimits`"

        ```yaml
        # Type: list
        teslamate_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`teslamate_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        teslamate_role_autoheal_enabled: true
        ```

    ??? variable string "`teslamate_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        teslamate_role_depends_on: ""
        ```

    ??? variable string "`teslamate_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        teslamate_role_depends_on_delay: "0"
        ```

    ??? variable string "`teslamate_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        teslamate_role_depends_on_healthchecks:
        ```

    ??? variable bool "`teslamate_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        teslamate_role_diun_enabled: true
        ```

    ??? variable bool "`teslamate_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        teslamate_role_dns_enabled: true
        ```

    ??? variable bool "`teslamate_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        teslamate_role_docker_controller: true
        ```

    ??? variable list "`teslamate_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        teslamate_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`teslamate_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_volumes_download:
        ```

    ??? variable string "`teslamate_role_themepark_addons`"

        ```yaml
        # Type: string
        teslamate_role_themepark_addons:
        ```

    ??? variable string "`teslamate_role_themepark_app`"

        ```yaml
        # Type: string
        teslamate_role_themepark_app:
        ```

    ??? variable string "`teslamate_role_themepark_theme`"

        ```yaml
        # Type: string
        teslamate_role_themepark_theme:
        ```

    ??? variable string "`teslamate_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        teslamate_role_traefik_api_middleware:
        ```

    ??? variable string "`teslamate_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        teslamate_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`teslamate_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`teslamate_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        teslamate_role_traefik_middleware_http:
        ```

    ??? variable bool "`teslamate_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`teslamate_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`teslamate_role_traefik_priority`"

        ```yaml
        # Type: string
        teslamate_role_traefik_priority:
        ```

    ??? variable bool "`teslamate_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`teslamate_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        teslamate_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        teslamate_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`teslamate_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        teslamate_role_web_api_http_port:
        ```

    ??? variable string "`teslamate_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        teslamate_role_web_api_http_scheme:
        ```

    ??? variable dict "`teslamate_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        teslamate_role_web_api_http_serverstransport:
        ```

    ??? variable string "`teslamate_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        teslamate_role_web_api_port:
        ```

    ??? variable string "`teslamate_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        teslamate_role_web_api_scheme:
        ```

    ??? variable dict "`teslamate_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        teslamate_role_web_api_serverstransport:
        ```

    ??? variable list "`teslamate_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        teslamate_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            teslamate_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "teslamate2.{{ user.domain }}"
              - "teslamate.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`teslamate_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        teslamate_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            teslamate_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'teslamate2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`teslamate_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        teslamate_role_web_http_port:
        ```

    ??? variable string "`teslamate_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        teslamate_role_web_http_scheme:
        ```

    ??? variable dict "`teslamate_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        teslamate_role_web_http_serverstransport:
        ```

    ??? variable string "`teslamate_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        teslamate_role_web_scheme:
        ```

    ??? variable dict "`teslamate_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        teslamate_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
