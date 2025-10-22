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

When you install existing roles in Saltbox, some things get handled behind the scenes for you. Notably, this includes creating the subdomain[s] at Cloudflare and creating the `/opt/xAPP_NAMEx` directory tree.

When you add a container manually as outlined on this page, neither of those things will be done for you (unless you have installed our ddns container), so prior to running the docker commands described below you will have to create the `xAPP_NAMEx.domain.tld` subdomain at Cloudflare [or wherever your DNS is] and create the required `/opt/xAPP_NAMEx` directory tree.

!!! info "Two approaches available"
    - **Recommended:** Use the [Generate Traefik Template](#utilizing-generate-traefik-template-recommended) for the easiest setup
    - **Advanced:** Manually create docker-compose files using the [templates below](#docker-compose-manual-setup)

If you want to create a role file that you can install like the built-in applications, see [contributing to sandbox apps](../sandbox/basics.md#contributing-to-sandbox-apps).

## Utilizing Generate Traefik Template (Recommended)

!!! tip "Easiest Method"
    Using the Generate Traefik Template is the **easiest and preferred way** to get started with adding your own containers to Saltbox. This tool will automatically generate a properly configured docker-compose file for you.

1. Create your application folder:

    ```shell
    mkdir /opt/xAPP_NAMEx
    ```

2. Run the Generate Traefik Template:

    ```shell
    sb install generate-traefik-template
    ```

3. Answer the prompts for your container configuration. Saltbox will create a file at `/tmp/docker-compose.yml`

4. Move the generated file to your application directory:

    ```shell
    mv /tmp/docker-compose.yml /opt/xAPP_NAMEx/
    ```

5. Edit `/opt/xAPP_NAMEx/docker-compose.yml` to customize it for your specific container requirements.

6. Start your container:

    ```shell
    cd /opt/xAPP_NAMEx
    docker compose up -d
    ```

!!! note
    The generated template includes all the necessary Traefik labels and Saltbox-specific configurations. You'll only need to modify the image name, ports, volumes, and environment variables specific to your application.

## Docker Compose (Manual Setup)

<label>Enter domain name: <input data-input-for="DOMAIN_NAME"></label>

<label>Enter application name: <input data-input-for="APP_NAME"></label>

<label>Enter application Docker image repo: <input data-input-for="DOCKER_IMAGE_REPO"></label>

<label>Enter application Docker image tag: <input data-input-for="DOCKER_IMAGE_TAG"></label>

<label>Enter web port: <input data-input-for="APP_WEB_PORT"></label>

<label>Enter in-container appdata path: <input data-input-for="INTERNAL_APPDATA_PATH"></label>

<label for="www"><input type="checkbox" id="www" data-input-for="APP_URL_TOGGLE"> Reveal your dAPP_NAMEd URL</label>: 

[dAPP_URL_TOGGLEd](https://iFQDNi)

=== "Using Traefik (Authelia)"
    ```yaml
    services:
      xAPP_NAMEx:
        restart: unless-stopped # (1)!
        container_name: xAPP_NAMEx # (2)!
        image: xDOCKER_IMAGE_REPOx:xDOCKER_IMAGE_TAGx # (3)!
        hostname: xAPP_NAMEx # (4)!
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
          traefik.http.routers.xAPP_NAMEx-http.entrypoints: web # (10)!
          traefik.http.routers.xAPP_NAMEx-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (11)!
          traefik.http.routers.xAPP_NAMEx-http.rule: Host(`xAPP_NAMEx.xDOMAIN_NAMEx`) # (12)!
          traefik.http.routers.xAPP_NAMEx-http.service: xAPP_NAMEx # (13)!
          traefik.http.routers.xAPP_NAMEx.entrypoints: websecure # (14)!
          traefik.http.routers.xAPP_NAMEx.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (15)!
          traefik.http.routers.xAPP_NAMEx.rule: Host(`xAPP_NAMEx.xDOMAIN_NAMEx`) # (16)!
          traefik.http.routers.xAPP_NAMEx.service: xAPP_NAMEx # (17)!
          traefik.http.routers.xAPP_NAMEx.tls.certresolver: cfdns # (18)!
          traefik.http.routers.xAPP_NAMEx.tls.options: securetls@file # (19)!
          traefik.http.services.xAPP_NAMEx.loadbalancer.server.port: xAPP_WEB_PORTx # (20)!
        volumes: # (21)!
          - /opt/xAPP_NAMEx:xINTERNAL_APPDATA_PATHx
          - /etc/localtime:/etc/localtime:ro

    networks: # (22)!
      saltbox:
        external: true
    ```

    1.  Defines the container's restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers, you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  (Optional) If [diun](https://docs.saltbox.dev/apps/diun/) is installed, this label will allow the container to be monitored for updates
    9.  This label enables router creation in Traefik.
    10.  Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    11. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS, make sure to include the redirect-to-https middleware.

    12. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    13. Defines which service the router should route traffic to.
    14. Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    15. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

    16. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    17. Defines which service the router should route traffic to.
    18. Defines the certificate resolver to use in order to generate a certificate.

        If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

        If you don't use Cloudflare with the URL used, or for another reason it cannot use DNS validation, use `httpresolver`.

        Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

    19. Defines the configuration used for SSL; leave this alone unless you know what you are doing.
    20. Defines which port Traefik routes the traffic to.
    21. Add any volume mounts the container needs.

        /host_path:/container_path

    22. This section tells Docker Compose that the network is managed outside of this compose file.

=== "Using Traefik (Authelia + API Router)"
    ```yaml
    services:
      xAPP_NAMEx:
        restart: unless-stopped # (1)!
        container_name: xAPP_NAMEx # (2)!
        image: xDOCKER_IMAGE_REPOx:xDOCKER_IMAGE_TAGx # (3)!
        hostname: xAPP_NAMEx # (4)!
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
          traefik.http.routers.xAPP_NAMEx-api-http.entrypoints: web # (10)!
          traefik.http.routers.xAPP_NAMEx-api-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker # (11)!
          traefik.http.routers.xAPP_NAMEx-api-http.priority: 99 # (12)!
          traefik.http.routers.xAPP_NAMEx-api-http.rule: Host(`xAPP_NAMEx.domain.tld`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (13)!
          traefik.http.routers.xAPP_NAMEx-api-http.service: xAPP_NAMEx # (14)!
          traefik.http.routers.xAPP_NAMEx-api.entrypoints: websecure # (15)!
          traefik.http.routers.xAPP_NAMEx-api.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker # (16)!
          traefik.http.routers.xAPP_NAMEx-api.priority: 99 # (17)!
          traefik.http.routers.xAPP_NAMEx-api.rule: Host(`xAPP_NAMEx.domain.tld`) && (PathPrefix(`/api`) || PathPrefix(`/ping`)) # (18)!
          traefik.http.routers.xAPP_NAMEx-api.service: xAPP_NAMEx # (19)!
          traefik.http.routers.xAPP_NAMEx-api.tls.certresolver: cfdns # (20)!
          traefik.http.routers.xAPP_NAMEx-api.tls.options: securetls@file # (21)!
          traefik.http.routers.xAPP_NAMEx-http.entrypoints: web # (22)!
          traefik.http.routers.xAPP_NAMEx-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (23)!
          traefik.http.routers.xAPP_NAMEx-http.rule: Host(`xAPP_NAMEx.xDOMAIN_NAMEx`) # (24)!
          traefik.http.routers.xAPP_NAMEx-http.service: xAPP_NAMEx # (25)!
          traefik.http.routers.xAPP_NAMEx.entrypoints: websecure # (26)!
          traefik.http.routers.xAPP_NAMEx.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker,authelia@docker # (27)!
          traefik.http.routers.xAPP_NAMEx.rule: Host(`xAPP_NAMEx.xDOMAIN_NAMEx`) # (28)!
          traefik.http.routers.xAPP_NAMEx.service: xAPP_NAMEx # (29)!
          traefik.http.routers.xAPP_NAMEx.tls.certresolver: cfdns # (30)!
          traefik.http.routers.xAPP_NAMEx.tls.options: securetls@file # (31)!
          traefik.http.services.xAPP_NAMEx.loadbalancer.server.port: xAPP_WEB_PORTx # (32)!
        volumes: # (33)!
          - /opt/xAPP_NAMEx:xINTERNAL_APPDATA_PATHx
          - /etc/localtime:/etc/localtime:ro

    networks: # (34)!
      saltbox:
        external: true
    ```

    1.  Defines the container's restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers, you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  (Optional) If [diun](https://docs.saltbox.dev/apps/diun/) is installed, this label will allow the container to be monitored for updates
    9.  This label enables router creation in Traefik.
    10.  Defines the entrypoint used for the HTTP Traefik router.
    
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

    34. This section tells Docker Compose that the network is managed outside of this compose file.

=== "Using Traefik"
    ```yaml
    services:
      xAPP_NAMEx:
        restart: unless-stopped # (1)!
        container_name: xAPP_NAMEx # (2)!
        image: xDOCKER_IMAGE_REPOx:xDOCKER_IMAGE_TAGx # (3)!
        hostname: xAPP_NAMEx # (4)!
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
          traefik.http.routers.xAPP_NAMEx-http.entrypoints: web # (10)!
          traefik.http.routers.xAPP_NAMEx-http.middlewares: globalHeaders@file,redirect-to-https@docker,robotHeaders@file,cloudflarewarp@docker # (11)!
          traefik.http.routers.xAPP_NAMEx-http.rule: Host(`xAPP_NAMEx.xDOMAIN_NAMEx`) # (12)!
          traefik.http.routers.xAPP_NAMEx-http.service: xAPP_NAMEx # (13)!
          traefik.http.routers.xAPP_NAMEx.entrypoints: websecure # (14)!
          traefik.http.routers.xAPP_NAMEx.middlewares: globalHeaders@file,secureHeaders@file,robotHeaders@file,cloudflarewarp@docker # (15)!
          traefik.http.routers.xAPP_NAMEx.rule: Host(`xAPP_NAMEx.xDOMAIN_NAMEx`) # (16)!
          traefik.http.routers.xAPP_NAMEx.service: xAPP_NAMEx # (17)!
          traefik.http.routers.xAPP_NAMEx.tls.certresolver: cfdns # (18)!
          traefik.http.routers.xAPP_NAMEx.tls.options: securetls@file # (19)!
          traefik.http.services.xAPP_NAMEx.loadbalancer.server.port: xAPP_WEB_PORTx # (20)!
        volumes: # (21)!
          - /opt/xAPP_NAMEx:xINTERNAL_APPDATA_PATHx
          - /etc/localtime:/etc/localtime:ro

    networks: # (22)!
      saltbox:
        external: true
    ```

    1.  Defines the container's restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers, you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  (Optional) If [diun](https://docs.saltbox.dev/apps/diun/) is installed, this label will allow the container to be monitored for updates
    9.  This label enables router creation in Traefik.
    10.  Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    11. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

        Unless you intend to allow HTTP traffic instead of auto-upgrading to HTTPS, make sure to include the redirect-to-https middleware.

    12. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    13. Defines which service the router should route traffic to.
    14. Defines the entrypoint used for the HTTP Traefik router.
    
        Leave as is unless you know what you are doing.

    15. Defines which middleware is used on the router.

        A list of currently added middleware can be found on the Traefik dashboard (dash.domain.tld).

    16. This value defines which locations Traefik routes to the application.

        Docs: https://doc.traefik.io/traefik/routing/routers/#rule

    17. Defines which service the router should route traffic to.
    18. Defines the certificate resolver to use in order to generate a certificate.

        If the url is using Cloudflare, with the same account as Saltbox uses, the value should be `cfdns`.

        If you don't use Cloudflare with the URL used, or for another reason it cannot use DNS validation, use `httpresolver`.

        Remember to enable http_validation in the adv_settings.yml config to enable the httpresolver when using Cloudflare.

    19. Defines the configuration used for SSL; leave this alone unless you know what you are doing.
    20. Defines which port Traefik routes the traffic to.
    21. Add any volume mounts the container needs.

        /host_path:/container_path

    22. This section tells Docker Compose that the network is managed outside of this compose file.

=== "Without Traefik"
    ```yaml
    services:
      xAPP_NAMEx:
        restart: unless-stopped # (1)!
        container_name: xAPP_NAMEx # (2)!
        image: xDOCKER_IMAGE_REPOx:xDOCKER_IMAGE_TAGx # (3)!
        hostname: xAPP_NAMEx # (4)!
        environment: # (5)!
          - PUID=1000
          - PGID=1000
          - TZ=Etc/UTC
        networks: # (6)!
          - saltbox
        labels:
          com.github.saltbox.saltbox_managed: true # (7)!
          diun.enable: true # (8)!
        volumes: # (9)!
          - /opt/xAPP_NAMEx:xINTERNAL_APPDATA_PATHx
          - /etc/localtime:/etc/localtime:ro

    networks: # (10)!
      saltbox:
        external: true
    ```

    1.  Defines the container's restart policy.

        [Reference](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy)

    2.  Defines the name of the container.
    3.  Defines the image and tag used when creating the container.
    4.  Defines the hostname used on the Docker network.
    5.  Defines the environment variables which are often used to change configuration of the underlying application inside of the container.

        While the TZ (Timezone) variable is used in pretty much all containers, you will have to figure out the rest as it can differ quite a bit between different containers.

    6.  Defines which Docker networks the container will join upon creation.

        We generally recommend using the saltbox network unless you know what you are doing.

    7.  This label will tell Saltbox to manage the container during backups (stopping and starting it).
    8.  (Optional) If [diun](https://docs.saltbox.dev/apps/diun/) is installed, this label will allow the container to be monitored for updates
    9.  Add any volume mounts the container needs.

        /host_path:/container_path

    10.  This section tells Docker Compose that the network is managed outside of this compose file.

## Creating and running the container

Once you have a docker-compose file as described above, you will use standard Docker commands to create and run the container.

If the file is named `docker-compose.yml` and is located in the current working directory:

```shell
docker compose up -d
```

If the file has some other name or is located elsewhere in the file system:

```shell
docker compose -f /path/to/something.yml up -d
```

Remember to create the `xAPP_NAMEx.domain.tld` subdomain at Cloudflare [or wherever your DNS is] and create the required `/opt/xAPP_NAMEx` directory tree prior to running that command.
