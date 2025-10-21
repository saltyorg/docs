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

- The Notifiarr url will only display the app status `https://notifiarr._yourdomain.com_`

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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable string "`notifiarr_name`"

        ```yaml
        # Type: string
        notifiarr_name: notifiarr
        ```

=== "Settings"

    ??? variable bool "`notifiarr_role_privileged`"

        ```yaml
        # Type: bool (true/false)
        notifiarr_role_privileged: false
        ```

=== "Paths"

    ??? variable string "`notifiarr_role_paths_folder`"

        ```yaml
        # Type: string
        notifiarr_role_paths_folder: "{{ notifiarr_name }}"
        ```

    ??? variable string "`notifiarr_role_paths_location`"

        ```yaml
        # Type: string
        notifiarr_role_paths_location: "{{ server_appdata_path }}/{{ notifiarr_role_paths_folder }}"
        ```

    ??? variable bool "`notifiarr_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        notifiarr_role_paths_recursive: true
        ```

    ??? variable string "`notifiarr_role_paths_config_location`"

        ```yaml
        # Type: string
        notifiarr_role_paths_config_location: "{{ notifiarr_role_paths_location }}/notifiarr.conf"
        ```

    ??? variable string "`notifiarr_role_radarr_config`"

        ```yaml
        # Type: string
        notifiarr_role_radarr_config: "{{ lookup('role_var', '_paths_location', role='radarr') }}/config.xml"
        ```

    ??? variable string "`notifiarr_role_sonarr_config`"

        ```yaml
        # Type: string
        notifiarr_role_sonarr_config: "{{ lookup('role_var', '_paths_location', role='sonarr') }}/config.xml"
        ```

    ??? variable string "`notifiarr_role_tautulli_config`"

        ```yaml
        # Type: string
        notifiarr_role_tautulli_config: "{{ lookup('role_var', '_paths_location', role='tautulli') }}/config.ini"
        ```

    ??? variable string "`notifiarr_role_tautulli_api_key`"

        ```yaml
        # Type: string
        notifiarr_role_tautulli_api_key: "{{ lookup('ini', 'api_key section=General file=' ~ lookup('role_var', '_tautulli_config', role='notifiarr')) if notifiarr_tautulli_config_stat.stat.exists else '' }}"
        ```

=== "Web"

    ??? variable string "`notifiarr_role_web_subdomain`"

        ```yaml
        # Type: string
        notifiarr_role_web_subdomain: "{{ notifiarr_name }}"
        ```

    ??? variable string "`notifiarr_role_web_domain`"

        ```yaml
        # Type: string
        notifiarr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`notifiarr_role_web_port`"

        ```yaml
        # Type: string
        notifiarr_role_web_port: "5454"
        ```

    ??? variable string "`notifiarr_role_web_url`"

        ```yaml
        # Type: string
        notifiarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='notifiarr') + '.' + lookup('role_var', '_web_domain', role='notifiarr')
                                 if (lookup('role_var', '_web_subdomain', role='notifiarr') | length > 0)
                                 else lookup('role_var', '_web_domain', role='notifiarr')) }}"
        ```

=== "DNS"

    ??? variable string "`notifiarr_role_dns_record`"

        ```yaml
        # Type: string
        notifiarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='notifiarr') }}"
        ```

    ??? variable string "`notifiarr_role_dns_zone`"

        ```yaml
        # Type: string
        notifiarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='notifiarr') }}"
        ```

    ??? variable bool "`notifiarr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        notifiarr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`notifiarr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        notifiarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`notifiarr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        notifiarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`notifiarr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        notifiarr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`notifiarr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        notifiarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`notifiarr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        notifiarr_role_traefik_enabled: true
        ```

    ??? variable bool "`notifiarr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        notifiarr_role_traefik_api_enabled: true
        ```

    ??? variable string "`notifiarr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        notifiarr_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/plex`)"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`notifiarr_role_docker_container`"

        ```yaml
        # Type: string
        notifiarr_role_docker_container: "{{ notifiarr_name }}"
        ```

    ##### Image

    ??? variable bool "`notifiarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        notifiarr_role_docker_image_pull: true
        ```

    ??? variable string "`notifiarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        notifiarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`notifiarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        notifiarr_role_docker_image_repo: "golift/notifiarr"
        ```

    ??? variable string "`notifiarr_role_docker_image`"

        ```yaml
        # Type: string
        notifiarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='notifiarr') }}:{{ lookup('role_var', '_docker_image_tag', role='notifiarr') }}"
        ```

    ##### Envs

    ??? variable dict "`notifiarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        notifiarr_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`notifiarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        notifiarr_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`notifiarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        notifiarr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='notifiarr') }}:/config"
          - "/var/run/utmp:/var/run/utmp"
        ```

    ??? variable list "`notifiarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        notifiarr_role_docker_volumes_custom: []
        ```

    ##### Mounts

    ??? variable list "`notifiarr_role_docker_mounts_default`"

        ```yaml
        # Type: list
        notifiarr_role_docker_mounts_default: 
          - target: /tmp
            type: tmpfs
        ```

    ??? variable list "`notifiarr_role_docker_mounts_custom`"

        ```yaml
        # Type: list
        notifiarr_role_docker_mounts_custom: []
        ```

    ##### Hostname

    ??? variable string "`notifiarr_role_docker_hostname`"

        ```yaml
        # Type: string
        notifiarr_role_docker_hostname: "{{ traefik_host }}"
        ```

    ##### Networks

    ??? variable string "`notifiarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        notifiarr_role_docker_networks_alias: "{{ notifiarr_name }}"
        ```

    ??? variable list "`notifiarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        notifiarr_role_docker_networks_default: []
        ```

    ??? variable list "`notifiarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        notifiarr_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`notifiarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        notifiarr_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`notifiarr_role_docker_state`"

        ```yaml
        # Type: string
        notifiarr_role_docker_state: started
        ```

    ##### User

    ??? variable string "`notifiarr_role_docker_user`"

        ```yaml
        # Type: string
        notifiarr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    ##### Privileged

    ??? variable string "`notifiarr_role_docker_privileged`"

        ```yaml
        # Type: string
        notifiarr_role_docker_privileged: "{{ lookup('role_var', '_privileged', role='notifiarr') | bool }}"
        ```

=== "Global Override Options"

    ??? variable bool "`notifiarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        notifiarr_role_autoheal_enabled: true
        ```

    ??? variable string "`notifiarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        notifiarr_role_depends_on: ""
        ```

    ??? variable string "`notifiarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        notifiarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`notifiarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        notifiarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`notifiarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        notifiarr_role_diun_enabled: true
        ```

    ??? variable bool "`notifiarr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        notifiarr_role_dns_enabled: true
        ```

    ??? variable bool "`notifiarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        notifiarr_role_docker_controller: true
        ```

    ??? variable bool "`notifiarr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        notifiarr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`notifiarr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        notifiarr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`notifiarr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        notifiarr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`notifiarr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        notifiarr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`notifiarr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        notifiarr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`notifiarr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        notifiarr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`notifiarr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        notifiarr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`notifiarr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        notifiarr_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            notifiarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "notifiarr2.{{ user.domain }}"
              - "notifiarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`notifiarr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        notifiarr_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            notifiarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'notifiarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`notifiarr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        notifiarr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->