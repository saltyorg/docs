---
icon: material/docker
hide:
  - tags
tags:
  - guacamole
  - networking
  - remote-access
saltbox_automation:
  app_links:
    - name: Manual
      url: https://guacamole.apache.org/doc/gug
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/jasonbean/guacamole/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Guacamole
    summary: |-
      a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH.
    link: https://guacamole.apache.org/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Guacamole

## Overview

[Guacamole](https://guacamole.apache.org/) is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://guacamole.apache.org/doc/gug){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/jasonbean/guacamole/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-guacamole
```

## Usage

Visit <https://guacamole.iYOUR_DOMAIN_NAMEi>.

## Basics

- Log in with user and password `guacadmin`. Change the default user and password immediately.

- [:octicons-link-16: Documentation: Guacamole Docs](https://guacamole.apache.org/doc/gug){: .header-icons }

### Enable Extensions (Optional)

Guacamole supports various authentication extensions that can be enabled through your [Inventory](https://docs.saltbox.dev/saltbox/inventory/). Add any of the following options to enable specific extensions:

=== "TOTP (Two-Factor Authentication)"

    Enable time-based one-time passwords for enhanced security:

    ```yml
    guacamole_docker_envs_custom:
      OPT_TOTP: "Y"
    ```

=== "LDAP"

    Enable LDAP authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_LDAP: "Y"
    ```

=== "RADIUS"

    Enable RADIUS authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_RADIUS: "Y"
    ```

=== "Duo Security"

    Enable Duo two-factor authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_DUO: "Y"
    ```

=== "CAS"

    Enable Central Authentication Service:

    ```yml
    guacamole_docker_envs_custom:
      OPT_CAS: "Y"
    ```

=== "OpenID Connect"

    Enable OpenID Connect authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_OPENID: "Y"
    ```

=== "SAML"

    Enable SAML authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_SAML: "Y"
    ```

=== "Header Authentication"

    Enable HTTP header-based authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_HEADER: "Y"
    ```

After adding any extension options, run `sb install sandbox-guacamole` to apply changes.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        guacamole_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `guacamole_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `guacamole_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`guacamole_name`"

        ```yaml
        # Type: string
        guacamole_name: guacamole
        ```

=== "Settings"

    ??? variable bool "`guacamole_role_totp_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_totp_enable: false
        ```

    ??? variable bool "`guacamole_role_ldap_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_ldap_enable: false
        ```

    ??? variable bool "`guacamole_role_radius_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_radius_enable: false
        ```

    ??? variable bool "`guacamole_role_duo_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_duo_enable: false
        ```

    ??? variable bool "`guacamole_role_cas_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_cas_enable: false
        ```

    ??? variable bool "`guacamole_role_openid_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_openid_enable: false
        ```

    ??? variable bool "`guacamole_role_saml_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_saml_enable: false
        ```

    ??? variable bool "`guacamole_role_header_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_header_enable: false
        ```

=== "Web"

    ??? variable string "`guacamole_role_web_subdomain`"

        ```yaml
        # Type: string
        guacamole_role_web_subdomain: "{{ guacamole_name }}"
        ```

    ??? variable string "`guacamole_role_web_domain`"

        ```yaml
        # Type: string
        guacamole_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`guacamole_role_web_port`"

        ```yaml
        # Type: string
        guacamole_role_web_port: "8080"
        ```

    ??? variable string "`guacamole_role_web_url`"

        ```yaml
        # Type: string
        guacamole_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='guacamole') + '.' + lookup('role_var', '_web_domain', role='guacamole')
                                 if (lookup('role_var', '_web_subdomain', role='guacamole') | length > 0)
                                 else lookup('role_var', '_web_domain', role='guacamole')) }}"
        ```

=== "DNS"

    ??? variable string "`guacamole_role_dns_record`"

        ```yaml
        # Type: string
        guacamole_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='guacamole') }}"
        ```

    ??? variable string "`guacamole_role_dns_zone`"

        ```yaml
        # Type: string
        guacamole_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='guacamole') }}"
        ```

    ??? variable bool "`guacamole_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`guacamole_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        guacamole_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`guacamole_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        guacamole_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`guacamole_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        guacamole_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`guacamole_role_traefik_certresolver`"

        ```yaml
        # Type: string
        guacamole_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`guacamole_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_enabled: true
        ```

    ??? variable bool "`guacamole_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_api_enabled: false
        ```

    ??? variable string "`guacamole_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        guacamole_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`guacamole_role_docker_container`"

        ```yaml
        # Type: string
        guacamole_role_docker_container: "{{ guacamole_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`guacamole_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_image_pull: true
        ```

    ??? variable string "`guacamole_role_docker_image_repo`"

        ```yaml
        # Type: string
        guacamole_role_docker_image_repo: "jasonbean/guacamole"
        ```

    ??? variable string "`guacamole_role_docker_image_tag`"

        ```yaml
        # Type: string
        guacamole_role_docker_image_tag: "latest"
        ```

    ??? variable string "`guacamole_role_docker_image`"

        ```yaml
        # Type: string
        guacamole_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='guacamole') }}:{{ lookup('role_var', '_docker_image_tag', role='guacamole') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`guacamole_role_docker_envs_default`"

        ```yaml
        # Type: dict
        guacamole_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          OPT_MYSQL: "Y"
          OPT_TOTP: "{{ 'Y' if lookup('role_var', '_totp_enable', role='guacamole') else omit }}"
          OPT_LDAP: "{{ 'Y' if lookup('role_var', '_ldap_enable', role='guacamole') else omit }}"
          OPT_RADIUS: "{{ 'Y' if lookup('role_var', '_radius_enable', role='guacamole') else omit }}"
          OPT_DUO: "{{ 'Y' if lookup('role_var', '_duo_enable', role='guacamole') else omit }}"
          OPT_CAS: "{{ 'Y' if lookup('role_var', '_cas_enable', role='guacamole') else omit }}"
          OPT_OPENID: "{{ 'Y' if lookup('role_var', '_openid_enable', role='guacamole') else omit }}"
          OPT_SAML: "{{ 'Y' if lookup('role_var', '_saml_enable', role='guacamole') else omit }}"
          OPT_HEADER: "{{ 'Y' if lookup('role_var', '_header_enable', role='guacamole') else omit }}"
        ```

    ??? variable dict "`guacamole_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        guacamole_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`guacamole_role_docker_volumes_default`"

        ```yaml
        # Type: list
        guacamole_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='guacamole') }}/config:/config"
        ```

    ??? variable list "`guacamole_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        guacamole_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`guacamole_role_docker_hostname`"

        ```yaml
        # Type: string
        guacamole_role_docker_hostname: "{{ guacamole_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`guacamole_role_docker_networks_alias`"

        ```yaml
        # Type: string
        guacamole_role_docker_networks_alias: "{{ guacamole_name }}"
        ```

    ??? variable list "`guacamole_role_docker_networks_default`"

        ```yaml
        # Type: list
        guacamole_role_docker_networks_default: []
        ```

    ??? variable list "`guacamole_role_docker_networks_custom`"

        ```yaml
        # Type: list
        guacamole_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`guacamole_role_docker_restart_policy`"

        ```yaml
        # Type: string
        guacamole_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`guacamole_role_docker_state`"

        ```yaml
        # Type: string
        guacamole_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`guacamole_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        guacamole_role_docker_blkio_weight:
        ```

    ??? variable int "`guacamole_role_docker_cpu_period`"

        ```yaml
        # Type: int
        guacamole_role_docker_cpu_period:
        ```

    ??? variable int "`guacamole_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        guacamole_role_docker_cpu_quota:
        ```

    ??? variable int "`guacamole_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        guacamole_role_docker_cpu_shares:
        ```

    ??? variable string "`guacamole_role_docker_cpus`"

        ```yaml
        # Type: string
        guacamole_role_docker_cpus:
        ```

    ??? variable string "`guacamole_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        guacamole_role_docker_cpuset_cpus:
        ```

    ??? variable string "`guacamole_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        guacamole_role_docker_cpuset_mems:
        ```

    ??? variable string "`guacamole_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        guacamole_role_docker_kernel_memory:
        ```

    ??? variable string "`guacamole_role_docker_memory`"

        ```yaml
        # Type: string
        guacamole_role_docker_memory:
        ```

    ??? variable string "`guacamole_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        guacamole_role_docker_memory_reservation:
        ```

    ??? variable string "`guacamole_role_docker_memory_swap`"

        ```yaml
        # Type: string
        guacamole_role_docker_memory_swap:
        ```

    ??? variable int "`guacamole_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        guacamole_role_docker_memory_swappiness:
        ```

    ??? variable string "`guacamole_role_docker_shm_size`"

        ```yaml
        # Type: string
        guacamole_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`guacamole_role_docker_cap_drop`"

        ```yaml
        # Type: list
        guacamole_role_docker_cap_drop:
        ```

    ??? variable string "`guacamole_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        guacamole_role_docker_cgroupns_mode:
        ```

    ??? variable list "`guacamole_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        guacamole_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`guacamole_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        guacamole_role_docker_device_read_bps:
        ```

    ??? variable list "`guacamole_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        guacamole_role_docker_device_read_iops:
        ```

    ??? variable list "`guacamole_role_docker_device_requests`"

        ```yaml
        # Type: list
        guacamole_role_docker_device_requests:
        ```

    ??? variable list "`guacamole_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        guacamole_role_docker_device_write_bps:
        ```

    ??? variable list "`guacamole_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        guacamole_role_docker_device_write_iops:
        ```

    ??? variable list "`guacamole_role_docker_devices`"

        ```yaml
        # Type: list
        guacamole_role_docker_devices:
        ```

    ??? variable string "`guacamole_role_docker_devices_default`"

        ```yaml
        # Type: string
        guacamole_role_docker_devices_default:
        ```

    ??? variable list "`guacamole_role_docker_groups`"

        ```yaml
        # Type: list
        guacamole_role_docker_groups:
        ```

    ??? variable bool "`guacamole_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_privileged:
        ```

    ??? variable list "`guacamole_role_docker_security_opts`"

        ```yaml
        # Type: list
        guacamole_role_docker_security_opts:
        ```

    ??? variable string "`guacamole_role_docker_user`"

        ```yaml
        # Type: string
        guacamole_role_docker_user:
        ```

    ??? variable string "`guacamole_role_docker_userns_mode`"

        ```yaml
        # Type: string
        guacamole_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`guacamole_role_docker_dns_opts`"

        ```yaml
        # Type: list
        guacamole_role_docker_dns_opts:
        ```

    ??? variable list "`guacamole_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        guacamole_role_docker_dns_search_domains:
        ```

    ??? variable list "`guacamole_role_docker_dns_servers`"

        ```yaml
        # Type: list
        guacamole_role_docker_dns_servers:
        ```

    ??? variable string "`guacamole_role_docker_domainname`"

        ```yaml
        # Type: string
        guacamole_role_docker_domainname:
        ```

    ??? variable list "`guacamole_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        guacamole_role_docker_exposed_ports:
        ```

    ??? variable dict "`guacamole_role_docker_hosts`"

        ```yaml
        # Type: dict
        guacamole_role_docker_hosts:
        ```

    ??? variable bool "`guacamole_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_hosts_use_common:
        ```

    ??? variable string "`guacamole_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        guacamole_role_docker_ipc_mode:
        ```

    ??? variable list "`guacamole_role_docker_links`"

        ```yaml
        # Type: list
        guacamole_role_docker_links:
        ```

    ??? variable string "`guacamole_role_docker_network_mode`"

        ```yaml
        # Type: string
        guacamole_role_docker_network_mode:
        ```

    ??? variable string "`guacamole_role_docker_pid_mode`"

        ```yaml
        # Type: string
        guacamole_role_docker_pid_mode:
        ```

    ??? variable list "`guacamole_role_docker_ports`"

        ```yaml
        # Type: list
        guacamole_role_docker_ports:
        ```

    ??? variable string "`guacamole_role_docker_uts`"

        ```yaml
        # Type: string
        guacamole_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`guacamole_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_keep_volumes:
        ```

    ??? variable list "`guacamole_role_docker_mounts`"

        ```yaml
        # Type: list
        guacamole_role_docker_mounts:
        ```

    ??? variable dict "`guacamole_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        guacamole_role_docker_storage_opts:
        ```

    ??? variable list "`guacamole_role_docker_tmpfs`"

        ```yaml
        # Type: list
        guacamole_role_docker_tmpfs:
        ```

    ??? variable string "`guacamole_role_docker_volume_driver`"

        ```yaml
        # Type: string
        guacamole_role_docker_volume_driver:
        ```

    ??? variable list "`guacamole_role_docker_volumes_from`"

        ```yaml
        # Type: list
        guacamole_role_docker_volumes_from:
        ```

    ??? variable bool "`guacamole_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_volumes_global:
        ```

    ??? variable string "`guacamole_role_docker_working_dir`"

        ```yaml
        # Type: string
        guacamole_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`guacamole_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_auto_remove:
        ```

    ??? variable bool "`guacamole_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_cleanup:
        ```

    ??? variable string "`guacamole_role_docker_force_kill`"

        ```yaml
        # Type: string
        guacamole_role_docker_force_kill:
        ```

    ??? variable dict "`guacamole_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        guacamole_role_docker_healthcheck:
        ```

    ??? variable int "`guacamole_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        guacamole_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`guacamole_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_init:
        ```

    ??? variable string "`guacamole_role_docker_kill_signal`"

        ```yaml
        # Type: string
        guacamole_role_docker_kill_signal:
        ```

    ??? variable string "`guacamole_role_docker_log_driver`"

        ```yaml
        # Type: string
        guacamole_role_docker_log_driver:
        ```

    ??? variable dict "`guacamole_role_docker_log_options`"

        ```yaml
        # Type: dict
        guacamole_role_docker_log_options:
        ```

    ??? variable bool "`guacamole_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_oom_killer:
        ```

    ??? variable int "`guacamole_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        guacamole_role_docker_oom_score_adj:
        ```

    ??? variable bool "`guacamole_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_output_logs:
        ```

    ??? variable bool "`guacamole_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_paused:
        ```

    ??? variable bool "`guacamole_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_recreate:
        ```

    ??? variable int "`guacamole_role_docker_restart_retries`"

        ```yaml
        # Type: int
        guacamole_role_docker_restart_retries:
        ```

    ??? variable int "`guacamole_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        guacamole_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`guacamole_role_docker_capabilities`"

        ```yaml
        # Type: list
        guacamole_role_docker_capabilities:
        ```

    ??? variable string "`guacamole_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        guacamole_role_docker_cgroup_parent:
        ```

    ??? variable list "`guacamole_role_docker_commands`"

        ```yaml
        # Type: list
        guacamole_role_docker_commands:
        ```

    ??? variable int "`guacamole_role_docker_create_timeout`"

        ```yaml
        # Type: int
        guacamole_role_docker_create_timeout:
        ```

    ??? variable string "`guacamole_role_docker_entrypoint`"

        ```yaml
        # Type: string
        guacamole_role_docker_entrypoint:
        ```

    ??? variable string "`guacamole_role_docker_env_file`"

        ```yaml
        # Type: string
        guacamole_role_docker_env_file:
        ```

    ??? variable dict "`guacamole_role_docker_labels`"

        ```yaml
        # Type: dict
        guacamole_role_docker_labels:
        ```

    ??? variable bool "`guacamole_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_labels_use_common:
        ```

    ??? variable bool "`guacamole_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_read_only:
        ```

    ??? variable string "`guacamole_role_docker_runtime`"

        ```yaml
        # Type: string
        guacamole_role_docker_runtime:
        ```

    ??? variable list "`guacamole_role_docker_sysctls`"

        ```yaml
        # Type: list
        guacamole_role_docker_sysctls:
        ```

    ??? variable list "`guacamole_role_docker_ulimits`"

        ```yaml
        # Type: list
        guacamole_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`guacamole_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        guacamole_role_autoheal_enabled: true
        ```

    ??? variable string "`guacamole_role_cas_enable`"

        ```yaml
        # Type: string
        guacamole_role_cas_enable:
        ```

    ??? variable string "`guacamole_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        guacamole_role_depends_on: ""
        ```

    ??? variable string "`guacamole_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        guacamole_role_depends_on_delay: "0"
        ```

    ??? variable string "`guacamole_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        guacamole_role_depends_on_healthchecks:
        ```

    ??? variable bool "`guacamole_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        guacamole_role_diun_enabled: true
        ```

    ??? variable bool "`guacamole_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        guacamole_role_dns_enabled: true
        ```

    ??? variable bool "`guacamole_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        guacamole_role_docker_controller: true
        ```

    ??? variable string "`guacamole_role_docker_image_repo`"

        ```yaml
        # Type: string
        guacamole_role_docker_image_repo:
        ```

    ??? variable string "`guacamole_role_docker_image_tag`"

        ```yaml
        # Type: string
        guacamole_role_docker_image_tag:
        ```

    ??? variable bool "`guacamole_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_volumes_download:
        ```

    ??? variable string "`guacamole_role_duo_enable`"

        ```yaml
        # Type: string
        guacamole_role_duo_enable:
        ```

    ??? variable string "`guacamole_role_header_enable`"

        ```yaml
        # Type: string
        guacamole_role_header_enable:
        ```

    ??? variable string "`guacamole_role_ldap_enable`"

        ```yaml
        # Type: string
        guacamole_role_ldap_enable:
        ```

    ??? variable string "`guacamole_role_openid_enable`"

        ```yaml
        # Type: string
        guacamole_role_openid_enable:
        ```

    ??? variable string "`guacamole_role_paths_location`"

        ```yaml
        # Type: string
        guacamole_role_paths_location:
        ```

    ??? variable string "`guacamole_role_radius_enable`"

        ```yaml
        # Type: string
        guacamole_role_radius_enable:
        ```

    ??? variable string "`guacamole_role_saml_enable`"

        ```yaml
        # Type: string
        guacamole_role_saml_enable:
        ```

    ??? variable string "`guacamole_role_themepark_addons`"

        ```yaml
        # Type: string
        guacamole_role_themepark_addons:
        ```

    ??? variable string "`guacamole_role_themepark_app`"

        ```yaml
        # Type: string
        guacamole_role_themepark_app:
        ```

    ??? variable string "`guacamole_role_themepark_theme`"

        ```yaml
        # Type: string
        guacamole_role_themepark_theme:
        ```

    ??? variable string "`guacamole_role_totp_enable`"

        ```yaml
        # Type: string
        guacamole_role_totp_enable:
        ```

    ??? variable dict "`guacamole_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        guacamole_role_traefik_api_endpoint:
        ```

    ??? variable string "`guacamole_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        guacamole_role_traefik_api_middleware:
        ```

    ??? variable string "`guacamole_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        guacamole_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`guacamole_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`guacamole_role_traefik_certresolver`"

        ```yaml
        # Type: string
        guacamole_role_traefik_certresolver:
        ```

    ??? variable bool "`guacamole_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`guacamole_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        guacamole_role_traefik_middleware_http:
        ```

    ??? variable bool "`guacamole_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`guacamole_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`guacamole_role_traefik_priority`"

        ```yaml
        # Type: string
        guacamole_role_traefik_priority:
        ```

    ??? variable bool "`guacamole_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`guacamole_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        guacamole_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        guacamole_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`guacamole_role_web_domain`"

        ```yaml
        # Type: string
        guacamole_role_web_domain:
        ```

    ??? variable list "`guacamole_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        guacamole_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            guacamole_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "guacamole2.{{ user.domain }}"
              - "guacamole.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`guacamole_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        guacamole_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            guacamole_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'guacamole2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`guacamole_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        guacamole_role_web_http_port:
        ```

    ??? variable string "`guacamole_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        guacamole_role_web_http_scheme:
        ```

    ??? variable dict "`guacamole_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        guacamole_role_web_http_serverstransport:
        ```

    ??? variable string "`guacamole_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        guacamole_role_web_scheme:
        ```

    ??? variable dict "`guacamole_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        guacamole_role_web_serverstransport:
        ```

    ??? variable string "`guacamole_role_web_subdomain`"

        ```yaml
        # Type: string
        guacamole_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->