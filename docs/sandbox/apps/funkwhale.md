---
icon: material/docker
hide:
  - tags
tags:
  - funkwhale
  - media
  - music
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.funkwhale.audio
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/funkwhale/all-in-one/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Funkwhale
    summary: |-
      a modern, self-hosted, free and open-source music server.
    link: https://funkwhale.audio/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Funkwhale

## Overview

[Funkwhale](https://funkwhale.audio/) is a modern, self-hosted, free and open-source music server.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.funkwhale.audio){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/funkwhale/all-in-one/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-funkwhale
```

## Usage

Visit <https://funkwhale.iYOUR_DOMAIN_NAMEi>.

## Basics

- First create the superuser

- `docker exec -it funkwhale manage createsuperuser` <br />
   (for ease of access, set it as your Saltbox user and password.)
- enter the `exit` command when finished to return to your server's shell.

- Now configure these settings via the web GUI

- Access Funkwhale, visit <https://funkwhale.iYOUR_DOMAIN_NAMEi> and log in with the user and password you just created.
- Enter `Music->Add Content->Create a new Library` and fill out the information.
- Enter your new Library and Details. There will be a sharing link such as:
  `https://funkwhale.domain.com/federation/music/libraries/da8bd97b-3c3f-4e7b-92cb-6ba45721837b`
- Copy out the last portion: `da8bd97b-3c3f-4e7b-92cb-6ba45721837b`

- Return to the shell session to import music library

- `docker exec -it funkwhale /usr/bin/python3 /app/api/manage.py import_files da8bd97b-3c3f-4e7b-92cb-6ba45721837b "/music/Media/Audio/Music/**/**/*.flac" --in-place --async --recursive`

The above line explained:

- `docker exec -it funkwhale /usr/bin/python3 /app/api/manage.py import_files` tells funkwhale to import music.
- `da8bd97b-3c3f-4e7b-92cb-6ba45721837b` is your library id
- `"/music/Media/Audio/Music/**/**/*.flac"` is the path to your media.
- `--in-place` means do not copy the media into Funkwhale and leave it where it is.
- `--async` means it will import the music first and then pull the metadata`
- `--recursive` will recursively scan the folders

If everything goes as planned you'll get prompted like this:

```shell
> Checking imported paths against settings.MUSIC_DIRECTORY_PATH
> Import summary:
> - 149828 files found matching this pattern: ['/music/Media/Audio/Music/**/**/*.flac']

> - 0 files already found in database
> - 149828 new files
> Selected options: in place
> Are you sure you want to do this?
> Type 'yes' to continue, or 'no' to cancel:
```

- Answer yes at the prompt and the import will begin.

!!! info
    Useful URLs <br />
    Libraries URL: `https://funkwhale.domain.com/content/libraries/` <br />
    Admin Account Edit Page: `https://funkwhale.domain.com/api/admin/users/user/1/change/` <br />

!!! info
    If you want to use subsonic clients then you'll need to set a password here:  <br />
    `https://funkwhale.domain.com/settings`
    (subsonic protocol requires storing password in cleartext, so to avoid compromising your Funkwhale account, we use a different password).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        funkwhale_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `funkwhale_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `funkwhale_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`funkwhale_name`"

        ```yaml
        # Type: string
        funkwhale_name: funkwhale
        ```

=== "Web"

    ??? variable string "`funkwhale_role_web_subdomain`"

        ```yaml
        # Type: string
        funkwhale_role_web_subdomain: "{{ funkwhale_name }}"
        ```

    ??? variable string "`funkwhale_role_web_domain`"

        ```yaml
        # Type: string
        funkwhale_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`funkwhale_role_web_port`"

        ```yaml
        # Type: string
        funkwhale_role_web_port: "80"
        ```

    ??? variable string "`funkwhale_role_web_url`"

        ```yaml
        # Type: string
        funkwhale_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='funkwhale') + '.' + lookup('role_var', '_web_domain', role='funkwhale')
                                 if (lookup('role_var', '_web_subdomain', role='funkwhale') | length > 0)
                                 else lookup('role_var', '_web_domain', role='funkwhale')) }}"
        ```

=== "DNS"

    ??? variable string "`funkwhale_role_dns_record`"

        ```yaml
        # Type: string
        funkwhale_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='funkwhale') }}"
        ```

    ??? variable string "`funkwhale_role_dns_zone`"

        ```yaml
        # Type: string
        funkwhale_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='funkwhale') }}"
        ```

    ??? variable bool "`funkwhale_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`funkwhale_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`funkwhale_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`funkwhale_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`funkwhale_role_traefik_certresolver`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`funkwhale_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_enabled: true
        ```

    ??? variable bool "`funkwhale_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_api_enabled: false
        ```

    ??? variable string "`funkwhale_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`funkwhale_role_docker_container`"

        ```yaml
        # Type: string
        funkwhale_role_docker_container: "{{ funkwhale_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`funkwhale_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_image_pull: true
        ```

    ??? variable string "`funkwhale_role_docker_image_repo`"

        ```yaml
        # Type: string
        funkwhale_role_docker_image_repo: "funkwhale/all-in-one"
        ```

    ??? variable string "`funkwhale_role_docker_image_tag`"

        ```yaml
        # Type: string
        funkwhale_role_docker_image_tag: "latest"
        ```

    ??? variable string "`funkwhale_role_docker_image`"

        ```yaml
        # Type: string
        funkwhale_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='funkwhale') }}:{{ lookup('role_var', '_docker_image_tag', role='funkwhale') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`funkwhale_role_docker_envs_default`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_envs_default:
          FUNKWHALE_HOSTNAME: "{{ lookup('role_var', '_web_subdomain', role='funkwhale') + '.' + lookup('role_var', '_web_domain', role='funkwhale') }}"
          NESTED_PROXY: "1"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`funkwhale_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`funkwhale_role_docker_volumes_default`"

        ```yaml
        # Type: list
        funkwhale_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='funkwhale') }}/data:/data"
          - "/mnt/unionfs:/music:ro"
        ```

    ??? variable list "`funkwhale_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        funkwhale_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`funkwhale_role_docker_hostname`"

        ```yaml
        # Type: string
        funkwhale_role_docker_hostname: "{{ funkwhale_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`funkwhale_role_docker_networks_alias`"

        ```yaml
        # Type: string
        funkwhale_role_docker_networks_alias: "{{ funkwhale_name }}"
        ```

    ??? variable list "`funkwhale_role_docker_networks_default`"

        ```yaml
        # Type: list
        funkwhale_role_docker_networks_default: []
        ```

    ??? variable list "`funkwhale_role_docker_networks_custom`"

        ```yaml
        # Type: list
        funkwhale_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`funkwhale_role_docker_restart_policy`"

        ```yaml
        # Type: string
        funkwhale_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`funkwhale_role_docker_state`"

        ```yaml
        # Type: string
        funkwhale_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`funkwhale_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        funkwhale_role_docker_blkio_weight:
        ```

    ??? variable int "`funkwhale_role_docker_cpu_period`"

        ```yaml
        # Type: int
        funkwhale_role_docker_cpu_period:
        ```

    ??? variable int "`funkwhale_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        funkwhale_role_docker_cpu_quota:
        ```

    ??? variable int "`funkwhale_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        funkwhale_role_docker_cpu_shares:
        ```

    ??? variable string "`funkwhale_role_docker_cpus`"

        ```yaml
        # Type: string
        funkwhale_role_docker_cpus:
        ```

    ??? variable string "`funkwhale_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        funkwhale_role_docker_cpuset_cpus:
        ```

    ??? variable string "`funkwhale_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        funkwhale_role_docker_cpuset_mems:
        ```

    ??? variable string "`funkwhale_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        funkwhale_role_docker_kernel_memory:
        ```

    ??? variable string "`funkwhale_role_docker_memory`"

        ```yaml
        # Type: string
        funkwhale_role_docker_memory:
        ```

    ??? variable string "`funkwhale_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        funkwhale_role_docker_memory_reservation:
        ```

    ??? variable string "`funkwhale_role_docker_memory_swap`"

        ```yaml
        # Type: string
        funkwhale_role_docker_memory_swap:
        ```

    ??? variable int "`funkwhale_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        funkwhale_role_docker_memory_swappiness:
        ```

    ??? variable string "`funkwhale_role_docker_shm_size`"

        ```yaml
        # Type: string
        funkwhale_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`funkwhale_role_docker_cap_drop`"

        ```yaml
        # Type: list
        funkwhale_role_docker_cap_drop:
        ```

    ??? variable string "`funkwhale_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        funkwhale_role_docker_cgroupns_mode:
        ```

    ??? variable list "`funkwhale_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        funkwhale_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`funkwhale_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        funkwhale_role_docker_device_read_bps:
        ```

    ??? variable list "`funkwhale_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        funkwhale_role_docker_device_read_iops:
        ```

    ??? variable list "`funkwhale_role_docker_device_requests`"

        ```yaml
        # Type: list
        funkwhale_role_docker_device_requests:
        ```

    ??? variable list "`funkwhale_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        funkwhale_role_docker_device_write_bps:
        ```

    ??? variable list "`funkwhale_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        funkwhale_role_docker_device_write_iops:
        ```

    ??? variable list "`funkwhale_role_docker_devices`"

        ```yaml
        # Type: list
        funkwhale_role_docker_devices:
        ```

    ??? variable string "`funkwhale_role_docker_devices_default`"

        ```yaml
        # Type: string
        funkwhale_role_docker_devices_default:
        ```

    ??? variable list "`funkwhale_role_docker_groups`"

        ```yaml
        # Type: list
        funkwhale_role_docker_groups:
        ```

    ??? variable bool "`funkwhale_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_privileged:
        ```

    ??? variable list "`funkwhale_role_docker_security_opts`"

        ```yaml
        # Type: list
        funkwhale_role_docker_security_opts:
        ```

    ??? variable string "`funkwhale_role_docker_user`"

        ```yaml
        # Type: string
        funkwhale_role_docker_user:
        ```

    ??? variable string "`funkwhale_role_docker_userns_mode`"

        ```yaml
        # Type: string
        funkwhale_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`funkwhale_role_docker_dns_opts`"

        ```yaml
        # Type: list
        funkwhale_role_docker_dns_opts:
        ```

    ??? variable list "`funkwhale_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        funkwhale_role_docker_dns_search_domains:
        ```

    ??? variable list "`funkwhale_role_docker_dns_servers`"

        ```yaml
        # Type: list
        funkwhale_role_docker_dns_servers:
        ```

    ??? variable string "`funkwhale_role_docker_domainname`"

        ```yaml
        # Type: string
        funkwhale_role_docker_domainname:
        ```

    ??? variable list "`funkwhale_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        funkwhale_role_docker_exposed_ports:
        ```

    ??? variable dict "`funkwhale_role_docker_hosts`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_hosts:
        ```

    ??? variable bool "`funkwhale_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_hosts_use_common:
        ```

    ??? variable string "`funkwhale_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        funkwhale_role_docker_ipc_mode:
        ```

    ??? variable list "`funkwhale_role_docker_links`"

        ```yaml
        # Type: list
        funkwhale_role_docker_links:
        ```

    ??? variable string "`funkwhale_role_docker_network_mode`"

        ```yaml
        # Type: string
        funkwhale_role_docker_network_mode:
        ```

    ??? variable string "`funkwhale_role_docker_pid_mode`"

        ```yaml
        # Type: string
        funkwhale_role_docker_pid_mode:
        ```

    ??? variable list "`funkwhale_role_docker_ports`"

        ```yaml
        # Type: list
        funkwhale_role_docker_ports:
        ```

    ??? variable string "`funkwhale_role_docker_uts`"

        ```yaml
        # Type: string
        funkwhale_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`funkwhale_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_keep_volumes:
        ```

    ??? variable list "`funkwhale_role_docker_mounts`"

        ```yaml
        # Type: list
        funkwhale_role_docker_mounts:
        ```

    ??? variable dict "`funkwhale_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_storage_opts:
        ```

    ??? variable list "`funkwhale_role_docker_tmpfs`"

        ```yaml
        # Type: list
        funkwhale_role_docker_tmpfs:
        ```

    ??? variable string "`funkwhale_role_docker_volume_driver`"

        ```yaml
        # Type: string
        funkwhale_role_docker_volume_driver:
        ```

    ??? variable list "`funkwhale_role_docker_volumes_from`"

        ```yaml
        # Type: list
        funkwhale_role_docker_volumes_from:
        ```

    ??? variable bool "`funkwhale_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_volumes_global:
        ```

    ??? variable string "`funkwhale_role_docker_working_dir`"

        ```yaml
        # Type: string
        funkwhale_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`funkwhale_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_auto_remove:
        ```

    ??? variable bool "`funkwhale_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_cleanup:
        ```

    ??? variable string "`funkwhale_role_docker_force_kill`"

        ```yaml
        # Type: string
        funkwhale_role_docker_force_kill:
        ```

    ??? variable dict "`funkwhale_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_healthcheck:
        ```

    ??? variable int "`funkwhale_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        funkwhale_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`funkwhale_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_init:
        ```

    ??? variable string "`funkwhale_role_docker_kill_signal`"

        ```yaml
        # Type: string
        funkwhale_role_docker_kill_signal:
        ```

    ??? variable string "`funkwhale_role_docker_log_driver`"

        ```yaml
        # Type: string
        funkwhale_role_docker_log_driver:
        ```

    ??? variable dict "`funkwhale_role_docker_log_options`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_log_options:
        ```

    ??? variable bool "`funkwhale_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_oom_killer:
        ```

    ??? variable int "`funkwhale_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        funkwhale_role_docker_oom_score_adj:
        ```

    ??? variable bool "`funkwhale_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_output_logs:
        ```

    ??? variable bool "`funkwhale_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_paused:
        ```

    ??? variable bool "`funkwhale_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_recreate:
        ```

    ??? variable int "`funkwhale_role_docker_restart_retries`"

        ```yaml
        # Type: int
        funkwhale_role_docker_restart_retries:
        ```

    ??? variable int "`funkwhale_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        funkwhale_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`funkwhale_role_docker_capabilities`"

        ```yaml
        # Type: list
        funkwhale_role_docker_capabilities:
        ```

    ??? variable string "`funkwhale_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        funkwhale_role_docker_cgroup_parent:
        ```

    ??? variable list "`funkwhale_role_docker_commands`"

        ```yaml
        # Type: list
        funkwhale_role_docker_commands:
        ```

    ??? variable int "`funkwhale_role_docker_create_timeout`"

        ```yaml
        # Type: int
        funkwhale_role_docker_create_timeout:
        ```

    ??? variable string "`funkwhale_role_docker_entrypoint`"

        ```yaml
        # Type: string
        funkwhale_role_docker_entrypoint:
        ```

    ??? variable string "`funkwhale_role_docker_env_file`"

        ```yaml
        # Type: string
        funkwhale_role_docker_env_file:
        ```

    ??? variable dict "`funkwhale_role_docker_labels`"

        ```yaml
        # Type: dict
        funkwhale_role_docker_labels:
        ```

    ??? variable bool "`funkwhale_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_labels_use_common:
        ```

    ??? variable bool "`funkwhale_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_read_only:
        ```

    ??? variable string "`funkwhale_role_docker_runtime`"

        ```yaml
        # Type: string
        funkwhale_role_docker_runtime:
        ```

    ??? variable list "`funkwhale_role_docker_sysctls`"

        ```yaml
        # Type: list
        funkwhale_role_docker_sysctls:
        ```

    ??? variable list "`funkwhale_role_docker_ulimits`"

        ```yaml
        # Type: list
        funkwhale_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`funkwhale_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        funkwhale_role_autoheal_enabled: true
        ```

    ??? variable string "`funkwhale_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        funkwhale_role_depends_on: ""
        ```

    ??? variable string "`funkwhale_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        funkwhale_role_depends_on_delay: "0"
        ```

    ??? variable string "`funkwhale_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        funkwhale_role_depends_on_healthchecks:
        ```

    ??? variable bool "`funkwhale_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        funkwhale_role_diun_enabled: true
        ```

    ??? variable bool "`funkwhale_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        funkwhale_role_dns_enabled: true
        ```

    ??? variable bool "`funkwhale_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        funkwhale_role_docker_controller: true
        ```

    ??? variable list "`funkwhale_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        funkwhale_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`funkwhale_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_docker_volumes_download:
        ```

    ??? variable string "`funkwhale_role_themepark_addons`"

        ```yaml
        # Type: string
        funkwhale_role_themepark_addons:
        ```

    ??? variable string "`funkwhale_role_themepark_app`"

        ```yaml
        # Type: string
        funkwhale_role_themepark_app:
        ```

    ??? variable string "`funkwhale_role_themepark_theme`"

        ```yaml
        # Type: string
        funkwhale_role_themepark_theme:
        ```

    ??? variable string "`funkwhale_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_api_middleware:
        ```

    ??? variable string "`funkwhale_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`funkwhale_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`funkwhale_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_middleware_http:
        ```

    ??? variable bool "`funkwhale_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`funkwhale_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        funkwhale_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`funkwhale_role_traefik_priority`"

        ```yaml
        # Type: string
        funkwhale_role_traefik_priority:
        ```

    ??? variable bool "`funkwhale_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`funkwhale_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`funkwhale_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        funkwhale_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`funkwhale_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        funkwhale_role_web_api_http_port:
        ```

    ??? variable string "`funkwhale_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        funkwhale_role_web_api_http_scheme:
        ```

    ??? variable dict "`funkwhale_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        funkwhale_role_web_api_http_serverstransport:
        ```

    ??? variable string "`funkwhale_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        funkwhale_role_web_api_port:
        ```

    ??? variable string "`funkwhale_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        funkwhale_role_web_api_scheme:
        ```

    ??? variable dict "`funkwhale_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        funkwhale_role_web_api_serverstransport:
        ```

    ??? variable list "`funkwhale_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        funkwhale_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            funkwhale_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "funkwhale2.{{ user.domain }}"
              - "funkwhale.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`funkwhale_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        funkwhale_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            funkwhale_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'funkwhale2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`funkwhale_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        funkwhale_role_web_http_port:
        ```

    ??? variable string "`funkwhale_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        funkwhale_role_web_http_scheme:
        ```

    ??? variable dict "`funkwhale_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        funkwhale_role_web_http_serverstransport:
        ```

    ??? variable string "`funkwhale_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        funkwhale_role_web_scheme:
        ```

    ??? variable dict "`funkwhale_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        funkwhale_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
