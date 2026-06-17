---
icon: material/docker
status: draft2
hide:
  - tags
tags:
  - sure
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
sb install sandbox-sure
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        sure_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `sure_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `sure_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`sure_name`"

        ```yaml
        # Type: string
        sure_name: sure
        ```

=== "Settings"

    ??? variable string "`sure_role_onboarding_state`"

        ```yaml
        # Valid options: open, closed, invite_only
        # Type: string
        sure_role_onboarding_state: "open"
        ```

    ??? variable string "`sure_role_rails_force_ssl`"

        ```yaml
        # Valid options: "true", "false"
        # Type: string
        sure_role_rails_force_ssl: "false"
        ```

    ??? variable string "`sure_role_rails_assume_ssl`"

        ```yaml
        # Valid options: "true", "false"
        # Type: string
        sure_role_rails_assume_ssl: "true"
        ```

    ??? variable string "`sure_role_sidekiq_web_username`"

        ```yaml
        # Type: string
        sure_role_sidekiq_web_username: "{{ user.name }}"
        ```

    ??? variable string "`sure_role_sidekiq_web_password`"

        ```yaml
        # Type: string
        sure_role_sidekiq_web_password: "{{ user.pass }}"
        ```

    ??? variable string "`sure_role_openai_access_token`"

        ```yaml
        # Type: string
        sure_role_openai_access_token: ""
        ```

    ??? variable string "`sure_role_openai_model`"

        ```yaml
        # Type: string
        sure_role_openai_model: ""
        ```

    ??? variable string "`sure_role_openai_uri_base`"

        ```yaml
        # Type: string
        sure_role_openai_uri_base: ""
        ```

    ??? variable string "`sure_role_langfuse_host`"

        ```yaml
        # Type: string
        sure_role_langfuse_host: "https://cloud.langfuse.com"
        ```

    ??? variable string "`sure_role_langfuse_public_key`"

        ```yaml
        # Type: string
        sure_role_langfuse_public_key: ""
        ```

    ??? variable string "`sure_role_langfuse_secret_key`"

        ```yaml
        # Type: string
        sure_role_langfuse_secret_key: ""
        ```

    ??? variable string "`sure_role_twelve_data_api_key`"

        ```yaml
        # Type: string
        sure_role_twelve_data_api_key: ""
        ```

    ??? variable string "`sure_role_exchange_rate_provider`"

        ```yaml
        # Valid options: twelve_data, yahoo_finance
        # Type: string
        sure_role_exchange_rate_provider: "yahoo_finance"
        ```

    ??? variable string "`sure_role_securities_provider`"

        ```yaml
        # Valid options: twelve_data, yahoo_finance
        # Type: string
        sure_role_securities_provider: "yahoo_finance"
        ```

    ??? variable string "`sure_role_smtp_address`"

        ```yaml
        # Type: string
        sure_role_smtp_address: ""
        ```

    ??? variable string "`sure_role_smtp_port`"

        ```yaml
        # Type: string
        sure_role_smtp_port: ""
        ```

    ??? variable string "`sure_role_smtp_username`"

        ```yaml
        # Type: string
        sure_role_smtp_username: ""
        ```

    ??? variable string "`sure_role_smtp_password`"

        ```yaml
        # Type: string
        sure_role_smtp_password: ""
        ```

    ??? variable string "`sure_role_smtp_tls_enabled`"

        ```yaml
        # Valid options: "true", "false"
        # Type: string
        sure_role_smtp_tls_enabled: "true"
        ```

    ??? variable string "`sure_role_email_sender`"

        ```yaml
        # Type: string
        sure_role_email_sender: ""
        ```

=== "Redis"

    ??? variable string "`sure_role_redis_name`"

        ```yaml
        # Type: string
        sure_role_redis_name: "{{ sure_name }}-redis"
        ```

    ??? variable string "`sure_role_redis_docker_image_tag`"

        ```yaml
        # Type: string
        sure_role_redis_docker_image_tag: "8-alpine"
        ```

    ??? variable string "`sure_role_redis_paths_folder`"

        ```yaml
        # Type: string
        sure_role_redis_paths_folder: "{{ sure_name }}"
        ```

    ??? variable string "`sure_role_redis_paths_location`"

        ```yaml
        # Type: string
        sure_role_redis_paths_location: "{{ server_appdata_path }}/{{ sure_role_redis_paths_folder }}/redis"
        ```

=== "Postgres"

    ??? variable bool "`sure_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        sure_role_postgres_deploy: true
        ```

    ??? variable string "`sure_role_postgres_name`"

        ```yaml
        # Type: string
        sure_role_postgres_name: "{{ sure_name }}-postgres"
        ```

    ??? variable string "`sure_role_postgres_user`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        sure_role_postgres_user: ""
        ```

    ??? variable string "`sure_role_postgres_password`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        sure_role_postgres_password: ""
        ```

    ??? variable string "`sure_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        sure_role_postgres_docker_env_db: "{{ sure_name }}_production"
        ```

    ??? variable string "`sure_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        sure_role_postgres_docker_image_tag: "16"
        ```

    ??? variable string "`sure_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        sure_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`sure_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        sure_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='sure') }} -U {{ lookup('role_var', '_postgres_user', role='sure') if (lookup('role_var', '_postgres_user', role='sure') | length > 0) else lookup('role_var', '_docker_env_user', role='postgres') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`sure_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        sure_role_postgres_paths_folder: "{{ sure_name }}"
        ```

    ??? variable string "`sure_role_postgres_paths_location`"

        ```yaml
        # Type: string
        sure_role_postgres_paths_location: "{{ server_appdata_path }}/{{ sure_role_postgres_paths_folder }}/postgres"
        ```

=== "Web"

    ??? variable string "`sure_role_web_subdomain`"

        ```yaml
        # Type: string
        sure_role_web_subdomain: "{{ sure_name }}"
        ```

    ??? variable string "`sure_role_web_domain`"

        ```yaml
        # Type: string
        sure_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`sure_role_web_port`"

        ```yaml
        # Type: string
        sure_role_web_port: "3000"
        ```

    ??? variable string "`sure_role_web_url`"

        ```yaml
        # Type: string
        sure_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sure') + '.' + lookup('role_var', '_web_domain', role='sure')
                            if (lookup('role_var', '_web_subdomain', role='sure') | length > 0)
                            else lookup('role_var', '_web_domain', role='sure')) }}"
        ```

    ??? variable string "`sure_role_web_host`"

        ```yaml
        # Type: string
        sure_role_web_host: "{{ (lookup('role_var', '_web_subdomain', role='sure') + '.' + lookup('role_var', '_web_domain', role='sure')
                             if (lookup('role_var', '_web_subdomain', role='sure') | length > 0)
                             else lookup('role_var', '_web_domain', role='sure')) }}"
        ```

=== "DNS"

    ??? variable string "`sure_role_dns_record`"

        ```yaml
        # Type: string
        sure_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sure') }}"
        ```

    ??? variable string "`sure_role_dns_zone`"

        ```yaml
        # Type: string
        sure_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sure') }}"
        ```

    ??? variable bool "`sure_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        sure_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`sure_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        sure_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`sure_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        sure_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`sure_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        sure_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`sure_role_traefik_certresolver`"

        ```yaml
        # Type: string
        sure_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`sure_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        sure_role_traefik_enabled: true
        ```

    ??? variable bool "`sure_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        sure_role_traefik_api_enabled: false
        ```

    ??? variable string "`sure_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        sure_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`sure_role_docker_container`"

        ```yaml
        # Type: string
        sure_role_docker_container: "{{ sure_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`sure_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_image_pull: true
        ```

    ??? variable string "`sure_role_docker_image_repo`"

        ```yaml
        # Type: string
        sure_role_docker_image_repo: "ghcr.io/we-promise/sure"
        ```

    <h5>Valid options in Sure docs: latest, stable</h5>

    ??? variable string "`sure_role_docker_image_tag`"

        ```yaml
        # Type: string
        sure_role_docker_image_tag: "stable"
        ```

    ??? variable string "`sure_role_docker_image`"

        ```yaml
        # Type: string
        sure_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sure') }}:{{ lookup('role_var', '_docker_image_tag', role='sure') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`sure_role_docker_envs_default`"

        ```yaml
        # Type: dict
        sure_role_docker_envs_default:
          TZ: "{{ tz }}"
          PORT: "{{ lookup('role_var', '_web_port', role='sure') }}"
          SELF_HOSTED: "true"
          ONBOARDING_STATE: "{{ lookup('role_var', '_onboarding_state', role='sure') }}"
          SECRET_KEY_BASE: "{{ sure_saltbox_facts.facts.secret_key }}"
          RAILS_FORCE_SSL: "{{ lookup('role_var', '_rails_force_ssl', role='sure') }}"
          RAILS_ASSUME_SSL: "{{ lookup('role_var', '_rails_assume_ssl', role='sure') }}"
          APP_DOMAIN: "{{ lookup('role_var', '_web_host', role='sure') }}"
          DB_HOST: "{{ lookup('role_var', '_postgres_name', role='sure') }}"
          DB_PORT: "5432"
          POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='sure')
                          if (lookup('role_var', '_postgres_user', role='sure') | length > 0)
                          else lookup('role_var', '_docker_env_user', role='postgres') }}"
          POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='sure')
                              if (lookup('role_var', '_postgres_password', role='sure') | length > 0)
                              else lookup('role_var', '_docker_env_password', role='postgres') }}"
          POSTGRES_DB: "{{ lookup('role_var', '_postgres_docker_env_db', role='sure') }}"
          REDIS_URL: "redis://{{ lookup('role_var', '_redis_name', role='sure') }}:6379/1"
          SIDEKIQ_WEB_USERNAME: "{{ lookup('role_var', '_sidekiq_web_username', role='sure') }}"
          SIDEKIQ_WEB_PASSWORD: "{{ lookup('role_var', '_sidekiq_web_password', role='sure') }}"
          OPENAI_ACCESS_TOKEN: "{{ lookup('role_var', '_openai_access_token', role='sure')
                                if (lookup('role_var', '_openai_access_token', role='sure') | length > 0)
                                else omit }}"
          OPENAI_MODEL: "{{ lookup('role_var', '_openai_model', role='sure')
                         if (lookup('role_var', '_openai_model', role='sure') | length > 0)
                         else omit }}"
          OPENAI_URI_BASE: "{{ lookup('role_var', '_openai_uri_base', role='sure')
                            if (lookup('role_var', '_openai_uri_base', role='sure') | length > 0)
                            else omit }}"
          LANGFUSE_HOST: "{{ lookup('role_var', '_langfuse_host', role='sure') }}"
          LANGFUSE_PUBLIC_KEY: "{{ lookup('role_var', '_langfuse_public_key', role='sure')
                                if (lookup('role_var', '_langfuse_public_key', role='sure') | length > 0)
                                else omit }}"
          LANGFUSE_SECRET_KEY: "{{ lookup('role_var', '_langfuse_secret_key', role='sure')
                                if (lookup('role_var', '_langfuse_secret_key', role='sure') | length > 0)
                                else omit }}"
          TWELVE_DATA_API_KEY: "{{ lookup('role_var', '_twelve_data_api_key', role='sure')
                                if (lookup('role_var', '_twelve_data_api_key', role='sure') | length > 0)
                                else omit }}"
          EXCHANGE_RATE_PROVIDER: "{{ lookup('role_var', '_exchange_rate_provider', role='sure') }}"
          SECURITIES_PROVIDER: "{{ lookup('role_var', '_securities_provider', role='sure') }}"
          SMTP_ADDRESS: "{{ lookup('role_var', '_smtp_address', role='sure')
                         if (lookup('role_var', '_smtp_address', role='sure') | length > 0)
                         else omit }}"
          SMTP_PORT: "{{ lookup('role_var', '_smtp_port', role='sure')
                      if (lookup('role_var', '_smtp_address', role='sure') | length > 0)
                      else omit }}"
          SMTP_USERNAME: "{{ lookup('role_var', '_smtp_username', role='sure')
                          if (lookup('role_var', '_smtp_address', role='sure') | length > 0)
                          else omit }}"
          SMTP_PASSWORD: "{{ lookup('role_var', '_smtp_password', role='sure')
                          if (lookup('role_var', '_smtp_address', role='sure') | length > 0)
                          else omit }}"
          SMTP_TLS_ENABLED: "{{ lookup('role_var', '_smtp_tls_enabled', role='sure')
                             if (lookup('role_var', '_smtp_address', role='sure') | length > 0)
                             else omit }}"
          EMAIL_SENDER: "{{ lookup('role_var', '_email_sender', role='sure')
                         if (lookup('role_var', '_email_sender', role='sure') | length > 0)
                         else omit }}"
        ```

    ??? variable dict "`sure_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        sure_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`sure_role_docker_volumes_default`"

        ```yaml
        # Type: list
        sure_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='sure') }}/storage:/rails/storage"
        ```

    ??? variable list "`sure_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        sure_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`sure_role_docker_hostname`"

        ```yaml
        # Type: string
        sure_role_docker_hostname: "{{ sure_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`sure_role_docker_networks_alias`"

        ```yaml
        # Type: string
        sure_role_docker_networks_alias: "{{ sure_name }}"
        ```

    ??? variable list "`sure_role_docker_networks_default`"

        ```yaml
        # Type: list
        sure_role_docker_networks_default: []
        ```

    ??? variable list "`sure_role_docker_networks_custom`"

        ```yaml
        # Type: list
        sure_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`sure_role_docker_restart_policy`"

        ```yaml
        # Type: string
        sure_role_docker_restart_policy: unless-stopped
        ```

=== "Dependencies"

    ??? variable string "`sure_role_depends_on`"

        ```yaml
        # Type: string
        sure_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='sure') }},{{ lookup('role_var', '_redis_name', role='sure') }}"
        ```

    ??? variable string "`sure_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        sure_role_depends_on_delay: "0"
        ```

    ??? variable string "`sure_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        sure_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`sure_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        sure_role_docker_blkio_weight:
        ```

    ??? variable int "`sure_role_docker_cpu_period`"

        ```yaml
        # Type: int
        sure_role_docker_cpu_period:
        ```

    ??? variable int "`sure_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        sure_role_docker_cpu_quota:
        ```

    ??? variable int "`sure_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        sure_role_docker_cpu_shares:
        ```

    ??? variable string "`sure_role_docker_cpus`"

        ```yaml
        # Type: string
        sure_role_docker_cpus:
        ```

    ??? variable string "`sure_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        sure_role_docker_cpuset_cpus:
        ```

    ??? variable string "`sure_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        sure_role_docker_cpuset_mems:
        ```

    ??? variable string "`sure_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        sure_role_docker_kernel_memory:
        ```

    ??? variable string "`sure_role_docker_memory`"

        ```yaml
        # Type: string
        sure_role_docker_memory:
        ```

    ??? variable string "`sure_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        sure_role_docker_memory_reservation:
        ```

    ??? variable string "`sure_role_docker_memory_swap`"

        ```yaml
        # Type: string
        sure_role_docker_memory_swap:
        ```

    ??? variable int "`sure_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        sure_role_docker_memory_swappiness:
        ```

    ??? variable string "`sure_role_docker_shm_size`"

        ```yaml
        # Type: string
        sure_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`sure_role_docker_cap_drop`"

        ```yaml
        # Type: list
        sure_role_docker_cap_drop:
        ```

    ??? variable string "`sure_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        sure_role_docker_cgroupns_mode:
        ```

    ??? variable list "`sure_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        sure_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`sure_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        sure_role_docker_device_read_bps:
        ```

    ??? variable list "`sure_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        sure_role_docker_device_read_iops:
        ```

    ??? variable list "`sure_role_docker_device_requests`"

        ```yaml
        # Type: list
        sure_role_docker_device_requests:
        ```

    ??? variable list "`sure_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        sure_role_docker_device_write_bps:
        ```

    ??? variable list "`sure_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        sure_role_docker_device_write_iops:
        ```

    ??? variable list "`sure_role_docker_devices`"

        ```yaml
        # Type: list
        sure_role_docker_devices:
        ```

    ??? variable list "`sure_role_docker_groups`"

        ```yaml
        # Type: list
        sure_role_docker_groups:
        ```

    ??? variable bool "`sure_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_privileged:
        ```

    ??? variable list "`sure_role_docker_security_opts`"

        ```yaml
        # Type: list
        sure_role_docker_security_opts:
        ```

    ??? variable string "`sure_role_docker_user`"

        ```yaml
        # Type: string
        sure_role_docker_user:
        ```

    ??? variable string "`sure_role_docker_userns_mode`"

        ```yaml
        # Type: string
        sure_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`sure_role_docker_dns_opts`"

        ```yaml
        # Type: list
        sure_role_docker_dns_opts:
        ```

    ??? variable list "`sure_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        sure_role_docker_dns_search_domains:
        ```

    ??? variable list "`sure_role_docker_dns_servers`"

        ```yaml
        # Type: list
        sure_role_docker_dns_servers:
        ```

    ??? variable string "`sure_role_docker_domainname`"

        ```yaml
        # Type: string
        sure_role_docker_domainname:
        ```

    ??? variable list "`sure_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        sure_role_docker_exposed_ports:
        ```

    ??? variable dict "`sure_role_docker_hosts`"

        ```yaml
        # Type: dict
        sure_role_docker_hosts:
        ```

    ??? variable bool "`sure_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_hosts_use_common:
        ```

    ??? variable string "`sure_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        sure_role_docker_ipc_mode:
        ```

    ??? variable list "`sure_role_docker_links`"

        ```yaml
        # Type: list
        sure_role_docker_links:
        ```

    ??? variable string "`sure_role_docker_network_mode`"

        ```yaml
        # Type: string
        sure_role_docker_network_mode:
        ```

    ??? variable string "`sure_role_docker_pid_mode`"

        ```yaml
        # Type: string
        sure_role_docker_pid_mode:
        ```

    ??? variable list "`sure_role_docker_ports`"

        ```yaml
        # Type: list
        sure_role_docker_ports:
        ```

    ??? variable string "`sure_role_docker_uts`"

        ```yaml
        # Type: string
        sure_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`sure_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_keep_volumes:
        ```

    ??? variable list "`sure_role_docker_mounts`"

        ```yaml
        # Type: list
        sure_role_docker_mounts:
        ```

    ??? variable dict "`sure_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        sure_role_docker_storage_opts:
        ```

    ??? variable list "`sure_role_docker_tmpfs`"

        ```yaml
        # Type: list
        sure_role_docker_tmpfs:
        ```

    ??? variable string "`sure_role_docker_volume_driver`"

        ```yaml
        # Type: string
        sure_role_docker_volume_driver:
        ```

    ??? variable list "`sure_role_docker_volumes_from`"

        ```yaml
        # Type: list
        sure_role_docker_volumes_from:
        ```

    ??? variable bool "`sure_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_volumes_global:
        ```

    ??? variable string "`sure_role_docker_working_dir`"

        ```yaml
        # Type: string
        sure_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`sure_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_auto_remove:
        ```

    ??? variable bool "`sure_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_cleanup:
        ```

    ??? variable string "`sure_role_docker_force_kill`"

        ```yaml
        # Type: string
        sure_role_docker_force_kill:
        ```

    ??? variable dict "`sure_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        sure_role_docker_healthcheck:
        ```

    ??? variable int "`sure_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        sure_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`sure_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_init:
        ```

    ??? variable string "`sure_role_docker_kill_signal`"

        ```yaml
        # Type: string
        sure_role_docker_kill_signal:
        ```

    ??? variable string "`sure_role_docker_log_driver`"

        ```yaml
        # Type: string
        sure_role_docker_log_driver:
        ```

    ??? variable dict "`sure_role_docker_log_options`"

        ```yaml
        # Type: dict
        sure_role_docker_log_options:
        ```

    ??? variable bool "`sure_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_oom_killer:
        ```

    ??? variable int "`sure_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        sure_role_docker_oom_score_adj:
        ```

    ??? variable bool "`sure_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_output_logs:
        ```

    ??? variable bool "`sure_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_paused:
        ```

    ??? variable bool "`sure_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_recreate:
        ```

    ??? variable int "`sure_role_docker_restart_retries`"

        ```yaml
        # Type: int
        sure_role_docker_restart_retries:
        ```

    ??? variable string "`sure_role_docker_stop_signal`"

        ```yaml
        # Type: string
        sure_role_docker_stop_signal:
        ```

    ??? variable int "`sure_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        sure_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`sure_role_docker_capabilities`"

        ```yaml
        # Type: list
        sure_role_docker_capabilities:
        ```

    ??? variable string "`sure_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        sure_role_docker_cgroup_parent:
        ```

    ??? variable list "`sure_role_docker_commands`"

        ```yaml
        # Type: list
        sure_role_docker_commands:
        ```

    ??? variable int "`sure_role_docker_create_timeout`"

        ```yaml
        # Type: int
        sure_role_docker_create_timeout:
        ```

    ??? variable string "`sure_role_docker_entrypoint`"

        ```yaml
        # Type: string
        sure_role_docker_entrypoint:
        ```

    ??? variable string "`sure_role_docker_env_file`"

        ```yaml
        # Type: string
        sure_role_docker_env_file:
        ```

    ??? variable dict "`sure_role_docker_labels`"

        ```yaml
        # Type: dict
        sure_role_docker_labels:
        ```

    ??? variable bool "`sure_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_labels_use_common:
        ```

    ??? variable bool "`sure_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_read_only:
        ```

    ??? variable string "`sure_role_docker_runtime`"

        ```yaml
        # Type: string
        sure_role_docker_runtime:
        ```

    ??? variable list "`sure_role_docker_sysctls`"

        ```yaml
        # Type: list
        sure_role_docker_sysctls:
        ```

    ??? variable list "`sure_role_docker_ulimits`"

        ```yaml
        # Type: list
        sure_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`sure_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        sure_role_autoheal_enabled: true
        ```

    ??? variable bool "`sure_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        sure_role_diun_enabled: true
        ```

    ??? variable bool "`sure_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        sure_role_dns_enabled: true
        ```

    ??? variable bool "`sure_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        sure_role_docker_controller: true
        ```

    ??? variable list "`sure_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        sure_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`sure_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        sure_role_docker_volumes_download:
        ```

    ??? variable string "`sure_role_themepark_addons`"

        ```yaml
        # Type: string
        sure_role_themepark_addons:
        ```

    ??? variable string "`sure_role_themepark_app`"

        ```yaml
        # Type: string
        sure_role_themepark_app:
        ```

    ??? variable string "`sure_role_themepark_theme`"

        ```yaml
        # Type: string
        sure_role_themepark_theme:
        ```

    ??? variable string "`sure_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        sure_role_traefik_api_middleware:
        ```

    ??? variable string "`sure_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        sure_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`sure_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        sure_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`sure_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        sure_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`sure_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        sure_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`sure_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        sure_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`sure_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        sure_role_traefik_middleware_http:
        ```

    ??? variable bool "`sure_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        sure_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`sure_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        sure_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`sure_role_traefik_priority`"

        ```yaml
        # Type: string
        sure_role_traefik_priority:
        ```

    ??? variable bool "`sure_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        sure_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`sure_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        sure_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`sure_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        sure_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`sure_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        sure_role_web_api_http_port:
        ```

    ??? variable string "`sure_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        sure_role_web_api_http_scheme:
        ```

    ??? variable dict "`sure_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        sure_role_web_api_http_serverstransport:
        ```

    ??? variable string "`sure_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        sure_role_web_api_port:
        ```

    ??? variable string "`sure_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        sure_role_web_api_scheme:
        ```

    ??? variable dict "`sure_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        sure_role_web_api_serverstransport:
        ```

    ??? variable list "`sure_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        sure_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            sure_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "sure2.{{ user.domain }}"
              - "sure.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`sure_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        sure_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            sure_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sure2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`sure_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        sure_role_web_http_port:
        ```

    ??? variable string "`sure_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        sure_role_web_http_scheme:
        ```

    ??? variable dict "`sure_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        sure_role_web_http_serverstransport:
        ```

    ??? variable string "`sure_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        sure_role_web_scheme:
        ```

    ??? variable dict "`sure_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        sure_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
