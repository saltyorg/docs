---
icon: material/play
title: Traefik Template
status: draft
hide:
  - tags
tags:
  - compose
  - custom
  - generate
  - template
saltbox_automation:
  sections:
    inventory: false
  project_description:
    name: Traefik Template
    summary: |-
      a Saltbox module that generates a Docker Compose template with Traefik publishing.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Traefik Template

## Overview

Traefik Template is a Saltbox module that generates a Docker Compose template with Traefik publishing.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install generate-traefik-template
```

## Usage

1.  Run the tag and answer the prompts. The file will be saved as `/tmp/docker-compose.yml` by default.

1.  Create the application directory (under `/opt` is recommended, for consistency and backup purposes)

    ```shell
    mkdir /opt/xCUSTOM_APP_NAMEx
    ```

1.  It is recommended to store the Compose file in the root of the application directory:

    ```shell
    mv /tmp/docker-compose.yml /opt/xCUSTOM_APP_NAMEx/compose.yaml
    ```

1.  Edit `/opt/xCUSTOM_APP_NAMEx/compose.yaml` as appropriate for your application.

    - Always needs changing:

        ``` { .yaml .no-copy }
        image: your_image:your_tag
        ```

    - Often needs changing:

        ``` { .yaml .no-copy hl_lines="2-4" }
        environment:
          # Remove unsupported environment variables and add image-specific ones, e.g.:
          SOME_SETTING: "myvalue" # (1)!
          OTHER_SETTING: "true"
        ```

        1. List syntax is also supported:

            ```yaml
            environment:
              - SOME_SETTING="myvalue"
              - OTHER_SETTING="true"
            ```

        ``` { .yaml .no-copy hl_lines="2-3" }
        volumes:
          - /opt/xCUSTOM_APP_NAMEx:/config # (1)!
          # Set other volume mappings the image requires
        ```

        1.  Image may use a different path than `/config`

    ??? info "Cheat Sheet (some content may be outdated)"

        ```yaml
        services:
          xCUSTOM_APP_NAMEx:
            restart: unless-stopped # (1)!
            container_name: xCUSTOM_APP_NAMEx # (2)!
            image: DOCKER/IMAGE:TAG # (3)!
            hostname: xCUSTOM_APP_NAMEx # (4)!
            environment: # (5)!
              PUID: "1000"
              PGID: "1000"
              TZ: "Etc/UTC"
            networks: # (6)!
              - saltbox
            labels:
              com.github.saltbox.saltbox_managed: true # (7)!
              diun.enable: true # (8)!
              traefik.enable: true # (9)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api-http.entrypoints: web # (10)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker # (11)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api-http.priority: 99 # (12)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api-http.rule: Host(`xCUSTOM_APP_NAMEx.xYOUR_DOMAIN_NAMEx`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (13)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api-http.service: xCUSTOM_APP_NAMEx # (14)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api.entrypoints: websecure # (15)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker # (16)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api.priority: 99 # (17)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api.rule: Host(`xCUSTOM_APP_NAMEx.xYOUR_DOMAIN_NAMEx`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (18)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api.service: xCUSTOM_APP_NAMEx # (19)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api.tls.certresolver: cfdns # (20)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-api.tls.options: securetls@file # (21)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-http.entrypoints: web # (22)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (23)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-http.rule: Host(`xCUSTOM_APP_NAMEx.xYOUR_DOMAIN_NAMEx`) # (24)!
              traefik.http.routers.xCUSTOM_APP_NAMEx-http.service: xCUSTOM_APP_NAMEx # (25)!
              traefik.http.routers.xCUSTOM_APP_NAMEx.entrypoints: websecure # (26)!
              traefik.http.routers.xCUSTOM_APP_NAMEx.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (27)!
              traefik.http.routers.xCUSTOM_APP_NAMEx.rule: Host(`xCUSTOM_APP_NAMEx.xYOUR_DOMAIN_NAMEx`) # (28)!
              traefik.http.routers.xCUSTOM_APP_NAMEx.service: xCUSTOM_APP_NAMEx # (29)!
              traefik.http.routers.xCUSTOM_APP_NAMEx.tls.certresolver: cfdns # (30)!
              traefik.http.routers.xCUSTOM_APP_NAMEx.tls.options: securetls@file # (31)!
              traefik.http.services.xCUSTOM_APP_NAMEx.loadbalancer.server.port: APPLICATION_PORT # (32)!
            volumes: # (33)!
              - /opt/xCUSTOM_APP_NAMEx:xCUSTOM_CONTAINER_APPDATA_PATHx
              - /etc/localtime:/etc/localtime:ro # (34)!

        networks: # (35)!
          saltbox:
            external: true
        ```

        1.  Defines the container's restart policy.
            [Reference:octicons-link-external-16:{ .md-icon--sm }](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

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

            A list of currently added middleware can be found on the Traefik dashboard (dash.xYOUR_DOMAIN_NAMEx).

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

            A list of currently added middleware can be found on the Traefik dashboard (dash.xYOUR_DOMAIN_NAMEx).

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

            A list of currently added middleware can be found on the Traefik dashboard (dash.xYOUR_DOMAIN_NAMEx).

            Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS, make sure to include the redirect-to-https middleware.

        24. This value defines which locations Traefik routes to the application.

            Docs: https://doc.traefik.io/traefik/routing/routers/#rule

        25. Defines which service the router should route traffic to.

        26. Defines the entrypoint used for the HTTP Traefik router.

            Leave as is unless you know what you are doing.

        27. Defines which middleware is used on the router.

            A list of currently added middleware can be found on the Traefik dashboard (dash.xYOUR_DOMAIN_NAMEx).

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

1.  Ensure a DNS A record exists that points to the application (e.g., `xCUSTOM_APP_FQDNx`). This can be achieved by creating it manually, by running [DDNS](../apps/ddns.md) (Cloudflare only), or through a wildcard DNS record.

1.  Deploy and start the container:

    ```shell
    cd /opt/xCUSTOM_APP_NAMEx
    docker compose up -d
    ```

1.  Assuming you have configured everything correctly, you can access your application at <https://iCUSTOM_APP_FQDNi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
