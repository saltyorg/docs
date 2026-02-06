---
icon: material/docker
title: Firefly III Importer
hide:
  - tags
tags:
  - fireflyiii-importer
  - finance
  - tools
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.firefly-iii.org/tutorials/firefly-iii/importing-data
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/fireflyiii/data-importer/tags
      type: docker
    - name: Community
      url: https://github.com/orgs/firefly-iii/discussions
      type: github
  project_description:
    name: Firefly III Data Importer
    summary: |-
      a tool designed to import financial data into the Firefly III personal finance manager.
    link: https://www.firefly-iii.org
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Firefly III Data Importer

## Overview

[Firefly III Data Importer](https://www.firefly-iii.org) is a tool designed to import financial data into the Firefly III personal finance manager.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.firefly-iii.org/tutorials/firefly-iii/importing-data){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/fireflyiii/data-importer/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/orgs/firefly-iii/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

### Connection To Firefly III

The Required variables that should be defined in [inventory](../../saltbox/inventory/index.md):

To authenticate the Data Importer to Firefly III you require to use either:

- [Access Token](#access-token)
- [Client ID](#client-id)

#### Access Token

```yaml title="Firefly III Data Importer Access Token Settings"
fireflyiii_importer_docker_envs_custom:
  - FIREFLY_III_ACCESS_TOKEN: ""  # (1)!
```

1. Your access token from your instance of Firefly III | Options | Profile | OAuth | Personal Access Tokens | Create New Token.

#### Client ID

```yaml title="Firefly III Data Importer Client ID Settings"
fireflyiii_importer_docker_envs_custom:
  - FIREFLY_III_CLIENT_ID: "1"  # (1)!
```

1. Your client id from your instance of Firefly III | Options | Profile | OAuth | OAuth Clients | Create New Client.
> Note: Your require to leave Confidential unticked

## Import data

For the following methods, your data need to be formatted in CSV.

### Web import

You can refer to the following documentation to execute import from the server: [web import](https://docs.firefly-iii.org/how-to/data-importer/import/csv/)

### Server import

You can refer to the following documentation to execute import from the server: [CLI import](https://docs.firefly-iii.org/how-to/data-importer/advanced/cli/)

## Additional Settings

> **Note: For all available settings please refer to the Firefly III Data Importer [example env](https://raw.githubusercontent.com/firefly-iii/docker/main/docker-compose-importer.yml)**

### Email Notifications
To enable email notifications, set the following [inventory](../../saltbox/inventory/index.md) entries to your desired values:

```yaml title="Firefly III Data Importer Email Settings"
MAIL_MAILER: "log"  # (1)!
MAIL_HOST: "localhost"  # (2)!
MAIL_PORT: "25"  # (3)!
MAIL_FROM: "fireflyiii@domain.com"  # (4)!
MAIL_USERNAME: ""  # (5)!
MAIL_PASSWORD: ""  # (6)!
MAIN_ENCRYPTION: ""  # (7)!
```

1. The MAIL_MAILER-setting indicates the system that is used for mailing. Firefly III supports the following mail systems: smtp, sendmail, mailgun, mandrill, sparkpost and log. [Here](https://docs.firefly-iii.org/how-to/firefly-iii/advanced/notifications/#email) is an explanation about each MAIL_MAILER option
2. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
4. Replace `25` with your email port. IE: `587`
3. The email address you want to send to. Replace `""` with the email address you want to send to
5. Replace `""` with your email username if necessary.
6. Replace `""` with your email password if necessary.
7. Use `SSL` or `TLS` for communication with the SMTP server. Can be `true` or '`false`.

## Deployment

```shell
sb install sandbox-fireflyiii_importer
```

## Usage

Visit <https://fireflyiii-importer.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        fireflyiii_importer_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `fireflyiii_importer_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `fireflyiii_importer_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`fireflyiii_importer_name`"

        ```yaml
        # Type: string
        fireflyiii_importer_name: fireflyiii-importer
        ```

=== "Web"

    ??? variable string "`fireflyiii_importer_role_web_subdomain`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_web_subdomain: "{{ fireflyiii_importer_name }}"
        ```

    ??? variable string "`fireflyiii_importer_role_web_domain`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`fireflyiii_importer_role_web_port`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_web_port: "8080"
        ```

    ??? variable string "`fireflyiii_importer_role_web_url`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='fireflyiii_importer') + '.' + lookup('role_var', '_web_domain', role='fireflyiii_importer')
                                           if (lookup('role_var', '_web_subdomain', role='fireflyiii_importer') | length > 0)
                                           else lookup('role_var', '_web_domain', role='fireflyiii_importer')) }}"
        ```

=== "DNS"

    ??? variable string "`fireflyiii_importer_role_dns_record`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='fireflyiii_importer') }}"
        ```

    ??? variable string "`fireflyiii_importer_role_dns_zone`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='fireflyiii_importer') }}"
        ```

    ??? variable bool "`fireflyiii_importer_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`fireflyiii_importer_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_certresolver`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_enabled: true
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_api_enabled: false
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`fireflyiii_importer_role_docker_container`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_container: "{{ fireflyiii_importer_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`fireflyiii_importer_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_image_pull: true
        ```

    ??? variable string "`fireflyiii_importer_role_docker_image_repo`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_image_repo: "fireflyiii/data-importer"
        ```

    ??? variable string "`fireflyiii_importer_role_docker_image_tag`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_image_tag: "latest"
        ```

    ??? variable string "`fireflyiii_importer_role_docker_image`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='fireflyiii_importer') }}:{{ lookup('role_var', '_docker_image_tag', role='fireflyiii_importer') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`fireflyiii_importer_role_docker_envs_default`"

        ```yaml
        # Type: dict
        fireflyiii_importer_role_docker_envs_default:
          IMPORT_DIR_ALLOWLIST: /import
          FIREFLY_III_URL: "http://{{ fireflyiii_name }}:8080"
          VANITY_URL: "{{ lookup('role_var', '_web_url', role='fireflyiii') }}"
          TRUSTED_PROXIES: "**"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`fireflyiii_importer_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        fireflyiii_importer_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`fireflyiii_importer_role_docker_volumes_default`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='fireflyiii') }}/import:/import"
          - "/etc/timezone:/etc/timezone:ro"
          - "/etc/localtime:/etc/localtime:ro"
        ```

    ??? variable list "`fireflyiii_importer_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`fireflyiii_importer_role_docker_hostname`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_hostname: "{{ fireflyiii_importer_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`fireflyiii_importer_role_docker_networks_alias`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_networks_alias: "{{ fireflyiii_importer_name }}"
        ```

    ??? variable list "`fireflyiii_importer_role_docker_networks_default`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_networks_default: []
        ```

    ??? variable list "`fireflyiii_importer_role_docker_networks_custom`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`fireflyiii_importer_role_docker_restart_policy`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`fireflyiii_importer_role_docker_state`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`fireflyiii_importer_role_depends_on`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_depends_on: "{{ fireflyiii_name }}"
        ```

    ??? variable string "`fireflyiii_importer_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        fireflyiii_importer_role_depends_on_delay: "0"
        ```

    ??? variable string "`fireflyiii_importer_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        fireflyiii_importer_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`fireflyiii_importer_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_blkio_weight:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_cpu_period`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_cpu_period:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_cpu_quota:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_cpu_shares:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_cpus`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_cpus:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_cpuset_cpus:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_cpuset_mems:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_kernel_memory:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_memory`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_memory:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_memory_reservation:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_memory_swap`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_memory_swap:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_memory_swappiness:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_shm_size`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`fireflyiii_importer_role_docker_cap_drop`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_cap_drop:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_cgroupns_mode:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_device_read_bps:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_device_read_iops:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_device_requests`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_device_requests:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_device_write_bps:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_device_write_iops:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_devices`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_devices:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_groups`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_groups:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_privileged:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_security_opts`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_security_opts:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_user`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_user:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_userns_mode`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`fireflyiii_importer_role_docker_dns_opts`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_dns_opts:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_dns_search_domains:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_dns_servers`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_dns_servers:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_domainname`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_domainname:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_exposed_ports:
        ```

    ??? variable dict "`fireflyiii_importer_role_docker_hosts`"

        ```yaml
        # Type: dict
        fireflyiii_importer_role_docker_hosts:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_hosts_use_common:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_ipc_mode:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_links`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_links:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_network_mode`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_network_mode:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_pid_mode`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_pid_mode:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_ports`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_ports:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_uts`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`fireflyiii_importer_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_keep_volumes:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_mounts`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_mounts:
        ```

    ??? variable dict "`fireflyiii_importer_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        fireflyiii_importer_role_docker_storage_opts:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_tmpfs`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_tmpfs:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_volume_driver`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_volume_driver:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_volumes_from`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_volumes_from:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_volumes_global:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_working_dir`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`fireflyiii_importer_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_auto_remove:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_cleanup:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_force_kill`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_force_kill:
        ```

    ??? variable dict "`fireflyiii_importer_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        fireflyiii_importer_role_docker_healthcheck:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_init:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_kill_signal`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_kill_signal:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_log_driver`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_log_driver:
        ```

    ??? variable dict "`fireflyiii_importer_role_docker_log_options`"

        ```yaml
        # Type: dict
        fireflyiii_importer_role_docker_log_options:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_oom_killer:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_oom_score_adj:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_output_logs:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_paused:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_recreate:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_restart_retries`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_restart_retries:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_stop_signal`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_stop_signal:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`fireflyiii_importer_role_docker_capabilities`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_capabilities:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_cgroup_parent:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_commands`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_commands:
        ```

    ??? variable int "`fireflyiii_importer_role_docker_create_timeout`"

        ```yaml
        # Type: int
        fireflyiii_importer_role_docker_create_timeout:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_dev_dri`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_dev_dri:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_entrypoint`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_entrypoint:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_env_file`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_env_file:
        ```

    ??? variable dict "`fireflyiii_importer_role_docker_labels`"

        ```yaml
        # Type: dict
        fireflyiii_importer_role_docker_labels:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_labels_use_common:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_read_only:
        ```

    ??? variable string "`fireflyiii_importer_role_docker_runtime`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_docker_runtime:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_sysctls`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_sysctls:
        ```

    ??? variable list "`fireflyiii_importer_role_docker_ulimits`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`fireflyiii_importer_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        fireflyiii_importer_role_autoheal_enabled: true
        ```

    ??? variable bool "`fireflyiii_importer_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        fireflyiii_importer_role_diun_enabled: true
        ```

    ??? variable bool "`fireflyiii_importer_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_dns_enabled: true
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_controller: true
        ```

    ??? variable list "`fireflyiii_importer_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        fireflyiii_importer_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`fireflyiii_importer_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_docker_volumes_download:
        ```

    ??? variable string "`fireflyiii_importer_role_themepark_addons`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_themepark_addons:
        ```

    ??? variable string "`fireflyiii_importer_role_themepark_app`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_themepark_app:
        ```

    ??? variable string "`fireflyiii_importer_role_themepark_theme`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_themepark_theme:
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_api_middleware:
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_middleware_http:
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`fireflyiii_importer_role_traefik_priority`"

        ```yaml
        # Type: string
        fireflyiii_importer_role_traefik_priority:
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`fireflyiii_importer_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        fireflyiii_importer_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`fireflyiii_importer_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        fireflyiii_importer_role_web_api_http_port:
        ```

    ??? variable string "`fireflyiii_importer_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        fireflyiii_importer_role_web_api_http_scheme:
        ```

    ??? variable dict "`fireflyiii_importer_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        fireflyiii_importer_role_web_api_http_serverstransport:
        ```

    ??? variable string "`fireflyiii_importer_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        fireflyiii_importer_role_web_api_port:
        ```

    ??? variable string "`fireflyiii_importer_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        fireflyiii_importer_role_web_api_scheme:
        ```

    ??? variable dict "`fireflyiii_importer_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        fireflyiii_importer_role_web_api_serverstransport:
        ```

    ??? variable list "`fireflyiii_importer_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        fireflyiii_importer_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            fireflyiii_importer_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "fireflyiii_importer2.{{ user.domain }}"
              - "fireflyiii_importer.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`fireflyiii_importer_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        fireflyiii_importer_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            fireflyiii_importer_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'fireflyiii_importer2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`fireflyiii_importer_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        fireflyiii_importer_role_web_http_port:
        ```

    ??? variable string "`fireflyiii_importer_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        fireflyiii_importer_role_web_http_scheme:
        ```

    ??? variable dict "`fireflyiii_importer_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        fireflyiii_importer_role_web_http_serverstransport:
        ```

    ??? variable string "`fireflyiii_importer_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        fireflyiii_importer_role_web_scheme:
        ```

    ??? variable dict "`fireflyiii_importer_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        fireflyiii_importer_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
