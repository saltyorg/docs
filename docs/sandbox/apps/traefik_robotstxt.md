---
hide:
  - tags
tags:
  - traefik-robotstxt
  - networking
  - seo
---

# Robotstxt

## What is it?

[Robotstxt](https://github.com/mstroecker/zig-robotstxt) is a lightweight http-server, just serving a disallow-robots.txt file using the Zig programming language([https://ziglang.org/](https://ziglang.org/)).

__Robots.txt__ basically works like a “No Trespassing” sign. It actually, tells robots whether we want them to crawl the website or not. With this role, we are disallowing all robots to crawl and avoid indexing in search engines.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/mstroecker/zig-robotstxt){: .header-icons } | [:octicons-link-16: Docs](https://github.com/mstroecker/zig-robotstxt){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/mstroecker/zig-robotstxt){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/mstroecker/zig-robotstxt){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-traefik-robotstxt
```

### 2. Result

```text
HTTP/1.1 200 OK
Content-Length: 26

User-agent: *
Disallow: /
```

When you want to reach `*.yourdomain.tld/robots.txt`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        traefik_robotstxt_role_docker_image_tag: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `traefik_robotstxt_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `traefik_robotstxt_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    traefik_robotstxt_name: traefik-robotstxt

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    traefik_robotstxt_role_docker_container: "{{ traefik_robotstxt_name }}"

    # Image
    # Type: bool (true/false)
    traefik_robotstxt_role_docker_image_pull: true

    # Type: string
    traefik_robotstxt_role_docker_image_repo: "mstroecker/zig-robotstxt"

    # Type: string
    traefik_robotstxt_role_docker_image_tag: "latest"

    # Type: string
    traefik_robotstxt_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='traefik_robotstxt') }}:{{ lookup('role_var', '_docker_image_tag', role='traefik_robotstxt') }}"

    # Labels
    # Type: dict
    traefik_robotstxt_role_docker_labels_default: 
      traefik.enable: "true"
      traefik.http.routers.robotstxt.entrypoints: "web,websecure"
      traefik.http.routers.robotstxt.rule: "Path(`/robots.txt`)"
      traefik.http.routers.robotstxt.service: "robotstxt"
      traefik.http.services.robotstxt.loadbalancer.server.port: "8080"
      traefik.http.routers.robotstxt.priority: "99"

    # Type: dict
    traefik_robotstxt_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    traefik_robotstxt_role_docker_hostname: "{{ traefik_robotstxt_name }}"

    # Networks
    # Type: string
    traefik_robotstxt_role_docker_networks_alias: "{{ traefik_robotstxt_name }}"

    # Type: list
    traefik_robotstxt_role_docker_networks_default: []

    # Type: list
    traefik_robotstxt_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    traefik_robotstxt_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    traefik_robotstxt_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    traefik_robotstxt_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    traefik_robotstxt_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    traefik_robotstxt_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    traefik_robotstxt_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    traefik_robotstxt_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    traefik_robotstxt_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    traefik_robotstxt_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    traefik_robotstxt_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    traefik_robotstxt_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        traefik_robotstxt_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "traefik_robotstxt2.{{ user.domain }}"
          - "traefik_robotstxt.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        traefik_robotstxt_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'traefik_robotstxt2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
