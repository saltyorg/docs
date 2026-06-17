---
icon: material/docker
status: draft2
hide:
  - tags
tags:
  - koito
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url:
      type: github
    - name: Community
      url:
      type: community
  project_description:
    name:
    summary:
    link:
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# 

## Overview

 is 

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-koito
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        koito_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `koito_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `koito_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`koito_name`"

        ```yaml
        # Type: string
        koito_name: koito
        ```

=== "Settings"

    ??? variable bool "`koito_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        koito_role_postgres_deploy: true
        ```

    ??? variable string "`koito_role_postgres_name`"

        ```yaml
        # Type: string
        koito_role_postgres_name: "{{ koito_name }}-postgres"
        ```

    ??? variable string "`koito_role_postgres_user`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        koito_role_postgres_user: ""
        ```

    ??? variable string "`koito_role_postgres_password`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        koito_role_postgres_password: ""
        ```

    ??? variable string "`koito_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        koito_role_postgres_docker_env_db: "koitodb"
        ```

    ??? variable string "`koito_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        koito_role_postgres_docker_image_tag: "16"
        ```

    ??? variable string "`koito_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        koito_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`koito_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        koito_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='koito') }} -U {{ lookup('role_var', '_postgres_user', role='koito') if (lookup('role_var', '_postgres_user', role='koito') | length > 0) else lookup('role_var', '_docker_env_user', role='postgres') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`koito_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        koito_role_postgres_paths_folder: "{{ koito_name }}"
        ```

    ??? variable string "`koito_role_postgres_paths_location`"

        ```yaml
        # Type: string
        koito_role_postgres_paths_location: "{{ server_appdata_path }}/{{ koito_role_postgres_paths_folder }}/postgres"
        ```

    ??? variable string "`koito_role_default_username`"

        ```yaml
        # Type: string
        koito_role_default_username: "{{ user.name }}"
        ```

    ??? variable string "`koito_role_default_password`"

        ```yaml
        # Type: string
        koito_role_default_password: "{{ user.pass }}"
        ```

    ??? variable string "`koito_role_database_url`"

        ```yaml
        # Type: string
        koito_role_database_url: ""
        ```

    ??? variable string "`koito_role_default_theme`"

        ```yaml
        # Type: string
        koito_role_default_theme: "yuu"
        ```

    ??? variable string "`koito_role_login_gate`"

        ```yaml
        # Type: string
        koito_role_login_gate: "false"
        ```

    ??? variable string "`koito_role_bind_addr`"

        ```yaml
        # Type: string
        koito_role_bind_addr: ""
        ```

    ??? variable string "`koito_role_enable_structured_logging`"

        ```yaml
        # Type: string
        koito_role_enable_structured_logging: "false"
        ```

    ??? variable string "`koito_role_enable_full_image_cache`"

        ```yaml
        # Type: string
        koito_role_enable_full_image_cache: "false"
        ```

    ??? variable string "`koito_role_log_level`"

        ```yaml
        # Type: string
        koito_role_log_level: "info"
        ```

    ??? variable string "`koito_role_musicbrainz_url`"

        ```yaml
        # Type: string
        koito_role_musicbrainz_url: "https://musicbrainz.org"
        ```

    ??? variable string "`koito_role_musicbrainz_rate_limit`"

        ```yaml
        # Type: string
        koito_role_musicbrainz_rate_limit: "1"
        ```

    ??? variable string "`koito_role_enable_lbz_relay`"

        ```yaml
        # Type: string
        koito_role_enable_lbz_relay: "false"
        ```

    ??? variable string "`koito_role_lbz_relay_url`"

        ```yaml
        # Type: string
        koito_role_lbz_relay_url: ""
        ```

    ??? variable string "`koito_role_lbz_relay_token`"

        ```yaml
        # Type: string
        koito_role_lbz_relay_token: ""
        ```

    ??? variable string "`koito_role_force_tz`"

        ```yaml
        # Type: string
        koito_role_force_tz: ""
        ```

    ??? variable string "`koito_role_disable_deezer`"

        ```yaml
        # Type: string
        koito_role_disable_deezer: "false"
        ```

    ??? variable string "`koito_role_disable_cover_art_archive`"

        ```yaml
        # Type: string
        koito_role_disable_cover_art_archive: "false"
        ```

    ??? variable string "`koito_role_disable_musicbrainz`"

        ```yaml
        # Type: string
        koito_role_disable_musicbrainz: "false"
        ```

    ??? variable string "`koito_role_subsonic_url`"

        ```yaml
        # Type: string
        koito_role_subsonic_url: ""
        ```

    ??? variable string "`koito_role_subsonic_params`"

        ```yaml
        # Type: string
        koito_role_subsonic_params: ""
        ```

    ??? variable string "`koito_role_lastfm_api_key`"

        ```yaml
        # Type: string
        koito_role_lastfm_api_key: ""
        ```

    ??? variable string "`koito_role_skip_import`"

        ```yaml
        # Type: string
        koito_role_skip_import: "false"
        ```

    ??? variable string "`koito_role_disable_rate_limit`"

        ```yaml
        # Type: string
        koito_role_disable_rate_limit: "false"
        ```

    ??? variable string "`koito_role_throttle_imports_ms`"

        ```yaml
        # Type: string
        koito_role_throttle_imports_ms: "0"
        ```

    ??? variable string "`koito_role_import_before_unix`"

        ```yaml
        # Type: string
        koito_role_import_before_unix: ""
        ```

    ??? variable string "`koito_role_import_after_unix`"

        ```yaml
        # Type: string
        koito_role_import_after_unix: ""
        ```

    ??? variable string "`koito_role_fetch_images_during_import`"

        ```yaml
        # Type: string
        koito_role_fetch_images_during_import: "false"
        ```

    ??? variable string "`koito_role_cors_allowed_origins`"

        ```yaml
        # Type: string
        koito_role_cors_allowed_origins: ""
        ```

=== "Web"

    ??? variable string "`koito_role_web_subdomain`"

        ```yaml
        # Type: string
        koito_role_web_subdomain: "{{ koito_name }}"
        ```

    ??? variable string "`koito_role_web_domain`"

        ```yaml
        # Type: string
        koito_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`koito_role_web_port`"

        ```yaml
        # Type: string
        koito_role_web_port: "4110"
        ```

    ??? variable string "`koito_role_web_url`"

        ```yaml
        # Type: string
        koito_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='koito') + '.' + lookup('role_var', '_web_domain', role='koito')
                              if (lookup('role_var', '_web_subdomain', role='koito') | length > 0)
                              else lookup('role_var', '_web_domain', role='koito')) }}"
        ```

    ??? variable string "`koito_role_web_host`"

        ```yaml
        # Type: string
        koito_role_web_host: "{{ (lookup('role_var', '_web_subdomain', role='koito') + '.' + lookup('role_var', '_web_domain', role='koito')
                               if (lookup('role_var', '_web_subdomain', role='koito') | length > 0)
                               else lookup('role_var', '_web_domain', role='koito')) }}"
        ```

    ??? variable string "`koito_role_allowed_hosts`"

        ```yaml
        # Type: string
        koito_role_allowed_hosts: "{{ lookup('role_var', '_web_host', role='koito') }}"
        ```

=== "DNS"

    ??? variable string "`koito_role_dns_record`"

        ```yaml
        # Type: string
        koito_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='koito') }}"
        ```

    ??? variable string "`koito_role_dns_zone`"

        ```yaml
        # Type: string
        koito_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='koito') }}"
        ```

    ??? variable bool "`koito_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        koito_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`koito_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        koito_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`koito_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        koito_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`koito_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        koito_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`koito_role_traefik_certresolver`"

        ```yaml
        # Type: string
        koito_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`koito_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        koito_role_traefik_enabled: true
        ```

    ??? variable bool "`koito_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        koito_role_traefik_api_enabled: true
        ```

    ??? variable string "`koito_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        koito_role_traefik_api_endpoint: "PathPrefix(`/apis`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`koito_role_docker_container`"

        ```yaml
        # Type: string
        koito_role_docker_container: "{{ koito_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`koito_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_image_pull: true
        ```

    ??? variable string "`koito_role_docker_image_repo`"

        ```yaml
        # Type: string
        koito_role_docker_image_repo: "gabehf/koito"
        ```

    ??? variable string "`koito_role_docker_image_tag`"

        ```yaml
        # Type: string
        koito_role_docker_image_tag: "latest"
        ```

    ??? variable string "`koito_role_docker_image`"

        ```yaml
        # Type: string
        koito_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='koito') }}:{{ lookup('role_var', '_docker_image_tag', role='koito') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`koito_role_docker_envs_default`"

        ```yaml
        # Type: dict
        koito_role_docker_envs_default:
          TZ: "{{ tz }}"
          KOITO_DATABASE_URL: "{{ lookup('role_var', '_database_url', role='koito')
                               if (lookup('role_var', '_database_url', role='koito') | length > 0)
                               else 'postgres://' + (lookup('role_var', '_postgres_user', role='koito')
                               if (lookup('role_var', '_postgres_user', role='koito') | length > 0)
                               else lookup('role_var', '_docker_env_user', role='postgres')) + ':' + (lookup('role_var', '_postgres_password', role='koito')
                               if (lookup('role_var', '_postgres_password', role='koito') | length > 0)
                               else lookup('role_var', '_docker_env_password', role='postgres')) + '@' + lookup('role_var', '_postgres_name', role='koito') + ':5432/' + lookup('role_var', '_postgres_docker_env_db', role='koito') }}"
          KOITO_ALLOWED_HOSTS: "{{ lookup('role_var', '_allowed_hosts', role='koito') }}"
          KOITO_DEFAULT_USERNAME: "{{ lookup('role_var', '_default_username', role='koito') }}"
          KOITO_DEFAULT_PASSWORD: "{{ lookup('role_var', '_default_password', role='koito') }}"
          KOITO_DEFAULT_THEME: "{{ lookup('role_var', '_default_theme', role='koito') }}"
          KOITO_LOGIN_GATE: "{{ lookup('role_var', '_login_gate', role='koito') }}"
          KOITO_BIND_ADDR: "{{ lookup('role_var', '_bind_addr', role='koito')
                            if (lookup('role_var', '_bind_addr', role='koito') | length > 0)
                            else omit }}"
          KOITO_LISTEN_PORT: "{{ lookup('role_var', '_web_port', role='koito') }}"
          KOITO_ENABLE_STRUCTURED_LOGGING: "{{ lookup('role_var', '_enable_structured_logging', role='koito') }}"
          KOITO_ENABLE_FULL_IMAGE_CACHE: "{{ lookup('role_var', '_enable_full_image_cache', role='koito') }}"
          KOITO_LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='koito') }}"
          KOITO_MUSICBRAINZ_URL: "{{ lookup('role_var', '_musicbrainz_url', role='koito') }}"
          KOITO_MUSICBRAINZ_RATE_LIMIT: "{{ lookup('role_var', '_musicbrainz_rate_limit', role='koito') }}"
          KOITO_ENABLE_LBZ_RELAY: "{{ lookup('role_var', '_enable_lbz_relay', role='koito') }}"
          KOITO_LBZ_RELAY_URL: "{{ lookup('role_var', '_lbz_relay_url', role='koito')
                                if (lookup('role_var', '_enable_lbz_relay', role='koito') == 'true')
                                else omit }}"
          KOITO_LBZ_RELAY_TOKEN: "{{ lookup('role_var', '_lbz_relay_token', role='koito')
                                  if (lookup('role_var', '_enable_lbz_relay', role='koito') == 'true')
                                  else omit }}"
          KOITO_FORCE_TZ: "{{ lookup('role_var', '_force_tz', role='koito')
                            if (lookup('role_var', '_force_tz', role='koito') | length > 0)
                            else omit }}"
          KOITO_DISABLE_DEEZER: "{{ lookup('role_var', '_disable_deezer', role='koito') }}"
          KOITO_DISABLE_COVER_ART_ARCHIVE: "{{ lookup('role_var', '_disable_cover_art_archive', role='koito') }}"
          KOITO_DISABLE_MUSICBRAINZ: "{{ lookup('role_var', '_disable_musicbrainz', role='koito') }}"
          KOITO_SUBSONIC_URL: "{{ lookup('role_var', '_subsonic_url', role='koito')
                                if (lookup('role_var', '_subsonic_url', role='koito') | length > 0)
                                else omit }}"
          KOITO_SUBSONIC_PARAMS: "{{ lookup('role_var', '_subsonic_params', role='koito')
                                   if (lookup('role_var', '_subsonic_params', role='koito') | length > 0)
                                   else omit }}"
          KOITO_LASTFM_API_KEY: "{{ lookup('role_var', '_lastfm_api_key', role='koito')
                                  if (lookup('role_var', '_lastfm_api_key', role='koito') | length > 0)
                                  else omit }}"
          KOITO_SKIP_IMPORT: "{{ lookup('role_var', '_skip_import', role='koito') }}"
          KOITO_DISABLE_RATE_LIMIT: "{{ lookup('role_var', '_disable_rate_limit', role='koito') }}"
          KOITO_THROTTLE_IMPORTS_MS: "{{ lookup('role_var', '_throttle_imports_ms', role='koito') }}"
          KOITO_IMPORT_BEFORE_UNIX: "{{ lookup('role_var', '_import_before_unix', role='koito')
                                     if (lookup('role_var', '_import_before_unix', role='koito') | length > 0)
                                     else omit }}"
          KOITO_IMPORT_AFTER_UNIX: "{{ lookup('role_var', '_import_after_unix', role='koito')
                                    if (lookup('role_var', '_import_after_unix', role='koito') | length > 0)
                                    else omit }}"
          KOITO_FETCH_IMAGES_DURING_IMPORT: "{{ lookup('role_var', '_fetch_images_during_import', role='koito') }}"
          KOITO_CORS_ALLOWED_ORIGINS: "{{ lookup('role_var', '_cors_allowed_origins', role='koito')
                                       if (lookup('role_var', '_cors_allowed_origins', role='koito') | length > 0)
                                       else omit }}"
        ```

    ??? variable dict "`koito_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        koito_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`koito_role_docker_volumes_default`"

        ```yaml
        # Type: list
        koito_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location_data', role='koito') }}:/etc/koito"
        ```

    ??? variable list "`koito_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        koito_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`koito_role_docker_hostname`"

        ```yaml
        # Type: string
        koito_role_docker_hostname: "{{ koito_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`koito_role_docker_networks_alias`"

        ```yaml
        # Type: string
        koito_role_docker_networks_alias: "{{ koito_name }}"
        ```

    ??? variable list "`koito_role_docker_networks_default`"

        ```yaml
        # Type: list
        koito_role_docker_networks_default: []
        ```

    ??? variable list "`koito_role_docker_networks_custom`"

        ```yaml
        # Type: list
        koito_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`koito_role_docker_restart_policy`"

        ```yaml
        # Type: string
        koito_role_docker_restart_policy: unless-stopped
        ```

    <h5>User</h5>

    ??? variable string "`koito_role_docker_user`"

        ```yaml
        # Type: string
        koito_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`koito_role_depends_on`"

        ```yaml
        # Type: string
        koito_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='koito')
                                if lookup('role_var', '_postgres_deploy', role='koito')
                                else '' }}"
        ```

    ??? variable string "`koito_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        koito_role_depends_on_delay: "0"
        ```

    ??? variable string "`koito_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        koito_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`koito_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        koito_role_docker_blkio_weight:
        ```

    ??? variable int "`koito_role_docker_cpu_period`"

        ```yaml
        # Type: int
        koito_role_docker_cpu_period:
        ```

    ??? variable int "`koito_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        koito_role_docker_cpu_quota:
        ```

    ??? variable int "`koito_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        koito_role_docker_cpu_shares:
        ```

    ??? variable string "`koito_role_docker_cpus`"

        ```yaml
        # Type: string
        koito_role_docker_cpus:
        ```

    ??? variable string "`koito_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        koito_role_docker_cpuset_cpus:
        ```

    ??? variable string "`koito_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        koito_role_docker_cpuset_mems:
        ```

    ??? variable string "`koito_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        koito_role_docker_kernel_memory:
        ```

    ??? variable string "`koito_role_docker_memory`"

        ```yaml
        # Type: string
        koito_role_docker_memory:
        ```

    ??? variable string "`koito_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        koito_role_docker_memory_reservation:
        ```

    ??? variable string "`koito_role_docker_memory_swap`"

        ```yaml
        # Type: string
        koito_role_docker_memory_swap:
        ```

    ??? variable int "`koito_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        koito_role_docker_memory_swappiness:
        ```

    ??? variable string "`koito_role_docker_shm_size`"

        ```yaml
        # Type: string
        koito_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`koito_role_docker_cap_drop`"

        ```yaml
        # Type: list
        koito_role_docker_cap_drop:
        ```

    ??? variable string "`koito_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        koito_role_docker_cgroupns_mode:
        ```

    ??? variable list "`koito_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        koito_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`koito_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        koito_role_docker_device_read_bps:
        ```

    ??? variable list "`koito_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        koito_role_docker_device_read_iops:
        ```

    ??? variable list "`koito_role_docker_device_requests`"

        ```yaml
        # Type: list
        koito_role_docker_device_requests:
        ```

    ??? variable list "`koito_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        koito_role_docker_device_write_bps:
        ```

    ??? variable list "`koito_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        koito_role_docker_device_write_iops:
        ```

    ??? variable list "`koito_role_docker_devices`"

        ```yaml
        # Type: list
        koito_role_docker_devices:
        ```

    ??? variable list "`koito_role_docker_groups`"

        ```yaml
        # Type: list
        koito_role_docker_groups:
        ```

    ??? variable bool "`koito_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_privileged:
        ```

    ??? variable list "`koito_role_docker_security_opts`"

        ```yaml
        # Type: list
        koito_role_docker_security_opts:
        ```

    ??? variable string "`koito_role_docker_userns_mode`"

        ```yaml
        # Type: string
        koito_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`koito_role_docker_dns_opts`"

        ```yaml
        # Type: list
        koito_role_docker_dns_opts:
        ```

    ??? variable list "`koito_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        koito_role_docker_dns_search_domains:
        ```

    ??? variable list "`koito_role_docker_dns_servers`"

        ```yaml
        # Type: list
        koito_role_docker_dns_servers:
        ```

    ??? variable string "`koito_role_docker_domainname`"

        ```yaml
        # Type: string
        koito_role_docker_domainname:
        ```

    ??? variable list "`koito_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        koito_role_docker_exposed_ports:
        ```

    ??? variable dict "`koito_role_docker_hosts`"

        ```yaml
        # Type: dict
        koito_role_docker_hosts:
        ```

    ??? variable bool "`koito_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_hosts_use_common:
        ```

    ??? variable string "`koito_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        koito_role_docker_ipc_mode:
        ```

    ??? variable list "`koito_role_docker_links`"

        ```yaml
        # Type: list
        koito_role_docker_links:
        ```

    ??? variable string "`koito_role_docker_network_mode`"

        ```yaml
        # Type: string
        koito_role_docker_network_mode:
        ```

    ??? variable string "`koito_role_docker_pid_mode`"

        ```yaml
        # Type: string
        koito_role_docker_pid_mode:
        ```

    ??? variable list "`koito_role_docker_ports`"

        ```yaml
        # Type: list
        koito_role_docker_ports:
        ```

    ??? variable string "`koito_role_docker_uts`"

        ```yaml
        # Type: string
        koito_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`koito_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_keep_volumes:
        ```

    ??? variable list "`koito_role_docker_mounts`"

        ```yaml
        # Type: list
        koito_role_docker_mounts:
        ```

    ??? variable dict "`koito_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        koito_role_docker_storage_opts:
        ```

    ??? variable list "`koito_role_docker_tmpfs`"

        ```yaml
        # Type: list
        koito_role_docker_tmpfs:
        ```

    ??? variable string "`koito_role_docker_volume_driver`"

        ```yaml
        # Type: string
        koito_role_docker_volume_driver:
        ```

    ??? variable list "`koito_role_docker_volumes_from`"

        ```yaml
        # Type: list
        koito_role_docker_volumes_from:
        ```

    ??? variable bool "`koito_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_volumes_global:
        ```

    ??? variable string "`koito_role_docker_working_dir`"

        ```yaml
        # Type: string
        koito_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`koito_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_auto_remove:
        ```

    ??? variable bool "`koito_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_cleanup:
        ```

    ??? variable string "`koito_role_docker_force_kill`"

        ```yaml
        # Type: string
        koito_role_docker_force_kill:
        ```

    ??? variable dict "`koito_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        koito_role_docker_healthcheck:
        ```

    ??? variable int "`koito_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        koito_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`koito_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_init:
        ```

    ??? variable string "`koito_role_docker_kill_signal`"

        ```yaml
        # Type: string
        koito_role_docker_kill_signal:
        ```

    ??? variable string "`koito_role_docker_log_driver`"

        ```yaml
        # Type: string
        koito_role_docker_log_driver:
        ```

    ??? variable dict "`koito_role_docker_log_options`"

        ```yaml
        # Type: dict
        koito_role_docker_log_options:
        ```

    ??? variable bool "`koito_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_oom_killer:
        ```

    ??? variable int "`koito_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        koito_role_docker_oom_score_adj:
        ```

    ??? variable bool "`koito_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_output_logs:
        ```

    ??? variable bool "`koito_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_paused:
        ```

    ??? variable bool "`koito_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_recreate:
        ```

    ??? variable int "`koito_role_docker_restart_retries`"

        ```yaml
        # Type: int
        koito_role_docker_restart_retries:
        ```

    ??? variable string "`koito_role_docker_stop_signal`"

        ```yaml
        # Type: string
        koito_role_docker_stop_signal:
        ```

    ??? variable int "`koito_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        koito_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`koito_role_docker_capabilities`"

        ```yaml
        # Type: list
        koito_role_docker_capabilities:
        ```

    ??? variable string "`koito_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        koito_role_docker_cgroup_parent:
        ```

    ??? variable list "`koito_role_docker_commands`"

        ```yaml
        # Type: list
        koito_role_docker_commands:
        ```

    ??? variable int "`koito_role_docker_create_timeout`"

        ```yaml
        # Type: int
        koito_role_docker_create_timeout:
        ```

    ??? variable string "`koito_role_docker_entrypoint`"

        ```yaml
        # Type: string
        koito_role_docker_entrypoint:
        ```

    ??? variable string "`koito_role_docker_env_file`"

        ```yaml
        # Type: string
        koito_role_docker_env_file:
        ```

    ??? variable dict "`koito_role_docker_labels`"

        ```yaml
        # Type: dict
        koito_role_docker_labels:
        ```

    ??? variable bool "`koito_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_labels_use_common:
        ```

    ??? variable bool "`koito_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_read_only:
        ```

    ??? variable string "`koito_role_docker_runtime`"

        ```yaml
        # Type: string
        koito_role_docker_runtime:
        ```

    ??? variable list "`koito_role_docker_sysctls`"

        ```yaml
        # Type: list
        koito_role_docker_sysctls:
        ```

    ??? variable list "`koito_role_docker_ulimits`"

        ```yaml
        # Type: list
        koito_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`koito_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        koito_role_autoheal_enabled: true
        ```

    ??? variable bool "`koito_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        koito_role_diun_enabled: true
        ```

    ??? variable bool "`koito_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        koito_role_dns_enabled: true
        ```

    ??? variable bool "`koito_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        koito_role_docker_controller: true
        ```

    ??? variable list "`koito_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        koito_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`koito_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        koito_role_docker_volumes_download:
        ```

    ??? variable string "`koito_role_themepark_addons`"

        ```yaml
        # Type: string
        koito_role_themepark_addons:
        ```

    ??? variable string "`koito_role_themepark_app`"

        ```yaml
        # Type: string
        koito_role_themepark_app:
        ```

    ??? variable string "`koito_role_themepark_theme`"

        ```yaml
        # Type: string
        koito_role_themepark_theme:
        ```

    ??? variable string "`koito_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        koito_role_traefik_api_middleware:
        ```

    ??? variable string "`koito_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        koito_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`koito_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        koito_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`koito_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        koito_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`koito_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        koito_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`koito_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        koito_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`koito_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        koito_role_traefik_middleware_http:
        ```

    ??? variable bool "`koito_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        koito_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`koito_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        koito_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`koito_role_traefik_priority`"

        ```yaml
        # Type: string
        koito_role_traefik_priority:
        ```

    ??? variable bool "`koito_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        koito_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`koito_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        koito_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`koito_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        koito_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`koito_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        koito_role_web_api_http_port:
        ```

    ??? variable string "`koito_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        koito_role_web_api_http_scheme:
        ```

    ??? variable dict "`koito_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        koito_role_web_api_http_serverstransport:
        ```

    ??? variable string "`koito_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        koito_role_web_api_port:
        ```

    ??? variable string "`koito_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        koito_role_web_api_scheme:
        ```

    ??? variable dict "`koito_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        koito_role_web_api_serverstransport:
        ```

    ??? variable list "`koito_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        koito_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            koito_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "koito2.{{ user.domain }}"
              - "koito.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`koito_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        koito_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            koito_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'koito2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`koito_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        koito_role_web_http_port:
        ```

    ??? variable string "`koito_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        koito_role_web_http_scheme:
        ```

    ??? variable dict "`koito_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        koito_role_web_http_serverstransport:
        ```

    ??? variable string "`koito_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        koito_role_web_scheme:
        ```

    ??? variable dict "`koito_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        koito_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
