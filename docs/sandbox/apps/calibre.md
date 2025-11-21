---
icon: material/docker
hide:
  - tags
tags:
  - calibre
  - ebooks
  - management
---

# Calibre

## Overview

[Calibre](https://calibre-ebook.com/) is a powerful and easy to use e-book manager. Users say it’s outstanding and a must-have. It’ll allow you to do nearly everything and it takes things a step beyond normal e-book software. It’s also completely free and open source and great for both casual users and computer experts.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://calibre-ebook.com/){: .header-icons } | [:octicons-link-16: Docs](https://manual.calibre-ebook.com/){: .header-icons } |  | [:material-docker: Docker](https://registry.hub.docker.com/r/linuxserver/calibre){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-calibre
```

### 2. URL

- To access Calibre, visit <https://calibre.iYOUR_DOMAIN_NAMEi>

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

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of calibre:" }
    calibre_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `calibre2`):" }
    calibre2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `calibre_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `calibre_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`calibre_instances`"

        ```yaml
        # Type: list
        calibre_instances: ["calibre"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            calibre_instances: ["calibre", "calibre2"]
            ```

=== "Paths"

    ??? variable string "`calibre_role_paths_folder`{ .sb-show-on-unchecked }`calibre2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_paths_folder: "{{ calibre_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_paths_folder: "{{ calibre_name }}"
        ```

    ??? variable string "`calibre_role_paths_location`{ .sb-show-on-unchecked }`calibre2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_paths_location: "{{ server_appdata_path }}/{{ calibre_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_paths_location: "{{ server_appdata_path }}/{{ calibre_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`calibre_role_web_subdomain`{ .sb-show-on-unchecked }`calibre2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web_subdomain: "{{ calibre_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web_subdomain: "{{ calibre_name }}"
        ```

    ??? variable string "`calibre_role_web_domain`{ .sb-show-on-unchecked }`calibre2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`calibre_role_web_port`{ .sb-show-on-unchecked }`calibre2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web_port: "8080"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web_port: "8080"
        ```

    ??? variable string "`calibre_role_web_url`{ .sb-show-on-unchecked }`calibre2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='calibre') + '.' + lookup('role_var', '_web_domain', role='calibre')
                               if (lookup('role_var', '_web_subdomain', role='calibre') | length > 0)
                               else lookup('role_var', '_web_domain', role='calibre')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='calibre') + '.' + lookup('role_var', '_web_domain', role='calibre')
                           if (lookup('role_var', '_web_subdomain', role='calibre') | length > 0)
                           else lookup('role_var', '_web_domain', role='calibre')) }}"
        ```

    ??? variable string "`calibre_role_web2_subdomain`{ .sb-show-on-unchecked }`calibre2_web2_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web2_subdomain: "{{ calibre_name }}books"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web2_subdomain: "{{ calibre_name }}books"
        ```

    ??? variable string "`calibre_role_web2_domain`{ .sb-show-on-unchecked }`calibre2_web2_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web2_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web2_domain: "{{ user.domain }}"
        ```

    ??? variable string "`calibre_role_web2_port`{ .sb-show-on-unchecked }`calibre2_web2_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web2_port: "8081"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web2_port: "8081"
        ```

    ??? variable string "`calibre_role_web2_role_web_url`{ .sb-show-on-unchecked }`calibre2_web2_role_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_web2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web2_subdomain', role='calibre') + '.' + lookup('role_var', '_web2_domain', role='calibre')
                                         if (lookup('role_var', '_web2_subdomain', role='calibre') | length > 0)
                                         else lookup('role_var', '_web2_domain', role='calibre')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_web2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web2_subdomain', role='calibre') + '.' + lookup('role_var', '_web2_domain', role='calibre')
                                     if (lookup('role_var', '_web2_subdomain', role='calibre') | length > 0)
                                     else lookup('role_var', '_web2_domain', role='calibre')) }}"
        ```

=== "DNS"

    ??? variable string "`calibre_role_dns_record`{ .sb-show-on-unchecked }`calibre2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='calibre') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='calibre') }}"
        ```

    ??? variable string "`calibre_role_dns_zone`{ .sb-show-on-unchecked }`calibre2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='calibre') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_dns_zone: "{{ lookup('role_var', '_web_domain', role='calibre') }}"
        ```

    ??? variable bool "`calibre_role_dns_proxy`{ .sb-show-on-unchecked }`calibre2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_dns_proxy: "{{ dns_proxied }}"
        ```

    ??? variable string "`calibre_role_dns2_record`{ .sb-show-on-unchecked }`calibre2_dns2_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_dns2_record: "{{ lookup('role_var', '_web2_subdomain', role='calibre') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_dns2_record: "{{ lookup('role_var', '_web2_subdomain', role='calibre') }}"
        ```

    ??? variable string "`calibre_role_dns2_zone`{ .sb-show-on-unchecked }`calibre2_dns2_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_dns2_zone: "{{ lookup('role_var', '_web2_domain', role='calibre') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_dns2_zone: "{{ lookup('role_var', '_web2_domain', role='calibre') }}"
        ```

    ??? variable string "`calibre_role_dns2_proxy`{ .sb-show-on-unchecked }`calibre2_dns2_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_dns2_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_dns2_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`calibre_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`calibre2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_sso_middleware: ""
        ```

    ??? variable string "`calibre_role_traefik_middleware_default`{ .sb-show-on-unchecked }`calibre2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`calibre_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`calibre2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_middleware_custom: ""
        ```

    ??? variable string "`calibre_role_traefik_certresolver`{ .sb-show-on-unchecked }`calibre2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`calibre_role_traefik_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_traefik_enabled: true
        ```

    ??? variable string "`calibre_role_books_traefik_sso_middleware`{ .sb-show-on-unchecked }`calibre2_books_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_books_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_books_traefik_sso_middleware: ""
        ```

    ??? variable string "`calibre_role_books_traefik_middleware_default`{ .sb-show-on-unchecked }`calibre2_books_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_books_traefik_middleware_default: "{{ traefik_default_middleware
                                                           + (',' + lookup('role_var', '_books_traefik_sso_middleware', role='calibre')
                                                             if (lookup('role_var', '_books_traefik_sso_middleware', role='calibre') | length > 0)
                                                             else '') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_books_traefik_middleware_default: "{{ traefik_default_middleware
                                                       + (',' + lookup('role_var', '_books_traefik_sso_middleware', role='calibre')
                                                         if (lookup('role_var', '_books_traefik_sso_middleware', role='calibre') | length > 0)
                                                         else '') }}"
        ```

    ??? variable string "`calibre_role_books_traefik_middleware_custom`{ .sb-show-on-unchecked }`calibre2_books_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_books_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_books_traefik_middleware_custom: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`calibre_role_docker_container`{ .sb-show-on-unchecked }`calibre2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_container: "{{ calibre_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_container: "{{ calibre_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`calibre_role_docker_image_pull`{ .sb-show-on-unchecked }`calibre2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_image_pull: true
        ```

    ??? variable string "`calibre_role_docker_image_repo`{ .sb-show-on-unchecked }`calibre2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_image_repo: "lscr.io/linuxserver/calibre"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_image_repo: "lscr.io/linuxserver/calibre"
        ```

    ??? variable string "`calibre_role_docker_image_tag`{ .sb-show-on-unchecked }`calibre2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_image_tag: "latest"
        ```

    ??? variable string "`calibre_role_docker_image`{ .sb-show-on-unchecked }`calibre2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='calibre') }}:{{ lookup('role_var', '_docker_image_tag', role='calibre') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='calibre') }}:{{ lookup('role_var', '_docker_image_tag', role='calibre') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`calibre_role_docker_envs_default`{ .sb-show-on-unchecked }`calibre2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        calibre_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          CUSTOM_USER: "{{ user.name }}"
          PASSWORD: "{{ user.pass }}"
          LIBRARYINTERNALPATH: "/library"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        calibre2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          CUSTOM_USER: "{{ user.name }}"
          PASSWORD: "{{ user.pass }}"
          LIBRARYINTERNALPATH: "/library"
        ```

    ??? variable dict "`calibre_role_docker_envs_custom`{ .sb-show-on-unchecked }`calibre2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        calibre_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        calibre2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`calibre_role_docker_volumes_default`{ .sb-show-on-unchecked }`calibre2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='calibre') }}:/config"
          - "/mnt/unionfs/Media/Books:/library"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='calibre') }}:/config"
          - "/mnt/unionfs/Media/Books:/library"
        ```

    ??? variable list "`calibre_role_docker_volumes_custom`{ .sb-show-on-unchecked }`calibre2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable list "`calibre_role_docker_labels_default`{ .sb-show-on-unchecked }`calibre2_docker_labels_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
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

        ```yaml { .sb-show-on-checked }
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

    ??? variable dict "`calibre_role_docker_labels_custom`{ .sb-show-on-unchecked }`calibre2_docker_labels_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        calibre_role_docker_labels_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        calibre2_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`calibre_role_docker_hostname`{ .sb-show-on-unchecked }`calibre2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_hostname: "{{ calibre_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_hostname: "{{ calibre_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`calibre_role_docker_networks_alias`{ .sb-show-on-unchecked }`calibre2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_networks_alias: "{{ calibre_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_networks_alias: "{{ calibre_name }}"
        ```

    ??? variable list "`calibre_role_docker_networks_default`{ .sb-show-on-unchecked }`calibre2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_networks_default: []
        ```

    ??? variable list "`calibre_role_docker_networks_custom`{ .sb-show-on-unchecked }`calibre2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_networks_custom: []
        ```

    <h5>Security Opts</h5>

    ??? variable list "`calibre_role_docker_security_opts_default`{ .sb-show-on-unchecked }`calibre2_docker_security_opts_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_security_opts_default:
          - seccomp=unconfined
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_security_opts_default: 
          - seccomp=unconfined
        ```

    ??? variable list "`calibre_role_docker_security_opts_custom`{ .sb-show-on-unchecked }`calibre2_docker_security_opts_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_security_opts_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_security_opts_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`calibre_role_docker_restart_policy`{ .sb-show-on-unchecked }`calibre2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`calibre_role_docker_state`{ .sb-show-on-unchecked }`calibre2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`calibre_role_autoheal_enabled`{ .sb-show-on-unchecked }`calibre2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        calibre_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        calibre2_autoheal_enabled: true
        ```

    ??? variable string "`calibre_role_depends_on`{ .sb-show-on-unchecked }`calibre2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        calibre_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        calibre2_depends_on: ""
        ```

    ??? variable string "`calibre_role_depends_on_delay`{ .sb-show-on-unchecked }`calibre2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        calibre_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        calibre2_depends_on_delay: "0"
        ```

    ??? variable string "`calibre_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`calibre2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        calibre_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        calibre2_depends_on_healthchecks:
        ```

    ??? variable bool "`calibre_role_diun_enabled`{ .sb-show-on-unchecked }`calibre2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        calibre_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        calibre2_diun_enabled: true
        ```

    ??? variable bool "`calibre_role_dns_enabled`{ .sb-show-on-unchecked }`calibre2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        calibre_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        calibre2_dns_enabled: true
        ```

    ??? variable bool "`calibre_role_docker_controller`{ .sb-show-on-unchecked }`calibre2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        calibre_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        calibre2_docker_controller: true
        ```

    ??? variable bool "`calibre_role_docker_volumes_download`{ .sb-show-on-unchecked }`calibre2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_volumes_download:
        ```

    ??? variable bool "`calibre_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        calibre2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`calibre_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        calibre2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`calibre_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        calibre2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`calibre_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        calibre2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`calibre_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`calibre2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`calibre_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`calibre2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`calibre_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        calibre_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        calibre2_traefik_robot_enabled: true
        ```

    ??? variable bool "`calibre_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        calibre_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        calibre2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`calibre_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`calibre2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        calibre_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        calibre2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`calibre_role_web_fqdn_override`{ .sb-show-on-unchecked }`calibre2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        calibre_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        calibre2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            calibre_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "calibre2.{{ user.domain }}"
              - "calibre.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            calibre2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "calibre2.{{ user.domain }}"
              - "calibre.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`calibre_role_web_host_override`{ .sb-show-on-unchecked }`calibre2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        calibre_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        calibre2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            calibre_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'calibre2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            calibre2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'calibre2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`calibre_role_web_scheme`{ .sb-show-on-unchecked }`calibre2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        calibre_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        calibre2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->