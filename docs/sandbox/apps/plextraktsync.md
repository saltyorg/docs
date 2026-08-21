---
icon: material/docker
title: Plex-Trakt-Sync
hide:
  - tags
tags:
  - plextraktsync
  - trakt
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/Taxel/PlexTraktSync/blob/main/README.md#setup
      type: documentation
    - name: Releases
      url: https://github.com/linuxserver-labs/docker-plextraktsync/pkgs/container/plextraktsync
      type: github
    - name: Community
      url: https://github.com/Taxel/PlexTraktSync/discussions
      type: github
  project_description:
    name: Plex-Trakt-Sync
    summary: |-
      a two-way synchronization tool between trakt.tv and Plex Media Server, allowing users to sync media collections, ratings, watched status, and watchlists without requiring a Plex Pass or Trakt VIP subscription.
    link: https://github.com/Taxel/PlexTraktSync
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Plex-Trakt-Sync

## Overview

[Plex-Trakt-Sync](https://github.com/Taxel/PlexTraktSync) is a two-way synchronization tool between trakt.tv and Plex Media Server, allowing users to sync media collections, ratings, watched status, and watchlists without requiring a Plex Pass or Trakt VIP subscription.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/Taxel/PlexTraktSync/blob/main/README.md#setup){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/linuxserver-labs/docker-plextraktsync/pkgs/container/plextraktsync){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/Taxel/PlexTraktSync/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Pre-Deployment

If you need more than one Plex-Trakt account pair processed, that can be achieved through multiple instances, e.g.:

```yaml
plextraktsync_instances: ['plextraktsync-seed', 'plextraktsync-alice', 'plextraktsync-charlie']
```

## Deployment

```shell
sb install sandbox-plextraktsync
```

## Usage

```shell
docker exec plextraktsync plextraktsync --help
```

### Finishing the setup

The role sets the target Plex server to your Saltbox Plex instance if deployed. To add the missing Trakt.tv credentials, you can run:

```shell
docker exec -it plextraktsync plextraktsync login
```

### Resetting Plex credentials

```shell
docker exec -it plextraktsync plextraktsync plex-login
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override scope"><input type="checkbox" name="scope" hidden/></label>

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `plextraktsync_instances`.**

    !!! example "Example override"

        === "Role-scoped"

            ```yaml
            plextraktsync_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of plextraktsync

        === "Instance-scoped"

            ```yaml
            plextraktsync2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named plextraktsync2

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `plextraktsync_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `plextraktsync_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`plextraktsync_instances`"

        ```yaml
        # Type: list
        plextraktsync_instances: ['plextraktsync']
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            plextraktsync_instances: ["plextraktsync", "plextraktsync2"]
            ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`plextraktsync_role_docker_container`{ .sb-show-on-unchecked }`plextraktsync2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_container: "{{ plextraktsync_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_container: "{{ plextraktsync_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`plextraktsync_role_docker_image_pull`{ .sb-show-on-unchecked }`plextraktsync2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_image_pull: true
        ```

    ??? variable string "`plextraktsync_role_docker_image_tag`{ .sb-show-on-unchecked }`plextraktsync2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_image_tag: "latest"
        ```

    ??? variable string "`plextraktsync_role_docker_image_repo`{ .sb-show-on-unchecked }`plextraktsync2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_image_repo: "lscr.io/linuxserver-labs/plextraktsync"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_image_repo: "lscr.io/linuxserver-labs/plextraktsync"
        ```

    ??? variable string "`plextraktsync_role_docker_image`{ .sb-show-on-unchecked }`plextraktsync2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plextraktsync') }}:{{ lookup('role_var', '_docker_image_tag', role='plextraktsync') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plextraktsync') }}:{{ lookup('role_var', '_docker_image_tag', role='plextraktsync') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`plextraktsync_role_docker_envs_default`{ .sb-show-on-unchecked }`plextraktsync2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        plextraktsync_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        plextraktsync2_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`plextraktsync_role_docker_envs_custom`{ .sb-show-on-unchecked }`plextraktsync2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        plextraktsync_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        plextraktsync2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`plextraktsync_role_docker_volumes_default`{ .sb-show-on-unchecked }`plextraktsync2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='plextraktsync') }}:/config"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='plextraktsync') }}:/config"
        ```

    ??? variable list "`plextraktsync_role_docker_volumes_custom`{ .sb-show-on-unchecked }`plextraktsync2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`plextraktsync_role_docker_hostname`{ .sb-show-on-unchecked }`plextraktsync2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_hostname: "{{ plextraktsync_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_hostname: "{{ plextraktsync_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`plextraktsync_role_docker_networks_alias`{ .sb-show-on-unchecked }`plextraktsync2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_networks_alias: "{{ plextraktsync_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_networks_alias: "{{ plextraktsync_name }}"
        ```

    ??? variable list "`plextraktsync_role_docker_networks_default`{ .sb-show-on-unchecked }`plextraktsync2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_networks_default: []
        ```

    ??? variable list "`plextraktsync_role_docker_networks_custom`{ .sb-show-on-unchecked }`plextraktsync2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`plextraktsync_role_docker_restart_policy`{ .sb-show-on-unchecked }`plextraktsync2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_restart_policy: unless-stopped
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>GPU</h5>

    ??? variable bool "`plextraktsync_role_docker_gpu_enabled`{ .sb-show-on-unchecked }`plextraktsync2_docker_gpu_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        plextraktsync_role_docker_gpu_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        plextraktsync2_docker_gpu_enabled: false
        ```

    ??? variable bool "`plextraktsync_role_docker_nvidia_disabled`{ .sb-show-on-unchecked }`plextraktsync2_docker_nvidia_disabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        plextraktsync_role_docker_nvidia_disabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        plextraktsync2_docker_nvidia_disabled: false
        ```

    ??? variable bool "`plextraktsync_role_docker_dev_dri_disabled`{ .sb-show-on-unchecked }`plextraktsync2_docker_dev_dri_disabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        plextraktsync_role_docker_dev_dri_disabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        plextraktsync2_docker_dev_dri_disabled: false
        ```

    <h5>Resource Limits</h5>

    ??? variable int "`plextraktsync_role_docker_blkio_weight`{ .sb-show-on-unchecked }`plextraktsync2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_blkio_weight:
        ```

    ??? variable int "`plextraktsync_role_docker_cpu_period`{ .sb-show-on-unchecked }`plextraktsync2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_cpu_period:
        ```

    ??? variable int "`plextraktsync_role_docker_cpu_quota`{ .sb-show-on-unchecked }`plextraktsync2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_cpu_quota:
        ```

    ??? variable int "`plextraktsync_role_docker_cpu_shares`{ .sb-show-on-unchecked }`plextraktsync2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_cpu_shares:
        ```

    ??? variable string "`plextraktsync_role_docker_cpus`{ .sb-show-on-unchecked }`plextraktsync2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_cpus:
        ```

    ??? variable string "`plextraktsync_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`plextraktsync2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_cpuset_cpus:
        ```

    ??? variable string "`plextraktsync_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`plextraktsync2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_cpuset_mems:
        ```

    ??? variable string "`plextraktsync_role_docker_kernel_memory`{ .sb-show-on-unchecked }`plextraktsync2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_kernel_memory:
        ```

    ??? variable string "`plextraktsync_role_docker_memory`{ .sb-show-on-unchecked }`plextraktsync2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_memory:
        ```

    ??? variable string "`plextraktsync_role_docker_memory_reservation`{ .sb-show-on-unchecked }`plextraktsync2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_memory_reservation:
        ```

    ??? variable string "`plextraktsync_role_docker_memory_swap`{ .sb-show-on-unchecked }`plextraktsync2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_memory_swap:
        ```

    ??? variable int "`plextraktsync_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`plextraktsync2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_memory_swappiness:
        ```

    ??? variable string "`plextraktsync_role_docker_shm_size`{ .sb-show-on-unchecked }`plextraktsync2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`plextraktsync_role_docker_cap_drop`{ .sb-show-on-unchecked }`plextraktsync2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_cap_drop:
        ```

    ??? variable string "`plextraktsync_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`plextraktsync2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_cgroupns_mode:
        ```

    ??? variable list "`plextraktsync_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`plextraktsync2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_device_cgroup_rules:
        ```

    ??? variable list "`plextraktsync_role_docker_device_read_bps`{ .sb-show-on-unchecked }`plextraktsync2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_device_read_bps:
        ```

    ??? variable list "`plextraktsync_role_docker_device_read_iops`{ .sb-show-on-unchecked }`plextraktsync2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_device_read_iops:
        ```

    ??? variable list "`plextraktsync_role_docker_device_requests`{ .sb-show-on-unchecked }`plextraktsync2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_device_requests:
        ```

    ??? variable list "`plextraktsync_role_docker_device_write_bps`{ .sb-show-on-unchecked }`plextraktsync2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_device_write_bps:
        ```

    ??? variable list "`plextraktsync_role_docker_device_write_iops`{ .sb-show-on-unchecked }`plextraktsync2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_device_write_iops:
        ```

    ??? variable list "`plextraktsync_role_docker_devices`{ .sb-show-on-unchecked }`plextraktsync2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_devices:
        ```

    ??? variable list "`plextraktsync_role_docker_groups`{ .sb-show-on-unchecked }`plextraktsync2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_groups:
        ```

    ??? variable bool "`plextraktsync_role_docker_privileged`{ .sb-show-on-unchecked }`plextraktsync2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_privileged:
        ```

    ??? variable list "`plextraktsync_role_docker_security_opts`{ .sb-show-on-unchecked }`plextraktsync2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_security_opts:
        ```

    ??? variable string "`plextraktsync_role_docker_user`{ .sb-show-on-unchecked }`plextraktsync2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_user:
        ```

    ??? variable string "`plextraktsync_role_docker_userns_mode`{ .sb-show-on-unchecked }`plextraktsync2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`plextraktsync_role_docker_dns_opts`{ .sb-show-on-unchecked }`plextraktsync2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_dns_opts:
        ```

    ??? variable list "`plextraktsync_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`plextraktsync2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_dns_search_domains:
        ```

    ??? variable list "`plextraktsync_role_docker_dns_servers`{ .sb-show-on-unchecked }`plextraktsync2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_dns_servers:
        ```

    ??? variable string "`plextraktsync_role_docker_domainname`{ .sb-show-on-unchecked }`plextraktsync2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_domainname:
        ```

    ??? variable list "`plextraktsync_role_docker_exposed_ports`{ .sb-show-on-unchecked }`plextraktsync2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_exposed_ports:
        ```

    ??? variable dict "`plextraktsync_role_docker_hosts`{ .sb-show-on-unchecked }`plextraktsync2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        plextraktsync_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        plextraktsync2_docker_hosts:
        ```

    ??? variable bool "`plextraktsync_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`plextraktsync2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_hosts_use_common:
        ```

    ??? variable string "`plextraktsync_role_docker_ipc_mode`{ .sb-show-on-unchecked }`plextraktsync2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_ipc_mode:
        ```

    ??? variable list "`plextraktsync_role_docker_links`{ .sb-show-on-unchecked }`plextraktsync2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_links:
        ```

    ??? variable string "`plextraktsync_role_docker_network_mode`{ .sb-show-on-unchecked }`plextraktsync2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_network_mode:
        ```

    ??? variable string "`plextraktsync_role_docker_pid_mode`{ .sb-show-on-unchecked }`plextraktsync2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_pid_mode:
        ```

    ??? variable list "`plextraktsync_role_docker_ports`{ .sb-show-on-unchecked }`plextraktsync2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_ports:
        ```

    ??? variable string "`plextraktsync_role_docker_uts`{ .sb-show-on-unchecked }`plextraktsync2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`plextraktsync_role_docker_keep_volumes`{ .sb-show-on-unchecked }`plextraktsync2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_keep_volumes:
        ```

    ??? variable list "`plextraktsync_role_docker_mounts`{ .sb-show-on-unchecked }`plextraktsync2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_mounts:
        ```

    ??? variable dict "`plextraktsync_role_docker_storage_opts`{ .sb-show-on-unchecked }`plextraktsync2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        plextraktsync_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        plextraktsync2_docker_storage_opts:
        ```

    ??? variable list "`plextraktsync_role_docker_tmpfs`{ .sb-show-on-unchecked }`plextraktsync2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_tmpfs:
        ```

    ??? variable string "`plextraktsync_role_docker_volume_driver`{ .sb-show-on-unchecked }`plextraktsync2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_volume_driver:
        ```

    ??? variable list "`plextraktsync_role_docker_volumes_from`{ .sb-show-on-unchecked }`plextraktsync2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_volumes_from:
        ```

    ??? variable bool "`plextraktsync_role_docker_volumes_global`{ .sb-show-on-unchecked }`plextraktsync2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_volumes_global:
        ```

    ??? variable string "`plextraktsync_role_docker_working_dir`{ .sb-show-on-unchecked }`plextraktsync2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`plextraktsync_role_docker_auto_remove`{ .sb-show-on-unchecked }`plextraktsync2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_auto_remove:
        ```

    ??? variable bool "`plextraktsync_role_docker_cleanup`{ .sb-show-on-unchecked }`plextraktsync2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_cleanup:
        ```

    ??? variable string "`plextraktsync_role_docker_force_kill`{ .sb-show-on-unchecked }`plextraktsync2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_force_kill:
        ```

    ??? variable dict "`plextraktsync_role_docker_healthcheck`{ .sb-show-on-unchecked }`plextraktsync2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        plextraktsync_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        plextraktsync2_docker_healthcheck:
        ```

    ??? variable int "`plextraktsync_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`plextraktsync2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`plextraktsync_role_docker_init`{ .sb-show-on-unchecked }`plextraktsync2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_init:
        ```

    ??? variable string "`plextraktsync_role_docker_kill_signal`{ .sb-show-on-unchecked }`plextraktsync2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_kill_signal:
        ```

    ??? variable string "`plextraktsync_role_docker_log_driver`{ .sb-show-on-unchecked }`plextraktsync2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_log_driver:
        ```

    ??? variable dict "`plextraktsync_role_docker_log_options`{ .sb-show-on-unchecked }`plextraktsync2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        plextraktsync_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        plextraktsync2_docker_log_options:
        ```

    ??? variable bool "`plextraktsync_role_docker_oom_killer`{ .sb-show-on-unchecked }`plextraktsync2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_oom_killer:
        ```

    ??? variable int "`plextraktsync_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`plextraktsync2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_oom_score_adj:
        ```

    ??? variable bool "`plextraktsync_role_docker_output_logs`{ .sb-show-on-unchecked }`plextraktsync2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_output_logs:
        ```

    ??? variable bool "`plextraktsync_role_docker_paused`{ .sb-show-on-unchecked }`plextraktsync2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_paused:
        ```

    ??? variable bool "`plextraktsync_role_docker_recreate`{ .sb-show-on-unchecked }`plextraktsync2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_recreate:
        ```

    ??? variable int "`plextraktsync_role_docker_restart_retries`{ .sb-show-on-unchecked }`plextraktsync2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_restart_retries:
        ```

    ??? variable string "`plextraktsync_role_docker_stop_signal`{ .sb-show-on-unchecked }`plextraktsync2_docker_stop_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_stop_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_stop_signal:
        ```

    ??? variable int "`plextraktsync_role_docker_stop_timeout`{ .sb-show-on-unchecked }`plextraktsync2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`plextraktsync_role_docker_capabilities`{ .sb-show-on-unchecked }`plextraktsync2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_capabilities:
        ```

    ??? variable string "`plextraktsync_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`plextraktsync2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_cgroup_parent:
        ```

    ??? variable list "`plextraktsync_role_docker_commands`{ .sb-show-on-unchecked }`plextraktsync2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_commands:
        ```

    ??? variable int "`plextraktsync_role_docker_create_timeout`{ .sb-show-on-unchecked }`plextraktsync2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        plextraktsync_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        plextraktsync2_docker_create_timeout:
        ```

    ??? variable string "`plextraktsync_role_docker_entrypoint`{ .sb-show-on-unchecked }`plextraktsync2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_entrypoint:
        ```

    ??? variable string "`plextraktsync_role_docker_env_file`{ .sb-show-on-unchecked }`plextraktsync2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_env_file:
        ```

    ??? variable dict "`plextraktsync_role_docker_labels`{ .sb-show-on-unchecked }`plextraktsync2_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        plextraktsync_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        plextraktsync2_docker_labels:
        ```

    ??? variable bool "`plextraktsync_role_docker_labels_use_common`{ .sb-show-on-unchecked }`plextraktsync2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_labels_use_common:
        ```

    ??? variable bool "`plextraktsync_role_docker_read_only`{ .sb-show-on-unchecked }`plextraktsync2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_read_only:
        ```

    ??? variable string "`plextraktsync_role_docker_runtime`{ .sb-show-on-unchecked }`plextraktsync2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        plextraktsync_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        plextraktsync2_docker_runtime:
        ```

    ??? variable list "`plextraktsync_role_docker_sysctls`{ .sb-show-on-unchecked }`plextraktsync2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_sysctls:
        ```

    ??? variable list "`plextraktsync_role_docker_ulimits`{ .sb-show-on-unchecked }`plextraktsync2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`plextraktsync_role_autoheal_enabled`{ .sb-show-on-unchecked }`plextraktsync2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        plextraktsync_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        plextraktsync2_autoheal_enabled: true
        ```

    ??? variable string "`plextraktsync_role_depends_on`{ .sb-show-on-unchecked }`plextraktsync2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        plextraktsync_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        plextraktsync2_depends_on: ""
        ```

    ??? variable string "`plextraktsync_role_depends_on_delay`{ .sb-show-on-unchecked }`plextraktsync2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        plextraktsync_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        plextraktsync2_depends_on_delay: "0"
        ```

    ??? variable string "`plextraktsync_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`plextraktsync2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plextraktsync_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plextraktsync2_depends_on_healthchecks:
        ```

    ??? variable bool "`plextraktsync_role_diun_enabled`{ .sb-show-on-unchecked }`plextraktsync2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        plextraktsync_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        plextraktsync2_diun_enabled: true
        ```

    ??? variable bool "`plextraktsync_role_docker_controller`{ .sb-show-on-unchecked }`plextraktsync2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        plextraktsync_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        plextraktsync2_docker_controller: true
        ```

    ??? variable list "`plextraktsync_role_docker_networks_alias_custom`{ .sb-show-on-unchecked }`plextraktsync2_docker_networks_alias_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        plextraktsync_role_docker_networks_alias_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        plextraktsync2_docker_networks_alias_custom:
        ```

    ??? variable bool "`plextraktsync_role_docker_volumes_download`{ .sb-show-on-unchecked }`plextraktsync2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        plextraktsync_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        plextraktsync2_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
