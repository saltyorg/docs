---
icon: material/docker
hide:
  - tags
tags:
  - doplarr
  - media
  - discord
saltbox_automation:
  app_links:
    - name: Manual
      url: https://kiranshila.github.io/Doplarr/#/configuration
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/doplarr/tags
      type: docker
    - name: Community
      url: https://linuxserver.io/discord
      type: discord
  project_description:
    name: Doplarr
    summary: |-
      a chatbot used to simplify using services like Sonarr/Radarr/Overseer via the use of chat. Current platform is Discord only.
    link: https://kiranshila.github.io/Doplarr/#
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Doplarr

## Overview

[Doplarr](https://kiranshila.github.io/Doplarr/#) is a chatbot used to simplify using services like Sonarr/Radarr/Overseer via the use of chat. Current platform is Discord only.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://kiranshila.github.io/Doplarr/#/configuration){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/doplarr/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

!!! note
      📢 You may also override the default setting of Doplarr working with overseer, to work with Sonarr and Radarr.
      The recommended way to customize these parameters is to use the [inventory](../../saltbox/inventory/index.md). You should edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section.

    ```yaml title="Inventory"
    doplarr_docker_envs_defaults:
      SONARR__URL: # (1)!
      RADARR__URL: # (2)!
      SONARR__API: # (3)!
      RADARR__API: # (4)!
      DISCORD__TOKEN: # (5)!
    ```

    1. This line will set the Sonarr URL. Saltbox defaults to `"http://sonarr:8989"`.
    2. This line will set the Radarr URL. Saltbox defaults to `"http://radarr:7878"`.
    3. This line will set the Sonarr API key. Place your API key here. Wrap it in quotes.
    4. This line will set the Radarr API key. Place your API key here. Wrap it in quotes.
    5. This line will set the Discord token. Place your token here. Wrap it in quotes.

### Create Discord bot

1. Create a new [Application](https://discord.com/developers/applications) in Discord
2. Go to the Bot tab and add a new bot
3. Copy the token and paste it in `/opt/sandbox/settings.yml` in the `doplarr.discord_token` field:

    ```yaml title="/opt/sandbox/settings.yml"
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ```

4. Go to OAuth2 and under "OAuth2 URL Generator", enable `applications.commands` and `bot`
5. Copy the resulting URL and open it in your browser in order to invite your bot to your discord channel.

### Set up overseer parameters

1. In `/opt/sandbox/settings.yml` : set up the overseer url in the corresponding field `doplarr.overseerr_url` according to your setings. If you have not customize saltbox settings, the default url `http://overseerr:5055` should be correct:

    ```yaml title="/opt/sandbox/settings.yml"
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ```

2. In `/opt/sandbox/settings.yml` : set up the overseer API key in the corresponding field `doplarr.overseerr_api` according to your overseer settings.
You can get your api keys in your main setting page in overseer: <https://overseerr.iYOUR_DOMAIN_NAMEi/settings>:

    ```yaml title="/opt/sandbox/settings.yml"
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ```

## Deployment

```shell
sb install sandbox-doplarr
```

## Usage

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        doplarr_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `doplarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `doplarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`doplarr_name`"

        ```yaml
        # Type: string
        doplarr_name: doplarr
        ```

=== "Settings"

    ??? variable string "`doplarr_role_discord_token`"

        ```yaml
        # Type: string
        doplarr_role_discord_token: ""
        ```

    ??? variable string "`doplarr_role_overseerr_url`"

        ```yaml
        # Type: string
        doplarr_role_overseerr_url: ""
        ```

    ??? variable string "`doplarr_role_overseerr_api`"

        ```yaml
        # Type: string
        doplarr_role_overseerr_api: ""
        ```

    ??? variable string "`doplarr_role_radarr_api`"

        ```yaml
        # Type: string
        doplarr_role_radarr_api: ""
        ```

    ??? variable string "`doplarr_role_radarr_url`"

        ```yaml
        # Type: string
        doplarr_role_radarr_url: ""
        ```

    ??? variable string "`doplarr_role_sonarr_api`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_api: ""
        ```

    ??? variable string "`doplarr_role_sonarr_url`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_url: ""
        ```

    ??? variable string "`doplarr_role_discord_max_results`"

        ```yaml
        # Type: string
        doplarr_role_discord_max_results: "25"
        ```

    ??? variable string "`doplarr_role_discord_role_id`"

        ```yaml
        # Type: string
        doplarr_role_discord_role_id: ""
        ```

    ??? variable string "`doplarr_role_discord_requested_msg_style`"

        ```yaml
        # Type: string
        doplarr_role_discord_requested_msg_style: ":plain"
        ```

    ??? variable string "`doplarr_role_sonarr_quality_profile`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_quality_profile: ""
        ```

    ??? variable string "`doplarr_role_radarr_quality_profile`"

        ```yaml
        # Type: string
        doplarr_role_radarr_quality_profile: ""
        ```

    ??? variable string "`doplarr_role_sonarr_language_profile`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_language_profile: ""
        ```

    ??? variable string "`doplarr_role_overseer_default_id`"

        ```yaml
        # Type: string
        doplarr_role_overseer_default_id: ""
        ```

    ??? variable string "`doplarr_role_partial_seasons`"

        ```yaml
        # Type: string
        doplarr_role_partial_seasons: "true"
        ```

    ??? variable string "`doplarr_role_log_level`"

        ```yaml
        # Type: string
        doplarr_role_log_level: ":info"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`doplarr_role_docker_container`"

        ```yaml
        # Type: string
        doplarr_role_docker_container: "{{ doplarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`doplarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_image_pull: true
        ```

    ??? variable string "`doplarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        doplarr_role_docker_image_repo: "lscr.io/linuxserver/doplarr"
        ```

    ??? variable string "`doplarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        doplarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`doplarr_role_docker_image`"

        ```yaml
        # Type: string
        doplarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='doplarr') }}:{{ lookup('role_var', '_docker_image_tag', role='doplarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`doplarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        doplarr_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          DISCORD__TOKEN: "{{ lookup('role_var', '_discord_token', role='doplarr') }}"
          OVERSEERR__URL: "{{ lookup('role_var', '_overseerr_url', role='doplarr') }}"
          OVERSEERR__API: "{{ lookup('role_var', '_overseerr_api', role='doplarr') }}"
          RADARR__API: "{{ lookup('role_var', '_radarr_api', role='doplarr') }}"
          RADARR__URL: "{{ lookup('role_var', '_radarr_url', role='doplarr') }}"
          SONARR__API: "{{ lookup('role_var', '_sonarr_api', role='doplarr') }}"
          SONARR__URL: "{{ lookup('role_var', '_sonarr_url', role='doplarr') }}"
          DISCORD__MAX_RESULTS: "{{ lookup('role_var', '_discord_max_results', role='doplarr') }}"
          DISCORD__ROLE_ID: "{{ lookup('role_var', '_discord_role_id', role='doplarr') }}"
          DISCORD__REQUESTED_MSG_STYLE: "{{ lookup('role_var', '_discord_requested_msg_style', role='doplarr') }}"
          SONARR__QUALITY_PROFILE: "{{ lookup('role_var', '_sonarr_quality_profile', role='doplarr') }}"
          RADARR__QUALITY_PROFILE: "{{ lookup('role_var', '_radarr_quality_profile', role='doplarr') }}"
          SONARR__LANGUAGE_PROFILE: "{{ lookup('role_var', '_sonarr_language_profile', role='doplarr') }}"
          OVERSEERR__DEFAULT_ID: "{{ lookup('role_var', '_overseer_default_id', role='doplarr') }}"
          PARTIAL_SEASONS: "{{ lookup('role_var', '_partial_seasons', role='doplarr') }}"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='doplarr') }}"
        ```

    ??? variable list "`doplarr_role_docker_envs_custom`"

        ```yaml
        # Type: list
        doplarr_role_docker_envs_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`doplarr_role_docker_hostname`"

        ```yaml
        # Type: string
        doplarr_role_docker_hostname: "{{ doplarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`doplarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        doplarr_role_docker_networks_alias: "{{ doplarr_name }}"
        ```

    ??? variable list "`doplarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        doplarr_role_docker_networks_default: []
        ```

    ??? variable list "`doplarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        doplarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`doplarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        doplarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`doplarr_role_docker_state`"

        ```yaml
        # Type: string
        doplarr_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`doplarr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        doplarr_role_docker_blkio_weight:
        ```

    ??? variable int "`doplarr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        doplarr_role_docker_cpu_period:
        ```

    ??? variable int "`doplarr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        doplarr_role_docker_cpu_quota:
        ```

    ??? variable int "`doplarr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        doplarr_role_docker_cpu_shares:
        ```

    ??? variable string "`doplarr_role_docker_cpus`"

        ```yaml
        # Type: string
        doplarr_role_docker_cpus:
        ```

    ??? variable string "`doplarr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        doplarr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`doplarr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        doplarr_role_docker_cpuset_mems:
        ```

    ??? variable string "`doplarr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        doplarr_role_docker_kernel_memory:
        ```

    ??? variable string "`doplarr_role_docker_memory`"

        ```yaml
        # Type: string
        doplarr_role_docker_memory:
        ```

    ??? variable string "`doplarr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        doplarr_role_docker_memory_reservation:
        ```

    ??? variable string "`doplarr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        doplarr_role_docker_memory_swap:
        ```

    ??? variable int "`doplarr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        doplarr_role_docker_memory_swappiness:
        ```

    ??? variable string "`doplarr_role_docker_shm_size`"

        ```yaml
        # Type: string
        doplarr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`doplarr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        doplarr_role_docker_cap_drop:
        ```

    ??? variable string "`doplarr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        doplarr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`doplarr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        doplarr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`doplarr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        doplarr_role_docker_device_read_bps:
        ```

    ??? variable list "`doplarr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        doplarr_role_docker_device_read_iops:
        ```

    ??? variable list "`doplarr_role_docker_device_requests`"

        ```yaml
        # Type: list
        doplarr_role_docker_device_requests:
        ```

    ??? variable list "`doplarr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        doplarr_role_docker_device_write_bps:
        ```

    ??? variable list "`doplarr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        doplarr_role_docker_device_write_iops:
        ```

    ??? variable list "`doplarr_role_docker_devices`"

        ```yaml
        # Type: list
        doplarr_role_docker_devices:
        ```

    ??? variable string "`doplarr_role_docker_devices_default`"

        ```yaml
        # Type: string
        doplarr_role_docker_devices_default:
        ```

    ??? variable list "`doplarr_role_docker_groups`"

        ```yaml
        # Type: list
        doplarr_role_docker_groups:
        ```

    ??? variable bool "`doplarr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_privileged:
        ```

    ??? variable list "`doplarr_role_docker_security_opts`"

        ```yaml
        # Type: list
        doplarr_role_docker_security_opts:
        ```

    ??? variable string "`doplarr_role_docker_user`"

        ```yaml
        # Type: string
        doplarr_role_docker_user:
        ```

    ??? variable string "`doplarr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        doplarr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`doplarr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        doplarr_role_docker_dns_opts:
        ```

    ??? variable list "`doplarr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        doplarr_role_docker_dns_search_domains:
        ```

    ??? variable list "`doplarr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        doplarr_role_docker_dns_servers:
        ```

    ??? variable string "`doplarr_role_docker_domainname`"

        ```yaml
        # Type: string
        doplarr_role_docker_domainname:
        ```

    ??? variable list "`doplarr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        doplarr_role_docker_exposed_ports:
        ```

    ??? variable dict "`doplarr_role_docker_hosts`"

        ```yaml
        # Type: dict
        doplarr_role_docker_hosts:
        ```

    ??? variable bool "`doplarr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_hosts_use_common:
        ```

    ??? variable string "`doplarr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        doplarr_role_docker_ipc_mode:
        ```

    ??? variable list "`doplarr_role_docker_links`"

        ```yaml
        # Type: list
        doplarr_role_docker_links:
        ```

    ??? variable string "`doplarr_role_docker_network_mode`"

        ```yaml
        # Type: string
        doplarr_role_docker_network_mode:
        ```

    ??? variable string "`doplarr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        doplarr_role_docker_pid_mode:
        ```

    ??? variable list "`doplarr_role_docker_ports`"

        ```yaml
        # Type: list
        doplarr_role_docker_ports:
        ```

    ??? variable string "`doplarr_role_docker_uts`"

        ```yaml
        # Type: string
        doplarr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`doplarr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_keep_volumes:
        ```

    ??? variable list "`doplarr_role_docker_mounts`"

        ```yaml
        # Type: list
        doplarr_role_docker_mounts:
        ```

    ??? variable dict "`doplarr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        doplarr_role_docker_storage_opts:
        ```

    ??? variable list "`doplarr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        doplarr_role_docker_tmpfs:
        ```

    ??? variable string "`doplarr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        doplarr_role_docker_volume_driver:
        ```

    ??? variable list "`doplarr_role_docker_volumes`"

        ```yaml
        # Type: list
        doplarr_role_docker_volumes:
        ```

    ??? variable list "`doplarr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        doplarr_role_docker_volumes_from:
        ```

    ??? variable bool "`doplarr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_volumes_global:
        ```

    ??? variable string "`doplarr_role_docker_working_dir`"

        ```yaml
        # Type: string
        doplarr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`doplarr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_auto_remove:
        ```

    ??? variable bool "`doplarr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_cleanup:
        ```

    ??? variable string "`doplarr_role_docker_force_kill`"

        ```yaml
        # Type: string
        doplarr_role_docker_force_kill:
        ```

    ??? variable dict "`doplarr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        doplarr_role_docker_healthcheck:
        ```

    ??? variable int "`doplarr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        doplarr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`doplarr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_init:
        ```

    ??? variable string "`doplarr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        doplarr_role_docker_kill_signal:
        ```

    ??? variable string "`doplarr_role_docker_log_driver`"

        ```yaml
        # Type: string
        doplarr_role_docker_log_driver:
        ```

    ??? variable dict "`doplarr_role_docker_log_options`"

        ```yaml
        # Type: dict
        doplarr_role_docker_log_options:
        ```

    ??? variable bool "`doplarr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_oom_killer:
        ```

    ??? variable int "`doplarr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        doplarr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`doplarr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_output_logs:
        ```

    ??? variable bool "`doplarr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_paused:
        ```

    ??? variable bool "`doplarr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_recreate:
        ```

    ??? variable int "`doplarr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        doplarr_role_docker_restart_retries:
        ```

    ??? variable int "`doplarr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        doplarr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`doplarr_role_docker_capabilities`"

        ```yaml
        # Type: list
        doplarr_role_docker_capabilities:
        ```

    ??? variable string "`doplarr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        doplarr_role_docker_cgroup_parent:
        ```

    ??? variable list "`doplarr_role_docker_commands`"

        ```yaml
        # Type: list
        doplarr_role_docker_commands:
        ```

    ??? variable int "`doplarr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        doplarr_role_docker_create_timeout:
        ```

    ??? variable string "`doplarr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        doplarr_role_docker_entrypoint:
        ```

    ??? variable string "`doplarr_role_docker_env_file`"

        ```yaml
        # Type: string
        doplarr_role_docker_env_file:
        ```

    ??? variable dict "`doplarr_role_docker_labels`"

        ```yaml
        # Type: dict
        doplarr_role_docker_labels:
        ```

    ??? variable bool "`doplarr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_labels_use_common:
        ```

    ??? variable bool "`doplarr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_read_only:
        ```

    ??? variable string "`doplarr_role_docker_runtime`"

        ```yaml
        # Type: string
        doplarr_role_docker_runtime:
        ```

    ??? variable list "`doplarr_role_docker_sysctls`"

        ```yaml
        # Type: list
        doplarr_role_docker_sysctls:
        ```

    ??? variable list "`doplarr_role_docker_ulimits`"

        ```yaml
        # Type: list
        doplarr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`doplarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        doplarr_role_autoheal_enabled: true
        ```

    ??? variable string "`doplarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        doplarr_role_depends_on: ""
        ```

    ??? variable string "`doplarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        doplarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`doplarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        doplarr_role_depends_on_healthchecks:
        ```

    ??? variable string "`doplarr_role_discord_max_results`"

        ```yaml
        # Type: string
        doplarr_role_discord_max_results:
        ```

    ??? variable string "`doplarr_role_discord_requested_msg_style`"

        ```yaml
        # Type: string
        doplarr_role_discord_requested_msg_style:
        ```

    ??? variable string "`doplarr_role_discord_role_id`"

        ```yaml
        # Type: string
        doplarr_role_discord_role_id:
        ```

    ??? variable string "`doplarr_role_discord_token`"

        ```yaml
        # Type: string
        doplarr_role_discord_token:
        ```

    ??? variable bool "`doplarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        doplarr_role_diun_enabled: true
        ```

    ??? variable bool "`doplarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        doplarr_role_docker_controller: true
        ```

    ??? variable string "`doplarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        doplarr_role_docker_image_repo:
        ```

    ??? variable string "`doplarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        doplarr_role_docker_image_tag:
        ```

    ??? variable bool "`doplarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        doplarr_role_docker_volumes_download:
        ```

    ??? variable string "`doplarr_role_log_level`"

        ```yaml
        # Type: string
        doplarr_role_log_level:
        ```

    ??? variable string "`doplarr_role_overseer_default_id`"

        ```yaml
        # Type: string
        doplarr_role_overseer_default_id:
        ```

    ??? variable string "`doplarr_role_overseerr_api`"

        ```yaml
        # Type: string
        doplarr_role_overseerr_api:
        ```

    ??? variable string "`doplarr_role_overseerr_url`"

        ```yaml
        # Type: string
        doplarr_role_overseerr_url:
        ```

    ??? variable string "`doplarr_role_partial_seasons`"

        ```yaml
        # Type: string
        doplarr_role_partial_seasons:
        ```

    ??? variable string "`doplarr_role_radarr_api`"

        ```yaml
        # Type: string
        doplarr_role_radarr_api:
        ```

    ??? variable string "`doplarr_role_radarr_quality_profile`"

        ```yaml
        # Type: string
        doplarr_role_radarr_quality_profile:
        ```

    ??? variable string "`doplarr_role_radarr_url`"

        ```yaml
        # Type: string
        doplarr_role_radarr_url:
        ```

    ??? variable string "`doplarr_role_sonarr_api`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_api:
        ```

    ??? variable string "`doplarr_role_sonarr_language_profile`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_language_profile:
        ```

    ??? variable string "`doplarr_role_sonarr_quality_profile`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_quality_profile:
        ```

    ??? variable string "`doplarr_role_sonarr_url`"

        ```yaml
        # Type: string
        doplarr_role_sonarr_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
