---
icon: material/docker
title: Semaphore UI
hide:
  - tags
tags:
  - semaphoreui
  - ansible
  - automation
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.semaphoreui.com/user-guide/projects
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/semaphoreui/semaphore/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Semaphore UI
    summary: |-
      an open-source, self-hosted web interface designed to simplify and centralize the management of DevOps automation tools like Ansible, Terraform, OpenTofu, PowerShell, Bash, and Python scripts.
    link: https://github.com/semaphoreui/semaphore
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Semaphore UI

## Overview

[Semaphore UI](https://github.com/semaphoreui/semaphore) is an open-source, self-hosted web interface designed to simplify and centralize the management of DevOps automation tools like Ansible, Terraform, OpenTofu, PowerShell, Bash, and Python scripts.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.semaphoreui.com/user-guide/projects){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/semaphoreui/semaphore/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-semaphoreui
```

## Usage

Visit <https://semaphoreui.iYOUR_DOMAIN_NAMEi>.

## Basics

### Additional Settings

The default installation utilises a seperate postgres database. There is an option for this package to utilise mariadb / mysql but this isnt what this guide will be based on.

To enable email notifications, set these [inventory](../../saltbox/inventory/index.md) entries to your desired values:

```yaml title="Semaphoreui Email Settings"
SEMAPHORE_EMAIL_ALERT: "true" # (1)!
SEMAPHORE_EMAIL_SENDER: ""  # (2)!
SEMAPHORE_EMAIL_HOST: "localhost"  # (3)!¿˘˘˘˘˘˘˘˘˘¿¿˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘
SEMAPHORE_EMAIL_PORT: "25"  # (4)!¿˘˘˘˘˘˘
SEMAPHORE_EMAIL_USERNAME: ""  # (5)!
SEMAPHORE_EMAIL_PASSWORD: ""  # (6)!
SEMAPHORE_EMAIL_SECURE: ""  # (7)!
```

1. Flag which enables email alerts. Can be `true` or '`false`.
2. The email address you want to send to. Replace `""` with the email address you want to send to
3. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
4. Replace `25` with your email port. IE: `587`
5. Replace `""` with your email username if necessary.
6. Replace `""` with your email password if necessary.
7. Use `SSL` or `TLS` for communication with the SMTP server. Can be `true` or '`false`.

```yaml title="Semaphoreui Telgram Settings"
SEMAPHORE_TELEGRAM_ALERT: ""  # (1)!
SEMAPHORE_TELEGRAM_CHAT: ""  # (2)!
SEMAPHORE_TELEGRAM_TOKEN: ""  # (3)!
```

1. Flag which enables telegram alerts. Can be `true` or '`false`.
2. The chat id of which you want to send the message to
3. Your Telegram bot token

```yaml title="Semaphoreui Telgram Settings"
SEMAPHORE_SLACK_ALERT: ""  # (1)!
SEMAPHORE_SLACK_URL: ""  # (2)!
```

1. Flag which enables telegram alerts. Can be `true` or '`false`.
2. Your slack URL

Redeploy the Semaphoreui role to apply any of the above changes.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        semaphoreui_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `semaphoreui_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `semaphoreui_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`semaphoreui_name`"

        ```yaml
        # Type: string
        semaphoreui_name: semaphoreui
        ```

=== "Settings"

    ??? variable bool "`semaphoreui_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_postgres_deploy: true
        ```

    ??? variable string "`semaphoreui_role_postgres_name`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_name: "{{ semaphoreui_name }}-postgres"
        ```

    ??? variable string "`semaphoreui_role_postgres_user`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_user: "semaphoreui"
        ```

    ??? variable string "`semaphoreui_role_postgres_password`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_password: "semaphoreui"
        ```

    ??? variable string "`semaphoreui_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_docker_env_db: "semaphoreui"
        ```

    ??? variable string "`semaphoreui_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_docker_image_tag: "15"
        ```

    ??? variable string "`semaphoreui_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`semaphoreui_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        semaphoreui_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='semaphoreui') }} -U {{ lookup('role_var', '_postgres_user', role='semaphoreui') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`semaphoreui_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_paths_folder: "{{ semaphoreui_name }}"
        ```

    ??? variable string "`semaphoreui_role_postgres_paths_location`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_paths_location: "{{ server_appdata_path }}/{{ semaphoreui_role_postgres_paths_folder }}/postgres"
        ```

=== "Web"

    ??? variable string "`semaphoreui_role_web_subdomain`"

        ```yaml
        # Type: string
        semaphoreui_role_web_subdomain: "{{ semaphoreui_name }}"
        ```

    ??? variable string "`semaphoreui_role_web_domain`"

        ```yaml
        # Type: string
        semaphoreui_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`semaphoreui_role_web_port`"

        ```yaml
        # Type: string
        semaphoreui_role_web_port: "3000"
        ```

    ??? variable string "`semaphoreui_role_web_url`"

        ```yaml
        # Type: string
        semaphoreui_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='semaphoreui') + '.' + lookup('role_var', '_web_domain', role='semaphoreui')
                                   if (lookup('role_var', '_web_subdomain', role='semaphoreui') | length > 0)
                                   else lookup('role_var', '_web_domain', role='semaphoreui')) }}"
        ```

=== "DNS"

    ??? variable string "`semaphoreui_role_dns_record`"

        ```yaml
        # Type: string
        semaphoreui_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='semaphoreui') }}"
        ```

    ??? variable string "`semaphoreui_role_dns_zone`"

        ```yaml
        # Type: string
        semaphoreui_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='semaphoreui') }}"
        ```

    ??? variable bool "`semaphoreui_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`semaphoreui_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`semaphoreui_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`semaphoreui_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`semaphoreui_role_traefik_certresolver`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`semaphoreui_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_traefik_enabled: true
        ```

    ??? variable bool "`semaphoreui_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_traefik_api_enabled: true
        ```

    ??? variable string "`semaphoreui_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`semaphoreui_role_docker_container`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_container: "{{ semaphoreui_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`semaphoreui_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_image_pull: true
        ```

    ??? variable string "`semaphoreui_role_docker_image_tag`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_image_tag: "latest"
        ```

    ??? variable string "`semaphoreui_role_docker_image_repo`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_image_repo: "semaphoreui/semaphore"
        ```

    ??? variable string "`semaphoreui_role_docker_image`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='semaphoreui') }}:{{ lookup('role_var', '_docker_image_tag', role='semaphoreui') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`semaphoreui_role_docker_envs_default`"

        ```yaml
        # Type: dict
        semaphoreui_role_docker_envs_default:
          SEMAPHORE_DB_USER: "{{ lookup('role_var', '_postgres_user', role='semaphoreui') }}"
          SEMAPHORE_DB_PASS: "{{ lookup('role_var', '_postgres_password', role='semaphoreui') }}"
          SEMAPHORE_DB_HOST: "{{ lookup('role_var', '_postgres_name', role='semaphoreui') }}"
          SEMAPHORE_DB_PORT: "5432"
          SEMAPHORE_DB_DIALECT: "postgres"
          SEMAPHORE_DB: "{{ lookup('role_var', '_postgres_docker_env_db', role='semaphoreui') }}"
          SEMAPHORE_PLAYBOOK_PATH: "{{ lookup('role_var', '_paths_location', role='semaphoreui') }}/playbooks"
          SEMAPHORE_ADMIN_PASSWORD: "{{ user.pass }}"
          SEMAPHORE_ADMIN_NAME: "{{ user.name }}"
          SEMAPHORE_ADMIN_EMAIL: "{{ user.email }}"
          SEMAPHORE_ADMIN: "{{ user.name }}"
          SEMAPHORE_ACCESS_KEY_ENCRYPTION: "{{ semaphoreui_saltbox_facts.facts.secret_key }}"
          TZ: "{{ timezone }}"
        ```

    ??? variable dict "`semaphoreui_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        semaphoreui_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`semaphoreui_role_docker_hostname`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_hostname: "{{ semaphoreui_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`semaphoreui_role_docker_networks_alias`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_networks_alias: "{{ semaphoreui_name }}"
        ```

    ??? variable list "`semaphoreui_role_docker_networks_default`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_networks_default: []
        ```

    ??? variable list "`semaphoreui_role_docker_networks_custom`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`semaphoreui_role_docker_restart_policy`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`semaphoreui_role_docker_state`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`semaphoreui_role_depends_on`"

        ```yaml
        # Type: string
        semaphoreui_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='semaphoreui') }}"
        ```

    ??? variable string "`semaphoreui_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        semaphoreui_role_depends_on_delay: "0"
        ```

    ??? variable string "`semaphoreui_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        semaphoreui_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`semaphoreui_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_blkio_weight:
        ```

    ??? variable int "`semaphoreui_role_docker_cpu_period`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_cpu_period:
        ```

    ??? variable int "`semaphoreui_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_cpu_quota:
        ```

    ??? variable int "`semaphoreui_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_cpu_shares:
        ```

    ??? variable string "`semaphoreui_role_docker_cpus`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_cpus:
        ```

    ??? variable string "`semaphoreui_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_cpuset_cpus:
        ```

    ??? variable string "`semaphoreui_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_cpuset_mems:
        ```

    ??? variable string "`semaphoreui_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_kernel_memory:
        ```

    ??? variable string "`semaphoreui_role_docker_memory`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_memory:
        ```

    ??? variable string "`semaphoreui_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_memory_reservation:
        ```

    ??? variable string "`semaphoreui_role_docker_memory_swap`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_memory_swap:
        ```

    ??? variable int "`semaphoreui_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_memory_swappiness:
        ```

    ??? variable string "`semaphoreui_role_docker_shm_size`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`semaphoreui_role_docker_cap_drop`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_cap_drop:
        ```

    ??? variable string "`semaphoreui_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_cgroupns_mode:
        ```

    ??? variable list "`semaphoreui_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`semaphoreui_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_device_read_bps:
        ```

    ??? variable list "`semaphoreui_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_device_read_iops:
        ```

    ??? variable list "`semaphoreui_role_docker_device_requests`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_device_requests:
        ```

    ??? variable list "`semaphoreui_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_device_write_bps:
        ```

    ??? variable list "`semaphoreui_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_device_write_iops:
        ```

    ??? variable list "`semaphoreui_role_docker_devices`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_devices:
        ```

    ??? variable string "`semaphoreui_role_docker_devices_default`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_devices_default:
        ```

    ??? variable list "`semaphoreui_role_docker_groups`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_groups:
        ```

    ??? variable bool "`semaphoreui_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_privileged:
        ```

    ??? variable list "`semaphoreui_role_docker_security_opts`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_security_opts:
        ```

    ??? variable string "`semaphoreui_role_docker_user`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_user:
        ```

    ??? variable string "`semaphoreui_role_docker_userns_mode`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`semaphoreui_role_docker_dns_opts`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_dns_opts:
        ```

    ??? variable list "`semaphoreui_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_dns_search_domains:
        ```

    ??? variable list "`semaphoreui_role_docker_dns_servers`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_dns_servers:
        ```

    ??? variable string "`semaphoreui_role_docker_domainname`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_domainname:
        ```

    ??? variable list "`semaphoreui_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_exposed_ports:
        ```

    ??? variable dict "`semaphoreui_role_docker_hosts`"

        ```yaml
        # Type: dict
        semaphoreui_role_docker_hosts:
        ```

    ??? variable bool "`semaphoreui_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_hosts_use_common:
        ```

    ??? variable string "`semaphoreui_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_ipc_mode:
        ```

    ??? variable list "`semaphoreui_role_docker_links`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_links:
        ```

    ??? variable string "`semaphoreui_role_docker_network_mode`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_network_mode:
        ```

    ??? variable string "`semaphoreui_role_docker_pid_mode`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_pid_mode:
        ```

    ??? variable list "`semaphoreui_role_docker_ports`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_ports:
        ```

    ??? variable string "`semaphoreui_role_docker_uts`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`semaphoreui_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_keep_volumes:
        ```

    ??? variable list "`semaphoreui_role_docker_mounts`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_mounts:
        ```

    ??? variable dict "`semaphoreui_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        semaphoreui_role_docker_storage_opts:
        ```

    ??? variable list "`semaphoreui_role_docker_tmpfs`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_tmpfs:
        ```

    ??? variable string "`semaphoreui_role_docker_volume_driver`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_volume_driver:
        ```

    ??? variable list "`semaphoreui_role_docker_volumes`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_volumes:
        ```

    ??? variable list "`semaphoreui_role_docker_volumes_from`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_volumes_from:
        ```

    ??? variable bool "`semaphoreui_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_volumes_global:
        ```

    ??? variable string "`semaphoreui_role_docker_working_dir`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`semaphoreui_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_auto_remove:
        ```

    ??? variable bool "`semaphoreui_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_cleanup:
        ```

    ??? variable string "`semaphoreui_role_docker_force_kill`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_force_kill:
        ```

    ??? variable dict "`semaphoreui_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        semaphoreui_role_docker_healthcheck:
        ```

    ??? variable int "`semaphoreui_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`semaphoreui_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_init:
        ```

    ??? variable string "`semaphoreui_role_docker_kill_signal`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_kill_signal:
        ```

    ??? variable string "`semaphoreui_role_docker_log_driver`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_log_driver:
        ```

    ??? variable dict "`semaphoreui_role_docker_log_options`"

        ```yaml
        # Type: dict
        semaphoreui_role_docker_log_options:
        ```

    ??? variable bool "`semaphoreui_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_oom_killer:
        ```

    ??? variable int "`semaphoreui_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_oom_score_adj:
        ```

    ??? variable bool "`semaphoreui_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_output_logs:
        ```

    ??? variable bool "`semaphoreui_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_paused:
        ```

    ??? variable bool "`semaphoreui_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_recreate:
        ```

    ??? variable int "`semaphoreui_role_docker_restart_retries`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_restart_retries:
        ```

    ??? variable int "`semaphoreui_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`semaphoreui_role_docker_capabilities`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_capabilities:
        ```

    ??? variable string "`semaphoreui_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_cgroup_parent:
        ```

    ??? variable list "`semaphoreui_role_docker_commands`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_commands:
        ```

    ??? variable int "`semaphoreui_role_docker_create_timeout`"

        ```yaml
        # Type: int
        semaphoreui_role_docker_create_timeout:
        ```

    ??? variable string "`semaphoreui_role_docker_entrypoint`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_entrypoint:
        ```

    ??? variable string "`semaphoreui_role_docker_env_file`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_env_file:
        ```

    ??? variable dict "`semaphoreui_role_docker_labels`"

        ```yaml
        # Type: dict
        semaphoreui_role_docker_labels:
        ```

    ??? variable bool "`semaphoreui_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_labels_use_common:
        ```

    ??? variable bool "`semaphoreui_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_read_only:
        ```

    ??? variable string "`semaphoreui_role_docker_runtime`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_runtime:
        ```

    ??? variable list "`semaphoreui_role_docker_sysctls`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_sysctls:
        ```

    ??? variable list "`semaphoreui_role_docker_ulimits`"

        ```yaml
        # Type: list
        semaphoreui_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`semaphoreui_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        semaphoreui_role_autoheal_enabled: true
        ```

    ??? variable string "`semaphoreui_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        semaphoreui_role_depends_on: ""
        ```

    ??? variable string "`semaphoreui_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        semaphoreui_role_depends_on_delay: "0"
        ```

    ??? variable string "`semaphoreui_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        semaphoreui_role_depends_on_healthchecks:
        ```

    ??? variable bool "`semaphoreui_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        semaphoreui_role_diun_enabled: true
        ```

    ??? variable bool "`semaphoreui_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        semaphoreui_role_dns_enabled: true
        ```

    ??? variable bool "`semaphoreui_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        semaphoreui_role_docker_controller: true
        ```

    ??? variable string "`semaphoreui_role_docker_image_repo`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_image_repo:
        ```

    ??? variable string "`semaphoreui_role_docker_image_tag`"

        ```yaml
        # Type: string
        semaphoreui_role_docker_image_tag:
        ```

    ??? variable bool "`semaphoreui_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_docker_volumes_download:
        ```

    ??? variable string "`semaphoreui_role_paths_location`"

        ```yaml
        # Type: string
        semaphoreui_role_paths_location:
        ```

    ??? variable string "`semaphoreui_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_docker_env_db:
        ```

    ??? variable string "`semaphoreui_role_postgres_name`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_name:
        ```

    ??? variable string "`semaphoreui_role_postgres_password`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_password:
        ```

    ??? variable string "`semaphoreui_role_postgres_user`"

        ```yaml
        # Type: string
        semaphoreui_role_postgres_user:
        ```

    ??? variable string "`semaphoreui_role_themepark_addons`"

        ```yaml
        # Type: string
        semaphoreui_role_themepark_addons:
        ```

    ??? variable string "`semaphoreui_role_themepark_app`"

        ```yaml
        # Type: string
        semaphoreui_role_themepark_app:
        ```

    ??? variable string "`semaphoreui_role_themepark_theme`"

        ```yaml
        # Type: string
        semaphoreui_role_themepark_theme:
        ```

    ??? variable dict "`semaphoreui_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        semaphoreui_role_traefik_api_endpoint:
        ```

    ??? variable string "`semaphoreui_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_api_middleware:
        ```

    ??? variable string "`semaphoreui_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`semaphoreui_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        semaphoreui_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`semaphoreui_role_traefik_certresolver`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_certresolver:
        ```

    ??? variable bool "`semaphoreui_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        semaphoreui_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`semaphoreui_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        semaphoreui_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`semaphoreui_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        semaphoreui_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`semaphoreui_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_middleware_http:
        ```

    ??? variable bool "`semaphoreui_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`semaphoreui_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        semaphoreui_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`semaphoreui_role_traefik_priority`"

        ```yaml
        # Type: string
        semaphoreui_role_traefik_priority:
        ```

    ??? variable bool "`semaphoreui_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        semaphoreui_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`semaphoreui_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        semaphoreui_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`semaphoreui_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        semaphoreui_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`semaphoreui_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        semaphoreui_role_web_api_http_port:
        ```

    ??? variable string "`semaphoreui_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        semaphoreui_role_web_api_http_scheme:
        ```

    ??? variable dict "`semaphoreui_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        semaphoreui_role_web_api_http_serverstransport:
        ```

    ??? variable string "`semaphoreui_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        semaphoreui_role_web_api_port:
        ```

    ??? variable string "`semaphoreui_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        semaphoreui_role_web_api_scheme:
        ```

    ??? variable dict "`semaphoreui_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        semaphoreui_role_web_api_serverstransport:
        ```

    ??? variable string "`semaphoreui_role_web_domain`"

        ```yaml
        # Type: string
        semaphoreui_role_web_domain:
        ```

    ??? variable list "`semaphoreui_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        semaphoreui_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            semaphoreui_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "semaphoreui2.{{ user.domain }}"
              - "semaphoreui.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`semaphoreui_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        semaphoreui_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            semaphoreui_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'semaphoreui2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`semaphoreui_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        semaphoreui_role_web_http_port:
        ```

    ??? variable string "`semaphoreui_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        semaphoreui_role_web_http_scheme:
        ```

    ??? variable dict "`semaphoreui_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        semaphoreui_role_web_http_serverstransport:
        ```

    ??? variable string "`semaphoreui_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        semaphoreui_role_web_scheme:
        ```

    ??? variable dict "`semaphoreui_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        semaphoreui_role_web_serverstransport:
        ```

    ??? variable string "`semaphoreui_role_web_subdomain`"

        ```yaml
        # Type: string
        semaphoreui_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->