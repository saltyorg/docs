---
icon: material/docker
hide:
  - tags
tags:
  - membarr
  - discord
  - automation
---

# Membarr

## Overview

[Membarr](https://github.com/Yoruio/Membarr) is a fork of Invitarr that invites discord users to Plex and Jellyfin. You can also automate this bot to invite discord users to a media server once a certain role is given to a user or the user can also be added manually.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/Yoruio/Membarr){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/yoruio/membarr/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-membarr
```

## Usage

## Basics

### Create Discord bot

1. Create the Discord server that your users will get member roles or use an existing discord that you can assign roles from.
2. Log into the [Discord Developer Portal] and click 'New Application'
3. Add a short description and an icon for the bot. Save changes. *(Optional)*
4. Go to **Bot** section in the side menu.
5. Uncheck 'Public Bot' under **Authorization Flow**
6. Check all 3 boxes under Privileged Gateway Intents: **Presence Intent**, **Server Members Intent**, and **Message Content Intent**. Save changes.
7. Copy the token under the username or reset it to copy. This is the token used in the docker image.
8. Go to **OAuth2** section in the side menu, then click **URL Generator**.
9. Under **Scopes**, check **bot** and **applications.commands**.
10. Copy the **Generated URL** and paste into your browser and add it to your discord server from Step 1.
11. The bot will come online after the docker container is running with the correct Bot Token.

  [Discord Developer Portal]: https://discord.com/developers/applications

### Set up Plex parameters

When you install the role, it will create 2 files, an `app.db` file and `config.ini`. You will need to edit the `config.ini` file with your preferred editing program. (ie `nano` or `vim` etc) Add your Plex credentials like so:

```toml
[bot_envs]
plex_user =
plex_pass =
plex_server_name = ServerFriendlyName
plex_roles =
plex_token = token
plex_base_url = https://plex.xYOUR_DOMAIN_NAMEx
plex_enabled = True
```

Now restart the Membarr container `docker restart membarr`.

???+ Success "Plex Token"
    To get the Plex token, you will run the following command: `sb install plex-auth-token`
    Look for the **Display Plex Auth Token** task in the log.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    membarr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `membarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `membarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`membarr_name`"

        ```yaml
        # Type: string
        membarr_name: membarr
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`membarr_role_docker_container`"

        ```yaml
        # Type: string
        membarr_role_docker_container: "{{ membarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`membarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_image_pull: true
        ```

    ??? variable string "`membarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        membarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`membarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        membarr_role_docker_image_repo: "yoruio/membarr"
        ```

    ??? variable string "`membarr_role_docker_image`"

        ```yaml
        # Type: string
        membarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='membarr') }}:{{ lookup('role_var', '_docker_image_tag', role='membarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`membarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        membarr_role_docker_envs_default:
          TZ: "{{ tz }}"
          token: "{{ membarr.discord_token }}"
        ```

    ??? variable dict "`membarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        membarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`membarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        membarr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='membarr') }}:/app/app/config"
        ```

    ??? variable list "`membarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        membarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`membarr_role_docker_hostname`"

        ```yaml
        # Type: string
        membarr_role_docker_hostname: "{{ membarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`membarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        membarr_role_docker_networks_alias: "{{ membarr_name }}"
        ```

    ??? variable list "`membarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        membarr_role_docker_networks_default: []
        ```

    ??? variable list "`membarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        membarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`membarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        membarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`membarr_role_docker_state`"

        ```yaml
        # Type: string
        membarr_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`membarr_role_docker_user`"

        ```yaml
        # Type: string
        membarr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`membarr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        membarr_role_docker_blkio_weight:
        ```

    ??? variable int "`membarr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        membarr_role_docker_cpu_period:
        ```

    ??? variable int "`membarr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        membarr_role_docker_cpu_quota:
        ```

    ??? variable int "`membarr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        membarr_role_docker_cpu_shares:
        ```

    ??? variable string "`membarr_role_docker_cpus`"

        ```yaml
        # Type: string
        membarr_role_docker_cpus:
        ```

    ??? variable string "`membarr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        membarr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`membarr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        membarr_role_docker_cpuset_mems:
        ```

    ??? variable string "`membarr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        membarr_role_docker_kernel_memory:
        ```

    ??? variable string "`membarr_role_docker_memory`"

        ```yaml
        # Type: string
        membarr_role_docker_memory:
        ```

    ??? variable string "`membarr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        membarr_role_docker_memory_reservation:
        ```

    ??? variable string "`membarr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        membarr_role_docker_memory_swap:
        ```

    ??? variable int "`membarr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        membarr_role_docker_memory_swappiness:
        ```

    ??? variable string "`membarr_role_docker_shm_size`"

        ```yaml
        # Type: string
        membarr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`membarr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        membarr_role_docker_cap_drop:
        ```

    ??? variable string "`membarr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        membarr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`membarr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        membarr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`membarr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        membarr_role_docker_device_read_bps:
        ```

    ??? variable list "`membarr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        membarr_role_docker_device_read_iops:
        ```

    ??? variable list "`membarr_role_docker_device_requests`"

        ```yaml
        # Type: list
        membarr_role_docker_device_requests:
        ```

    ??? variable list "`membarr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        membarr_role_docker_device_write_bps:
        ```

    ??? variable list "`membarr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        membarr_role_docker_device_write_iops:
        ```

    ??? variable list "`membarr_role_docker_devices`"

        ```yaml
        # Type: list
        membarr_role_docker_devices:
        ```

    ??? variable string "`membarr_role_docker_devices_default`"

        ```yaml
        # Type: string
        membarr_role_docker_devices_default:
        ```

    ??? variable list "`membarr_role_docker_groups`"

        ```yaml
        # Type: list
        membarr_role_docker_groups:
        ```

    ??? variable bool "`membarr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_privileged:
        ```

    ??? variable list "`membarr_role_docker_security_opts`"

        ```yaml
        # Type: list
        membarr_role_docker_security_opts:
        ```

    ??? variable string "`membarr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        membarr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`membarr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        membarr_role_docker_dns_opts:
        ```

    ??? variable list "`membarr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        membarr_role_docker_dns_search_domains:
        ```

    ??? variable list "`membarr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        membarr_role_docker_dns_servers:
        ```

    ??? variable string "`membarr_role_docker_domainname`"

        ```yaml
        # Type: string
        membarr_role_docker_domainname:
        ```

    ??? variable list "`membarr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        membarr_role_docker_exposed_ports:
        ```

    ??? variable dict "`membarr_role_docker_hosts`"

        ```yaml
        # Type: dict
        membarr_role_docker_hosts:
        ```

    ??? variable bool "`membarr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_hosts_use_common:
        ```

    ??? variable string "`membarr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        membarr_role_docker_ipc_mode:
        ```

    ??? variable list "`membarr_role_docker_links`"

        ```yaml
        # Type: list
        membarr_role_docker_links:
        ```

    ??? variable string "`membarr_role_docker_network_mode`"

        ```yaml
        # Type: string
        membarr_role_docker_network_mode:
        ```

    ??? variable string "`membarr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        membarr_role_docker_pid_mode:
        ```

    ??? variable list "`membarr_role_docker_ports`"

        ```yaml
        # Type: list
        membarr_role_docker_ports:
        ```

    ??? variable string "`membarr_role_docker_uts`"

        ```yaml
        # Type: string
        membarr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`membarr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_keep_volumes:
        ```

    ??? variable list "`membarr_role_docker_mounts`"

        ```yaml
        # Type: list
        membarr_role_docker_mounts:
        ```

    ??? variable dict "`membarr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        membarr_role_docker_storage_opts:
        ```

    ??? variable list "`membarr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        membarr_role_docker_tmpfs:
        ```

    ??? variable string "`membarr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        membarr_role_docker_volume_driver:
        ```

    ??? variable list "`membarr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        membarr_role_docker_volumes_from:
        ```

    ??? variable bool "`membarr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_volumes_global:
        ```

    ??? variable string "`membarr_role_docker_working_dir`"

        ```yaml
        # Type: string
        membarr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`membarr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_auto_remove:
        ```

    ??? variable bool "`membarr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_cleanup:
        ```

    ??? variable string "`membarr_role_docker_force_kill`"

        ```yaml
        # Type: string
        membarr_role_docker_force_kill:
        ```

    ??? variable dict "`membarr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        membarr_role_docker_healthcheck:
        ```

    ??? variable int "`membarr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        membarr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`membarr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_init:
        ```

    ??? variable string "`membarr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        membarr_role_docker_kill_signal:
        ```

    ??? variable string "`membarr_role_docker_log_driver`"

        ```yaml
        # Type: string
        membarr_role_docker_log_driver:
        ```

    ??? variable dict "`membarr_role_docker_log_options`"

        ```yaml
        # Type: dict
        membarr_role_docker_log_options:
        ```

    ??? variable bool "`membarr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_oom_killer:
        ```

    ??? variable int "`membarr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        membarr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`membarr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_output_logs:
        ```

    ??? variable bool "`membarr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_paused:
        ```

    ??? variable bool "`membarr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_recreate:
        ```

    ??? variable int "`membarr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        membarr_role_docker_restart_retries:
        ```

    ??? variable int "`membarr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        membarr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`membarr_role_docker_capabilities`"

        ```yaml
        # Type: list
        membarr_role_docker_capabilities:
        ```

    ??? variable string "`membarr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        membarr_role_docker_cgroup_parent:
        ```

    ??? variable list "`membarr_role_docker_commands`"

        ```yaml
        # Type: list
        membarr_role_docker_commands:
        ```

    ??? variable int "`membarr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        membarr_role_docker_create_timeout:
        ```

    ??? variable string "`membarr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        membarr_role_docker_entrypoint:
        ```

    ??? variable string "`membarr_role_docker_env_file`"

        ```yaml
        # Type: string
        membarr_role_docker_env_file:
        ```

    ??? variable dict "`membarr_role_docker_labels`"

        ```yaml
        # Type: dict
        membarr_role_docker_labels:
        ```

    ??? variable bool "`membarr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_labels_use_common:
        ```

    ??? variable bool "`membarr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_read_only:
        ```

    ??? variable string "`membarr_role_docker_runtime`"

        ```yaml
        # Type: string
        membarr_role_docker_runtime:
        ```

    ??? variable list "`membarr_role_docker_sysctls`"

        ```yaml
        # Type: list
        membarr_role_docker_sysctls:
        ```

    ??? variable list "`membarr_role_docker_ulimits`"

        ```yaml
        # Type: list
        membarr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`membarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        membarr_role_autoheal_enabled: true
        ```

    ??? variable string "`membarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        membarr_role_depends_on: ""
        ```

    ??? variable string "`membarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        membarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`membarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        membarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`membarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        membarr_role_diun_enabled: true
        ```

    ??? variable bool "`membarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        membarr_role_docker_controller: true
        ```

    ??? variable string "`membarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        membarr_role_docker_image_repo:
        ```

    ??? variable string "`membarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        membarr_role_docker_image_tag:
        ```

    ??? variable bool "`membarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        membarr_role_docker_volumes_download:
        ```

    ??? variable string "`membarr_role_paths_location`"

        ```yaml
        # Type: string
        membarr_role_paths_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->