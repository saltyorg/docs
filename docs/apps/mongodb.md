---
icon: material/docker
title: MongoDB
hide:
  - tags
tags:
  - mongodb
  - database
  - nosql
saltbox_automation:
  app_links:
    - name: Manual
      url: https://www.mongodb.com/docs
      type: documentation
      purpose: manual
    - name: Releases
      url: https://hub.docker.com/_/mongo/tags
      type: docker
      purpose: release
    - name: Community
      url:
      type: community
      purpose: community
  project_description:
    name: MongoDB
    summary: |-
      a free and open-source cross-platform document-oriented database program.
    link: https://www.mongodb.com
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# MongoDB

## Overview

[MongoDB](https://www.mongodb.com) is a free and open-source cross-platform document-oriented database program.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://www.mongodb.com/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/mongo/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install mongodb
```

## Usage

MongoDB 8.0 is deployed in a Docker container with data persisting to `/opt/mongo/`. Connect from other containers using `mongodb://mongo:27017/`. Multiple instances are supported via the `mongodb_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md).

For official `mongo` images, Saltbox discovers the source version of existing data from MongoDB FTDC metadata and applies every required binary and feature compatibility version transition. Before a cross-series upgrade, Saltbox retains a verified cold copy at `<data path>_backup`; this copy is retained after success, and another cross-series upgrade is refused until it is removed manually. Unknown upgrade paths, missing FTDC metadata, downgrades, and incompatible host kernels fail before the data is changed.

Automatic upgrades require the `/data/db` and `/data/configdb` bindings to use `mongodb_role_paths_location`; change that path variable instead of overriding those two Docker volume targets. Custom image repositories continue to use ordinary deployment without automatic version upgrades.

Note: No authentication is configured by default.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override scope"><input type="checkbox" name="scope" hidden/></label>

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `mongodb_instances`.**

    !!! example "Example override"

        === "Role-scoped"

            ```yaml
            mongodb_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of mongodb

        === "Instance-scoped"

            ```yaml
            mongodb2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named mongodb2

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `mongodb_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `mongodb_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`mongodb_instances`"

        ```yaml
        # Type: list
        mongodb_instances: ["mongo"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            mongodb_instances: ["mongodb", "mongodb2"]
            ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`mongodb_role_docker_container`{ .sb-show-on-unchecked }`mongodb2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_container: "{{ mongodb_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_container: "{{ mongodb_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`mongodb_role_docker_image_pull`{ .sb-show-on-unchecked }`mongodb2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_image_pull: true
        ```

    ??? variable string "`mongodb_role_docker_image_repo`{ .sb-show-on-unchecked }`mongodb2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_image_repo: "mongo"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_image_repo: "mongo"
        ```

    ??? variable string "`mongodb_role_docker_image_tag`{ .sb-show-on-unchecked }`mongodb2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_image_tag: "8.0"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_image_tag: "8.0"
        ```

    ??? variable string "`mongodb_role_docker_image`{ .sb-show-on-unchecked }`mongodb2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mongodb') }}:{{ lookup('role_var', '_docker_image_tag', role='mongodb') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mongodb') }}:{{ lookup('role_var', '_docker_image_tag', role='mongodb') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`mongodb_role_docker_envs_default`{ .sb-show-on-unchecked }`mongodb2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_envs_default:
          MONGO_DATA_DIR: "/data/db"
          MONGO_LOG_DIR: "/dev/null"
          MONGO_URL: "mongodb://{{ mongodb_name }}:27017/"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_envs_default:
          MONGO_DATA_DIR: "/data/db"
          MONGO_LOG_DIR: "/dev/null"
          MONGO_URL: "mongodb://{{ mongodb_name }}:27017/"
        ```

    ??? variable dict "`mongodb_role_docker_envs_custom`{ .sb-show-on-unchecked }`mongodb2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`mongodb_role_docker_volumes_default`{ .sb-show-on-unchecked }`mongodb2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='mongodb') }}:/data/db:rw"
          - "{{ lookup('role_var', '_paths_location', role='mongodb') }}/config:/data/configdb"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='mongodb') }}:/data/db:rw"
          - "{{ lookup('role_var', '_paths_location', role='mongodb') }}/config:/data/configdb"
        ```

    ??? variable list "`mongodb_role_docker_volumes_custom`{ .sb-show-on-unchecked }`mongodb2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`mongodb_role_docker_hostname`{ .sb-show-on-unchecked }`mongodb2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_hostname: "{{ mongodb_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_hostname: "{{ mongodb_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`mongodb_role_docker_networks_alias`{ .sb-show-on-unchecked }`mongodb2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_networks_alias: "{{ mongodb_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_networks_alias: "{{ mongodb_name }}"
        ```

    ??? variable list "`mongodb_role_docker_networks_default`{ .sb-show-on-unchecked }`mongodb2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_networks_default: []
        ```

    ??? variable list "`mongodb_role_docker_networks_custom`{ .sb-show-on-unchecked }`mongodb2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`mongodb_role_docker_restart_policy`{ .sb-show-on-unchecked }`mongodb2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_restart_policy: unless-stopped
        ```

    <h5>User</h5>

    ??? variable string "`mongodb_role_docker_user`{ .sb-show-on-unchecked }`mongodb2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    A blank value is YAML null and inherits any lower-precedence role or shared default. Explicit Ansible omit is accepted only for optional Docker settings; default-backed and required settings reject it. Use the documented typed empty value, such as `""`, `[]`, or `{}`, when disabling a guaranteed setting.

    <h5>GPU</h5>

    ??? variable bool "`mongodb_role_docker_gpu_enabled`{ .sb-show-on-unchecked }`mongodb2_docker_gpu_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        mongodb_role_docker_gpu_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        mongodb2_docker_gpu_enabled: false
        ```

    ??? variable bool "`mongodb_role_docker_nvidia_disabled`{ .sb-show-on-unchecked }`mongodb2_docker_nvidia_disabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        mongodb_role_docker_nvidia_disabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        mongodb2_docker_nvidia_disabled: false
        ```

    ??? variable bool "`mongodb_role_docker_dev_dri_disabled`{ .sb-show-on-unchecked }`mongodb2_docker_dev_dri_disabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        mongodb_role_docker_dev_dri_disabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        mongodb2_docker_dev_dri_disabled: false
        ```

    <h5>Resource Limits</h5>

    ??? variable int "`mongodb_role_docker_blkio_weight`{ .sb-show-on-unchecked }`mongodb2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_blkio_weight:
        ```

    ??? variable int "`mongodb_role_docker_cpu_period`{ .sb-show-on-unchecked }`mongodb2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_cpu_period:
        ```

    ??? variable int "`mongodb_role_docker_cpu_quota`{ .sb-show-on-unchecked }`mongodb2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_cpu_quota:
        ```

    ??? variable int "`mongodb_role_docker_cpu_shares`{ .sb-show-on-unchecked }`mongodb2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_cpu_shares:
        ```

    ??? variable string "`mongodb_role_docker_cpus`{ .sb-show-on-unchecked }`mongodb2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # CPU allocation accepted as a numeric string, such as 1.5
        # Type: string (quoted number)
        mongodb_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # CPU allocation accepted as a numeric string, such as 1.5
        # Type: string (quoted number)
        mongodb2_docker_cpus:
        ```

    ??? variable string "`mongodb_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`mongodb2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_cpuset_cpus:
        ```

    ??? variable string "`mongodb_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`mongodb2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_cpuset_mems:
        ```

    ??? variable string "`mongodb_role_docker_kernel_memory`{ .sb-show-on-unchecked }`mongodb2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_kernel_memory:
        ```

    ??? variable string "`mongodb_role_docker_memory`{ .sb-show-on-unchecked }`mongodb2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_memory:
        ```

    ??? variable string "`mongodb_role_docker_memory_reservation`{ .sb-show-on-unchecked }`mongodb2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_memory_reservation:
        ```

    ??? variable string "`mongodb_role_docker_memory_swap`{ .sb-show-on-unchecked }`mongodb2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_memory_swap:
        ```

    ??? variable int "`mongodb_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`mongodb2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_memory_swappiness:
        ```

    ??? variable string "`mongodb_role_docker_shm_size`{ .sb-show-on-unchecked }`mongodb2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`mongodb_role_docker_cap_drop`{ .sb-show-on-unchecked }`mongodb2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_cap_drop:
        ```

    ??? variable string "`mongodb_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`mongodb2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_cgroupns_mode:
        ```

    ??? variable list "`mongodb_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`mongodb2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_device_cgroup_rules:
        ```

    ??? variable list "`mongodb_role_docker_device_read_bps`{ .sb-show-on-unchecked }`mongodb2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_device_read_bps:
        ```

    ??? variable list "`mongodb_role_docker_device_read_iops`{ .sb-show-on-unchecked }`mongodb2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_device_read_iops:
        ```

    ??? variable list "`mongodb_role_docker_device_requests`{ .sb-show-on-unchecked }`mongodb2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_device_requests:
        ```

    ??? variable list "`mongodb_role_docker_device_write_bps`{ .sb-show-on-unchecked }`mongodb2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_device_write_bps:
        ```

    ??? variable list "`mongodb_role_docker_device_write_iops`{ .sb-show-on-unchecked }`mongodb2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_device_write_iops:
        ```

    ??? variable list "`mongodb_role_docker_devices`{ .sb-show-on-unchecked }`mongodb2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_devices:
        ```

    ??? variable list "`mongodb_role_docker_groups`{ .sb-show-on-unchecked }`mongodb2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_groups:
        ```

    ??? variable bool "`mongodb_role_docker_privileged`{ .sb-show-on-unchecked }`mongodb2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_privileged:
        ```

    ??? variable list "`mongodb_role_docker_security_opts`{ .sb-show-on-unchecked }`mongodb2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_security_opts:
        ```

    ??? variable string "`mongodb_role_docker_userns_mode`{ .sb-show-on-unchecked }`mongodb2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`mongodb_role_docker_dns_opts`{ .sb-show-on-unchecked }`mongodb2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_dns_opts:
        ```

    ??? variable list "`mongodb_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`mongodb2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_dns_search_domains:
        ```

    ??? variable list "`mongodb_role_docker_dns_servers`{ .sb-show-on-unchecked }`mongodb2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_dns_servers:
        ```

    ??? variable string "`mongodb_role_docker_domainname`{ .sb-show-on-unchecked }`mongodb2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_domainname:
        ```

    ??? variable list "`mongodb_role_docker_exposed_ports`{ .sb-show-on-unchecked }`mongodb2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_exposed_ports:
        ```

    ??? variable dict "`mongodb_role_docker_hosts`{ .sb-show-on-unchecked }`mongodb2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_hosts:
        ```

    ??? variable bool "`mongodb_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`mongodb2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_hosts_use_common:
        ```

    ??? variable string "`mongodb_role_docker_ipc_mode`{ .sb-show-on-unchecked }`mongodb2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_ipc_mode:
        ```

    ??? variable list "`mongodb_role_docker_links`{ .sb-show-on-unchecked }`mongodb2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_links:
        ```

    ??? variable string "`mongodb_role_docker_network_mode`{ .sb-show-on-unchecked }`mongodb2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_network_mode:
        ```

    ??? variable string "`mongodb_role_docker_pid_mode`{ .sb-show-on-unchecked }`mongodb2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_pid_mode:
        ```

    ??? variable list "`mongodb_role_docker_ports`{ .sb-show-on-unchecked }`mongodb2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_ports:
        ```

    ??? variable string "`mongodb_role_docker_uts`{ .sb-show-on-unchecked }`mongodb2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`mongodb_role_docker_keep_volumes`{ .sb-show-on-unchecked }`mongodb2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_keep_volumes:
        ```

    ??? variable list "`mongodb_role_docker_mounts`{ .sb-show-on-unchecked }`mongodb2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_mounts:
        ```

    ??? variable dict "`mongodb_role_docker_storage_opts`{ .sb-show-on-unchecked }`mongodb2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_storage_opts:
        ```

    ??? variable list "`mongodb_role_docker_tmpfs`{ .sb-show-on-unchecked }`mongodb2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_tmpfs:
        ```

    ??? variable string "`mongodb_role_docker_volume_driver`{ .sb-show-on-unchecked }`mongodb2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_volume_driver:
        ```

    ??? variable list "`mongodb_role_docker_volumes_from`{ .sb-show-on-unchecked }`mongodb2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_volumes_from:
        ```

    ??? variable bool "`mongodb_role_docker_volumes_global`{ .sb-show-on-unchecked }`mongodb2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_volumes_global:
        ```

    ??? variable string "`mongodb_role_docker_working_dir`{ .sb-show-on-unchecked }`mongodb2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`mongodb_role_docker_auto_remove`{ .sb-show-on-unchecked }`mongodb2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_auto_remove:
        ```

    ??? variable bool "`mongodb_role_docker_cleanup`{ .sb-show-on-unchecked }`mongodb2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_cleanup:
        ```

    ??? variable bool "`mongodb_role_docker_force_kill`{ .sb-show-on-unchecked }`mongodb2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_force_kill:
        ```

    ??? variable dict "`mongodb_role_docker_healthcheck`{ .sb-show-on-unchecked }`mongodb2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_healthcheck:
        ```

    ??? variable int "`mongodb_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`mongodb2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Healthy-state wait timeout in seconds
        # Type: int
        mongodb_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Healthy-state wait timeout in seconds
        # Type: int
        mongodb2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`mongodb_role_docker_init`{ .sb-show-on-unchecked }`mongodb2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_init:
        ```

    ??? variable string "`mongodb_role_docker_kill_signal`{ .sb-show-on-unchecked }`mongodb2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_kill_signal:
        ```

    ??? variable string "`mongodb_role_docker_log_driver`{ .sb-show-on-unchecked }`mongodb2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_log_driver:
        ```

    ??? variable dict "`mongodb_role_docker_log_options`{ .sb-show-on-unchecked }`mongodb2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_log_options:
        ```

    ??? variable bool "`mongodb_role_docker_oom_killer`{ .sb-show-on-unchecked }`mongodb2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_oom_killer:
        ```

    ??? variable int "`mongodb_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`mongodb2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_oom_score_adj:
        ```

    ??? variable bool "`mongodb_role_docker_output_logs`{ .sb-show-on-unchecked }`mongodb2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_output_logs:
        ```

    ??? variable bool "`mongodb_role_docker_paused`{ .sb-show-on-unchecked }`mongodb2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_paused:
        ```

    ??? variable bool "`mongodb_role_docker_recreate`{ .sb-show-on-unchecked }`mongodb2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_recreate:
        ```

    ??? variable int "`mongodb_role_docker_restart_retries`{ .sb-show-on-unchecked }`mongodb2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_restart_retries:
        ```

    ??? variable string "`mongodb_role_docker_stop_signal`{ .sb-show-on-unchecked }`mongodb2_docker_stop_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_stop_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_stop_signal:
        ```

    ??? variable int "`mongodb_role_docker_stop_timeout`{ .sb-show-on-unchecked }`mongodb2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`mongodb_role_docker_capabilities`{ .sb-show-on-unchecked }`mongodb2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_capabilities:
        ```

    ??? variable string "`mongodb_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`mongodb2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_cgroup_parent:
        ```

    ??? variable list "`mongodb_role_docker_commands`{ .sb-show-on-unchecked }`mongodb2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_commands:
        ```

    ??? variable int "`mongodb_role_docker_create_timeout`{ .sb-show-on-unchecked }`mongodb2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        mongodb_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        mongodb2_docker_create_timeout:
        ```

    ??? variable list "`mongodb_role_docker_entrypoint`{ .sb-show-on-unchecked }`mongodb2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_entrypoint:
        ```

    ??? variable string "`mongodb_role_docker_env_file`{ .sb-show-on-unchecked }`mongodb2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_env_file:
        ```

    ??? variable dict "`mongodb_role_docker_labels`{ .sb-show-on-unchecked }`mongodb2_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_labels:
        ```

    ??? variable bool "`mongodb_role_docker_labels_use_common`{ .sb-show-on-unchecked }`mongodb2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_labels_use_common:
        ```

    ??? variable bool "`mongodb_role_docker_read_only`{ .sb-show-on-unchecked }`mongodb2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_read_only:
        ```

    ??? variable string "`mongodb_role_docker_runtime`{ .sb-show-on-unchecked }`mongodb2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        mongodb_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        mongodb2_docker_runtime:
        ```

    ??? variable dict "`mongodb_role_docker_sysctls`{ .sb-show-on-unchecked }`mongodb2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        mongodb_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        mongodb2_docker_sysctls:
        ```

    ??? variable list "`mongodb_role_docker_ulimits`{ .sb-show-on-unchecked }`mongodb2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`mongodb_role_autoheal_enabled`{ .sb-show-on-unchecked }`mongodb2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        mongodb_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        mongodb2_autoheal_enabled: true
        ```

    ??? variable string "`mongodb_role_depends_on`{ .sb-show-on-unchecked }`mongodb2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        mongodb_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        mongodb2_depends_on: ""
        ```

    ??? variable string "`mongodb_role_depends_on_delay`{ .sb-show-on-unchecked }`mongodb2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        mongodb_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        mongodb2_depends_on_delay: "0"
        ```

    ??? variable string "`mongodb_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`mongodb2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mongodb_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mongodb2_depends_on_healthchecks:
        ```

    ??? variable bool "`mongodb_role_diun_enabled`{ .sb-show-on-unchecked }`mongodb2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        mongodb_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        mongodb2_diun_enabled: true
        ```

    ??? variable bool "`mongodb_role_docker_controller`{ .sb-show-on-unchecked }`mongodb2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        mongodb_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        mongodb2_docker_controller: true
        ```

    ??? variable list "`mongodb_role_docker_networks_alias_custom`{ .sb-show-on-unchecked }`mongodb2_docker_networks_alias_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        mongodb_role_docker_networks_alias_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        mongodb2_docker_networks_alias_custom:
        ```

    ??? variable bool "`mongodb_role_docker_volumes_download`{ .sb-show-on-unchecked }`mongodb2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        mongodb_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        mongodb2_docker_volumes_download:
        ```

    ??? variable list "`mongodb_role_paths_folders_list_custom`{ .sb-show-on-unchecked }`mongodb2_paths_folders_list_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Extra directories to create
        # Type: list
        mongodb_role_paths_folders_list_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Extra directories to create
        # Type: list
        mongodb2_paths_folders_list_custom:
        ```

    ??? variable string "`mongodb_role_paths_group`{ .sb-show-on-unchecked }`mongodb2_paths_group`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Group for directories created by the role
        # Type: string
        mongodb_role_paths_group:
        ```

        ```yaml { .sb-show-on-checked }
        # Group for directories created by the role
        # Type: string
        mongodb2_paths_group:
        ```

    ??? variable string "`mongodb_role_paths_owner`{ .sb-show-on-unchecked }`mongodb2_paths_owner`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Owner for directories created by the role
        # Type: string
        mongodb_role_paths_owner:
        ```

        ```yaml { .sb-show-on-checked }
        # Owner for directories created by the role
        # Type: string
        mongodb2_paths_owner:
        ```

    ??? variable string "`mongodb_role_paths_permissions`{ .sb-show-on-unchecked }`mongodb2_paths_permissions`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Permissions for directories created by the role
        # Type: string
        mongodb_role_paths_permissions:
        ```

        ```yaml { .sb-show-on-checked }
        # Permissions for directories created by the role
        # Type: string
        mongodb2_paths_permissions:
        ```

    ??? variable bool "`mongodb_role_paths_recursive`{ .sb-show-on-unchecked }`mongodb2_paths_recursive`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Apply ownership and permissions recursively
        # Type: bool (true/false)
        mongodb_role_paths_recursive:
        ```

        ```yaml { .sb-show-on-checked }
        # Apply ownership and permissions recursively
        # Type: bool (true/false)
        mongodb2_paths_recursive:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
