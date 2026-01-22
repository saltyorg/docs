---
icon: material/docker
title: InvoiceNinja
hide:
  - tags
tags:
  - invoiceninja
  - finance
  - invoicing
saltbox_automation:
  app_links:
    - name: Manual
      url: https://invoiceninja.github.io
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/invoiceninja/invoiceninja/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: InvoiceNinja
    summary: |-
      a self-hosted accounting system with ability to Quote & Invoice Clients, Time Billable-Tasks, Track Expenses, Get Paid.
    link: https://www.invoiceninja.com/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# InvoiceNinja

## Overview

[InvoiceNinja](https://www.invoiceninja.com/) is a self-hosted accounting system with ability to Quote & Invoice Clients, Time Billable-Tasks, Track Expenses, Get Paid.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://invoiceninja.github.io){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/invoiceninja/invoiceninja/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Ideally you should set a unique app key in settings.yml.
Generate the key using:

```shell
docker run --rm -it invoiceninja/invoiceninja php artisan key:generate --show
```

insert this in the invoiceninja.app_key setting in `/opt/sandbox/settings.yml`

```shell
sb install sandbox-invoiceninja
```

## Usage

Visit <https://invoiceninja.iYOUR_DOMAIN_NAMEi>.

### Log in

Enter email, and password from accounts.yml setting.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        invoiceninjav5_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `invoiceninjav5_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `invoiceninjav5_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`invoiceninjav5_name`"

        ```yaml
        # Type: string
        invoiceninjav5_name: "invoiceninja"
        ```

=== "Settings"

    ??? variable bool "`invoiceninjav5_overwrite_nginx_config`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_overwrite_nginx_config: true
        ```

    ??? variable string "`invoiceninjav5_role_app_key`"

        ```yaml
        # Type: string
        invoiceninjav5_role_app_key: "base64:O1S3kAJEDgo92gPkXtxfdCJpoGShgKloUSdcaHMXmoY="
        ```

=== "Web"

    ??? variable string "`invoiceninjav5_role_nginx_web_subdomain`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_subdomain: "invoiceninja"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_web_domain`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_web_port`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_port: "80"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_web_url`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_url: "{{ 'https://' + (lookup('role_var', '_nginx_web_subdomain', role='invoiceninjav5') + '.' + lookup('role_var', '_nginx_web_domain', role='invoiceninjav5')
                                            if (lookup('role_var', '_nginx_web_subdomain', role='invoiceninjav5') | length > 0)
                                            else lookup('role_var', '_nginx_web_domain', role='invoiceninjav5')) }}"
        ```

=== "DNS"

    ??? variable string "`invoiceninjav5_role_nginx_dns_record`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_dns_record: "{{ lookup('role_var', '_nginx_web_subdomain', role='invoiceninjav5') }}"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_dns_zone`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_dns_zone: "{{ lookup('role_var', '_nginx_web_domain', role='invoiceninjav5') }}"
        ```

    ??? variable bool "`invoiceninjav5_role_nginx_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_nginx_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`invoiceninjav5_role_docker_container`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_container: "{{ invoiceninjav5_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`invoiceninjav5_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_image_pull: true
        ```

    ??? variable string "`invoiceninjav5_role_docker_image_repo`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_image_repo: "invoiceninja/invoiceninja"
        ```

    ??? variable string "`invoiceninjav5_role_docker_image_tag`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_image_tag: "5"
        ```

    ??? variable string "`invoiceninjav5_role_docker_image`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='invoiceninjav5') }}:{{ lookup('role_var', '_docker_image_tag', role='invoiceninjav5') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`invoiceninjav5_role_docker_envs_default`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_envs_default:
          TZ: "{{ tz }}"
          APP_URL: "{{ lookup('role_var', '_nginx_web_url', role='invoiceninjav5') }}"
          APP_KEY: "{{ lookup('role_var', '_app_key', role='invoiceninjav5') }}"
          APP_ENV: "production"
          APP_DEBUG: "false"
          TRUSTED_PROXIES: "*"
          REQUIRE_HTTPS: "true"
          DB_TYPE: "mysql"
          DB_HOST: "mariadb"
          DB_USERNAME: "root"
          DB_PASSWORD: "password321"
          DB_DATABASE: "invoiceninjav5db"
          DB_PORT: "3306"
          PDF_GENERATOR: "hosted_ninja"
          IS_DOCKER: "true"
          PHANTOMJS_PDF_GENERATION: "false"
          IN_USER_EMAIL: "{{ user.email }}"
          IN_PASSWORD: "{{ user.pass }}"
        ```

    ??? variable dict "`invoiceninjav5_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`invoiceninjav5_role_docker_volumes_default`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/public:/var/www/app/public"
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/storage:/var/www/app/storage"
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/php.ini:/usr/local/etc/php/php.ini"
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/php-cli.ini:/usr/local/etc/php/php-cli.ini"
        ```

    ??? variable list "`invoiceninjav5_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`invoiceninjav5_role_docker_hostname`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_hostname: "{{ invoiceninjav5_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`invoiceninjav5_role_docker_networks_alias`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_networks_alias: "{{ invoiceninjav5_name }}"
        ```

    ??? variable list "`invoiceninjav5_role_docker_networks_default`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_networks_default: []
        ```

    ??? variable list "`invoiceninjav5_role_docker_networks_custom`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`invoiceninjav5_role_docker_restart_policy`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`invoiceninjav5_role_docker_state`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`invoiceninjav5_role_depends_on`"

        ```yaml
        # Type: string
        invoiceninjav5_role_depends_on: "invoiceninja-nginx,mariadb"
        ```

    ??? variable string "`invoiceninjav5_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        invoiceninjav5_role_depends_on_delay: "0"
        ```

    ??? variable string "`invoiceninjav5_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        invoiceninjav5_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`invoiceninjav5_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_blkio_weight:
        ```

    ??? variable int "`invoiceninjav5_role_docker_cpu_period`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_cpu_period:
        ```

    ??? variable int "`invoiceninjav5_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_cpu_quota:
        ```

    ??? variable int "`invoiceninjav5_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_cpu_shares:
        ```

    ??? variable string "`invoiceninjav5_role_docker_cpus`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_cpus:
        ```

    ??? variable string "`invoiceninjav5_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_cpuset_cpus:
        ```

    ??? variable string "`invoiceninjav5_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_cpuset_mems:
        ```

    ??? variable string "`invoiceninjav5_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_kernel_memory:
        ```

    ??? variable string "`invoiceninjav5_role_docker_memory`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_memory:
        ```

    ??? variable string "`invoiceninjav5_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_memory_reservation:
        ```

    ??? variable string "`invoiceninjav5_role_docker_memory_swap`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_memory_swap:
        ```

    ??? variable int "`invoiceninjav5_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_memory_swappiness:
        ```

    ??? variable string "`invoiceninjav5_role_docker_shm_size`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`invoiceninjav5_role_docker_cap_drop`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_cap_drop:
        ```

    ??? variable string "`invoiceninjav5_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_cgroupns_mode:
        ```

    ??? variable list "`invoiceninjav5_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`invoiceninjav5_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_device_read_bps:
        ```

    ??? variable list "`invoiceninjav5_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_device_read_iops:
        ```

    ??? variable list "`invoiceninjav5_role_docker_device_requests`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_device_requests:
        ```

    ??? variable list "`invoiceninjav5_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_device_write_bps:
        ```

    ??? variable list "`invoiceninjav5_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_device_write_iops:
        ```

    ??? variable list "`invoiceninjav5_role_docker_devices`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_devices:
        ```

    ??? variable string "`invoiceninjav5_role_docker_devices_default`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_devices_default:
        ```

    ??? variable list "`invoiceninjav5_role_docker_groups`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_groups:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_privileged:
        ```

    ??? variable list "`invoiceninjav5_role_docker_security_opts`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_security_opts:
        ```

    ??? variable string "`invoiceninjav5_role_docker_user`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_user:
        ```

    ??? variable string "`invoiceninjav5_role_docker_userns_mode`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`invoiceninjav5_role_docker_dns_opts`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_dns_opts:
        ```

    ??? variable list "`invoiceninjav5_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_dns_search_domains:
        ```

    ??? variable list "`invoiceninjav5_role_docker_dns_servers`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_dns_servers:
        ```

    ??? variable string "`invoiceninjav5_role_docker_domainname`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_domainname:
        ```

    ??? variable list "`invoiceninjav5_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_exposed_ports:
        ```

    ??? variable dict "`invoiceninjav5_role_docker_hosts`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_hosts:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_hosts_use_common:
        ```

    ??? variable string "`invoiceninjav5_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_ipc_mode:
        ```

    ??? variable list "`invoiceninjav5_role_docker_links`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_links:
        ```

    ??? variable string "`invoiceninjav5_role_docker_network_mode`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_network_mode:
        ```

    ??? variable string "`invoiceninjav5_role_docker_pid_mode`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_pid_mode:
        ```

    ??? variable list "`invoiceninjav5_role_docker_ports`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_ports:
        ```

    ??? variable string "`invoiceninjav5_role_docker_uts`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`invoiceninjav5_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_keep_volumes:
        ```

    ??? variable list "`invoiceninjav5_role_docker_mounts`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_mounts:
        ```

    ??? variable dict "`invoiceninjav5_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_storage_opts:
        ```

    ??? variable list "`invoiceninjav5_role_docker_tmpfs`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_tmpfs:
        ```

    ??? variable string "`invoiceninjav5_role_docker_volume_driver`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_volume_driver:
        ```

    ??? variable list "`invoiceninjav5_role_docker_volumes_from`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_volumes_from:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_volumes_global:
        ```

    ??? variable string "`invoiceninjav5_role_docker_working_dir`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`invoiceninjav5_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_auto_remove:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_cleanup:
        ```

    ??? variable string "`invoiceninjav5_role_docker_force_kill`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_force_kill:
        ```

    ??? variable dict "`invoiceninjav5_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_healthcheck:
        ```

    ??? variable int "`invoiceninjav5_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_init:
        ```

    ??? variable string "`invoiceninjav5_role_docker_kill_signal`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_kill_signal:
        ```

    ??? variable string "`invoiceninjav5_role_docker_log_driver`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_log_driver:
        ```

    ??? variable dict "`invoiceninjav5_role_docker_log_options`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_log_options:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_oom_killer:
        ```

    ??? variable int "`invoiceninjav5_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_oom_score_adj:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_output_logs:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_paused:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_recreate:
        ```

    ??? variable int "`invoiceninjav5_role_docker_restart_retries`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_restart_retries:
        ```

    ??? variable int "`invoiceninjav5_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`invoiceninjav5_role_docker_capabilities`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_capabilities:
        ```

    ??? variable string "`invoiceninjav5_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_cgroup_parent:
        ```

    ??? variable list "`invoiceninjav5_role_docker_commands`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_commands:
        ```

    ??? variable int "`invoiceninjav5_role_docker_create_timeout`"

        ```yaml
        # Type: int
        invoiceninjav5_role_docker_create_timeout:
        ```

    ??? variable string "`invoiceninjav5_role_docker_entrypoint`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_entrypoint:
        ```

    ??? variable string "`invoiceninjav5_role_docker_env_file`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_env_file:
        ```

    ??? variable dict "`invoiceninjav5_role_docker_labels`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_labels:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_labels_use_common:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_read_only:
        ```

    ??? variable string "`invoiceninjav5_role_docker_runtime`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_runtime:
        ```

    ??? variable list "`invoiceninjav5_role_docker_sysctls`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_sysctls:
        ```

    ??? variable list "`invoiceninjav5_role_docker_ulimits`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`invoiceninjav5_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        invoiceninjav5_role_autoheal_enabled: true
        ```

    ??? variable bool "`invoiceninjav5_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        invoiceninjav5_role_diun_enabled: true
        ```

    ??? variable bool "`invoiceninjav5_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        invoiceninjav5_role_dns_enabled: true
        ```

    ??? variable bool "`invoiceninjav5_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        invoiceninjav5_role_docker_controller: true
        ```

    ??? variable list "`invoiceninjav5_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`invoiceninjav5_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_volumes_download:
        ```

    ??? variable string "`invoiceninjav5_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        invoiceninjav5_role_web_api_http_port:
        ```

    ??? variable string "`invoiceninjav5_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        invoiceninjav5_role_web_api_http_scheme:
        ```

    ??? variable dict "`invoiceninjav5_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        invoiceninjav5_role_web_api_http_serverstransport:
        ```

    ??? variable string "`invoiceninjav5_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        invoiceninjav5_role_web_api_port:
        ```

    ??? variable string "`invoiceninjav5_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        invoiceninjav5_role_web_api_scheme:
        ```

    ??? variable dict "`invoiceninjav5_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        invoiceninjav5_role_web_api_serverstransport:
        ```

    ??? variable list "`invoiceninjav5_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        invoiceninjav5_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            invoiceninjav5_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "invoiceninjav52.{{ user.domain }}"
              - "invoiceninjav5.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`invoiceninjav5_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        invoiceninjav5_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            invoiceninjav5_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'invoiceninjav52.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`invoiceninjav5_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        invoiceninjav5_role_web_http_port:
        ```

    ??? variable string "`invoiceninjav5_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        invoiceninjav5_role_web_http_scheme:
        ```

    ??? variable dict "`invoiceninjav5_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        invoiceninjav5_role_web_http_serverstransport:
        ```

    ??? variable string "`invoiceninjav5_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        invoiceninjav5_role_web_scheme:
        ```

    ??? variable dict "`invoiceninjav5_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        invoiceninjav5_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
