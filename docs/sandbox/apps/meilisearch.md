---
icon: material/docker
hide:
  - tags
tags:
  - meilisearch
  - search
  - database
saltbox_automation:
  app_links:
    - name: Manual
      url: https://www.meilisearch.com/docs
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/getmeili/meilisearch/tags
      type: docker
    - name: Community
      url: https://discord.meilisearch.com
      type: discord
  project_description:
    name: Meilisearch
    summary: |
      an AI powered search tool.
    link: https://www.meilisearch.com
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Meilisearch

## Overview

[Meilisearch](https://www.meilisearch.com) is an AI powered search tool.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://www.meilisearch.com/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/getmeili/meilisearch/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.meilisearch.com){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

Use the `sb inventory` system to set any environment variables that are desired.

See [Meilisearch Environment Variables](https://www.meilisearch.com/docs/learn/self_hosted/configure_meilisearch_at_launch#environment) for supported variables

## Deployment

```shell
sb install sandbox-meilisearch
```

## Usage

Port 7700 is open to the container by default. Also analytics are disabled by default.

Visit `https://www.meilisearch.com/docs`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        meilisearch_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `meilisearch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `meilisearch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`meilisearch_name`"

        ```yaml
        # Type: string
        meilisearch_name: meilisearch
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`meilisearch_role_docker_container`"

        ```yaml
        # Type: string
        meilisearch_role_docker_container: "{{ meilisearch_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`meilisearch_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_image_pull: true
        ```

    ??? variable string "`meilisearch_role_docker_image_repo`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image_repo: "getmeili/meilisearch"
        ```

    ??? variable string "`meilisearch_role_docker_image`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='meilisearch') }}:{{ lookup('role_var', '_docker_image_tag', role='meilisearch') }}"
        ```

    ??? variable string "`meilisearch_role_docker_image_tag`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image_tag: "v1.11.1"
        ```

    <h5>Envs</h5>

    ??? variable dict "`meilisearch_role_docker_envs_default`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          MEILI_NO_ANALYTICS: "true"
          MEILI_MASTER_KEY: "{{ meilisearch_saltbox_facts.facts.secret_key }}"
        ```

    ??? variable dict "`meilisearch_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`meilisearch_role_docker_volumes_default`"

        ```yaml
        # Type: list
        meilisearch_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='meilisearch') }}/data:/meili_data"
        ```

    ??? variable list "`meilisearch_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        meilisearch_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`meilisearch_role_docker_hostname`"

        ```yaml
        # Type: string
        meilisearch_role_docker_hostname: "{{ meilisearch_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`meilisearch_role_docker_networks_alias`"

        ```yaml
        # Type: string
        meilisearch_role_docker_networks_alias: "{{ meilisearch_name }}"
        ```

    ??? variable list "`meilisearch_role_docker_networks_default`"

        ```yaml
        # Type: list
        meilisearch_role_docker_networks_default: []
        ```

    ??? variable list "`meilisearch_role_docker_networks_custom`"

        ```yaml
        # Type: list
        meilisearch_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`meilisearch_role_docker_restart_policy`"

        ```yaml
        # Type: string
        meilisearch_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`meilisearch_role_docker_state`"

        ```yaml
        # Type: string
        meilisearch_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`meilisearch_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        meilisearch_role_docker_blkio_weight:
        ```

    ??? variable int "`meilisearch_role_docker_cpu_period`"

        ```yaml
        # Type: int
        meilisearch_role_docker_cpu_period:
        ```

    ??? variable int "`meilisearch_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        meilisearch_role_docker_cpu_quota:
        ```

    ??? variable int "`meilisearch_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        meilisearch_role_docker_cpu_shares:
        ```

    ??? variable string "`meilisearch_role_docker_cpus`"

        ```yaml
        # Type: string
        meilisearch_role_docker_cpus:
        ```

    ??? variable string "`meilisearch_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        meilisearch_role_docker_cpuset_cpus:
        ```

    ??? variable string "`meilisearch_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        meilisearch_role_docker_cpuset_mems:
        ```

    ??? variable string "`meilisearch_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        meilisearch_role_docker_kernel_memory:
        ```

    ??? variable string "`meilisearch_role_docker_memory`"

        ```yaml
        # Type: string
        meilisearch_role_docker_memory:
        ```

    ??? variable string "`meilisearch_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        meilisearch_role_docker_memory_reservation:
        ```

    ??? variable string "`meilisearch_role_docker_memory_swap`"

        ```yaml
        # Type: string
        meilisearch_role_docker_memory_swap:
        ```

    ??? variable int "`meilisearch_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        meilisearch_role_docker_memory_swappiness:
        ```

    ??? variable string "`meilisearch_role_docker_shm_size`"

        ```yaml
        # Type: string
        meilisearch_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`meilisearch_role_docker_cap_drop`"

        ```yaml
        # Type: list
        meilisearch_role_docker_cap_drop:
        ```

    ??? variable string "`meilisearch_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        meilisearch_role_docker_cgroupns_mode:
        ```

    ??? variable list "`meilisearch_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        meilisearch_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`meilisearch_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        meilisearch_role_docker_device_read_bps:
        ```

    ??? variable list "`meilisearch_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        meilisearch_role_docker_device_read_iops:
        ```

    ??? variable list "`meilisearch_role_docker_device_requests`"

        ```yaml
        # Type: list
        meilisearch_role_docker_device_requests:
        ```

    ??? variable list "`meilisearch_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        meilisearch_role_docker_device_write_bps:
        ```

    ??? variable list "`meilisearch_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        meilisearch_role_docker_device_write_iops:
        ```

    ??? variable list "`meilisearch_role_docker_devices`"

        ```yaml
        # Type: list
        meilisearch_role_docker_devices:
        ```

    ??? variable string "`meilisearch_role_docker_devices_default`"

        ```yaml
        # Type: string
        meilisearch_role_docker_devices_default:
        ```

    ??? variable list "`meilisearch_role_docker_groups`"

        ```yaml
        # Type: list
        meilisearch_role_docker_groups:
        ```

    ??? variable bool "`meilisearch_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_privileged:
        ```

    ??? variable list "`meilisearch_role_docker_security_opts`"

        ```yaml
        # Type: list
        meilisearch_role_docker_security_opts:
        ```

    ??? variable string "`meilisearch_role_docker_user`"

        ```yaml
        # Type: string
        meilisearch_role_docker_user:
        ```

    ??? variable string "`meilisearch_role_docker_userns_mode`"

        ```yaml
        # Type: string
        meilisearch_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`meilisearch_role_docker_dns_opts`"

        ```yaml
        # Type: list
        meilisearch_role_docker_dns_opts:
        ```

    ??? variable list "`meilisearch_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        meilisearch_role_docker_dns_search_domains:
        ```

    ??? variable list "`meilisearch_role_docker_dns_servers`"

        ```yaml
        # Type: list
        meilisearch_role_docker_dns_servers:
        ```

    ??? variable string "`meilisearch_role_docker_domainname`"

        ```yaml
        # Type: string
        meilisearch_role_docker_domainname:
        ```

    ??? variable list "`meilisearch_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        meilisearch_role_docker_exposed_ports:
        ```

    ??? variable dict "`meilisearch_role_docker_hosts`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_hosts:
        ```

    ??? variable bool "`meilisearch_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_hosts_use_common:
        ```

    ??? variable string "`meilisearch_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        meilisearch_role_docker_ipc_mode:
        ```

    ??? variable list "`meilisearch_role_docker_links`"

        ```yaml
        # Type: list
        meilisearch_role_docker_links:
        ```

    ??? variable string "`meilisearch_role_docker_network_mode`"

        ```yaml
        # Type: string
        meilisearch_role_docker_network_mode:
        ```

    ??? variable string "`meilisearch_role_docker_pid_mode`"

        ```yaml
        # Type: string
        meilisearch_role_docker_pid_mode:
        ```

    ??? variable list "`meilisearch_role_docker_ports`"

        ```yaml
        # Type: list
        meilisearch_role_docker_ports:
        ```

    ??? variable string "`meilisearch_role_docker_uts`"

        ```yaml
        # Type: string
        meilisearch_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`meilisearch_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_keep_volumes:
        ```

    ??? variable list "`meilisearch_role_docker_mounts`"

        ```yaml
        # Type: list
        meilisearch_role_docker_mounts:
        ```

    ??? variable dict "`meilisearch_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_storage_opts:
        ```

    ??? variable list "`meilisearch_role_docker_tmpfs`"

        ```yaml
        # Type: list
        meilisearch_role_docker_tmpfs:
        ```

    ??? variable string "`meilisearch_role_docker_volume_driver`"

        ```yaml
        # Type: string
        meilisearch_role_docker_volume_driver:
        ```

    ??? variable list "`meilisearch_role_docker_volumes_from`"

        ```yaml
        # Type: list
        meilisearch_role_docker_volumes_from:
        ```

    ??? variable bool "`meilisearch_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_volumes_global:
        ```

    ??? variable string "`meilisearch_role_docker_working_dir`"

        ```yaml
        # Type: string
        meilisearch_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`meilisearch_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_auto_remove:
        ```

    ??? variable bool "`meilisearch_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_cleanup:
        ```

    ??? variable string "`meilisearch_role_docker_force_kill`"

        ```yaml
        # Type: string
        meilisearch_role_docker_force_kill:
        ```

    ??? variable dict "`meilisearch_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_healthcheck:
        ```

    ??? variable int "`meilisearch_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        meilisearch_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`meilisearch_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_init:
        ```

    ??? variable string "`meilisearch_role_docker_kill_signal`"

        ```yaml
        # Type: string
        meilisearch_role_docker_kill_signal:
        ```

    ??? variable string "`meilisearch_role_docker_log_driver`"

        ```yaml
        # Type: string
        meilisearch_role_docker_log_driver:
        ```

    ??? variable dict "`meilisearch_role_docker_log_options`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_log_options:
        ```

    ??? variable bool "`meilisearch_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_oom_killer:
        ```

    ??? variable int "`meilisearch_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        meilisearch_role_docker_oom_score_adj:
        ```

    ??? variable bool "`meilisearch_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_output_logs:
        ```

    ??? variable bool "`meilisearch_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_paused:
        ```

    ??? variable bool "`meilisearch_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_recreate:
        ```

    ??? variable int "`meilisearch_role_docker_restart_retries`"

        ```yaml
        # Type: int
        meilisearch_role_docker_restart_retries:
        ```

    ??? variable int "`meilisearch_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        meilisearch_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`meilisearch_role_docker_capabilities`"

        ```yaml
        # Type: list
        meilisearch_role_docker_capabilities:
        ```

    ??? variable string "`meilisearch_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        meilisearch_role_docker_cgroup_parent:
        ```

    ??? variable list "`meilisearch_role_docker_commands`"

        ```yaml
        # Type: list
        meilisearch_role_docker_commands:
        ```

    ??? variable int "`meilisearch_role_docker_create_timeout`"

        ```yaml
        # Type: int
        meilisearch_role_docker_create_timeout:
        ```

    ??? variable string "`meilisearch_role_docker_entrypoint`"

        ```yaml
        # Type: string
        meilisearch_role_docker_entrypoint:
        ```

    ??? variable string "`meilisearch_role_docker_env_file`"

        ```yaml
        # Type: string
        meilisearch_role_docker_env_file:
        ```

    ??? variable dict "`meilisearch_role_docker_labels`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_labels:
        ```

    ??? variable bool "`meilisearch_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_labels_use_common:
        ```

    ??? variable bool "`meilisearch_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_read_only:
        ```

    ??? variable string "`meilisearch_role_docker_runtime`"

        ```yaml
        # Type: string
        meilisearch_role_docker_runtime:
        ```

    ??? variable list "`meilisearch_role_docker_sysctls`"

        ```yaml
        # Type: list
        meilisearch_role_docker_sysctls:
        ```

    ??? variable list "`meilisearch_role_docker_ulimits`"

        ```yaml
        # Type: list
        meilisearch_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`meilisearch_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        meilisearch_role_autoheal_enabled: true
        ```

    ??? variable string "`meilisearch_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        meilisearch_role_depends_on: ""
        ```

    ??? variable string "`meilisearch_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        meilisearch_role_depends_on_delay: "0"
        ```

    ??? variable string "`meilisearch_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        meilisearch_role_depends_on_healthchecks:
        ```

    ??? variable bool "`meilisearch_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        meilisearch_role_diun_enabled: true
        ```

    ??? variable bool "`meilisearch_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        meilisearch_role_docker_controller: true
        ```

    ??? variable string "`meilisearch_role_docker_image_repo`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image_repo:
        ```

    ??? variable string "`meilisearch_role_docker_image_tag`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image_tag:
        ```

    ??? variable bool "`meilisearch_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_volumes_download:
        ```

    ??? variable string "`meilisearch_role_paths_location`"

        ```yaml
        # Type: string
        meilisearch_role_paths_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->