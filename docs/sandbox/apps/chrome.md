---
hide:
  - tags
tags:
  - chrome
  - browser
  - headless
---

# Chrome

Headless container running Google Chrome. Useful for testing, filling out forms, web crawling, getting webpage screenshots, etc.

This was created for use with Hoarder which calls for a specific version (123)

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-bookshelf: Github Repo&nbsp;&nbsp;](https://github.com/jlandure/alpine-chrome/blob/master/Dockerfile){ .md-button .md-button--stretch }

[:material-git: Google Artifact&nbsp;&nbsp;](https://console.cloud.google.com/artifacts/docker/zenika-hub/us/gcr.io/alpine-chrome/sha256:e38563d4475a3d791e986500a2e4125c9afd13798067138881cf770b1f6f3980){ .md-button .md-button--stretch }

</div>

This role is not exposed by default.

## Deployment

```shell
sb install sandbox-chrome
```

## Usage

The docker commands are set to the following by default. Port 9222 is open to the container by default.

```yaml
  - --no-sandbox
  - --disable-gpu
  - --disable-dev-shm-usage
  - --remote-debugging-address=0.0.0.0
  - --remote-debugging-port=9222
  - --hide-scrollbars
```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        chrome_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `chrome_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `chrome_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    chrome_name: chrome

    ```

??? example "Paths"

    ```yaml
    # Type: string
    chrome_role_paths_folder: "{{ chrome_name }}"

    # Type: string
    chrome_role_paths_location: "{{ server_appdata_path }}/{{ chrome_role_paths_folder }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    chrome_role_docker_container: "{{ chrome_name }}"

    # Image
    # Type: bool (true/false)
    chrome_role_docker_image_pull: true

    # Type: string
    chrome_role_docker_image_repo: "gcr.io/zenika-hub/alpine-chrome"

    # Type: string
    chrome_role_docker_image_tag: "124"

    # Type: string
    chrome_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='chrome') }}:{{ lookup('role_var', '_docker_image_tag', role='chrome') }}"

    # Envs
    # Type: dict
    chrome_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    chrome_role_docker_envs_custom: {}

    # Commands
    # Type: list
    chrome_role_docker_commands_default: 
      - "--no-sandbox"
      - "--disable-gpu"
      - "--disable-dev-shm-usage"
      - "--remote-debugging-address=0.0.0.0"
      - "--remote-debugging-port=9222"
      - "--hide-scrollbars"

    # Type: list
    chrome_role_docker_commands_custom: []

    # Hostname
    # Type: string
    chrome_role_docker_hostname: "{{ chrome_name }}"

    # Networks
    # Type: string
    chrome_role_docker_networks_alias: "{{ chrome_name }}"

    # Type: list
    chrome_role_docker_networks_default: []

    # Type: list
    chrome_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    chrome_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    chrome_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    chrome_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    chrome_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    chrome_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    chrome_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    chrome_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    chrome_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    chrome_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    chrome_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    chrome_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    chrome_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    chrome_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    chrome_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    chrome_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    chrome_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    chrome_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    chrome_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    chrome_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        chrome_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "chrome2.{{ user.domain }}"
          - "chrome.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        chrome_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'chrome2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
