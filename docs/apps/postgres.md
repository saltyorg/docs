---
icon: material/docker
title: PostgreSQL
hide:
  - tags
tags:
  - postgres
saltbox_automation:
  app_links:
    - name: Manual
      url: https://www.postgresql.org/docs/12/index.html
      type: documentation
    - name: Releases
      url: https://hub.docker.com/_/postgres/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: PostgreSQL
    summary: |-
      an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance.
    link: https://www.postgresql.org
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# PostgreSQL

## Overview

[PostgreSQL](https://www.postgresql.org) is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://www.postgresql.org/docs/12/index.html){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/postgres/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install postgres
```

## Usage

!!! info
    The default password for this container is `password4321`
    To easily manage the db, consider [adminer](../sandbox/apps/adminer.md)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override scope"><input type="checkbox" name="scope" hidden/></label>

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `postgres_instances`.**

    !!! example "Example override"

        === "Role-scoped"

            ```yaml
            postgres_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of postgres

        === "Instance-scoped"

            ```yaml
            postgres2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named postgres2

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `postgres_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `postgres_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`postgres_instances`"

        ```yaml
        # Type: list
        postgres_instances: ["postgres"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            postgres_instances: ["postgres", "postgres2"]
            ```

=== "Settings"

    ??? variable string "`postgres_role_docker_env_password`{ .sb-show-on-unchecked }`postgres2_docker_env_password`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_env_password: "password4321"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_env_password: "password4321"
        ```

    ??? variable string "`postgres_role_docker_env_user`{ .sb-show-on-unchecked }`postgres2_docker_env_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_env_user: "{{ user.name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_env_user: "{{ user.name }}"
        ```

    ??? variable string "`postgres_role_docker_env_db`{ .sb-show-on-unchecked }`postgres2_docker_env_db`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_env_db: "saltbox"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_env_db: "saltbox"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`postgres_role_docker_container`{ .sb-show-on-unchecked }`postgres2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_container: "{{ postgres_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_container: "{{ postgres_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`postgres_role_docker_image_pull`{ .sb-show-on-unchecked }`postgres2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_image_pull: true
        ```

    ??? variable string "`postgres_role_docker_image_tag`{ .sb-show-on-unchecked }`postgres2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_image_tag: "17-alpine"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_image_tag: "17-alpine"
        ```

    ??? variable string "`postgres_role_docker_image_repo`{ .sb-show-on-unchecked }`postgres2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_image_repo: "postgres"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_image_repo: "postgres"
        ```

    ??? variable string "`postgres_role_docker_image`{ .sb-show-on-unchecked }`postgres2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='postgres') }}:{{ lookup('role_var', '_docker_image_tag', role='postgres') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='postgres') }}:{{ lookup('role_var', '_docker_image_tag', role='postgres') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`postgres_role_docker_envs_default`{ .sb-show-on-unchecked }`postgres2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        postgres_role_docker_envs_default:
          TZ: "{{ tz }}"
          PGDATA: "/data"
          POSTGRES_PASSWORD: "{{ postgres_role_docker_env_password_effective }}"
          POSTGRES_USER: "{{ postgres_role_docker_env_user_effective }}"
          POSTGRES_DB: "{{ lookup('role_var', '_docker_env_db', role='postgres') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        postgres2_docker_envs_default:
          TZ: "{{ tz }}"
          PGDATA: "/data"
          POSTGRES_PASSWORD: "{{ postgres_role_docker_env_password_effective }}"
          POSTGRES_USER: "{{ postgres_role_docker_env_user_effective }}"
          POSTGRES_DB: "{{ lookup('role_var', '_docker_env_db', role='postgres') }}"
        ```

    ??? variable dict "`postgres_role_docker_envs_custom`{ .sb-show-on-unchecked }`postgres2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        postgres_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        postgres2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`postgres_role_docker_volumes_default`{ .sb-show-on-unchecked }`postgres2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_volumes_default:
          - "{{ postgres_role_paths_location }}:/data"
          - "{{ postgres_role_paths_location }}:/var/lib/postgresql/data"
          - "/etc/passwd:/etc/passwd:ro"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_volumes_default:
          - "{{ postgres_role_paths_location }}:/data"
          - "{{ postgres_role_paths_location }}:/var/lib/postgresql/data"
          - "/etc/passwd:/etc/passwd:ro"
        ```

    ??? variable list "`postgres_role_docker_volumes_custom`{ .sb-show-on-unchecked }`postgres2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`postgres_role_docker_hostname`{ .sb-show-on-unchecked }`postgres2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_hostname: "{{ postgres_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_hostname: "{{ postgres_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`postgres_role_docker_networks_alias`{ .sb-show-on-unchecked }`postgres2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_networks_alias: "{{ postgres_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_networks_alias: "{{ postgres_name }}"
        ```

    ??? variable list "`postgres_role_docker_networks_default`{ .sb-show-on-unchecked }`postgres2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_networks_default: []
        ```

    ??? variable list "`postgres_role_docker_networks_custom`{ .sb-show-on-unchecked }`postgres2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`postgres_role_docker_restart_policy`{ .sb-show-on-unchecked }`postgres2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`postgres_role_docker_state`{ .sb-show-on-unchecked }`postgres2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`postgres_role_docker_user`{ .sb-show-on-unchecked }`postgres2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>SHM size</h5>

    ??? variable string "`postgres_role_docker_shm_size`{ .sb-show-on-unchecked }`postgres2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_shm_size: "128M"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_shm_size: "128M"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`postgres_role_docker_blkio_weight`{ .sb-show-on-unchecked }`postgres2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_blkio_weight:
        ```

    ??? variable int "`postgres_role_docker_cpu_period`{ .sb-show-on-unchecked }`postgres2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_cpu_period:
        ```

    ??? variable int "`postgres_role_docker_cpu_quota`{ .sb-show-on-unchecked }`postgres2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_cpu_quota:
        ```

    ??? variable int "`postgres_role_docker_cpu_shares`{ .sb-show-on-unchecked }`postgres2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_cpu_shares:
        ```

    ??? variable string "`postgres_role_docker_cpus`{ .sb-show-on-unchecked }`postgres2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_cpus:
        ```

    ??? variable string "`postgres_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`postgres2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_cpuset_cpus:
        ```

    ??? variable string "`postgres_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`postgres2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_cpuset_mems:
        ```

    ??? variable string "`postgres_role_docker_kernel_memory`{ .sb-show-on-unchecked }`postgres2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_kernel_memory:
        ```

    ??? variable string "`postgres_role_docker_memory`{ .sb-show-on-unchecked }`postgres2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_memory:
        ```

    ??? variable string "`postgres_role_docker_memory_reservation`{ .sb-show-on-unchecked }`postgres2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_memory_reservation:
        ```

    ??? variable string "`postgres_role_docker_memory_swap`{ .sb-show-on-unchecked }`postgres2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_memory_swap:
        ```

    ??? variable int "`postgres_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`postgres2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`postgres_role_docker_cap_drop`{ .sb-show-on-unchecked }`postgres2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_cap_drop:
        ```

    ??? variable string "`postgres_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`postgres2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_cgroupns_mode:
        ```

    ??? variable list "`postgres_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`postgres2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_device_cgroup_rules:
        ```

    ??? variable list "`postgres_role_docker_device_read_bps`{ .sb-show-on-unchecked }`postgres2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_device_read_bps:
        ```

    ??? variable list "`postgres_role_docker_device_read_iops`{ .sb-show-on-unchecked }`postgres2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_device_read_iops:
        ```

    ??? variable list "`postgres_role_docker_device_requests`{ .sb-show-on-unchecked }`postgres2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_device_requests:
        ```

    ??? variable list "`postgres_role_docker_device_write_bps`{ .sb-show-on-unchecked }`postgres2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_device_write_bps:
        ```

    ??? variable list "`postgres_role_docker_device_write_iops`{ .sb-show-on-unchecked }`postgres2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_device_write_iops:
        ```

    ??? variable list "`postgres_role_docker_devices`{ .sb-show-on-unchecked }`postgres2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_devices:
        ```

    ??? variable list "`postgres_role_docker_groups`{ .sb-show-on-unchecked }`postgres2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_groups:
        ```

    ??? variable bool "`postgres_role_docker_privileged`{ .sb-show-on-unchecked }`postgres2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_privileged:
        ```

    ??? variable list "`postgres_role_docker_security_opts`{ .sb-show-on-unchecked }`postgres2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_security_opts:
        ```

    ??? variable string "`postgres_role_docker_userns_mode`{ .sb-show-on-unchecked }`postgres2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`postgres_role_docker_dns_opts`{ .sb-show-on-unchecked }`postgres2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_dns_opts:
        ```

    ??? variable list "`postgres_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`postgres2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_dns_search_domains:
        ```

    ??? variable list "`postgres_role_docker_dns_servers`{ .sb-show-on-unchecked }`postgres2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_dns_servers:
        ```

    ??? variable string "`postgres_role_docker_domainname`{ .sb-show-on-unchecked }`postgres2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_domainname:
        ```

    ??? variable list "`postgres_role_docker_exposed_ports`{ .sb-show-on-unchecked }`postgres2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_exposed_ports:
        ```

    ??? variable dict "`postgres_role_docker_hosts`{ .sb-show-on-unchecked }`postgres2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        postgres_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        postgres2_docker_hosts:
        ```

    ??? variable bool "`postgres_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`postgres2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_hosts_use_common:
        ```

    ??? variable string "`postgres_role_docker_ipc_mode`{ .sb-show-on-unchecked }`postgres2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_ipc_mode:
        ```

    ??? variable list "`postgres_role_docker_links`{ .sb-show-on-unchecked }`postgres2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_links:
        ```

    ??? variable string "`postgres_role_docker_network_mode`{ .sb-show-on-unchecked }`postgres2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_network_mode:
        ```

    ??? variable string "`postgres_role_docker_pid_mode`{ .sb-show-on-unchecked }`postgres2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_pid_mode:
        ```

    ??? variable list "`postgres_role_docker_ports`{ .sb-show-on-unchecked }`postgres2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_ports:
        ```

    ??? variable string "`postgres_role_docker_uts`{ .sb-show-on-unchecked }`postgres2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`postgres_role_docker_keep_volumes`{ .sb-show-on-unchecked }`postgres2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_keep_volumes:
        ```

    ??? variable list "`postgres_role_docker_mounts`{ .sb-show-on-unchecked }`postgres2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_mounts:
        ```

    ??? variable dict "`postgres_role_docker_storage_opts`{ .sb-show-on-unchecked }`postgres2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        postgres_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        postgres2_docker_storage_opts:
        ```

    ??? variable list "`postgres_role_docker_tmpfs`{ .sb-show-on-unchecked }`postgres2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_tmpfs:
        ```

    ??? variable string "`postgres_role_docker_volume_driver`{ .sb-show-on-unchecked }`postgres2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_volume_driver:
        ```

    ??? variable list "`postgres_role_docker_volumes_from`{ .sb-show-on-unchecked }`postgres2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_volumes_from:
        ```

    ??? variable bool "`postgres_role_docker_volumes_global`{ .sb-show-on-unchecked }`postgres2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_volumes_global:
        ```

    ??? variable string "`postgres_role_docker_working_dir`{ .sb-show-on-unchecked }`postgres2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`postgres_role_docker_auto_remove`{ .sb-show-on-unchecked }`postgres2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_auto_remove:
        ```

    ??? variable bool "`postgres_role_docker_cleanup`{ .sb-show-on-unchecked }`postgres2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_cleanup:
        ```

    ??? variable string "`postgres_role_docker_force_kill`{ .sb-show-on-unchecked }`postgres2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_force_kill:
        ```

    ??? variable dict "`postgres_role_docker_healthcheck`{ .sb-show-on-unchecked }`postgres2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        postgres_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        postgres2_docker_healthcheck:
        ```

    ??? variable int "`postgres_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`postgres2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`postgres_role_docker_init`{ .sb-show-on-unchecked }`postgres2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_init:
        ```

    ??? variable string "`postgres_role_docker_kill_signal`{ .sb-show-on-unchecked }`postgres2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_kill_signal:
        ```

    ??? variable string "`postgres_role_docker_log_driver`{ .sb-show-on-unchecked }`postgres2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_log_driver:
        ```

    ??? variable dict "`postgres_role_docker_log_options`{ .sb-show-on-unchecked }`postgres2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        postgres_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        postgres2_docker_log_options:
        ```

    ??? variable bool "`postgres_role_docker_oom_killer`{ .sb-show-on-unchecked }`postgres2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_oom_killer:
        ```

    ??? variable int "`postgres_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`postgres2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_oom_score_adj:
        ```

    ??? variable bool "`postgres_role_docker_output_logs`{ .sb-show-on-unchecked }`postgres2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_output_logs:
        ```

    ??? variable bool "`postgres_role_docker_paused`{ .sb-show-on-unchecked }`postgres2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_paused:
        ```

    ??? variable bool "`postgres_role_docker_recreate`{ .sb-show-on-unchecked }`postgres2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_recreate:
        ```

    ??? variable int "`postgres_role_docker_restart_retries`{ .sb-show-on-unchecked }`postgres2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_restart_retries:
        ```

    ??? variable string "`postgres_role_docker_stop_signal`{ .sb-show-on-unchecked }`postgres2_docker_stop_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_stop_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_stop_signal:
        ```

    ??? variable int "`postgres_role_docker_stop_timeout`{ .sb-show-on-unchecked }`postgres2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`postgres_role_docker_capabilities`{ .sb-show-on-unchecked }`postgres2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_capabilities:
        ```

    ??? variable string "`postgres_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`postgres2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_cgroup_parent:
        ```

    ??? variable list "`postgres_role_docker_commands`{ .sb-show-on-unchecked }`postgres2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_commands:
        ```

    ??? variable int "`postgres_role_docker_create_timeout`{ .sb-show-on-unchecked }`postgres2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        postgres_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        postgres2_docker_create_timeout:
        ```

    ??? variable string "`postgres_role_docker_dev_dri`{ .sb-show-on-unchecked }`postgres2_docker_dev_dri`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_dev_dri:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_dev_dri:
        ```

    ??? variable string "`postgres_role_docker_entrypoint`{ .sb-show-on-unchecked }`postgres2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_entrypoint:
        ```

    ??? variable string "`postgres_role_docker_env_file`{ .sb-show-on-unchecked }`postgres2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_env_file:
        ```

    ??? variable dict "`postgres_role_docker_labels`{ .sb-show-on-unchecked }`postgres2_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        postgres_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        postgres2_docker_labels:
        ```

    ??? variable bool "`postgres_role_docker_labels_use_common`{ .sb-show-on-unchecked }`postgres2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_labels_use_common:
        ```

    ??? variable bool "`postgres_role_docker_read_only`{ .sb-show-on-unchecked }`postgres2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_read_only:
        ```

    ??? variable string "`postgres_role_docker_runtime`{ .sb-show-on-unchecked }`postgres2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        postgres_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        postgres2_docker_runtime:
        ```

    ??? variable list "`postgres_role_docker_sysctls`{ .sb-show-on-unchecked }`postgres2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_sysctls:
        ```

    ??? variable list "`postgres_role_docker_ulimits`{ .sb-show-on-unchecked }`postgres2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`postgres_role_autoheal_enabled`{ .sb-show-on-unchecked }`postgres2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        postgres_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        postgres2_autoheal_enabled: true
        ```

    ??? variable string "`postgres_role_depends_on`{ .sb-show-on-unchecked }`postgres2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        postgres_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        postgres2_depends_on: ""
        ```

    ??? variable string "`postgres_role_depends_on_delay`{ .sb-show-on-unchecked }`postgres2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        postgres_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        postgres2_depends_on_delay: "0"
        ```

    ??? variable string "`postgres_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`postgres2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        postgres_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        postgres2_depends_on_healthchecks:
        ```

    ??? variable bool "`postgres_role_diun_enabled`{ .sb-show-on-unchecked }`postgres2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        postgres_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        postgres2_diun_enabled: true
        ```

    ??? variable bool "`postgres_role_docker_controller`{ .sb-show-on-unchecked }`postgres2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        postgres_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        postgres2_docker_controller: true
        ```

    ??? variable list "`postgres_role_docker_networks_alias_custom`{ .sb-show-on-unchecked }`postgres2_docker_networks_alias_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        postgres_role_docker_networks_alias_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        postgres2_docker_networks_alias_custom:
        ```

    ??? variable bool "`postgres_role_docker_volumes_download`{ .sb-show-on-unchecked }`postgres2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        postgres_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        postgres2_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
