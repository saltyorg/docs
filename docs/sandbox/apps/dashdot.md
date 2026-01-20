---
icon: material/docker
hide:
  - tags
tags:
  - dashdot
  - dashboard
  - monitoring
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/mauricenino/dashdot/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Dashdot
    summary: |-
      a simple, modern server dashboard designed with glassmorphism aesthetics, primarily intended for smaller VPS and private servers. It provides real-time system monitoring and beautiful visualizations.
    link: https://getdashdot.com/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Dashdot

## Overview

[Dashdot](https://getdashdot.com/) is a simple, modern server dashboard designed with glassmorphism aesthetics, primarily intended for smaller VPS and private servers. It provides real-time system monitoring and beautiful visualizations.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/mauricenino/dashdot/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-dashdot
```

## Usage

Visit <https://dashdot.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        dashdot_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `dashdot_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `dashdot_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`dashdot_name`"

        ```yaml
        # Type: string
        dashdot_name: dashdot
        ```

=== "Settings"

    ??? variable string "`dashdot_role_show_host`"

        ```yaml
        # Type: string
        dashdot_role_show_host: "false"
        ```

    ??? variable string "`dashdot_role_cpu_temps`"

        ```yaml
        # Type: string
        dashdot_role_cpu_temps: "false"
        ```

    ??? variable string "`dashdot_role_imperial`"

        ```yaml
        # Type: string
        dashdot_role_imperial: "false"
        ```

    ??? variable string "`dashdot_role_always_show_percentages`"

        ```yaml
        # Type: string
        dashdot_role_always_show_percentages: "false"
        ```

    ??? variable string "`dashdot_role_title`"

        ```yaml
        # Type: string
        dashdot_role_title: "dash."
        ```

    ??? variable string "`dashdot_role_widget_list`"

        ```yaml
        # Type: string
        dashdot_role_widget_list: "os,cpu,storage,ram,network"
        ```

    ??? variable string "`dashdot_role_os_label_list`"

        ```yaml
        # Type: string
        dashdot_role_os_label_list: "os,arch,up_since"
        ```

    ??? variable string "`dashdot_role_cpu_label_list`"

        ```yaml
        # Type: string
        dashdot_role_cpu_label_list: "brand,model,cores,threads,frequency"
        ```

    ??? variable string "`dashdot_role_storage_label_list`"

        ```yaml
        # Type: string
        dashdot_role_storage_label_list: "brand,size,type"
        ```

    ??? variable string "`dashdot_role_ram_label_list`"

        ```yaml
        # Type: string
        dashdot_role_ram_label_list: "brand,size,type,frequency"
        ```

    ??? variable string "`dashdot_role_network_label_list`"

        ```yaml
        # Type: string
        dashdot_role_network_label_list: "type,speed_up,speed_down,interface_speed"
        ```

    ??? variable string "`dashdot_role_gpu_label_list`"

        ```yaml
        # Type: string
        dashdot_role_gpu_label_list: "brand,model,memory"
        ```

=== "Web"

    ??? variable string "`dashdot_role_web_subdomain`"

        ```yaml
        # Type: string
        dashdot_role_web_subdomain: "{{ dashdot_name }}"
        ```

    ??? variable string "`dashdot_role_web_domain`"

        ```yaml
        # Type: string
        dashdot_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`dashdot_role_web_port`"

        ```yaml
        # Type: string
        dashdot_role_web_port: "3001"
        ```

    ??? variable string "`dashdot_role_web_url`"

        ```yaml
        # Type: string
        dashdot_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='dashdot') + '.' + lookup('role_var', '_web_domain', role='dashdot')
                               if (lookup('role_var', '_web_subdomain', role='dashdot') | length > 0)
                               else lookup('role_var', '_web_domain', role='dashdot')) }}"
        ```

=== "DNS"

    ??? variable string "`dashdot_role_dns_record`"

        ```yaml
        # Type: string
        dashdot_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dashdot') }}"
        ```

    ??? variable string "`dashdot_role_dns_zone`"

        ```yaml
        # Type: string
        dashdot_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dashdot') }}"
        ```

    ??? variable bool "`dashdot_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`dashdot_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        dashdot_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`dashdot_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        dashdot_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`dashdot_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        dashdot_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`dashdot_role_traefik_certresolver`"

        ```yaml
        # Type: string
        dashdot_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`dashdot_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_enabled: true
        ```

    ??? variable bool "`dashdot_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_api_enabled: false
        ```

    ??? variable string "`dashdot_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        dashdot_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`dashdot_role_docker_container`"

        ```yaml
        # Type: string
        dashdot_role_docker_container: "{{ dashdot_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`dashdot_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_image_pull: true
        ```

    ??? variable string "`dashdot_role_docker_image_repo`"

        ```yaml
        # Type: string
        dashdot_role_docker_image_repo: "mauricenino/dashdot"
        ```

    ??? variable string "`dashdot_role_docker_image_tag`"

        ```yaml
        # Type: string
        dashdot_role_docker_image_tag: "latest"
        ```

    ??? variable string "`dashdot_role_docker_image`"

        ```yaml
        # Type: string
        dashdot_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dashdot') }}:{{ lookup('role_var', '_docker_image_tag', role='dashdot') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`dashdot_role_docker_envs_default`"

        ```yaml
        # Type: dict
        dashdot_role_docker_envs_default:
          DASHDOT_SHOW_HOST: "{{ lookup('role_var', '_show_host', role='dashdot') }}"
          DASHDOT_CUSTOM_HOST: "{{ lookup('role_var', '_web_subdomain', role='dashdot') + '.' + lookup('role_var', '_web_domain', role='dashdot') }}"
          DASHDOT_ENABLE_CPU_TEMPS: "{{ lookup('role_var', '_cpu_temps', role='dashdot') }}"
          DASHDOT_USE_IMPERIAL: "{{ lookup('role_var', '_imperial', role='dashdot') }}"
          DASHDOT_ALWAYS_SHOW_PERCENTAGES: "{{ lookup('role_var', '_always_show_percentages', role='dashdot') }}"
          DASHDOT_PAGE_TITLE: "{{ lookup('role_var', '_title', role='dashdot') }}"
          DASHDOT_WIDGET_LIST: "{{ lookup('role_var', '_widget_list', role='dashdot') }}"
          DASHDOT_OS_LABEL_LIST: "{{ lookup('role_var', '_os_label_list', role='dashdot') }}"
          DASHDOT_CPU_LABEL_LIST: "{{ lookup('role_var', '_cpu_label_list', role='dashdot') }}"
          DASHDOT_STORAGE_LABEL_LIST: "{{ lookup('role_var', '_storage_label_list', role='dashdot') }}"
          DASHDOT_RAM_LABEL_LIST: "{{ lookup('role_var', '_ram_label_list', role='dashdot') }}"
          DASHDOT_NETWORK_LABEL_LIST: "{{ lookup('role_var', '_network_label_list', role='dashdot') }}"
          DASHDOT_GPU_LABEL_LIST: "{{ lookup('role_var', '_gpu_label_list', role='dashdot') }}"
          DASHDOT_ACCEPT_OOKLA_EULA: "true"
        ```

    ??? variable dict "`dashdot_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        dashdot_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`dashdot_role_docker_volumes_default`"

        ```yaml
        # Type: list
        dashdot_role_docker_volumes_default:
          - "/:/mnt/host:ro"
        ```

    ??? variable list "`dashdot_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        dashdot_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`dashdot_role_docker_hostname`"

        ```yaml
        # Type: string
        dashdot_role_docker_hostname: "{{ dashdot_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`dashdot_role_docker_networks_alias`"

        ```yaml
        # Type: string
        dashdot_role_docker_networks_alias: "{{ dashdot_name }}"
        ```

    ??? variable list "`dashdot_role_docker_networks_default`"

        ```yaml
        # Type: list
        dashdot_role_docker_networks_default: []
        ```

    ??? variable list "`dashdot_role_docker_networks_custom`"

        ```yaml
        # Type: list
        dashdot_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`dashdot_role_docker_restart_policy`"

        ```yaml
        # Type: string
        dashdot_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`dashdot_role_docker_state`"

        ```yaml
        # Type: string
        dashdot_role_docker_state: started
        ```

    <h5>Privileged</h5>

    ??? variable bool "`dashdot_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_privileged: true
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`dashdot_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        dashdot_role_docker_blkio_weight:
        ```

    ??? variable int "`dashdot_role_docker_cpu_period`"

        ```yaml
        # Type: int
        dashdot_role_docker_cpu_period:
        ```

    ??? variable int "`dashdot_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        dashdot_role_docker_cpu_quota:
        ```

    ??? variable int "`dashdot_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        dashdot_role_docker_cpu_shares:
        ```

    ??? variable string "`dashdot_role_docker_cpus`"

        ```yaml
        # Type: string
        dashdot_role_docker_cpus:
        ```

    ??? variable string "`dashdot_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        dashdot_role_docker_cpuset_cpus:
        ```

    ??? variable string "`dashdot_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        dashdot_role_docker_cpuset_mems:
        ```

    ??? variable string "`dashdot_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        dashdot_role_docker_kernel_memory:
        ```

    ??? variable string "`dashdot_role_docker_memory`"

        ```yaml
        # Type: string
        dashdot_role_docker_memory:
        ```

    ??? variable string "`dashdot_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        dashdot_role_docker_memory_reservation:
        ```

    ??? variable string "`dashdot_role_docker_memory_swap`"

        ```yaml
        # Type: string
        dashdot_role_docker_memory_swap:
        ```

    ??? variable int "`dashdot_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        dashdot_role_docker_memory_swappiness:
        ```

    ??? variable string "`dashdot_role_docker_shm_size`"

        ```yaml
        # Type: string
        dashdot_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`dashdot_role_docker_cap_drop`"

        ```yaml
        # Type: list
        dashdot_role_docker_cap_drop:
        ```

    ??? variable string "`dashdot_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        dashdot_role_docker_cgroupns_mode:
        ```

    ??? variable list "`dashdot_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        dashdot_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`dashdot_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        dashdot_role_docker_device_read_bps:
        ```

    ??? variable list "`dashdot_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        dashdot_role_docker_device_read_iops:
        ```

    ??? variable list "`dashdot_role_docker_device_requests`"

        ```yaml
        # Type: list
        dashdot_role_docker_device_requests:
        ```

    ??? variable list "`dashdot_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        dashdot_role_docker_device_write_bps:
        ```

    ??? variable list "`dashdot_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        dashdot_role_docker_device_write_iops:
        ```

    ??? variable list "`dashdot_role_docker_devices`"

        ```yaml
        # Type: list
        dashdot_role_docker_devices:
        ```

    ??? variable string "`dashdot_role_docker_devices_default`"

        ```yaml
        # Type: string
        dashdot_role_docker_devices_default:
        ```

    ??? variable list "`dashdot_role_docker_groups`"

        ```yaml
        # Type: list
        dashdot_role_docker_groups:
        ```

    ??? variable list "`dashdot_role_docker_security_opts`"

        ```yaml
        # Type: list
        dashdot_role_docker_security_opts:
        ```

    ??? variable string "`dashdot_role_docker_user`"

        ```yaml
        # Type: string
        dashdot_role_docker_user:
        ```

    ??? variable string "`dashdot_role_docker_userns_mode`"

        ```yaml
        # Type: string
        dashdot_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`dashdot_role_docker_dns_opts`"

        ```yaml
        # Type: list
        dashdot_role_docker_dns_opts:
        ```

    ??? variable list "`dashdot_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        dashdot_role_docker_dns_search_domains:
        ```

    ??? variable list "`dashdot_role_docker_dns_servers`"

        ```yaml
        # Type: list
        dashdot_role_docker_dns_servers:
        ```

    ??? variable string "`dashdot_role_docker_domainname`"

        ```yaml
        # Type: string
        dashdot_role_docker_domainname:
        ```

    ??? variable list "`dashdot_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        dashdot_role_docker_exposed_ports:
        ```

    ??? variable dict "`dashdot_role_docker_hosts`"

        ```yaml
        # Type: dict
        dashdot_role_docker_hosts:
        ```

    ??? variable bool "`dashdot_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_hosts_use_common:
        ```

    ??? variable string "`dashdot_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        dashdot_role_docker_ipc_mode:
        ```

    ??? variable list "`dashdot_role_docker_links`"

        ```yaml
        # Type: list
        dashdot_role_docker_links:
        ```

    ??? variable string "`dashdot_role_docker_network_mode`"

        ```yaml
        # Type: string
        dashdot_role_docker_network_mode:
        ```

    ??? variable string "`dashdot_role_docker_pid_mode`"

        ```yaml
        # Type: string
        dashdot_role_docker_pid_mode:
        ```

    ??? variable list "`dashdot_role_docker_ports`"

        ```yaml
        # Type: list
        dashdot_role_docker_ports:
        ```

    ??? variable string "`dashdot_role_docker_uts`"

        ```yaml
        # Type: string
        dashdot_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`dashdot_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_keep_volumes:
        ```

    ??? variable list "`dashdot_role_docker_mounts`"

        ```yaml
        # Type: list
        dashdot_role_docker_mounts:
        ```

    ??? variable dict "`dashdot_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        dashdot_role_docker_storage_opts:
        ```

    ??? variable list "`dashdot_role_docker_tmpfs`"

        ```yaml
        # Type: list
        dashdot_role_docker_tmpfs:
        ```

    ??? variable string "`dashdot_role_docker_volume_driver`"

        ```yaml
        # Type: string
        dashdot_role_docker_volume_driver:
        ```

    ??? variable list "`dashdot_role_docker_volumes_from`"

        ```yaml
        # Type: list
        dashdot_role_docker_volumes_from:
        ```

    ??? variable bool "`dashdot_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_volumes_global:
        ```

    ??? variable string "`dashdot_role_docker_working_dir`"

        ```yaml
        # Type: string
        dashdot_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`dashdot_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_auto_remove:
        ```

    ??? variable bool "`dashdot_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_cleanup:
        ```

    ??? variable string "`dashdot_role_docker_force_kill`"

        ```yaml
        # Type: string
        dashdot_role_docker_force_kill:
        ```

    ??? variable dict "`dashdot_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        dashdot_role_docker_healthcheck:
        ```

    ??? variable int "`dashdot_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        dashdot_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`dashdot_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_init:
        ```

    ??? variable string "`dashdot_role_docker_kill_signal`"

        ```yaml
        # Type: string
        dashdot_role_docker_kill_signal:
        ```

    ??? variable string "`dashdot_role_docker_log_driver`"

        ```yaml
        # Type: string
        dashdot_role_docker_log_driver:
        ```

    ??? variable dict "`dashdot_role_docker_log_options`"

        ```yaml
        # Type: dict
        dashdot_role_docker_log_options:
        ```

    ??? variable bool "`dashdot_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_oom_killer:
        ```

    ??? variable int "`dashdot_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        dashdot_role_docker_oom_score_adj:
        ```

    ??? variable bool "`dashdot_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_output_logs:
        ```

    ??? variable bool "`dashdot_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_paused:
        ```

    ??? variable bool "`dashdot_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_recreate:
        ```

    ??? variable int "`dashdot_role_docker_restart_retries`"

        ```yaml
        # Type: int
        dashdot_role_docker_restart_retries:
        ```

    ??? variable int "`dashdot_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        dashdot_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`dashdot_role_docker_capabilities`"

        ```yaml
        # Type: list
        dashdot_role_docker_capabilities:
        ```

    ??? variable string "`dashdot_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        dashdot_role_docker_cgroup_parent:
        ```

    ??? variable list "`dashdot_role_docker_commands`"

        ```yaml
        # Type: list
        dashdot_role_docker_commands:
        ```

    ??? variable int "`dashdot_role_docker_create_timeout`"

        ```yaml
        # Type: int
        dashdot_role_docker_create_timeout:
        ```

    ??? variable string "`dashdot_role_docker_entrypoint`"

        ```yaml
        # Type: string
        dashdot_role_docker_entrypoint:
        ```

    ??? variable string "`dashdot_role_docker_env_file`"

        ```yaml
        # Type: string
        dashdot_role_docker_env_file:
        ```

    ??? variable dict "`dashdot_role_docker_labels`"

        ```yaml
        # Type: dict
        dashdot_role_docker_labels:
        ```

    ??? variable bool "`dashdot_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_labels_use_common:
        ```

    ??? variable bool "`dashdot_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_read_only:
        ```

    ??? variable string "`dashdot_role_docker_runtime`"

        ```yaml
        # Type: string
        dashdot_role_docker_runtime:
        ```

    ??? variable list "`dashdot_role_docker_sysctls`"

        ```yaml
        # Type: list
        dashdot_role_docker_sysctls:
        ```

    ??? variable list "`dashdot_role_docker_ulimits`"

        ```yaml
        # Type: list
        dashdot_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable string "`dashdot_role_always_show_percentages`"

        ```yaml
        # Type: string
        dashdot_role_always_show_percentages:
        ```

    ??? variable bool "`dashdot_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        dashdot_role_autoheal_enabled: true
        ```

    ??? variable string "`dashdot_role_cpu_label_list`"

        ```yaml
        # Type: string
        dashdot_role_cpu_label_list:
        ```

    ??? variable string "`dashdot_role_cpu_temps`"

        ```yaml
        # Type: string
        dashdot_role_cpu_temps:
        ```

    ??? variable string "`dashdot_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        dashdot_role_depends_on: ""
        ```

    ??? variable string "`dashdot_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        dashdot_role_depends_on_delay: "0"
        ```

    ??? variable string "`dashdot_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        dashdot_role_depends_on_healthchecks:
        ```

    ??? variable bool "`dashdot_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        dashdot_role_diun_enabled: true
        ```

    ??? variable bool "`dashdot_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        dashdot_role_dns_enabled: true
        ```

    ??? variable bool "`dashdot_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        dashdot_role_docker_controller: true
        ```

    ??? variable string "`dashdot_role_docker_image_repo`"

        ```yaml
        # Type: string
        dashdot_role_docker_image_repo:
        ```

    ??? variable string "`dashdot_role_docker_image_tag`"

        ```yaml
        # Type: string
        dashdot_role_docker_image_tag:
        ```

    ??? variable bool "`dashdot_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_docker_volumes_download:
        ```

    ??? variable string "`dashdot_role_gpu_label_list`"

        ```yaml
        # Type: string
        dashdot_role_gpu_label_list:
        ```

    ??? variable string "`dashdot_role_imperial`"

        ```yaml
        # Type: string
        dashdot_role_imperial:
        ```

    ??? variable string "`dashdot_role_network_label_list`"

        ```yaml
        # Type: string
        dashdot_role_network_label_list:
        ```

    ??? variable string "`dashdot_role_os_label_list`"

        ```yaml
        # Type: string
        dashdot_role_os_label_list:
        ```

    ??? variable string "`dashdot_role_ram_label_list`"

        ```yaml
        # Type: string
        dashdot_role_ram_label_list:
        ```

    ??? variable string "`dashdot_role_show_host`"

        ```yaml
        # Type: string
        dashdot_role_show_host:
        ```

    ??? variable string "`dashdot_role_storage_label_list`"

        ```yaml
        # Type: string
        dashdot_role_storage_label_list:
        ```

    ??? variable string "`dashdot_role_themepark_addons`"

        ```yaml
        # Type: string
        dashdot_role_themepark_addons:
        ```

    ??? variable string "`dashdot_role_themepark_app`"

        ```yaml
        # Type: string
        dashdot_role_themepark_app:
        ```

    ??? variable string "`dashdot_role_themepark_theme`"

        ```yaml
        # Type: string
        dashdot_role_themepark_theme:
        ```

    ??? variable string "`dashdot_role_title`"

        ```yaml
        # Type: string
        dashdot_role_title:
        ```

    ??? variable dict "`dashdot_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        dashdot_role_traefik_api_endpoint:
        ```

    ??? variable string "`dashdot_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        dashdot_role_traefik_api_middleware:
        ```

    ??? variable string "`dashdot_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        dashdot_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`dashdot_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`dashdot_role_traefik_certresolver`"

        ```yaml
        # Type: string
        dashdot_role_traefik_certresolver:
        ```

    ??? variable bool "`dashdot_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`dashdot_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        dashdot_role_traefik_middleware_http:
        ```

    ??? variable bool "`dashdot_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`dashdot_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        dashdot_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`dashdot_role_traefik_priority`"

        ```yaml
        # Type: string
        dashdot_role_traefik_priority:
        ```

    ??? variable bool "`dashdot_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        dashdot_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`dashdot_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        dashdot_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`dashdot_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        dashdot_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`dashdot_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        dashdot_role_web_api_http_port:
        ```

    ??? variable string "`dashdot_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        dashdot_role_web_api_http_scheme:
        ```

    ??? variable dict "`dashdot_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        dashdot_role_web_api_http_serverstransport:
        ```

    ??? variable string "`dashdot_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        dashdot_role_web_api_port:
        ```

    ??? variable string "`dashdot_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        dashdot_role_web_api_scheme:
        ```

    ??? variable dict "`dashdot_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        dashdot_role_web_api_serverstransport:
        ```

    ??? variable string "`dashdot_role_web_domain`"

        ```yaml
        # Type: string
        dashdot_role_web_domain:
        ```

    ??? variable list "`dashdot_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        dashdot_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            dashdot_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "dashdot2.{{ user.domain }}"
              - "dashdot.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`dashdot_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        dashdot_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            dashdot_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dashdot2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`dashdot_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        dashdot_role_web_http_port:
        ```

    ??? variable string "`dashdot_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        dashdot_role_web_http_scheme:
        ```

    ??? variable dict "`dashdot_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        dashdot_role_web_http_serverstransport:
        ```

    ??? variable string "`dashdot_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        dashdot_role_web_scheme:
        ```

    ??? variable dict "`dashdot_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        dashdot_role_web_serverstransport:
        ```

    ??? variable string "`dashdot_role_web_subdomain`"

        ```yaml
        # Type: string
        dashdot_role_web_subdomain:
        ```

    ??? variable string "`dashdot_role_widget_list`"

        ```yaml
        # Type: string
        dashdot_role_widget_list:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->