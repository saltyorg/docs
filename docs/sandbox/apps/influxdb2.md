---
icon: material/docker
hide:
  - tags
tags:
  - influxdb2
  - database
  - timeseries
---

# InfluxDB2

## Overview

[InfluxDB2](https://www.influxdata.com/products/influxdb/) is an open source time series database for recording metrics, events, and analytics.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.influxdata.com/influxdb/latest){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/influxdb/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-influxdb2
```

## Usage

Visit <https://influxdb2.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `influxdb2_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of influxdb2:" }
    influxdb2_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `influxdb22`):" }
    influxdb22_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `influxdb2_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `influxdb2_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`influxdb2_instances`"

        ```yaml
        # Type: list
        influxdb2_instances: ["influxdb2"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            influxdb2_instances: ["influxdb2", "influxdb22"]
            ```

=== "Paths"

    ??? variable string "`influxdb2_role_paths_folder`{ .sb-show-on-unchecked }`influxdb22_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_paths_folder: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_paths_folder: "{{ influxdb2_name }}"
        ```

    ??? variable string "`influxdb2_role_paths_location`{ .sb-show-on-unchecked }`influxdb22_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`influxdb2_role_web_subdomain`{ .sb-show-on-unchecked }`influxdb22_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_subdomain: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_subdomain: "{{ influxdb2_name }}"
        ```

    ??? variable string "`influxdb2_role_web_domain`{ .sb-show-on-unchecked }`influxdb22_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`influxdb2_role_web_port`{ .sb-show-on-unchecked }`influxdb22_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_port: "8086"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_port: "8086"
        ```

    ??? variable string "`influxdb2_role_web_url`{ .sb-show-on-unchecked }`influxdb22_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                                 if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                                 else lookup('role_var', '_web_domain', role='influxdb2')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                             if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                             else lookup('role_var', '_web_domain', role='influxdb2')) }}"
        ```

=== "DNS"

    ??? variable string "`influxdb2_role_dns_record`{ .sb-show-on-unchecked }`influxdb22_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"
        ```

    ??? variable string "`influxdb2_role_dns_zone`{ .sb-show-on-unchecked }`influxdb22_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"
        ```

    ??? variable bool "`influxdb2_role_dns_proxy`{ .sb-show-on-unchecked }`influxdb22_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`influxdb2_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`influxdb22_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`influxdb2_role_traefik_middleware_default`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`influxdb2_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_middleware_custom: ""
        ```

    ??? variable string "`influxdb2_role_traefik_certresolver`{ .sb-show-on-unchecked }`influxdb22_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`influxdb2_role_traefik_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_enabled: true
        ```

    ??? variable bool "`influxdb2_role_traefik_api_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_api_enabled: false
        ```

    ??? variable string "`influxdb2_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`influxdb22_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`influxdb2_role_docker_container`{ .sb-show-on-unchecked }`influxdb22_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_container: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_container: "{{ influxdb2_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`influxdb2_role_docker_image_pull`{ .sb-show-on-unchecked }`influxdb22_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_image_pull: true
        ```

    ??? variable string "`influxdb2_role_docker_image_tag`{ .sb-show-on-unchecked }`influxdb22_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image_tag: "2-alpine"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image_tag: "2-alpine"
        ```

    ??? variable string "`influxdb2_role_docker_image_repo`{ .sb-show-on-unchecked }`influxdb22_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image_repo: "influxdb"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image_repo: "influxdb"
        ```

    ??? variable string "`influxdb2_role_docker_image`{ .sb-show-on-unchecked }`influxdb22_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`influxdb2_role_docker_volumes_default`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"
        ```

    ??? variable list "`influxdb2_role_docker_volumes_custom`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`influxdb2_role_docker_hostname`{ .sb-show-on-unchecked }`influxdb22_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_hostname: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_hostname: "{{ influxdb2_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`influxdb2_role_docker_networks_alias`{ .sb-show-on-unchecked }`influxdb22_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_networks_alias: "{{ influxdb2_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_networks_alias: "{{ influxdb2_name }}"
        ```

    ??? variable list "`influxdb2_role_docker_networks_default`{ .sb-show-on-unchecked }`influxdb22_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_networks_default: []
        ```

    ??? variable list "`influxdb2_role_docker_networks_custom`{ .sb-show-on-unchecked }`influxdb22_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`influxdb2_role_docker_restart_policy`{ .sb-show-on-unchecked }`influxdb22_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`influxdb2_role_docker_state`{ .sb-show-on-unchecked }`influxdb22_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`influxdb2_role_docker_blkio_weight`{ .sb-show-on-unchecked }`influxdb22_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_blkio_weight:
        ```

    ??? variable int "`influxdb2_role_docker_cpu_period`{ .sb-show-on-unchecked }`influxdb22_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_cpu_period:
        ```

    ??? variable int "`influxdb2_role_docker_cpu_quota`{ .sb-show-on-unchecked }`influxdb22_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_cpu_quota:
        ```

    ??? variable int "`influxdb2_role_docker_cpu_shares`{ .sb-show-on-unchecked }`influxdb22_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_cpu_shares:
        ```

    ??? variable string "`influxdb2_role_docker_cpus`{ .sb-show-on-unchecked }`influxdb22_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_cpus:
        ```

    ??? variable string "`influxdb2_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`influxdb22_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_cpuset_cpus:
        ```

    ??? variable string "`influxdb2_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`influxdb22_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_cpuset_mems:
        ```

    ??? variable string "`influxdb2_role_docker_kernel_memory`{ .sb-show-on-unchecked }`influxdb22_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_kernel_memory:
        ```

    ??? variable string "`influxdb2_role_docker_memory`{ .sb-show-on-unchecked }`influxdb22_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_memory:
        ```

    ??? variable string "`influxdb2_role_docker_memory_reservation`{ .sb-show-on-unchecked }`influxdb22_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_memory_reservation:
        ```

    ??? variable string "`influxdb2_role_docker_memory_swap`{ .sb-show-on-unchecked }`influxdb22_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_memory_swap:
        ```

    ??? variable int "`influxdb2_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`influxdb22_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_memory_swappiness:
        ```

    ??? variable string "`influxdb2_role_docker_shm_size`{ .sb-show-on-unchecked }`influxdb22_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`influxdb2_role_docker_cap_drop`{ .sb-show-on-unchecked }`influxdb22_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_cap_drop:
        ```

    ??? variable string "`influxdb2_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`influxdb22_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_cgroupns_mode:
        ```

    ??? variable list "`influxdb2_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`influxdb22_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_device_cgroup_rules:
        ```

    ??? variable list "`influxdb2_role_docker_device_read_bps`{ .sb-show-on-unchecked }`influxdb22_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_device_read_bps:
        ```

    ??? variable list "`influxdb2_role_docker_device_read_iops`{ .sb-show-on-unchecked }`influxdb22_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_device_read_iops:
        ```

    ??? variable list "`influxdb2_role_docker_device_requests`{ .sb-show-on-unchecked }`influxdb22_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_device_requests:
        ```

    ??? variable list "`influxdb2_role_docker_device_write_bps`{ .sb-show-on-unchecked }`influxdb22_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_device_write_bps:
        ```

    ??? variable list "`influxdb2_role_docker_device_write_iops`{ .sb-show-on-unchecked }`influxdb22_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_device_write_iops:
        ```

    ??? variable list "`influxdb2_role_docker_devices`{ .sb-show-on-unchecked }`influxdb22_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_devices:
        ```

    ??? variable string "`influxdb2_role_docker_devices_default`{ .sb-show-on-unchecked }`influxdb22_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_devices_default:
        ```

    ??? variable list "`influxdb2_role_docker_groups`{ .sb-show-on-unchecked }`influxdb22_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_groups:
        ```

    ??? variable bool "`influxdb2_role_docker_privileged`{ .sb-show-on-unchecked }`influxdb22_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_privileged:
        ```

    ??? variable list "`influxdb2_role_docker_security_opts`{ .sb-show-on-unchecked }`influxdb22_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_security_opts:
        ```

    ??? variable string "`influxdb2_role_docker_user`{ .sb-show-on-unchecked }`influxdb22_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_user:
        ```

    ??? variable string "`influxdb2_role_docker_userns_mode`{ .sb-show-on-unchecked }`influxdb22_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`influxdb2_role_docker_dns_opts`{ .sb-show-on-unchecked }`influxdb22_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_dns_opts:
        ```

    ??? variable list "`influxdb2_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`influxdb22_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_dns_search_domains:
        ```

    ??? variable list "`influxdb2_role_docker_dns_servers`{ .sb-show-on-unchecked }`influxdb22_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_dns_servers:
        ```

    ??? variable string "`influxdb2_role_docker_domainname`{ .sb-show-on-unchecked }`influxdb22_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_domainname:
        ```

    ??? variable list "`influxdb2_role_docker_exposed_ports`{ .sb-show-on-unchecked }`influxdb22_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_exposed_ports:
        ```

    ??? variable dict "`influxdb2_role_docker_hosts`{ .sb-show-on-unchecked }`influxdb22_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        influxdb2_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        influxdb22_docker_hosts:
        ```

    ??? variable bool "`influxdb2_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`influxdb22_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_hosts_use_common:
        ```

    ??? variable string "`influxdb2_role_docker_ipc_mode`{ .sb-show-on-unchecked }`influxdb22_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_ipc_mode:
        ```

    ??? variable list "`influxdb2_role_docker_links`{ .sb-show-on-unchecked }`influxdb22_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_links:
        ```

    ??? variable string "`influxdb2_role_docker_network_mode`{ .sb-show-on-unchecked }`influxdb22_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_network_mode:
        ```

    ??? variable string "`influxdb2_role_docker_pid_mode`{ .sb-show-on-unchecked }`influxdb22_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_pid_mode:
        ```

    ??? variable list "`influxdb2_role_docker_ports`{ .sb-show-on-unchecked }`influxdb22_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_ports:
        ```

    ??? variable string "`influxdb2_role_docker_uts`{ .sb-show-on-unchecked }`influxdb22_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`influxdb2_role_docker_keep_volumes`{ .sb-show-on-unchecked }`influxdb22_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_keep_volumes:
        ```

    ??? variable list "`influxdb2_role_docker_mounts`{ .sb-show-on-unchecked }`influxdb22_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_mounts:
        ```

    ??? variable dict "`influxdb2_role_docker_storage_opts`{ .sb-show-on-unchecked }`influxdb22_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        influxdb2_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        influxdb22_docker_storage_opts:
        ```

    ??? variable list "`influxdb2_role_docker_tmpfs`{ .sb-show-on-unchecked }`influxdb22_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_tmpfs:
        ```

    ??? variable string "`influxdb2_role_docker_volume_driver`{ .sb-show-on-unchecked }`influxdb22_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_volume_driver:
        ```

    ??? variable list "`influxdb2_role_docker_volumes_from`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_volumes_from:
        ```

    ??? variable bool "`influxdb2_role_docker_volumes_global`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_volumes_global:
        ```

    ??? variable string "`influxdb2_role_docker_working_dir`{ .sb-show-on-unchecked }`influxdb22_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`influxdb2_role_docker_auto_remove`{ .sb-show-on-unchecked }`influxdb22_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_auto_remove:
        ```

    ??? variable bool "`influxdb2_role_docker_cleanup`{ .sb-show-on-unchecked }`influxdb22_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_cleanup:
        ```

    ??? variable string "`influxdb2_role_docker_force_kill`{ .sb-show-on-unchecked }`influxdb22_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_force_kill:
        ```

    ??? variable dict "`influxdb2_role_docker_healthcheck`{ .sb-show-on-unchecked }`influxdb22_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        influxdb2_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        influxdb22_docker_healthcheck:
        ```

    ??? variable int "`influxdb2_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`influxdb22_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`influxdb2_role_docker_init`{ .sb-show-on-unchecked }`influxdb22_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_init:
        ```

    ??? variable string "`influxdb2_role_docker_kill_signal`{ .sb-show-on-unchecked }`influxdb22_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_kill_signal:
        ```

    ??? variable string "`influxdb2_role_docker_log_driver`{ .sb-show-on-unchecked }`influxdb22_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_log_driver:
        ```

    ??? variable dict "`influxdb2_role_docker_log_options`{ .sb-show-on-unchecked }`influxdb22_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        influxdb2_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        influxdb22_docker_log_options:
        ```

    ??? variable bool "`influxdb2_role_docker_oom_killer`{ .sb-show-on-unchecked }`influxdb22_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_oom_killer:
        ```

    ??? variable int "`influxdb2_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`influxdb22_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_oom_score_adj:
        ```

    ??? variable bool "`influxdb2_role_docker_output_logs`{ .sb-show-on-unchecked }`influxdb22_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_output_logs:
        ```

    ??? variable bool "`influxdb2_role_docker_paused`{ .sb-show-on-unchecked }`influxdb22_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_paused:
        ```

    ??? variable bool "`influxdb2_role_docker_recreate`{ .sb-show-on-unchecked }`influxdb22_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_recreate:
        ```

    ??? variable int "`influxdb2_role_docker_restart_retries`{ .sb-show-on-unchecked }`influxdb22_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_restart_retries:
        ```

    ??? variable int "`influxdb2_role_docker_stop_timeout`{ .sb-show-on-unchecked }`influxdb22_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`influxdb2_role_docker_capabilities`{ .sb-show-on-unchecked }`influxdb22_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_capabilities:
        ```

    ??? variable string "`influxdb2_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`influxdb22_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_cgroup_parent:
        ```

    ??? variable list "`influxdb2_role_docker_commands`{ .sb-show-on-unchecked }`influxdb22_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_commands:
        ```

    ??? variable int "`influxdb2_role_docker_create_timeout`{ .sb-show-on-unchecked }`influxdb22_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        influxdb2_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        influxdb22_docker_create_timeout:
        ```

    ??? variable string "`influxdb2_role_docker_entrypoint`{ .sb-show-on-unchecked }`influxdb22_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_entrypoint:
        ```

    ??? variable string "`influxdb2_role_docker_env_file`{ .sb-show-on-unchecked }`influxdb22_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_env_file:
        ```

    ??? variable dict "`influxdb2_role_docker_envs`{ .sb-show-on-unchecked }`influxdb22_docker_envs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        influxdb2_role_docker_envs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        influxdb22_docker_envs:
        ```

    ??? variable dict "`influxdb2_role_docker_labels`{ .sb-show-on-unchecked }`influxdb22_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        influxdb2_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        influxdb22_docker_labels:
        ```

    ??? variable bool "`influxdb2_role_docker_labels_use_common`{ .sb-show-on-unchecked }`influxdb22_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_labels_use_common:
        ```

    ??? variable bool "`influxdb2_role_docker_read_only`{ .sb-show-on-unchecked }`influxdb22_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_read_only:
        ```

    ??? variable string "`influxdb2_role_docker_runtime`{ .sb-show-on-unchecked }`influxdb22_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_runtime:
        ```

    ??? variable list "`influxdb2_role_docker_sysctls`{ .sb-show-on-unchecked }`influxdb22_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_sysctls:
        ```

    ??? variable list "`influxdb2_role_docker_ulimits`{ .sb-show-on-unchecked }`influxdb22_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        influxdb2_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        influxdb22_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`influxdb2_role_autoheal_enabled`{ .sb-show-on-unchecked }`influxdb22_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        influxdb2_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        influxdb22_autoheal_enabled: true
        ```

    ??? variable string "`influxdb2_role_depends_on`{ .sb-show-on-unchecked }`influxdb22_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        influxdb2_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        influxdb22_depends_on: ""
        ```

    ??? variable string "`influxdb2_role_depends_on_delay`{ .sb-show-on-unchecked }`influxdb22_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        influxdb2_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        influxdb22_depends_on_delay: "0"
        ```

    ??? variable string "`influxdb2_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`influxdb22_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb2_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb22_depends_on_healthchecks:
        ```

    ??? variable bool "`influxdb2_role_diun_enabled`{ .sb-show-on-unchecked }`influxdb22_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        influxdb2_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        influxdb22_diun_enabled: true
        ```

    ??? variable bool "`influxdb2_role_dns_enabled`{ .sb-show-on-unchecked }`influxdb22_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        influxdb2_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        influxdb22_dns_enabled: true
        ```

    ??? variable bool "`influxdb2_role_docker_controller`{ .sb-show-on-unchecked }`influxdb22_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        influxdb2_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        influxdb22_docker_controller: true
        ```

    ??? variable string "`influxdb2_role_docker_image_repo`{ .sb-show-on-unchecked }`influxdb22_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image_repo:
        ```

    ??? variable string "`influxdb2_role_docker_image_tag`{ .sb-show-on-unchecked }`influxdb22_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_docker_image_tag:
        ```

    ??? variable bool "`influxdb2_role_docker_volumes_download`{ .sb-show-on-unchecked }`influxdb22_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_docker_volumes_download:
        ```

    ??? variable string "`influxdb2_role_paths_location`{ .sb-show-on-unchecked }`influxdb22_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_paths_location:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_paths_location:
        ```

    ??? variable string "`influxdb2_role_themepark_addons`{ .sb-show-on-unchecked }`influxdb22_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_themepark_addons:
        ```

    ??? variable string "`influxdb2_role_themepark_app`{ .sb-show-on-unchecked }`influxdb22_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_themepark_app:
        ```

    ??? variable string "`influxdb2_role_themepark_theme`{ .sb-show-on-unchecked }`influxdb22_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_themepark_theme:
        ```

    ??? variable dict/omit "`influxdb2_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`influxdb22_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        influxdb2_role_traefik_api_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        influxdb22_traefik_api_endpoint:
        ```

    ??? variable string "`influxdb2_role_traefik_api_middleware`{ .sb-show-on-unchecked }`influxdb22_traefik_api_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_api_middleware:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_api_middleware:
        ```

    ??? variable string "`influxdb2_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`influxdb22_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_api_middleware_http:
        ```

    ??? variable bool "`influxdb2_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_autodetect_enabled: false
        ```

    ??? variable string "`influxdb2_role_traefik_certresolver`{ .sb-show-on-unchecked }`influxdb22_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_certresolver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_certresolver:
        ```

    ??? variable bool "`influxdb2_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_gzip_enabled: false
        ```

    ??? variable string "`influxdb2_role_traefik_middleware_http`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_middleware_http:
        ```

    ??? variable bool "`influxdb2_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`influxdb2_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`influxdb22_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        influxdb2_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        influxdb22_traefik_middleware_http_insecure:
        ```

    ??? variable string "`influxdb2_role_traefik_priority`{ .sb-show-on-unchecked }`influxdb22_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_traefik_priority:
        ```

    ??? variable bool "`influxdb2_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        influxdb22_traefik_robot_enabled: true
        ```

    ??? variable bool "`influxdb2_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        influxdb22_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`influxdb2_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`influxdb22_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        influxdb22_traefik_wildcard_enabled: true
        ```

    ??? variable string "`influxdb2_role_web_domain`{ .sb-show-on-unchecked }`influxdb22_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_domain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_domain:
        ```

    ??? variable list "`influxdb2_role_web_fqdn_override`{ .sb-show-on-unchecked }`influxdb22_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        influxdb2_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        influxdb22_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            influxdb2_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "influxdb22.{{ user.domain }}"
              - "influxdb2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            influxdb22_web_fqdn_override:
              - "{{ traefik_host }}"
              - "influxdb22.{{ user.domain }}"
              - "influxdb2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`influxdb2_role_web_host_override`{ .sb-show-on-unchecked }`influxdb22_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        influxdb2_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        influxdb22_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            influxdb2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            influxdb22_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`influxdb2_role_web_http_port`{ .sb-show-on-unchecked }`influxdb22_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        influxdb2_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        influxdb22_web_http_port:
        ```

    ??? variable string "`influxdb2_role_web_http_scheme`{ .sb-show-on-unchecked }`influxdb22_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        influxdb2_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        influxdb22_web_http_scheme:
        ```

    ??? variable dict/omit "`influxdb2_role_web_http_serverstransport`{ .sb-show-on-unchecked }`influxdb22_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        influxdb2_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        influxdb22_web_http_serverstransport:
        ```

    ??? variable string "`influxdb2_role_web_scheme`{ .sb-show-on-unchecked }`influxdb22_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        influxdb2_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        influxdb22_web_scheme:
        ```

    ??? variable dict/omit "`influxdb2_role_web_serverstransport`{ .sb-show-on-unchecked }`influxdb22_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        influxdb2_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        influxdb22_web_serverstransport:
        ```

    ??? variable string "`influxdb2_role_web_subdomain`{ .sb-show-on-unchecked }`influxdb22_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        influxdb2_role_web_subdomain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        influxdb22_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->