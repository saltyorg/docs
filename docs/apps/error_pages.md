---
icon: material/docker
title: Error Pages
hide:
  - tags
tags:
  - error-pages
  - traefik
  - error-handling
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/tarampampam/error-pages/blob/master/README.md#-usage-scenarios
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/tarampampam/error-pages/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Error Pages
    summary: |-
      a GitHub repository that provides visually appealing, customizable error pages for HTTP servers, Kubernetes clusters, and other systems like Traefik and Nginx.
    link: https://github.com/tarampampam/error-pages
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Error Pages

## Overview

[Error Pages](https://github.com/tarampampam/error-pages) is a GitHub repository that provides visually appealing, customizable error pages for HTTP servers, Kubernetes clusters, and other systems like Traefik and Nginx.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/tarampampam/error-pages/blob/master/README.md#-usage-scenarios){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/tarampampam/error-pages/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Installation

Enable in `adv_settings.yml`:

```yaml
traefik:
  error_pages: yes
```

Then install/update Traefik:

```shell
sb install traefik
```

## Configuration

### Change Template

Change the template in your [inventory](../saltbox/inventory/index.md):

```yaml
error_pages_role_template: "ghost"
```

Available templates: `l7` (default), `ghost`, `noise`, `hacker-terminal`, `shuffle`, `lost-in-space`, `app-down`, `connection`, and [more](https://github.com/tarampampam/error-pages).

Rebuild after changing:

```shell
sb install traefik
```

### Disable for Specific Apps

Disable error pages for specific apps in your [inventory](../saltbox/inventory/index.md):

```yaml
plex_role_traefik_error_pages_enabled: false
```

## Notes

- Error pages stored in `/opt/error-pages/`
- Pre-generated at install time from selected template
- Applied globally via Traefik middleware
- Manual edits overwritten on rebuild

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        error_pages_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `error_pages_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `error_pages_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`error_pages_name`"

        ```yaml
        # Type: string
        error_pages_name: error-pages
        ```

=== "Config"

    ??? variable string "`error_pages_role_template`"

        ```yaml
        # Template options listed here https://github.com/tarampampam/error-pages
        # Type: string
        error_pages_role_template: "l7"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`error_pages_role_docker_container`"

        ```yaml
        # Type: string
        error_pages_role_docker_container: "{{ error_pages_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`error_pages_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_image_pull: true
        ```

    ??? variable string "`error_pages_role_docker_image_repo`"

        ```yaml
        # Type: string
        error_pages_role_docker_image_repo: "tarampampam/error-pages"
        ```

    ??? variable string "`error_pages_role_docker_image_tag`"

        ```yaml
        # Type: string
        error_pages_role_docker_image_tag: "latest"
        ```

    ??? variable string "`error_pages_role_docker_image`"

        ```yaml
        # Type: string
        error_pages_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='error_pages') }}:{{ lookup('role_var', '_docker_image_tag', role='error_pages') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`error_pages_role_docker_envs_default`"

        ```yaml
        # Type: dict
        error_pages_role_docker_envs_default:
          TEMPLATE_NAME: "{{ lookup('role_var', '_template', role='error_pages') }}"
        ```

    ??? variable dict "`error_pages_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        error_pages_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`error_pages_role_docker_volumes_default`"

        ```yaml
        # Type: list
        error_pages_role_docker_volumes_default:
          - "{{ server_appdata_path }}/error-pages:/opt/html"
        ```

    ??? variable list "`error_pages_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        error_pages_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`error_pages_role_docker_labels_default`"

        ```yaml
        # Type: dict
        error_pages_role_docker_labels_default:
          traefik.enable: "true"
          traefik.http.routers.error-pages-router.rule: "PathPrefix(`/`)"
          traefik.http.routers.error-pages-router.priority: "5"
          traefik.http.routers.error-pages-router.entrypoints: "web,websecure"
          traefik.http.routers.error-pages-router.middlewares: "error-pages-middleware"
          traefik.http.middlewares.error-pages-middleware.errors.status: "400-599"
          traefik.http.middlewares.error-pages-middleware.errors.service: "error-pages-service"
          traefik.http.middlewares.error-pages-middleware.errors.query: "/{status}.html"
          traefik.http.services.error-pages-service.loadbalancer.server.port: "8080"
        ```

    ??? variable dict "`error_pages_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        error_pages_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`error_pages_role_docker_hostname`"

        ```yaml
        # Type: string
        error_pages_role_docker_hostname: "{{ error_pages_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`error_pages_role_docker_networks_alias`"

        ```yaml
        # Type: string
        error_pages_role_docker_networks_alias: "{{ error_pages_name }}"
        ```

    ??? variable list "`error_pages_role_docker_networks_default`"

        ```yaml
        # Type: list
        error_pages_role_docker_networks_default: []
        ```

    ??? variable list "`error_pages_role_docker_networks_custom`"

        ```yaml
        # Type: list
        error_pages_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`error_pages_role_docker_restart_policy`"

        ```yaml
        # Type: string
        error_pages_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`error_pages_role_docker_state`"

        ```yaml
        # Type: string
        error_pages_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`error_pages_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        error_pages_role_docker_blkio_weight:
        ```

    ??? variable int "`error_pages_role_docker_cpu_period`"

        ```yaml
        # Type: int
        error_pages_role_docker_cpu_period:
        ```

    ??? variable int "`error_pages_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        error_pages_role_docker_cpu_quota:
        ```

    ??? variable int "`error_pages_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        error_pages_role_docker_cpu_shares:
        ```

    ??? variable string "`error_pages_role_docker_cpus`"

        ```yaml
        # Type: string
        error_pages_role_docker_cpus:
        ```

    ??? variable string "`error_pages_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        error_pages_role_docker_cpuset_cpus:
        ```

    ??? variable string "`error_pages_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        error_pages_role_docker_cpuset_mems:
        ```

    ??? variable string "`error_pages_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        error_pages_role_docker_kernel_memory:
        ```

    ??? variable string "`error_pages_role_docker_memory`"

        ```yaml
        # Type: string
        error_pages_role_docker_memory:
        ```

    ??? variable string "`error_pages_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        error_pages_role_docker_memory_reservation:
        ```

    ??? variable string "`error_pages_role_docker_memory_swap`"

        ```yaml
        # Type: string
        error_pages_role_docker_memory_swap:
        ```

    ??? variable int "`error_pages_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        error_pages_role_docker_memory_swappiness:
        ```

    ??? variable string "`error_pages_role_docker_shm_size`"

        ```yaml
        # Type: string
        error_pages_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`error_pages_role_docker_cap_drop`"

        ```yaml
        # Type: list
        error_pages_role_docker_cap_drop:
        ```

    ??? variable string "`error_pages_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        error_pages_role_docker_cgroupns_mode:
        ```

    ??? variable list "`error_pages_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        error_pages_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`error_pages_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        error_pages_role_docker_device_read_bps:
        ```

    ??? variable list "`error_pages_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        error_pages_role_docker_device_read_iops:
        ```

    ??? variable list "`error_pages_role_docker_device_requests`"

        ```yaml
        # Type: list
        error_pages_role_docker_device_requests:
        ```

    ??? variable list "`error_pages_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        error_pages_role_docker_device_write_bps:
        ```

    ??? variable list "`error_pages_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        error_pages_role_docker_device_write_iops:
        ```

    ??? variable list "`error_pages_role_docker_devices`"

        ```yaml
        # Type: list
        error_pages_role_docker_devices:
        ```

    ??? variable list "`error_pages_role_docker_groups`"

        ```yaml
        # Type: list
        error_pages_role_docker_groups:
        ```

    ??? variable bool "`error_pages_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_privileged:
        ```

    ??? variable list "`error_pages_role_docker_security_opts`"

        ```yaml
        # Type: list
        error_pages_role_docker_security_opts:
        ```

    ??? variable string "`error_pages_role_docker_user`"

        ```yaml
        # Type: string
        error_pages_role_docker_user:
        ```

    ??? variable string "`error_pages_role_docker_userns_mode`"

        ```yaml
        # Type: string
        error_pages_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`error_pages_role_docker_dns_opts`"

        ```yaml
        # Type: list
        error_pages_role_docker_dns_opts:
        ```

    ??? variable list "`error_pages_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        error_pages_role_docker_dns_search_domains:
        ```

    ??? variable list "`error_pages_role_docker_dns_servers`"

        ```yaml
        # Type: list
        error_pages_role_docker_dns_servers:
        ```

    ??? variable string "`error_pages_role_docker_domainname`"

        ```yaml
        # Type: string
        error_pages_role_docker_domainname:
        ```

    ??? variable list "`error_pages_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        error_pages_role_docker_exposed_ports:
        ```

    ??? variable dict "`error_pages_role_docker_hosts`"

        ```yaml
        # Type: dict
        error_pages_role_docker_hosts:
        ```

    ??? variable bool "`error_pages_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_hosts_use_common:
        ```

    ??? variable string "`error_pages_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        error_pages_role_docker_ipc_mode:
        ```

    ??? variable list "`error_pages_role_docker_links`"

        ```yaml
        # Type: list
        error_pages_role_docker_links:
        ```

    ??? variable string "`error_pages_role_docker_network_mode`"

        ```yaml
        # Type: string
        error_pages_role_docker_network_mode:
        ```

    ??? variable string "`error_pages_role_docker_pid_mode`"

        ```yaml
        # Type: string
        error_pages_role_docker_pid_mode:
        ```

    ??? variable list "`error_pages_role_docker_ports`"

        ```yaml
        # Type: list
        error_pages_role_docker_ports:
        ```

    ??? variable string "`error_pages_role_docker_uts`"

        ```yaml
        # Type: string
        error_pages_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`error_pages_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_keep_volumes:
        ```

    ??? variable list "`error_pages_role_docker_mounts`"

        ```yaml
        # Type: list
        error_pages_role_docker_mounts:
        ```

    ??? variable dict "`error_pages_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        error_pages_role_docker_storage_opts:
        ```

    ??? variable list "`error_pages_role_docker_tmpfs`"

        ```yaml
        # Type: list
        error_pages_role_docker_tmpfs:
        ```

    ??? variable string "`error_pages_role_docker_volume_driver`"

        ```yaml
        # Type: string
        error_pages_role_docker_volume_driver:
        ```

    ??? variable list "`error_pages_role_docker_volumes_from`"

        ```yaml
        # Type: list
        error_pages_role_docker_volumes_from:
        ```

    ??? variable bool "`error_pages_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_volumes_global:
        ```

    ??? variable string "`error_pages_role_docker_working_dir`"

        ```yaml
        # Type: string
        error_pages_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`error_pages_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_auto_remove:
        ```

    ??? variable bool "`error_pages_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_cleanup:
        ```

    ??? variable string "`error_pages_role_docker_force_kill`"

        ```yaml
        # Type: string
        error_pages_role_docker_force_kill:
        ```

    ??? variable dict "`error_pages_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        error_pages_role_docker_healthcheck:
        ```

    ??? variable int "`error_pages_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        error_pages_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`error_pages_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_init:
        ```

    ??? variable string "`error_pages_role_docker_kill_signal`"

        ```yaml
        # Type: string
        error_pages_role_docker_kill_signal:
        ```

    ??? variable string "`error_pages_role_docker_log_driver`"

        ```yaml
        # Type: string
        error_pages_role_docker_log_driver:
        ```

    ??? variable dict "`error_pages_role_docker_log_options`"

        ```yaml
        # Type: dict
        error_pages_role_docker_log_options:
        ```

    ??? variable bool "`error_pages_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_oom_killer:
        ```

    ??? variable int "`error_pages_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        error_pages_role_docker_oom_score_adj:
        ```

    ??? variable bool "`error_pages_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_output_logs:
        ```

    ??? variable bool "`error_pages_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_paused:
        ```

    ??? variable bool "`error_pages_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_recreate:
        ```

    ??? variable int "`error_pages_role_docker_restart_retries`"

        ```yaml
        # Type: int
        error_pages_role_docker_restart_retries:
        ```

    ??? variable string "`error_pages_role_docker_stop_signal`"

        ```yaml
        # Type: string
        error_pages_role_docker_stop_signal:
        ```

    ??? variable int "`error_pages_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        error_pages_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`error_pages_role_docker_capabilities`"

        ```yaml
        # Type: list
        error_pages_role_docker_capabilities:
        ```

    ??? variable string "`error_pages_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        error_pages_role_docker_cgroup_parent:
        ```

    ??? variable list "`error_pages_role_docker_commands`"

        ```yaml
        # Type: list
        error_pages_role_docker_commands:
        ```

    ??? variable int "`error_pages_role_docker_create_timeout`"

        ```yaml
        # Type: int
        error_pages_role_docker_create_timeout:
        ```

    ??? variable string "`error_pages_role_docker_dev_dri`"

        ```yaml
        # Type: string
        error_pages_role_docker_dev_dri:
        ```

    ??? variable string "`error_pages_role_docker_entrypoint`"

        ```yaml
        # Type: string
        error_pages_role_docker_entrypoint:
        ```

    ??? variable string "`error_pages_role_docker_env_file`"

        ```yaml
        # Type: string
        error_pages_role_docker_env_file:
        ```

    ??? variable bool "`error_pages_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_labels_use_common:
        ```

    ??? variable bool "`error_pages_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_read_only:
        ```

    ??? variable string "`error_pages_role_docker_runtime`"

        ```yaml
        # Type: string
        error_pages_role_docker_runtime:
        ```

    ??? variable list "`error_pages_role_docker_sysctls`"

        ```yaml
        # Type: list
        error_pages_role_docker_sysctls:
        ```

    ??? variable list "`error_pages_role_docker_ulimits`"

        ```yaml
        # Type: list
        error_pages_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`error_pages_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        error_pages_role_autoheal_enabled: true
        ```

    ??? variable string "`error_pages_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        error_pages_role_depends_on: ""
        ```

    ??? variable string "`error_pages_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        error_pages_role_depends_on_delay: "0"
        ```

    ??? variable string "`error_pages_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        error_pages_role_depends_on_healthchecks:
        ```

    ??? variable bool "`error_pages_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        error_pages_role_diun_enabled: true
        ```

    ??? variable bool "`error_pages_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        error_pages_role_docker_controller: true
        ```

    ??? variable list "`error_pages_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        error_pages_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`error_pages_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        error_pages_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
