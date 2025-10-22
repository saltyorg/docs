---
hide:
  - tags
tags:
  - firefox
  - browser
---

# Firefox

Implements a Docker container for Firefox. The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://jlesage.github.io/docker-apps){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/jlesage/docker-firefox/blob/master/README.md#usage){ .md-button .md-button--stretch }

[:fontawesome-brands-docker: Releases&nbsp;&nbsp;](https://hub.docker.com/r/jlesage/firefox/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github: Community&nbsp;&nbsp;](https://github.com/jlesage/docker-firefox/discussions){ .md-button .md-button--stretch }

</div>

---

## Configuration

Settings are available as environment variables[<sup>:octicons-link-external-16:</sup>][envs] in `/opt/firefox/.env`.

???+ question "Security"

    By default, web access is restricted by Authelia, and VNC access is secured through SSH authentication; hence, no VNC password is configured. To add this extra layer of security, the process is straightforward:

    1. Run the following command:
       ```shell
       $EDITOR /opt/firefox/.vncpass_clear
       ```
    
    2. Enter your desired password (up to 8 characters in length) and save the file.
    
    3. At a minimum, a container restart is required for changes to take effect.

## Deployment

``` shell
sb install sandbox-firefox
```

!!! info inline end sb-wide "Downloads Save Location"
    ```
    /mnt/unionfs/downloads/firefox
    ```

## Usage

### :material-web: Web

Visit `https://firefox.xDOMAIN_NAMEx`.

### :material-remote-desktop: VNC

The role supports VNC access over an SSH tunnel (local port forwarding) to Saltbox.

!!! example "Example Command on Local Machine <span style="float:right;color:#00bfa5">:material-fire: Some VNC apps have this functionality built-in!</span>"
    ```shell
    ssh -L localhost:5900:firefox:5900 seed@203.0.113.1 -p 8843 # (1)!
    ```

    1. `-L localhost:5900:firefox:5900`: This part specifies local port forwarding. It tells SSH to listen on port 5900 on your local machine and forward any traffic to the firefox Docker container on port 5900 on the Saltbox host. In other words, it sets up a tunnel between your local port 5900 and the container's port 5900.

        Complete the command with your usual SSH info: `USERNAME@SALTBOX_EXTERNAL_IP -p SSH_PORT`.

While the tunnel is active, you can use a VNC client to access the GUI via the address `localhost:5900`.

  [envs]: https://github.com/jlesage/docker-firefox#environment-variables "Access project Docker environment variables breakdown"

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        firefox_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `firefox_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `firefox_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    firefox_name: firefox

    ```

??? example "Paths"

    ```yaml
    # Type: string
    firefox_role_paths_folder: "{{ firefox_name }}"

    # Type: string
    firefox_role_paths_location: "{{ server_appdata_path }}/{{ firefox_role_paths_folder }}"

    # Type: string
    firefox_role_paths_downloads_location: "{{ downloads_root_path }}/{{ firefox_role_paths_folder }}"

    # Type: string
    firefox_role_paths_env_file_location: "{{ firefox_role_paths_location }}/.env"

    ```

??? example "Web"

    ```yaml
    # Type: string
    firefox_role_web_subdomain: "{{ firefox_name }}"

    # Type: string
    firefox_role_web_domain: "{{ user.domain }}"

    # Type: string
    firefox_role_web_port: "5800"

    # Type: string
    firefox_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='firefox') + '.' + lookup('role_var', '_web_domain', role='firefox')
                           if (lookup('role_var', '_web_subdomain', role='firefox') | length > 0)
                           else lookup('role_var', '_web_domain', role='firefox')) }}"

    ```

??? example "VNC"

    ```yaml
    # Type: string
    firefox_role_vnc_port: "5900"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    firefox_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='firefox') }}"

    # Type: string
    firefox_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='firefox') }}"

    # Type: bool (true/false)
    firefox_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    firefox_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    firefox_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    firefox_role_traefik_middleware_custom: ""

    # Type: string
    firefox_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    firefox_role_traefik_enabled: true

    # Type: bool (true/false)
    firefox_role_traefik_api_enabled: false

    # Type: string
    firefox_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    firefox_role_docker_container: "{{ firefox_name }}"

    # Image
    # Type: bool (true/false)
    firefox_role_docker_image_pull: true

    # Type: string
    firefox_role_docker_image_repo: "jlesage/firefox"

    # Type: string
    firefox_role_docker_image_tag: "latest"

    # Type: string
    firefox_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='firefox') }}:{{ lookup('role_var', '_docker_image_tag', role='firefox') }}"

    # Envs
    # Type: string
    firefox_role_docker_env_file: "{{ lookup('role_var', '_paths_env_file_location', role='firefox') }}"

    # Volumes
    # Type: list
    firefox_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='firefox') }}:/config"

    # Type: list
    firefox_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    firefox_role_docker_hostname: "{{ firefox_name }}"

    # Networks
    # Type: string
    firefox_role_docker_networks_alias: "{{ firefox_name }}"

    # Type: list
    firefox_role_docker_networks_default: []

    # Type: list
    firefox_role_docker_networks_custom: []

    # Capabilities
    # Type: list
    firefox_role_docker_capabilities_default: 
      - "SYS_NICE"

    # Type: list
    firefox_role_docker_capabilities_custom: []

    # Restart Policy
    # Type: string
    firefox_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    firefox_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    firefox_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    firefox_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    firefox_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    firefox_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    firefox_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    firefox_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    firefox_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    firefox_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    firefox_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    firefox_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    firefox_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    firefox_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    firefox_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    firefox_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    firefox_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    firefox_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    firefox_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        firefox_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "firefox2.{{ user.domain }}"
          - "firefox.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        firefox_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'firefox2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
