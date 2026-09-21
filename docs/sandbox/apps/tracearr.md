---
icon: material/docker
hide:
  - tags
tags:
  - tracearr
  - monitoring
  - statistics
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.tracearr.com
      type: documentation
      purpose: manual
    - name: Releases
      url: https://github.com/connorgallopo/Tracearr/pkgs/container/tracearr
      type: github
      purpose: release
    - name: Community
      url: https://discord.gg/a7n3sFd2Yw
      type: discord
      purpose: community
  project_description:
    name: Tracearr
    summary: |-
      a monitoring platform for Plex, Jellyfin, and Emby that tracks active streams, playback history, and account sharing.
    link: https://tracearr.com
    categories:
      - Accessories > For Media Server > Monitoring
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Tracearr

## Overview

[Tracearr](https://tracearr.com) is a monitoring platform for Plex, Jellyfin, and Emby that tracks active streams, playback history, and account sharing.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.tracearr.com){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/connorgallopo/Tracearr/pkgs/container/tracearr){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/a7n3sFd2Yw){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Pre-deployment

For SSO through Authelia or Authentik, create an OIDC client with the redirect URI `https://tracearr.iYOUR_DOMAIN_NAMEi/api/v1/auth/oauth2/callback/oidc` and set `tracearr_role_oidc_issuer_url`, `tracearr_role_oidc_client_id` and `tracearr_role_oidc_client_secret`.

## Deployment

```shell
sb install sandbox-tracearr
```

```shell
sb install sandbox-tracearr-claim # (1)!
```

1. Prints the saved Tracearr claim code and its web URL so you can enter the code and complete Tracearr’s initial setup. Does not install Tracearr itself.

## Usage

Visit <https://tracearr.iYOUR_DOMAIN_NAMEi>.

The first account created becomes the owner. Add media servers by their container address, for example `http://plex:32400` or `http://jellyfin:8096`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        tracearr_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `tracearr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `tracearr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tracearr_name`"

        ```yaml
        # Type: string
        tracearr_name: tracearr
        ```

=== "Settings"

    ??? variable string "`tracearr_role_jwt_secret`"

        ```yaml
        # JWT signing secret. Defaults to a persisted generated value.
        # Keep it stable across reinstalls; overrides must be 64 hexadecimal characters.
        # Type: string
        tracearr_role_jwt_secret: "{{ tracearr_saltbox_facts.facts.jwt_secret }}"
        ```

    ??? variable string "`tracearr_role_cookie_secret`"

        ```yaml
        # Cookie signing secret. Defaults to a persisted generated value.
        # Keep it stable across reinstalls; overrides must be 64 hexadecimal characters.
        # Type: string
        tracearr_role_cookie_secret: "{{ tracearr_saltbox_facts.facts.cookie_secret }}"
        ```

    ??? variable string "`tracearr_role_claim_code`"

        ```yaml
        # Protects first-time setup. Defaults to a persisted generated claim code.
        # Retrieve it with the tracearr-claim tag; overrides must be non-empty strings.
        # Type: string
        tracearr_role_claim_code: "{{ tracearr_saltbox_facts.facts.claim_code }}"
        ```

    ??? variable string "`tracearr_role_log_level`"

        ```yaml
        # Logging verbosity
        # Valid values: "debug", "info", "warn", "error"
        # Type: string
        tracearr_role_log_level: ""
        ```

    ??? variable string "`tracearr_role_oidc_issuer_url`"

        ```yaml
        # Type: string
        tracearr_role_oidc_issuer_url: ""
        ```

    ??? variable string "`tracearr_role_oidc_client_id`"

        ```yaml
        # Type: string
        tracearr_role_oidc_client_id: ""
        ```

    ??? variable string "`tracearr_role_oidc_client_secret`"

        ```yaml
        # Type: string
        tracearr_role_oidc_client_secret: ""
        ```

    ??? variable string "`tracearr_role_oidc_provider_name`"

        ```yaml
        # Label for the SSO login button
        # Type: string
        tracearr_role_oidc_provider_name: ""
        ```

=== "Postgres"

    ??? variable bool "`tracearr_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_postgres_deploy: true
        ```

    ??? variable string "`tracearr_role_postgres_name`"

        ```yaml
        # Type: string
        tracearr_role_postgres_name: "{{ tracearr_name }}-postgres"
        ```

    ??? variable string "`tracearr_role_postgres_user`"

        ```yaml
        # If empty it will fall back to the timescaledb role default.
        # Type: string
        tracearr_role_postgres_user: ""
        ```

    ??? variable string "`tracearr_role_postgres_password`"

        ```yaml
        # If empty it will fall back to the timescaledb role default.
        # Type: string
        tracearr_role_postgres_password: ""
        ```

    ??? variable string "`tracearr_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        tracearr_role_postgres_docker_env_db: "{{ tracearr_name }}"
        ```

    ??? variable string "`tracearr_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        tracearr_role_postgres_docker_image_repo: "timescale/timescaledb-ha"
        ```

    ??? variable string "`tracearr_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        tracearr_role_postgres_docker_image_tag: "pg18.4-ts2.29.1"
        ```

    ??? variable list "`tracearr_role_postgres_docker_commands`"

        ```yaml
        # Type: list
        tracearr_role_postgres_docker_commands:
          - "postgres"
          - "-c"
          - "timescaledb.license=timescale"
          - "-c"
          - "timescaledb.telemetry_level=off"
          - "-c"
          - "max_locks_per_transaction=4096"
          - "-c"
          - "max_connections=150"
        ```

    ??? variable string "`tracearr_role_postgres_docker_shm_size`"

        ```yaml
        # Type: string
        tracearr_role_postgres_docker_shm_size: "512M"
        ```

    ??? variable list "`tracearr_role_postgres_docker_ulimits`"

        ```yaml
        # Type: list
        tracearr_role_postgres_docker_ulimits:
          - "nofile:65536:65536"
        ```

    ??? variable string "`tracearr_role_database_url`"

        ```yaml
        # Type: string
        tracearr_role_database_url: "postgres://{{ lookup('role_var', '_postgres_credentials_lookup', role='tracearr') }}@{{ lookup('role_var', '_postgres_name', role='tracearr') }}:5432/{{ lookup('role_var', '_postgres_docker_env_db', role='tracearr') }}"
        ```

    ??? variable dict "`tracearr_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        tracearr_role_postgres_docker_healthcheck:
          test:
            - "CMD"
            - "pg_isready"
            - "-d"
            - "{{ lookup('role_var', '_postgres_docker_env_db', role='tracearr') }}"
            - "-U"
            - "{{ lookup('role_var', '_postgres_user_lookup', role='tracearr') }}"
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`tracearr_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        tracearr_role_postgres_paths_folder: "{{ tracearr_name }}"
        ```

    ??? variable string "`tracearr_role_postgres_paths_location`"

        ```yaml
        # Type: string
        tracearr_role_postgres_paths_location: "{{ server_appdata_path }}/{{ tracearr_role_postgres_paths_folder }}/postgres"
        ```

=== "Redis"

    ??? variable string "`tracearr_role_redis_name`"

        ```yaml
        # Type: string
        tracearr_role_redis_name: "{{ tracearr_name }}-redis"
        ```

    ??? variable string "`tracearr_role_redis_docker_image_tag`"

        ```yaml
        # Type: string
        tracearr_role_redis_docker_image_tag: "8-alpine"
        ```

    ??? variable list "`tracearr_role_redis_docker_commands`"

        ```yaml
        # Type: list
        tracearr_role_redis_docker_commands:
          - "redis-server"
          - "--appendonly"
          - "yes"
        ```

    ??? variable string "`tracearr_role_redis_paths_folder`"

        ```yaml
        # Type: string
        tracearr_role_redis_paths_folder: "{{ tracearr_name }}"
        ```

    ??? variable string "`tracearr_role_redis_paths_location`"

        ```yaml
        # Type: string
        tracearr_role_redis_paths_location: "{{ server_appdata_path }}/{{ tracearr_role_redis_paths_folder }}/redis"
        ```

=== "Web"

    ??? variable string "`tracearr_role_web_subdomain`"

        ```yaml
        # Type: string
        tracearr_role_web_subdomain: "{{ tracearr_name }}"
        ```

    ??? variable string "`tracearr_role_web_domain`"

        ```yaml
        # Type: string
        tracearr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tracearr_role_web_port`"

        ```yaml
        # Type: string
        tracearr_role_web_port: "3000"
        ```

    ??? variable string "`tracearr_role_web_url`"

        ```yaml
        # Type: string
        tracearr_role_web_url: "{{ lookup('role_web', role='tracearr', scheme='https') }}"
        ```

=== "DNS"

    ??? variable string "`tracearr_role_dns_record`"

        ```yaml
        # Type: string
        tracearr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tracearr') }}"
        ```

    ??? variable string "`tracearr_role_dns_zone`"

        ```yaml
        # Type: string
        tracearr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tracearr') }}"
        ```

    ??? variable bool "`tracearr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tracearr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tracearr_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`tracearr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tracearr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tracearr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tracearr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tracearr_role_traefik_middleware_default_api`"

        ```yaml
        # Type: string
        tracearr_role_traefik_middleware_default_api: "{{ traefik_default_middleware_api }}"
        ```

    ??? variable string "`tracearr_role_traefik_middleware_custom_api`"

        ```yaml
        # Type: string
        tracearr_role_traefik_middleware_custom_api: ""
        ```

    ??? variable string "`tracearr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tracearr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tracearr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_traefik_enabled: true
        ```

    ??? variable bool "`tracearr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_traefik_api_enabled: false
        ```

    ??? variable string "`tracearr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tracearr_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`tracearr_role_docker_container`"

        ```yaml
        # Type: string
        tracearr_role_docker_container: "{{ tracearr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`tracearr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_image_pull: true
        ```

    ??? variable string "`tracearr_role_docker_image_repo`"

        ```yaml
        # Type: string
        tracearr_role_docker_image_repo: "ghcr.io/connorgallopo/tracearr"
        ```

    ??? variable string "`tracearr_role_docker_image_tag`"

        ```yaml
        # Type: string
        tracearr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`tracearr_role_docker_image`"

        ```yaml
        # Type: string
        tracearr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tracearr') }}:{{ lookup('role_var', '_docker_image_tag', role='tracearr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`tracearr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        tracearr_role_docker_envs_default:
          TZ: "{{ tz }}"
          DATABASE_URL: "{{ lookup('role_var', '_database_url', role='tracearr') }}"
          REDIS_URL: "redis://{{ lookup('role_var', '_redis_name', role='tracearr') }}:6379"
          JWT_SECRET: "{{ lookup('role_var', '_jwt_secret', role='tracearr') }}"
          COOKIE_SECRET: "{{ lookup('role_var', '_cookie_secret', role='tracearr') }}"
          CLAIM_CODE: "{{ lookup('role_var', '_claim_code', role='tracearr') }}"
          TRUST_PROXY: "true"
          BACKUP_DIR: "/data/backup"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='tracearr', default=omit, default_if_empty=true) }}"
          OIDC_ISSUER_URL: "{{ lookup('role_var', '_oidc_issuer_url', role='tracearr', default=omit, default_if_empty=true) }}"
          OIDC_CLIENT_ID: "{{ lookup('role_var', '_oidc_client_id', role='tracearr', default=omit, default_if_empty=true) }}"
          OIDC_CLIENT_SECRET: "{{ lookup('role_var', '_oidc_client_secret', role='tracearr', default=omit, default_if_empty=true) }}"
          OIDC_PROVIDER_NAME: "{{ lookup('role_var', '_oidc_provider_name', role='tracearr', default=omit, default_if_empty=true) }}"
        ```

    ??? variable dict "`tracearr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tracearr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`tracearr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        tracearr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='tracearr') }}/backup:/data/backup"
          - "{{ lookup('role_var', '_paths_location', role='tracearr') }}/image-cache:/app/data/image-cache"
        ```

    ??? variable list "`tracearr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tracearr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`tracearr_role_docker_hostname`"

        ```yaml
        # Type: string
        tracearr_role_docker_hostname: "{{ tracearr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`tracearr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tracearr_role_docker_networks_alias: "{{ tracearr_name }}"
        ```

    ??? variable list "`tracearr_role_docker_networks_default`"

        ```yaml
        # Type: list
        tracearr_role_docker_networks_default: []
        ```

    ??? variable list "`tracearr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tracearr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`tracearr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tracearr_role_docker_restart_policy: unless-stopped
        ```

    <h5>User</h5>

    ??? variable string "`tracearr_role_docker_user`"

        ```yaml
        # Type: string
        tracearr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`tracearr_role_depends_on`"

        ```yaml
        # Type: string
        tracearr_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='tracearr') }},{{ lookup('role_var', '_redis_name', role='tracearr') }}"
        ```

    ??? variable string "`tracearr_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        tracearr_role_depends_on_delay: "0"
        ```

    ??? variable string "`tracearr_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        tracearr_role_depends_on_healthchecks: "false"
        ```

    <h5>CI</h5>

    ??? variable int "`tracearr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        tracearr_role_docker_create_timeout: 300
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    A blank value is YAML null and inherits any lower-precedence role or shared default. Explicit Ansible omit is accepted only for optional Docker settings; default-backed and required settings reject it. Use the documented typed empty value, such as `""`, `[]`, or `{}`, when disabling a guaranteed setting.

    <h5>GPU</h5>

    ??? variable bool "`tracearr_role_docker_gpu_enabled`"

        ```yaml
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        tracearr_role_docker_gpu_enabled: false
        ```

    ??? variable bool "`tracearr_role_docker_nvidia_disabled`"

        ```yaml
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        tracearr_role_docker_nvidia_disabled: false
        ```

    ??? variable bool "`tracearr_role_docker_dev_dri_disabled`"

        ```yaml
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        tracearr_role_docker_dev_dri_disabled: false
        ```

    <h5>Resource Limits</h5>

    ??? variable int "`tracearr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        tracearr_role_docker_blkio_weight:
        ```

    ??? variable int "`tracearr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        tracearr_role_docker_cpu_period:
        ```

    ??? variable int "`tracearr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        tracearr_role_docker_cpu_quota:
        ```

    ??? variable int "`tracearr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        tracearr_role_docker_cpu_shares:
        ```

    ??? variable string "`tracearr_role_docker_cpus`"

        ```yaml
        # CPU allocation accepted as a numeric string, such as 1.5
        # Type: string (quoted number)
        tracearr_role_docker_cpus:
        ```

    ??? variable string "`tracearr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        tracearr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`tracearr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        tracearr_role_docker_cpuset_mems:
        ```

    ??? variable string "`tracearr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        tracearr_role_docker_kernel_memory:
        ```

    ??? variable string "`tracearr_role_docker_memory`"

        ```yaml
        # Type: string
        tracearr_role_docker_memory:
        ```

    ??? variable string "`tracearr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        tracearr_role_docker_memory_reservation:
        ```

    ??? variable string "`tracearr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        tracearr_role_docker_memory_swap:
        ```

    ??? variable int "`tracearr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        tracearr_role_docker_memory_swappiness:
        ```

    ??? variable string "`tracearr_role_docker_shm_size`"

        ```yaml
        # Type: string
        tracearr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`tracearr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        tracearr_role_docker_cap_drop:
        ```

    ??? variable string "`tracearr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        tracearr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`tracearr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        tracearr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`tracearr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        tracearr_role_docker_device_read_bps:
        ```

    ??? variable list "`tracearr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        tracearr_role_docker_device_read_iops:
        ```

    ??? variable list "`tracearr_role_docker_device_requests`"

        ```yaml
        # Type: list
        tracearr_role_docker_device_requests:
        ```

    ??? variable list "`tracearr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        tracearr_role_docker_device_write_bps:
        ```

    ??? variable list "`tracearr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        tracearr_role_docker_device_write_iops:
        ```

    ??? variable list "`tracearr_role_docker_devices`"

        ```yaml
        # Type: list
        tracearr_role_docker_devices:
        ```

    ??? variable list "`tracearr_role_docker_groups`"

        ```yaml
        # Type: list
        tracearr_role_docker_groups:
        ```

    ??? variable bool "`tracearr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_privileged:
        ```

    ??? variable list "`tracearr_role_docker_security_opts`"

        ```yaml
        # Type: list
        tracearr_role_docker_security_opts:
        ```

    ??? variable string "`tracearr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        tracearr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`tracearr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        tracearr_role_docker_dns_opts:
        ```

    ??? variable list "`tracearr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        tracearr_role_docker_dns_search_domains:
        ```

    ??? variable list "`tracearr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        tracearr_role_docker_dns_servers:
        ```

    ??? variable string "`tracearr_role_docker_domainname`"

        ```yaml
        # Type: string
        tracearr_role_docker_domainname:
        ```

    ??? variable list "`tracearr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        tracearr_role_docker_exposed_ports:
        ```

    ??? variable dict "`tracearr_role_docker_hosts`"

        ```yaml
        # Type: dict
        tracearr_role_docker_hosts:
        ```

    ??? variable bool "`tracearr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_hosts_use_common:
        ```

    ??? variable string "`tracearr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        tracearr_role_docker_ipc_mode:
        ```

    ??? variable list "`tracearr_role_docker_links`"

        ```yaml
        # Type: list
        tracearr_role_docker_links:
        ```

    ??? variable string "`tracearr_role_docker_network_mode`"

        ```yaml
        # Type: string
        tracearr_role_docker_network_mode:
        ```

    ??? variable string "`tracearr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        tracearr_role_docker_pid_mode:
        ```

    ??? variable list "`tracearr_role_docker_ports`"

        ```yaml
        # Type: list
        tracearr_role_docker_ports:
        ```

    ??? variable string "`tracearr_role_docker_uts`"

        ```yaml
        # Type: string
        tracearr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`tracearr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_keep_volumes:
        ```

    ??? variable list "`tracearr_role_docker_mounts`"

        ```yaml
        # Type: list
        tracearr_role_docker_mounts:
        ```

    ??? variable dict "`tracearr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        tracearr_role_docker_storage_opts:
        ```

    ??? variable list "`tracearr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        tracearr_role_docker_tmpfs:
        ```

    ??? variable string "`tracearr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        tracearr_role_docker_volume_driver:
        ```

    ??? variable list "`tracearr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        tracearr_role_docker_volumes_from:
        ```

    ??? variable bool "`tracearr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_volumes_global:
        ```

    ??? variable string "`tracearr_role_docker_working_dir`"

        ```yaml
        # Type: string
        tracearr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`tracearr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_auto_remove:
        ```

    ??? variable bool "`tracearr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_cleanup:
        ```

    ??? variable bool "`tracearr_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_force_kill:
        ```

    ??? variable dict "`tracearr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        tracearr_role_docker_healthcheck:
        ```

    ??? variable int "`tracearr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Healthy-state wait timeout in seconds
        # Type: int
        tracearr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`tracearr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_init:
        ```

    ??? variable string "`tracearr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        tracearr_role_docker_kill_signal:
        ```

    ??? variable string "`tracearr_role_docker_log_driver`"

        ```yaml
        # Type: string
        tracearr_role_docker_log_driver:
        ```

    ??? variable dict "`tracearr_role_docker_log_options`"

        ```yaml
        # Type: dict
        tracearr_role_docker_log_options:
        ```

    ??? variable bool "`tracearr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_oom_killer:
        ```

    ??? variable int "`tracearr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        tracearr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`tracearr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_output_logs:
        ```

    ??? variable bool "`tracearr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_paused:
        ```

    ??? variable bool "`tracearr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_recreate:
        ```

    ??? variable int "`tracearr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        tracearr_role_docker_restart_retries:
        ```

    ??? variable string "`tracearr_role_docker_stop_signal`"

        ```yaml
        # Type: string
        tracearr_role_docker_stop_signal:
        ```

    ??? variable int "`tracearr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        tracearr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`tracearr_role_docker_capabilities`"

        ```yaml
        # Type: list
        tracearr_role_docker_capabilities:
        ```

    ??? variable string "`tracearr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        tracearr_role_docker_cgroup_parent:
        ```

    ??? variable list "`tracearr_role_docker_commands`"

        ```yaml
        # Type: list
        tracearr_role_docker_commands:
        ```

    ??? variable list "`tracearr_role_docker_entrypoint`"

        ```yaml
        # Type: list
        tracearr_role_docker_entrypoint:
        ```

    ??? variable string "`tracearr_role_docker_env_file`"

        ```yaml
        # Type: string
        tracearr_role_docker_env_file:
        ```

    ??? variable dict "`tracearr_role_docker_labels`"

        ```yaml
        # Type: dict
        tracearr_role_docker_labels:
        ```

    ??? variable bool "`tracearr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_labels_use_common:
        ```

    ??? variable bool "`tracearr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_read_only:
        ```

    ??? variable string "`tracearr_role_docker_runtime`"

        ```yaml
        # Type: string
        tracearr_role_docker_runtime:
        ```

    ??? variable dict "`tracearr_role_docker_sysctls`"

        ```yaml
        # Type: dict
        tracearr_role_docker_sysctls:
        ```

    ??? variable list "`tracearr_role_docker_ulimits`"

        ```yaml
        # Type: list
        tracearr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`tracearr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tracearr_role_autoheal_enabled: true
        ```

    ??? variable bool "`tracearr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tracearr_role_diun_enabled: true
        ```

    ??? variable bool "`tracearr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tracearr_role_dns_enabled: true
        ```

    ??? variable bool "`tracearr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tracearr_role_docker_controller: true
        ```

    ??? variable list "`tracearr_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        tracearr_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`tracearr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_docker_volumes_download:
        ```

    ??? variable list "`tracearr_role_paths_folders_list_custom`"

        ```yaml
        # Extra directories to create
        # Type: list
        tracearr_role_paths_folders_list_custom:
        ```

    ??? variable string "`tracearr_role_paths_group`"

        ```yaml
        # Group for directories created by the role
        # Type: string
        tracearr_role_paths_group:
        ```

    ??? variable string "`tracearr_role_paths_owner`"

        ```yaml
        # Owner for directories created by the role
        # Type: string
        tracearr_role_paths_owner:
        ```

    ??? variable string "`tracearr_role_paths_permissions`"

        ```yaml
        # Permissions for directories created by the role
        # Type: string
        tracearr_role_paths_permissions:
        ```

    ??? variable bool "`tracearr_role_paths_recursive`"

        ```yaml
        # Apply owner and group recursively without changing child modes
        # Type: bool (true/false)
        tracearr_role_paths_recursive:
        ```

    ??? variable list "`tracearr_role_themepark_addons`"

        ```yaml
        # ThemePark addon names to enable
        # Type: list
        tracearr_role_themepark_addons:
        ```

    ??? variable string "`tracearr_role_themepark_app`"

        ```yaml
        # Type: string
        tracearr_role_themepark_app:
        ```

    ??? variable string "`tracearr_role_themepark_theme`"

        ```yaml
        # Type: string
        tracearr_role_themepark_theme:
        ```

    ??? variable string "`tracearr_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        tracearr_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`tracearr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tracearr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`tracearr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tracearr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tracearr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tracearr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tracearr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tracearr_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`tracearr_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        tracearr_role_traefik_middleware_http:
        ```

    ??? variable bool "`tracearr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tracearr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tracearr_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`tracearr_role_traefik_priority`"

        ```yaml
        # Type: string
        tracearr_role_traefik_priority:
        ```

    ??? variable bool "`tracearr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tracearr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tracearr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tracearr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tracearr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tracearr_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`tracearr_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        tracearr_role_web_api_http_port:
        ```

    ??? variable string "`tracearr_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        tracearr_role_web_api_http_scheme:
        ```

    ??? variable dict "`tracearr_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        tracearr_role_web_api_http_serverstransport:
        ```

    ??? variable string "`tracearr_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        tracearr_role_web_api_port:
        ```

    ??? variable string "`tracearr_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        tracearr_role_web_api_scheme:
        ```

    ??? variable dict "`tracearr_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        tracearr_role_web_api_serverstransport:
        ```

    ??? variable list "`tracearr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tracearr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            tracearr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tracearr2.{{ user.domain }}"
              - "tracearr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`tracearr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tracearr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            tracearr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tracearr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`tracearr_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        tracearr_role_web_http_port:
        ```

    ??? variable string "`tracearr_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        tracearr_role_web_http_scheme:
        ```

    ??? variable dict "`tracearr_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        tracearr_role_web_http_serverstransport:
        ```

    ??? variable string "`tracearr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tracearr_role_web_scheme:
        ```

    ??? variable dict "`tracearr_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        tracearr_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
