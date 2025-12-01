---
icon: material/docker
hide:
  - tags
tags:
  - thelounge
  - irc
  - chat
---

# The Lounge

## Overview

[linuxserver/thelounge](https://docs.linuxserver.io/images/docker-thelounge) is a Docker container image for The Lounge.

> [The Lounge](https://thelounge.chat/) is a self hosted web IRC client. In private mode, The Lounge acts like a bouncer and a client combined, in order to offer an experience similar to other modern chat applications outside the IRC world. Users can then access and resume their session without being disconnected from their channels. [:material-bookshelf:](https://thelounge.chat/docs) [:fontawesome-solid-people-group:](https://thelounge.chat/community)

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.linuxserver.io/general/container-customization){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/thelounge/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-thelounge
```

## Usage

Visit <https://thelounge.iYOUR_DOMAIN_NAMEi>.

## Basics

- When the application first runs, it will populate its /config
- Stop the container
- Now from the host, edit /config/config.js, wherever you've mapped it
- In most cases you want the value public: false to allow named users only
- Setting the two prefetch values to true improves usability, but uses more storage
- Once you have the configuration you want, save it and start the container again
- For each user, run the command

      ```shell
        docker exec -it thelounge s6-setuidgid abc thelounge add <user>
      ```

- You will be prompted to enter a password that will not be echoed.
- Saving logs to disk is the default, this consumes more space but allows scrollback.
- To log in to the application, browse to <https://thelounge.iYOUR_DOMAIN_NAMEi>
- You should now be prompted for a username and password on the webinterface.
- Once logged in, you can add an IRC network. Some defaults are preset for Freenode.

### ZNC

To connect to **[znc](../../sandbox/apps/znc.md)**, you need to have a **[znc](../../sandbox/apps/znc.md)** server running. A guide to using The Lounge with ZNC can be found [here](https://thelounge.chat/docs/guides/znc)

- In this image we have a ZNC network defined.

![ZNC network Screenshot](../../sandbox/images/znc_network.png)

- To add this network to The Lounge, give it a Name, it does not have to match the ZNC network settings.
- For the Server, use `znc` and set the port to `6502`
- For the Password, enter your `ZNC user password`
- Uncheck `Use secure connection (TLS)
- In the User Preferences section enter your Nick - I would recommend the same Nick as that set in ZNC.
- For the user name enter the `<ZNC username>/<ZNC_Network_Name>`.
- For Real Name, enter your desired `<real_name>` it does not need to match ZNC
- Save the network, and it should connect to ZNC.

![The Lounge network Screenshot](../../sandbox/images/lounge_network.png)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    thelounge_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `thelounge_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `thelounge_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`thelounge_name`"

        ```yaml
        # Type: string
        thelounge_name: thelounge
        ```

=== "Web"

    ??? variable string "`thelounge_role_web_subdomain`"

        ```yaml
        # Type: string
        thelounge_role_web_subdomain: "{{ thelounge_name }}"
        ```

    ??? variable string "`thelounge_role_web_domain`"

        ```yaml
        # Type: string
        thelounge_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`thelounge_role_web_port`"

        ```yaml
        # Type: string
        thelounge_role_web_port: "9000"
        ```

    ??? variable string "`thelounge_role_web_url`"

        ```yaml
        # Type: string
        thelounge_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='thelounge') + '.' + lookup('role_var', '_web_domain', role='thelounge')
                                 if (lookup('role_var', '_web_subdomain', role='thelounge') | length > 0)
                                 else lookup('role_var', '_web_domain', role='thelounge')) }}"
        ```

=== "DNS"

    ??? variable string "`thelounge_role_dns_record`"

        ```yaml
        # Type: string
        thelounge_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='thelounge') }}"
        ```

    ??? variable string "`thelounge_role_dns_zone`"

        ```yaml
        # Type: string
        thelounge_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='thelounge') }}"
        ```

    ??? variable bool "`thelounge_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`thelounge_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        thelounge_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`thelounge_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        thelounge_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`thelounge_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        thelounge_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`thelounge_role_traefik_certresolver`"

        ```yaml
        # Type: string
        thelounge_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`thelounge_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_traefik_enabled: true
        ```

    ??? variable bool "`thelounge_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_traefik_api_enabled: true
        ```

    ??? variable string "`thelounge_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        thelounge_role_traefik_api_endpoint: "PathPrefix(`/uploads`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`thelounge_role_docker_container`"

        ```yaml
        # Type: string
        thelounge_role_docker_container: "{{ thelounge_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`thelounge_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_image_pull: true
        ```

    ??? variable string "`thelounge_role_docker_image_repo`"

        ```yaml
        # Type: string
        thelounge_role_docker_image_repo: "lscr.io/linuxserver/thelounge"
        ```

    ??? variable string "`thelounge_role_docker_image_tag`"

        ```yaml
        # Type: string
        thelounge_role_docker_image_tag: "latest"
        ```

    ??? variable string "`thelounge_role_docker_image`"

        ```yaml
        # Type: string
        thelounge_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='thelounge') }}:{{ lookup('role_var', '_docker_image_tag', role='thelounge') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`thelounge_role_docker_envs_default`"

        ```yaml
        # Type: dict
        thelounge_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`thelounge_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        thelounge_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`thelounge_role_docker_volumes_default`"

        ```yaml
        # Type: list
        thelounge_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='thelounge') }}:/config"
        ```

    ??? variable list "`thelounge_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        thelounge_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`thelounge_role_docker_hostname`"

        ```yaml
        # Type: string
        thelounge_role_docker_hostname: "{{ thelounge_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`thelounge_role_docker_networks_alias`"

        ```yaml
        # Type: string
        thelounge_role_docker_networks_alias: "{{ thelounge_name }}"
        ```

    ??? variable list "`thelounge_role_docker_networks_default`"

        ```yaml
        # Type: list
        thelounge_role_docker_networks_default: []
        ```

    ??? variable list "`thelounge_role_docker_networks_custom`"

        ```yaml
        # Type: list
        thelounge_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`thelounge_role_docker_restart_policy`"

        ```yaml
        # Type: string
        thelounge_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`thelounge_role_docker_state`"

        ```yaml
        # Type: string
        thelounge_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`thelounge_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        thelounge_role_docker_blkio_weight:
        ```

    ??? variable int "`thelounge_role_docker_cpu_period`"

        ```yaml
        # Type: int
        thelounge_role_docker_cpu_period:
        ```

    ??? variable int "`thelounge_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        thelounge_role_docker_cpu_quota:
        ```

    ??? variable int "`thelounge_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        thelounge_role_docker_cpu_shares:
        ```

    ??? variable string "`thelounge_role_docker_cpus`"

        ```yaml
        # Type: string
        thelounge_role_docker_cpus:
        ```

    ??? variable string "`thelounge_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        thelounge_role_docker_cpuset_cpus:
        ```

    ??? variable string "`thelounge_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        thelounge_role_docker_cpuset_mems:
        ```

    ??? variable string "`thelounge_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        thelounge_role_docker_kernel_memory:
        ```

    ??? variable string "`thelounge_role_docker_memory`"

        ```yaml
        # Type: string
        thelounge_role_docker_memory:
        ```

    ??? variable string "`thelounge_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        thelounge_role_docker_memory_reservation:
        ```

    ??? variable string "`thelounge_role_docker_memory_swap`"

        ```yaml
        # Type: string
        thelounge_role_docker_memory_swap:
        ```

    ??? variable int "`thelounge_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        thelounge_role_docker_memory_swappiness:
        ```

    ??? variable string "`thelounge_role_docker_shm_size`"

        ```yaml
        # Type: string
        thelounge_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`thelounge_role_docker_cap_drop`"

        ```yaml
        # Type: list
        thelounge_role_docker_cap_drop:
        ```

    ??? variable string "`thelounge_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        thelounge_role_docker_cgroupns_mode:
        ```

    ??? variable list "`thelounge_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        thelounge_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`thelounge_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        thelounge_role_docker_device_read_bps:
        ```

    ??? variable list "`thelounge_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        thelounge_role_docker_device_read_iops:
        ```

    ??? variable list "`thelounge_role_docker_device_requests`"

        ```yaml
        # Type: list
        thelounge_role_docker_device_requests:
        ```

    ??? variable list "`thelounge_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        thelounge_role_docker_device_write_bps:
        ```

    ??? variable list "`thelounge_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        thelounge_role_docker_device_write_iops:
        ```

    ??? variable list "`thelounge_role_docker_devices`"

        ```yaml
        # Type: list
        thelounge_role_docker_devices:
        ```

    ??? variable string "`thelounge_role_docker_devices_default`"

        ```yaml
        # Type: string
        thelounge_role_docker_devices_default:
        ```

    ??? variable list "`thelounge_role_docker_groups`"

        ```yaml
        # Type: list
        thelounge_role_docker_groups:
        ```

    ??? variable bool "`thelounge_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_privileged:
        ```

    ??? variable list "`thelounge_role_docker_security_opts`"

        ```yaml
        # Type: list
        thelounge_role_docker_security_opts:
        ```

    ??? variable string "`thelounge_role_docker_user`"

        ```yaml
        # Type: string
        thelounge_role_docker_user:
        ```

    ??? variable string "`thelounge_role_docker_userns_mode`"

        ```yaml
        # Type: string
        thelounge_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`thelounge_role_docker_dns_opts`"

        ```yaml
        # Type: list
        thelounge_role_docker_dns_opts:
        ```

    ??? variable list "`thelounge_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        thelounge_role_docker_dns_search_domains:
        ```

    ??? variable list "`thelounge_role_docker_dns_servers`"

        ```yaml
        # Type: list
        thelounge_role_docker_dns_servers:
        ```

    ??? variable string "`thelounge_role_docker_domainname`"

        ```yaml
        # Type: string
        thelounge_role_docker_domainname:
        ```

    ??? variable list "`thelounge_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        thelounge_role_docker_exposed_ports:
        ```

    ??? variable dict "`thelounge_role_docker_hosts`"

        ```yaml
        # Type: dict
        thelounge_role_docker_hosts:
        ```

    ??? variable bool "`thelounge_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_hosts_use_common:
        ```

    ??? variable string "`thelounge_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        thelounge_role_docker_ipc_mode:
        ```

    ??? variable list "`thelounge_role_docker_links`"

        ```yaml
        # Type: list
        thelounge_role_docker_links:
        ```

    ??? variable string "`thelounge_role_docker_network_mode`"

        ```yaml
        # Type: string
        thelounge_role_docker_network_mode:
        ```

    ??? variable string "`thelounge_role_docker_pid_mode`"

        ```yaml
        # Type: string
        thelounge_role_docker_pid_mode:
        ```

    ??? variable list "`thelounge_role_docker_ports`"

        ```yaml
        # Type: list
        thelounge_role_docker_ports:
        ```

    ??? variable string "`thelounge_role_docker_uts`"

        ```yaml
        # Type: string
        thelounge_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`thelounge_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_keep_volumes:
        ```

    ??? variable list "`thelounge_role_docker_mounts`"

        ```yaml
        # Type: list
        thelounge_role_docker_mounts:
        ```

    ??? variable dict "`thelounge_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        thelounge_role_docker_storage_opts:
        ```

    ??? variable list "`thelounge_role_docker_tmpfs`"

        ```yaml
        # Type: list
        thelounge_role_docker_tmpfs:
        ```

    ??? variable string "`thelounge_role_docker_volume_driver`"

        ```yaml
        # Type: string
        thelounge_role_docker_volume_driver:
        ```

    ??? variable list "`thelounge_role_docker_volumes_from`"

        ```yaml
        # Type: list
        thelounge_role_docker_volumes_from:
        ```

    ??? variable bool "`thelounge_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_volumes_global:
        ```

    ??? variable string "`thelounge_role_docker_working_dir`"

        ```yaml
        # Type: string
        thelounge_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`thelounge_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_auto_remove:
        ```

    ??? variable bool "`thelounge_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_cleanup:
        ```

    ??? variable string "`thelounge_role_docker_force_kill`"

        ```yaml
        # Type: string
        thelounge_role_docker_force_kill:
        ```

    ??? variable dict "`thelounge_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        thelounge_role_docker_healthcheck:
        ```

    ??? variable int "`thelounge_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        thelounge_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`thelounge_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_init:
        ```

    ??? variable string "`thelounge_role_docker_kill_signal`"

        ```yaml
        # Type: string
        thelounge_role_docker_kill_signal:
        ```

    ??? variable string "`thelounge_role_docker_log_driver`"

        ```yaml
        # Type: string
        thelounge_role_docker_log_driver:
        ```

    ??? variable dict "`thelounge_role_docker_log_options`"

        ```yaml
        # Type: dict
        thelounge_role_docker_log_options:
        ```

    ??? variable bool "`thelounge_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_oom_killer:
        ```

    ??? variable int "`thelounge_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        thelounge_role_docker_oom_score_adj:
        ```

    ??? variable bool "`thelounge_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_output_logs:
        ```

    ??? variable bool "`thelounge_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_paused:
        ```

    ??? variable bool "`thelounge_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_recreate:
        ```

    ??? variable int "`thelounge_role_docker_restart_retries`"

        ```yaml
        # Type: int
        thelounge_role_docker_restart_retries:
        ```

    ??? variable int "`thelounge_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        thelounge_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`thelounge_role_docker_capabilities`"

        ```yaml
        # Type: list
        thelounge_role_docker_capabilities:
        ```

    ??? variable string "`thelounge_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        thelounge_role_docker_cgroup_parent:
        ```

    ??? variable list "`thelounge_role_docker_commands`"

        ```yaml
        # Type: list
        thelounge_role_docker_commands:
        ```

    ??? variable int "`thelounge_role_docker_create_timeout`"

        ```yaml
        # Type: int
        thelounge_role_docker_create_timeout:
        ```

    ??? variable string "`thelounge_role_docker_entrypoint`"

        ```yaml
        # Type: string
        thelounge_role_docker_entrypoint:
        ```

    ??? variable string "`thelounge_role_docker_env_file`"

        ```yaml
        # Type: string
        thelounge_role_docker_env_file:
        ```

    ??? variable dict "`thelounge_role_docker_labels`"

        ```yaml
        # Type: dict
        thelounge_role_docker_labels:
        ```

    ??? variable bool "`thelounge_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_labels_use_common:
        ```

    ??? variable bool "`thelounge_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_read_only:
        ```

    ??? variable string "`thelounge_role_docker_runtime`"

        ```yaml
        # Type: string
        thelounge_role_docker_runtime:
        ```

    ??? variable list "`thelounge_role_docker_sysctls`"

        ```yaml
        # Type: list
        thelounge_role_docker_sysctls:
        ```

    ??? variable list "`thelounge_role_docker_ulimits`"

        ```yaml
        # Type: list
        thelounge_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`thelounge_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        thelounge_role_autoheal_enabled: true
        ```

    ??? variable string "`thelounge_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        thelounge_role_depends_on: ""
        ```

    ??? variable string "`thelounge_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        thelounge_role_depends_on_delay: "0"
        ```

    ??? variable string "`thelounge_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        thelounge_role_depends_on_healthchecks:
        ```

    ??? variable bool "`thelounge_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        thelounge_role_diun_enabled: true
        ```

    ??? variable bool "`thelounge_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        thelounge_role_dns_enabled: true
        ```

    ??? variable bool "`thelounge_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        thelounge_role_docker_controller: true
        ```

    ??? variable string "`thelounge_role_docker_image_repo`"

        ```yaml
        # Type: string
        thelounge_role_docker_image_repo:
        ```

    ??? variable string "`thelounge_role_docker_image_tag`"

        ```yaml
        # Type: string
        thelounge_role_docker_image_tag:
        ```

    ??? variable bool "`thelounge_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_docker_volumes_download:
        ```

    ??? variable string "`thelounge_role_paths_location`"

        ```yaml
        # Type: string
        thelounge_role_paths_location:
        ```

    ??? variable string "`thelounge_role_themepark_addons`"

        ```yaml
        # Type: string
        thelounge_role_themepark_addons:
        ```

    ??? variable string "`thelounge_role_themepark_app`"

        ```yaml
        # Type: string
        thelounge_role_themepark_app:
        ```

    ??? variable string "`thelounge_role_themepark_theme`"

        ```yaml
        # Type: string
        thelounge_role_themepark_theme:
        ```

    ??? variable dict/omit "`thelounge_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        thelounge_role_traefik_api_endpoint:
        ```

    ??? variable string "`thelounge_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        thelounge_role_traefik_api_middleware:
        ```

    ??? variable string "`thelounge_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        thelounge_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`thelounge_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        thelounge_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`thelounge_role_traefik_certresolver`"

        ```yaml
        # Type: string
        thelounge_role_traefik_certresolver:
        ```

    ??? variable bool "`thelounge_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        thelounge_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`thelounge_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        thelounge_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`thelounge_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        thelounge_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`thelounge_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        thelounge_role_traefik_middleware_http:
        ```

    ??? variable bool "`thelounge_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`thelounge_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        thelounge_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`thelounge_role_traefik_priority`"

        ```yaml
        # Type: string
        thelounge_role_traefik_priority:
        ```

    ??? variable bool "`thelounge_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        thelounge_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`thelounge_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        thelounge_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`thelounge_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        thelounge_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`thelounge_role_web_domain`"

        ```yaml
        # Type: string
        thelounge_role_web_domain:
        ```

    ??? variable list "`thelounge_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        thelounge_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            thelounge_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "thelounge2.{{ user.domain }}"
              - "thelounge.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`thelounge_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        thelounge_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            thelounge_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'thelounge2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`thelounge_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        thelounge_role_web_http_port:
        ```

    ??? variable string "`thelounge_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        thelounge_role_web_http_scheme:
        ```

    ??? variable dict/omit "`thelounge_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        thelounge_role_web_http_serverstransport:
        ```

    ??? variable string "`thelounge_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        thelounge_role_web_scheme:
        ```

    ??? variable dict/omit "`thelounge_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        thelounge_role_web_serverstransport:
        ```

    ??? variable string "`thelounge_role_web_subdomain`"

        ```yaml
        # Type: string
        thelounge_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->