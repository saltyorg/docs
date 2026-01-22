---
icon: material/docker
hide:
  - tags
tags:
  - calibre
  - ebooks
  - management
saltbox_automation:
  app_links:
    - name: Manual
      url: https://manual.calibre-ebook.com
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/calibre/tags
      type: docker
    - name: Community
      url: https://linuxserver.io/discord
      type: discord
  project_description:
    name: Calibre
    summary: |-
      a cross-platform, free, and open-source suite of e-book software designed for managing digital book collections.
    link: https://calibre-ebook.com
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Calibre

## Overview

[Calibre](https://calibre-ebook.com) is a cross-platform, free, and open-source suite of e-book software designed for managing digital book collections.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://manual.calibre-ebook.com){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/calibre/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-calibre
```

## Usage

Visit <https://calibre.iYOUR_DOMAIN_NAMEi>.

## Basics

- The username and password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

- The second books url serves the Calibre Content server and has a default user of abc and password abc, so make sure to remove/edit that user and enable 'Require username and password to access the Content server' otherwise it will be completely open.

- Calibre is ready for use. If you added your pre-existing Calibre library to /mnt/local/Media/Books then you should see your library is ready to go. If not, then you have a blank library ready for you to fill.

!!! info
    Running Calibre on a headless server is not very fun. If at all possible, run Calibre on your local, home computer. Use rclone to sync the files from home to google drive, and then another sync from google drive to your server so that Calibre-Web can use it.

    A local database file is required. This means you cannot run either Calibre or Calibre-Web from a mounted teamdrive, and this is the biggest pain for many of us. The easiest solution is to simply have your database and book files all located in /mnt/local/Media/Books.

    Both Calibre and Calibre-Web expect to find your library in `/mnt/unionfs/Media/Books`. Note that per standard Saltbox setup, `/mnt/local` is included inside `/mnt/unionfs`. However, both dockers also include access to anything in your `/mnt` directory.

### Handy commands for managing your calibre docker

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
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override level"><input type="checkbox" name="scope" hidden/></label>

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `calibre_instances`.**

    !!! example "Example override"

        === "Role-level"

            ```yaml
            calibre_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of calibre

        === "Instance-level"

            ```yaml
            calibre2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named calibre2

    !!! warning "Avoid overriding variables ending in `_default`"

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

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`calibre_role_docker_blkio_weight`{ .sb-show-on-unchecked }`calibre2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_blkio_weight:
        ```

    ??? variable int "`calibre_role_docker_cpu_period`{ .sb-show-on-unchecked }`calibre2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_cpu_period:
        ```

    ??? variable int "`calibre_role_docker_cpu_quota`{ .sb-show-on-unchecked }`calibre2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_cpu_quota:
        ```

    ??? variable int "`calibre_role_docker_cpu_shares`{ .sb-show-on-unchecked }`calibre2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_cpu_shares:
        ```

    ??? variable string "`calibre_role_docker_cpus`{ .sb-show-on-unchecked }`calibre2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_cpus:
        ```

    ??? variable string "`calibre_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`calibre2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_cpuset_cpus:
        ```

    ??? variable string "`calibre_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`calibre2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_cpuset_mems:
        ```

    ??? variable string "`calibre_role_docker_kernel_memory`{ .sb-show-on-unchecked }`calibre2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_kernel_memory:
        ```

    ??? variable string "`calibre_role_docker_memory`{ .sb-show-on-unchecked }`calibre2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_memory:
        ```

    ??? variable string "`calibre_role_docker_memory_reservation`{ .sb-show-on-unchecked }`calibre2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_memory_reservation:
        ```

    ??? variable string "`calibre_role_docker_memory_swap`{ .sb-show-on-unchecked }`calibre2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_memory_swap:
        ```

    ??? variable int "`calibre_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`calibre2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_memory_swappiness:
        ```

    ??? variable string "`calibre_role_docker_shm_size`{ .sb-show-on-unchecked }`calibre2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`calibre_role_docker_cap_drop`{ .sb-show-on-unchecked }`calibre2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_cap_drop:
        ```

    ??? variable string "`calibre_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`calibre2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_cgroupns_mode:
        ```

    ??? variable list "`calibre_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`calibre2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_device_cgroup_rules:
        ```

    ??? variable list "`calibre_role_docker_device_read_bps`{ .sb-show-on-unchecked }`calibre2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_device_read_bps:
        ```

    ??? variable list "`calibre_role_docker_device_read_iops`{ .sb-show-on-unchecked }`calibre2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_device_read_iops:
        ```

    ??? variable list "`calibre_role_docker_device_requests`{ .sb-show-on-unchecked }`calibre2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_device_requests:
        ```

    ??? variable list "`calibre_role_docker_device_write_bps`{ .sb-show-on-unchecked }`calibre2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_device_write_bps:
        ```

    ??? variable list "`calibre_role_docker_device_write_iops`{ .sb-show-on-unchecked }`calibre2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_device_write_iops:
        ```

    ??? variable list "`calibre_role_docker_devices`{ .sb-show-on-unchecked }`calibre2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_devices:
        ```

    ??? variable string "`calibre_role_docker_devices_default`{ .sb-show-on-unchecked }`calibre2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_devices_default:
        ```

    ??? variable list "`calibre_role_docker_groups`{ .sb-show-on-unchecked }`calibre2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_groups:
        ```

    ??? variable bool "`calibre_role_docker_privileged`{ .sb-show-on-unchecked }`calibre2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_privileged:
        ```

    ??? variable string "`calibre_role_docker_user`{ .sb-show-on-unchecked }`calibre2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_user:
        ```

    ??? variable string "`calibre_role_docker_userns_mode`{ .sb-show-on-unchecked }`calibre2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`calibre_role_docker_dns_opts`{ .sb-show-on-unchecked }`calibre2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_dns_opts:
        ```

    ??? variable list "`calibre_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`calibre2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_dns_search_domains:
        ```

    ??? variable list "`calibre_role_docker_dns_servers`{ .sb-show-on-unchecked }`calibre2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_dns_servers:
        ```

    ??? variable string "`calibre_role_docker_domainname`{ .sb-show-on-unchecked }`calibre2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_domainname:
        ```

    ??? variable list "`calibre_role_docker_exposed_ports`{ .sb-show-on-unchecked }`calibre2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_exposed_ports:
        ```

    ??? variable dict "`calibre_role_docker_hosts`{ .sb-show-on-unchecked }`calibre2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        calibre_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        calibre2_docker_hosts:
        ```

    ??? variable bool "`calibre_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`calibre2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_hosts_use_common:
        ```

    ??? variable string "`calibre_role_docker_ipc_mode`{ .sb-show-on-unchecked }`calibre2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_ipc_mode:
        ```

    ??? variable list "`calibre_role_docker_links`{ .sb-show-on-unchecked }`calibre2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_links:
        ```

    ??? variable string "`calibre_role_docker_network_mode`{ .sb-show-on-unchecked }`calibre2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_network_mode:
        ```

    ??? variable string "`calibre_role_docker_pid_mode`{ .sb-show-on-unchecked }`calibre2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_pid_mode:
        ```

    ??? variable list "`calibre_role_docker_ports`{ .sb-show-on-unchecked }`calibre2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_ports:
        ```

    ??? variable string "`calibre_role_docker_uts`{ .sb-show-on-unchecked }`calibre2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`calibre_role_docker_keep_volumes`{ .sb-show-on-unchecked }`calibre2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_keep_volumes:
        ```

    ??? variable list "`calibre_role_docker_mounts`{ .sb-show-on-unchecked }`calibre2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_mounts:
        ```

    ??? variable dict "`calibre_role_docker_storage_opts`{ .sb-show-on-unchecked }`calibre2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        calibre_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        calibre2_docker_storage_opts:
        ```

    ??? variable list "`calibre_role_docker_tmpfs`{ .sb-show-on-unchecked }`calibre2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_tmpfs:
        ```

    ??? variable string "`calibre_role_docker_volume_driver`{ .sb-show-on-unchecked }`calibre2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_volume_driver:
        ```

    ??? variable list "`calibre_role_docker_volumes_from`{ .sb-show-on-unchecked }`calibre2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_volumes_from:
        ```

    ??? variable bool "`calibre_role_docker_volumes_global`{ .sb-show-on-unchecked }`calibre2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_volumes_global:
        ```

    ??? variable string "`calibre_role_docker_working_dir`{ .sb-show-on-unchecked }`calibre2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`calibre_role_docker_auto_remove`{ .sb-show-on-unchecked }`calibre2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_auto_remove:
        ```

    ??? variable bool "`calibre_role_docker_cleanup`{ .sb-show-on-unchecked }`calibre2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_cleanup:
        ```

    ??? variable string "`calibre_role_docker_force_kill`{ .sb-show-on-unchecked }`calibre2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_force_kill:
        ```

    ??? variable dict "`calibre_role_docker_healthcheck`{ .sb-show-on-unchecked }`calibre2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        calibre_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        calibre2_docker_healthcheck:
        ```

    ??? variable int "`calibre_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`calibre2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`calibre_role_docker_init`{ .sb-show-on-unchecked }`calibre2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_init:
        ```

    ??? variable string "`calibre_role_docker_kill_signal`{ .sb-show-on-unchecked }`calibre2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_kill_signal:
        ```

    ??? variable string "`calibre_role_docker_log_driver`{ .sb-show-on-unchecked }`calibre2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_log_driver:
        ```

    ??? variable dict "`calibre_role_docker_log_options`{ .sb-show-on-unchecked }`calibre2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        calibre_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        calibre2_docker_log_options:
        ```

    ??? variable bool "`calibre_role_docker_oom_killer`{ .sb-show-on-unchecked }`calibre2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_oom_killer:
        ```

    ??? variable int "`calibre_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`calibre2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_oom_score_adj:
        ```

    ??? variable bool "`calibre_role_docker_output_logs`{ .sb-show-on-unchecked }`calibre2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_output_logs:
        ```

    ??? variable bool "`calibre_role_docker_paused`{ .sb-show-on-unchecked }`calibre2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_paused:
        ```

    ??? variable bool "`calibre_role_docker_recreate`{ .sb-show-on-unchecked }`calibre2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_recreate:
        ```

    ??? variable int "`calibre_role_docker_restart_retries`{ .sb-show-on-unchecked }`calibre2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_restart_retries:
        ```

    ??? variable int "`calibre_role_docker_stop_timeout`{ .sb-show-on-unchecked }`calibre2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`calibre_role_docker_capabilities`{ .sb-show-on-unchecked }`calibre2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_capabilities:
        ```

    ??? variable string "`calibre_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`calibre2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_cgroup_parent:
        ```

    ??? variable list "`calibre_role_docker_commands`{ .sb-show-on-unchecked }`calibre2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_commands:
        ```

    ??? variable int "`calibre_role_docker_create_timeout`{ .sb-show-on-unchecked }`calibre2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        calibre_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        calibre2_docker_create_timeout:
        ```

    ??? variable string "`calibre_role_docker_entrypoint`{ .sb-show-on-unchecked }`calibre2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_entrypoint:
        ```

    ??? variable string "`calibre_role_docker_env_file`{ .sb-show-on-unchecked }`calibre2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_env_file:
        ```

    ??? variable bool "`calibre_role_docker_labels_use_common`{ .sb-show-on-unchecked }`calibre2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_labels_use_common:
        ```

    ??? variable bool "`calibre_role_docker_read_only`{ .sb-show-on-unchecked }`calibre2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        calibre_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        calibre2_docker_read_only:
        ```

    ??? variable string "`calibre_role_docker_runtime`{ .sb-show-on-unchecked }`calibre2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_docker_runtime:
        ```

    ??? variable list "`calibre_role_docker_sysctls`{ .sb-show-on-unchecked }`calibre2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_sysctls:
        ```

    ??? variable list "`calibre_role_docker_ulimits`{ .sb-show-on-unchecked }`calibre2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_ulimits:
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

    ??? variable list "`calibre_role_docker_networks_alias_custom`{ .sb-show-on-unchecked }`calibre2_docker_networks_alias_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        calibre_role_docker_networks_alias_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        calibre2_docker_networks_alias_custom:
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

    ??? variable string "`calibre_role_themepark_addons`{ .sb-show-on-unchecked }`calibre2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_themepark_addons:
        ```

    ??? variable string "`calibre_role_themepark_app`{ .sb-show-on-unchecked }`calibre2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_themepark_app:
        ```

    ??? variable string "`calibre_role_themepark_theme`{ .sb-show-on-unchecked }`calibre2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_themepark_theme:
        ```

    ??? variable dict "`calibre_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`calibre2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        calibre_role_traefik_api_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        calibre2_traefik_api_endpoint:
        ```

    ??? variable string "`calibre_role_traefik_api_middleware`{ .sb-show-on-unchecked }`calibre2_traefik_api_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_api_middleware:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_api_middleware:
        ```

    ??? variable string "`calibre_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`calibre2_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_api_middleware_http:
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

    ??? variable string "`calibre_role_traefik_middleware_http`{ .sb-show-on-unchecked }`calibre2_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_middleware_http:
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

    ??? variable string "`calibre_role_traefik_priority`{ .sb-show-on-unchecked }`calibre2_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        calibre_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        calibre2_traefik_priority:
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

    ??? variable string "`calibre_role_web_api_http_port`{ .sb-show-on-unchecked }`calibre2_web_api_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        calibre_role_web_api_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        calibre2_web_api_http_port:
        ```

    ??? variable string "`calibre_role_web_api_http_scheme`{ .sb-show-on-unchecked }`calibre2_web_api_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        calibre_role_web_api_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        calibre2_web_api_http_scheme:
        ```

    ??? variable dict "`calibre_role_web_api_http_serverstransport`{ .sb-show-on-unchecked }`calibre2_web_api_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        calibre_role_web_api_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        calibre2_web_api_http_serverstransport:
        ```

    ??? variable string "`calibre_role_web_api_port`{ .sb-show-on-unchecked }`calibre2_web_api_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        calibre_role_web_api_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        calibre2_web_api_port:
        ```

    ??? variable string "`calibre_role_web_api_scheme`{ .sb-show-on-unchecked }`calibre2_web_api_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        calibre_role_web_api_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        calibre2_web_api_scheme:
        ```

    ??? variable dict "`calibre_role_web_api_serverstransport`{ .sb-show-on-unchecked }`calibre2_web_api_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        calibre_role_web_api_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        calibre2_web_api_serverstransport:
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


    ??? variable string "`calibre_role_web_http_port`{ .sb-show-on-unchecked }`calibre2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        calibre_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        calibre2_web_http_port:
        ```

    ??? variable string "`calibre_role_web_http_scheme`{ .sb-show-on-unchecked }`calibre2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        calibre_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        calibre2_web_http_scheme:
        ```

    ??? variable dict "`calibre_role_web_http_serverstransport`{ .sb-show-on-unchecked }`calibre2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        calibre_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        calibre2_web_http_serverstransport:
        ```

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

    ??? variable dict "`calibre_role_web_serverstransport`{ .sb-show-on-unchecked }`calibre2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        calibre_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        calibre2_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
