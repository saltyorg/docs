---
icon: material/docker
hide:
  - tags
tags:
  - silo
  - media
  - streaming
  - transcoding
saltbox_automation:
  app_links:
    - name: Manual
      url: https://siloserver.org/docs
      type: documentation
    - name: Releases
      url: https://github.com/Silo-Server/silo-server/pkgs/container/silo-server
      type: github
    - name: Community
      url: https://discord.gg/4RxuUQAEnW
      type: discord
  project_description:
    name: Silo
    summary: |-
      a self-hosted media server for movies, shows, music, and books with direct play, transcoding, and optional Jellyfin-compatible client support.
    link: https://siloserver.org
    categories:
      - Content Delivery Apps > Media Server
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Silo

## Overview

[Silo](https://siloserver.org) is a self-hosted media server for movies, shows, music, and books with direct play, transcoding, and optional Jellyfin-compatible client support.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://siloserver.org/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/Silo-Server/silo-server/pkgs/container/silo-server){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/4RxuUQAEnW){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-silo
```

## Usage

Visit <https://silo.iYOUR_DOMAIN_NAMEi>.

Configure libraries against the usual `/mnt/unionfs/...` paths in the admin UI.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        silo_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `silo_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `silo_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`silo_name`"

        ```yaml
        # Type: string
        silo_name: silo
        ```

=== "Settings"

    ??? variable bool "`silo_role_jf_enabled`"

        ```yaml
        # Toggle Jellyfin-compatible endpoint
        # Type: bool (true/false)
        silo_role_jf_enabled: false
        ```

    ??? variable bool "`silo_role_abs_enabled`"

        ```yaml
        # Toggle Audiobookshelf-compatible endpoint
        # Type: bool (true/false)
        silo_role_abs_enabled: false
        ```

=== "Postgres"

    ??? variable bool "`silo_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        silo_role_postgres_deploy: true
        ```

    ??? variable string "`silo_role_postgres_name`"

        ```yaml
        # Type: string
        silo_role_postgres_name: "{{ silo_name }}-postgres"
        ```

    ??? variable string "`silo_role_postgres_user`"

        ```yaml
        # If empty it will fall back to the postgres role default.
        # Type: string
        silo_role_postgres_user: ""
        ```

    ??? variable string "`silo_role_postgres_password`"

        ```yaml
        # If empty it will fall back to the postgres role default.
        # Type: string
        silo_role_postgres_password: ""
        ```

    ??? variable string "`silo_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        silo_role_postgres_docker_env_db: "silo"
        ```

    ??? variable string "`silo_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        silo_role_postgres_docker_image_repo: "pgvector/pgvector"
        ```

    ??? variable string "`silo_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        silo_role_postgres_docker_image_tag: "pg18"
        ```

    ??? variable string "`silo_role_postgres_docker_shm_size`"

        ```yaml
        # Type: string
        silo_role_postgres_docker_shm_size: "8G"
        ```

    ??? variable string "`silo_role_database_url`"

        ```yaml
        # Type: string
        silo_role_database_url: "postgres://{{ lookup('role_var', '_postgres_credentials_lookup', role='silo') }}@{{ lookup('role_var', '_postgres_name', role='silo') }}:5432/{{ lookup('role_var', '_postgres_docker_env_db', role='silo') }}?sslmode=disable"
        ```

    ??? variable dict "`silo_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        silo_role_postgres_docker_healthcheck:
          test:
            - "CMD"
            - "pg_isready"
            - "-d"
            - "{{ lookup('role_var', '_postgres_docker_env_db', role='silo') }}"
            - "-U"
            - "{{ lookup('role_var', '_postgres_user_lookup', role='silo') }}"
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`silo_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        silo_role_postgres_paths_folder: "{{ silo_name }}"
        ```

    ??? variable string "`silo_role_postgres_paths_location`"

        ```yaml
        # Type: string
        silo_role_postgres_paths_location: "{{ server_appdata_path }}/{{ silo_role_postgres_paths_folder }}/postgres"
        ```

=== "Redis"

    ??? variable string "`silo_role_redis_name`"

        ```yaml
        # Type: string
        silo_role_redis_name: "{{ silo_name }}-redis"
        ```

    ??? variable string "`silo_role_redis_docker_image_tag`"

        ```yaml
        # Type: string
        silo_role_redis_docker_image_tag: "alpine"
        ```

    ??? variable string "`silo_role_redis_paths_folder`"

        ```yaml
        # Type: string
        silo_role_redis_paths_folder: "{{ silo_name }}"
        ```

    ??? variable string "`silo_role_redis_paths_location`"

        ```yaml
        # Type: string
        silo_role_redis_paths_location: "{{ server_appdata_path }}/{{ silo_role_redis_paths_folder }}/redis"
        ```

=== "Web"

    ??? variable string "`silo_role_web_subdomain`"

        ```yaml
        # Type: string
        silo_role_web_subdomain: "{{ silo_name }}"
        ```

    ??? variable string "`silo_role_web_domain`"

        ```yaml
        # Type: string
        silo_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`silo_role_web_port`"

        ```yaml
        # Type: string
        silo_role_web_port: "8080"
        ```

    ??? variable string "`silo_role_web_url`"

        ```yaml
        # Type: string
        silo_role_web_url: "{{ lookup('role_web', role='silo', scheme='https') }}"
        ```

    ??? variable string "`silo_role_web_jf_subdomain`"

        ```yaml
        # Type: string
        silo_role_web_jf_subdomain: "{{ silo_name }}jf"
        ```

    ??? variable string "`silo_role_web_jf_domain`"

        ```yaml
        # Type: string
        silo_role_web_jf_domain: "{{ user.domain }}"
        ```

    ??? variable string "`silo_role_web_jf_port`"

        ```yaml
        # Type: string
        silo_role_web_jf_port: "8096"
        ```

    ??? variable string "`silo_role_web_jf_host`"

        ```yaml
        # Type: string
        silo_role_web_jf_host: "{{ lookup('role_web', role='silo', endpoint='web_jf') }}"
        ```

    ??? variable string "`silo_role_web_jf_url`"

        ```yaml
        # Type: string
        silo_role_web_jf_url: "https://{{ lookup('role_var', '_web_jf_host', role='silo') }}"
        ```

    ??? variable string "`silo_role_web_abs_subdomain`"

        ```yaml
        # Type: string
        silo_role_web_abs_subdomain: "{{ silo_name }}abs"
        ```

    ??? variable string "`silo_role_web_abs_domain`"

        ```yaml
        # Type: string
        silo_role_web_abs_domain: "{{ user.domain }}"
        ```

    ??? variable string "`silo_role_web_abs_port`"

        ```yaml
        # Type: string
        silo_role_web_abs_port: "13378"
        ```

    ??? variable string "`silo_role_web_abs_host`"

        ```yaml
        # Type: string
        silo_role_web_abs_host: "{{ lookup('role_web', role='silo', endpoint='web_abs') }}"
        ```

    ??? variable string "`silo_role_web_abs_url`"

        ```yaml
        # Type: string
        silo_role_web_abs_url: "https://{{ lookup('role_var', '_web_abs_host', role='silo') }}"
        ```

=== "DNS"

    ??? variable string "`silo_role_dns_record`"

        ```yaml
        # Type: string
        silo_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='silo') }}"
        ```

    ??? variable string "`silo_role_dns_zone`"

        ```yaml
        # Type: string
        silo_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='silo') }}"
        ```

    ??? variable bool "`silo_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        silo_role_dns_proxy: "{{ dns_proxied }}"
        ```

    ??? variable string "`silo_role_jf_dns_record`"

        ```yaml
        # Type: string
        silo_role_jf_dns_record: "{{ lookup('role_var', '_web_jf_subdomain', role='silo') }}"
        ```

    ??? variable string "`silo_role_jf_dns_zone`"

        ```yaml
        # Type: string
        silo_role_jf_dns_zone: "{{ lookup('role_var', '_web_jf_domain', role='silo') }}"
        ```

    ??? variable bool "`silo_role_jf_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        silo_role_jf_dns_proxy: "{{ lookup('role_var', '_dns_proxy', role='silo') }}"
        ```

    ??? variable string "`silo_role_abs_dns_record`"

        ```yaml
        # Type: string
        silo_role_abs_dns_record: "{{ lookup('role_var', '_web_abs_subdomain', role='silo') }}"
        ```

    ??? variable string "`silo_role_abs_dns_zone`"

        ```yaml
        # Type: string
        silo_role_abs_dns_zone: "{{ lookup('role_var', '_web_abs_domain', role='silo') }}"
        ```

    ??? variable bool "`silo_role_abs_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        silo_role_abs_dns_proxy: "{{ lookup('role_var', '_dns_proxy', role='silo') }}"
        ```

=== "Traefik"

    ??? variable string "`silo_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        silo_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`silo_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        silo_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`silo_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        silo_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`silo_role_traefik_middleware_default_api`"

        ```yaml
        # Type: string
        silo_role_traefik_middleware_default_api: "{{ traefik_default_middleware_api }}"
        ```

    ??? variable string "`silo_role_traefik_middleware_custom_api`"

        ```yaml
        # Type: string
        silo_role_traefik_middleware_custom_api: ""
        ```

    ??? variable string "`silo_role_traefik_certresolver`"

        ```yaml
        # Type: string
        silo_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`silo_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        silo_role_traefik_enabled: true
        ```

    ??? variable bool "`silo_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        silo_role_traefik_api_enabled: false
        ```

    ??? variable string "`silo_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        silo_role_traefik_api_endpoint: ""
        ```

    ??? variable bool "`silo_role_traefik_gzip_enabled`"

        ```yaml
        # Type: bool (true/false)
        silo_role_traefik_gzip_enabled: false
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`silo_role_docker_container`"

        ```yaml
        # Type: string
        silo_role_docker_container: "{{ silo_name }}"
        ```

    <h5>GPU</h5>

    ??? variable bool "`silo_role_docker_gpu_enabled`"

        ```yaml
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        silo_role_docker_gpu_enabled: true
        ```

    ??? variable bool "`silo_role_docker_nvidia_disabled`"

        ```yaml
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        silo_role_docker_nvidia_disabled: false
        ```

    ??? variable bool "`silo_role_docker_dev_dri_disabled`"

        ```yaml
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        silo_role_docker_dev_dri_disabled: false
        ```

    <h5>Image</h5>

    ??? variable bool "`silo_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_image_pull: true
        ```

    ??? variable string "`silo_role_docker_image_repo`"

        ```yaml
        # Type: string
        silo_role_docker_image_repo: "ghcr.io/silo-server/silo-server"
        ```

    ??? variable string "`silo_role_docker_image_tag`"

        ```yaml
        # Type: string
        silo_role_docker_image_tag: "latest"
        ```

    ??? variable string "`silo_role_docker_image`"

        ```yaml
        # Type: string
        silo_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='silo') }}:{{ lookup('role_var', '_docker_image_tag', role='silo') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`silo_role_docker_envs_default`"

        ```yaml
        # Type: dict
        silo_role_docker_envs_default:
          HOME: "/tmp"
          SILO_PUBLIC_URL: "{{ lookup('role_var', '_web_url', role='silo') }}"
          MODE: "integrated"
          SECRET_KEY: "{{ silo_saltbox_facts.facts.secret_key }}"
          DATABASE_URL: "{{ lookup('role_var', '_database_url', role='silo') }}"
          REDIS_URL: "redis://{{ lookup('role_var', '_redis_name', role='silo') }}:6379"
          SILO_PLUGIN_CACHE_DIR: "/var/lib/silo/plugins"
          POSTGRES_TUNE: "auto"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`silo_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        silo_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`silo_role_docker_volumes_default`"

        ```yaml
        # Type: list
        silo_role_docker_volumes_default:
          - "{{ silo_role_paths_location }}/plugins:/var/lib/silo/plugins"
          - "{{ silo_role_paths_location }}/compat:/var/lib/silo/compat"
          - "{{ silo_role_paths_transcodes_location }}:/tmp/silo-transcode"
          - "{{ silo_role_paths_location }}/audiobook-covers:/var/lib/silo/audiobook-covers"
          - "{{ silo_role_paths_location }}/catalog-seeds:/catalog-seeds:ro"
          - "/proc/meminfo:/host/proc/meminfo:ro"
        ```

    ??? variable list "`silo_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        silo_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable list "`silo_role_docker_labels_jf_template`"

        ```yaml
        # Type: list
        silo_role_docker_labels_jf_template:
          - '{ "traefik.http.routers.{{ silo_name }}-jf-http.entrypoints": "{{ traefik_entrypoint_web }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf-http.service": "{{ silo_name }}-jf" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf-http.rule": "Host(`{{ lookup("role_var", "_web_jf_host", role="silo") }}`)" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf-http.middlewares": "{{ traefik_default_middleware_http }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf-http.priority": "20" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf.entrypoints": "{{ traefik_entrypoint_websecure }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf.service": "{{ silo_name }}-jf" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf.rule": "Host(`{{ lookup("role_var", "_web_jf_host", role="silo") }}`)" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="silo") }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf.middlewares": "{{ lookup("role_var", "_traefik_middleware_default", role="silo") }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-jf.priority": "20" }'
          - '{ "traefik.http.services.{{ silo_name }}-jf.loadbalancer.server.port": "{{ lookup("role_var", "_web_jf_port", role="silo") }}" }'
        ```

    ??? variable string "`silo_role_docker_labels_jf`"

        ```yaml
        # Type: string
        silo_role_docker_labels_jf: "{{ (silo_role_docker_labels_jf_template | map('from_json') | combine)
                                     if (lookup('role_var', '_jf_enabled', role='silo') | bool)
                                     else {} }}"
        ```

    ??? variable list "`silo_role_docker_labels_abs_template`"

        ```yaml
        # Type: list
        silo_role_docker_labels_abs_template:
          - '{ "traefik.http.routers.{{ silo_name }}-abs-http.entrypoints": "{{ traefik_entrypoint_web }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs-http.service": "{{ silo_name }}-abs" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs-http.rule": "Host(`{{ lookup("role_var", "_web_abs_host", role="silo") }}`)" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs-http.middlewares": "{{ traefik_default_middleware_http }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs-http.priority": "20" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs.entrypoints": "{{ traefik_entrypoint_websecure }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs.service": "{{ silo_name }}-abs" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs.rule": "Host(`{{ lookup("role_var", "_web_abs_host", role="silo") }}`)" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="silo") }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs.middlewares": "{{ lookup("role_var", "_traefik_middleware_default", role="silo") }}" }'
          - '{ "traefik.http.routers.{{ silo_name }}-abs.priority": "20" }'
          - '{ "traefik.http.services.{{ silo_name }}-abs.loadbalancer.server.port": "{{ lookup("role_var", "_web_abs_port", role="silo") }}" }'
        ```

    ??? variable string "`silo_role_docker_labels_abs`"

        ```yaml
        # Type: string
        silo_role_docker_labels_abs: "{{ (silo_role_docker_labels_abs_template | map('from_json') | combine)
                                      if (lookup('role_var', '_abs_enabled', role='silo') | bool)
                                      else {} }}"
        ```

    ??? variable dict "`silo_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        silo_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`silo_role_docker_hostname`"

        ```yaml
        # Type: string
        silo_role_docker_hostname: "{{ silo_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`silo_role_docker_networks_alias`"

        ```yaml
        # Type: string
        silo_role_docker_networks_alias: "{{ silo_name }}"
        ```

    ??? variable list "`silo_role_docker_networks_default`"

        ```yaml
        # Type: list
        silo_role_docker_networks_default: []
        ```

    ??? variable list "`silo_role_docker_networks_custom`"

        ```yaml
        # Type: list
        silo_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`silo_role_docker_restart_policy`"

        ```yaml
        # Type: string
        silo_role_docker_restart_policy: unless-stopped
        ```

    <h5>User</h5>

    ??? variable string "`silo_role_docker_user`"

        ```yaml
        # Type: string
        silo_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`silo_role_depends_on`"

        ```yaml
        # Type: string
        silo_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='silo') }},{{ lookup('role_var', '_redis_name', role='silo') }}"
        ```

    ??? variable string "`silo_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        silo_role_depends_on_delay: "0"
        ```

    ??? variable string "`silo_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        silo_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    A blank value is YAML null and inherits any lower-precedence role or shared default. Explicit Ansible omit is accepted only for optional Docker settings; default-backed and required settings reject it. Use the documented typed empty value, such as `""`, `[]`, or `{}`, when disabling a guaranteed setting.

    <h5>Resource Limits</h5>

    ??? variable int "`silo_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        silo_role_docker_blkio_weight:
        ```

    ??? variable int "`silo_role_docker_cpu_period`"

        ```yaml
        # Type: int
        silo_role_docker_cpu_period:
        ```

    ??? variable int "`silo_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        silo_role_docker_cpu_quota:
        ```

    ??? variable int "`silo_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        silo_role_docker_cpu_shares:
        ```

    ??? variable string "`silo_role_docker_cpus`"

        ```yaml
        # Type: string
        silo_role_docker_cpus:
        ```

    ??? variable string "`silo_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        silo_role_docker_cpuset_cpus:
        ```

    ??? variable string "`silo_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        silo_role_docker_cpuset_mems:
        ```

    ??? variable string "`silo_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        silo_role_docker_kernel_memory:
        ```

    ??? variable string "`silo_role_docker_memory`"

        ```yaml
        # Type: string
        silo_role_docker_memory:
        ```

    ??? variable string "`silo_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        silo_role_docker_memory_reservation:
        ```

    ??? variable string "`silo_role_docker_memory_swap`"

        ```yaml
        # Type: string
        silo_role_docker_memory_swap:
        ```

    ??? variable int "`silo_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        silo_role_docker_memory_swappiness:
        ```

    ??? variable string "`silo_role_docker_shm_size`"

        ```yaml
        # Type: string
        silo_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`silo_role_docker_cap_drop`"

        ```yaml
        # Type: list
        silo_role_docker_cap_drop:
        ```

    ??? variable string "`silo_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        silo_role_docker_cgroupns_mode:
        ```

    ??? variable list "`silo_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        silo_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`silo_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        silo_role_docker_device_read_bps:
        ```

    ??? variable list "`silo_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        silo_role_docker_device_read_iops:
        ```

    ??? variable list "`silo_role_docker_device_requests`"

        ```yaml
        # Type: list
        silo_role_docker_device_requests:
        ```

    ??? variable list "`silo_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        silo_role_docker_device_write_bps:
        ```

    ??? variable list "`silo_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        silo_role_docker_device_write_iops:
        ```

    ??? variable list "`silo_role_docker_devices`"

        ```yaml
        # Type: list
        silo_role_docker_devices:
        ```

    ??? variable list "`silo_role_docker_groups`"

        ```yaml
        # Type: list
        silo_role_docker_groups:
        ```

    ??? variable bool "`silo_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_privileged:
        ```

    ??? variable list "`silo_role_docker_security_opts`"

        ```yaml
        # Type: list
        silo_role_docker_security_opts:
        ```

    ??? variable string "`silo_role_docker_userns_mode`"

        ```yaml
        # Type: string
        silo_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`silo_role_docker_dns_opts`"

        ```yaml
        # Type: list
        silo_role_docker_dns_opts:
        ```

    ??? variable list "`silo_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        silo_role_docker_dns_search_domains:
        ```

    ??? variable list "`silo_role_docker_dns_servers`"

        ```yaml
        # Type: list
        silo_role_docker_dns_servers:
        ```

    ??? variable string "`silo_role_docker_domainname`"

        ```yaml
        # Type: string
        silo_role_docker_domainname:
        ```

    ??? variable list "`silo_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        silo_role_docker_exposed_ports:
        ```

    ??? variable dict "`silo_role_docker_hosts`"

        ```yaml
        # Type: dict
        silo_role_docker_hosts:
        ```

    ??? variable bool "`silo_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_hosts_use_common:
        ```

    ??? variable string "`silo_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        silo_role_docker_ipc_mode:
        ```

    ??? variable list "`silo_role_docker_links`"

        ```yaml
        # Type: list
        silo_role_docker_links:
        ```

    ??? variable string "`silo_role_docker_network_mode`"

        ```yaml
        # Type: string
        silo_role_docker_network_mode:
        ```

    ??? variable string "`silo_role_docker_pid_mode`"

        ```yaml
        # Type: string
        silo_role_docker_pid_mode:
        ```

    ??? variable list "`silo_role_docker_ports`"

        ```yaml
        # Type: list
        silo_role_docker_ports:
        ```

    ??? variable string "`silo_role_docker_uts`"

        ```yaml
        # Type: string
        silo_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`silo_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_keep_volumes:
        ```

    ??? variable list "`silo_role_docker_mounts`"

        ```yaml
        # Type: list
        silo_role_docker_mounts:
        ```

    ??? variable dict "`silo_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        silo_role_docker_storage_opts:
        ```

    ??? variable list "`silo_role_docker_tmpfs`"

        ```yaml
        # Type: list
        silo_role_docker_tmpfs:
        ```

    ??? variable string "`silo_role_docker_volume_driver`"

        ```yaml
        # Type: string
        silo_role_docker_volume_driver:
        ```

    ??? variable list "`silo_role_docker_volumes_from`"

        ```yaml
        # Type: list
        silo_role_docker_volumes_from:
        ```

    ??? variable bool "`silo_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_volumes_global:
        ```

    ??? variable string "`silo_role_docker_working_dir`"

        ```yaml
        # Type: string
        silo_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`silo_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_auto_remove:
        ```

    ??? variable bool "`silo_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_cleanup:
        ```

    ??? variable string "`silo_role_docker_force_kill`"

        ```yaml
        # Type: string
        silo_role_docker_force_kill:
        ```

    ??? variable dict "`silo_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        silo_role_docker_healthcheck:
        ```

    ??? variable int "`silo_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        silo_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`silo_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_init:
        ```

    ??? variable string "`silo_role_docker_kill_signal`"

        ```yaml
        # Type: string
        silo_role_docker_kill_signal:
        ```

    ??? variable string "`silo_role_docker_log_driver`"

        ```yaml
        # Type: string
        silo_role_docker_log_driver:
        ```

    ??? variable dict "`silo_role_docker_log_options`"

        ```yaml
        # Type: dict
        silo_role_docker_log_options:
        ```

    ??? variable bool "`silo_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_oom_killer:
        ```

    ??? variable int "`silo_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        silo_role_docker_oom_score_adj:
        ```

    ??? variable bool "`silo_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_output_logs:
        ```

    ??? variable bool "`silo_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_paused:
        ```

    ??? variable bool "`silo_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_recreate:
        ```

    ??? variable int "`silo_role_docker_restart_retries`"

        ```yaml
        # Type: int
        silo_role_docker_restart_retries:
        ```

    ??? variable string "`silo_role_docker_stop_signal`"

        ```yaml
        # Type: string
        silo_role_docker_stop_signal:
        ```

    ??? variable int "`silo_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        silo_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`silo_role_docker_capabilities`"

        ```yaml
        # Type: list
        silo_role_docker_capabilities:
        ```

    ??? variable string "`silo_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        silo_role_docker_cgroup_parent:
        ```

    ??? variable list "`silo_role_docker_commands`"

        ```yaml
        # Type: list
        silo_role_docker_commands:
        ```

    ??? variable int "`silo_role_docker_create_timeout`"

        ```yaml
        # Type: int
        silo_role_docker_create_timeout:
        ```

    ??? variable string "`silo_role_docker_entrypoint`"

        ```yaml
        # Type: string
        silo_role_docker_entrypoint:
        ```

    ??? variable string "`silo_role_docker_env_file`"

        ```yaml
        # Type: string
        silo_role_docker_env_file:
        ```

    ??? variable bool "`silo_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_labels_use_common:
        ```

    ??? variable bool "`silo_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_read_only:
        ```

    ??? variable string "`silo_role_docker_runtime`"

        ```yaml
        # Type: string
        silo_role_docker_runtime:
        ```

    ??? variable list "`silo_role_docker_sysctls`"

        ```yaml
        # Type: list
        silo_role_docker_sysctls:
        ```

    ??? variable list "`silo_role_docker_ulimits`"

        ```yaml
        # Type: list
        silo_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`silo_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        silo_role_autoheal_enabled: true
        ```

    ??? variable bool "`silo_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        silo_role_diun_enabled: true
        ```

    ??? variable bool "`silo_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        silo_role_dns_enabled: true
        ```

    ??? variable bool "`silo_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        silo_role_docker_controller: true
        ```

    ??? variable list "`silo_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        silo_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`silo_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        silo_role_docker_volumes_download:
        ```

    ??? variable string "`silo_role_themepark_addons`"

        ```yaml
        # Type: string
        silo_role_themepark_addons:
        ```

    ??? variable string "`silo_role_themepark_app`"

        ```yaml
        # Type: string
        silo_role_themepark_app:
        ```

    ??? variable string "`silo_role_themepark_theme`"

        ```yaml
        # Type: string
        silo_role_themepark_theme:
        ```

    ??? variable string "`silo_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        silo_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`silo_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        silo_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`silo_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        silo_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`silo_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        silo_role_traefik_error_pages_enabled: false
        ```

    ??? variable string "`silo_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        silo_role_traefik_middleware_http:
        ```

    ??? variable bool "`silo_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        silo_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`silo_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        silo_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`silo_role_traefik_priority`"

        ```yaml
        # Type: string
        silo_role_traefik_priority:
        ```

    ??? variable bool "`silo_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        silo_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`silo_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        silo_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`silo_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        silo_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`silo_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        silo_role_web_api_http_port:
        ```

    ??? variable string "`silo_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        silo_role_web_api_http_scheme:
        ```

    ??? variable dict "`silo_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        silo_role_web_api_http_serverstransport:
        ```

    ??? variable string "`silo_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        silo_role_web_api_port:
        ```

    ??? variable string "`silo_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        silo_role_web_api_scheme:
        ```

    ??? variable dict "`silo_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        silo_role_web_api_serverstransport:
        ```

    ??? variable list "`silo_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        silo_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            silo_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "silo2.{{ user.domain }}"
              - "silo.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`silo_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        silo_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            silo_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'silo2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`silo_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        silo_role_web_http_port:
        ```

    ??? variable string "`silo_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        silo_role_web_http_scheme:
        ```

    ??? variable dict "`silo_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        silo_role_web_http_serverstransport:
        ```

    ??? variable string "`silo_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        silo_role_web_scheme:
        ```

    ??? variable dict "`silo_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        silo_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
