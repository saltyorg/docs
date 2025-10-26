---
hide:
  - tags
tags:
  - cli
  - compose
  - container
  - custom
  - docker
---

# Adding your own containers to Saltbox

Use this guide to extend your setup beyond the stock catalog. While arbitrary deployments fall outside our support scope, we offer resources to facilitate their integration with the Saltbox ecosystem.

## [Docker Compose:octicons-link-external-16:{ .sb-icon--sm }](https://docs.docker.com/reference/cli/docker/compose)

Recommended for GUI applications and web services.

1.  Run the interactive role to generate a Compose file with Traefik provisioning:

    ```sh
    sb install generate-traefik-template
    ```

    The file will be saved as `/tmp/docker-compose.yml`.

1.  Create the application directory (under `/opt` is recommended, for consistency and backup purposes)

    ```sh
    mkdir /opt/APPNAME
    ```

1.  It is recommended to store the Compose file in the root of the application directory:

    ```sh
    mv /tmp/docker-compose.yml /opt/APPNAME/compose.yaml
    ```

1.  Edit `/opt/APPNAME/compose.yaml` as appropriate for your application.

    - Always needs changing:

        ```yaml
        image: your_image:your_tag
        ```

    - Often needs changing:

        ```yaml hl_lines="2"
        environment:
          # (1)!
        ```

        1.  Set image-specific environment variables and remove unsupported ones          

        ```yaml hl_lines="2-3"
        volumes:
          - /opt/APPNAME:/config # (1)!
          # (2)!
        ```

        1.  Image may use a different path than `/config`

        2.  Set other volume mappings the image requires 

    ??? info "Cheat Sheet (some content may be outdated)"

        ```yaml
        services:
          APPNAME:
            restart: unless-stopped # (1)!
            container_name: APPNAME # (2)!
            image: DOCKER/IMAGE:TAG # (3)!
            hostname: APPNAME # (4)!
            environment: # (5)!
              - PUID=1000
              - PGID=1000
              - TZ=Etc/UTC
            networks: # (6)!
              - saltbox
            labels:
              com.github.saltbox.saltbox_managed: true # (7)!
              diun.enable: true # (8)!
              traefik.enable: true # (9)!
              traefik.http.routers.APPNAME-api-http.entrypoints: web # (10)!
              traefik.http.routers.APPNAME-api-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker # (11)!
              traefik.http.routers.APPNAME-api-http.priority: 99 # (12)!
              traefik.http.routers.APPNAME-api-http.rule: Host(`APPNAME.domain.tld`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (13)!
              traefik.http.routers.APPNAME-api-http.service: APPNAME # (14)!
              traefik.http.routers.APPNAME-api.entrypoints: websecure # (15)!
              traefik.http.routers.APPNAME-api.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker # (16)!
              traefik.http.routers.APPNAME-api.priority: 99 # (17)!
              traefik.http.routers.APPNAME-api.rule: Host(`APPNAME.domain.tld`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (18)!
              traefik.http.routers.APPNAME-api.service: APPNAME # (19)!
              traefik.http.routers.APPNAME-api.tls.certresolver: cfdns # (20)!
              traefik.http.routers.APPNAME-api.tls.options: securetls@file # (21)!
              traefik.http.routers.APPNAME-http.entrypoints: web # (22)!
              traefik.http.routers.APPNAME-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (23)!
              traefik.http.routers.APPNAME-http.rule: Host(`APPNAME.yourdomain.com`) # (24)!
              traefik.http.routers.APPNAME-http.service: APPNAME # (25)!
              traefik.http.routers.APPNAME.entrypoints: websecure # (26)!
              traefik.http.routers.APPNAME.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (27)!
              traefik.http.routers.APPNAME.rule: Host(`APPNAME.yourdomain.com`) # (28)!
              traefik.http.routers.APPNAME.service: APPNAME # (29)!
              traefik.http.routers.APPNAME.tls.certresolver: cfdns # (30)!
              traefik.http.routers.APPNAME.tls.options: securetls@file # (31)!
              traefik.http.services.APPNAME.loadbalancer.server.port: APPLICATION_PORT # (32)!
            volumes: # (33)!
              - /opt/APPNAME:/PATH/TO/CONFIG
              - /etc/localtime:/etc/localtime:ro # (34)!

        networks: # (35)!
          saltbox:
            external: true
        ```

        1.  Defines the container's restart policy.
            [Reference:octicons-link-external-16:{ .sb-icon--sm }](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

        2.  Defines the name of the container.

        3.  Defines the image and tag used when creating the container.

        4.  Defines the hostname used on the Docker network.

        5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

            While the TZ (Timezone) variable is used in pretty much all containers, you will have to figure out the rest as it can differ quite a bit between different containers.

        6.  Defines which Docker networks the container will join upon creation.

            We generally recommend using the saltbox network unless you know what you are doing.

        7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).

        8.  (Optional) If [diun](https://docs.saltbox.dev/apps/diun/) is installed, this label will allow the container to be monitored for updates.

        9.  This label enables router creation in Traefik.

        10. Defines the entrypoint used for the HTTP Traefik router.

            Leave as is unless you know what you are doing.

        11. Defines which middleware is used on the router.

            A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

            Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS, make sure to include the redirect-to-https middleware.

        12. Defines router priority.

            If multiple router paths match a given address, the one with the highest priority is used.

        13. This value defines which locations Traefik routes to the application.

            With the API Router, we only add paths to the router that should bypass Authelia.

            Docs: https://doc.traefik.io/traefik/routing/routers/#rule

        14. Defines which service the router should route traffic to.

        15. Defines the entrypoint used for the HTTP Traefik router.

            Leave as is unless you know what you are doing.

        16. Defines which middleware is used on the router.

            A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        17. Defines router priority.

            If multiple router paths match a given address, the one with the highest priority is used.

        18. This value defines which locations Traefik routes to the application.

            With the API Router, we only add paths to the router that should bypass Authelia.

            Docs: https://doc.traefik.io/traefik/routing/routers/#rule

        19. Defines which service the router should route traffic to.

        20. Defines the certificate resolver to use in order to generate a certificate.

            If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

            If you don't use Cloudflare with the URL used, or for another reason it cannot use DNS validation, use `httpresolver`.

            Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

        21. Defines the configuration used for SSL, leave this alone unless you know what you are doing.

        22. Defines the entrypoint used for the HTTP Traefik router.

            Leave as is unless you know what you are doing.

        23. Defines which middleware is used on the router.

            A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

            Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS, make sure to include the redirect-to-https middleware.

        24. This value defines which locations Traefik routes to the application.

            Docs: https://doc.traefik.io/traefik/routing/routers/#rule

        25. Defines which service the router should route traffic to.

        26. Defines the entrypoint used for the HTTP Traefik router.

            Leave as is unless you know what you are doing.

        27. Defines which middleware is used on the router.

            A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        28. This value defines which locations Traefik routes to the application.

            Docs: https://doc.traefik.io/traefik/routing/routers/#rule

        29. Defines which service the router should route traffic to.

        30. Defines the certificate resolver to use in order to generate a certificate.

            If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

            If you don't use Cloudflare with the URL used, or for another reason it cannot use DNS validation, use `httpresolver`.

            Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

        31. Defines the configuration used for SSL, leave this alone unless you know what you are doing.

        32. Defines which port Traefik routes the traffic to.

        33. Add any volume mounts the container needs.

            /host_path:/container_path

        34. Maps the host's timezone to the container's.

            This is an alternative to the `TZ` environment variable.

        35. This section tells Docker Compose that the network is managed outside of this compose file.

1.  Ensure a DNS A record exists that points to the application (e.g., `APPNAME.domain.tld`). This can be achieved by creating it manually, by running [DDNS](../apps/ddns.md) (Cloudflare only), or through a wildcard DNS record.

1.  Deploy and start the container:

    ```sh
    cd /opt/APPNAME
    docker compose up -d
    ```

## [Docker CLI:octicons-link-external-16:{ .sb-icon--sm }](https://docs.docker.com/reference/cli/docker/container/run)

Recommended for command‑line utilities where a container is invoked ad hoc or on a schedule.

While such containers can be run via Compose, you may prefer to avoid the extra files. Optionally, register them as functions in your shell environment, so they can be called in their native, host-level form.

=== "`~/.bashrc` `~/.zshrc`"

    ```sh
    APPNAME() {
      docker run --rm -it \
        DOCKER/IMAGE:TAG "$@"
    }
    ```

=== "Saltbox Inventory"

    ??? variable string "`shell_bash_bashrc_block_custom`"
    
        ```yaml
        shell_bash_bashrc_block_custom: |

          APPNAME() {
            docker run --rm -it \
              DOCKER/IMAGE:TAG "$@"
          }
        ```

    ??? variable string "`shell_zsh_zshrc_block_custom`"
    
        ```yaml
        shell_zsh_zshrc_block_custom: |

          APPNAME() {
            docker run --rm -it \
              DOCKER/IMAGE:TAG "$@"
          }
        ```

Then call from your regular shell with a command such as `APPNAME --help`.

!!! example

    === "`~/.bashrc` `~/.zshrc`"

        ```sh
        yt-dlp() {
          docker run --rm -it \
            -v "$(pwd)":/downloads:rw \
            -u $(id -u):$(id -g) \
            ghcr.io/jauderho/yt-dlp:latest "$@"
        }
        ```
    
        ```sh
        speedtest() {
          docker run --rm -it \
            gists/speedtest-cli "$@"
        }
        ```

    === "Saltbox Inventory"

        ??? variable string "`shell_bash_bashrc_block_custom`"
    
            ```yaml
            shell_bash_bashrc_block_custom: |

              yt-dlp() {
                docker run --rm -it \
                  -v "$(pwd)":/downloads:rw \
                  -u $(id -u):$(id -g) \
                ghcr.io/jauderho/yt-dlp:latest "$@"
              }
    
              speedtest() {
                docker run --rm -it \
                  gists/speedtest-cli "$@"
              }
            ```
    
        ??? variable string "`shell_zsh_zshrc_block_custom`"
    
            ```yaml
            shell_zsh_zshrc_block_custom: |

              yt-dlp() {
                docker run --rm -it \
                  -v "$(pwd)":/downloads:rw \
                  -u $(id -u):$(id -g) \
                ghcr.io/jauderho/yt-dlp:latest "$@"
              }
    
              speedtest() {
                docker run --rm -it \
                  gists/speedtest-cli "$@"
              }
            ```

    Call using `yt-dlp` and `speedtest` commands.

## [Ansible Roles:octicons-link-external-16:{ .sb-icon--sm }](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html)

Recommended when you need more automation and are comfortable working with [YAML:octicons-link-external-16:{ .sb-icon--sm }](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html) and [Jinja2:octicons-link-external-16:{ .sb-icon--sm }](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html).

[:fontawesome-brands-github: saltbox_mod](https://github.com/saltyorg/saltbox_mod){ .md-button }
