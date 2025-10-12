---
hide:
  - tags
tags:
  - organizr
---

# Organizr

# What is it?

[Organizr](https://organizr.app/) (by CauseFX) is a web-based, HTPC server organizer, that allows you to manage various tools and programs within tabs. Also supports user management, allowing for non admin users or guests to access certain web-pages via Organizr, even if it is behind HTTP authentication. This guide is to help you get Organizr setup and running by no means is this a complete guide to Organizr as you'll see the depth of it is pretty vast and there are plenty of customizations available to you at every turn.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://organizr.app){: .header-icons } | [:octicons-link-16: Docs](https://organizr.app/howtos/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/causefx/Organizr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/organizr/organizr){: .header-icons }|

## 2. URL

- To access Organizr, visit `https://organizr._yourdomain_.com`

## 3. Initial Setup

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

## 4. Settings

1. You will now be taken to the main Organizr Page and asked to login with the credentials you created in the previous steps.

    ![Organizr](https://i.imgur.com/J1rVQQk.png)

### Tabs

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
    | Portainer     | `https://portainer.yourdomain.tld`    | images/organizr.png (default) |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Sonarr        | `https://sonarr.yourdomain.tld`       | images/sonarr.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Radarr        | `https://radarr.yourdomain.tld`       | images/radarr.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | NZBGet        | `https://nzbget.yourdomain.tld`       | images/nzbget.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | qbittorrent     | `https://qbittorrent.yourdomain.tld`    | images/qbittorrent.png          |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | NZBHydra2     | `https://nzbhydra2.yourdomain.tld`    | images/hydra.png              |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Jackett       | `https://jackett.yourdomain.tld`      | images/jackett.png            |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Plex          | `https://plex.yourdomain.tld`         | images/plex.png               |   Unsorted   |  User    |   iFrame   |     Y     |
    | Tautulli      | `https://tautulli.yourdomain.tld`     | images/tautulli.png           |   Unsorted   |  User    |   iFrame   |     Y     |
    | Ombi          | `https://ombi.yourdomain.tld`         | images/ombi.png               |   Unsorted   |  User    |   iFrame   |     Y     |
    | Overseerr     | `https://overseerr.yourdomain.tld`    | images/overseerr.png          |   Unsorted   |  User    |   iFrame   |     Y     |

    ![Tab Editor](https://i.imgur.com/aXwGxpx.png)

- Note: If Sonarr or Radarr are lagging a lot, you may set it to a specific page in each. (e.g. Sonarr: `https://sonarr.yourdomain.com/calendar` ; Radarr: `https://radarr.yourdomain.com/activity/history`)

### Homepage (Make you have Homepage ACTIVE in Tabs section)

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

### Homepage Order

1. This is where you organize the apps and other items and how they will appear on your Homepage.  There's no right or wrong order so simply move things around and find out what works for you.

    ![Homepage Order](https://i.imgur.com/A2FPosN.png)

Any additional question please reach out to the [Organizr](https://organizr.app/) team, either via their [Discord Server](https://organizr.app/discord) or their [subreddit](https://www.reddit.com/r/organizr/)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        organizr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `organizr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `organizr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    organizr_name: organizr

    ```

??? example "Settings"

    ```yaml
    # Type: string
    organizr_branch: "v2-master"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    organizr_role_paths_folder: "{{ organizr_name }}"

    # Type: string
    organizr_role_paths_location: "{{ server_appdata_path }}/{{ organizr_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    organizr_role_web_subdomain: "{{ organizr_name }}"

    # Type: string
    organizr_role_web_domain: "{{ user.domain }}"

    # Type: string
    organizr_role_web_port: "80"

    # Type: string
    organizr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='organizr') + '.' + lookup('role_var', '_web_domain', role='organizr')
                            if (lookup('role_var', '_web_subdomain', role='organizr') | length > 0)
                            else lookup('role_var', '_web_domain', role='organizr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    organizr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='organizr') }}"

    # Type: string
    organizr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='organizr') }}"

    # Type: bool (true/false)
    organizr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    organizr_role_traefik_sso_middleware: ""

    # Type: string
    organizr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    organizr_role_traefik_middleware_custom: ""

    # Type: string
    organizr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    organizr_role_traefik_enabled: true

    # Type: bool (true/false)
    organizr_role_traefik_api_enabled: false

    # Type: string
    organizr_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    organizr_role_docker_container: "{{ organizr_name }}"

    # Image
    # Type: bool (true/false)
    organizr_role_docker_image_pull: true

    # Type: string
    organizr_role_docker_image_repo: "organizr/organizr"

    # Type: string
    organizr_role_docker_image_tag: "latest"

    # Type: string
    organizr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='organizr') }}:{{ lookup('role_var', '_docker_image_tag', role='organizr') }}"

    # Envs
    # Type: dict
    organizr_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      branch: "{{ organizr_branch }}"

    # Type: dict
    organizr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    organizr_role_docker_volumes_default: 
      - "{{ organizr_role_paths_location }}:/config"

    # Type: list
    organizr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    organizr_role_docker_hostname: "{{ organizr_name }}"

    # Networks
    # Type: string
    organizr_role_docker_networks_alias: "{{ organizr_name }}"

    # Type: list
    organizr_role_docker_networks_default: []

    # Type: list
    organizr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    organizr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    organizr_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    organizr_role_docker_blkio_weight:

    # Type: int
    organizr_role_docker_cpu_period:

    # Type: int
    organizr_role_docker_cpu_quota:

    # Type: int
    organizr_role_docker_cpu_shares:

    # Type: string
    organizr_role_docker_cpus:

    # Type: string
    organizr_role_docker_cpuset_cpus:

    # Type: string
    organizr_role_docker_cpuset_mems:

    # Type: string
    organizr_role_docker_kernel_memory:

    # Type: string
    organizr_role_docker_memory:

    # Type: string
    organizr_role_docker_memory_reservation:

    # Type: string
    organizr_role_docker_memory_swap:

    # Type: int
    organizr_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    organizr_role_docker_cap_drop:

    # Type: list
    organizr_role_docker_device_cgroup_rules:

    # Type: list
    organizr_role_docker_device_read_bps:

    # Type: list
    organizr_role_docker_device_read_iops:

    # Type: list
    organizr_role_docker_device_requests:

    # Type: list
    organizr_role_docker_device_write_bps:

    # Type: list
    organizr_role_docker_device_write_iops:

    # Type: list
    organizr_role_docker_devices:

    # Type: string
    organizr_role_docker_devices_default:

    # Type: bool (true/false)
    organizr_role_docker_privileged:

    # Type: list
    organizr_role_docker_security_opts:


    # Networking
    # Type: list
    organizr_role_docker_dns_opts:

    # Type: list
    organizr_role_docker_dns_search_domains:

    # Type: list
    organizr_role_docker_dns_servers:

    # Type: dict
    organizr_role_docker_hosts:

    # Type: string
    organizr_role_docker_hosts_use_common:

    # Type: string
    organizr_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    organizr_role_docker_keep_volumes:

    # Type: list
    organizr_role_docker_mounts:

    # Type: string
    organizr_role_docker_volume_driver:

    # Type: list
    organizr_role_docker_volumes_from:

    # Type: string
    organizr_role_docker_volumes_global:

    # Type: string
    organizr_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    organizr_role_docker_healthcheck:

    # Type: bool (true/false)
    organizr_role_docker_init:

    # Type: string
    organizr_role_docker_log_driver:

    # Type: dict
    organizr_role_docker_log_options:

    # Type: bool (true/false)
    organizr_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    organizr_role_docker_auto_remove:

    # Type: list
    organizr_role_docker_capabilities:

    # Type: string
    organizr_role_docker_cgroup_parent:

    # Type: string
    organizr_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    organizr_role_docker_cleanup:

    # Type: list
    organizr_role_docker_commands:

    # Type: string
    organizr_role_docker_create_timeout:

    # Type: string
    organizr_role_docker_domainname:

    # Type: string
    organizr_role_docker_entrypoint:

    # Type: string
    organizr_role_docker_env_file:

    # Type: list
    organizr_role_docker_exposed_ports:

    # Type: string
    organizr_role_docker_force_kill:

    # Type: list
    organizr_role_docker_groups:

    # Type: int
    organizr_role_docker_healthy_wait_timeout:

    # Type: string
    organizr_role_docker_ipc_mode:

    # Type: string
    organizr_role_docker_kill_signal:

    # Type: dict
    organizr_role_docker_labels:

    # Type: string
    organizr_role_docker_labels_use_common:

    # Type: list
    organizr_role_docker_links:

    # Type: bool (true/false)
    organizr_role_docker_oom_killer:

    # Type: int
    organizr_role_docker_oom_score_adj:

    # Type: bool (true/false)
    organizr_role_docker_paused:

    # Type: string
    organizr_role_docker_pid_mode:

    # Type: list
    organizr_role_docker_ports:

    # Type: bool (true/false)
    organizr_role_docker_read_only:

    # Type: bool (true/false)
    organizr_role_docker_recreate:

    # Type: int
    organizr_role_docker_restart_retries:

    # Type: string
    organizr_role_docker_runtime:

    # Type: string
    organizr_role_docker_shm_size:

    # Type: int
    organizr_role_docker_stop_timeout:

    # Type: dict
    organizr_role_docker_storage_opts:

    # Type: list
    organizr_role_docker_sysctls:

    # Type: list
    organizr_role_docker_tmpfs:

    # Type: list
    organizr_role_docker_ulimits:

    # Type: string
    organizr_role_docker_user:

    # Type: string
    organizr_role_docker_userns_mode:

    # Type: string
    organizr_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    organizr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    organizr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    organizr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    organizr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    organizr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    organizr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    organizr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    organizr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    organizr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    organizr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    organizr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    organizr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    organizr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    organizr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    organizr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    organizr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    organizr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        organizr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "organizr2.{{ user.domain }}"
          - "organizr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        organizr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'organizr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  You're ready to explore Saltbox! You can start checking out community apps in [Sandbox](../sandbox/basics.md) if you wish.
