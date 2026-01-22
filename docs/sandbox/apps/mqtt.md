---
icon: material/docker
title: MQTT
hide:
  - tags
tags:
  - mqtt
  - automation
  - messaging
saltbox_automation:
  app_links:
    - name: Manual
      url: https://mosquitto.org/man/mosquitto-conf-5.html
      type: documentation
    - name: Releases
      url: https://hub.docker.com/_/eclipse-mosquitto/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: MQTT
    summary: |-
      a lightweight messaging protocol that is designed for use in constrained devices and low-bandwidth, high-latency, or unreliable networks. It is commonly used in Internet of Things (IoT) devices/applications for efficient and reliable communication between devices.
    link: https://mosquitto.org/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# MQTT

## Overview

[MQTT](https://mosquitto.org/) is a lightweight messaging protocol that is designed for use in constrained devices and low-bandwidth, high-latency, or unreliable networks. It is commonly used in Internet of Things (IoT) devices/applications for efficient and reliable communication between devices.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://mosquitto.org/man/mosquitto-conf-5.html){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/eclipse-mosquitto/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-mqtt
```

## Usage

MQTT does not have a web interface, so you will need to use a client to interact with it.

## Basics

You can connect MQTT to [Home Assistant](homeassistant.md) and [Node Red](node_red.md) via docker hostname. Add the MQTT integration in Home Assistant and use `mqtt` as the hostname/Broker, and 1883 as the port. In Node Red, you can use the `mqtt` node to connect to the MQTT server.

While MQTT can be set up to use a username and password, it is not recommended to expose it to the internet. So by default, MQTT is not exposed to the internet, nor does it have a username and password.

To add a username and password, you will need to edit the `mosquitto.conf` file. You can find the file in the `/opt/mqtt/config/` directory. You will need to add the following lines to the file:

```shell title="mosquitto.conf"
allow_anonymous false # (1)!
user <username> # (2)!
password <password> # (3)!
```

1. This line will disable anonymous access to the MQTT server. It is currently set to `true` by default.
2. This line will add a username to the MQTT server. Replace `<username>` with your desired username.
3. This line will add a password to the MQTT server. Replace `<password>` with your desired password.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        mqtt_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `mqtt_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `mqtt_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`mqtt_name`"

        ```yaml
        # Type: string
        mqtt_name: mqtt
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`mqtt_role_docker_container`"

        ```yaml
        # Type: string
        mqtt_role_docker_container: "{{ mqtt_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`mqtt_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_image_pull: true
        ```

    ??? variable string "`mqtt_role_docker_image_tag`"

        ```yaml
        # Type: string
        mqtt_role_docker_image_tag: "latest"
        ```

    ??? variable string "`mqtt_role_docker_image_repo`"

        ```yaml
        # Type: string
        mqtt_role_docker_image_repo: "eclipse-mosquitto"
        ```

    ??? variable string "`mqtt_role_docker_image`"

        ```yaml
        # Type: string
        mqtt_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mqtt') }}:{{ lookup('role_var', '_docker_image_tag', role='mqtt') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`mqtt_role_docker_envs_default`"

        ```yaml
        # Type: dict
        mqtt_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`mqtt_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        mqtt_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`mqtt_role_docker_volumes_default`"

        ```yaml
        # Type: list
        mqtt_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='mqtt') }}/config:/mosquitto/config"
          - "{{ lookup('role_var', '_paths_location', role='mqtt') }}/data:/mosquitto/data"
          - "{{ lookup('role_var', '_paths_location', role='mqtt') }}/log:/mosquitto/log"
          - "/etc/localtime:/etc/localtime:ro"
        ```

    ??? variable list "`mqtt_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        mqtt_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`mqtt_role_docker_hostname`"

        ```yaml
        # Type: string
        mqtt_role_docker_hostname: "{{ mqtt_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`mqtt_role_docker_networks_alias`"

        ```yaml
        # Type: string
        mqtt_role_docker_networks_alias: "{{ mqtt_name }}"
        ```

    ??? variable list "`mqtt_role_docker_networks_default`"

        ```yaml
        # Type: list
        mqtt_role_docker_networks_default: []
        ```

    ??? variable list "`mqtt_role_docker_networks_custom`"

        ```yaml
        # Type: list
        mqtt_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`mqtt_role_docker_restart_policy`"

        ```yaml
        # Type: string
        mqtt_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`mqtt_role_docker_state`"

        ```yaml
        # Type: string
        mqtt_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`mqtt_role_docker_user`"

        ```yaml
        # Type: string
        mqtt_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`mqtt_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        mqtt_role_docker_blkio_weight:
        ```

    ??? variable int "`mqtt_role_docker_cpu_period`"

        ```yaml
        # Type: int
        mqtt_role_docker_cpu_period:
        ```

    ??? variable int "`mqtt_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        mqtt_role_docker_cpu_quota:
        ```

    ??? variable int "`mqtt_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        mqtt_role_docker_cpu_shares:
        ```

    ??? variable string "`mqtt_role_docker_cpus`"

        ```yaml
        # Type: string
        mqtt_role_docker_cpus:
        ```

    ??? variable string "`mqtt_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        mqtt_role_docker_cpuset_cpus:
        ```

    ??? variable string "`mqtt_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        mqtt_role_docker_cpuset_mems:
        ```

    ??? variable string "`mqtt_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        mqtt_role_docker_kernel_memory:
        ```

    ??? variable string "`mqtt_role_docker_memory`"

        ```yaml
        # Type: string
        mqtt_role_docker_memory:
        ```

    ??? variable string "`mqtt_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        mqtt_role_docker_memory_reservation:
        ```

    ??? variable string "`mqtt_role_docker_memory_swap`"

        ```yaml
        # Type: string
        mqtt_role_docker_memory_swap:
        ```

    ??? variable int "`mqtt_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        mqtt_role_docker_memory_swappiness:
        ```

    ??? variable string "`mqtt_role_docker_shm_size`"

        ```yaml
        # Type: string
        mqtt_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`mqtt_role_docker_cap_drop`"

        ```yaml
        # Type: list
        mqtt_role_docker_cap_drop:
        ```

    ??? variable string "`mqtt_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        mqtt_role_docker_cgroupns_mode:
        ```

    ??? variable list "`mqtt_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        mqtt_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`mqtt_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        mqtt_role_docker_device_read_bps:
        ```

    ??? variable list "`mqtt_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        mqtt_role_docker_device_read_iops:
        ```

    ??? variable list "`mqtt_role_docker_device_requests`"

        ```yaml
        # Type: list
        mqtt_role_docker_device_requests:
        ```

    ??? variable list "`mqtt_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        mqtt_role_docker_device_write_bps:
        ```

    ??? variable list "`mqtt_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        mqtt_role_docker_device_write_iops:
        ```

    ??? variable list "`mqtt_role_docker_devices`"

        ```yaml
        # Type: list
        mqtt_role_docker_devices:
        ```

    ??? variable string "`mqtt_role_docker_devices_default`"

        ```yaml
        # Type: string
        mqtt_role_docker_devices_default:
        ```

    ??? variable list "`mqtt_role_docker_groups`"

        ```yaml
        # Type: list
        mqtt_role_docker_groups:
        ```

    ??? variable bool "`mqtt_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_privileged:
        ```

    ??? variable list "`mqtt_role_docker_security_opts`"

        ```yaml
        # Type: list
        mqtt_role_docker_security_opts:
        ```

    ??? variable string "`mqtt_role_docker_userns_mode`"

        ```yaml
        # Type: string
        mqtt_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`mqtt_role_docker_dns_opts`"

        ```yaml
        # Type: list
        mqtt_role_docker_dns_opts:
        ```

    ??? variable list "`mqtt_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        mqtt_role_docker_dns_search_domains:
        ```

    ??? variable list "`mqtt_role_docker_dns_servers`"

        ```yaml
        # Type: list
        mqtt_role_docker_dns_servers:
        ```

    ??? variable string "`mqtt_role_docker_domainname`"

        ```yaml
        # Type: string
        mqtt_role_docker_domainname:
        ```

    ??? variable list "`mqtt_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        mqtt_role_docker_exposed_ports:
        ```

    ??? variable dict "`mqtt_role_docker_hosts`"

        ```yaml
        # Type: dict
        mqtt_role_docker_hosts:
        ```

    ??? variable bool "`mqtt_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_hosts_use_common:
        ```

    ??? variable string "`mqtt_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        mqtt_role_docker_ipc_mode:
        ```

    ??? variable list "`mqtt_role_docker_links`"

        ```yaml
        # Type: list
        mqtt_role_docker_links:
        ```

    ??? variable string "`mqtt_role_docker_network_mode`"

        ```yaml
        # Type: string
        mqtt_role_docker_network_mode:
        ```

    ??? variable string "`mqtt_role_docker_pid_mode`"

        ```yaml
        # Type: string
        mqtt_role_docker_pid_mode:
        ```

    ??? variable list "`mqtt_role_docker_ports`"

        ```yaml
        # Type: list
        mqtt_role_docker_ports:
        ```

    ??? variable string "`mqtt_role_docker_uts`"

        ```yaml
        # Type: string
        mqtt_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`mqtt_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_keep_volumes:
        ```

    ??? variable list "`mqtt_role_docker_mounts`"

        ```yaml
        # Type: list
        mqtt_role_docker_mounts:
        ```

    ??? variable dict "`mqtt_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        mqtt_role_docker_storage_opts:
        ```

    ??? variable list "`mqtt_role_docker_tmpfs`"

        ```yaml
        # Type: list
        mqtt_role_docker_tmpfs:
        ```

    ??? variable string "`mqtt_role_docker_volume_driver`"

        ```yaml
        # Type: string
        mqtt_role_docker_volume_driver:
        ```

    ??? variable list "`mqtt_role_docker_volumes_from`"

        ```yaml
        # Type: list
        mqtt_role_docker_volumes_from:
        ```

    ??? variable bool "`mqtt_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_volumes_global:
        ```

    ??? variable string "`mqtt_role_docker_working_dir`"

        ```yaml
        # Type: string
        mqtt_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`mqtt_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_auto_remove:
        ```

    ??? variable bool "`mqtt_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_cleanup:
        ```

    ??? variable string "`mqtt_role_docker_force_kill`"

        ```yaml
        # Type: string
        mqtt_role_docker_force_kill:
        ```

    ??? variable dict "`mqtt_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        mqtt_role_docker_healthcheck:
        ```

    ??? variable int "`mqtt_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        mqtt_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`mqtt_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_init:
        ```

    ??? variable string "`mqtt_role_docker_kill_signal`"

        ```yaml
        # Type: string
        mqtt_role_docker_kill_signal:
        ```

    ??? variable string "`mqtt_role_docker_log_driver`"

        ```yaml
        # Type: string
        mqtt_role_docker_log_driver:
        ```

    ??? variable dict "`mqtt_role_docker_log_options`"

        ```yaml
        # Type: dict
        mqtt_role_docker_log_options:
        ```

    ??? variable bool "`mqtt_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_oom_killer:
        ```

    ??? variable int "`mqtt_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        mqtt_role_docker_oom_score_adj:
        ```

    ??? variable bool "`mqtt_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_output_logs:
        ```

    ??? variable bool "`mqtt_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_paused:
        ```

    ??? variable bool "`mqtt_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_recreate:
        ```

    ??? variable int "`mqtt_role_docker_restart_retries`"

        ```yaml
        # Type: int
        mqtt_role_docker_restart_retries:
        ```

    ??? variable int "`mqtt_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        mqtt_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`mqtt_role_docker_capabilities`"

        ```yaml
        # Type: list
        mqtt_role_docker_capabilities:
        ```

    ??? variable string "`mqtt_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        mqtt_role_docker_cgroup_parent:
        ```

    ??? variable list "`mqtt_role_docker_commands`"

        ```yaml
        # Type: list
        mqtt_role_docker_commands:
        ```

    ??? variable int "`mqtt_role_docker_create_timeout`"

        ```yaml
        # Type: int
        mqtt_role_docker_create_timeout:
        ```

    ??? variable string "`mqtt_role_docker_entrypoint`"

        ```yaml
        # Type: string
        mqtt_role_docker_entrypoint:
        ```

    ??? variable string "`mqtt_role_docker_env_file`"

        ```yaml
        # Type: string
        mqtt_role_docker_env_file:
        ```

    ??? variable dict "`mqtt_role_docker_labels`"

        ```yaml
        # Type: dict
        mqtt_role_docker_labels:
        ```

    ??? variable bool "`mqtt_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_labels_use_common:
        ```

    ??? variable bool "`mqtt_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_read_only:
        ```

    ??? variable string "`mqtt_role_docker_runtime`"

        ```yaml
        # Type: string
        mqtt_role_docker_runtime:
        ```

    ??? variable list "`mqtt_role_docker_sysctls`"

        ```yaml
        # Type: list
        mqtt_role_docker_sysctls:
        ```

    ??? variable list "`mqtt_role_docker_ulimits`"

        ```yaml
        # Type: list
        mqtt_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`mqtt_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        mqtt_role_autoheal_enabled: true
        ```

    ??? variable string "`mqtt_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        mqtt_role_depends_on: ""
        ```

    ??? variable string "`mqtt_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        mqtt_role_depends_on_delay: "0"
        ```

    ??? variable string "`mqtt_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mqtt_role_depends_on_healthchecks:
        ```

    ??? variable bool "`mqtt_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        mqtt_role_diun_enabled: true
        ```

    ??? variable bool "`mqtt_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        mqtt_role_docker_controller: true
        ```

    ??? variable list "`mqtt_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        mqtt_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`mqtt_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
