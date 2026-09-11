---
icon: material/docker
hide:
  - tags
tags:
  - container
  - dockhand
  - docker
  - oidc
saltbox_automation:
  inventory:
    hide_sections:
      - OIDC
  app_links:
    - name: Manual
      url: https://dockhand.pro/manual
      type: documentation
      purpose: manual
    - name: Versions
      url: https://hub.docker.com/r/fnsys/dockhand/tags
      type: docker
      purpose: release
    - name: Community
      url: https://discord.gg/rMxW9Y5cQw
      type: discord
      purpose: community
  project_description:
    name: Dockhand
    summary: a modern, efficient Docker management application providing real-time container management, Compose stack orchestration, and multi-environment support.
    link: https://dockhand.pro
    categories:
      - Admin Apps > Container Operation
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Dockhand

## Overview

[Dockhand](https://dockhand.pro) is a modern, efficient Docker management application providing real-time container management, Compose stack orchestration, and multi-environment support.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://dockhand.pro/manual){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Versions**](https://hub.docker.com/r/fnsys/dockhand/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/rMxW9Y5cQw){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-dockhand
```

```shell
sb install sandbox-dockhand-oidc # (1)!
```

1.  ### Enabling OIDC

    This optional tag deploys Dockhand and also primes it for OIDC authentication:

    - Creates a local admin user (required to enable authentication)
    - Registers an OIDC provider based on your selected SSO middleware provider or the `dockhand_role_oidc_provider` value.
    - Generates an Authelia OIDC client configuration snippet at `/tmp/dockhand_oidc_client.yml`

    ???+note

        It's unnecessary to run the `dockhand-oidc` tag more than once, unless you need a snippet generated again.

    #### Finishing the setup

    1.  **Authelia**: copy and paste the client block from the snippet into your Authelia configuration, adjusting the values to your preference, and restart the Authelia container.
        
        **Authentik** (or another OIDC provider): you can use the snippet as a reference to fill out its OIDC form.
    
    1.  Turn on authentication in the Dockhand UI.

    1.  Confirm success by logging out and in through OIDC

    #### Pre-deployment

    Next, you will likely want to disable local login and Traefik SSO with the following Inventory entries:

    ```yaml
    dockhand_role_disable_local_login: "true"
    dockhand_role_traefik_sso_middleware: ""
    ```

    Redeploy with the regular tag to apply.

## Usage

Visit <https://dockhand.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        dockhand_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `dockhand_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `dockhand_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`dockhand_name`"

        ```yaml
        # Type: string
        dockhand_name: dockhand
        ```

=== "Settings"

    ??? variable bool "`dockhand_role_postgres_deploy`"

        ```yaml
        # Enable PostgreSQL (false = SQLite)
        # Type: bool (true/false)
        dockhand_role_postgres_deploy: true
        ```

    ??? variable string "`dockhand_role_database_url`"

        ```yaml
        # Type: string
        dockhand_role_database_url: ""
        ```

    ??? variable string "`dockhand_role_skip_df_collection`"

        ```yaml
        # Disable disk usage collection
        # Valid values: "true", "false"
        # Type: string
        dockhand_role_skip_df_collection: ""
        ```

    ??? variable string "`dockhand_role_disable_local_login`"

        ```yaml
        # Hide local username/password login form
        # Valid values: "true", "false"
        # Type: string
        dockhand_role_disable_local_login: ""
        ```

    ??? variable string "`dockhand_role_disable_whats_new`"

        ```yaml
        # Suppress post-upgrade "What's New" popup
        # Valid values: "true", "false"
        # Type: string
        dockhand_role_disable_whats_new: ""
        ```

    ??? variable string "`dockhand_role_dns_result_order`"

        ```yaml
        # Outbound DNS family preference
        # Valid values: "ipv4first", "verbatim", "ipv6first"
        # Type: string
        dockhand_role_dns_result_order: ""
        ```

    ??? variable string "`dockhand_role_export_metrics`"

        ```yaml
        # Expose Prometheus metrics at /metrics
        # Valid values: "true", "false"
        # Type: string
        dockhand_role_export_metrics: ""
        ```

    ??? variable string "`dockhand_role_trust_forwarded_headers`"

        ```yaml
        # Trust `X-Forwarded-For` / `X-Real-IP` for the client IP
        # Valid values: "true", "false"
        # Type: string
        dockhand_role_trust_forwarded_headers: "true"
        ```

    ??? variable string "`dockhand_role_disable_metrics`"

        ```yaml
        # Skip CPU/memory metrics collection entirely
        # Valid values: "true", "false"
        # Type: string
        dockhand_role_disable_metrics: ""
        ```

    ??? variable string "`dockhand_role_disable_events`"

        ```yaml
        # Skip container-event collection (start/stop/health/OOM)
        # Valid values: "true", "false"
        # Type: string
        dockhand_role_disable_events: ""
        ```

    ??? variable bool "`dockhand_role_insight_enable`"

        ```yaml
        # Enable Docker socket INFO and SYSTEM access
        # Type: bool (true/false)
        dockhand_role_insight_enable: true
        ```

    ??? variable bool "`dockhand_role_cycle_enable`"

        ```yaml
        # Enable Docker socket container lifecycle access
        # Type: bool (true/false)
        dockhand_role_cycle_enable: true
        ```

    ??? variable bool "`dockhand_role_logs_enable`"

        ```yaml
        # Enable Docker socket ALLOW_LOGS
        # Type: bool (true/false)
        dockhand_role_logs_enable: true
        ```

    ??? variable bool "`dockhand_role_exec_enable`"

        ```yaml
        # Enable Docker socket EXEC access
        # Type: bool (true/false)
        dockhand_role_exec_enable: false
        ```

    ??? variable bool "`dockhand_role_archive_enable`"

        ```yaml
        # Enable Docker socket ALLOW_ARCHIVE
        # Type: bool (true/false)
        dockhand_role_archive_enable: false
        ```

    ??? variable string "`dockhand_role_oidc_provider`"

        ```yaml
        # OIDC provider name
        # If empty will fall back to your default SSO middleware provider
        # Type: string
        dockhand_role_oidc_provider: ""
        ```

=== "Postgres"

    ??? variable string "`dockhand_role_postgres_name`"

        ```yaml
        # Type: string
        dockhand_role_postgres_name: "{{ dockhand_name }}-postgres"
        ```

    ??? variable string "`dockhand_role_postgres_user`"

        ```yaml
        # If empty it will fall back to postgres role default
        # Type: string
        dockhand_role_postgres_user: ""
        ```

    ??? variable string "`dockhand_role_postgres_password`"

        ```yaml
        # If empty it will fall back to postgres role default
        # Type: string
        dockhand_role_postgres_password: ""
        ```

    ??? variable string "`dockhand_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        dockhand_role_postgres_docker_env_db: "{{ dockhand_name }}"
        ```

    ??? variable string "`dockhand_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        dockhand_role_postgres_docker_image_tag: "16-alpine"
        ```

    ??? variable string "`dockhand_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        dockhand_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable string "`dockhand_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        dockhand_role_postgres_paths_folder: "{{ dockhand_name }}"
        ```

    ??? variable string "`dockhand_role_postgres_paths_location`"

        ```yaml
        # Type: string
        dockhand_role_postgres_paths_location: "{{ server_appdata_path }}/{{ dockhand_role_postgres_paths_folder }}/postgres"
        ```

    ??? variable dict "`dockhand_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        dockhand_role_postgres_docker_healthcheck:
          test:
            - "CMD"
            - "pg_isready"
            - "-d"
            - "{{ lookup('role_var', '_postgres_docker_env_db', role='dockhand') }}"
            - "-U"
            - "{{ lookup('role_var', '_postgres_user', role='dockhand', default=lookup('role_var', '_docker_env_user', role='postgres'), default_if_empty=true) }}"
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable dict "`dockhand_role_postgres_labels_default`"

        ```yaml
        # Type: dict
        dockhand_role_postgres_labels_default:
          dockhand.update: "false"
          dockhand.notify: "false"
        ```

    ??? variable dict "`dockhand_role_postgres_labels_custom`"

        ```yaml
        # Type: dict
        dockhand_role_postgres_labels_custom: {}
        ```

=== "Docker Socket Proxy"

    ??? variable string "`dockhand_role_docker_socket_proxy_name`"

        ```yaml
        # Type: string
        dockhand_role_docker_socket_proxy_name: "{{ dockhand_name }}-docker-socket-proxy"
        ```

    ??? variable dict "`dockhand_role_docker_socket_proxy_envs_default`"

        ```yaml
        # Type: dict
        dockhand_role_docker_socket_proxy_envs_default:
          CONTAINERS: "1"
          IMAGES: "1"
          NETWORKS: "1"
          VOLUMES: "1"
          EVENTS: "1"
          POST: "1"
          DELETE: "1"
          INFO: "{{ '1'
                 if lookup('role_var', '_insight_enable', role='dockhand')
                 else omit }}"
          SYSTEM: "{{ '1'
                   if lookup('role_var', '_insight_enable', role='dockhand')
                   else omit }}"
          ALLOW_START: "{{ '1'
                        if lookup('role_var', '_cycle_enable', role='dockhand')
                        else omit }}"
          ALLOW_STOP: "{{ '1'
                       if lookup('role_var', '_cycle_enable', role='dockhand')
                       else omit }}"
          ALLOW_RESTARTS: "{{ '1'
                           if lookup('role_var', '_cycle_enable', role='dockhand')
                           else omit }}"
          ALLOW_LOGS: "{{ '1'
                       if lookup('role_var', '_logs_enable', role='dockhand')
                       else omit }}"
          EXEC: "{{ '1'
                 if lookup('role_var', '_exec_enable', role='dockhand')
                 else omit }}"
          ALLOW_ARCHIVE: "{{ '1'
                          if lookup('role_var', '_archive_enable', role='dockhand')
                          else omit }}"
        ```

    ??? variable dict "`dockhand_role_docker_socket_proxy_envs_custom`"

        ```yaml
        # Type: dict
        dockhand_role_docker_socket_proxy_envs_custom: {}
        ```

    ??? variable dict "`dockhand_role_docker_socket_proxy_labels_default`"

        ```yaml
        # Type: dict
        dockhand_role_docker_socket_proxy_labels_default:
          dockhand.update: "false"
          dockhand.notify: "false"
        ```

    ??? variable dict "`dockhand_role_docker_socket_proxy_labels_custom`"

        ```yaml
        # Type: dict
        dockhand_role_docker_socket_proxy_labels_custom: {}
        ```

=== "Web"

    ??? variable string "`dockhand_role_web_subdomain`"

        ```yaml
        # Type: string
        dockhand_role_web_subdomain: "{{ dockhand_name }}"
        ```

    ??? variable string "`dockhand_role_web_domain`"

        ```yaml
        # Type: string
        dockhand_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`dockhand_role_web_port`"

        ```yaml
        # Type: string
        dockhand_role_web_port: "3000"
        ```

    ??? variable string "`dockhand_role_web_url`"

        ```yaml
        # Type: string
        dockhand_role_web_url: "{{ lookup('role_web', role='dockhand', scheme='https') }}"
        ```

    ??? variable string "`dockhand_role_web_host`"

        ```yaml
        # Type: string
        dockhand_role_web_host: "{{ lookup('role_web', role='dockhand') }}"
        ```

=== "DNS"

    ??? variable string "`dockhand_role_dns_record`"

        ```yaml
        # Type: string
        dockhand_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dockhand') }}"
        ```

    ??? variable string "`dockhand_role_dns_zone`"

        ```yaml
        # Type: string
        dockhand_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dockhand') }}"
        ```

    ??? variable bool "`dockhand_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`dockhand_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        dockhand_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`dockhand_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        dockhand_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`dockhand_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        dockhand_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`dockhand_role_traefik_middleware_default_api`"

        ```yaml
        # Type: string
        dockhand_role_traefik_middleware_default_api: "{{ traefik_default_middleware_api }}"
        ```

    ??? variable string "`dockhand_role_traefik_middleware_custom_api`"

        ```yaml
        # Type: string
        dockhand_role_traefik_middleware_custom_api: ""
        ```

    ??? variable string "`dockhand_role_traefik_certresolver`"

        ```yaml
        # Type: string
        dockhand_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`dockhand_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_traefik_enabled: true
        ```

    ??? variable bool "`dockhand_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_traefik_api_enabled: true
        ```

    ??? variable string "`dockhand_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        dockhand_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Setup"

    ??? variable string "`dockhand_role_host`"

        ```yaml
        # Type: string
        dockhand_role_host: "http://{{ lookup('role_var', '_docker_networks_alias', role='dockhand') }}:{{ lookup('role_var', '_web_port', role='dockhand') }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`dockhand_role_docker_container`"

        ```yaml
        # Type: string
        dockhand_role_docker_container: "{{ dockhand_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`dockhand_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_image_pull: true
        ```

    ??? variable string "`dockhand_role_docker_image_repo`"

        ```yaml
        # Type: string
        dockhand_role_docker_image_repo: "fnsys/dockhand"
        ```

    ??? variable string "`dockhand_role_docker_image_tag`"

        ```yaml
        # Type: string
        dockhand_role_docker_image_tag: "latest"
        ```

    ??? variable string "`dockhand_role_docker_image`"

        ```yaml
        # Type: string
        dockhand_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dockhand') }}:{{ lookup('role_var', '_docker_image_tag', role='dockhand') }}"
        ```

    <h5>Envs</h5>

    ??? variable string "`dockhand_role_docker_envs_database_url`"

        ```yaml
        # Type: string
        dockhand_role_docker_envs_database_url: "{{ lookup('role_var',
                                                           '_database_url',
                                                           role='dockhand',
                                                           default=lookup('role_var', '_postgres_database_url', role='dockhand'),
                                                           default_if_empty=true) }}"
        ```

    ??? variable string "`dockhand_role_docker_envs_dns_result_order`"

        ```yaml
        # Type: string
        dockhand_role_docker_envs_dns_result_order: "{{ 'verbatim'
                                                     if (dns_ipv4_enabled and dns_ipv6_enabled)
                                                     else 'ipv6first'
                                                          if dns_ipv6_enabled
                                                          else '' }}"
        ```

    ??? variable dict "`dockhand_role_docker_envs_default`"

        ```yaml
        # Type: dict
        dockhand_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          DATABASE_URL: "{{ lookup('role_var', '_docker_envs_database_url', role='dockhand')
                         if lookup('role_var', '_postgres_deploy', role='dockhand')
                         else omit }}"
          SKIP_DF_COLLECTION: "{{ lookup('role_var', '_skip_df_collection', role='dockhand', default=omit, default_if_empty=true) }}"
          DISABLE_LOCAL_LOGIN: "{{ lookup('role_var', '_disable_local_login', role='dockhand', default=omit, default_if_empty=true) }}"
          DISABLE_WHATS_NEW: "{{ lookup('role_var', '_disable_whats_new', role='dockhand', default=omit, default_if_empty=true) }}"
          DNS_RESULT_ORDER: "{{ lookup('role_var',
                                       '_dns_result_order',
                                       role='dockhand',
                                       default=lookup('role_var', '_docker_envs_dns_result_order', role='dockhand'),
                                       default_if_empty=true) }}"
          EXPORT_METRICS: "{{ lookup('role_var', '_export_metrics', role='dockhand', default=omit, default_if_empty=true) }}"
          TRUST_FORWARDED_HEADERS: "{{ lookup('role_var', '_trust_forwarded_headers', role='dockhand', default=omit, default_if_empty=true) }}"
          DISABLE_METRICS: "{{ lookup('role_var', '_disable_metrics', role='dockhand', default=omit, default_if_empty=true) }}"
          DISABLE_EVENTS: "{{ lookup('role_var', '_disable_events', role='dockhand', default=omit, default_if_empty=true) }}"
        ```

    ??? variable dict "`dockhand_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        dockhand_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`dockhand_role_docker_volumes_default`"

        ```yaml
        # Type: list
        dockhand_role_docker_volumes_default:
          - "{{ dockhand_role_paths_location }}:/app/data"
        ```

    ??? variable list "`dockhand_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        dockhand_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`dockhand_role_docker_hostname`"

        ```yaml
        # Type: string
        dockhand_role_docker_hostname: "{{ dockhand_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`dockhand_role_docker_networks_alias`"

        ```yaml
        # Type: string
        dockhand_role_docker_networks_alias: "{{ dockhand_name }}"
        ```

    ??? variable list "`dockhand_role_docker_networks_default`"

        ```yaml
        # Type: list
        dockhand_role_docker_networks_default: []
        ```

    ??? variable list "`dockhand_role_docker_networks_custom`"

        ```yaml
        # Type: list
        dockhand_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`dockhand_role_docker_restart_policy`"

        ```yaml
        # Type: string
        dockhand_role_docker_restart_policy: unless-stopped
        ```

    <h5>Dependencies</h5>

    ??? variable string "`dockhand_role_depends_on`"

        ```yaml
        # Type: string
        dockhand_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='dockhand')
                                   if lookup('role_var', '_postgres_deploy', role='dockhand')
                                   else lookup('role_var', '_docker_socket_proxy_name', role='dockhand') }}"
        ```

    ??? variable string "`dockhand_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        dockhand_role_depends_on_delay: "0"
        ```

    ??? variable string "`dockhand_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        dockhand_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    A blank value is YAML null and inherits any lower-precedence role or shared default. Explicit Ansible omit is accepted only for optional Docker settings; default-backed and required settings reject it. Use the documented typed empty value, such as `""`, `[]`, or `{}`, when disabling a guaranteed setting.

    <h5>GPU</h5>

    ??? variable bool "`dockhand_role_docker_gpu_enabled`"

        ```yaml
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        dockhand_role_docker_gpu_enabled: false
        ```

    ??? variable bool "`dockhand_role_docker_nvidia_disabled`"

        ```yaml
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        dockhand_role_docker_nvidia_disabled: false
        ```

    ??? variable bool "`dockhand_role_docker_dev_dri_disabled`"

        ```yaml
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        dockhand_role_docker_dev_dri_disabled: false
        ```

    <h5>Resource Limits</h5>

    ??? variable int "`dockhand_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        dockhand_role_docker_blkio_weight:
        ```

    ??? variable int "`dockhand_role_docker_cpu_period`"

        ```yaml
        # Type: int
        dockhand_role_docker_cpu_period:
        ```

    ??? variable int "`dockhand_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        dockhand_role_docker_cpu_quota:
        ```

    ??? variable int "`dockhand_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        dockhand_role_docker_cpu_shares:
        ```

    ??? variable string "`dockhand_role_docker_cpus`"

        ```yaml
        # CPU allocation accepted as a numeric string, such as 1.5
        # Type: string (quoted number)
        dockhand_role_docker_cpus:
        ```

    ??? variable string "`dockhand_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        dockhand_role_docker_cpuset_cpus:
        ```

    ??? variable string "`dockhand_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        dockhand_role_docker_cpuset_mems:
        ```

    ??? variable string "`dockhand_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        dockhand_role_docker_kernel_memory:
        ```

    ??? variable string "`dockhand_role_docker_memory`"

        ```yaml
        # Type: string
        dockhand_role_docker_memory:
        ```

    ??? variable string "`dockhand_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        dockhand_role_docker_memory_reservation:
        ```

    ??? variable string "`dockhand_role_docker_memory_swap`"

        ```yaml
        # Type: string
        dockhand_role_docker_memory_swap:
        ```

    ??? variable int "`dockhand_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        dockhand_role_docker_memory_swappiness:
        ```

    ??? variable string "`dockhand_role_docker_shm_size`"

        ```yaml
        # Type: string
        dockhand_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`dockhand_role_docker_cap_drop`"

        ```yaml
        # Type: list
        dockhand_role_docker_cap_drop:
        ```

    ??? variable string "`dockhand_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        dockhand_role_docker_cgroupns_mode:
        ```

    ??? variable list "`dockhand_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        dockhand_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`dockhand_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        dockhand_role_docker_device_read_bps:
        ```

    ??? variable list "`dockhand_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        dockhand_role_docker_device_read_iops:
        ```

    ??? variable list "`dockhand_role_docker_device_requests`"

        ```yaml
        # Type: list
        dockhand_role_docker_device_requests:
        ```

    ??? variable list "`dockhand_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        dockhand_role_docker_device_write_bps:
        ```

    ??? variable list "`dockhand_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        dockhand_role_docker_device_write_iops:
        ```

    ??? variable list "`dockhand_role_docker_devices`"

        ```yaml
        # Type: list
        dockhand_role_docker_devices:
        ```

    ??? variable list "`dockhand_role_docker_groups`"

        ```yaml
        # Type: list
        dockhand_role_docker_groups:
        ```

    ??? variable bool "`dockhand_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_privileged:
        ```

    ??? variable list "`dockhand_role_docker_security_opts`"

        ```yaml
        # Type: list
        dockhand_role_docker_security_opts:
        ```

    ??? variable string "`dockhand_role_docker_user`"

        ```yaml
        # Type: string
        dockhand_role_docker_user:
        ```

    ??? variable string "`dockhand_role_docker_userns_mode`"

        ```yaml
        # Type: string
        dockhand_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`dockhand_role_docker_dns_opts`"

        ```yaml
        # Type: list
        dockhand_role_docker_dns_opts:
        ```

    ??? variable list "`dockhand_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        dockhand_role_docker_dns_search_domains:
        ```

    ??? variable list "`dockhand_role_docker_dns_servers`"

        ```yaml
        # Type: list
        dockhand_role_docker_dns_servers:
        ```

    ??? variable string "`dockhand_role_docker_domainname`"

        ```yaml
        # Type: string
        dockhand_role_docker_domainname:
        ```

    ??? variable list "`dockhand_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        dockhand_role_docker_exposed_ports:
        ```

    ??? variable dict "`dockhand_role_docker_hosts`"

        ```yaml
        # Type: dict
        dockhand_role_docker_hosts:
        ```

    ??? variable bool "`dockhand_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_hosts_use_common:
        ```

    ??? variable string "`dockhand_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        dockhand_role_docker_ipc_mode:
        ```

    ??? variable list "`dockhand_role_docker_links`"

        ```yaml
        # Type: list
        dockhand_role_docker_links:
        ```

    ??? variable string "`dockhand_role_docker_network_mode`"

        ```yaml
        # Type: string
        dockhand_role_docker_network_mode:
        ```

    ??? variable string "`dockhand_role_docker_pid_mode`"

        ```yaml
        # Type: string
        dockhand_role_docker_pid_mode:
        ```

    ??? variable list "`dockhand_role_docker_ports`"

        ```yaml
        # Type: list
        dockhand_role_docker_ports:
        ```

    ??? variable string "`dockhand_role_docker_uts`"

        ```yaml
        # Type: string
        dockhand_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`dockhand_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_keep_volumes:
        ```

    ??? variable list "`dockhand_role_docker_mounts`"

        ```yaml
        # Type: list
        dockhand_role_docker_mounts:
        ```

    ??? variable dict "`dockhand_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        dockhand_role_docker_storage_opts:
        ```

    ??? variable list "`dockhand_role_docker_tmpfs`"

        ```yaml
        # Type: list
        dockhand_role_docker_tmpfs:
        ```

    ??? variable string "`dockhand_role_docker_volume_driver`"

        ```yaml
        # Type: string
        dockhand_role_docker_volume_driver:
        ```

    ??? variable list "`dockhand_role_docker_volumes_from`"

        ```yaml
        # Type: list
        dockhand_role_docker_volumes_from:
        ```

    ??? variable bool "`dockhand_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_volumes_global:
        ```

    ??? variable string "`dockhand_role_docker_working_dir`"

        ```yaml
        # Type: string
        dockhand_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`dockhand_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_auto_remove:
        ```

    ??? variable bool "`dockhand_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_cleanup:
        ```

    ??? variable bool "`dockhand_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_force_kill:
        ```

    ??? variable dict "`dockhand_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        dockhand_role_docker_healthcheck:
        ```

    ??? variable int "`dockhand_role_docker_healthy_wait_timeout`"

        ```yaml
        # Healthy-state wait timeout in seconds
        # Type: int
        dockhand_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`dockhand_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_init:
        ```

    ??? variable string "`dockhand_role_docker_kill_signal`"

        ```yaml
        # Type: string
        dockhand_role_docker_kill_signal:
        ```

    ??? variable string "`dockhand_role_docker_log_driver`"

        ```yaml
        # Type: string
        dockhand_role_docker_log_driver:
        ```

    ??? variable dict "`dockhand_role_docker_log_options`"

        ```yaml
        # Type: dict
        dockhand_role_docker_log_options:
        ```

    ??? variable bool "`dockhand_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_oom_killer:
        ```

    ??? variable int "`dockhand_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        dockhand_role_docker_oom_score_adj:
        ```

    ??? variable bool "`dockhand_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_output_logs:
        ```

    ??? variable bool "`dockhand_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_paused:
        ```

    ??? variable bool "`dockhand_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_recreate:
        ```

    ??? variable int "`dockhand_role_docker_restart_retries`"

        ```yaml
        # Type: int
        dockhand_role_docker_restart_retries:
        ```

    ??? variable string "`dockhand_role_docker_stop_signal`"

        ```yaml
        # Type: string
        dockhand_role_docker_stop_signal:
        ```

    ??? variable int "`dockhand_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        dockhand_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`dockhand_role_docker_capabilities`"

        ```yaml
        # Type: list
        dockhand_role_docker_capabilities:
        ```

    ??? variable string "`dockhand_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        dockhand_role_docker_cgroup_parent:
        ```

    ??? variable list "`dockhand_role_docker_commands`"

        ```yaml
        # Type: list
        dockhand_role_docker_commands:
        ```

    ??? variable int "`dockhand_role_docker_create_timeout`"

        ```yaml
        # Type: int
        dockhand_role_docker_create_timeout:
        ```

    ??? variable list "`dockhand_role_docker_entrypoint`"

        ```yaml
        # Type: list
        dockhand_role_docker_entrypoint:
        ```

    ??? variable string "`dockhand_role_docker_env_file`"

        ```yaml
        # Type: string
        dockhand_role_docker_env_file:
        ```

    ??? variable dict "`dockhand_role_docker_labels`"

        ```yaml
        # Type: dict
        dockhand_role_docker_labels:
        ```

    ??? variable bool "`dockhand_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_labels_use_common:
        ```

    ??? variable bool "`dockhand_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_read_only:
        ```

    ??? variable string "`dockhand_role_docker_runtime`"

        ```yaml
        # Type: string
        dockhand_role_docker_runtime:
        ```

    ??? variable dict "`dockhand_role_docker_sysctls`"

        ```yaml
        # Type: dict
        dockhand_role_docker_sysctls:
        ```

    ??? variable list "`dockhand_role_docker_ulimits`"

        ```yaml
        # Type: list
        dockhand_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`dockhand_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        dockhand_role_autoheal_enabled: true
        ```

    ??? variable bool "`dockhand_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        dockhand_role_diun_enabled: true
        ```

    ??? variable bool "`dockhand_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        dockhand_role_dns_enabled: true
        ```

    ??? variable bool "`dockhand_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        dockhand_role_docker_controller: true
        ```

    ??? variable list "`dockhand_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        dockhand_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`dockhand_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_docker_volumes_download:
        ```

    ??? variable list "`dockhand_role_paths_folders_list_custom`"

        ```yaml
        # Extra directories to create
        # Type: list
        dockhand_role_paths_folders_list_custom:
        ```

    ??? variable string "`dockhand_role_paths_group`"

        ```yaml
        # Group for directories created by the role
        # Type: string
        dockhand_role_paths_group:
        ```

    ??? variable string "`dockhand_role_paths_owner`"

        ```yaml
        # Owner for directories created by the role
        # Type: string
        dockhand_role_paths_owner:
        ```

    ??? variable string "`dockhand_role_paths_permissions`"

        ```yaml
        # Permissions for directories created by the role
        # Type: string
        dockhand_role_paths_permissions:
        ```

    ??? variable bool "`dockhand_role_paths_recursive`"

        ```yaml
        # Apply owner and group recursively without changing child modes
        # Type: bool (true/false)
        dockhand_role_paths_recursive:
        ```

    ??? variable list "`dockhand_role_themepark_addons`"

        ```yaml
        # ThemePark addon names to enable
        # Type: list
        dockhand_role_themepark_addons:
        ```

    ??? variable string "`dockhand_role_themepark_app`"

        ```yaml
        # Type: string
        dockhand_role_themepark_app:
        ```

    ??? variable string "`dockhand_role_themepark_theme`"

        ```yaml
        # Type: string
        dockhand_role_themepark_theme:
        ```

    ??? variable string "`dockhand_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        dockhand_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`dockhand_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        dockhand_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`dockhand_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        dockhand_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`dockhand_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        dockhand_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`dockhand_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        dockhand_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`dockhand_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        dockhand_role_traefik_middleware_http:
        ```

    ??? variable bool "`dockhand_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`dockhand_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        dockhand_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`dockhand_role_traefik_priority`"

        ```yaml
        # Type: string
        dockhand_role_traefik_priority:
        ```

    ??? variable bool "`dockhand_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        dockhand_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`dockhand_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        dockhand_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`dockhand_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        dockhand_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`dockhand_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        dockhand_role_web_api_http_port:
        ```

    ??? variable string "`dockhand_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        dockhand_role_web_api_http_scheme:
        ```

    ??? variable dict "`dockhand_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        dockhand_role_web_api_http_serverstransport:
        ```

    ??? variable string "`dockhand_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        dockhand_role_web_api_port:
        ```

    ??? variable string "`dockhand_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        dockhand_role_web_api_scheme:
        ```

    ??? variable dict "`dockhand_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        dockhand_role_web_api_serverstransport:
        ```

    ??? variable list "`dockhand_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        dockhand_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            dockhand_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "dockhand2.{{ user.domain }}"
              - "dockhand.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`dockhand_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        dockhand_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            dockhand_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dockhand2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`dockhand_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        dockhand_role_web_http_port:
        ```

    ??? variable string "`dockhand_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        dockhand_role_web_http_scheme:
        ```

    ??? variable dict "`dockhand_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        dockhand_role_web_http_serverstransport:
        ```

    ??? variable string "`dockhand_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        dockhand_role_web_scheme:
        ```

    ??? variable dict "`dockhand_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        dockhand_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
