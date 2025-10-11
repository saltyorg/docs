---
hide:
  - tags
tags:
  - thelounge
  - irc
  - chat
---

# The Lounge

## What is it?

[The Lounge](https://thelounge.chat/) is a self hosted web IRC client. In private mode, The Lounge acts like a bouncer and a client combined, in order to offer an experience similar to other modern chat applications outside the IRC world. Users can then access and resume their session without being disconnected from their channels.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: The Lounge](https://thelounge.chat/){: .header-icons } | [:octicons-link-16: Docs](https://thelounge.chat/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/thelounge/thelounge ){: .header-icons } | [:material-docker: Docker:](https://docs.linuxserver.io/images/docker-thelounge){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-thelounge

```

### 2. URL

- To access The Lounge, visit `https://thelounge._yourdomain.com_`

### 3. Setup

- When the application first runs, it will populate its /config
- Stop the container
- Now from the host, edit /config/config.js, wherever you've mapped it
- In most cases you want the value public: false to allow named users only
- Setting the two prefetch values to true improves usability, but uses more storage
- Once you have the configuration you want, save it and start the container again
- For each user, run the command

      ``` shell
        docker exec -it thelounge s6-setuidgid abc thelounge add <user>
      ```
  - You will be prompted to enter a password that will not be echoed.
  - Saving logs to disk is the default, this consumes more space but allows scrollback.
- To log in to the application, browse to `https://thelounge._yourdomain.com_`
- You should now be prompted for a username and password on the webinterface.
- Once logged in, you can add an IRC network. Some defaults are preset for Freenode.

### ZNC

To connect to **[znc](../../sandbox/apps/znc.md)**, you need to have a **[znc](../../sandbox/apps/znc.md)** server running. A guide to using The Lounge with ZNC can be found [here](https://thelounge.chat/docs/guides/znc)

- In this image we have a ZNC network defined.

![ZNC network Screenshot](../../sandbox/images/znc_network.png)

- To add this network to The Lounge, give it a Name, it does not have to match the ZNC network settings.
- For the Server, use `znc` and set the port to `6502`
- For the Password, enter your `ZNC user password`
- Uncheck `Use secure connection (TLS)
- In the User Preferences section enter your Nick - I would recommend the same Nick as that set in ZNC.
- For the user name enter the `<ZNC username>/<ZNC_Network_Name>`.
- For Real Name, enter your desired `<real_name>` it does not need to match ZNC
- Save the network, and it should connect to ZNC.

![The Lounge network Screenshot](../../sandbox/images/lounge_network.png)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        thelounge_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    thelounge_name: thelounge

    ```

??? example "Paths"

    ```yaml
    # Type: string
    thelounge_role_paths_folder: "{{ thelounge_name }}"

    # Type: string
    thelounge_role_paths_location: "{{ server_appdata_path }}/{{ thelounge_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    thelounge_role_web_subdomain: "{{ thelounge_name }}"

    # Type: string
    thelounge_role_web_domain: "{{ user.domain }}"

    # Type: string
    thelounge_role_web_port: "9000"

    # Type: string
    thelounge_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='thelounge') + '.' + lookup('role_var', '_web_domain', role='thelounge')
                             if (lookup('role_var', '_web_subdomain', role='thelounge') | length > 0)
                             else lookup('role_var', '_web_domain', role='thelounge')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    thelounge_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='thelounge') }}"

    # Type: string
    thelounge_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='thelounge') }}"

    # Type: bool (true/false)
    thelounge_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    thelounge_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    thelounge_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    thelounge_role_traefik_middleware_custom: ""

    # Type: string
    thelounge_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    thelounge_role_traefik_enabled: true

    # Type: bool (true/false)
    thelounge_role_traefik_api_enabled: true

    # Type: string
    thelounge_role_traefik_api_endpoint: "PathPrefix(`/uploads`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    thelounge_role_docker_container: "{{ thelounge_name }}"

    # Image
    # Type: bool (true/false)
    thelounge_role_docker_image_pull: true

    # Type: string
    thelounge_role_docker_image_repo: "lscr.io/linuxserver/thelounge"

    # Type: string
    thelounge_role_docker_image_tag: "latest"

    # Type: string
    thelounge_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='thelounge') }}:{{ lookup('role_var', '_docker_image_tag', role='thelounge') }}"

    # Envs
    # Type: dict
    thelounge_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    thelounge_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    thelounge_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='thelounge') }}:/config"

    # Type: list
    thelounge_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    thelounge_role_docker_hostname: "{{ thelounge_name }}"

    # Networks
    # Type: string
    thelounge_role_docker_networks_alias: "{{ thelounge_name }}"

    # Type: list
    thelounge_role_docker_networks_default: []

    # Type: list
    thelounge_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    thelounge_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    thelounge_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    thelounge_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    thelounge_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    thelounge_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    thelounge_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    thelounge_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    thelounge_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    thelounge_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    thelounge_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    thelounge_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    thelounge_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    thelounge_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    thelounge_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    thelounge_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    thelounge_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    thelounge_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    thelounge_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    thelounge_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        thelounge_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "thelounge2.{{ user.domain }}"
          - "thelounge.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        thelounge_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'thelounge2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
