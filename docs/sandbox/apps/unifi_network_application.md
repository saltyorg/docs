---
icon: material/docker
title: UniFi
hide:
  - tags
tags:
  - unifi
  - networking
  - wireless
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/linuxserver/docker-unifi-network-application/blob/main/README.md
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/unifi-network-application/tags
      type: docker
    - name: Community
      url: https://linuxserver.io/discord
      type: discord
  project_description:
    name: UniFi Network Application
    summary: |-
      a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance.
    link: https://www.ui.com/download/unifi
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# UniFi Network Application

## Overview

[UniFi Network Application](https://www.ui.com/download/unifi) is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/linuxserver/docker-unifi-network-application/blob/main/README.md){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/unifi-network-application/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! warning
    This role is a replacement for the previous Unifi Controller role. This is not an in-place replacement. In order to migrate, you must perform a full backup from the Unifi web interface, and restore from that backup when running the setup wizard in a fresh instance of the Unifi Network Application. You must rename/remove the previous appdata from `/opt/unifi` before deploying the Unifi Network Application role.

## Deployment

```shell
sb install sandbox-unifi-network-application
```

## Usage

Visit <https://unifi.iYOUR_DOMAIN_NAMEi>.

## Basics

  1. Visit the Unifi Network Application site at <https://unifi.iYOUR_DOMAIN_NAMEi>

  2. For Unifi to adopt other devices, e.g. an Access Point, it is required to change the inform IP address. Because Unifi runs inside Docker by default it uses an IP address not accessible by other devices. To change this go to Settings > System Settings > Controller Configuration and set the Controller Hostname/IP to a hostname or IP address accessible by your devices. Additionally the checkbox "Override inform host with controller hostname/IP" has to be checked, so that devices can connect to the controller during adoption (devices use the inform-endpoint during adoption).

  In order to manually adopt a device take these steps:

  ```shell
  ssh ubnt@$AP-IP
  set-inform http://$address:8080/inform
  ```

  The default device password is `ubnt`. `$address` is the IP address of the host you are running this container on and `$AP-IP` is the Access Point IP address.

  When using a Security Gateway (router) it could be that network connected devices are unable to obtain an ip address. This can be fixed by setting "DHCP Gateway IP", under Settings > Networks > network_name, to a correct (and accessible) ip address.

- [:octicons-link-16: Documentation: Unifi Net App Docs](https://github.com/linuxserver/docker-unifi-network-application/blob/master/README.md){: .header-icons }

!!! note
      📢 The default setup only publish the 8080 tcp port, which is the bare minimum to allow communication between your network equipment and Unifi Network Application.
      Depending on your requirements, you may need additional ports according to the [:octicons-link-16: Documentation](https://github.com/linuxserver/docker-unifi-network-application#parameters) .

      The recommended way to customize these parameters is to use the [inventory](../../saltbox/inventory/index.md).

      Edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section:

      ```
      ### Open Specified Ports for the specified container ###
      ##### Unifi Ports for aditional services #####
      unifi_network_application_docker_ports_custom:
        - "1900:1900/udp" #Required for Make controller discoverable on L2 network option
        - "8843:8843/tcp" #Unifi guest portal HTTPS redirect port
        - "8880:8880/tcp" #Unifi guest portal HTTP redirect port
        - "6789:6789/tcp" #For mobile throughput test
        - "5514:5514/udp" #Remote syslog port
      ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        unifi_network_application_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `unifi_network_application_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `unifi_network_application_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`unifi_network_application_name`"

        ```yaml
        # Type: string
        unifi_network_application_name: unifi
        ```

=== "Settings"

    ??? variable string "`unifi_network_application_mongo_user`"

        ```yaml
        # Type: string
        unifi_network_application_mongo_user: "unifi"
        ```

    ??? variable string "`unifi_network_application_mongo_pass`"

        ```yaml
        # Type: string
        unifi_network_application_mongo_pass: "password4321"
        ```

    ??? variable string "`unifi_network_application_mongo_port`"

        ```yaml
        # Type: string
        unifi_network_application_mongo_port: "27017"
        ```

    ??? variable string "`unifi_network_application_mongo_dbname`"

        ```yaml
        # Type: string
        unifi_network_application_mongo_dbname: "unifi"
        ```

=== "Web"

    ??? variable string "`unifi_network_application_role_web_subdomain`"

        ```yaml
        # Type: string
        unifi_network_application_role_web_subdomain: "{{ unifi_network_application_name }}"
        ```

    ??? variable string "`unifi_network_application_role_web_domain`"

        ```yaml
        # Type: string
        unifi_network_application_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`unifi_network_application_role_web_port`"

        ```yaml
        # Type: string
        unifi_network_application_role_web_port: "8443"
        ```

    ??? variable string "`unifi_network_application_role_web_scheme`"

        ```yaml
        # Type: string
        unifi_network_application_role_web_scheme: "https"
        ```

    ??? variable string "`unifi_network_application_role_web_serverstransport`"

        ```yaml
        # Type: string
        unifi_network_application_role_web_serverstransport: "skipverify@file"
        ```

    ??? variable string "`unifi_network_application_role_web_url`"

        ```yaml
        # Type: string
        unifi_network_application_role_web_url: "{{ 'https://' + (unifi_network_application_role_web_subdomain + '.' + unifi_network_application_role_web_domain
                                                 if (unifi_network_application_role_web_subdomain | length > 0)
                                                 else unifi_network_application_role_web_domain) }}"
        ```

=== "DNS"

    ??? variable string "`unifi_network_application_role_dns_record`"

        ```yaml
        # Type: string
        unifi_network_application_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='unifi_network_application') }}"
        ```

    ??? variable string "`unifi_network_application_role_dns_zone`"

        ```yaml
        # Type: string
        unifi_network_application_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='unifi_network_application') }}"
        ```

    ??? variable bool "`unifi_network_application_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`unifi_network_application_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`unifi_network_application_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`unifi_network_application_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`unifi_network_application_role_traefik_certresolver`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`unifi_network_application_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_traefik_enabled: true
        ```

    ??? variable bool "`unifi_network_application_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_traefik_api_enabled: false
        ```

    ??? variable string "`unifi_network_application_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`unifi_network_application_role_docker_container`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_container: "{{ unifi_network_application_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`unifi_network_application_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_image_pull: true
        ```

    ??? variable string "`unifi_network_application_role_docker_image_tag`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_image_tag: "latest"
        ```

    ??? variable string "`unifi_network_application_role_docker_image_repo`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_image_repo: "lscr.io/linuxserver/unifi-network-application"
        ```

    ??? variable string "`unifi_network_application_role_docker_image`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='unifi_network_application') }}:{{ lookup('role_var', '_docker_image_tag', role='unifi_network_application') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`unifi_network_application_role_docker_ports_default`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_ports_default:
          - "8080:8080/tcp"
          - "3478:3478/udp"
          - "10001:10001/udp"
        ```

    ??? variable list "`unifi_network_application_role_docker_ports_custom`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`unifi_network_application_role_docker_envs_default`"

        ```yaml
        # Type: dict
        unifi_network_application_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          MONGO_USER: "{{ unifi_network_application_mongo_user }}"
          MONGO_PASS: "{{ unifi_network_application_mongo_pass }}"
          MONGO_HOST: "{{ unifi_network_application_name }}-mongo"
          MONGO_PORT: "{{ unifi_network_application_mongo_port }}"
          MONGO_DBNAME: "{{ unifi_network_application_mongo_dbname }}"
        ```

    ??? variable dict "`unifi_network_application_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        unifi_network_application_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`unifi_network_application_role_docker_volumes_default`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_volumes_default:
          - "{{ unifi_network_application_role_paths_location }}:/config"
        ```

    ??? variable list "`unifi_network_application_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`unifi_network_application_role_docker_hostname`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_hostname: "{{ unifi_network_application_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`unifi_network_application_role_docker_networks_alias`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_networks_alias: "{{ unifi_network_application_name }}"
        ```

    ??? variable list "`unifi_network_application_role_docker_networks_default`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_networks_default: []
        ```

    ??? variable list "`unifi_network_application_role_docker_networks_custom`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`unifi_network_application_role_docker_restart_policy`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`unifi_network_application_role_docker_state`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`unifi_network_application_role_depends_on`"

        ```yaml
        # Type: string
        unifi_network_application_role_depends_on: "{{ unifi_network_application_name }}-mongo"
        ```

    ??? variable string "`unifi_network_application_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        unifi_network_application_role_depends_on_delay: "0"
        ```

    ??? variable string "`unifi_network_application_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        unifi_network_application_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`unifi_network_application_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_blkio_weight:
        ```

    ??? variable int "`unifi_network_application_role_docker_cpu_period`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_cpu_period:
        ```

    ??? variable int "`unifi_network_application_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_cpu_quota:
        ```

    ??? variable int "`unifi_network_application_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_cpu_shares:
        ```

    ??? variable string "`unifi_network_application_role_docker_cpus`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_cpus:
        ```

    ??? variable string "`unifi_network_application_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_cpuset_cpus:
        ```

    ??? variable string "`unifi_network_application_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_cpuset_mems:
        ```

    ??? variable string "`unifi_network_application_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_kernel_memory:
        ```

    ??? variable string "`unifi_network_application_role_docker_memory`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_memory:
        ```

    ??? variable string "`unifi_network_application_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_memory_reservation:
        ```

    ??? variable string "`unifi_network_application_role_docker_memory_swap`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_memory_swap:
        ```

    ??? variable int "`unifi_network_application_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_memory_swappiness:
        ```

    ??? variable string "`unifi_network_application_role_docker_shm_size`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`unifi_network_application_role_docker_cap_drop`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_cap_drop:
        ```

    ??? variable string "`unifi_network_application_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_cgroupns_mode:
        ```

    ??? variable list "`unifi_network_application_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`unifi_network_application_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_device_read_bps:
        ```

    ??? variable list "`unifi_network_application_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_device_read_iops:
        ```

    ??? variable list "`unifi_network_application_role_docker_device_requests`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_device_requests:
        ```

    ??? variable list "`unifi_network_application_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_device_write_bps:
        ```

    ??? variable list "`unifi_network_application_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_device_write_iops:
        ```

    ??? variable list "`unifi_network_application_role_docker_devices`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_devices:
        ```

    ??? variable string "`unifi_network_application_role_docker_devices_default`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_devices_default:
        ```

    ??? variable list "`unifi_network_application_role_docker_groups`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_groups:
        ```

    ??? variable bool "`unifi_network_application_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_privileged:
        ```

    ??? variable list "`unifi_network_application_role_docker_security_opts`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_security_opts:
        ```

    ??? variable string "`unifi_network_application_role_docker_user`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_user:
        ```

    ??? variable string "`unifi_network_application_role_docker_userns_mode`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`unifi_network_application_role_docker_dns_opts`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_dns_opts:
        ```

    ??? variable list "`unifi_network_application_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_dns_search_domains:
        ```

    ??? variable list "`unifi_network_application_role_docker_dns_servers`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_dns_servers:
        ```

    ??? variable string "`unifi_network_application_role_docker_domainname`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_domainname:
        ```

    ??? variable list "`unifi_network_application_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_exposed_ports:
        ```

    ??? variable dict "`unifi_network_application_role_docker_hosts`"

        ```yaml
        # Type: dict
        unifi_network_application_role_docker_hosts:
        ```

    ??? variable bool "`unifi_network_application_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_hosts_use_common:
        ```

    ??? variable string "`unifi_network_application_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_ipc_mode:
        ```

    ??? variable list "`unifi_network_application_role_docker_links`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_links:
        ```

    ??? variable string "`unifi_network_application_role_docker_network_mode`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_network_mode:
        ```

    ??? variable string "`unifi_network_application_role_docker_pid_mode`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_pid_mode:
        ```

    ??? variable string "`unifi_network_application_role_docker_uts`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`unifi_network_application_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_keep_volumes:
        ```

    ??? variable list "`unifi_network_application_role_docker_mounts`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_mounts:
        ```

    ??? variable dict "`unifi_network_application_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        unifi_network_application_role_docker_storage_opts:
        ```

    ??? variable list "`unifi_network_application_role_docker_tmpfs`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_tmpfs:
        ```

    ??? variable string "`unifi_network_application_role_docker_volume_driver`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_volume_driver:
        ```

    ??? variable list "`unifi_network_application_role_docker_volumes_from`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_volumes_from:
        ```

    ??? variable bool "`unifi_network_application_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_volumes_global:
        ```

    ??? variable string "`unifi_network_application_role_docker_working_dir`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`unifi_network_application_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_auto_remove:
        ```

    ??? variable bool "`unifi_network_application_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_cleanup:
        ```

    ??? variable string "`unifi_network_application_role_docker_force_kill`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_force_kill:
        ```

    ??? variable dict "`unifi_network_application_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        unifi_network_application_role_docker_healthcheck:
        ```

    ??? variable int "`unifi_network_application_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`unifi_network_application_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_init:
        ```

    ??? variable string "`unifi_network_application_role_docker_kill_signal`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_kill_signal:
        ```

    ??? variable string "`unifi_network_application_role_docker_log_driver`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_log_driver:
        ```

    ??? variable dict "`unifi_network_application_role_docker_log_options`"

        ```yaml
        # Type: dict
        unifi_network_application_role_docker_log_options:
        ```

    ??? variable bool "`unifi_network_application_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_oom_killer:
        ```

    ??? variable int "`unifi_network_application_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_oom_score_adj:
        ```

    ??? variable bool "`unifi_network_application_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_output_logs:
        ```

    ??? variable bool "`unifi_network_application_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_paused:
        ```

    ??? variable bool "`unifi_network_application_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_recreate:
        ```

    ??? variable int "`unifi_network_application_role_docker_restart_retries`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_restart_retries:
        ```

    ??? variable int "`unifi_network_application_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`unifi_network_application_role_docker_capabilities`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_capabilities:
        ```

    ??? variable string "`unifi_network_application_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_cgroup_parent:
        ```

    ??? variable list "`unifi_network_application_role_docker_commands`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_commands:
        ```

    ??? variable int "`unifi_network_application_role_docker_create_timeout`"

        ```yaml
        # Type: int
        unifi_network_application_role_docker_create_timeout:
        ```

    ??? variable string "`unifi_network_application_role_docker_entrypoint`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_entrypoint:
        ```

    ??? variable string "`unifi_network_application_role_docker_env_file`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_env_file:
        ```

    ??? variable dict "`unifi_network_application_role_docker_labels`"

        ```yaml
        # Type: dict
        unifi_network_application_role_docker_labels:
        ```

    ??? variable bool "`unifi_network_application_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_labels_use_common:
        ```

    ??? variable bool "`unifi_network_application_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_read_only:
        ```

    ??? variable string "`unifi_network_application_role_docker_runtime`"

        ```yaml
        # Type: string
        unifi_network_application_role_docker_runtime:
        ```

    ??? variable list "`unifi_network_application_role_docker_sysctls`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_sysctls:
        ```

    ??? variable list "`unifi_network_application_role_docker_ulimits`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`unifi_network_application_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        unifi_network_application_role_autoheal_enabled: true
        ```

    ??? variable bool "`unifi_network_application_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        unifi_network_application_role_diun_enabled: true
        ```

    ??? variable bool "`unifi_network_application_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        unifi_network_application_role_dns_enabled: true
        ```

    ??? variable bool "`unifi_network_application_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        unifi_network_application_role_docker_controller: true
        ```

    ??? variable list "`unifi_network_application_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        unifi_network_application_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`unifi_network_application_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_docker_volumes_download:
        ```

    ??? variable string "`unifi_network_application_role_themepark_addons`"

        ```yaml
        # Type: string
        unifi_network_application_role_themepark_addons:
        ```

    ??? variable string "`unifi_network_application_role_themepark_app`"

        ```yaml
        # Type: string
        unifi_network_application_role_themepark_app:
        ```

    ??? variable string "`unifi_network_application_role_themepark_theme`"

        ```yaml
        # Type: string
        unifi_network_application_role_themepark_theme:
        ```

    ??? variable string "`unifi_network_application_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_api_middleware:
        ```

    ??? variable string "`unifi_network_application_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`unifi_network_application_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        unifi_network_application_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`unifi_network_application_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        unifi_network_application_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`unifi_network_application_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        unifi_network_application_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`unifi_network_application_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        unifi_network_application_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`unifi_network_application_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_middleware_http:
        ```

    ??? variable bool "`unifi_network_application_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`unifi_network_application_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        unifi_network_application_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`unifi_network_application_role_traefik_priority`"

        ```yaml
        # Type: string
        unifi_network_application_role_traefik_priority:
        ```

    ??? variable bool "`unifi_network_application_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        unifi_network_application_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`unifi_network_application_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        unifi_network_application_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`unifi_network_application_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        unifi_network_application_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`unifi_network_application_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        unifi_network_application_role_web_api_http_port:
        ```

    ??? variable string "`unifi_network_application_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        unifi_network_application_role_web_api_http_scheme:
        ```

    ??? variable dict "`unifi_network_application_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        unifi_network_application_role_web_api_http_serverstransport:
        ```

    ??? variable string "`unifi_network_application_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        unifi_network_application_role_web_api_port:
        ```

    ??? variable string "`unifi_network_application_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        unifi_network_application_role_web_api_scheme:
        ```

    ??? variable dict "`unifi_network_application_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        unifi_network_application_role_web_api_serverstransport:
        ```

    ??? variable list "`unifi_network_application_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        unifi_network_application_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            unifi_network_application_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "unifi_network_application2.{{ user.domain }}"
              - "unifi_network_application.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`unifi_network_application_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        unifi_network_application_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            unifi_network_application_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'unifi_network_application2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`unifi_network_application_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        unifi_network_application_role_web_http_port:
        ```

    ??? variable string "`unifi_network_application_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        unifi_network_application_role_web_http_scheme:
        ```

    ??? variable dict "`unifi_network_application_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        unifi_network_application_role_web_http_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
