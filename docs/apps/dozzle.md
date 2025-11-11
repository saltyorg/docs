---
icon: material/docker
hide:
  - tags
tags:
  - dozzle
---

# Dozzle

## Overview

[Dozzle](https://dozzle.dev/) is a small lightweight application with a web based interface to monitor Docker logs. It doesn’t store any log files. It is for live monitoring of your container logs only. Dozzle can only access logs written to stdout or stderr which is the same functionality as the `docker logs` command. See below for more info on that.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://dozzle.dev/){: .header-icons } | [:octicons-link-16: Docs](https://dozzle.dev/guide/what-is-dozzle){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/amir20/dozzle){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/amir20/dozzle){: .header-icons }|

### 1. Installation

``` shell

sb install dozzle

```

### 2. URL

- To access Dozzle, visit <https://dozzle.iYOUR_DOMAIN_NAMEi>

### 3. Setup

To view log files that are NOT written to stdout or stderr, use the following to setup a basic Alpine Linux container via Docker Compose that just tails a mounted log file (in this case, Cloudplow) which then exposes it to Dozzle. Adjust as needed for your circumstances.

``` yaml
  tail-cloudplow: # (1)!
    container_name: tail-cloudplow # (2)!
    image: alpine
    volumes:
      - /opt/cloudplow/cloudplow.log:/opt/cloudplow/cloudplow.log:ro # (3)!
    command:
      - tail
      - -F
      - /opt/cloudplow/cloudplow.log # (4)!
    network_mode: none
    restart: unless-stopped
    user: 1000:1000 # (5)!
```

1. You can pick any name for the container, but it is recommended to pick a memorable name that you will recognize in the Dozzle menu.
2. You can pick any name for the container, but it is recommended to pick a memorable name that you will recognize in the Dozzle menu.
3. The volume mount for the log file. This takes the format of `/host/path/to.log:/container/path/to.log:ro`. The `:ro` suffix is optional but recommended to give this container only read-only access to the log file.
4. The path inside of the container where the log file is accessible. This must be the same in the `volumes` section above and this `command` section. Matching the annotation example, this would be `/container/path/to.log`.
5. Provide your `uid:gid` if they are different. You can check these values by running the `id` command.

???+ note
    To get the container running, follow our docs on starting a docker container here; [Your Own Containers](../advanced/your-own-containers.md#docker-compose).

### 4. Adding Additional Hosts

You can add additional hosts to Dozzle using the `dozzle_additional_hosts` inventory variable. This will append the additional host(s) to the default entry. You can review the upstream documentation [here](https://dozzle.dev/guide/remote-hosts) for the proper syntax. The initiai `,` will be added after the default entry, you must comma separate the hosts if you are adding multiple entries such as:

```yaml
dozzle_additional_hosts: "tcp://otherserver:2375|otherserver,tcp://thirdserver:2375|thirdserver"
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    dozzle_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `dozzle_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `dozzle_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`dozzle_name`"

        ```yaml
        # Type: string
        dozzle_name: dozzle
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`dozzle_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        dozzle_docker_socket_proxy_envs: 
          CONTAINERS: "1"
          INFO: "1"
        ```

=== "Settings"

    ??? variable string "`dozzle_role_additional_hosts`"

        ```yaml
        # Type: string
        dozzle_role_additional_hosts: ""
        ```

    ??? variable string "`dozzle_role_agent_hosts`"

        ```yaml
        # Type: string
        dozzle_role_agent_hosts: ""
        ```

    ??? variable bool "`dozzle_role_agent_mode`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_agent_mode: false
        ```

=== "Paths"

    ??? variable string "`dozzle_role_paths_folder`"

        ```yaml
        # Type: string
        dozzle_role_paths_folder: "{{ dozzle_name }}"
        ```

    ??? variable string "`dozzle_role_paths_location`"

        ```yaml
        # Type: string
        dozzle_role_paths_location: "{{ server_appdata_path }}/{{ dozzle_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`dozzle_role_web_subdomain`"

        ```yaml
        # Type: string
        dozzle_role_web_subdomain: "{{ dozzle_name }}"
        ```

    ??? variable string "`dozzle_role_web_domain`"

        ```yaml
        # Type: string
        dozzle_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`dozzle_role_web_port`"

        ```yaml
        # Type: string
        dozzle_role_web_port: "8080"
        ```

    ??? variable string "`dozzle_role_web_url`"

        ```yaml
        # Type: string
        dozzle_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='dozzle') + '.' + lookup('role_var', '_web_domain', role='dozzle')
                              if (lookup('role_var', '_web_subdomain', role='dozzle') | length > 0)
                              else lookup('role_var', '_web_domain', role='dozzle')) }}"
        ```

=== "DNS"

    ??? variable string "`dozzle_role_dns_record`"

        ```yaml
        # Type: string
        dozzle_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dozzle') }}"
        ```

    ??? variable string "`dozzle_role_dns_zone`"

        ```yaml
        # Type: string
        dozzle_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dozzle') }}"
        ```

    ??? variable bool "`dozzle_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`dozzle_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        dozzle_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`dozzle_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        dozzle_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',dropsecurityheaders@file,themepark-' + dozzle_name
                                                      if (lookup('role_var', '_themepark_enabled', role='dozzle') and global_themepark_plugin_enabled)
                                                      else '') }}"
        ```

    ??? variable string "`dozzle_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        dozzle_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`dozzle_role_traefik_certresolver`"

        ```yaml
        # Type: string
        dozzle_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`dozzle_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_traefik_enabled: true
        ```

    ??? variable bool "`dozzle_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_traefik_api_enabled: false
        ```

    ??? variable string "`dozzle_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        dozzle_role_traefik_api_endpoint: ""
        ```

=== "Theme"

    ??? variable bool "`dozzle_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        dozzle_role_themepark_enabled: false
        ```

    ??? variable string "`dozzle_role_themepark_app`"

        ```yaml
        # Type: string
        dozzle_role_themepark_app: "dozzle"
        ```

    ??? variable string "`dozzle_role_themepark_theme`"

        ```yaml
        # Type: string
        dozzle_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`dozzle_role_themepark_domain`"

        ```yaml
        # Type: string
        dozzle_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`dozzle_role_themepark_addons`"

        ```yaml
        # Type: list
        dozzle_role_themepark_addons: []
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`dozzle_role_docker_container`"

        ```yaml
        # Type: string
        dozzle_role_docker_container: "{{ dozzle_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`dozzle_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_image_pull: true
        ```

    ??? variable string "`dozzle_role_docker_image_repo`"

        ```yaml
        # Type: string
        dozzle_role_docker_image_repo: "amir20/dozzle"
        ```

    ??? variable string "`dozzle_role_docker_image_tag`"

        ```yaml
        # Type: string
        dozzle_role_docker_image_tag: "latest"
        ```

    ??? variable string "`dozzle_role_docker_image`"

        ```yaml
        # Type: string
        dozzle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dozzle') }}:{{ lookup('role_var', '_docker_image_tag', role='dozzle') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`dozzle_role_docker_envs_default`"

        ```yaml
        # Type: dict
        dozzle_role_docker_envs_default: 
          DOZZLE_AUTH_PROVIDER: "{{ 'forward-proxy' if (lookup('role_var', '_traefik_sso_middleware', role='dozzle') | length > 0) else omit }}"
          DOZZLE_REMOTE_AGENT: "{{ lookup('role_var', '_agent_hosts', role='dozzle') if (lookup('role_var', '_additional_hosts', role='dozzle') | length > 0) else omit }}"
          DOZZLE_REMOTE_HOST: "{{ 'tcp://' + dozzle_name + '-docker-socket-proxy:2375|' + traefik_host + ',' + lookup('role_var', '_additional_hosts', role='dozzle')
                               if (lookup('role_var', '_additional_hosts', role='dozzle') | length > 0)
                               else 'tcp://' + dozzle_name + '-docker-socket-proxy:2375|' + traefik_host }}"
          DOZZLE_AUTH_HEADER_USER: "{{ 'X-authentik-username' if 'authentik' in lookup('role_var', '_traefik_sso_middleware', role='dozzle') else omit }}"
          DOZZLE_AUTH_HEADER_EMAIL: "{{ 'X-authentik-email' if 'authentik' in lookup('role_var', '_traefik_sso_middleware', role='dozzle') else omit }}"
          DOZZLE_AUTH_HEADER_NAME: "{{ 'X-authentik-name' if 'authentik' in lookup('role_var', '_traefik_sso_middleware', role='dozzle') else omit }}"
        ```

    ??? variable dict "`dozzle_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        dozzle_role_docker_envs_custom: {}
        ```

    <h5>Commands</h5>

    ??? variable string "`dozzle_role_docker_commands_agent`"

        ```yaml
        # Type: string
        dozzle_role_docker_commands_agent: "agent"
        ```

    ??? variable list "`dozzle_role_docker_commands_default`"

        ```yaml
        # Type: list
        dozzle_role_docker_commands_default: []
        ```

    ??? variable list "`dozzle_role_docker_commands_custom`"

        ```yaml
        # Type: list
        dozzle_role_docker_commands_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`dozzle_role_docker_labels_default`"

        ```yaml
        # Type: dict
        dozzle_role_docker_labels_default: {}
        ```

    ??? variable dict "`dozzle_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        dozzle_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`dozzle_role_docker_hostname`"

        ```yaml
        # Type: string
        dozzle_role_docker_hostname: "{{ dozzle_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`dozzle_role_docker_networks_alias`"

        ```yaml
        # Type: string
        dozzle_role_docker_networks_alias: "{{ dozzle_name }}"
        ```

    ??? variable list "`dozzle_role_docker_networks_default`"

        ```yaml
        # Type: list
        dozzle_role_docker_networks_default: []
        ```

    ??? variable list "`dozzle_role_docker_networks_custom`"

        ```yaml
        # Type: list
        dozzle_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`dozzle_role_docker_restart_policy`"

        ```yaml
        # Type: string
        dozzle_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`dozzle_role_docker_state`"

        ```yaml
        # Type: string
        dozzle_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`dozzle_role_depends_on`"

        ```yaml
        # Type: string
        dozzle_role_depends_on: "{{ dozzle_name }}-docker-socket-proxy"
        ```

    ??? variable string "`dozzle_role_depends_on_delay`"

        ```yaml
        # Type: string
        dozzle_role_depends_on_delay: "0"
        ```

    ??? variable string "`dozzle_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        dozzle_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`dozzle_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        dozzle_role_docker_blkio_weight:
        ```

    ??? variable int "`dozzle_role_docker_cpu_period`"

        ```yaml
        # Type: int
        dozzle_role_docker_cpu_period:
        ```

    ??? variable int "`dozzle_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        dozzle_role_docker_cpu_quota:
        ```

    ??? variable int "`dozzle_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        dozzle_role_docker_cpu_shares:
        ```

    ??? variable string "`dozzle_role_docker_cpus`"

        ```yaml
        # Type: string
        dozzle_role_docker_cpus:
        ```

    ??? variable string "`dozzle_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        dozzle_role_docker_cpuset_cpus:
        ```

    ??? variable string "`dozzle_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        dozzle_role_docker_cpuset_mems:
        ```

    ??? variable string "`dozzle_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        dozzle_role_docker_kernel_memory:
        ```

    ??? variable string "`dozzle_role_docker_memory`"

        ```yaml
        # Type: string
        dozzle_role_docker_memory:
        ```

    ??? variable string "`dozzle_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        dozzle_role_docker_memory_reservation:
        ```

    ??? variable string "`dozzle_role_docker_memory_swap`"

        ```yaml
        # Type: string
        dozzle_role_docker_memory_swap:
        ```

    ??? variable int "`dozzle_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        dozzle_role_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`dozzle_role_docker_cap_drop`"

        ```yaml
        # Type: list
        dozzle_role_docker_cap_drop:
        ```

    ??? variable list "`dozzle_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        dozzle_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`dozzle_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        dozzle_role_docker_device_read_bps:
        ```

    ??? variable list "`dozzle_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        dozzle_role_docker_device_read_iops:
        ```

    ??? variable list "`dozzle_role_docker_device_requests`"

        ```yaml
        # Type: list
        dozzle_role_docker_device_requests:
        ```

    ??? variable list "`dozzle_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        dozzle_role_docker_device_write_bps:
        ```

    ??? variable list "`dozzle_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        dozzle_role_docker_device_write_iops:
        ```

    ??? variable list "`dozzle_role_docker_devices`"

        ```yaml
        # Type: list
        dozzle_role_docker_devices:
        ```

    ??? variable string "`dozzle_role_docker_devices_default`"

        ```yaml
        # Type: string
        dozzle_role_docker_devices_default:
        ```

    ??? variable bool "`dozzle_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_privileged:
        ```

    ??? variable list "`dozzle_role_docker_security_opts`"

        ```yaml
        # Type: list
        dozzle_role_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`dozzle_role_docker_dns_opts`"

        ```yaml
        # Type: list
        dozzle_role_docker_dns_opts:
        ```

    ??? variable list "`dozzle_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        dozzle_role_docker_dns_search_domains:
        ```

    ??? variable list "`dozzle_role_docker_dns_servers`"

        ```yaml
        # Type: list
        dozzle_role_docker_dns_servers:
        ```

    ??? variable dict "`dozzle_role_docker_hosts`"

        ```yaml
        # Type: dict
        dozzle_role_docker_hosts:
        ```

    ??? variable string "`dozzle_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        dozzle_role_docker_hosts_use_common:
        ```

    ??? variable string "`dozzle_role_docker_network_mode`"

        ```yaml
        # Type: string
        dozzle_role_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`dozzle_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_keep_volumes:
        ```

    ??? variable list "`dozzle_role_docker_mounts`"

        ```yaml
        # Type: list
        dozzle_role_docker_mounts:
        ```

    ??? variable string "`dozzle_role_docker_volume_driver`"

        ```yaml
        # Type: string
        dozzle_role_docker_volume_driver:
        ```

    ??? variable list "`dozzle_role_docker_volumes`"

        ```yaml
        # Type: list
        dozzle_role_docker_volumes:
        ```

    ??? variable list "`dozzle_role_docker_volumes_from`"

        ```yaml
        # Type: list
        dozzle_role_docker_volumes_from:
        ```

    ??? variable string "`dozzle_role_docker_volumes_global`"

        ```yaml
        # Type: string
        dozzle_role_docker_volumes_global:
        ```

    ??? variable string "`dozzle_role_docker_working_dir`"

        ```yaml
        # Type: string
        dozzle_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`dozzle_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        dozzle_role_docker_healthcheck:
        ```

    ??? variable bool "`dozzle_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_init:
        ```

    ??? variable string "`dozzle_role_docker_log_driver`"

        ```yaml
        # Type: string
        dozzle_role_docker_log_driver:
        ```

    ??? variable dict "`dozzle_role_docker_log_options`"

        ```yaml
        # Type: dict
        dozzle_role_docker_log_options:
        ```

    ??? variable bool "`dozzle_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`dozzle_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_auto_remove:
        ```

    ??? variable list "`dozzle_role_docker_capabilities`"

        ```yaml
        # Type: list
        dozzle_role_docker_capabilities:
        ```

    ??? variable string "`dozzle_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        dozzle_role_docker_cgroup_parent:
        ```

    ??? variable string "`dozzle_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        dozzle_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`dozzle_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_cleanup:
        ```

    ??? variable string "`dozzle_role_docker_create_timeout`"

        ```yaml
        # Type: string
        dozzle_role_docker_create_timeout:
        ```

    ??? variable string "`dozzle_role_docker_domainname`"

        ```yaml
        # Type: string
        dozzle_role_docker_domainname:
        ```

    ??? variable string "`dozzle_role_docker_entrypoint`"

        ```yaml
        # Type: string
        dozzle_role_docker_entrypoint:
        ```

    ??? variable string "`dozzle_role_docker_env_file`"

        ```yaml
        # Type: string
        dozzle_role_docker_env_file:
        ```

    ??? variable list "`dozzle_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        dozzle_role_docker_exposed_ports:
        ```

    ??? variable string "`dozzle_role_docker_force_kill`"

        ```yaml
        # Type: string
        dozzle_role_docker_force_kill:
        ```

    ??? variable list "`dozzle_role_docker_groups`"

        ```yaml
        # Type: list
        dozzle_role_docker_groups:
        ```

    ??? variable int "`dozzle_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        dozzle_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`dozzle_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        dozzle_role_docker_ipc_mode:
        ```

    ??? variable string "`dozzle_role_docker_kill_signal`"

        ```yaml
        # Type: string
        dozzle_role_docker_kill_signal:
        ```

    ??? variable string "`dozzle_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        dozzle_role_docker_labels_use_common:
        ```

    ??? variable list "`dozzle_role_docker_links`"

        ```yaml
        # Type: list
        dozzle_role_docker_links:
        ```

    ??? variable bool "`dozzle_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_oom_killer:
        ```

    ??? variable int "`dozzle_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        dozzle_role_docker_oom_score_adj:
        ```

    ??? variable bool "`dozzle_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_paused:
        ```

    ??? variable string "`dozzle_role_docker_pid_mode`"

        ```yaml
        # Type: string
        dozzle_role_docker_pid_mode:
        ```

    ??? variable list "`dozzle_role_docker_ports`"

        ```yaml
        # Type: list
        dozzle_role_docker_ports:
        ```

    ??? variable bool "`dozzle_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_read_only:
        ```

    ??? variable bool "`dozzle_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_recreate:
        ```

    ??? variable int "`dozzle_role_docker_restart_retries`"

        ```yaml
        # Type: int
        dozzle_role_docker_restart_retries:
        ```

    ??? variable string "`dozzle_role_docker_runtime`"

        ```yaml
        # Type: string
        dozzle_role_docker_runtime:
        ```

    ??? variable string "`dozzle_role_docker_shm_size`"

        ```yaml
        # Type: string
        dozzle_role_docker_shm_size:
        ```

    ??? variable int "`dozzle_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        dozzle_role_docker_stop_timeout:
        ```

    ??? variable dict "`dozzle_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        dozzle_role_docker_storage_opts:
        ```

    ??? variable list "`dozzle_role_docker_sysctls`"

        ```yaml
        # Type: list
        dozzle_role_docker_sysctls:
        ```

    ??? variable list "`dozzle_role_docker_tmpfs`"

        ```yaml
        # Type: list
        dozzle_role_docker_tmpfs:
        ```

    ??? variable list "`dozzle_role_docker_ulimits`"

        ```yaml
        # Type: list
        dozzle_role_docker_ulimits:
        ```

    ??? variable string "`dozzle_role_docker_user`"

        ```yaml
        # Type: string
        dozzle_role_docker_user:
        ```

    ??? variable string "`dozzle_role_docker_userns_mode`"

        ```yaml
        # Type: string
        dozzle_role_docker_userns_mode:
        ```

    ??? variable string "`dozzle_role_docker_uts`"

        ```yaml
        # Type: string
        dozzle_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`dozzle_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        dozzle_role_autoheal_enabled: true
        ```

    ??? variable string "`dozzle_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        dozzle_role_depends_on: ""
        ```

    ??? variable string "`dozzle_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        dozzle_role_depends_on_delay: "0"
        ```

    ??? variable string "`dozzle_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        dozzle_role_depends_on_healthchecks:
        ```

    ??? variable bool "`dozzle_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        dozzle_role_diun_enabled: true
        ```

    ??? variable bool "`dozzle_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        dozzle_role_dns_enabled: true
        ```

    ??? variable bool "`dozzle_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        dozzle_role_docker_controller: true
        ```

    ??? variable bool "`dozzle_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_docker_volumes_download:
        ```

    ??? variable bool "`dozzle_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        dozzle_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`dozzle_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        dozzle_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`dozzle_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        dozzle_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`dozzle_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        dozzle_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`dozzle_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`dozzle_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        dozzle_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`dozzle_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        dozzle_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`dozzle_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        dozzle_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`dozzle_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        dozzle_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`dozzle_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        dozzle_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            dozzle_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "dozzle2.{{ user.domain }}"
              - "dozzle.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`dozzle_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        dozzle_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            dozzle_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dozzle2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`dozzle_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        dozzle_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->