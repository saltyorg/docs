
# Adding your own containers to Saltbox

When you install existing roles in saltbox, some things get handled behind the scenes for you.  Notably, this includes creating the subdomain[s] at cloudflare and creating the `/opt/APPNAME` directory tree.

When you add a container manually as outlined on this page, neither of those things will be done for you (unless you have installed our ddns container), so prior to running the docker commands described below you will have to create the `APPNAME.domain.tld` subdomain at cloudflare [or wherever your DNS is] and create the required `/opt/APPNAME` directory tree.

If you want to create a role file that you can install like the built-in applications, see [here](../sandbox/basics.md#contributing-to-sandbox-apps).

## Docker Compose

=== "Using Traefik (Authelia)"
    ```yaml
    version: "3"
    services:
      APPNAME:
        restart: unless-stopped # (1)!
        container_name: APPNAME # (2)!
        image: docker/image:tag # (3)!
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
          traefik.http.routers.APPNAME-http.middlewares: globalHeaders@file,redirect-to-https,authelia@docker # (10)!
          traefik.http.routers.APPNAME-http.rule: Host(`APPNAME.yourdomain.com`) # (11)!
          traefik.http.routers.APPNAME-http.service: APPNAME # (12)!
          traefik.http.routers.APPNAME.entrypoints: websecure # (13)!
          traefik.http.routers.APPNAME.middlewares: globalHeaders@file,secureHeaders@file,authelia@docker # (14)!
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
    
    10.  placeholder
    11.  placeholder
    12.  placeholder
    13.  placeholder
    14.  placeholder
    15.  placeholder
    16.  placeholder
    17.  placeholder
    18.  placeholder
    19.  placeholder
    20.  placeholder
    21.  placeholder

=== "Using Traefik"
    ```yaml
    version: "3"
    services:
      APPNAME:
        restart: unless-stopped # (1)!
        container_name: APPNAME # (2)!
        image: docker/image:tag # (3)!
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
          traefik.http.routers.APPNAME-http.middlewares: globalHeaders@file,redirect-to-https # (10)!
          traefik.http.routers.APPNAME-http.rule: Host(`APPNAME.yourdomain.com`) # (11)!
          traefik.http.routers.APPNAME-http.service: APPNAME # (12)!
          traefik.http.routers.APPNAME.entrypoints: websecure # (13)!
          traefik.http.routers.APPNAME.middlewares: globalHeaders@file,secureHeaders@file # (14)!
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
    9.  Defines the entrypoint used for the HTTP Traefik router. Leave as is.
    10.  placeholder
    11.  placeholder
    12.  placeholder
    13.  placeholder
    14.  placeholder
    15.  placeholder
    16.  placeholder
    17.  placeholder
    18.  placeholder
    19.  placeholder
    20.  placeholder
    21.  placeholder

=== "Without Traefik"
    ```yaml
    version: "3"
    services:
      APPNAME:
        restart: unless-stopped # (1)!
        container_name: APPNAME # (2)!
        image: docker/image:tag # (3)!
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

    1.  placeholder
    2.  placeholder
    3.  placeholder
    4.  placeholder
    5.  placeholder
    6.  placeholder
    7.  placeholder
    8.  placeholder
    9.  placeholder
