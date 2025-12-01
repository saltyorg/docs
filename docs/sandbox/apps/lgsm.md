---
icon: material/docker
hide:
  - tags
tags:
  - lgsm
  - gaming
  - server
---

# LinuxGSM

## Overview

[LinuxGSM](https://linuxgsm.com) is a command-line tool for quick and simple deployment and management of Linux dedicated game servers. It aims to make the process of managing game servers hassle-free. With LinuxGSM, we can avoid spending hours trying to configure and manage game servers. It provides a streamlined and efficient solution for setting up and maintaining dedicated game servers on Linux.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.linuxgsm.com){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/gameservermanagers/gameserver/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Configuration

To add instances, add the following to the inventory. See these instructions on inventory [here](../../saltbox/inventory/index.md).

```yaml title="Inventory"
lgsm_instances: ["lgsm_valheim", "lgsm_rust"] # (1)!
lgsm_valheim_docker_image_tag: "vh" # (2)!
lgsm_valheim_docker_ports_defaults: ["2456:2456/udp","2457:2457/udp"] # (3)!
lgsm_rust_docker_ports_defaults: ["28015:28015/udp","28017:28017/udp","28082:28082/udp"] # (4)!
```

1. Example setting image tag to correct shortcode from <https://github.com/GameServerManagers/LinuxGSM/blob/master/lgsm/data/serverlist.csv> using lgsm_shortcode will automatically pull the correct image tag
2. This is the valheim server shortcode
3. ports for valheim need to be exposed. Notice that rust is the image tag for the rust server. This means we don't have to specify it here.
4. The ports for the rust server need to be exposed as well.

Then run:

## Deployment

```shell
sb install sandbox-lgsm
```

## Usage

Visit <https://lgsm.iYOUR_DOMAIN_NAMEi>.

## Basics

LinuxGSM config files are the configuration files used by the game server to store various game server settings, such as the server name, maximum players, map cycle, etc. These settings can be edited to customise a game server. Different game server configs can use different syntax and work slightly differently, but all do the same basic job of editing a game server settings.

The configs for the lgsm servers are in `/opt/CONTAINERNAME/config-lgsm/LGSMSERVERNAME/`
For our valheim example the config would be `/opt/lgsm_valheim/config-lgsm/vhserver/vhserver.cfg` which is the lgsm instance config for that server.

`/opt/lgsm_valheim/config-lgsm/vhserver/common.cfg` works as well. Can read more [here](https://docs.linuxgsm.com/configuration/game-server-config)

Any actual game server configs will be in the `/opt/CONTAINERNAME/serverfiles/` and are all dependant on the game server installed.

In your game, connect to your ip and default ports for the server. Make sure you set the UDP and TCP for the ports correctly. If everything was setup correctly the game should connect to the server.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `lgsm_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of lgsm:" }
    lgsm_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `lgsm2`):" }
    lgsm2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `lgsm_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `lgsm_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`lgsm_instances`"

        ```yaml
        # Type: list
        lgsm_instances: []
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            lgsm_instances: ["lgsm", "lgsm2"]
            ```

=== "Paths"

    ??? variable string "`lgsm_role_paths_folder`{ .sb-show-on-unchecked }`lgsm2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_paths_folder: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_paths_folder: "{{ lgsm_name }}"
        ```

    ??? variable string "`lgsm_role_paths_location`{ .sb-show-on-unchecked }`lgsm2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_paths_location: "{{ server_appdata_path }}/{{ lgsm_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_paths_location: "{{ server_appdata_path }}/{{ lgsm_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`lgsm_role_web_subdomain`{ .sb-show-on-unchecked }`lgsm2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_web_subdomain: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_web_subdomain: "{{ lgsm_name }}"
        ```

    ??? variable string "`lgsm_role_web_domain`{ .sb-show-on-unchecked }`lgsm2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_web_domain: "{{ user.domain }}"
        ```

=== "DNS"

    ??? variable string "`lgsm_role_dns_record`{ .sb-show-on-unchecked }`lgsm2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lgsm') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lgsm') }}"
        ```

    ??? variable string "`lgsm_role_dns_zone`{ .sb-show-on-unchecked }`lgsm2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lgsm') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_dns_zone: "{{ lookup('role_var', '_web_domain', role='lgsm') }}"
        ```

    ??? variable bool "`lgsm_role_dns_proxy`{ .sb-show-on-unchecked }`lgsm2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_dns_proxy: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_dns_proxy: false
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`lgsm_role_docker_container`{ .sb-show-on-unchecked }`lgsm2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_container: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_container: "{{ lgsm_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`lgsm_role_docker_image_pull`{ .sb-show-on-unchecked }`lgsm2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_image_pull: true
        ```

    ??? variable string "`lgsm_role_docker_image_repo`{ .sb-show-on-unchecked }`lgsm2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image_repo: "gameservermanagers/gameserver"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image_repo: "gameservermanagers/gameserver"
        ```

    ??? variable string "`lgsm_role_docker_image_tag`{ .sb-show-on-unchecked }`lgsm2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image_tag: "{{ lgsm_name | replace('lgsm_', '') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image_tag: "{{ lgsm_name | replace('lgsm_', '') }}"
        ```

    ??? variable string "`lgsm_role_docker_image`{ .sb-show-on-unchecked }`lgsm2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lgsm') }}:{{ lookup('role_var', '_docker_image_tag', role='lgsm') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lgsm') }}:{{ lookup('role_var', '_docker_image_tag', role='lgsm') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`lgsm_role_docker_volumes_default`{ .sb-show-on-unchecked }`lgsm2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='lgsm') }}:/data"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='lgsm') }}:/data"
        ```

    ??? variable list "`lgsm_role_docker_volumes_custom`{ .sb-show-on-unchecked }`lgsm2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`lgsm_role_docker_hostname`{ .sb-show-on-unchecked }`lgsm2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_hostname: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_hostname: "{{ lgsm_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`lgsm_role_docker_networks_alias`{ .sb-show-on-unchecked }`lgsm2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_networks_alias: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_networks_alias: "{{ lgsm_name }}"
        ```

    ??? variable list "`lgsm_role_docker_networks_default`{ .sb-show-on-unchecked }`lgsm2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_networks_default: []
        ```

    ??? variable list "`lgsm_role_docker_networks_custom`{ .sb-show-on-unchecked }`lgsm2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`lgsm_role_docker_restart_policy`{ .sb-show-on-unchecked }`lgsm2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`lgsm_role_docker_state`{ .sb-show-on-unchecked }`lgsm2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`lgsm_role_docker_blkio_weight`{ .sb-show-on-unchecked }`lgsm2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_blkio_weight:
        ```

    ??? variable int "`lgsm_role_docker_cpu_period`{ .sb-show-on-unchecked }`lgsm2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_cpu_period:
        ```

    ??? variable int "`lgsm_role_docker_cpu_quota`{ .sb-show-on-unchecked }`lgsm2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_cpu_quota:
        ```

    ??? variable int "`lgsm_role_docker_cpu_shares`{ .sb-show-on-unchecked }`lgsm2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_cpu_shares:
        ```

    ??? variable string "`lgsm_role_docker_cpus`{ .sb-show-on-unchecked }`lgsm2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_cpus:
        ```

    ??? variable string "`lgsm_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`lgsm2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_cpuset_cpus:
        ```

    ??? variable string "`lgsm_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`lgsm2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_cpuset_mems:
        ```

    ??? variable string "`lgsm_role_docker_kernel_memory`{ .sb-show-on-unchecked }`lgsm2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_kernel_memory:
        ```

    ??? variable string "`lgsm_role_docker_memory`{ .sb-show-on-unchecked }`lgsm2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_memory:
        ```

    ??? variable string "`lgsm_role_docker_memory_reservation`{ .sb-show-on-unchecked }`lgsm2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_memory_reservation:
        ```

    ??? variable string "`lgsm_role_docker_memory_swap`{ .sb-show-on-unchecked }`lgsm2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_memory_swap:
        ```

    ??? variable int "`lgsm_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`lgsm2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_memory_swappiness:
        ```

    ??? variable string "`lgsm_role_docker_shm_size`{ .sb-show-on-unchecked }`lgsm2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`lgsm_role_docker_cap_drop`{ .sb-show-on-unchecked }`lgsm2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_cap_drop:
        ```

    ??? variable string "`lgsm_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`lgsm2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_cgroupns_mode:
        ```

    ??? variable list "`lgsm_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`lgsm2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_device_cgroup_rules:
        ```

    ??? variable list "`lgsm_role_docker_device_read_bps`{ .sb-show-on-unchecked }`lgsm2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_device_read_bps:
        ```

    ??? variable list "`lgsm_role_docker_device_read_iops`{ .sb-show-on-unchecked }`lgsm2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_device_read_iops:
        ```

    ??? variable list "`lgsm_role_docker_device_requests`{ .sb-show-on-unchecked }`lgsm2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_device_requests:
        ```

    ??? variable list "`lgsm_role_docker_device_write_bps`{ .sb-show-on-unchecked }`lgsm2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_device_write_bps:
        ```

    ??? variable list "`lgsm_role_docker_device_write_iops`{ .sb-show-on-unchecked }`lgsm2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_device_write_iops:
        ```

    ??? variable list "`lgsm_role_docker_devices`{ .sb-show-on-unchecked }`lgsm2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_devices:
        ```

    ??? variable string "`lgsm_role_docker_devices_default`{ .sb-show-on-unchecked }`lgsm2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_devices_default:
        ```

    ??? variable list "`lgsm_role_docker_groups`{ .sb-show-on-unchecked }`lgsm2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_groups:
        ```

    ??? variable bool "`lgsm_role_docker_privileged`{ .sb-show-on-unchecked }`lgsm2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_privileged:
        ```

    ??? variable list "`lgsm_role_docker_security_opts`{ .sb-show-on-unchecked }`lgsm2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_security_opts:
        ```

    ??? variable string "`lgsm_role_docker_user`{ .sb-show-on-unchecked }`lgsm2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_user:
        ```

    ??? variable string "`lgsm_role_docker_userns_mode`{ .sb-show-on-unchecked }`lgsm2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`lgsm_role_docker_dns_opts`{ .sb-show-on-unchecked }`lgsm2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_dns_opts:
        ```

    ??? variable list "`lgsm_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`lgsm2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_dns_search_domains:
        ```

    ??? variable list "`lgsm_role_docker_dns_servers`{ .sb-show-on-unchecked }`lgsm2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_dns_servers:
        ```

    ??? variable string "`lgsm_role_docker_domainname`{ .sb-show-on-unchecked }`lgsm2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_domainname:
        ```

    ??? variable list "`lgsm_role_docker_exposed_ports`{ .sb-show-on-unchecked }`lgsm2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_exposed_ports:
        ```

    ??? variable dict "`lgsm_role_docker_hosts`{ .sb-show-on-unchecked }`lgsm2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        lgsm_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        lgsm2_docker_hosts:
        ```

    ??? variable bool "`lgsm_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`lgsm2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_hosts_use_common:
        ```

    ??? variable string "`lgsm_role_docker_ipc_mode`{ .sb-show-on-unchecked }`lgsm2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_ipc_mode:
        ```

    ??? variable list "`lgsm_role_docker_links`{ .sb-show-on-unchecked }`lgsm2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_links:
        ```

    ??? variable string "`lgsm_role_docker_network_mode`{ .sb-show-on-unchecked }`lgsm2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_network_mode:
        ```

    ??? variable string "`lgsm_role_docker_pid_mode`{ .sb-show-on-unchecked }`lgsm2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_pid_mode:
        ```

    ??? variable list "`lgsm_role_docker_ports`{ .sb-show-on-unchecked }`lgsm2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_ports:
        ```

    ??? variable string "`lgsm_role_docker_uts`{ .sb-show-on-unchecked }`lgsm2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`lgsm_role_docker_keep_volumes`{ .sb-show-on-unchecked }`lgsm2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_keep_volumes:
        ```

    ??? variable list "`lgsm_role_docker_mounts`{ .sb-show-on-unchecked }`lgsm2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_mounts:
        ```

    ??? variable dict "`lgsm_role_docker_storage_opts`{ .sb-show-on-unchecked }`lgsm2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        lgsm_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        lgsm2_docker_storage_opts:
        ```

    ??? variable list "`lgsm_role_docker_tmpfs`{ .sb-show-on-unchecked }`lgsm2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_tmpfs:
        ```

    ??? variable string "`lgsm_role_docker_volume_driver`{ .sb-show-on-unchecked }`lgsm2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_volume_driver:
        ```

    ??? variable list "`lgsm_role_docker_volumes_from`{ .sb-show-on-unchecked }`lgsm2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_volumes_from:
        ```

    ??? variable bool "`lgsm_role_docker_volumes_global`{ .sb-show-on-unchecked }`lgsm2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_volumes_global:
        ```

    ??? variable string "`lgsm_role_docker_working_dir`{ .sb-show-on-unchecked }`lgsm2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`lgsm_role_docker_auto_remove`{ .sb-show-on-unchecked }`lgsm2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_auto_remove:
        ```

    ??? variable bool "`lgsm_role_docker_cleanup`{ .sb-show-on-unchecked }`lgsm2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_cleanup:
        ```

    ??? variable string "`lgsm_role_docker_force_kill`{ .sb-show-on-unchecked }`lgsm2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_force_kill:
        ```

    ??? variable dict "`lgsm_role_docker_healthcheck`{ .sb-show-on-unchecked }`lgsm2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        lgsm_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        lgsm2_docker_healthcheck:
        ```

    ??? variable int "`lgsm_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`lgsm2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`lgsm_role_docker_init`{ .sb-show-on-unchecked }`lgsm2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_init:
        ```

    ??? variable string "`lgsm_role_docker_kill_signal`{ .sb-show-on-unchecked }`lgsm2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_kill_signal:
        ```

    ??? variable string "`lgsm_role_docker_log_driver`{ .sb-show-on-unchecked }`lgsm2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_log_driver:
        ```

    ??? variable dict "`lgsm_role_docker_log_options`{ .sb-show-on-unchecked }`lgsm2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        lgsm_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        lgsm2_docker_log_options:
        ```

    ??? variable bool "`lgsm_role_docker_oom_killer`{ .sb-show-on-unchecked }`lgsm2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_oom_killer:
        ```

    ??? variable int "`lgsm_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`lgsm2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_oom_score_adj:
        ```

    ??? variable bool "`lgsm_role_docker_output_logs`{ .sb-show-on-unchecked }`lgsm2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_output_logs:
        ```

    ??? variable bool "`lgsm_role_docker_paused`{ .sb-show-on-unchecked }`lgsm2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_paused:
        ```

    ??? variable bool "`lgsm_role_docker_recreate`{ .sb-show-on-unchecked }`lgsm2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_recreate:
        ```

    ??? variable int "`lgsm_role_docker_restart_retries`{ .sb-show-on-unchecked }`lgsm2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_restart_retries:
        ```

    ??? variable int "`lgsm_role_docker_stop_timeout`{ .sb-show-on-unchecked }`lgsm2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`lgsm_role_docker_capabilities`{ .sb-show-on-unchecked }`lgsm2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_capabilities:
        ```

    ??? variable string "`lgsm_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`lgsm2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_cgroup_parent:
        ```

    ??? variable list "`lgsm_role_docker_commands`{ .sb-show-on-unchecked }`lgsm2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_commands:
        ```

    ??? variable int "`lgsm_role_docker_create_timeout`{ .sb-show-on-unchecked }`lgsm2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        lgsm_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        lgsm2_docker_create_timeout:
        ```

    ??? variable string "`lgsm_role_docker_entrypoint`{ .sb-show-on-unchecked }`lgsm2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_entrypoint:
        ```

    ??? variable string "`lgsm_role_docker_env_file`{ .sb-show-on-unchecked }`lgsm2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_env_file:
        ```

    ??? variable dict "`lgsm_role_docker_envs`{ .sb-show-on-unchecked }`lgsm2_docker_envs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        lgsm_role_docker_envs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        lgsm2_docker_envs:
        ```

    ??? variable dict "`lgsm_role_docker_labels`{ .sb-show-on-unchecked }`lgsm2_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        lgsm_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        lgsm2_docker_labels:
        ```

    ??? variable bool "`lgsm_role_docker_labels_use_common`{ .sb-show-on-unchecked }`lgsm2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_labels_use_common:
        ```

    ??? variable bool "`lgsm_role_docker_read_only`{ .sb-show-on-unchecked }`lgsm2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_read_only:
        ```

    ??? variable string "`lgsm_role_docker_runtime`{ .sb-show-on-unchecked }`lgsm2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_runtime:
        ```

    ??? variable list "`lgsm_role_docker_sysctls`{ .sb-show-on-unchecked }`lgsm2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_sysctls:
        ```

    ??? variable list "`lgsm_role_docker_ulimits`{ .sb-show-on-unchecked }`lgsm2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`lgsm_role_autoheal_enabled`{ .sb-show-on-unchecked }`lgsm2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        lgsm_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        lgsm2_autoheal_enabled: true
        ```

    ??? variable string "`lgsm_role_depends_on`{ .sb-show-on-unchecked }`lgsm2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        lgsm_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        lgsm2_depends_on: ""
        ```

    ??? variable string "`lgsm_role_depends_on_delay`{ .sb-show-on-unchecked }`lgsm2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        lgsm_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        lgsm2_depends_on_delay: "0"
        ```

    ??? variable string "`lgsm_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`lgsm2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lgsm_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lgsm2_depends_on_healthchecks:
        ```

    ??? variable bool "`lgsm_role_diun_enabled`{ .sb-show-on-unchecked }`lgsm2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        lgsm_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        lgsm2_diun_enabled: true
        ```

    ??? variable bool "`lgsm_role_dns_enabled`{ .sb-show-on-unchecked }`lgsm2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        lgsm_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        lgsm2_dns_enabled: true
        ```

    ??? variable bool "`lgsm_role_docker_controller`{ .sb-show-on-unchecked }`lgsm2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        lgsm_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        lgsm2_docker_controller: true
        ```

    ??? variable string "`lgsm_role_docker_image_repo`{ .sb-show-on-unchecked }`lgsm2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image_repo:
        ```

    ??? variable string "`lgsm_role_docker_image_tag`{ .sb-show-on-unchecked }`lgsm2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image_tag:
        ```

    ??? variable bool "`lgsm_role_docker_volumes_download`{ .sb-show-on-unchecked }`lgsm2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_volumes_download:
        ```

    ??? variable string "`lgsm_role_paths_location`{ .sb-show-on-unchecked }`lgsm2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_paths_location:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_paths_location:
        ```

    ??? variable string "`lgsm_role_web_domain`{ .sb-show-on-unchecked }`lgsm2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_web_domain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_web_domain:
        ```

    ??? variable list "`lgsm_role_web_fqdn_override`{ .sb-show-on-unchecked }`lgsm2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        lgsm_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        lgsm2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            lgsm_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lgsm2.{{ user.domain }}"
              - "lgsm.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            lgsm2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lgsm2.{{ user.domain }}"
              - "lgsm.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`lgsm_role_web_host_override`{ .sb-show-on-unchecked }`lgsm2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        lgsm_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        lgsm2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            lgsm_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lgsm2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            lgsm2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lgsm2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`lgsm_role_web_http_port`{ .sb-show-on-unchecked }`lgsm2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        lgsm_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        lgsm2_web_http_port:
        ```

    ??? variable string "`lgsm_role_web_http_scheme`{ .sb-show-on-unchecked }`lgsm2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        lgsm_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        lgsm2_web_http_scheme:
        ```

    ??? variable dict/omit "`lgsm_role_web_http_serverstransport`{ .sb-show-on-unchecked }`lgsm2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        lgsm_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        lgsm2_web_http_serverstransport:
        ```

    ??? variable string "`lgsm_role_web_scheme`{ .sb-show-on-unchecked }`lgsm2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        lgsm_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        lgsm2_web_scheme:
        ```

    ??? variable dict/omit "`lgsm_role_web_serverstransport`{ .sb-show-on-unchecked }`lgsm2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        lgsm_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        lgsm2_web_serverstransport:
        ```

    ??? variable string "`lgsm_role_web_subdomain`{ .sb-show-on-unchecked }`lgsm2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_web_subdomain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
