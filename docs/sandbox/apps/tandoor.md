---
icon: material/docker
hide:
  - tags
tags:
  - tandoor
  - recipes
  - planning
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
      url: https://docs.tandoor.dev
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/vabene1111/recipes/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Tandoor Recipes
    summary: |
      an application for managing recipes, planning meals, building shopping lists and much, much more!.
    link: https://github.com/TandoorRecipes/recipes
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Tandoor Recipes

## Overview

[Tandoor Recipes](https://github.com/TandoorRecipes/recipes) is an application for managing recipes, planning meals, building shopping lists and much, much more!.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.tandoor.dev){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/vabene1111/recipes/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

???+ warning "Migration Required for Existing Users"

    As of _role-refactor_, this role has been updated to use its own dedicated PostgreSQL database container instead of the shared `postgres` container. Once upgraded to role-refactor, existing users must follow the migration steps below to preserve their data.

    1.  Stop the containers:

        === "If additional apps use the `postgres` container"

            Be aware that this will cause the additional apps to go offline temporarily.

            ```shell
            docker stop tandoor postgres
            ```

        === "If Tandoor alone uses the `postgres` container"

            ```shell
            docker stop tandoor postgres
            docker rm postgres
            ```

    1.  Copy or rename the existing Postgres directory:

        === "If additional apps use the `postgres` container"

            ```shell
            cp -r /opt/postgres /opt/tandoor-postgres
            docker start postgres
            ```

        === "If Tandoor alone uses the `postgres` container"

            ```shell
            mv /opt/postgres /opt/tandoor-postgres
            ```

    1.  [Deploy Tandoor :material-arrow-down-bold:](#deployment)

## Deployment

```shell
sb install sandbox-tandoor
```

## Usage

Visit <https://tandoor.iYOUR_DOMAIN_NAMEi>.

## Basics

### Adding An Admin User

1.  Execute a shell in the container using `docker exec -it tandoor sh`,

1.  activate the virtual environment `source venv/bin/activate`,

1.  run `python manage.py createsuperuser` and follow the steps shown.

### Password Reset

1.  Execute a shell in the container using `docker exec -it tandoor sh`,

1.  activate the virtual environment `source venv/bin/activate`,

1.  run `python manage.py changepassword <username>` and follow the steps shown.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        tandoor_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `tandoor_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `tandoor_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tandoor_name`"

        ```yaml
        # Type: string
        tandoor_name: tandoor
        ```

=== "Settings"

    ??? variable bool "`tandoor_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_postgres_deploy: true
        ```

    ??? variable string "`tandoor_role_postgres_name`"

        ```yaml
        # Type: string
        tandoor_role_postgres_name: "{{ tandoor_name }}-postgres"
        ```

    ??? variable string "`tandoor_role_postgres_user`"

        ```yaml
        # Type: string
        tandoor_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`tandoor_role_postgres_password`"

        ```yaml
        # Type: string
        tandoor_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`tandoor_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        tandoor_role_postgres_docker_env_db: "{{ tandoor_name }}"
        ```

    ??? variable string "`tandoor_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        tandoor_role_postgres_docker_image_tag: "17-alpine"
        ```

    ??? variable string "`tandoor_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        tandoor_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`tandoor_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        tandoor_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='tandoor') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`tandoor_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        tandoor_role_postgres_paths_folder: "{{ tandoor_name }}"
        ```

    ??? variable string "`tandoor_role_postgres_paths_location`"

        ```yaml
        # Type: string
        tandoor_role_postgres_paths_location: "{{ server_appdata_path }}/{{ tandoor_role_postgres_paths_folder }}/postgres"
        ```

=== "Web"

    ??? variable string "`tandoor_role_web_subdomain`"

        ```yaml
        # Type: string
        tandoor_role_web_subdomain: "{{ tandoor_name }}"
        ```

    ??? variable string "`tandoor_role_web_domain`"

        ```yaml
        # Type: string
        tandoor_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tandoor_role_web_port`"

        ```yaml
        # Type: string
        tandoor_role_web_port: "80"
        ```

    ??? variable string "`tandoor_role_web_url`"

        ```yaml
        # Type: string
        tandoor_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tandoor') + '.' + lookup('role_var', '_web_domain', role='tandoor')
                               if (lookup('role_var', '_web_subdomain', role='tandoor') | length > 0)
                               else lookup('role_var', '_web_domain', role='tandoor')) }}"
        ```

=== "DNS"

    ??? variable string "`tandoor_role_dns_record`"

        ```yaml
        # Type: string
        tandoor_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tandoor') }}"
        ```

    ??? variable string "`tandoor_role_dns_zone`"

        ```yaml
        # Type: string
        tandoor_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tandoor') }}"
        ```

    ??? variable bool "`tandoor_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tandoor_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tandoor_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`tandoor_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tandoor_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tandoor_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tandoor_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tandoor_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tandoor_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tandoor_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_enabled: true
        ```

    ??? variable bool "`tandoor_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_api_enabled: false
        ```

    ??? variable string "`tandoor_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tandoor_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`tandoor_role_docker_container`"

        ```yaml
        # Type: string
        tandoor_role_docker_container: "{{ tandoor_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`tandoor_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_image_pull: true
        ```

    ??? variable string "`tandoor_role_docker_image_tag`"

        ```yaml
        # Type: string
        tandoor_role_docker_image_tag: "latest"
        ```

    ??? variable string "`tandoor_role_docker_image_repo`"

        ```yaml
        # Type: string
        tandoor_role_docker_image_repo: "vabene1111/recipes"
        ```

    ??? variable string "`tandoor_role_docker_image`"

        ```yaml
        # Type: string
        tandoor_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tandoor') }}:{{ lookup('role_var', '_docker_image_tag', role='tandoor') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`tandoor_role_docker_envs_default`"

        ```yaml
        # Type: dict
        tandoor_role_docker_envs_default:
          TZ: "{{ tz }}"
          SECRET_KEY: "{{ tandoor_saltbox_facts.facts.secret_key }}"
          DB_ENGINE: "django.db.backends.postgresql"
          POSTGRES_HOST: "{{ lookup('role_var', '_postgres_name', role='tandoor') }}"
          POSTGRES_PORT: "5432"
          POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='tandoor') }}"
          POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='tandoor') }}"
          POSTGRES_DB: "{{ lookup('role_var', '_postgres_docker_env_db', role='tandoor') }}"
          DEBUG: "0"
          GUNICORN_MEDIA: "1"
          REMOTE_USER_AUTH: "1"
        ```

    ??? variable dict "`tandoor_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tandoor_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`tandoor_role_docker_volumes_default`"

        ```yaml
        # Type: list
        tandoor_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='tandoor') }}/staticfiles:/opt/recipes/staticfiles"
          - "{{ lookup('role_var', '_paths_location', role='tandoor') }}/mediafiles:/opt/recipes/mediafiles"
        ```

    ??? variable list "`tandoor_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tandoor_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`tandoor_role_docker_hostname`"

        ```yaml
        # Type: string
        tandoor_role_docker_hostname: "{{ tandoor_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`tandoor_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tandoor_role_docker_networks_alias: "{{ tandoor_name }}"
        ```

    ??? variable list "`tandoor_role_docker_networks_default`"

        ```yaml
        # Type: list
        tandoor_role_docker_networks_default: []
        ```

    ??? variable list "`tandoor_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tandoor_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`tandoor_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tandoor_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`tandoor_role_docker_state`"

        ```yaml
        # Type: string
        tandoor_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`tandoor_role_depends_on`"

        ```yaml
        # Type: string
        tandoor_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='tandoor') }}"
        ```

    ??? variable string "`tandoor_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        tandoor_role_depends_on_delay: "0"
        ```

    ??? variable string "`tandoor_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        tandoor_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`tandoor_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        tandoor_role_docker_blkio_weight:
        ```

    ??? variable int "`tandoor_role_docker_cpu_period`"

        ```yaml
        # Type: int
        tandoor_role_docker_cpu_period:
        ```

    ??? variable int "`tandoor_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        tandoor_role_docker_cpu_quota:
        ```

    ??? variable int "`tandoor_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        tandoor_role_docker_cpu_shares:
        ```

    ??? variable string "`tandoor_role_docker_cpus`"

        ```yaml
        # Type: string
        tandoor_role_docker_cpus:
        ```

    ??? variable string "`tandoor_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        tandoor_role_docker_cpuset_cpus:
        ```

    ??? variable string "`tandoor_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        tandoor_role_docker_cpuset_mems:
        ```

    ??? variable string "`tandoor_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        tandoor_role_docker_kernel_memory:
        ```

    ??? variable string "`tandoor_role_docker_memory`"

        ```yaml
        # Type: string
        tandoor_role_docker_memory:
        ```

    ??? variable string "`tandoor_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        tandoor_role_docker_memory_reservation:
        ```

    ??? variable string "`tandoor_role_docker_memory_swap`"

        ```yaml
        # Type: string
        tandoor_role_docker_memory_swap:
        ```

    ??? variable int "`tandoor_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        tandoor_role_docker_memory_swappiness:
        ```

    ??? variable string "`tandoor_role_docker_shm_size`"

        ```yaml
        # Type: string
        tandoor_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`tandoor_role_docker_cap_drop`"

        ```yaml
        # Type: list
        tandoor_role_docker_cap_drop:
        ```

    ??? variable string "`tandoor_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        tandoor_role_docker_cgroupns_mode:
        ```

    ??? variable list "`tandoor_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        tandoor_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`tandoor_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        tandoor_role_docker_device_read_bps:
        ```

    ??? variable list "`tandoor_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        tandoor_role_docker_device_read_iops:
        ```

    ??? variable list "`tandoor_role_docker_device_requests`"

        ```yaml
        # Type: list
        tandoor_role_docker_device_requests:
        ```

    ??? variable list "`tandoor_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        tandoor_role_docker_device_write_bps:
        ```

    ??? variable list "`tandoor_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        tandoor_role_docker_device_write_iops:
        ```

    ??? variable list "`tandoor_role_docker_devices`"

        ```yaml
        # Type: list
        tandoor_role_docker_devices:
        ```

    ??? variable string "`tandoor_role_docker_devices_default`"

        ```yaml
        # Type: string
        tandoor_role_docker_devices_default:
        ```

    ??? variable list "`tandoor_role_docker_groups`"

        ```yaml
        # Type: list
        tandoor_role_docker_groups:
        ```

    ??? variable bool "`tandoor_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_privileged:
        ```

    ??? variable list "`tandoor_role_docker_security_opts`"

        ```yaml
        # Type: list
        tandoor_role_docker_security_opts:
        ```

    ??? variable string "`tandoor_role_docker_user`"

        ```yaml
        # Type: string
        tandoor_role_docker_user:
        ```

    ??? variable string "`tandoor_role_docker_userns_mode`"

        ```yaml
        # Type: string
        tandoor_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`tandoor_role_docker_dns_opts`"

        ```yaml
        # Type: list
        tandoor_role_docker_dns_opts:
        ```

    ??? variable list "`tandoor_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        tandoor_role_docker_dns_search_domains:
        ```

    ??? variable list "`tandoor_role_docker_dns_servers`"

        ```yaml
        # Type: list
        tandoor_role_docker_dns_servers:
        ```

    ??? variable string "`tandoor_role_docker_domainname`"

        ```yaml
        # Type: string
        tandoor_role_docker_domainname:
        ```

    ??? variable list "`tandoor_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        tandoor_role_docker_exposed_ports:
        ```

    ??? variable dict "`tandoor_role_docker_hosts`"

        ```yaml
        # Type: dict
        tandoor_role_docker_hosts:
        ```

    ??? variable bool "`tandoor_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_hosts_use_common:
        ```

    ??? variable string "`tandoor_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        tandoor_role_docker_ipc_mode:
        ```

    ??? variable list "`tandoor_role_docker_links`"

        ```yaml
        # Type: list
        tandoor_role_docker_links:
        ```

    ??? variable string "`tandoor_role_docker_network_mode`"

        ```yaml
        # Type: string
        tandoor_role_docker_network_mode:
        ```

    ??? variable string "`tandoor_role_docker_pid_mode`"

        ```yaml
        # Type: string
        tandoor_role_docker_pid_mode:
        ```

    ??? variable list "`tandoor_role_docker_ports`"

        ```yaml
        # Type: list
        tandoor_role_docker_ports:
        ```

    ??? variable string "`tandoor_role_docker_uts`"

        ```yaml
        # Type: string
        tandoor_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`tandoor_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_keep_volumes:
        ```

    ??? variable list "`tandoor_role_docker_mounts`"

        ```yaml
        # Type: list
        tandoor_role_docker_mounts:
        ```

    ??? variable dict "`tandoor_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        tandoor_role_docker_storage_opts:
        ```

    ??? variable list "`tandoor_role_docker_tmpfs`"

        ```yaml
        # Type: list
        tandoor_role_docker_tmpfs:
        ```

    ??? variable string "`tandoor_role_docker_volume_driver`"

        ```yaml
        # Type: string
        tandoor_role_docker_volume_driver:
        ```

    ??? variable list "`tandoor_role_docker_volumes_from`"

        ```yaml
        # Type: list
        tandoor_role_docker_volumes_from:
        ```

    ??? variable bool "`tandoor_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_volumes_global:
        ```

    ??? variable string "`tandoor_role_docker_working_dir`"

        ```yaml
        # Type: string
        tandoor_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`tandoor_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_auto_remove:
        ```

    ??? variable bool "`tandoor_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_cleanup:
        ```

    ??? variable string "`tandoor_role_docker_force_kill`"

        ```yaml
        # Type: string
        tandoor_role_docker_force_kill:
        ```

    ??? variable dict "`tandoor_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        tandoor_role_docker_healthcheck:
        ```

    ??? variable int "`tandoor_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        tandoor_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`tandoor_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_init:
        ```

    ??? variable string "`tandoor_role_docker_kill_signal`"

        ```yaml
        # Type: string
        tandoor_role_docker_kill_signal:
        ```

    ??? variable string "`tandoor_role_docker_log_driver`"

        ```yaml
        # Type: string
        tandoor_role_docker_log_driver:
        ```

    ??? variable dict "`tandoor_role_docker_log_options`"

        ```yaml
        # Type: dict
        tandoor_role_docker_log_options:
        ```

    ??? variable bool "`tandoor_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_oom_killer:
        ```

    ??? variable int "`tandoor_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        tandoor_role_docker_oom_score_adj:
        ```

    ??? variable bool "`tandoor_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_output_logs:
        ```

    ??? variable bool "`tandoor_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_paused:
        ```

    ??? variable bool "`tandoor_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_recreate:
        ```

    ??? variable int "`tandoor_role_docker_restart_retries`"

        ```yaml
        # Type: int
        tandoor_role_docker_restart_retries:
        ```

    ??? variable int "`tandoor_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        tandoor_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`tandoor_role_docker_capabilities`"

        ```yaml
        # Type: list
        tandoor_role_docker_capabilities:
        ```

    ??? variable string "`tandoor_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        tandoor_role_docker_cgroup_parent:
        ```

    ??? variable list "`tandoor_role_docker_commands`"

        ```yaml
        # Type: list
        tandoor_role_docker_commands:
        ```

    ??? variable int "`tandoor_role_docker_create_timeout`"

        ```yaml
        # Type: int
        tandoor_role_docker_create_timeout:
        ```

    ??? variable string "`tandoor_role_docker_entrypoint`"

        ```yaml
        # Type: string
        tandoor_role_docker_entrypoint:
        ```

    ??? variable string "`tandoor_role_docker_env_file`"

        ```yaml
        # Type: string
        tandoor_role_docker_env_file:
        ```

    ??? variable dict "`tandoor_role_docker_labels`"

        ```yaml
        # Type: dict
        tandoor_role_docker_labels:
        ```

    ??? variable bool "`tandoor_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_labels_use_common:
        ```

    ??? variable bool "`tandoor_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_read_only:
        ```

    ??? variable string "`tandoor_role_docker_runtime`"

        ```yaml
        # Type: string
        tandoor_role_docker_runtime:
        ```

    ??? variable list "`tandoor_role_docker_sysctls`"

        ```yaml
        # Type: list
        tandoor_role_docker_sysctls:
        ```

    ??? variable list "`tandoor_role_docker_ulimits`"

        ```yaml
        # Type: list
        tandoor_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`tandoor_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tandoor_role_autoheal_enabled: true
        ```

    ??? variable string "`tandoor_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tandoor_role_depends_on: ""
        ```

    ??? variable string "`tandoor_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tandoor_role_depends_on_delay: "0"
        ```

    ??? variable string "`tandoor_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tandoor_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tandoor_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tandoor_role_diun_enabled: true
        ```

    ??? variable bool "`tandoor_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tandoor_role_dns_enabled: true
        ```

    ??? variable bool "`tandoor_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tandoor_role_docker_controller: true
        ```

    ??? variable string "`tandoor_role_docker_image_repo`"

        ```yaml
        # Type: string
        tandoor_role_docker_image_repo:
        ```

    ??? variable string "`tandoor_role_docker_image_tag`"

        ```yaml
        # Type: string
        tandoor_role_docker_image_tag:
        ```

    ??? variable bool "`tandoor_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_volumes_download:
        ```

    ??? variable string "`tandoor_role_paths_location`"

        ```yaml
        # Type: string
        tandoor_role_paths_location:
        ```

    ??? variable string "`tandoor_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        tandoor_role_postgres_docker_env_db:
        ```

    ??? variable string "`tandoor_role_postgres_name`"

        ```yaml
        # Type: string
        tandoor_role_postgres_name:
        ```

    ??? variable string "`tandoor_role_postgres_password`"

        ```yaml
        # Type: string
        tandoor_role_postgres_password:
        ```

    ??? variable string "`tandoor_role_postgres_user`"

        ```yaml
        # Type: string
        tandoor_role_postgres_user:
        ```

    ??? variable string "`tandoor_role_themepark_addons`"

        ```yaml
        # Type: string
        tandoor_role_themepark_addons:
        ```

    ??? variable string "`tandoor_role_themepark_app`"

        ```yaml
        # Type: string
        tandoor_role_themepark_app:
        ```

    ??? variable string "`tandoor_role_themepark_theme`"

        ```yaml
        # Type: string
        tandoor_role_themepark_theme:
        ```

    ??? variable dict "`tandoor_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        tandoor_role_traefik_api_endpoint:
        ```

    ??? variable string "`tandoor_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        tandoor_role_traefik_api_middleware:
        ```

    ??? variable string "`tandoor_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        tandoor_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`tandoor_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`tandoor_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tandoor_role_traefik_certresolver:
        ```

    ??? variable bool "`tandoor_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`tandoor_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        tandoor_role_traefik_middleware_http:
        ```

    ??? variable bool "`tandoor_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tandoor_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`tandoor_role_traefik_priority`"

        ```yaml
        # Type: string
        tandoor_role_traefik_priority:
        ```

    ??? variable bool "`tandoor_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tandoor_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tandoor_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tandoor_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`tandoor_role_web_domain`"

        ```yaml
        # Type: string
        tandoor_role_web_domain:
        ```

    ??? variable list "`tandoor_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tandoor_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            tandoor_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tandoor2.{{ user.domain }}"
              - "tandoor.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`tandoor_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tandoor_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            tandoor_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tandoor2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`tandoor_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        tandoor_role_web_http_port:
        ```

    ??? variable string "`tandoor_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        tandoor_role_web_http_scheme:
        ```

    ??? variable dict "`tandoor_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        tandoor_role_web_http_serverstransport:
        ```

    ??? variable string "`tandoor_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tandoor_role_web_scheme:
        ```

    ??? variable dict "`tandoor_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        tandoor_role_web_serverstransport:
        ```

    ??? variable string "`tandoor_role_web_subdomain`"

        ```yaml
        # Type: string
        tandoor_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->