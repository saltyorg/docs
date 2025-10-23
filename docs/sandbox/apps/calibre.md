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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable list "`calibre_instances`"

        ```yaml
        # Type: list
        calibre_instances: ["calibre"]
        ```

        !!! example

            ```yaml
            # Type: list
            calibre_instances: ["calibre", "calibre2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`calibre_role_paths_folder`"

            ```yaml
            # Type: string
            calibre_role_paths_folder: "{{ calibre_name }}"
            ```

        ??? variable string "`calibre_role_paths_location`"

            ```yaml
            # Type: string
            calibre_role_paths_location: "{{ server_appdata_path }}/{{ calibre_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`calibre2_paths_folder`"

            ```yaml
            # Type: string
            calibre2_paths_folder: "{{ calibre_name }}"
            ```

        ??? variable string "`calibre2_paths_location`"

            ```yaml
            # Type: string
            calibre2_paths_location: "{{ server_appdata_path }}/{{ calibre_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`calibre_role_web_subdomain`"

            ```yaml
            # Type: string
            calibre_role_web_subdomain: "{{ calibre_name }}"
            ```

        ??? variable string "`calibre_role_web_domain`"

            ```yaml
            # Type: string
            calibre_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`calibre_role_web_port`"

            ```yaml
            # Type: string
            calibre_role_web_port: "8080"
            ```

        ??? variable string "`calibre_role_web_url`"

            ```yaml
            # Type: string
            calibre_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='calibre') + '.' + lookup('role_var', '_web_domain', role='calibre')
                                   if (lookup('role_var', '_web_subdomain', role='calibre') | length > 0)
                                   else lookup('role_var', '_web_domain', role='calibre')) }}"
            ```

        ??? variable string "`calibre_role_web2_subdomain`"

            ```yaml
            # Type: string
            calibre_role_web2_subdomain: "{{ calibre_name }}books"
            ```

        ??? variable string "`calibre_role_web2_domain`"

            ```yaml
            # Type: string
            calibre_role_web2_domain: "{{ user.domain }}"
            ```

        ??? variable string "`calibre_role_web2_port`"

            ```yaml
            # Type: string
            calibre_role_web2_port: "8081"
            ```

        ??? variable string "`calibre_role_web2_role_web_url`"

            ```yaml
            # Type: string
            calibre_role_web2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web2_subdomain', role='calibre') + '.' + lookup('role_var', '_web2_domain', role='calibre')
                                             if (lookup('role_var', '_web2_subdomain', role='calibre') | length > 0)
                                             else lookup('role_var', '_web2_domain', role='calibre')) }}"
            ```

    === "Instance-level"

        ??? variable string "`calibre2_web_subdomain`"

            ```yaml
            # Type: string
            calibre2_web_subdomain: "{{ calibre_name }}"
            ```

        ??? variable string "`calibre2_web_domain`"

            ```yaml
            # Type: string
            calibre2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`calibre2_web_port`"

            ```yaml
            # Type: string
            calibre2_web_port: "8080"
            ```

        ??? variable string "`calibre2_web_url`"

            ```yaml
            # Type: string
            calibre2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='calibre') + '.' + lookup('role_var', '_web_domain', role='calibre')
                               if (lookup('role_var', '_web_subdomain', role='calibre') | length > 0)
                               else lookup('role_var', '_web_domain', role='calibre')) }}"
            ```

        ??? variable string "`calibre2_web2_subdomain`"

            ```yaml
            # Type: string
            calibre2_web2_subdomain: "{{ calibre_name }}books"
            ```

        ??? variable string "`calibre2_web2_domain`"

            ```yaml
            # Type: string
            calibre2_web2_domain: "{{ user.domain }}"
            ```

        ??? variable string "`calibre2_web2_port`"

            ```yaml
            # Type: string
            calibre2_web2_port: "8081"
            ```

        ??? variable string "`calibre2_web2_role_web_url`"

            ```yaml
            # Type: string
            calibre2_web2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web2_subdomain', role='calibre') + '.' + lookup('role_var', '_web2_domain', role='calibre')
                                         if (lookup('role_var', '_web2_subdomain', role='calibre') | length > 0)
                                         else lookup('role_var', '_web2_domain', role='calibre')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`calibre_role_dns_record`"

            ```yaml
            # Type: string
            calibre_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='calibre') }}"
            ```

        ??? variable string "`calibre_role_dns_zone`"

            ```yaml
            # Type: string
            calibre_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='calibre') }}"
            ```

        ??? variable bool "`calibre_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            calibre_role_dns_proxy: "{{ dns_proxied }}"
            ```

        ??? variable string "`calibre_role_dns2_record`"

            ```yaml
            # Type: string
            calibre_role_dns2_record: "{{ lookup('role_var', '_web2_subdomain', role='calibre') }}"
            ```

        ??? variable string "`calibre_role_dns2_zone`"

            ```yaml
            # Type: string
            calibre_role_dns2_zone: "{{ lookup('role_var', '_web2_domain', role='calibre') }}"
            ```

        ??? variable string "`calibre_role_dns2_proxy`"

            ```yaml
            # Type: string
            calibre_role_dns2_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`calibre2_dns_record`"

            ```yaml
            # Type: string
            calibre2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='calibre') }}"
            ```

        ??? variable string "`calibre2_dns_zone`"

            ```yaml
            # Type: string
            calibre2_dns_zone: "{{ lookup('role_var', '_web_domain', role='calibre') }}"
            ```

        ??? variable bool "`calibre2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            calibre2_dns_proxy: "{{ dns_proxied }}"
            ```

        ??? variable string "`calibre2_dns2_record`"

            ```yaml
            # Type: string
            calibre2_dns2_record: "{{ lookup('role_var', '_web2_subdomain', role='calibre') }}"
            ```

        ??? variable string "`calibre2_dns2_zone`"

            ```yaml
            # Type: string
            calibre2_dns2_zone: "{{ lookup('role_var', '_web2_domain', role='calibre') }}"
            ```

        ??? variable string "`calibre2_dns2_proxy`"

            ```yaml
            # Type: string
            calibre2_dns2_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`calibre_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            calibre_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`calibre_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            calibre_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`calibre_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            calibre_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`calibre_role_traefik_certresolver`"

            ```yaml
            # Type: string
            calibre_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`calibre_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            calibre_role_traefik_enabled: true
            ```

        ??? variable string "`calibre_role_books_traefik_sso_middleware`"

            ```yaml
            # Type: string
            calibre_role_books_traefik_sso_middleware: ""
            ```

        ??? variable string "`calibre_role_books_traefik_middleware_default`"

            ```yaml
            # Type: string
            calibre_role_books_traefik_middleware_default: "{{ traefik_default_middleware
                                                               + (',' + lookup('role_var', '_books_traefik_sso_middleware', role='calibre')
                                                                 if (lookup('role_var', '_books_traefik_sso_middleware', role='calibre') | length > 0)
                                                                 else '') }}"
            ```

        ??? variable string "`calibre_role_books_traefik_middleware_custom`"

            ```yaml
            # Type: string
            calibre_role_books_traefik_middleware_custom: ""
            ```

    === "Instance-level"

        ??? variable string "`calibre2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            calibre2_traefik_sso_middleware: ""
            ```

        ??? variable string "`calibre2_traefik_middleware_default`"

            ```yaml
            # Type: string
            calibre2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`calibre2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            calibre2_traefik_middleware_custom: ""
            ```

        ??? variable string "`calibre2_traefik_certresolver`"

            ```yaml
            # Type: string
            calibre2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`calibre2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            calibre2_traefik_enabled: true
            ```

        ??? variable string "`calibre2_books_traefik_sso_middleware`"

            ```yaml
            # Type: string
            calibre2_books_traefik_sso_middleware: ""
            ```

        ??? variable string "`calibre2_books_traefik_middleware_default`"

            ```yaml
            # Type: string
            calibre2_books_traefik_middleware_default: "{{ traefik_default_middleware
                                                           + (',' + lookup('role_var', '_books_traefik_sso_middleware', role='calibre')
                                                             if (lookup('role_var', '_books_traefik_sso_middleware', role='calibre') | length > 0)
                                                             else '') }}"
            ```

        ??? variable string "`calibre2_books_traefik_middleware_custom`"

            ```yaml
            # Type: string
            calibre2_books_traefik_middleware_custom: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`calibre_role_docker_container`"

            ```yaml
            # Type: string
            calibre_role_docker_container: "{{ calibre_name }}"
            ```

        ##### Image

        ??? variable bool "`calibre_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            calibre_role_docker_image_pull: true
            ```

        ??? variable string "`calibre_role_docker_image_repo`"

            ```yaml
            # Type: string
            calibre_role_docker_image_repo: "lscr.io/linuxserver/calibre"
            ```

        ??? variable string "`calibre_role_docker_image_tag`"

            ```yaml
            # Type: string
            calibre_role_docker_image_tag: "latest"
            ```

        ??? variable string "`calibre_role_docker_image`"

            ```yaml
            # Type: string
            calibre_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='calibre') }}:{{ lookup('role_var', '_docker_image_tag', role='calibre') }}"
            ```

        ##### Envs

        ??? variable dict "`calibre_role_docker_envs_default`"

            ```yaml
            # Type: dict
            calibre_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              CUSTOM_USER: "{{ user.name }}"
              PASSWORD: "{{ user.pass }}"
              LIBRARYINTERNALPATH: "/library"
            ```

        ??? variable dict "`calibre_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            calibre_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`calibre_role_docker_volumes_default`"

            ```yaml
            # Type: list
            calibre_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='calibre') }}:/config"
              - "/mnt/unionfs/Media/Books:/library"
            ```

        ??? variable list "`calibre_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            calibre_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable list "`calibre_role_docker_labels_default`"

            ```yaml
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
            ```

        ??? variable dict "`calibre_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            calibre_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`calibre_role_docker_hostname`"

            ```yaml
            # Type: string
            calibre_role_docker_hostname: "{{ calibre_name }}"
            ```

        ##### Networks

        ??? variable string "`calibre_role_docker_networks_alias`"

            ```yaml
            # Type: string
            calibre_role_docker_networks_alias: "{{ calibre_name }}"
            ```

        ??? variable list "`calibre_role_docker_networks_default`"

            ```yaml
            # Type: list
            calibre_role_docker_networks_default: []
            ```

        ??? variable list "`calibre_role_docker_networks_custom`"

            ```yaml
            # Type: list
            calibre_role_docker_networks_custom: []
            ```

        ##### Security Opts

        ??? variable list "`calibre_role_docker_security_opts_default`"

            ```yaml
            # Type: list
            calibre_role_docker_security_opts_default: 
              - seccomp=unconfined
            ```

        ??? variable list "`calibre_role_docker_security_opts_custom`"

            ```yaml
            # Type: list
            calibre_role_docker_security_opts_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`calibre_role_docker_restart_policy`"

            ```yaml
            # Type: string
            calibre_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`calibre_role_docker_state`"

            ```yaml
            # Type: string
            calibre_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`calibre2_docker_container`"

            ```yaml
            # Type: string
            calibre2_docker_container: "{{ calibre_name }}"
            ```

        ##### Image

        ??? variable bool "`calibre2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            calibre2_docker_image_pull: true
            ```

        ??? variable string "`calibre2_docker_image_repo`"

            ```yaml
            # Type: string
            calibre2_docker_image_repo: "lscr.io/linuxserver/calibre"
            ```

        ??? variable string "`calibre2_docker_image_tag`"

            ```yaml
            # Type: string
            calibre2_docker_image_tag: "latest"
            ```

        ??? variable string "`calibre2_docker_image`"

            ```yaml
            # Type: string
            calibre2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='calibre') }}:{{ lookup('role_var', '_docker_image_tag', role='calibre') }}"
            ```

        ##### Envs

        ??? variable dict "`calibre2_docker_envs_default`"

            ```yaml
            # Type: dict
            calibre2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              CUSTOM_USER: "{{ user.name }}"
              PASSWORD: "{{ user.pass }}"
              LIBRARYINTERNALPATH: "/library"
            ```

        ??? variable dict "`calibre2_docker_envs_custom`"

            ```yaml
            # Type: dict
            calibre2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`calibre2_docker_volumes_default`"

            ```yaml
            # Type: list
            calibre2_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='calibre') }}:/config"
              - "/mnt/unionfs/Media/Books:/library"
            ```

        ??? variable list "`calibre2_docker_volumes_custom`"

            ```yaml
            # Type: list
            calibre2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable list "`calibre2_docker_labels_default`"

            ```yaml
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
            ```

        ??? variable dict "`calibre2_docker_labels_custom`"

            ```yaml
            # Type: dict
            calibre2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`calibre2_docker_hostname`"

            ```yaml
            # Type: string
            calibre2_docker_hostname: "{{ calibre_name }}"
            ```

        ##### Networks

        ??? variable string "`calibre2_docker_networks_alias`"

            ```yaml
            # Type: string
            calibre2_docker_networks_alias: "{{ calibre_name }}"
            ```

        ??? variable list "`calibre2_docker_networks_default`"

            ```yaml
            # Type: list
            calibre2_docker_networks_default: []
            ```

        ??? variable list "`calibre2_docker_networks_custom`"

            ```yaml
            # Type: list
            calibre2_docker_networks_custom: []
            ```

        ##### Security Opts

        ??? variable list "`calibre2_docker_security_opts_default`"

            ```yaml
            # Type: list
            calibre2_docker_security_opts_default: 
              - seccomp=unconfined
            ```

        ??? variable list "`calibre2_docker_security_opts_custom`"

            ```yaml
            # Type: list
            calibre2_docker_security_opts_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`calibre2_docker_restart_policy`"

            ```yaml
            # Type: string
            calibre2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`calibre2_docker_state`"

            ```yaml
            # Type: string
            calibre2_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`calibre_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            calibre_role_autoheal_enabled: true
            ```

        ??? variable string "`calibre_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            calibre_role_depends_on: ""
            ```

        ??? variable string "`calibre_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            calibre_role_depends_on_delay: "0"
            ```

        ??? variable string "`calibre_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            calibre_role_depends_on_healthchecks:
            ```

        ??? variable bool "`calibre_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            calibre_role_diun_enabled: true
            ```

        ??? variable bool "`calibre_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            calibre_role_dns_enabled: true
            ```

        ??? variable bool "`calibre_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            calibre_role_docker_controller: true
            ```

        ??? variable bool "`calibre_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            calibre_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`calibre_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            calibre_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`calibre_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            calibre_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`calibre_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            calibre_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`calibre_role_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            calibre_role_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`calibre_role_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            calibre_role_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`calibre_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            calibre_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`calibre_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            calibre_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`calibre_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            calibre_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`calibre_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            calibre_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                calibre_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "calibre2.{{ user.domain }}"
                  - "calibre.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`calibre_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            calibre_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                calibre_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'calibre2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`calibre_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            calibre_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `calibre2`):

        ??? variable bool "`calibre2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            calibre2_autoheal_enabled: true
            ```

        ??? variable string "`calibre2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            calibre2_depends_on: ""
            ```

        ??? variable string "`calibre2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            calibre2_depends_on_delay: "0"
            ```

        ??? variable string "`calibre2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            calibre2_depends_on_healthchecks:
            ```

        ??? variable bool "`calibre2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            calibre2_diun_enabled: true
            ```

        ??? variable bool "`calibre2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            calibre2_dns_enabled: true
            ```

        ??? variable bool "`calibre2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            calibre2_docker_controller: true
            ```

        ??? variable bool "`calibre2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            calibre2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`calibre2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            calibre2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`calibre2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            calibre2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`calibre2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            calibre2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`calibre2_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            calibre2_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`calibre2_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            calibre2_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`calibre2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            calibre2_traefik_robot_enabled: true
            ```

        ??? variable bool "`calibre2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            calibre2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`calibre2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            calibre2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`calibre2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            calibre2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                calibre2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "calibre2.{{ user.domain }}"
                  - "calibre.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`calibre2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            calibre2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                calibre2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'calibre2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`calibre2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            calibre2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->