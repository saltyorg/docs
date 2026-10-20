---
icon: material/docker
title: Arcane Agent
hide:
  - tags
tags:
  - arcane
  - agent
saltbox_automation:
  app_links:
    - name: Manual
      url: https://getarcane.app/docs/remote/environments
      type: documentation
      purpose: manual
    - name: Image tags
      url: https://github.com/getarcaneapp/agent/pkgs/container/agent
      type: github
      purpose: release
    - name: Community
      url: https://discord.gg/WyXYpdyV3Z
      type: community
      purpose: community
  project_description:
    name: Arcane Agent
    summary: a lightweight, headless process that runs on a remote Docker host to allow the central Arcane Manager to manage that host’s containers, images, volumes, and networks through a single unified interface.
    link: https://getarcane.app
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Arcane Agent

## Overview

[Arcane Agent](https://getarcane.app) is a lightweight, headless process that runs on a remote Docker host to allow the central Arcane Manager to manage that host’s containers, images, volumes, and networks through a single unified interface.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://getarcane.app/docs/remote/environments){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Image tags**](https://github.com/getarcaneapp/agent/pkgs/container/agent){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://discord.gg/WyXYpdyV3Z){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install arcane-agent
```

## Usage

Access [Arcane Manager](arcane.md) and register the agent as a remote environment.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        arcane_agent_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `arcane_agent_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `arcane_agent_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`arcane_agent_name`"

        ```yaml
        # Type: string
        arcane_agent_name: arcane-agent
        ```

=== "Settings"

    ??? variable string "`arcane_agent_role_manager_url`"

        ```yaml
        # Public HTTPS base URL of the Arcane manager, for example https://arcane.example.com.
        # Type: string
        arcane_agent_role_manager_url: ""
        ```

    ??? variable string "`arcane_agent_role_token`"

        ```yaml
        # Create an Edge environment in the manager and copy its generated agent token here.
        # Use a different token for each agent. It is passed to the container as AGENT_TOKEN.
        # After regenerating the token in Arcane, update this value and reinstall the agent.
        # Type: string
        arcane_agent_role_token: ""
        ```

    ??? variable string "`arcane_agent_role_transport`"

        ```yaml
        # WebSocket keeps an outbound HTTPS connection open and needs no inbound agent port,
        # gRPC router or Traefik entrypoint timeout changes. Other supported values are auto,
        # grpc and poll. Auto prefers gRPC with WebSocket fallback; grpc disables fallback.
        # Poll opens a gRPC or WebSocket tunnel on demand. Using gRPC requires an h2c router
        # and a disabled read timeout on the manager's HTTPS entrypoint.
        # Type: string
        arcane_agent_role_transport: websocket
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`arcane_agent_role_docker_container`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_container: "{{ arcane_agent_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`arcane_agent_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_image_pull: true
        ```

    ??? variable string "`arcane_agent_role_docker_image_repo`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_image_repo: "ghcr.io/getarcaneapp/agent"
        ```

    ??? variable string "`arcane_agent_role_docker_image_tag`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_image_tag: "latest"
        ```

    ??? variable string "`arcane_agent_role_docker_image`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='arcane_agent') }}:{{ lookup('role_var', '_docker_image_tag', role='arcane_agent') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`arcane_agent_role_docker_envs_default`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          EDGE_AGENT: "true"
          EDGE_TRANSPORT: "{{ lookup('role_var', '_transport', role='arcane_agent') }}"
          MANAGER_API_URL: "{{ lookup('role_var', '_manager_url', role='arcane_agent') }}"
          AGENT_TOKEN: "{{ lookup('role_var', '_token', role='arcane_agent') }}"
          PROJECTS_DIRECTORY: "{{ lookup('role_var', '_paths_projects_location', role='arcane_agent') }}"
        ```

    ??? variable dict "`arcane_agent_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable bool "`arcane_agent_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_volumes_global: false
        ```

    ??? variable list "`arcane_agent_role_docker_volumes_default`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_data_location', role='arcane_agent') }}:/app/data"
          - "{{ lookup('role_var', '_paths_projects_location', role='arcane_agent') }}:{{ lookup('role_var', '_paths_projects_location', role='arcane_agent') }}"
          - "/var/run/docker.sock:/var/run/docker.sock"
        ```

    ??? variable list "`arcane_agent_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_volumes_custom: []
        ```

    <h5>Cgroup namespace</h5>

    ??? variable string "`arcane_agent_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_cgroupns_mode: host
        ```

    <h5>Healthcheck</h5>

    ??? variable dict "`arcane_agent_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_healthcheck:
          test:
            - CMD
            - ./arcane-agent
            - health
            - --timeout
            - 2s
          interval: 10s
          timeout: 3s
          retries: 5
          start_period: 15s
        ```

    <h5>Hostname</h5>

    ??? variable string "`arcane_agent_role_docker_hostname`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_hostname: "{{ arcane_agent_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`arcane_agent_role_docker_networks_alias`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_networks_alias: "{{ arcane_agent_name }}"
        ```

    ??? variable list "`arcane_agent_role_docker_networks_default`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_networks_default: []
        ```

    ??? variable list "`arcane_agent_role_docker_networks_custom`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`arcane_agent_role_docker_restart_policy`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_restart_policy: unless-stopped
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    A blank value is YAML null and inherits any lower-precedence role or shared default. Explicit Ansible omit is accepted only for optional Docker settings; default-backed and required settings reject it. Use the documented typed empty value, such as `""`, `[]`, or `{}`, when disabling a guaranteed setting.

    <h5>GPU</h5>

    ??? variable bool "`arcane_agent_role_docker_gpu_enabled`"

        ```yaml
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        arcane_agent_role_docker_gpu_enabled: false
        ```

    ??? variable bool "`arcane_agent_role_docker_nvidia_disabled`"

        ```yaml
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        arcane_agent_role_docker_nvidia_disabled: false
        ```

    ??? variable bool "`arcane_agent_role_docker_dev_dri_disabled`"

        ```yaml
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        arcane_agent_role_docker_dev_dri_disabled: false
        ```

    <h5>Resource Limits</h5>

    ??? variable int "`arcane_agent_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_blkio_weight:
        ```

    ??? variable int "`arcane_agent_role_docker_cpu_period`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_cpu_period:
        ```

    ??? variable int "`arcane_agent_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_cpu_quota:
        ```

    ??? variable int "`arcane_agent_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_cpu_shares:
        ```

    ??? variable string "`arcane_agent_role_docker_cpus`"

        ```yaml
        # CPU allocation accepted as a numeric string, such as 1.5
        # Type: string (quoted number)
        arcane_agent_role_docker_cpus:
        ```

    ??? variable string "`arcane_agent_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_cpuset_cpus:
        ```

    ??? variable string "`arcane_agent_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_cpuset_mems:
        ```

    ??? variable string "`arcane_agent_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_kernel_memory:
        ```

    ??? variable string "`arcane_agent_role_docker_memory`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_memory:
        ```

    ??? variable string "`arcane_agent_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_memory_reservation:
        ```

    ??? variable string "`arcane_agent_role_docker_memory_swap`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_memory_swap:
        ```

    ??? variable int "`arcane_agent_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_memory_swappiness:
        ```

    ??? variable string "`arcane_agent_role_docker_shm_size`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`arcane_agent_role_docker_cap_drop`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_cap_drop:
        ```

    ??? variable list "`arcane_agent_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`arcane_agent_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_device_read_bps:
        ```

    ??? variable list "`arcane_agent_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_device_read_iops:
        ```

    ??? variable list "`arcane_agent_role_docker_device_requests`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_device_requests:
        ```

    ??? variable list "`arcane_agent_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_device_write_bps:
        ```

    ??? variable list "`arcane_agent_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_device_write_iops:
        ```

    ??? variable list "`arcane_agent_role_docker_devices`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_devices:
        ```

    ??? variable list "`arcane_agent_role_docker_groups`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_groups:
        ```

    ??? variable bool "`arcane_agent_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_privileged:
        ```

    ??? variable list "`arcane_agent_role_docker_security_opts`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_security_opts:
        ```

    ??? variable string "`arcane_agent_role_docker_user`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_user:
        ```

    ??? variable string "`arcane_agent_role_docker_userns_mode`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`arcane_agent_role_docker_dns_opts`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_dns_opts:
        ```

    ??? variable list "`arcane_agent_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_dns_search_domains:
        ```

    ??? variable list "`arcane_agent_role_docker_dns_servers`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_dns_servers:
        ```

    ??? variable string "`arcane_agent_role_docker_domainname`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_domainname:
        ```

    ??? variable list "`arcane_agent_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_exposed_ports:
        ```

    ??? variable dict "`arcane_agent_role_docker_hosts`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_hosts:
        ```

    ??? variable bool "`arcane_agent_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_hosts_use_common:
        ```

    ??? variable string "`arcane_agent_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_ipc_mode:
        ```

    ??? variable list "`arcane_agent_role_docker_links`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_links:
        ```

    ??? variable string "`arcane_agent_role_docker_network_mode`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_network_mode:
        ```

    ??? variable string "`arcane_agent_role_docker_pid_mode`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_pid_mode:
        ```

    ??? variable list "`arcane_agent_role_docker_ports`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_ports:
        ```

    ??? variable string "`arcane_agent_role_docker_uts`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`arcane_agent_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_keep_volumes:
        ```

    ??? variable list "`arcane_agent_role_docker_mounts`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_mounts:
        ```

    ??? variable dict "`arcane_agent_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_storage_opts:
        ```

    ??? variable list "`arcane_agent_role_docker_tmpfs`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_tmpfs:
        ```

    ??? variable string "`arcane_agent_role_docker_volume_driver`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_volume_driver:
        ```

    ??? variable list "`arcane_agent_role_docker_volumes_from`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_volumes_from:
        ```

    ??? variable string "`arcane_agent_role_docker_working_dir`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`arcane_agent_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_auto_remove:
        ```

    ??? variable bool "`arcane_agent_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_cleanup:
        ```

    ??? variable bool "`arcane_agent_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_force_kill:
        ```

    ??? variable int "`arcane_agent_role_docker_healthy_wait_timeout`"

        ```yaml
        # Healthy-state wait timeout in seconds
        # Type: int
        arcane_agent_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`arcane_agent_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_init:
        ```

    ??? variable string "`arcane_agent_role_docker_kill_signal`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_kill_signal:
        ```

    ??? variable string "`arcane_agent_role_docker_log_driver`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_log_driver:
        ```

    ??? variable dict "`arcane_agent_role_docker_log_options`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_log_options:
        ```

    ??? variable bool "`arcane_agent_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_oom_killer:
        ```

    ??? variable int "`arcane_agent_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_oom_score_adj:
        ```

    ??? variable bool "`arcane_agent_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_output_logs:
        ```

    ??? variable bool "`arcane_agent_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_paused:
        ```

    ??? variable bool "`arcane_agent_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_recreate:
        ```

    ??? variable int "`arcane_agent_role_docker_restart_retries`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_restart_retries:
        ```

    ??? variable string "`arcane_agent_role_docker_stop_signal`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_stop_signal:
        ```

    ??? variable int "`arcane_agent_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`arcane_agent_role_docker_capabilities`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_capabilities:
        ```

    ??? variable string "`arcane_agent_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_cgroup_parent:
        ```

    ??? variable list "`arcane_agent_role_docker_commands`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_commands:
        ```

    ??? variable int "`arcane_agent_role_docker_create_timeout`"

        ```yaml
        # Type: int
        arcane_agent_role_docker_create_timeout:
        ```

    ??? variable list "`arcane_agent_role_docker_entrypoint`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_entrypoint:
        ```

    ??? variable string "`arcane_agent_role_docker_env_file`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_env_file:
        ```

    ??? variable dict "`arcane_agent_role_docker_labels`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_labels:
        ```

    ??? variable bool "`arcane_agent_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_labels_use_common:
        ```

    ??? variable bool "`arcane_agent_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_read_only:
        ```

    ??? variable string "`arcane_agent_role_docker_runtime`"

        ```yaml
        # Type: string
        arcane_agent_role_docker_runtime:
        ```

    ??? variable dict "`arcane_agent_role_docker_sysctls`"

        ```yaml
        # Type: dict
        arcane_agent_role_docker_sysctls:
        ```

    ??? variable list "`arcane_agent_role_docker_ulimits`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`arcane_agent_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        arcane_agent_role_autoheal_enabled: true
        ```

    ??? variable string "`arcane_agent_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        arcane_agent_role_depends_on: ""
        ```

    ??? variable string "`arcane_agent_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        arcane_agent_role_depends_on_delay: "0"
        ```

    ??? variable string "`arcane_agent_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        arcane_agent_role_depends_on_healthchecks:
        ```

    ??? variable bool "`arcane_agent_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        arcane_agent_role_diun_enabled: true
        ```

    ??? variable bool "`arcane_agent_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        arcane_agent_role_docker_controller: true
        ```

    ??? variable list "`arcane_agent_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        arcane_agent_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`arcane_agent_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        arcane_agent_role_docker_volumes_download:
        ```

    ??? variable list "`arcane_agent_role_paths_folders_list_custom`"

        ```yaml
        # Extra directories to create
        # Type: list
        arcane_agent_role_paths_folders_list_custom:
        ```

    ??? variable string "`arcane_agent_role_paths_group`"

        ```yaml
        # Group for directories created by the role
        # Type: string
        arcane_agent_role_paths_group:
        ```

    ??? variable string "`arcane_agent_role_paths_owner`"

        ```yaml
        # Owner for directories created by the role
        # Type: string
        arcane_agent_role_paths_owner:
        ```

    ??? variable string "`arcane_agent_role_paths_permissions`"

        ```yaml
        # Permissions for directories created by the role
        # Type: string
        arcane_agent_role_paths_permissions:
        ```

    ??? variable bool "`arcane_agent_role_paths_recursive`"

        ```yaml
        # Apply owner and group recursively without changing child modes
        # Type: bool (true/false)
        arcane_agent_role_paths_recursive:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
