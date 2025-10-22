---
hide:
  - tags
tags:
  - notifiarr
  - discord
  - notifications
---

# Notifiarr Client

## What is it?

[Notifiarr Client](https://notifiarr.com/) is the unified client for Notifiarr.com. The client enables content requests from Media Bot in your Discord Server. It also provides reports for Plex usage and system health. Other features can be [configured on the Notifiarr website.](https://notifiarr.com/)

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://notifiarr.com/){: .header-icons } | [:octicons-link-16: Docs](https://notifiarr.wiki/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Notifiarr/notifiarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/golift/notifiarr){: .header-icons }|

### 1. Setup

You will need a Notifiarr account api key to use Notifiarr. You can get one by [signing up for a free account.](https://notifiarr.com/guest/register){: .header-icons }

After logging in, you should be redirected to your profile screen.

- Click on Generate API Key (This needs to be done)
- Select your Country
- Select your Timezone
- Change your Time Format to your liking
- Select your Notification Language
- **Don't forget to Save your changes**

Add your API key to the **[Sandbox settings file](../../sandbox/settings.md)**

You also need to define a username and password for the Notifiarr client webui in the [Sandbox settings file](../../sandbox/settings.md). You can review the password requirements [here](https://github.com/Notifiarr/notifiarr#webui).

### 2. Installation

``` shell

sb install sandbox-notifiarr

```

### 3. URL

- The Notifiarr url will only display the app status `https://notifiarr.xDOMAIN_NAMEx`

Now go to the Notifiarr website and configure your integrations and discord server.
Refer to the [Notifiarr documentation](https://notifiarr.wiki/) for more information.

The role will attempt to configure Sonarr, Radarr, Plex, and Tautulli. Other apps can be edited in the config file which can be found at `"/opt/notifiarr/notifiarr.conf"` in a standard install. From time to time new options will be added and an [example config file can be found here.](https://github.com/Notifiarr/notifiarr/blob/main/examples/notifiarr.conf.example)

A guide to setup and sync TRaSH guides with Radarr and Sonarr can be found on the [TRaSH Guides website](https://trash-guides.info/Guide-Sync/).

## Advanced

### Snapshot Feature Support

1. Add the following to your Inventory file to enable Privileged mode for Notifiarr and allow it access to system information

     ```yaml
     notifiarr_privileged: true
     ```

2. Run the Notifiarr role:

      ```shell
      sb install sandbox-notifiarr
      ```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        notifiarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `notifiarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `notifiarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    notifiarr_name: notifiarr

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    notifiarr_role_privileged: false

    ```

??? example "Paths"

    ```yaml
    # Type: string
    notifiarr_role_paths_folder: "{{ notifiarr_name }}"

    # Type: string
    notifiarr_role_paths_location: "{{ server_appdata_path }}/{{ notifiarr_role_paths_folder }}"

    # Type: bool (true/false)
    notifiarr_role_paths_recursive: true

    # Type: string
    notifiarr_role_paths_config_location: "{{ notifiarr_role_paths_location }}/notifiarr.conf"

    # Type: string
    notifiarr_role_radarr_config: "{{ lookup('role_var', '_paths_location', role='radarr') }}/config.xml"

    # Type: string
    notifiarr_role_sonarr_config: "{{ lookup('role_var', '_paths_location', role='sonarr') }}/config.xml"

    # Type: string
    notifiarr_role_tautulli_config: "{{ lookup('role_var', '_paths_location', role='tautulli') }}/config.ini"

    # Type: string
    notifiarr_role_tautulli_api_key: "{{ lookup('ini', 'api_key section=General file=' ~ lookup('role_var', '_tautulli_config', role='notifiarr')) if notifiarr_tautulli_config_stat.stat.exists else '' }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    notifiarr_role_web_subdomain: "{{ notifiarr_name }}"

    # Type: string
    notifiarr_role_web_domain: "{{ user.domain }}"

    # Type: string
    notifiarr_role_web_port: "5454"

    # Type: string
    notifiarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='notifiarr') + '.' + lookup('role_var', '_web_domain', role='notifiarr')
                             if (lookup('role_var', '_web_subdomain', role='notifiarr') | length > 0)
                             else lookup('role_var', '_web_domain', role='notifiarr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    notifiarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='notifiarr') }}"

    # Type: string
    notifiarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='notifiarr') }}"

    # Type: bool (true/false)
    notifiarr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    notifiarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    notifiarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    notifiarr_role_traefik_middleware_custom: ""

    # Type: string
    notifiarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    notifiarr_role_traefik_enabled: true

    # Type: bool (true/false)
    notifiarr_role_traefik_api_enabled: true

    # Type: string
    notifiarr_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/plex`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    notifiarr_role_docker_container: "{{ notifiarr_name }}"

    # Image
    # Type: bool (true/false)
    notifiarr_role_docker_image_pull: true

    # Type: string
    notifiarr_role_docker_image_tag: "latest"

    # Type: string
    notifiarr_role_docker_image_repo: "golift/notifiarr"

    # Type: string
    notifiarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='notifiarr') }}:{{ lookup('role_var', '_docker_image_tag', role='notifiarr') }}"

    # Envs
    # Type: dict
    notifiarr_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    notifiarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    notifiarr_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='notifiarr') }}:/config"
      - "/var/run/utmp:/var/run/utmp"

    # Type: list
    notifiarr_role_docker_volumes_custom: []

    # Mounts
    # Type: list
    notifiarr_role_docker_mounts_default: 
      - target: /tmp
        type: tmpfs

    # Type: list
    notifiarr_role_docker_mounts_custom: []

    # Hostname
    # Type: string
    notifiarr_role_docker_hostname: "{{ traefik_host }}"

    # Networks
    # Type: string
    notifiarr_role_docker_networks_alias: "{{ notifiarr_name }}"

    # Type: list
    notifiarr_role_docker_networks_default: []

    # Type: list
    notifiarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    notifiarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    notifiarr_role_docker_state: started

    # User
    # Type: string
    notifiarr_role_docker_user: "{{ uid }}:{{ gid }}"

    # Privileged
    # Type: string
    notifiarr_role_docker_privileged: "{{ lookup('role_var', '_privileged', role='notifiarr') | bool }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    notifiarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    notifiarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    notifiarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    notifiarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    notifiarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    notifiarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    notifiarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    notifiarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    notifiarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    notifiarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    notifiarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    notifiarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    notifiarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    notifiarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    notifiarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    notifiarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    notifiarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        notifiarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "notifiarr2.{{ user.domain }}"
          - "notifiarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        notifiarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'notifiarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
