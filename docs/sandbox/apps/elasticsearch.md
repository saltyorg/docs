---
icon: material/docker
hide:
  - tags
tags:
  - elasticsearch
  - search
  - analytics
saltbox_automation:
  app_links:
    - name: Manual
      url: https://www.elastic.co/docs
      type: documentation
    - name: Releases
      url: https://hub.docker.com/_/elasticsearch/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Elasticsearch
    summary: |
      an open source distributed, RESTful search and analytics engine, scalable data store, and vector database capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data for lightning-fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.
    link: https://www.elastic.co/elasticsearch
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Elasticsearch

## Overview

[Elasticsearch](https://www.elastic.co/elasticsearch) is an open source distributed, RESTful search and analytics engine, scalable data store, and vector database capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data for lightning-fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://www.elastic.co/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/elasticsearch/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! info
    Elasticsearch is typically not a standalone app, it is run in tandem with another role to enable features.

## Deployment

```shell
sb install sandbox-elasticsearch
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        elasticsearch_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `elasticsearch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `elasticsearch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`elasticsearch_name`"

        ```yaml
        # Type: string
        elasticsearch_name: elasticsearch
        ```

=== "Settings"

    ??? variable string "`elasticsearch_role_docker_env_password`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_password: "elastic789"
        ```

    ??? variable string "`elasticsearch_role_docker_env_http_port`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_http_port: "9200"
        ```

    ??? variable string "`elasticsearch_role_docker_env_transport_port`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_transport_port: "9300"
        ```

    ??? variable string "`elasticsearch_role_sysctl_vm_max_map_count`"

        ```yaml
        # Type: string
        elasticsearch_role_sysctl_vm_max_map_count: "262144"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`elasticsearch_role_docker_container`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_container: "{{ elasticsearch_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`elasticsearch_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_image_pull: true
        ```

    ??? variable string "`elasticsearch_role_docker_image_repo`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image_repo: "docker.elastic.co/elasticsearch/elasticsearch"
        ```

    ??? variable string "`elasticsearch_role_docker_image_tag`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image_tag: "8.11.0"
        ```

    ??? variable string "`elasticsearch_role_docker_image`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='elasticsearch') }}:{{ lookup('role_var', '_docker_image_tag', role='elasticsearch') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`elasticsearch_role_docker_envs_default`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_envs_default:
          TZ: "{{ tz }}"
          discovery.type: "single-node"
          node.name: "{{ elasticsearch_name }}"
          xpack.security.enabled: "false"
          ELASTIC_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='elasticsearch') }}"
        ```

    ??? variable dict "`elasticsearch_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`elasticsearch_role_docker_volumes_default`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='elasticsearch') }}:/usr/share/elasticsearch/data"
        ```

    ??? variable list "`elasticsearch_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`elasticsearch_role_docker_hostname`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_hostname: "{{ elasticsearch_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`elasticsearch_role_docker_networks_alias`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_networks_alias: "{{ elasticsearch_name }}"
        ```

    ??? variable list "`elasticsearch_role_docker_networks_default`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_networks_default: []
        ```

    ??? variable list "`elasticsearch_role_docker_networks_custom`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`elasticsearch_role_docker_restart_policy`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`elasticsearch_role_docker_state`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`elasticsearch_role_docker_user`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_user: "{{ uid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`elasticsearch_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_blkio_weight:
        ```

    ??? variable int "`elasticsearch_role_docker_cpu_period`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_cpu_period:
        ```

    ??? variable int "`elasticsearch_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_cpu_quota:
        ```

    ??? variable int "`elasticsearch_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_cpu_shares:
        ```

    ??? variable string "`elasticsearch_role_docker_cpus`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_cpus:
        ```

    ??? variable string "`elasticsearch_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_cpuset_cpus:
        ```

    ??? variable string "`elasticsearch_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_cpuset_mems:
        ```

    ??? variable string "`elasticsearch_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_kernel_memory:
        ```

    ??? variable string "`elasticsearch_role_docker_memory`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_memory:
        ```

    ??? variable string "`elasticsearch_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_memory_reservation:
        ```

    ??? variable string "`elasticsearch_role_docker_memory_swap`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_memory_swap:
        ```

    ??? variable int "`elasticsearch_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_memory_swappiness:
        ```

    ??? variable string "`elasticsearch_role_docker_shm_size`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`elasticsearch_role_docker_cap_drop`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_cap_drop:
        ```

    ??? variable string "`elasticsearch_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_cgroupns_mode:
        ```

    ??? variable list "`elasticsearch_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`elasticsearch_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_device_read_bps:
        ```

    ??? variable list "`elasticsearch_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_device_read_iops:
        ```

    ??? variable list "`elasticsearch_role_docker_device_requests`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_device_requests:
        ```

    ??? variable list "`elasticsearch_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_device_write_bps:
        ```

    ??? variable list "`elasticsearch_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_device_write_iops:
        ```

    ??? variable list "`elasticsearch_role_docker_devices`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_devices:
        ```

    ??? variable string "`elasticsearch_role_docker_devices_default`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_devices_default:
        ```

    ??? variable list "`elasticsearch_role_docker_groups`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_groups:
        ```

    ??? variable bool "`elasticsearch_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_privileged:
        ```

    ??? variable list "`elasticsearch_role_docker_security_opts`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_security_opts:
        ```

    ??? variable string "`elasticsearch_role_docker_userns_mode`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`elasticsearch_role_docker_dns_opts`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_dns_opts:
        ```

    ??? variable list "`elasticsearch_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_dns_search_domains:
        ```

    ??? variable list "`elasticsearch_role_docker_dns_servers`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_dns_servers:
        ```

    ??? variable string "`elasticsearch_role_docker_domainname`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_domainname:
        ```

    ??? variable list "`elasticsearch_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_exposed_ports:
        ```

    ??? variable dict "`elasticsearch_role_docker_hosts`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_hosts:
        ```

    ??? variable bool "`elasticsearch_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_hosts_use_common:
        ```

    ??? variable string "`elasticsearch_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_ipc_mode:
        ```

    ??? variable list "`elasticsearch_role_docker_links`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_links:
        ```

    ??? variable string "`elasticsearch_role_docker_network_mode`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_network_mode:
        ```

    ??? variable string "`elasticsearch_role_docker_pid_mode`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_pid_mode:
        ```

    ??? variable list "`elasticsearch_role_docker_ports`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_ports:
        ```

    ??? variable string "`elasticsearch_role_docker_uts`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`elasticsearch_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_keep_volumes:
        ```

    ??? variable list "`elasticsearch_role_docker_mounts`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_mounts:
        ```

    ??? variable dict "`elasticsearch_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_storage_opts:
        ```

    ??? variable list "`elasticsearch_role_docker_tmpfs`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_tmpfs:
        ```

    ??? variable string "`elasticsearch_role_docker_volume_driver`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_volume_driver:
        ```

    ??? variable list "`elasticsearch_role_docker_volumes_from`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_volumes_from:
        ```

    ??? variable bool "`elasticsearch_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_volumes_global:
        ```

    ??? variable string "`elasticsearch_role_docker_working_dir`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`elasticsearch_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_auto_remove:
        ```

    ??? variable bool "`elasticsearch_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_cleanup:
        ```

    ??? variable string "`elasticsearch_role_docker_force_kill`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_force_kill:
        ```

    ??? variable dict "`elasticsearch_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_healthcheck:
        ```

    ??? variable int "`elasticsearch_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`elasticsearch_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_init:
        ```

    ??? variable string "`elasticsearch_role_docker_kill_signal`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_kill_signal:
        ```

    ??? variable string "`elasticsearch_role_docker_log_driver`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_log_driver:
        ```

    ??? variable dict "`elasticsearch_role_docker_log_options`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_log_options:
        ```

    ??? variable bool "`elasticsearch_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_oom_killer:
        ```

    ??? variable int "`elasticsearch_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_oom_score_adj:
        ```

    ??? variable bool "`elasticsearch_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_output_logs:
        ```

    ??? variable bool "`elasticsearch_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_paused:
        ```

    ??? variable bool "`elasticsearch_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_recreate:
        ```

    ??? variable int "`elasticsearch_role_docker_restart_retries`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_restart_retries:
        ```

    ??? variable int "`elasticsearch_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`elasticsearch_role_docker_capabilities`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_capabilities:
        ```

    ??? variable string "`elasticsearch_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_cgroup_parent:
        ```

    ??? variable list "`elasticsearch_role_docker_commands`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_commands:
        ```

    ??? variable int "`elasticsearch_role_docker_create_timeout`"

        ```yaml
        # Type: int
        elasticsearch_role_docker_create_timeout:
        ```

    ??? variable string "`elasticsearch_role_docker_entrypoint`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_entrypoint:
        ```

    ??? variable string "`elasticsearch_role_docker_env_file`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_file:
        ```

    ??? variable dict "`elasticsearch_role_docker_labels`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_labels:
        ```

    ??? variable bool "`elasticsearch_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_labels_use_common:
        ```

    ??? variable bool "`elasticsearch_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_read_only:
        ```

    ??? variable string "`elasticsearch_role_docker_runtime`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_runtime:
        ```

    ??? variable list "`elasticsearch_role_docker_sysctls`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_sysctls:
        ```

    ??? variable list "`elasticsearch_role_docker_ulimits`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`elasticsearch_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        elasticsearch_role_autoheal_enabled: true
        ```

    ??? variable string "`elasticsearch_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        elasticsearch_role_depends_on: ""
        ```

    ??? variable string "`elasticsearch_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        elasticsearch_role_depends_on_delay: "0"
        ```

    ??? variable string "`elasticsearch_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        elasticsearch_role_depends_on_healthchecks:
        ```

    ??? variable bool "`elasticsearch_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        elasticsearch_role_diun_enabled: true
        ```

    ??? variable bool "`elasticsearch_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        elasticsearch_role_docker_controller: true
        ```

    ??? variable string "`elasticsearch_role_docker_env_password`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_password:
        ```

    ??? variable string "`elasticsearch_role_docker_image_repo`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image_repo:
        ```

    ??? variable string "`elasticsearch_role_docker_image_tag`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image_tag:
        ```

    ??? variable bool "`elasticsearch_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_volumes_download:
        ```

    ??? variable string "`elasticsearch_role_paths_location`"

        ```yaml
        # Type: string
        elasticsearch_role_paths_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->