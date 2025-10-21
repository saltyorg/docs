---
hide:
  - tags
tags:
  - tautulli
---

# Tautulli

# What is it?

[Tautulli](http://tautulli.com/) (Tautulli), by JonnyWong16, is a web-based application runs alongside the Plex Media Server to monitor activity and track various statistics (eg most watched media).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://tautulli.com){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Tautulli/Tautulli/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Tautulli/Tautulli){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/tautulli){: .header-icons }|

## 2. URL

To access Tautulli, visit `https://tautulli._yourdomain_.com`

## 3. Setup Wizard

1. First time you go to the Tautulli site, you will be presented with the "Tautulli Setup Wizard". Click `Next`.

    ![](../images/tautulli/01-tautulli-wizard.png)

2. On the "Plex Authentication" page, sign in with your Plex username and password, and click `Authenticate`. When you see the "Authentication successful." message, click `Next`.

    ![](../images/tautulli/02-tautulli-plex-auth.png)

3. On the "Plex Media Server" page, set the following:

    - "Plex IP or Hostname": `plex`
    - "Port Number": `32400`
    - "Use SSL": disabled
    - "Remote Server": disabled

     Click `Verify`. When you see the "Server found!" message, click `Next`.

     ![](../images/tautulli/03-tautulli-plex-media.png)

4. On the "Activity Logging" page, select your preferences (default is OK) and click `Next`.

    ![](../images/tautulli/04-tautulli-activity.png)

5. On the "Notifications" page, simply click `Next`.

    ![](../images/tautulli/05-tautulli-notifications.png)

6. On the "Database Import" page, click `Finish` to complete the setup.

    ![](../images/tautulli/06-tautulli-database.png)

## 4. Settings

1. Once the Tautulli page comes up, go to "Settings".

    ![](../images/tautulli/07-tautulli-settings.png)

2. Click "Web Interface" on the left. Fill in "HTTP Username" and "HTTP Password (this will be the login for your Tautulli site), but don't click `Save` yet.

    ![](../images/tautulli/08-tautulli-web.png)

3. On the "Restart" popup window, click `Restart`.

    ![](../images/tautulli/10-tautulli-reboot.png)

## Next

Are you setting Saltbox up for the first time?  Continue to [Overseerr](overseerr.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `tautulli_instances`.

    === "Role-level Override"

        Applies to all instances of tautulli:

        ```yaml
        tautulli_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `tautulli2`):

        ```yaml
        tautulli2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `tautulli_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tautulli_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`tautulli_instances`"

        ```yaml
        # Type: list
        tautulli_instances: ["tautulli"]
        ```

        !!! example

            ```yaml
            # Type: list
            tautulli_instances: ["tautulli", "tautulli2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`tautulli_role_paths_folder`"

            ```yaml
            # Type: string
            tautulli_role_paths_folder: "{{ tautulli_name }}"
            ```

        ??? variable string "`tautulli_role_paths_location`"

            ```yaml
            # Type: string
            tautulli_role_paths_location: "{{ server_appdata_path }}/{{ tautulli_role_paths_folder }}"
            ```

        ??? variable string "`tautulli_role_paths_scripts_location`"

            ```yaml
            # Type: string
            tautulli_role_paths_scripts_location: "{{ server_appdata_path }}/scripts/tautulli"
            ```

    === "Instance-level"

        ??? variable string "`tautulli2_paths_folder`"

            ```yaml
            # Type: string
            tautulli2_paths_folder: "{{ tautulli_name }}"
            ```

        ??? variable string "`tautulli2_paths_location`"

            ```yaml
            # Type: string
            tautulli2_paths_location: "{{ server_appdata_path }}/{{ tautulli_role_paths_folder }}"
            ```

        ??? variable string "`tautulli2_paths_scripts_location`"

            ```yaml
            # Type: string
            tautulli2_paths_scripts_location: "{{ server_appdata_path }}/scripts/tautulli"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`tautulli_role_web_subdomain`"

            ```yaml
            # Type: string
            tautulli_role_web_subdomain: "{{ tautulli_name }}"
            ```

        ??? variable string "`tautulli_role_web_domain`"

            ```yaml
            # Type: string
            tautulli_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`tautulli_role_web_port`"

            ```yaml
            # Type: string
            tautulli_role_web_port: "8181"
            ```

        ??? variable string "`tautulli_role_web_url`"

            ```yaml
            # Type: string
            tautulli_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tautulli') + '.' + lookup('role_var', '_web_domain', role='tautulli')
                                    if (lookup('role_var', '_web_subdomain', role='tautulli') | length > 0)
                                    else lookup('role_var', '_web_domain', role='tautulli')) }}"
            ```

    === "Instance-level"

        ??? variable string "`tautulli2_web_subdomain`"

            ```yaml
            # Type: string
            tautulli2_web_subdomain: "{{ tautulli_name }}"
            ```

        ??? variable string "`tautulli2_web_domain`"

            ```yaml
            # Type: string
            tautulli2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`tautulli2_web_port`"

            ```yaml
            # Type: string
            tautulli2_web_port: "8181"
            ```

        ??? variable string "`tautulli2_web_url`"

            ```yaml
            # Type: string
            tautulli2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tautulli') + '.' + lookup('role_var', '_web_domain', role='tautulli')
                                if (lookup('role_var', '_web_subdomain', role='tautulli') | length > 0)
                                else lookup('role_var', '_web_domain', role='tautulli')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`tautulli_role_dns_record`"

            ```yaml
            # Type: string
            tautulli_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tautulli') }}"
            ```

        ??? variable string "`tautulli_role_dns_zone`"

            ```yaml
            # Type: string
            tautulli_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tautulli') }}"
            ```

        ??? variable bool "`tautulli_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`tautulli2_dns_record`"

            ```yaml
            # Type: string
            tautulli2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tautulli') }}"
            ```

        ??? variable string "`tautulli2_dns_zone`"

            ```yaml
            # Type: string
            tautulli2_dns_zone: "{{ lookup('role_var', '_web_domain', role='tautulli') }}"
            ```

        ??? variable bool "`tautulli2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`tautulli_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            tautulli_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`tautulli_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            tautulli_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                          + (',themepark-' + tautulli_name
                                                            if (lookup('role_var', '_themepark_enabled', role='tautulli') and global_themepark_plugin_enabled)
                                                            else '') }}"
            ```

        ??? variable string "`tautulli_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            tautulli_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`tautulli_role_traefik_certresolver`"

            ```yaml
            # Type: string
            tautulli_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`tautulli_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_traefik_enabled: true
            ```

        ??? variable bool "`tautulli_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_traefik_api_enabled: true
            ```

        ??? variable string "`tautulli_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            tautulli_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/newsletter`) || PathPrefix(`/image`) || PathPrefix(`/pms_image_proxy`)"
            ```

        ??? variable bool "`tautulli_role_traefik_gzip_enabled`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_traefik_gzip_enabled: false
            ```

    === "Instance-level"

        ??? variable string "`tautulli2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            tautulli2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`tautulli2_traefik_middleware_default`"

            ```yaml
            # Type: string
            tautulli2_traefik_middleware_default: "{{ traefik_default_middleware
                                                      + (',themepark-' + tautulli_name
                                                        if (lookup('role_var', '_themepark_enabled', role='tautulli') and global_themepark_plugin_enabled)
                                                        else '') }}"
            ```

        ??? variable string "`tautulli2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            tautulli2_traefik_middleware_custom: ""
            ```

        ??? variable string "`tautulli2_traefik_certresolver`"

            ```yaml
            # Type: string
            tautulli2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`tautulli2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_traefik_enabled: true
            ```

        ??? variable bool "`tautulli2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_traefik_api_enabled: true
            ```

        ??? variable string "`tautulli2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            tautulli2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/newsletter`) || PathPrefix(`/image`) || PathPrefix(`/pms_image_proxy`)"
            ```

        ??? variable bool "`tautulli2_traefik_gzip_enabled`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_traefik_gzip_enabled: false
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`tautulli_role_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            tautulli_role_themepark_enabled: false
            ```

        ??? variable string "`tautulli_role_themepark_app`"

            ```yaml
            # Type: string
            tautulli_role_themepark_app: "tautulli"
            ```

        ??? variable string "`tautulli_role_themepark_theme`"

            ```yaml
            # Type: string
            tautulli_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`tautulli_role_themepark_domain`"

            ```yaml
            # Type: string
            tautulli_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`tautulli_role_themepark_addons`"

            ```yaml
            # Type: list
            tautulli_role_themepark_addons: []
            ```

    === "Instance-level"

        ??? variable bool "`tautulli2_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            tautulli2_themepark_enabled: false
            ```

        ??? variable string "`tautulli2_themepark_app`"

            ```yaml
            # Type: string
            tautulli2_themepark_app: "tautulli"
            ```

        ??? variable string "`tautulli2_themepark_theme`"

            ```yaml
            # Type: string
            tautulli2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`tautulli2_themepark_domain`"

            ```yaml
            # Type: string
            tautulli2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`tautulli2_themepark_addons`"

            ```yaml
            # Type: list
            tautulli2_themepark_addons: []
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`tautulli_role_docker_container`"

            ```yaml
            # Type: string
            tautulli_role_docker_container: "{{ tautulli_name }}"
            ```

        ##### Image

        ??? variable bool "`tautulli_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_image_pull: true
            ```

        ??? variable string "`tautulli_role_docker_image_repo`"

            ```yaml
            # Type: string
            tautulli_role_docker_image_repo: "ghcr.io/hotio/tautulli"
            ```

        ??? variable string "`tautulli_role_docker_image_tag`"

            ```yaml
            # Type: string
            tautulli_role_docker_image_tag: "release"
            ```

        ??? variable string "`tautulli_role_docker_image`"

            ```yaml
            # Type: string
            tautulli_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tautulli') }}:{{ lookup('role_var', '_docker_image_tag', role='tautulli') }}"
            ```

        ##### Envs

        ??? variable dict "`tautulli_role_docker_envs_default`"

            ```yaml
            # Type: dict
            tautulli_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`tautulli_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            tautulli_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`tautulli_role_docker_volumes_default`"

            ```yaml
            # Type: list
            tautulli_role_docker_volumes_default: 
              - "{{ tautulli_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`tautulli_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            tautulli_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`tautulli_role_docker_labels_default`"

            ```yaml
            # Type: dict
            tautulli_role_docker_labels_default: {}
            ```

        ??? variable dict "`tautulli_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            tautulli_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`tautulli_role_docker_hostname`"

            ```yaml
            # Type: string
            tautulli_role_docker_hostname: "{{ tautulli_name }}"
            ```

        ##### Networks

        ??? variable string "`tautulli_role_docker_networks_alias`"

            ```yaml
            # Type: string
            tautulli_role_docker_networks_alias: "{{ tautulli_name }}"
            ```

        ??? variable list "`tautulli_role_docker_networks_default`"

            ```yaml
            # Type: list
            tautulli_role_docker_networks_default: []
            ```

        ??? variable list "`tautulli_role_docker_networks_custom`"

            ```yaml
            # Type: list
            tautulli_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`tautulli_role_docker_restart_policy`"

            ```yaml
            # Type: string
            tautulli_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`tautulli_role_docker_state`"

            ```yaml
            # Type: string
            tautulli_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`tautulli2_docker_container`"

            ```yaml
            # Type: string
            tautulli2_docker_container: "{{ tautulli_name }}"
            ```

        ##### Image

        ??? variable bool "`tautulli2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_image_pull: true
            ```

        ??? variable string "`tautulli2_docker_image_repo`"

            ```yaml
            # Type: string
            tautulli2_docker_image_repo: "ghcr.io/hotio/tautulli"
            ```

        ??? variable string "`tautulli2_docker_image_tag`"

            ```yaml
            # Type: string
            tautulli2_docker_image_tag: "release"
            ```

        ??? variable string "`tautulli2_docker_image`"

            ```yaml
            # Type: string
            tautulli2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tautulli') }}:{{ lookup('role_var', '_docker_image_tag', role='tautulli') }}"
            ```

        ##### Envs

        ??? variable dict "`tautulli2_docker_envs_default`"

            ```yaml
            # Type: dict
            tautulli2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`tautulli2_docker_envs_custom`"

            ```yaml
            # Type: dict
            tautulli2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`tautulli2_docker_volumes_default`"

            ```yaml
            # Type: list
            tautulli2_docker_volumes_default: 
              - "{{ tautulli_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`tautulli2_docker_volumes_custom`"

            ```yaml
            # Type: list
            tautulli2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`tautulli2_docker_labels_default`"

            ```yaml
            # Type: dict
            tautulli2_docker_labels_default: {}
            ```

        ??? variable dict "`tautulli2_docker_labels_custom`"

            ```yaml
            # Type: dict
            tautulli2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`tautulli2_docker_hostname`"

            ```yaml
            # Type: string
            tautulli2_docker_hostname: "{{ tautulli_name }}"
            ```

        ##### Networks

        ??? variable string "`tautulli2_docker_networks_alias`"

            ```yaml
            # Type: string
            tautulli2_docker_networks_alias: "{{ tautulli_name }}"
            ```

        ??? variable list "`tautulli2_docker_networks_default`"

            ```yaml
            # Type: list
            tautulli2_docker_networks_default: []
            ```

        ??? variable list "`tautulli2_docker_networks_custom`"

            ```yaml
            # Type: list
            tautulli2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`tautulli2_docker_restart_policy`"

            ```yaml
            # Type: string
            tautulli2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`tautulli2_docker_state`"

            ```yaml
            # Type: string
            tautulli2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`tautulli_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            tautulli_role_docker_blkio_weight:
            ```

        ??? variable int "`tautulli_role_docker_cpu_period`"

            ```yaml
            # Type: int
            tautulli_role_docker_cpu_period:
            ```

        ??? variable int "`tautulli_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            tautulli_role_docker_cpu_quota:
            ```

        ??? variable int "`tautulli_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            tautulli_role_docker_cpu_shares:
            ```

        ??? variable string "`tautulli_role_docker_cpus`"

            ```yaml
            # Type: string
            tautulli_role_docker_cpus:
            ```

        ??? variable string "`tautulli_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            tautulli_role_docker_cpuset_cpus:
            ```

        ??? variable string "`tautulli_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            tautulli_role_docker_cpuset_mems:
            ```

        ??? variable string "`tautulli_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            tautulli_role_docker_kernel_memory:
            ```

        ??? variable string "`tautulli_role_docker_memory`"

            ```yaml
            # Type: string
            tautulli_role_docker_memory:
            ```

        ??? variable string "`tautulli_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            tautulli_role_docker_memory_reservation:
            ```

        ??? variable string "`tautulli_role_docker_memory_swap`"

            ```yaml
            # Type: string
            tautulli_role_docker_memory_swap:
            ```

        ??? variable int "`tautulli_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            tautulli_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`tautulli_role_docker_cap_drop`"

            ```yaml
            # Type: list
            tautulli_role_docker_cap_drop:
            ```

        ??? variable list "`tautulli_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            tautulli_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`tautulli_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            tautulli_role_docker_device_read_bps:
            ```

        ??? variable list "`tautulli_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            tautulli_role_docker_device_read_iops:
            ```

        ??? variable list "`tautulli_role_docker_device_requests`"

            ```yaml
            # Type: list
            tautulli_role_docker_device_requests:
            ```

        ??? variable list "`tautulli_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            tautulli_role_docker_device_write_bps:
            ```

        ??? variable list "`tautulli_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            tautulli_role_docker_device_write_iops:
            ```

        ??? variable list "`tautulli_role_docker_devices`"

            ```yaml
            # Type: list
            tautulli_role_docker_devices:
            ```

        ??? variable string "`tautulli_role_docker_devices_default`"

            ```yaml
            # Type: string
            tautulli_role_docker_devices_default:
            ```

        ??? variable bool "`tautulli_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_privileged:
            ```

        ??? variable list "`tautulli_role_docker_security_opts`"

            ```yaml
            # Type: list
            tautulli_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`tautulli_role_docker_dns_opts`"

            ```yaml
            # Type: list
            tautulli_role_docker_dns_opts:
            ```

        ??? variable list "`tautulli_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            tautulli_role_docker_dns_search_domains:
            ```

        ??? variable list "`tautulli_role_docker_dns_servers`"

            ```yaml
            # Type: list
            tautulli_role_docker_dns_servers:
            ```

        ??? variable dict "`tautulli_role_docker_hosts`"

            ```yaml
            # Type: dict
            tautulli_role_docker_hosts:
            ```

        ??? variable string "`tautulli_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            tautulli_role_docker_hosts_use_common:
            ```

        ??? variable string "`tautulli_role_docker_network_mode`"

            ```yaml
            # Type: string
            tautulli_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`tautulli_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_keep_volumes:
            ```

        ??? variable list "`tautulli_role_docker_mounts`"

            ```yaml
            # Type: list
            tautulli_role_docker_mounts:
            ```

        ??? variable string "`tautulli_role_docker_volume_driver`"

            ```yaml
            # Type: string
            tautulli_role_docker_volume_driver:
            ```

        ??? variable list "`tautulli_role_docker_volumes_from`"

            ```yaml
            # Type: list
            tautulli_role_docker_volumes_from:
            ```

        ??? variable string "`tautulli_role_docker_volumes_global`"

            ```yaml
            # Type: string
            tautulli_role_docker_volumes_global:
            ```

        ??? variable string "`tautulli_role_docker_working_dir`"

            ```yaml
            # Type: string
            tautulli_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`tautulli_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            tautulli_role_docker_healthcheck:
            ```

        ??? variable bool "`tautulli_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_init:
            ```

        ??? variable string "`tautulli_role_docker_log_driver`"

            ```yaml
            # Type: string
            tautulli_role_docker_log_driver:
            ```

        ??? variable dict "`tautulli_role_docker_log_options`"

            ```yaml
            # Type: dict
            tautulli_role_docker_log_options:
            ```

        ??? variable bool "`tautulli_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`tautulli_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_auto_remove:
            ```

        ??? variable list "`tautulli_role_docker_capabilities`"

            ```yaml
            # Type: list
            tautulli_role_docker_capabilities:
            ```

        ??? variable string "`tautulli_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            tautulli_role_docker_cgroup_parent:
            ```

        ??? variable string "`tautulli_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            tautulli_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`tautulli_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_cleanup:
            ```

        ??? variable list "`tautulli_role_docker_commands`"

            ```yaml
            # Type: list
            tautulli_role_docker_commands:
            ```

        ??? variable string "`tautulli_role_docker_create_timeout`"

            ```yaml
            # Type: string
            tautulli_role_docker_create_timeout:
            ```

        ??? variable string "`tautulli_role_docker_domainname`"

            ```yaml
            # Type: string
            tautulli_role_docker_domainname:
            ```

        ??? variable string "`tautulli_role_docker_entrypoint`"

            ```yaml
            # Type: string
            tautulli_role_docker_entrypoint:
            ```

        ??? variable string "`tautulli_role_docker_env_file`"

            ```yaml
            # Type: string
            tautulli_role_docker_env_file:
            ```

        ??? variable list "`tautulli_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            tautulli_role_docker_exposed_ports:
            ```

        ??? variable string "`tautulli_role_docker_force_kill`"

            ```yaml
            # Type: string
            tautulli_role_docker_force_kill:
            ```

        ??? variable list "`tautulli_role_docker_groups`"

            ```yaml
            # Type: list
            tautulli_role_docker_groups:
            ```

        ??? variable int "`tautulli_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            tautulli_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`tautulli_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            tautulli_role_docker_ipc_mode:
            ```

        ??? variable string "`tautulli_role_docker_kill_signal`"

            ```yaml
            # Type: string
            tautulli_role_docker_kill_signal:
            ```

        ??? variable string "`tautulli_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            tautulli_role_docker_labels_use_common:
            ```

        ??? variable list "`tautulli_role_docker_links`"

            ```yaml
            # Type: list
            tautulli_role_docker_links:
            ```

        ??? variable bool "`tautulli_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_oom_killer:
            ```

        ??? variable int "`tautulli_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            tautulli_role_docker_oom_score_adj:
            ```

        ??? variable bool "`tautulli_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_paused:
            ```

        ??? variable string "`tautulli_role_docker_pid_mode`"

            ```yaml
            # Type: string
            tautulli_role_docker_pid_mode:
            ```

        ??? variable list "`tautulli_role_docker_ports`"

            ```yaml
            # Type: list
            tautulli_role_docker_ports:
            ```

        ??? variable bool "`tautulli_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_read_only:
            ```

        ??? variable bool "`tautulli_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            tautulli_role_docker_recreate:
            ```

        ??? variable int "`tautulli_role_docker_restart_retries`"

            ```yaml
            # Type: int
            tautulli_role_docker_restart_retries:
            ```

        ??? variable string "`tautulli_role_docker_runtime`"

            ```yaml
            # Type: string
            tautulli_role_docker_runtime:
            ```

        ??? variable string "`tautulli_role_docker_shm_size`"

            ```yaml
            # Type: string
            tautulli_role_docker_shm_size:
            ```

        ??? variable int "`tautulli_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            tautulli_role_docker_stop_timeout:
            ```

        ??? variable dict "`tautulli_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            tautulli_role_docker_storage_opts:
            ```

        ??? variable list "`tautulli_role_docker_sysctls`"

            ```yaml
            # Type: list
            tautulli_role_docker_sysctls:
            ```

        ??? variable list "`tautulli_role_docker_tmpfs`"

            ```yaml
            # Type: list
            tautulli_role_docker_tmpfs:
            ```

        ??? variable list "`tautulli_role_docker_ulimits`"

            ```yaml
            # Type: list
            tautulli_role_docker_ulimits:
            ```

        ??? variable string "`tautulli_role_docker_user`"

            ```yaml
            # Type: string
            tautulli_role_docker_user:
            ```

        ??? variable string "`tautulli_role_docker_userns_mode`"

            ```yaml
            # Type: string
            tautulli_role_docker_userns_mode:
            ```

        ??? variable string "`tautulli_role_docker_uts`"

            ```yaml
            # Type: string
            tautulli_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`tautulli2_docker_blkio_weight`"

            ```yaml
            # Type: int
            tautulli2_docker_blkio_weight:
            ```

        ??? variable int "`tautulli2_docker_cpu_period`"

            ```yaml
            # Type: int
            tautulli2_docker_cpu_period:
            ```

        ??? variable int "`tautulli2_docker_cpu_quota`"

            ```yaml
            # Type: int
            tautulli2_docker_cpu_quota:
            ```

        ??? variable int "`tautulli2_docker_cpu_shares`"

            ```yaml
            # Type: int
            tautulli2_docker_cpu_shares:
            ```

        ??? variable string "`tautulli2_docker_cpus`"

            ```yaml
            # Type: string
            tautulli2_docker_cpus:
            ```

        ??? variable string "`tautulli2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            tautulli2_docker_cpuset_cpus:
            ```

        ??? variable string "`tautulli2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            tautulli2_docker_cpuset_mems:
            ```

        ??? variable string "`tautulli2_docker_kernel_memory`"

            ```yaml
            # Type: string
            tautulli2_docker_kernel_memory:
            ```

        ??? variable string "`tautulli2_docker_memory`"

            ```yaml
            # Type: string
            tautulli2_docker_memory:
            ```

        ??? variable string "`tautulli2_docker_memory_reservation`"

            ```yaml
            # Type: string
            tautulli2_docker_memory_reservation:
            ```

        ??? variable string "`tautulli2_docker_memory_swap`"

            ```yaml
            # Type: string
            tautulli2_docker_memory_swap:
            ```

        ??? variable int "`tautulli2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            tautulli2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`tautulli2_docker_cap_drop`"

            ```yaml
            # Type: list
            tautulli2_docker_cap_drop:
            ```

        ??? variable list "`tautulli2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            tautulli2_docker_device_cgroup_rules:
            ```

        ??? variable list "`tautulli2_docker_device_read_bps`"

            ```yaml
            # Type: list
            tautulli2_docker_device_read_bps:
            ```

        ??? variable list "`tautulli2_docker_device_read_iops`"

            ```yaml
            # Type: list
            tautulli2_docker_device_read_iops:
            ```

        ??? variable list "`tautulli2_docker_device_requests`"

            ```yaml
            # Type: list
            tautulli2_docker_device_requests:
            ```

        ??? variable list "`tautulli2_docker_device_write_bps`"

            ```yaml
            # Type: list
            tautulli2_docker_device_write_bps:
            ```

        ??? variable list "`tautulli2_docker_device_write_iops`"

            ```yaml
            # Type: list
            tautulli2_docker_device_write_iops:
            ```

        ??? variable list "`tautulli2_docker_devices`"

            ```yaml
            # Type: list
            tautulli2_docker_devices:
            ```

        ??? variable string "`tautulli2_docker_devices_default`"

            ```yaml
            # Type: string
            tautulli2_docker_devices_default:
            ```

        ??? variable bool "`tautulli2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_privileged:
            ```

        ??? variable list "`tautulli2_docker_security_opts`"

            ```yaml
            # Type: list
            tautulli2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`tautulli2_docker_dns_opts`"

            ```yaml
            # Type: list
            tautulli2_docker_dns_opts:
            ```

        ??? variable list "`tautulli2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            tautulli2_docker_dns_search_domains:
            ```

        ??? variable list "`tautulli2_docker_dns_servers`"

            ```yaml
            # Type: list
            tautulli2_docker_dns_servers:
            ```

        ??? variable dict "`tautulli2_docker_hosts`"

            ```yaml
            # Type: dict
            tautulli2_docker_hosts:
            ```

        ??? variable string "`tautulli2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            tautulli2_docker_hosts_use_common:
            ```

        ??? variable string "`tautulli2_docker_network_mode`"

            ```yaml
            # Type: string
            tautulli2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`tautulli2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_keep_volumes:
            ```

        ??? variable list "`tautulli2_docker_mounts`"

            ```yaml
            # Type: list
            tautulli2_docker_mounts:
            ```

        ??? variable string "`tautulli2_docker_volume_driver`"

            ```yaml
            # Type: string
            tautulli2_docker_volume_driver:
            ```

        ??? variable list "`tautulli2_docker_volumes_from`"

            ```yaml
            # Type: list
            tautulli2_docker_volumes_from:
            ```

        ??? variable string "`tautulli2_docker_volumes_global`"

            ```yaml
            # Type: string
            tautulli2_docker_volumes_global:
            ```

        ??? variable string "`tautulli2_docker_working_dir`"

            ```yaml
            # Type: string
            tautulli2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`tautulli2_docker_healthcheck`"

            ```yaml
            # Type: dict
            tautulli2_docker_healthcheck:
            ```

        ??? variable bool "`tautulli2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_init:
            ```

        ??? variable string "`tautulli2_docker_log_driver`"

            ```yaml
            # Type: string
            tautulli2_docker_log_driver:
            ```

        ??? variable dict "`tautulli2_docker_log_options`"

            ```yaml
            # Type: dict
            tautulli2_docker_log_options:
            ```

        ??? variable bool "`tautulli2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`tautulli2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_auto_remove:
            ```

        ??? variable list "`tautulli2_docker_capabilities`"

            ```yaml
            # Type: list
            tautulli2_docker_capabilities:
            ```

        ??? variable string "`tautulli2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            tautulli2_docker_cgroup_parent:
            ```

        ??? variable string "`tautulli2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            tautulli2_docker_cgroupns_mode:
            ```

        ??? variable bool "`tautulli2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_cleanup:
            ```

        ??? variable list "`tautulli2_docker_commands`"

            ```yaml
            # Type: list
            tautulli2_docker_commands:
            ```

        ??? variable string "`tautulli2_docker_create_timeout`"

            ```yaml
            # Type: string
            tautulli2_docker_create_timeout:
            ```

        ??? variable string "`tautulli2_docker_domainname`"

            ```yaml
            # Type: string
            tautulli2_docker_domainname:
            ```

        ??? variable string "`tautulli2_docker_entrypoint`"

            ```yaml
            # Type: string
            tautulli2_docker_entrypoint:
            ```

        ??? variable string "`tautulli2_docker_env_file`"

            ```yaml
            # Type: string
            tautulli2_docker_env_file:
            ```

        ??? variable list "`tautulli2_docker_exposed_ports`"

            ```yaml
            # Type: list
            tautulli2_docker_exposed_ports:
            ```

        ??? variable string "`tautulli2_docker_force_kill`"

            ```yaml
            # Type: string
            tautulli2_docker_force_kill:
            ```

        ??? variable list "`tautulli2_docker_groups`"

            ```yaml
            # Type: list
            tautulli2_docker_groups:
            ```

        ??? variable int "`tautulli2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            tautulli2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`tautulli2_docker_ipc_mode`"

            ```yaml
            # Type: string
            tautulli2_docker_ipc_mode:
            ```

        ??? variable string "`tautulli2_docker_kill_signal`"

            ```yaml
            # Type: string
            tautulli2_docker_kill_signal:
            ```

        ??? variable string "`tautulli2_docker_labels_use_common`"

            ```yaml
            # Type: string
            tautulli2_docker_labels_use_common:
            ```

        ??? variable list "`tautulli2_docker_links`"

            ```yaml
            # Type: list
            tautulli2_docker_links:
            ```

        ??? variable bool "`tautulli2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_oom_killer:
            ```

        ??? variable int "`tautulli2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            tautulli2_docker_oom_score_adj:
            ```

        ??? variable bool "`tautulli2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_paused:
            ```

        ??? variable string "`tautulli2_docker_pid_mode`"

            ```yaml
            # Type: string
            tautulli2_docker_pid_mode:
            ```

        ??? variable list "`tautulli2_docker_ports`"

            ```yaml
            # Type: list
            tautulli2_docker_ports:
            ```

        ??? variable bool "`tautulli2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_read_only:
            ```

        ??? variable bool "`tautulli2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            tautulli2_docker_recreate:
            ```

        ??? variable int "`tautulli2_docker_restart_retries`"

            ```yaml
            # Type: int
            tautulli2_docker_restart_retries:
            ```

        ??? variable string "`tautulli2_docker_runtime`"

            ```yaml
            # Type: string
            tautulli2_docker_runtime:
            ```

        ??? variable string "`tautulli2_docker_shm_size`"

            ```yaml
            # Type: string
            tautulli2_docker_shm_size:
            ```

        ??? variable int "`tautulli2_docker_stop_timeout`"

            ```yaml
            # Type: int
            tautulli2_docker_stop_timeout:
            ```

        ??? variable dict "`tautulli2_docker_storage_opts`"

            ```yaml
            # Type: dict
            tautulli2_docker_storage_opts:
            ```

        ??? variable list "`tautulli2_docker_sysctls`"

            ```yaml
            # Type: list
            tautulli2_docker_sysctls:
            ```

        ??? variable list "`tautulli2_docker_tmpfs`"

            ```yaml
            # Type: list
            tautulli2_docker_tmpfs:
            ```

        ??? variable list "`tautulli2_docker_ulimits`"

            ```yaml
            # Type: list
            tautulli2_docker_ulimits:
            ```

        ??? variable string "`tautulli2_docker_user`"

            ```yaml
            # Type: string
            tautulli2_docker_user:
            ```

        ??? variable string "`tautulli2_docker_userns_mode`"

            ```yaml
            # Type: string
            tautulli2_docker_userns_mode:
            ```

        ??? variable string "`tautulli2_docker_uts`"

            ```yaml
            # Type: string
            tautulli2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`tautulli_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            tautulli_role_autoheal_enabled: true
            ```

        ??? variable string "`tautulli_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            tautulli_role_depends_on: ""
            ```

        ??? variable string "`tautulli_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            tautulli_role_depends_on_delay: "0"
            ```

        ??? variable string "`tautulli_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            tautulli_role_depends_on_healthchecks:
            ```

        ??? variable bool "`tautulli_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            tautulli_role_diun_enabled: true
            ```

        ??? variable bool "`tautulli_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            tautulli_role_dns_enabled: true
            ```

        ??? variable bool "`tautulli_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            tautulli_role_docker_controller: true
            ```

        ??? variable bool "`tautulli_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            tautulli_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`tautulli_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            tautulli_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`tautulli_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            tautulli_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`tautulli_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            tautulli_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`tautulli_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            tautulli_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`tautulli_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            tautulli_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`tautulli_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            tautulli_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`tautulli_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            tautulli_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                tautulli_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "tautulli2.{{ user.domain }}"
                  - "tautulli.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`tautulli_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            tautulli_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                tautulli_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tautulli2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`tautulli_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            tautulli_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `tautulli2`):

        ??? variable bool "`tautulli2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            tautulli2_autoheal_enabled: true
            ```

        ??? variable string "`tautulli2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            tautulli2_depends_on: ""
            ```

        ??? variable string "`tautulli2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            tautulli2_depends_on_delay: "0"
            ```

        ??? variable string "`tautulli2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            tautulli2_depends_on_healthchecks:
            ```

        ??? variable bool "`tautulli2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            tautulli2_diun_enabled: true
            ```

        ??? variable bool "`tautulli2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            tautulli2_dns_enabled: true
            ```

        ??? variable bool "`tautulli2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            tautulli2_docker_controller: true
            ```

        ??? variable bool "`tautulli2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            tautulli2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`tautulli2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            tautulli2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`tautulli2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            tautulli2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`tautulli2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            tautulli2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`tautulli2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            tautulli2_traefik_robot_enabled: true
            ```

        ??? variable bool "`tautulli2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            tautulli2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`tautulli2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            tautulli2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`tautulli2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            tautulli2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                tautulli2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "tautulli2.{{ user.domain }}"
                  - "tautulli.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`tautulli2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            tautulli2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                tautulli2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tautulli2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`tautulli2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            tautulli2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->