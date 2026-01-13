---
icon: material/docker
hide:
  - tags
tags:
  - VPN
  - server
saltbox_automation:
  app_links:
    - name: Manual
      url: https://wg-easy.github.io/wg-easy/edge/guides/setup
      type: documentation
    - name: Releases
      url: https://github.com/wg-easy/wg-easy/pkgs/container/wg-easy
      type: github
    - name: Community
      url: https://github.com/wg-easy/wg-easy/discussions
      type: github
  project_description:
    name: Wireguard
    summary: |-
      an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography.
    link: https://www.wireguard.com
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Wireguard

## Overview

[Wireguard](https://www.wireguard.com) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://wg-easy.github.io/wg-easy/edge/guides/setup){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/wg-easy/wg-easy/pkgs/container/wg-easy){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/wg-easy/wg-easy/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-wireguard
```

## Usage

Visit <https://wireguard.iYOUR_DOMAIN_NAMEi>.

The password provisioned is your Saltbox password.

## Basics

- Use the Web UI to configure your clients.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        wireguard_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `wireguard_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `wireguard_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`wireguard_name`"

        ```yaml
        # Type: string
        wireguard_name: wireguard
        ```

=== "Settings"

    ??? variable string "`wireguard_role_listen_port`"

        ```yaml
        # Type: string
        wireguard_role_listen_port: "51820"
        ```

    ??? variable string "`wireguard_role_dns`"

        ```yaml
        # Type: string
        wireguard_role_dns: "1.1.1.1,8.8.8.8"
        ```

=== "Web"

    ??? variable string "`wireguard_role_web_subdomain`"

        ```yaml
        # Type: string
        wireguard_role_web_subdomain: "{{ wireguard_name }}"
        ```

    ??? variable string "`wireguard_role_web_domain`"

        ```yaml
        # Type: string
        wireguard_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wireguard_role_web_port`"

        ```yaml
        # Type: string
        wireguard_role_web_port: "51821"
        ```

    ??? variable string "`wireguard_role_web_url`"

        ```yaml
        # Type: string
        wireguard_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wireguard') + '.' + lookup('role_var', '_web_domain', role='wireguard')
                                 if (lookup('role_var', '_web_subdomain', role='wireguard') | length > 0)
                                 else lookup('role_var', '_web_domain', role='wireguard')) }}"
        ```

    ??? variable string "`wireguard_role_web_host`"

        ```yaml
        # Type: string
        wireguard_role_web_host: "{{ (lookup('role_var', '_web_subdomain', role='wireguard') + '.' + lookup('role_var', '_web_domain', role='wireguard')
                                  if (lookup('role_var', '_web_subdomain', role='wireguard') | length > 0)
                                  else lookup('role_var', '_web_domain', role='wireguard')) }}"
        ```

=== "DNS"

    ??? variable string "`wireguard_role_dns_record`"

        ```yaml
        # Type: string
        wireguard_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wireguard') }}"
        ```

    ??? variable string "`wireguard_role_dns_zone`"

        ```yaml
        # Type: string
        wireguard_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wireguard') }}"
        ```

    ??? variable bool "`wireguard_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wireguard_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        wireguard_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`wireguard_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        wireguard_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wireguard_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        wireguard_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`wireguard_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wireguard_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wireguard_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_enabled: true
        ```

    ??? variable bool "`wireguard_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_api_enabled: false
        ```

    ??? variable string "`wireguard_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        wireguard_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`wireguard_role_docker_container`"

        ```yaml
        # Type: string
        wireguard_role_docker_container: "{{ wireguard_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`wireguard_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_image_pull: true
        ```

    ??? variable string "`wireguard_role_docker_image_repo`"

        ```yaml
        # Type: string
        wireguard_role_docker_image_repo: "ghcr.io/wg-easy/wg-easy"
        ```

    ??? variable string "`wireguard_role_docker_image_tag`"

        ```yaml
        # Type: string
        wireguard_role_docker_image_tag: "15"
        ```

    ??? variable string "`wireguard_role_docker_image`"

        ```yaml
        # Type: string
        wireguard_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wireguard') }}:{{ lookup('role_var', '_docker_image_tag', role='wireguard') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`wireguard_role_docker_ports_default`"

        ```yaml
        # Type: list
        wireguard_role_docker_ports_default:
          - "{{ lookup('role_var', '_listen_port', role='wireguard') }}:{{ lookup('role_var', '_listen_port', role='wireguard') }}/udp"
        ```

    ??? variable list "`wireguard_role_docker_ports_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`wireguard_role_docker_envs_default`"

        ```yaml
        # Type: dict
        wireguard_role_docker_envs_default:
          TZ: "{{ tz }}"
          DISABLE_IPV6: "{{ 'false' if docker_ipv6 else 'true' }}"
          WG_DEVICE: "eth0"
        ```

    ??? variable dict "`wireguard_role_docker_envs_setup`"

        ```yaml
        # Type: dict
        wireguard_role_docker_envs_setup:
          INIT_ENABLED: "true"
          INIT_USERNAME: "{{ user.name }}"
          INIT_PASSWORD: "{{ user.pass }}"
          INIT_HOST: "{{ lookup('role_var', '_web_host', role='wireguard') }}"
          INIT_PORT: "{{ lookup('role_var', '_listen_port', role='wireguard') }}"
          INIT_DNS: "{{ lookup('role_var', '_dns', role='wireguard') }}"
          INIT_IPV4_CIDR: "10.8.0.0/24"
          INIT_IPV6_CIDR: "2001:0DB8::/32"
        ```

    ??? variable dict "`wireguard_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        wireguard_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`wireguard_role_docker_volumes_default`"

        ```yaml
        # Type: list
        wireguard_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='wireguard') }}:/etc/wireguard"
          - /lib/modules:/lib/modules:ro
        ```

    ??? variable list "`wireguard_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`wireguard_role_docker_hostname`"

        ```yaml
        # Type: string
        wireguard_role_docker_hostname: "{{ wireguard_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`wireguard_role_docker_networks_alias`"

        ```yaml
        # Type: string
        wireguard_role_docker_networks_alias: "{{ wireguard_name }}"
        ```

    ??? variable list "`wireguard_role_docker_networks_default`"

        ```yaml
        # Type: list
        wireguard_role_docker_networks_default:
          - name: wg
            ipv4_address: "10.42.42.42"
            ipv6_address: "{{ 'fdcc:ad94:bacf:61a3::2a' if docker_ipv6 else omit }}"
            gw_priority: 1
            driver_opts:
              com.docker.network.endpoint.ifname: eth0
        ```

    ??? variable list "`wireguard_role_docker_networks_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`wireguard_role_docker_capabilities_default`"

        ```yaml
        # Type: list
        wireguard_role_docker_capabilities_default:
          - NET_ADMIN
          - SYS_MODULE
        ```

    ??? variable list "`wireguard_role_docker_capabilities_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_capabilities_custom: []
        ```

    <h5>Sysctls</h5>

    ??? variable dict "`wireguard_role_docker_sysctls_ipv4`"

        ```yaml
        # Type: dict
        wireguard_role_docker_sysctls_ipv4:
          net.ipv4.conf.all.src_valid_mark: "1"
          net.ipv4.ip_forward: "1"
        ```

    ??? variable dict "`wireguard_role_docker_sysctls_ipv6`"

        ```yaml
        # Type: dict
        wireguard_role_docker_sysctls_ipv6:
          net.ipv6.conf.all.disable_ipv6: "0"
          net.ipv6.conf.all.forwarding: "1"
          net.ipv6.conf.default.forwarding: "1"
        ```

    ??? variable string "`wireguard_role_docker_sysctls`"

        ```yaml
        # Type: string
        wireguard_role_docker_sysctls: "{{ lookup('role_var', '_docker_sysctls_ipv4', role='wireguard')
                                           | combine(lookup('role_var', '_docker_sysctls_ipv6', role='wireguard')
                                                     if docker_ipv6
                                                     else {}) }}"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`wireguard_role_docker_restart_policy`"

        ```yaml
        # Type: string
        wireguard_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`wireguard_role_docker_state`"

        ```yaml
        # Type: string
        wireguard_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`wireguard_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        wireguard_role_docker_blkio_weight:
        ```

    ??? variable int "`wireguard_role_docker_cpu_period`"

        ```yaml
        # Type: int
        wireguard_role_docker_cpu_period:
        ```

    ??? variable int "`wireguard_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        wireguard_role_docker_cpu_quota:
        ```

    ??? variable int "`wireguard_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        wireguard_role_docker_cpu_shares:
        ```

    ??? variable string "`wireguard_role_docker_cpus`"

        ```yaml
        # Type: string
        wireguard_role_docker_cpus:
        ```

    ??? variable string "`wireguard_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        wireguard_role_docker_cpuset_cpus:
        ```

    ??? variable string "`wireguard_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        wireguard_role_docker_cpuset_mems:
        ```

    ??? variable string "`wireguard_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        wireguard_role_docker_kernel_memory:
        ```

    ??? variable string "`wireguard_role_docker_memory`"

        ```yaml
        # Type: string
        wireguard_role_docker_memory:
        ```

    ??? variable string "`wireguard_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        wireguard_role_docker_memory_reservation:
        ```

    ??? variable string "`wireguard_role_docker_memory_swap`"

        ```yaml
        # Type: string
        wireguard_role_docker_memory_swap:
        ```

    ??? variable int "`wireguard_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        wireguard_role_docker_memory_swappiness:
        ```

    ??? variable string "`wireguard_role_docker_shm_size`"

        ```yaml
        # Type: string
        wireguard_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`wireguard_role_docker_cap_drop`"

        ```yaml
        # Type: list
        wireguard_role_docker_cap_drop:
        ```

    ??? variable string "`wireguard_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        wireguard_role_docker_cgroupns_mode:
        ```

    ??? variable list "`wireguard_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        wireguard_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`wireguard_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        wireguard_role_docker_device_read_bps:
        ```

    ??? variable list "`wireguard_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        wireguard_role_docker_device_read_iops:
        ```

    ??? variable list "`wireguard_role_docker_device_requests`"

        ```yaml
        # Type: list
        wireguard_role_docker_device_requests:
        ```

    ??? variable list "`wireguard_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        wireguard_role_docker_device_write_bps:
        ```

    ??? variable list "`wireguard_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        wireguard_role_docker_device_write_iops:
        ```

    ??? variable list "`wireguard_role_docker_devices`"

        ```yaml
        # Type: list
        wireguard_role_docker_devices:
        ```

    ??? variable string "`wireguard_role_docker_devices_default`"

        ```yaml
        # Type: string
        wireguard_role_docker_devices_default:
        ```

    ??? variable list "`wireguard_role_docker_groups`"

        ```yaml
        # Type: list
        wireguard_role_docker_groups:
        ```

    ??? variable bool "`wireguard_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_privileged:
        ```

    ??? variable list "`wireguard_role_docker_security_opts`"

        ```yaml
        # Type: list
        wireguard_role_docker_security_opts:
        ```

    ??? variable string "`wireguard_role_docker_user`"

        ```yaml
        # Type: string
        wireguard_role_docker_user:
        ```

    ??? variable string "`wireguard_role_docker_userns_mode`"

        ```yaml
        # Type: string
        wireguard_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`wireguard_role_docker_dns_opts`"

        ```yaml
        # Type: list
        wireguard_role_docker_dns_opts:
        ```

    ??? variable list "`wireguard_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        wireguard_role_docker_dns_search_domains:
        ```

    ??? variable list "`wireguard_role_docker_dns_servers`"

        ```yaml
        # Type: list
        wireguard_role_docker_dns_servers:
        ```

    ??? variable string "`wireguard_role_docker_domainname`"

        ```yaml
        # Type: string
        wireguard_role_docker_domainname:
        ```

    ??? variable list "`wireguard_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        wireguard_role_docker_exposed_ports:
        ```

    ??? variable dict "`wireguard_role_docker_hosts`"

        ```yaml
        # Type: dict
        wireguard_role_docker_hosts:
        ```

    ??? variable bool "`wireguard_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_hosts_use_common:
        ```

    ??? variable string "`wireguard_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        wireguard_role_docker_ipc_mode:
        ```

    ??? variable list "`wireguard_role_docker_links`"

        ```yaml
        # Type: list
        wireguard_role_docker_links:
        ```

    ??? variable string "`wireguard_role_docker_network_mode`"

        ```yaml
        # Type: string
        wireguard_role_docker_network_mode:
        ```

    ??? variable string "`wireguard_role_docker_pid_mode`"

        ```yaml
        # Type: string
        wireguard_role_docker_pid_mode:
        ```

    ??? variable string "`wireguard_role_docker_uts`"

        ```yaml
        # Type: string
        wireguard_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`wireguard_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_keep_volumes:
        ```

    ??? variable list "`wireguard_role_docker_mounts`"

        ```yaml
        # Type: list
        wireguard_role_docker_mounts:
        ```

    ??? variable dict "`wireguard_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        wireguard_role_docker_storage_opts:
        ```

    ??? variable list "`wireguard_role_docker_tmpfs`"

        ```yaml
        # Type: list
        wireguard_role_docker_tmpfs:
        ```

    ??? variable string "`wireguard_role_docker_volume_driver`"

        ```yaml
        # Type: string
        wireguard_role_docker_volume_driver:
        ```

    ??? variable list "`wireguard_role_docker_volumes_from`"

        ```yaml
        # Type: list
        wireguard_role_docker_volumes_from:
        ```

    ??? variable bool "`wireguard_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_volumes_global:
        ```

    ??? variable string "`wireguard_role_docker_working_dir`"

        ```yaml
        # Type: string
        wireguard_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`wireguard_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_auto_remove:
        ```

    ??? variable bool "`wireguard_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_cleanup:
        ```

    ??? variable string "`wireguard_role_docker_force_kill`"

        ```yaml
        # Type: string
        wireguard_role_docker_force_kill:
        ```

    ??? variable dict "`wireguard_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        wireguard_role_docker_healthcheck:
        ```

    ??? variable int "`wireguard_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        wireguard_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`wireguard_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_init:
        ```

    ??? variable string "`wireguard_role_docker_kill_signal`"

        ```yaml
        # Type: string
        wireguard_role_docker_kill_signal:
        ```

    ??? variable string "`wireguard_role_docker_log_driver`"

        ```yaml
        # Type: string
        wireguard_role_docker_log_driver:
        ```

    ??? variable dict "`wireguard_role_docker_log_options`"

        ```yaml
        # Type: dict
        wireguard_role_docker_log_options:
        ```

    ??? variable bool "`wireguard_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_oom_killer:
        ```

    ??? variable int "`wireguard_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        wireguard_role_docker_oom_score_adj:
        ```

    ??? variable bool "`wireguard_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_output_logs:
        ```

    ??? variable bool "`wireguard_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_paused:
        ```

    ??? variable bool "`wireguard_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_recreate:
        ```

    ??? variable int "`wireguard_role_docker_restart_retries`"

        ```yaml
        # Type: int
        wireguard_role_docker_restart_retries:
        ```

    ??? variable int "`wireguard_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        wireguard_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable string "`wireguard_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        wireguard_role_docker_cgroup_parent:
        ```

    ??? variable list "`wireguard_role_docker_commands`"

        ```yaml
        # Type: list
        wireguard_role_docker_commands:
        ```

    ??? variable int "`wireguard_role_docker_create_timeout`"

        ```yaml
        # Type: int
        wireguard_role_docker_create_timeout:
        ```

    ??? variable string "`wireguard_role_docker_entrypoint`"

        ```yaml
        # Type: string
        wireguard_role_docker_entrypoint:
        ```

    ??? variable string "`wireguard_role_docker_env_file`"

        ```yaml
        # Type: string
        wireguard_role_docker_env_file:
        ```

    ??? variable dict "`wireguard_role_docker_labels`"

        ```yaml
        # Type: dict
        wireguard_role_docker_labels:
        ```

    ??? variable bool "`wireguard_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_labels_use_common:
        ```

    ??? variable bool "`wireguard_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_read_only:
        ```

    ??? variable string "`wireguard_role_docker_runtime`"

        ```yaml
        # Type: string
        wireguard_role_docker_runtime:
        ```

    ??? variable list "`wireguard_role_docker_ulimits`"

        ```yaml
        # Type: list
        wireguard_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`wireguard_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wireguard_role_autoheal_enabled: true
        ```

    ??? variable string "`wireguard_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        wireguard_role_depends_on: ""
        ```

    ??? variable string "`wireguard_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wireguard_role_depends_on_delay: "0"
        ```

    ??? variable string "`wireguard_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wireguard_role_depends_on_healthchecks:
        ```

    ??? variable bool "`wireguard_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wireguard_role_diun_enabled: true
        ```

    ??? variable string "`wireguard_role_dns`"

        ```yaml
        # Type: string
        wireguard_role_dns:
        ```

    ??? variable bool "`wireguard_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wireguard_role_dns_enabled: true
        ```

    ??? variable bool "`wireguard_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wireguard_role_docker_controller: true
        ```

    ??? variable string "`wireguard_role_docker_image_repo`"

        ```yaml
        # Type: string
        wireguard_role_docker_image_repo:
        ```

    ??? variable string "`wireguard_role_docker_image_tag`"

        ```yaml
        # Type: string
        wireguard_role_docker_image_tag:
        ```

    ??? variable string "`wireguard_role_docker_sysctls_ipv4`"

        ```yaml
        # Type: string
        wireguard_role_docker_sysctls_ipv4:
        ```

    ??? variable string "`wireguard_role_docker_sysctls_ipv6`"

        ```yaml
        # Type: string
        wireguard_role_docker_sysctls_ipv6:
        ```

    ??? variable bool "`wireguard_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_volumes_download:
        ```

    ??? variable string "`wireguard_role_listen_port`"

        ```yaml
        # Type: string (quoted number)
        wireguard_role_listen_port:
        ```

    ??? variable string "`wireguard_role_paths_location`"

        ```yaml
        # Type: string
        wireguard_role_paths_location:
        ```

    ??? variable string "`wireguard_role_themepark_addons`"

        ```yaml
        # Type: string
        wireguard_role_themepark_addons:
        ```

    ??? variable string "`wireguard_role_themepark_app`"

        ```yaml
        # Type: string
        wireguard_role_themepark_app:
        ```

    ??? variable string "`wireguard_role_themepark_theme`"

        ```yaml
        # Type: string
        wireguard_role_themepark_theme:
        ```

    ??? variable dict "`wireguard_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        wireguard_role_traefik_api_endpoint:
        ```

    ??? variable string "`wireguard_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        wireguard_role_traefik_api_middleware:
        ```

    ??? variable string "`wireguard_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        wireguard_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`wireguard_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`wireguard_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wireguard_role_traefik_certresolver:
        ```

    ??? variable bool "`wireguard_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`wireguard_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        wireguard_role_traefik_middleware_http:
        ```

    ??? variable bool "`wireguard_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`wireguard_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`wireguard_role_traefik_priority`"

        ```yaml
        # Type: string
        wireguard_role_traefik_priority:
        ```

    ??? variable bool "`wireguard_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`wireguard_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wireguard_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wireguard_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`wireguard_role_web_domain`"

        ```yaml
        # Type: string
        wireguard_role_web_domain:
        ```

    ??? variable list "`wireguard_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wireguard_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            wireguard_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wireguard2.{{ user.domain }}"
              - "wireguard.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`wireguard_role_web_host`"

        ```yaml
        # Type: string
        wireguard_role_web_host:
        ```

    ??? variable string "`wireguard_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        wireguard_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            wireguard_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wireguard2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`wireguard_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        wireguard_role_web_http_port:
        ```

    ??? variable string "`wireguard_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        wireguard_role_web_http_scheme:
        ```

    ??? variable dict "`wireguard_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        wireguard_role_web_http_serverstransport:
        ```

    ??? variable string "`wireguard_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wireguard_role_web_scheme:
        ```

    ??? variable dict "`wireguard_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        wireguard_role_web_serverstransport:
        ```

    ??? variable string "`wireguard_role_web_subdomain`"

        ```yaml
        # Type: string
        wireguard_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->