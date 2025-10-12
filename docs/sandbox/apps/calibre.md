---
hide:
  - tags
tags:
  - calibre
  - ebooks
  - management
---

# Calibre

## What is it?

[Calibre](https://calibre-ebook.com/) is a powerful and easy to use e-book manager. Users say it’s outstanding and a must-have. It’ll allow you to do nearly everything and it takes things a step beyond normal e-book software. It’s also completely free and open source and great for both casual users and computer experts.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://calibre-ebook.com/){: .header-icons } | [:octicons-link-16: Docs](https://manual.calibre-ebook.com/){: .header-icons } |  | [:material-docker: Docker](https://registry.hub.docker.com/r/linuxserver/calibre){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-calibre

```

### 2. URL

- To access Calibre, visit `https://calibre._yourdomain.com_`

### 3. Setup

- The username and password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

- The second books url serves the Calibre Content server and has a default user of abc and password abc, so make sure to remove/edit that user and enable 'Require username and password to access the Content server' otherwise it will be completely open.

- Calibre is ready for use. If you added your pre-existing Calibre library to /mnt/local/Media/Books then you should see your library is ready to go. If not, then you have a blank library ready for you to fill.

!!! info
    Running Calibre on a headless server is not very fun. If at all possible, run Calibre on your local, home computer. Use rclone to sync the files from home to google drive, and then another sync from google drive to your server so that Calibre-Web can use it.

    A local database file is required. This means you cannot run either Calibre or Calibre-Web from a mounted teamdrive, and this is the biggest pain for many of us. The easiest solution is to simply have your database and book files all located in /mnt/local/Media/Books.

    Both Calibre and Calibre-Web expect to find your library in `/mnt/unionfs/Media/Books`. Note that per standard Saltbox setup, `/mnt/local` is included inside `/mnt/unionfs`. However, both dockers also include access to anything in your `/mnt` directory.

### 4. Handy commands for managing your calibre docker

You can access advanced features of the Guacamole remote desktop using ctrl+alt+shift enabling you to use remote copy/paste and different languages.

- Shell access whilst the container is running: <br />
  `docker exec -it calibre /bin/bash`

- To monitor the logs of the container in realtime: <br />
  `docker logs -f calibre`

- Container version number: <br />
  `docker inspect -f '{{ index .Config.Labels "build_version" }}' calibre`

- Image version number: <br />
  `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/calibre`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `calibre_instances`.

    === "Role-level Override"

        Applies to all instances of calibre:

        ```yaml
        calibre_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `calibre2`):

        ```yaml
        calibre2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `calibre_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `calibre_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        calibre_instances: ["calibre"]

        ```

    === "Example"

        ```yaml
        # Type: list
        calibre_instances: ["calibre", "calibre2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        calibre_role_paths_folder: "{{ calibre_name }}"

        # Type: string
        calibre_role_paths_location: "{{ server_appdata_path }}/{{ calibre_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        calibre2_paths_folder: "{{ calibre_name }}"

        # Type: string
        calibre2_paths_location: "{{ server_appdata_path }}/{{ calibre_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        calibre_role_web_subdomain: "{{ calibre_name }}"

        # Type: string
        calibre_role_web_domain: "{{ user.domain }}"

        # Type: string
        calibre_role_web_port: "8080"

        # Type: string
        calibre_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='calibre') + '.' + lookup('role_var', '_web_domain', role='calibre')
                               if (lookup('role_var', '_web_subdomain', role='calibre') | length > 0)
                               else lookup('role_var', '_web_domain', role='calibre')) }}"

        # Type: string
        calibre_role_web2_subdomain: "{{ calibre_name }}books"

        # Type: string
        calibre_role_web2_domain: "{{ user.domain }}"

        # Type: string
        calibre_role_web2_port: "8081"

        # Type: string
        calibre_role_web2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web2_subdomain', role='calibre') + '.' + lookup('role_var', '_web2_domain', role='calibre')
                                         if (lookup('role_var', '_web2_subdomain', role='calibre') | length > 0)
                                         else lookup('role_var', '_web2_domain', role='calibre')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        calibre2_web_subdomain: "{{ calibre_name }}"

        # Type: string
        calibre2_web_domain: "{{ user.domain }}"

        # Type: string
        calibre2_web_port: "8080"

        # Type: string
        calibre2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='calibre') + '.' + lookup('role_var', '_web_domain', role='calibre')
                           if (lookup('role_var', '_web_subdomain', role='calibre') | length > 0)
                           else lookup('role_var', '_web_domain', role='calibre')) }}"

        # Type: string
        calibre2_web2_subdomain: "{{ calibre_name }}books"

        # Type: string
        calibre2_web2_domain: "{{ user.domain }}"

        # Type: string
        calibre2_web2_port: "8081"

        # Type: string
        calibre2_web2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web2_subdomain', role='calibre') + '.' + lookup('role_var', '_web2_domain', role='calibre')
                                     if (lookup('role_var', '_web2_subdomain', role='calibre') | length > 0)
                                     else lookup('role_var', '_web2_domain', role='calibre')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        calibre_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='calibre') }}"

        # Type: string
        calibre_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='calibre') }}"

        # Type: bool (true/false)
        calibre_role_dns_proxy: "{{ dns_proxied }}"

        # Type: string
        calibre_role_dns2_record: "{{ lookup('role_var', '_web2_subdomain', role='calibre') }}"

        # Type: string
        calibre_role_dns2_zone: "{{ lookup('role_var', '_web2_domain', role='calibre') }}"

        # Type: string
        calibre_role_dns2_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        calibre2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='calibre') }}"

        # Type: string
        calibre2_dns_zone: "{{ lookup('role_var', '_web_domain', role='calibre') }}"

        # Type: bool (true/false)
        calibre2_dns_proxy: "{{ dns_proxied }}"

        # Type: string
        calibre2_dns2_record: "{{ lookup('role_var', '_web2_subdomain', role='calibre') }}"

        # Type: string
        calibre2_dns2_zone: "{{ lookup('role_var', '_web2_domain', role='calibre') }}"

        # Type: string
        calibre2_dns2_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        calibre_role_traefik_sso_middleware: ""

        # Type: string
        calibre_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        calibre_role_traefik_middleware_custom: ""

        # Type: string
        calibre_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        calibre_role_traefik_enabled: true

        # Type: string
        calibre_role_books_traefik_sso_middleware: ""

        # Type: string
        calibre_role_books_traefik_middleware_default: "{{ traefik_default_middleware
                                                           + (',' + lookup('role_var', '_books_traefik_sso_middleware', role='calibre')
                                                             if (lookup('role_var', '_books_traefik_sso_middleware', role='calibre') | length > 0)
                                                             else '') }}"

        # Type: string
        calibre_role_books_traefik_middleware_custom: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        calibre2_traefik_sso_middleware: ""

        # Type: string
        calibre2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        calibre2_traefik_middleware_custom: ""

        # Type: string
        calibre2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        calibre2_traefik_enabled: true

        # Type: string
        calibre2_books_traefik_sso_middleware: ""

        # Type: string
        calibre2_books_traefik_middleware_default: "{{ traefik_default_middleware
                                                       + (',' + lookup('role_var', '_books_traefik_sso_middleware', role='calibre')
                                                         if (lookup('role_var', '_books_traefik_sso_middleware', role='calibre') | length > 0)
                                                         else '') }}"

        # Type: string
        calibre2_books_traefik_middleware_custom: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        calibre_role_docker_container: "{{ calibre_name }}"

        # Image
        # Type: bool (true/false)
        calibre_role_docker_image_pull: true

        # Type: string
        calibre_role_docker_image_repo: "lscr.io/linuxserver/calibre"

        # Type: string
        calibre_role_docker_image_tag: "latest"

        # Type: string
        calibre_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='calibre') }}:{{ lookup('role_var', '_docker_image_tag', role='calibre') }}"

        # Envs
        # Type: dict
        calibre_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          CUSTOM_USER: "{{ user.name }}"
          PASSWORD: "{{ user.pass }}"
          LIBRARYINTERNALPATH: "/library"

        # Type: dict
        calibre_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        calibre_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='calibre') }}:/config"
          - "/mnt/unionfs/Media/Books:/library"

        # Type: list
        calibre_role_docker_volumes_custom: []

        # Labels
        # Type: list
        calibre_role_docker_labels_default: 
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.entrypoints": "web" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.service": "{{ lookup("role_var", "_web2_subdomain", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.rule": "Host(`{{ lookup("role_var", "_web2_subdomain", role="calibre") + "." + lookup("role_var", "_web2_domain", role="calibre") }}`)" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.middlewares": "{{ traefik_default_middleware_http }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.priority": "20" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.entrypoints": "websecure" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.service": "{{ lookup("role_var", "_web2_subdomain", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.rule": "Host(`{{ lookup("role_var", "_web2_subdomain", role="calibre") + "." + lookup("role_var", "_web2_domain", role="calibre") }}`)" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.middlewares": "{{ lookup("role_var", "_books_traefik_middleware", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.priority": "20" }'
          - '{ "traefik.http.services.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.loadbalancer.server.port": "{{ lookup("role_var", "_web2_port", role="calibre") }}" }'

        # Type: dict
        calibre_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        calibre_role_docker_hostname: "{{ calibre_name }}"

        # Networks
        # Type: string
        calibre_role_docker_networks_alias: "{{ calibre_name }}"

        # Type: list
        calibre_role_docker_networks_default: []

        # Type: list
        calibre_role_docker_networks_custom: []

        # Security Opts
        # Type: list
        calibre_role_docker_security_opts_default: 
          - seccomp=unconfined

        # Type: list
        calibre_role_docker_security_opts_custom: []

        # Restart Policy
        # Type: string
        calibre_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        calibre_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        calibre2_docker_container: "{{ calibre_name }}"

        # Image
        # Type: bool (true/false)
        calibre2_docker_image_pull: true

        # Type: string
        calibre2_docker_image_repo: "lscr.io/linuxserver/calibre"

        # Type: string
        calibre2_docker_image_tag: "latest"

        # Type: string
        calibre2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='calibre') }}:{{ lookup('role_var', '_docker_image_tag', role='calibre') }}"

        # Envs
        # Type: dict
        calibre2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          CUSTOM_USER: "{{ user.name }}"
          PASSWORD: "{{ user.pass }}"
          LIBRARYINTERNALPATH: "/library"

        # Type: dict
        calibre2_docker_envs_custom: {}

        # Volumes
        # Type: list
        calibre2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='calibre') }}:/config"
          - "/mnt/unionfs/Media/Books:/library"

        # Type: list
        calibre2_docker_volumes_custom: []

        # Labels
        # Type: list
        calibre2_docker_labels_default: 
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.entrypoints": "web" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.service": "{{ lookup("role_var", "_web2_subdomain", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.rule": "Host(`{{ lookup("role_var", "_web2_subdomain", role="calibre") + "." + lookup("role_var", "_web2_domain", role="calibre") }}`)" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.middlewares": "{{ traefik_default_middleware_http }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}-http.priority": "20" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.entrypoints": "websecure" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.service": "{{ lookup("role_var", "_web2_subdomain", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.rule": "Host(`{{ lookup("role_var", "_web2_subdomain", role="calibre") + "." + lookup("role_var", "_web2_domain", role="calibre") }}`)" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.middlewares": "{{ lookup("role_var", "_books_traefik_middleware", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="calibre") }}" }'
          - '{ "traefik.http.routers.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.priority": "20" }'
          - '{ "traefik.http.services.{{ lookup("role_var", "_web2_subdomain", role="calibre") }}.loadbalancer.server.port": "{{ lookup("role_var", "_web2_port", role="calibre") }}" }'

        # Type: dict
        calibre2_docker_labels_custom: {}

        # Hostname
        # Type: string
        calibre2_docker_hostname: "{{ calibre_name }}"

        # Networks
        # Type: string
        calibre2_docker_networks_alias: "{{ calibre_name }}"

        # Type: list
        calibre2_docker_networks_default: []

        # Type: list
        calibre2_docker_networks_custom: []

        # Security Opts
        # Type: list
        calibre2_docker_security_opts_default: 
          - seccomp=unconfined

        # Type: list
        calibre2_docker_security_opts_custom: []

        # Restart Policy
        # Type: string
        calibre2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        calibre2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        calibre_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        calibre_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        calibre_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        calibre_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        calibre_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        calibre_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        calibre_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        calibre_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        calibre_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        calibre_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        calibre_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        calibre_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            calibre_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "calibre2.{{ user.domain }}"
              - "calibre.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            calibre_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'calibre2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `calibre2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        calibre2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        calibre2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        calibre2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        calibre2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        calibre2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        calibre2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        calibre2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        calibre2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        calibre2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        calibre2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        calibre2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        calibre2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        calibre2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        calibre2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        calibre2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        calibre2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        calibre2_web_scheme:

        ```

        1.  Example:

            ```yaml
            calibre2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "calibre2.{{ user.domain }}"
              - "calibre.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            calibre2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'calibre2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
