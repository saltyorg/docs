---
icon: material/docker
status: Outdated
hide:
  - tags
tags:
  - organizr
---

# Organizr

## Overview

[Organizr](https://organizr.app/) (by CauseFX) is a web-based, HTPC server organizer, that allows you to manage various tools and programs within tabs. Also supports user management, allowing for non admin users or guests to access certain web-pages via Organizr, even if it is behind HTTP authentication. This guide is to help you get Organizr setup and running by no means is this a complete guide to Organizr as you'll see the depth of it is pretty vast and there are plenty of customizations available to you at every turn.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://organizr.app){: .header-icons } | [:octicons-link-16: Docs](https://organizr.app/howtos/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/causefx/Organizr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/organizr/organizr){: .header-icons }|

---

## Usage

To access Organizr, visit <https://organizr.iYOUR_DOMAIN_NAMEi>

## Basics

### 3. Initial Setup

1. The first time you go to the Organizr page, you will be presented with `Install Type`, `Admin Info`, `Security`, `Database` and `Verify` sections.
In the `Install Type` section select `Personal`

    ![Main Setup-Install-Type](https://i.imgur.com/IgStX3L.png)

1. In the `Admin Info` section enter your details such as the preferred password to log in and personal email.
Note: it is suggested to enter your `plex username and password`

    ![Main Setup-Admin-Info](https://i.imgur.com/clOLSdn.png)

1. In the `Security` section enter your fill in the `Hash Key` and `Registration Password` any type of password will do but if you want a secure one then follow these steps;

- First for the `Hash Key` you can head over to [Base64 Encode](https://www.cleancss.com/base64-encode/) and convert a string to Base64. Keep in mind the `Hash Key` can be anywhere between 3 to 30 which mean you can enter string up to 21 characters in Base64

- For the password just use any strong password you prefer, if you want a strong one then [Password Generator](https://passwordsgenerator.net/), there is no limit on the password section go crazy ;)
- The API key should be auto-generated so no need to worry about this if the API key is throwing an error such as shorter than it suppose to be or longer it's most likely due to the web browser auto-fill, make sure it's disabled or just use another browser that doesn't have auto-fill or you don't use much e.g Internet Explorer 👀.
<br> <br>You should have something like this:

   ![Main Setup-Admin-Info](https://i.imgur.com/o7yp3YQ.png)

4. In the `Database` section enter your preferred database name (there is 30 character limit), then after that for the "Database Location" set it as `/config/www` then click test path it should be a success.
<br> <br>You should have something like this:

   ![Main Setup-Database](https://i.imgur.com/kJlIRpY.png)

5. In the `Verify` section you will just need to confirm everything but feel free to take note of your **API** key and save it somewhere safe. After clicking finish you will be taken to a log in the page just enter the `username` and `password` you have inserted in the `Admin info` section.
<br> <br>You should have something like this:

   ![Main Setup-Database](https://i.imgur.com/wbOhf12.png)

### 4. Settings

1. You will now be taken to the main Organizr Page and asked to login with the credentials you created in the previous steps.

    ![Organizr](https://i.imgur.com/J1rVQQk.png)

#### Tabs

1. Click "Settings" on the left menu, to be taken to the "Organizr Settings" page.

    ![Settings Tab](https://i.imgur.com/M7wfb1z.png)
    ![Tabs Editor](https://i.imgur.com/DJIvrh2.png)

1. Things to note on this page, the Homepage is disabled by default and note the "Type" is set to "Internal".  Your normal Apps with Saltbox will all need to have a Type: "iFrame" unless you have a particular app you wish to open in another window which is also a Type option.  Go ahead and click "+ on the right". You will be prompted for information regarding the tab.

    ![](https://i.imgur.com/KiXsQUI.png)

1. Before hitting the Edit Tab button in the bottom right, please hit the "Test Tab" button, sometimes the Tab will check for you if iFrame is possible.  This will test if the information you inputted can be open in an iFrame.  Which is the secret sauce in Organizr's tabbed browsing.

    ![New Tab](https://i.imgur.com/7UyBDAA.png)

1. You will need to create multiple tabs with the information below. These are merely a suggestion and examples to get you up and going.  Any changes made, won't be reflected until Organizr is reloaded. You can also drag and drop to change the order of the apps (don't forget to reload)

    | Tab Name      | Tab URL                             | Icon URL                      | Category | Group | Type | Active |
    | ------------- | ----------------------------------- | ----------------------------- |:------:|:----:|:-----:|:---------:|
    | Portainer     | <https://portainer.iYOUR_DOMAIN_NAMEi>    | images/organizr.png (default) |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Sonarr        | <https://sonarr.iYOUR_DOMAIN_NAMEi>       | images/sonarr.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Radarr        | <https://radarr.iYOUR_DOMAIN_NAMEi>       | images/radarr.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | NZBGet        | <https://nzbget.iYOUR_DOMAIN_NAMEi>       | images/nzbget.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | qbittorrent     | <https://qbittorrent.iYOUR_DOMAIN_NAMEi>    | images/qbittorrent.png          |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | NZBHydra2     | <https://nzbhydra2.iYOUR_DOMAIN_NAMEi>    | images/hydra.png              |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Jackett       | <https://jackett.iYOUR_DOMAIN_NAMEi>      | images/jackett.png            |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Plex          | <https://plex.iYOUR_DOMAIN_NAMEi>         | images/plex.png               |   Unsorted   |  User    |   iFrame   |     Y     |
    | Tautulli      | <https://tautulli.iYOUR_DOMAIN_NAMEi>     | images/tautulli.png           |   Unsorted   |  User    |   iFrame   |     Y     |
    | Ombi          | <https://ombi.iYOUR_DOMAIN_NAMEi>         | images/ombi.png               |   Unsorted   |  User    |   iFrame   |     Y     |
    | Overseerr     | <https://overseerr.iYOUR_DOMAIN_NAMEi>    | images/overseerr.png          |   Unsorted   |  User    |   iFrame   |     Y     |

    ![Tab Editor](https://i.imgur.com/aXwGxpx.png)

- Note: If Sonarr or Radarr are lagging a lot, you may set it to a specific page in each. (e.g. Sonarr: <https://sonarr.iYOUR_DOMAIN_NAMEi/calendar> ; Radarr: <https://radarr.iYOUR_DOMAIN_NAMEi/activity/history>)

#### Homepage (Make you have Homepage ACTIVE in Tabs section)

1. Click "Homepage Items" under the Tab Editor section, to be taken to the "Homepage Items" page.

    ![Edit Homepage](https://i.imgur.com/v0rz7Ap.png)

1. Click the Plex icon at the top.

    - You'll have to Enable it and verify the Minimum Authentication

    - Click on the Connection Tab and set "Plex URL": `http://plex:32400`

    - Click "Retrieve" under Get Plex Token
    - Click "Save" icon at the top right
    - Set your preferred options on the remaining tabs

    - Click "SAVE".

    ![  ](https://i.imgur.com/c84B5td.png)

1. Click the Sonarr icon at the top.

    - Enable it.

    - On the Connections Tab, Set "Sonarr URL": `http://sonarr:8989`

    - Set "Sonarr API Key": [[Your Sonarr API Key|Install: Sonarr#9-retrieving-the-api-key]]

    - Go over any other Miscellaneous Options on the next Tab and set your preferences.

    - Click "SAVE".

    ![  ](https://i.imgur.com/04b5Xmb.png)

1. Click the Radarr icon at the top.

    - Enable it.

    - Set "Radarr URL": `http://radarr:7878`

    - Set "Radarr API Key": [[Your Radarr API Key|Install: Radarr#9-retrieving-the-api-key]]

    - Go over any other Miscellaneous Options on the next Tab and set your preferences.

    - Click "SAVE".

    ![  ](https://i.imgur.com/0S1erVG.png)

1. Click the NZBGet icon at the top.

    - Enable it.

    - Set "NZBGet URL": `http://nzbget:6789`

    - For "Username" / "Password": fill in your NZBGet login (see [[NZBGet|Install: NZBGet#2-setup]])

    - Click "SAVE".

    ![  ](https://i.imgur.com/MRzv0Sa.png)

#### Homepage Order

1. This is where you organize the apps and other items and how they will appear on your Homepage.  There's no right or wrong order so simply move things around and find out what works for you.

    ![Homepage Order](https://i.imgur.com/A2FPosN.png)

Any additional question please reach out to the [Organizr](https://organizr.app/) team, either via their [Discord Server](https://organizr.app/discord) or their [subreddit](https://www.reddit.com/r/organizr/)

## Next


<div class="sb-directions-row" markdown>

Are you setting Saltbox up for the first time?

You're ready to explore Saltbox! You can start checking out community apps if you wish.

[Continue to Sandbox :material-forward:](../sandbox/basics.md){ .md-button }

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    organizr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `organizr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `organizr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`organizr_name`"

        ```yaml
        # Type: string
        organizr_name: organizr
        ```

=== "Settings"

    ??? variable string "`organizr_branch`"

        ```yaml
        # Type: string
        organizr_branch: "v2-master"
        ```

=== "Paths"

    ??? variable string "`organizr_role_paths_folder`"

        ```yaml
        # Type: string
        organizr_role_paths_folder: "{{ organizr_name }}"
        ```

    ??? variable string "`organizr_role_paths_location`"

        ```yaml
        # Type: string
        organizr_role_paths_location: "{{ server_appdata_path }}/{{ organizr_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`organizr_role_web_subdomain`"

        ```yaml
        # Type: string
        organizr_role_web_subdomain: "{{ organizr_name }}"
        ```

    ??? variable string "`organizr_role_web_domain`"

        ```yaml
        # Type: string
        organizr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`organizr_role_web_port`"

        ```yaml
        # Type: string
        organizr_role_web_port: "80"
        ```

    ??? variable string "`organizr_role_web_url`"

        ```yaml
        # Type: string
        organizr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='organizr') + '.' + lookup('role_var', '_web_domain', role='organizr')
                                if (lookup('role_var', '_web_subdomain', role='organizr') | length > 0)
                                else lookup('role_var', '_web_domain', role='organizr')) }}"
        ```

=== "DNS"

    ??? variable string "`organizr_role_dns_record`"

        ```yaml
        # Type: string
        organizr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='organizr') }}"
        ```

    ??? variable string "`organizr_role_dns_zone`"

        ```yaml
        # Type: string
        organizr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='organizr') }}"
        ```

    ??? variable bool "`organizr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`organizr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        organizr_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`organizr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        organizr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`organizr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        organizr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`organizr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        organizr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`organizr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_traefik_enabled: true
        ```

    ??? variable bool "`organizr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_traefik_api_enabled: false
        ```

    ??? variable string "`organizr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        organizr_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`organizr_role_docker_container`"

        ```yaml
        # Type: string
        organizr_role_docker_container: "{{ organizr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`organizr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_image_pull: true
        ```

    ??? variable string "`organizr_role_docker_image_repo`"

        ```yaml
        # Type: string
        organizr_role_docker_image_repo: "organizr/organizr"
        ```

    ??? variable string "`organizr_role_docker_image_tag`"

        ```yaml
        # Type: string
        organizr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`organizr_role_docker_image`"

        ```yaml
        # Type: string
        organizr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='organizr') }}:{{ lookup('role_var', '_docker_image_tag', role='organizr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`organizr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        organizr_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          branch: "{{ organizr_branch }}"
        ```

    ??? variable dict "`organizr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        organizr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`organizr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        organizr_role_docker_volumes_default: 
          - "{{ organizr_role_paths_location }}:/config"
        ```

    ??? variable list "`organizr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        organizr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`organizr_role_docker_hostname`"

        ```yaml
        # Type: string
        organizr_role_docker_hostname: "{{ organizr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`organizr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        organizr_role_docker_networks_alias: "{{ organizr_name }}"
        ```

    ??? variable list "`organizr_role_docker_networks_default`"

        ```yaml
        # Type: list
        organizr_role_docker_networks_default: []
        ```

    ??? variable list "`organizr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        organizr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`organizr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        organizr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`organizr_role_docker_state`"

        ```yaml
        # Type: string
        organizr_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`organizr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        organizr_role_docker_blkio_weight:
        ```

    ??? variable int "`organizr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        organizr_role_docker_cpu_period:
        ```

    ??? variable int "`organizr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        organizr_role_docker_cpu_quota:
        ```

    ??? variable int "`organizr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        organizr_role_docker_cpu_shares:
        ```

    ??? variable string "`organizr_role_docker_cpus`"

        ```yaml
        # Type: string
        organizr_role_docker_cpus:
        ```

    ??? variable string "`organizr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        organizr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`organizr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        organizr_role_docker_cpuset_mems:
        ```

    ??? variable string "`organizr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        organizr_role_docker_kernel_memory:
        ```

    ??? variable string "`organizr_role_docker_memory`"

        ```yaml
        # Type: string
        organizr_role_docker_memory:
        ```

    ??? variable string "`organizr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        organizr_role_docker_memory_reservation:
        ```

    ??? variable string "`organizr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        organizr_role_docker_memory_swap:
        ```

    ??? variable int "`organizr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        organizr_role_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`organizr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        organizr_role_docker_cap_drop:
        ```

    ??? variable list "`organizr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        organizr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`organizr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        organizr_role_docker_device_read_bps:
        ```

    ??? variable list "`organizr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        organizr_role_docker_device_read_iops:
        ```

    ??? variable list "`organizr_role_docker_device_requests`"

        ```yaml
        # Type: list
        organizr_role_docker_device_requests:
        ```

    ??? variable list "`organizr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        organizr_role_docker_device_write_bps:
        ```

    ??? variable list "`organizr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        organizr_role_docker_device_write_iops:
        ```

    ??? variable list "`organizr_role_docker_devices`"

        ```yaml
        # Type: list
        organizr_role_docker_devices:
        ```

    ??? variable string "`organizr_role_docker_devices_default`"

        ```yaml
        # Type: string
        organizr_role_docker_devices_default:
        ```

    ??? variable bool "`organizr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_privileged:
        ```

    ??? variable list "`organizr_role_docker_security_opts`"

        ```yaml
        # Type: list
        organizr_role_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`organizr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        organizr_role_docker_dns_opts:
        ```

    ??? variable list "`organizr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        organizr_role_docker_dns_search_domains:
        ```

    ??? variable list "`organizr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        organizr_role_docker_dns_servers:
        ```

    ??? variable dict "`organizr_role_docker_hosts`"

        ```yaml
        # Type: dict
        organizr_role_docker_hosts:
        ```

    ??? variable string "`organizr_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        organizr_role_docker_hosts_use_common:
        ```

    ??? variable string "`organizr_role_docker_network_mode`"

        ```yaml
        # Type: string
        organizr_role_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`organizr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_keep_volumes:
        ```

    ??? variable list "`organizr_role_docker_mounts`"

        ```yaml
        # Type: list
        organizr_role_docker_mounts:
        ```

    ??? variable string "`organizr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        organizr_role_docker_volume_driver:
        ```

    ??? variable list "`organizr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        organizr_role_docker_volumes_from:
        ```

    ??? variable string "`organizr_role_docker_volumes_global`"

        ```yaml
        # Type: string
        organizr_role_docker_volumes_global:
        ```

    ??? variable string "`organizr_role_docker_working_dir`"

        ```yaml
        # Type: string
        organizr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`organizr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        organizr_role_docker_healthcheck:
        ```

    ??? variable bool "`organizr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_init:
        ```

    ??? variable string "`organizr_role_docker_log_driver`"

        ```yaml
        # Type: string
        organizr_role_docker_log_driver:
        ```

    ??? variable dict "`organizr_role_docker_log_options`"

        ```yaml
        # Type: dict
        organizr_role_docker_log_options:
        ```

    ??? variable bool "`organizr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`organizr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_auto_remove:
        ```

    ??? variable list "`organizr_role_docker_capabilities`"

        ```yaml
        # Type: list
        organizr_role_docker_capabilities:
        ```

    ??? variable string "`organizr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        organizr_role_docker_cgroup_parent:
        ```

    ??? variable string "`organizr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        organizr_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`organizr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_cleanup:
        ```

    ??? variable list "`organizr_role_docker_commands`"

        ```yaml
        # Type: list
        organizr_role_docker_commands:
        ```

    ??? variable string "`organizr_role_docker_create_timeout`"

        ```yaml
        # Type: string
        organizr_role_docker_create_timeout:
        ```

    ??? variable string "`organizr_role_docker_domainname`"

        ```yaml
        # Type: string
        organizr_role_docker_domainname:
        ```

    ??? variable string "`organizr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        organizr_role_docker_entrypoint:
        ```

    ??? variable string "`organizr_role_docker_env_file`"

        ```yaml
        # Type: string
        organizr_role_docker_env_file:
        ```

    ??? variable list "`organizr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        organizr_role_docker_exposed_ports:
        ```

    ??? variable string "`organizr_role_docker_force_kill`"

        ```yaml
        # Type: string
        organizr_role_docker_force_kill:
        ```

    ??? variable list "`organizr_role_docker_groups`"

        ```yaml
        # Type: list
        organizr_role_docker_groups:
        ```

    ??? variable int "`organizr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        organizr_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`organizr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        organizr_role_docker_ipc_mode:
        ```

    ??? variable string "`organizr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        organizr_role_docker_kill_signal:
        ```

    ??? variable dict "`organizr_role_docker_labels`"

        ```yaml
        # Type: dict
        organizr_role_docker_labels:
        ```

    ??? variable string "`organizr_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        organizr_role_docker_labels_use_common:
        ```

    ??? variable list "`organizr_role_docker_links`"

        ```yaml
        # Type: list
        organizr_role_docker_links:
        ```

    ??? variable bool "`organizr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_oom_killer:
        ```

    ??? variable int "`organizr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        organizr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`organizr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_paused:
        ```

    ??? variable string "`organizr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        organizr_role_docker_pid_mode:
        ```

    ??? variable list "`organizr_role_docker_ports`"

        ```yaml
        # Type: list
        organizr_role_docker_ports:
        ```

    ??? variable bool "`organizr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_read_only:
        ```

    ??? variable bool "`organizr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_docker_recreate:
        ```

    ??? variable int "`organizr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        organizr_role_docker_restart_retries:
        ```

    ??? variable string "`organizr_role_docker_runtime`"

        ```yaml
        # Type: string
        organizr_role_docker_runtime:
        ```

    ??? variable string "`organizr_role_docker_shm_size`"

        ```yaml
        # Type: string
        organizr_role_docker_shm_size:
        ```

    ??? variable int "`organizr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        organizr_role_docker_stop_timeout:
        ```

    ??? variable dict "`organizr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        organizr_role_docker_storage_opts:
        ```

    ??? variable list "`organizr_role_docker_sysctls`"

        ```yaml
        # Type: list
        organizr_role_docker_sysctls:
        ```

    ??? variable list "`organizr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        organizr_role_docker_tmpfs:
        ```

    ??? variable list "`organizr_role_docker_ulimits`"

        ```yaml
        # Type: list
        organizr_role_docker_ulimits:
        ```

    ??? variable string "`organizr_role_docker_user`"

        ```yaml
        # Type: string
        organizr_role_docker_user:
        ```

    ??? variable string "`organizr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        organizr_role_docker_userns_mode:
        ```

    ??? variable string "`organizr_role_docker_uts`"

        ```yaml
        # Type: string
        organizr_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`organizr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        organizr_role_autoheal_enabled: true
        ```

    ??? variable string "`organizr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        organizr_role_depends_on: ""
        ```

    ??? variable string "`organizr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        organizr_role_depends_on_delay: "0"
        ```

    ??? variable string "`organizr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        organizr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`organizr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        organizr_role_diun_enabled: true
        ```

    ??? variable bool "`organizr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        organizr_role_dns_enabled: true
        ```

    ??? variable bool "`organizr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        organizr_role_docker_controller: true
        ```

    ??? variable bool "`organizr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        organizr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`organizr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        organizr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`organizr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        organizr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`organizr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        organizr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`organizr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`organizr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        organizr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`organizr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        organizr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`organizr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        organizr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`organizr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        organizr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`organizr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        organizr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            organizr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "organizr2.{{ user.domain }}"
              - "organizr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`organizr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        organizr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            organizr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'organizr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`organizr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        organizr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->