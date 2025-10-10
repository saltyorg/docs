---
hide:
  - tags
tags:
  - emby
---

# Emby

# What is it?

[Emby](https://emby.media) is a media server designed to organize, play, and stream audio and video to a variety of devices

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://emby.media){: .header-icons } | [:octicons-link-16: Docs](https://support.emby.media/support/home){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/MediaBrowser/Emby){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/emby/embyserver){: .header-icons }|

## 1. Introduction

![Emby media server splash screen and logo](../images/emby/emby-splash.jpg)

## 2. URL

- To access Emby, visit `https://emby._yourdomain.com_`

## 3. Initial Setup

## i. Domain

- See [Adding a Subdomain](../reference/subdomain.md) on how to add the subdomain `emby` to your DNS provider.

- _Note: You can skip this step if you are using [Cloudflare](../reference/domain.md#__tabbed_1_3) with Saltbox._

## ii. Install

- Run the following command:

    ```shell
    sb install emby
    ```

## 4. Setup Wizard

1. Visit `https://emby._yourdomain.com_`.

1. Select your **preferred display language**. Click **Next**.

   ![](../images/emby/emby-welcome-english.png))

1. **Type** the following and click **Next**:

    - **Username:** _The username you wwant to use to log into Emby_

    - **New Password:** _A strong password you'll use to log into Emby_

    - **New Password Confirm:** _That same password again_

    - **Emby connect username or email address**: _your [Emby Connect username](https://emby.media/connect)_ (important)

   ![](../images/emby/emby-firstuser.png)

1. Confirm the message by clicking **Got It**.

   ![](../images/emby/emby-added.png)

1. **Confirm** the link in your email.

   ![](../images/emby/emby-confirm-link.png)

   ![](../images/emby/emby-link-accepted.png)

2. Skip the adding of the libraries. Click **Next**.

   ![](../images/emby/emby-setup-media-libs.png)

3. Select your **Preferred Metadata Language** and **Country** (_`English` and `United States` are recommended_) and click **Next**.

   ![](../images/emby/emby-preferred-metadata.png)

4. Uncheck **Enable automatic port mapping**. Click **Next**.

   ![](../images/emby/emby-config-remote-access.png)

5. **Check** to accept the terms. Click **Next**.

   ![](../images/emby/emby-terms.png)

6. Click **Finish**.

   ![](../images/emby/emby-done.png)

7. You will now be taken to the **Dashboard** view.

## 5. Settings

## i. Transcoding

1. Go to **Settings**.

1. Go to **Transcoding**.

   ![](../images/emby/emby-transcoding.png)

1. Under **Enable hardware acceleration when available**, select **Advanced**.

   ![](../images/emby/emby-transcoding-advanced.png)

2. Under **Transcoding temporary path**, type in or choose `/transcode`.

   ![](../images/emby/emby-transcoding-hardware-path.png)

3. Click **Save**.

## iii. Libraries

In this section, we will add two libraries: one for Movies and one for TV Shows.

### Add Movie Library

1. Go to **Settings**.

1. Go to **Library**.

   ![](../images/emby/emby-setup-media-libs.png)

1. Click **+ New Library**.

1. Under **Content type**, select **Movies**.

   ![](../images/emby/emby-new-library.png)

   ![](../images/emby/emby-new-library-movie-name.png)

1. Click **+** next to **Folders**.

1. Type in or choose `/mnt/unionfs/Media/Movies`. Click **OK**.

   _Note: These [paths](../saltbox/basics/paths.md) are for the standard library setup. If you have [customized](../reference/customizing-plex-libs.md) it, use those paths instead._

   ![](../images/emby/emby-new-library-movie-path.png)

2. Click **OK** once more.

### Add TV Shows Library

1. Go to **Settings**.

1. Go to **Library**.

   ![](../images/emby/emby-setup-media-libs.png)

1. Click **+ New Library**.

1. Under **Content type**, select **TV shows**.

   ![](../images/emby/emby-new-library.png)

   ![](../images/emby/emby-new-library-tv-name.png)

1. Click **+** next to **Folders**.

1. Type in or choose `/mnt/unionfs/Media/TV`. Click **OK**.

   _Note: These [paths](../saltbox/basics/paths.md) are for the standard library setup. If you have [customized](../reference/customizing-plex-libs.md) it, use those paths instead._

   ![](../images/emby/emby-new-library-tv-path.png)

2. Click **OK** once more.

## 6. API Key

Instructions below will guide you through creating an API Key for a specific app.

1. Click the **Settings** icon.

2. Under **Advanced**, click **API Keys**.

   ![](../images/emby/emby-new-api-key.png)

3. Click **+ New API Key**.

   ![](../images/emby/emby-new-api-key-name.png)

4. Fill in an **App name** (e.g. Ombi) and click **OK**.

5. You have now have created an **Api Key** for your app.

   ![](../images/emby/emby-new-api-show.png)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `emby_instances`.

    === "Role-level Override"

        Applies to all instances of emby:

        ```yaml
        emby_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `emby2`):

        ```yaml
        emby2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        emby_instances: ["emby"]

        ```

    === "Example"

        ```yaml
        # Type: list
        emby_instances: ["emby", "emby2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: int
        emby_role_config_cache_size: 1024

        ```

    === "Instance-level"

        ```yaml
        # Type: int
        emby2_config_cache_size: 1024

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        emby_role_paths_folder: "{{ emby_name }}"

        # Type: string
        emby_role_paths_location: "{{ server_appdata_path }}/{{ emby_role_paths_folder }}"

        # Type: string
        emby_role_paths_transcodes_location: "{{ transcodes_path }}/{{ emby_role_paths_folder }}"

        # Type: string
        emby_role_paths_config_location: "{{ emby_role_paths_location }}/config/system.xml"

        # Type: string
        emby_role_paths_dlna_xml_location: "{{ emby_role_paths_location }}/config/dlna.xml"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        emby2_paths_folder: "{{ emby_name }}"

        # Type: string
        emby2_paths_location: "{{ server_appdata_path }}/{{ emby_role_paths_folder }}"

        # Type: string
        emby2_paths_transcodes_location: "{{ transcodes_path }}/{{ emby_role_paths_folder }}"

        # Type: string
        emby2_paths_config_location: "{{ emby_role_paths_location }}/config/system.xml"

        # Type: string
        emby2_paths_dlna_xml_location: "{{ emby_role_paths_location }}/config/dlna.xml"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        emby_role_web_subdomain: "{{ emby_name }}"

        # Type: string
        emby_role_web_domain: "{{ user.domain }}"

        # Type: string
        emby_role_web_port: "8096"

        # Type: string
        emby_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='emby') + '.' + lookup('role_var', '_web_domain', role='emby')
                            if (lookup('role_var', '_web_subdomain', role='emby') | length > 0)
                            else lookup('role_var', '_web_domain', role='emby')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        emby2_web_subdomain: "{{ emby_name }}"

        # Type: string
        emby2_web_domain: "{{ user.domain }}"

        # Type: string
        emby2_web_port: "8096"

        # Type: string
        emby2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='emby') + '.' + lookup('role_var', '_web_domain', role='emby')
                        if (lookup('role_var', '_web_subdomain', role='emby') | length > 0)
                        else lookup('role_var', '_web_domain', role='emby')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        emby_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='emby') }}"

        # Type: string
        emby_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='emby') }}"

        # Type: bool (true/false)
        emby_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        emby2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='emby') }}"

        # Type: string
        emby2_dns_zone: "{{ lookup('role_var', '_web_domain', role='emby') }}"

        # Type: bool (true/false)
        emby2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        emby_role_traefik_sso_middleware: ""

        # Type: string
        emby_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                  + (',themepark-' + emby_name
                                                    if (lookup('role_var', '_themepark_enabled', role='emby') and global_themepark_plugin_enabled)
                                                    else '') }}"

        # Type: string
        emby_role_traefik_middleware_custom: ""

        # Type: string
        emby_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        emby_role_traefik_enabled: true

        # Type: bool (true/false)
        emby_role_traefik_gzip_enabled: false

        # Type: bool (true/false)
        emby_role_traefik_api_enabled: false

        # Type: string
        emby_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        emby2_traefik_sso_middleware: ""

        # Type: string
        emby2_traefik_middleware_default: "{{ traefik_default_middleware
                                              + (',themepark-' + emby_name
                                                if (lookup('role_var', '_themepark_enabled', role='emby') and global_themepark_plugin_enabled)
                                                else '') }}"

        # Type: string
        emby2_traefik_middleware_custom: ""

        # Type: string
        emby2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        emby2_traefik_enabled: true

        # Type: bool (true/false)
        emby2_traefik_gzip_enabled: false

        # Type: bool (true/false)
        emby2_traefik_api_enabled: false

        # Type: string
        emby2_traefik_api_endpoint: ""

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        emby_role_themepark_enabled: false

        # Type: string
        emby_role_themepark_app: "emby"

        # Type: string
        emby_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        emby_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        emby_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        emby2_themepark_enabled: false

        # Type: string
        emby2_themepark_app: "emby"

        # Type: string
        emby2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        emby2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        emby2_themepark_addons: []

        ```

??? example "Config"

    === "Role-level"

        ```yaml
        # Type: list
        emby_role_config_settings_default: 
          - { xpath: 'IsBehindProxy', value: 'true' }
          - { xpath: 'WanDdns', value: '{{ lookup("role_var", "_web_subdomain", role="emby") }}.{{ lookup("role_var", "_web_domain", role="emby") }}' }
          - { xpath: 'PublicPort', value: '80' }
          - { xpath: 'PublicHttpsPort', value: '443' }
          - { xpath: 'EnableHttps', value: 'true' }
          - { xpath: 'RequireHttps', value: 'false' }
          - { xpath: 'EnableUPnP', value: 'false' }
          - { xpath: 'DatabaseCacheSizeMB', value: '{{ lookup("role_var", "_config_cache_size", role="emby") | string }}' }

        # Type: list
        emby_role_config_settings_custom: []

        # Type: string
        emby_role_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='emby') + lookup('role_var', '_config_settings_custom', role='emby') }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: list
        emby2_config_settings_default: 
          - { xpath: 'IsBehindProxy', value: 'true' }
          - { xpath: 'WanDdns', value: '{{ lookup("role_var", "_web_subdomain", role="emby") }}.{{ lookup("role_var", "_web_domain", role="emby") }}' }
          - { xpath: 'PublicPort', value: '80' }
          - { xpath: 'PublicHttpsPort', value: '443' }
          - { xpath: 'EnableHttps', value: 'true' }
          - { xpath: 'RequireHttps', value: 'false' }
          - { xpath: 'EnableUPnP', value: 'false' }
          - { xpath: 'DatabaseCacheSizeMB', value: '{{ lookup("role_var", "_config_cache_size", role="emby") | string }}' }

        # Type: list
        emby2_config_settings_custom: []

        # Type: string
        emby2_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='emby') + lookup('role_var', '_config_settings_custom', role='emby') }}"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        emby_role_docker_container: "{{ emby_name }}"

        # Image
        # Type: bool (true/false)
        emby_role_docker_image_pull: true

        # Type: string
        emby_role_docker_image_repo: "lscr.io/linuxserver/emby"

        # Type: string
        emby_role_docker_image_tag: "latest"

        # Type: string
        emby_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='emby') }}:{{ lookup('role_var', '_docker_image_tag', role='emby') }}"

        # Envs
        # Type: dict
        emby_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"

        # Type: dict
        emby_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        emby_role_docker_volumes_default: 
          - "{{ emby_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ emby_role_paths_transcodes_location }}:/transcode"

        # Type: list
        emby_role_docker_volumes_legacy: 
          - "/mnt/unionfs/Media:/data"

        # Type: list
        emby_role_docker_volumes_custom: []

        # Mounts
        # Type: list
        emby_role_docker_mounts_default: 
          - target: /tmp
            type: tmpfs

        # Type: list
        emby_role_docker_mounts_custom: []

        # Labels
        # Type: dict
        emby_role_docker_labels_default: {}

        # Type: dict
        emby_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        emby_role_docker_hostname: "{{ emby_name }}"

        # Networks
        # Type: string
        emby_role_docker_networks_alias: "{{ emby_name }}"

        # Type: list
        emby_role_docker_networks_default: []

        # Type: list
        emby_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        emby_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        emby_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        emby_role_docker_blkio_weight:

        # Type: int
        emby_role_docker_cpu_period:

        # Type: int
        emby_role_docker_cpu_quota:

        # Type: int
        emby_role_docker_cpu_shares:

        # Type: string
        emby_role_docker_cpus:

        # Type: string
        emby_role_docker_cpuset_cpus:

        # Type: string
        emby_role_docker_cpuset_mems:

        # Type: string
        emby_role_docker_kernel_memory:

        # Type: string
        emby_role_docker_memory:

        # Type: string
        emby_role_docker_memory_reservation:

        # Type: string
        emby_role_docker_memory_swap:

        # Type: int
        emby_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        emby_role_docker_cap_drop:

        # Type: list
        emby_role_docker_device_cgroup_rules:

        # Type: list
        emby_role_docker_device_read_bps:

        # Type: list
        emby_role_docker_device_read_iops:

        # Type: list
        emby_role_docker_device_requests:

        # Type: list
        emby_role_docker_device_write_bps:

        # Type: list
        emby_role_docker_device_write_iops:

        # Type: list
        emby_role_docker_devices:

        # Type: string
        emby_role_docker_devices_default:

        # Type: bool (true/false)
        emby_role_docker_privileged:

        # Type: list
        emby_role_docker_security_opts:

        # Networking
        # Type: list
        emby_role_docker_dns_opts:

        # Type: list
        emby_role_docker_dns_search_domains:

        # Type: list
        emby_role_docker_dns_servers:

        # Type: dict
        emby_role_docker_hosts:

        # Type: string
        emby_role_docker_hosts_use_common:

        # Type: string
        emby_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        emby_role_docker_keep_volumes:

        # Type: string
        emby_role_docker_volume_driver:

        # Type: list
        emby_role_docker_volumes_from:

        # Type: string
        emby_role_docker_volumes_global:

        # Type: string
        emby_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        emby_role_docker_healthcheck:

        # Type: bool (true/false)
        emby_role_docker_init:

        # Type: string
        emby_role_docker_log_driver:

        # Type: dict
        emby_role_docker_log_options:

        # Type: bool (true/false)
        emby_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        emby_role_docker_auto_remove:

        # Type: list
        emby_role_docker_capabilities:

        # Type: string
        emby_role_docker_cgroup_parent:

        # Type: string
        emby_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        emby_role_docker_cleanup:

        # Type: list
        emby_role_docker_commands:

        # Type: string
        emby_role_docker_create_timeout:

        # Type: string
        emby_role_docker_domainname:

        # Type: string
        emby_role_docker_entrypoint:

        # Type: string
        emby_role_docker_env_file:

        # Type: list
        emby_role_docker_exposed_ports:

        # Type: string
        emby_role_docker_force_kill:

        # Type: list
        emby_role_docker_groups:

        # Type: int
        emby_role_docker_healthy_wait_timeout:

        # Type: string
        emby_role_docker_ipc_mode:

        # Type: string
        emby_role_docker_kill_signal:

        # Type: string
        emby_role_docker_labels_use_common:

        # Type: list
        emby_role_docker_links:

        # Type: bool (true/false)
        emby_role_docker_oom_killer:

        # Type: int
        emby_role_docker_oom_score_adj:

        # Type: bool (true/false)
        emby_role_docker_paused:

        # Type: string
        emby_role_docker_pid_mode:

        # Type: list
        emby_role_docker_ports:

        # Type: bool (true/false)
        emby_role_docker_read_only:

        # Type: bool (true/false)
        emby_role_docker_recreate:

        # Type: int
        emby_role_docker_restart_retries:

        # Type: string
        emby_role_docker_runtime:

        # Type: string
        emby_role_docker_shm_size:

        # Type: int
        emby_role_docker_stop_timeout:

        # Type: dict
        emby_role_docker_storage_opts:

        # Type: list
        emby_role_docker_sysctls:

        # Type: list
        emby_role_docker_tmpfs:

        # Type: list
        emby_role_docker_ulimits:

        # Type: string
        emby_role_docker_user:

        # Type: string
        emby_role_docker_userns_mode:

        # Type: string
        emby_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        emby2_docker_container: "{{ emby_name }}"

        # Image
        # Type: bool (true/false)
        emby2_docker_image_pull: true

        # Type: string
        emby2_docker_image_repo: "lscr.io/linuxserver/emby"

        # Type: string
        emby2_docker_image_tag: "latest"

        # Type: string
        emby2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='emby') }}:{{ lookup('role_var', '_docker_image_tag', role='emby') }}"

        # Envs
        # Type: dict
        emby2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"

        # Type: dict
        emby2_docker_envs_custom: {}

        # Volumes
        # Type: list
        emby2_docker_volumes_default: 
          - "{{ emby_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ emby_role_paths_transcodes_location }}:/transcode"

        # Type: list
        emby2_docker_volumes_legacy: 
          - "/mnt/unionfs/Media:/data"

        # Type: list
        emby2_docker_volumes_custom: []

        # Mounts
        # Type: list
        emby2_docker_mounts_default: 
          - target: /tmp
            type: tmpfs

        # Type: list
        emby2_docker_mounts_custom: []

        # Labels
        # Type: dict
        emby2_docker_labels_default: {}

        # Type: dict
        emby2_docker_labels_custom: {}

        # Hostname
        # Type: string
        emby2_docker_hostname: "{{ emby_name }}"

        # Networks
        # Type: string
        emby2_docker_networks_alias: "{{ emby_name }}"

        # Type: list
        emby2_docker_networks_default: []

        # Type: list
        emby2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        emby2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        emby2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        emby2_docker_blkio_weight:
        # Type: int
        emby2_docker_cpu_period:
        # Type: int
        emby2_docker_cpu_quota:
        # Type: int
        emby2_docker_cpu_shares:
        # Type: string
        emby2_docker_cpus:
        # Type: string
        emby2_docker_cpuset_cpus:
        # Type: string
        emby2_docker_cpuset_mems:
        # Type: string
        emby2_docker_kernel_memory:
        # Type: string
        emby2_docker_memory:
        # Type: string
        emby2_docker_memory_reservation:
        # Type: string
        emby2_docker_memory_swap:
        # Type: int
        emby2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        emby2_docker_cap_drop:
        # Type: list
        emby2_docker_device_cgroup_rules:
        # Type: list
        emby2_docker_device_read_bps:
        # Type: list
        emby2_docker_device_read_iops:
        # Type: list
        emby2_docker_device_requests:
        # Type: list
        emby2_docker_device_write_bps:
        # Type: list
        emby2_docker_device_write_iops:
        # Type: list
        emby2_docker_devices:
        # Type: string
        emby2_docker_devices_default:
        # Type: bool (true/false)
        emby2_docker_privileged:
        # Type: list
        emby2_docker_security_opts:

        # Networking
        # Type: list
        emby2_docker_dns_opts:
        # Type: list
        emby2_docker_dns_search_domains:
        # Type: list
        emby2_docker_dns_servers:
        # Type: dict
        emby2_docker_hosts:
        # Type: string
        emby2_docker_hosts_use_common:
        # Type: string
        emby2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        emby2_docker_keep_volumes:
        # Type: string
        emby2_docker_volume_driver:
        # Type: list
        emby2_docker_volumes_from:
        # Type: string
        emby2_docker_volumes_global:
        # Type: string
        emby2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        emby2_docker_healthcheck:
        # Type: bool (true/false)
        emby2_docker_init:
        # Type: string
        emby2_docker_log_driver:
        # Type: dict
        emby2_docker_log_options:
        # Type: bool (true/false)
        emby2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        emby2_docker_auto_remove:
        # Type: list
        emby2_docker_capabilities:
        # Type: string
        emby2_docker_cgroup_parent:
        # Type: string
        emby2_docker_cgroupns_mode:
        # Type: bool (true/false)
        emby2_docker_cleanup:
        # Type: list
        emby2_docker_commands:
        # Type: string
        emby2_docker_create_timeout:
        # Type: string
        emby2_docker_domainname:
        # Type: string
        emby2_docker_entrypoint:
        # Type: string
        emby2_docker_env_file:
        # Type: list
        emby2_docker_exposed_ports:
        # Type: string
        emby2_docker_force_kill:
        # Type: list
        emby2_docker_groups:
        # Type: int
        emby2_docker_healthy_wait_timeout:
        # Type: string
        emby2_docker_ipc_mode:
        # Type: string
        emby2_docker_kill_signal:
        # Type: string
        emby2_docker_labels_use_common:
        # Type: list
        emby2_docker_links:
        # Type: bool (true/false)
        emby2_docker_oom_killer:
        # Type: int
        emby2_docker_oom_score_adj:
        # Type: bool (true/false)
        emby2_docker_paused:
        # Type: string
        emby2_docker_pid_mode:
        # Type: list
        emby2_docker_ports:
        # Type: bool (true/false)
        emby2_docker_read_only:
        # Type: bool (true/false)
        emby2_docker_recreate:
        # Type: int
        emby2_docker_restart_retries:
        # Type: string
        emby2_docker_runtime:
        # Type: string
        emby2_docker_shm_size:
        # Type: int
        emby2_docker_stop_timeout:
        # Type: dict
        emby2_docker_storage_opts:
        # Type: list
        emby2_docker_sysctls:
        # Type: list
        emby2_docker_tmpfs:
        # Type: list
        emby2_docker_ulimits:
        # Type: string
        emby2_docker_user:
        # Type: string
        emby2_docker_userns_mode:
        # Type: string
        emby2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        emby_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        emby_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        emby_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        emby_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        emby_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        emby_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        emby_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        emby_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        emby_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        emby_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        emby_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        emby_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            emby_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "emby2.{{ user.domain }}"
              - "emby.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            emby_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'emby2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

    === "Instance-level"

        Override for a specific instance (e.g., `emby2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        emby2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        emby2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        emby2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        emby2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        emby2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        emby2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        emby2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        emby2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        emby2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        emby2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        emby2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        emby2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        emby2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        emby2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        emby2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        emby2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        emby2_web_scheme:

        ```

        1.  Example:

            ```yaml
            emby2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "emby2.{{ user.domain }}"
              - "emby.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            emby2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'emby2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
