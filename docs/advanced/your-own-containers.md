---
hide:
  - tags
tags:
  - container
  - add
  - docker-compose
  - docker-run
  - docker
  - compose
---

# Adding your own containers to Saltbox

When you install existing roles in saltbox, some things get handled behind the scenes for you.  Notably, this includes creating the subdomain[s] at cloudflare and creating the `/opt/APPNAME` directory tree.

When you add a container manually as outlined on this page, neither of those things will be done for you (unless you have installed our ddns container), so prior to running the docker commands described below you will have to create the `APPNAME.domain.tld` subdomain at cloudflare [or wherever your DNS is] and create the required `/opt/APPNAME` directory tree.

If you want to create a role file that you can install like the built-in applications, see [contributing to sandbox apps](../sandbox/basics.md#contributing-to-sandbox-apps).

## Utilizing Generate Traefik Template

Create your application folder

    mkdir /opt/APPNAME

Run the Generate Traefik Template

    sb install generate-traefik-template

Once you've answered the required fields, Saltbox will create a file in `/tmp/docker-compose.yml`

Move the newly created `/tmp/docker-compose.yml` to the `/opt/APPNAME`

    mv /tmp/docker-compose.yml /opt/APPNAME

Once moved, modify `/opt/APPNAME/docker-compose.yml` to the requirements of your container. See IMPORTANT below.

IMPORTANT: In the examples below, `APPNAME`, `APPLICATION_PORT`, `/CONFIG`, and `DOCKER/IMAGE:TAG` are _placeholders_.  *You need to change those* **everywhere they appear** to match the application you are installing.

## Docker Compose

=== "Using Traefik (Authelia)"
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
          traefik.enable: true # (8)!
          traefik.http.routers.APPNAME-http.entrypoints: web # (9)!
          traefik.http.routers.APPNAME-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (10)!
          traefik.http.routers.APPNAME-http.rule: Host(`APPNAME.yourdomain.com`) # (11)!
          traefik.http.routers.APPNAME-http.service: APPNAME # (12)!
          traefik.http.routers.APPNAME.entrypoints: websecure # (13)!
          traefik.http.routers.APPNAME.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (14)!
          traefik.http.routers.APPNAME.rule: Host(`APPNAME.yourdomain.com`) # (15)!
          traefik.http.routers.APPNAME.service: APPNAME # (16)!
          traefik.http.routers.APPNAME.tls.certresolver: cfdns # (17)!
          traefik.http.routers.APPNAME.tls.options: securetls@file # (18)!
          traefik.http.services.APPNAME.loadbalancer.server.port: APPLICATION_PORT # (19)!
        volumes: # (20)!
          - /opt/APPNAME:/CONFIG
          - /etc/localtime:/etc/localtime:ro

    networks: # (21)!
      saltbox:
        external: true
    ```

    1.  Defines the containers restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  This label enables router creation in Traefik.
    9.  Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    10. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS make sure to include the redirect-to-https middleware.

    11. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    12. Defines which service the router should route traffic to.
    13. Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    14. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

    15. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    16. Defines which service the router should route traffic to.
    17. Defines the certificate resolver to use in order to generate a certificate.

        If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

        If you don't use Cloudflare with the URL used or another reason why it cannot use DNS validation use `httpresolver`.

        Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

    18. Defines the configuration used for SSL, leave this alone unless you know what you are doing.
    19. Defines which port Traefik routes the traffic to.
    20. Add any volume mounts the container needs.

        /host_path:/container_path

    21. This section tells docker compose that the network is managed outside of this compose file.

=== "Using Traefik (Authelia + API Router)"
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
          traefik.enable: true # (8)!
          traefik.http.routers.APPNAME-api-http.entrypoints: web # (9)!
          traefik.http.routers.APPNAME-api-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker # (10)!
          traefik.http.routers.APPNAME-api-http.priority: 99 # (11)!
          traefik.http.routers.APPNAME-api-http.rule: Host(`APPNAME.domain.tld`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (12)!
          traefik.http.routers.APPNAME-api-http.service: APPNAME # (13)!
          traefik.http.routers.APPNAME-api.entrypoints: websecure # (14)!
          traefik.http.routers.APPNAME-api.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker # (15)!
          traefik.http.routers.APPNAME-api.priority: 99 # (16)!
          traefik.http.routers.APPNAME-api.rule: Host(`APPNAME.domain.tld`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (17)!
          traefik.http.routers.APPNAME-api.service: APPNAME # (18)!
          traefik.http.routers.APPNAME-api.tls.certresolver: cfdns # (19)!
          traefik.http.routers.APPNAME-api.tls.options: securetls@file # (20)!
          traefik.http.routers.APPNAME-http.entrypoints: web # (21)!
          traefik.http.routers.APPNAME-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (22)!
          traefik.http.routers.APPNAME-http.rule: Host(`APPNAME.yourdomain.com`) # (23)!
          traefik.http.routers.APPNAME-http.service: APPNAME # (24)!
          traefik.http.routers.APPNAME.entrypoints: websecure # (25)!
          traefik.http.routers.APPNAME.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (26)!
          traefik.http.routers.APPNAME.rule: Host(`APPNAME.yourdomain.com`) # (27)!
          traefik.http.routers.APPNAME.service: APPNAME # (28)!
          traefik.http.routers.APPNAME.tls.certresolver: cfdns # (29)!
          traefik.http.routers.APPNAME.tls.options: securetls@file # (30)!
          traefik.http.services.APPNAME.loadbalancer.server.port: APPLICATION_PORT # (31)!
        volumes: # (32)!
          - /opt/APPNAME:/CONFIG
          - /etc/localtime:/etc/localtime:ro

    networks: # (33)!
      saltbox:
        external: true
    ```

    1.  Defines the containers restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  This label enables router creation in Traefik.
    9.  Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    10. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS make sure to include the redirect-to-https middleware.

    11. Defines router priority.

        If multiple router paths match a given address the one with the highest priority is used.

    12. This value defines which locations Traefik routes to the application.

        With the API Router we only add paths to the router that should go around Authelia.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    13. Defines which service the router should route traffic to.
    14. Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    15. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

    16. Defines router priority.

        If multiple router paths match a given address the one with the highest priority is used.

    17. This value defines which locations Traefik routes to the application.

        With the API Router we only add paths to the router that should go around Authelia.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    18. Defines which service the router should route traffic to.
    19. Defines the certificate resolver to use in order to generate a certificate.

        If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

        If you don't use Cloudflare with the URL used or another reason why it cannot use DNS validation use `httpresolver`.

        Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

    20. Defines the configuration used for SSL, leave this alone unless you know what you are doing.
    21. Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    22. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS make sure to include the redirect-to-https middleware.

    23. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    24. Defines which service the router should route traffic to.
    25. Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    26. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

    27. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    28. Defines which service the router should route traffic to.
    29. Defines the certificate resolver to use in order to generate a certificate.

        If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

        If you don't use Cloudflare with the URL used or another reason why it cannot use DNS validation use `httpresolver`.

        Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

    30. Defines the configuration used for SSL, leave this alone unless you know what you are doing.
    31. Defines which port Traefik routes the traffic to.
    32. Add any volume mounts the container needs.

        /host_path:/container_path

    33. This section tells docker compose that the network is managed outside of this compose file.

=== "Using Traefik"
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
          traefik.enable: true # (8)!
          traefik.http.routers.APPNAME-http.entrypoints: web # (9)!
          traefik.http.routers.APPNAME-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker # (10)!
          traefik.http.routers.APPNAME-http.rule: Host(`APPNAME.yourdomain.com`) # (11)!
          traefik.http.routers.APPNAME-http.service: APPNAME # (12)!
          traefik.http.routers.APPNAME.entrypoints: websecure # (13)!
          traefik.http.routers.APPNAME.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker # (14)!
          traefik.http.routers.APPNAME.rule: Host(`APPNAME.yourdomain.com`) # (15)!
          traefik.http.routers.APPNAME.service: APPNAME # (16)!
          traefik.http.routers.APPNAME.tls.certresolver: cfdns # (17)!
          traefik.http.routers.APPNAME.tls.options: securetls@file # (18)!
          traefik.http.services.APPNAME.loadbalancer.server.port: APPLICATION_PORT # (19)!
        volumes: # (20)!
          - /opt/APPNAME:/CONFIG
          - /etc/localtime:/etc/localtime:ro

    networks: # (21)!
      saltbox:
        external: true
    ```

    1.  Defines the containers restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  This label enables router creation in Traefik.
    9.  Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    10. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS make sure to include the redirect-to-https middleware.

    11. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    12. Defines which service the router should route traffic to.
    13. Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    14. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

    15. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    16. Defines which service the router should route traffic to.
    17. Defines the certificate resolver to use in order to generate a certificate.

        If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

        If you don't use Cloudflare with the URL used or another reason why it cannot use DNS validation use `httpresolver`.

        Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

    18. Defines the configuration used for SSL, leave this alone unless you know what you are doing.
    19. Defines which port Traefik routes the traffic to.
    20. Add any volume mounts the container needs.

        /host_path:/container_path

    21. This section tells docker compose that the network is managed outside of this compose file.

=== "Without Traefik"
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
        volumes: # (8)!
          - /opt/APPNAME:/CONFIG
          - /etc/localtime:/etc/localtime:ro

    networks: # (9)!
      saltbox:
        external: true
    ```

    1.  Defines the containers restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  Add any volume mounts the container needs.

        /host_path:/container_path

    9.  This section tells docker compose that the network is managed outside of this compose file.

## Creating and running the container

Once you have a docker-compose file as described above, you will use standard docker commands to create and run the container.

If the file is named `docker-compose.yml` and is located in the current working directory:

    docker compose up -d

If the file has some other name or is located elsewhere in the file system:

    docker compose -f /path/to/something.yml up -d

Remember to create the `APPNAME.domain.tld` subdomain at cloudflare [or wherever your DNS is] and create the required `/opt/APPNAME` directory tree prior to running that command.
