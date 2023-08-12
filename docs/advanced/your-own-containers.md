
# Adding your own containers to Saltbox

When you install existing roles in saltbox, some things get handled behind the scenes for you.  Notably, this includes creating the subdomain[s] at cloudflare and creating the `/opt/APPNAME` directory tree.

When you add a container manually as outlined on this page, neither of those things will be done for you, so prior to running the docker commands described below you will have to create the `APPNAME.domain.tld` subdomain at cloudflare [or wherever your DNS is] and create the required `/opt/APPNAME` directory tree.

The examples below are `docker run` commands that you would execute in an SSH session on your server.

If you want to create a role file that you can install like the built-in applications, see [here](../sandbox/basics.md#contributing-to-sandbox-apps).

# Format

<pre>
docker run -d  \
  --name=<strong>APPNAME</strong>  \
  --restart=unless-stopped  \
  -e PGID=<strong>1000</strong> -e PUID=<strong>1000</strong>  \
  -v /opt/<strong>APPNAME</strong>:<strong>/CONFIG</strong>  \
  -v /etc/localtime:/etc/localtime:ro  \
  --network=saltbox \
  --network-alias=<strong>APPNAME</strong>  \
  --label com.github.saltbox.saltbox_managed=true \
  --label traefik.enable=true \
  --label traefik.http.routers.<strong>APPNAME</strong>-http.entrypoints=web \
  --label traefik.http.routers.<strong>APPNAME</strong>-http.middlewares=globalHeaders@file,redirect-to-https,gzip \
  --label traefik.http.routers.<strong>APPNAME</strong>-http.rule=Host\(\`<strong>APPNAME</strong>.yourdomain.com\`\) \
  --label traefik.http.routers.<strong>APPNAME</strong>-http.service=<strong>APPNAME</strong> \
  --label traefik.http.routers.<strong>APPNAME</strong>.entrypoints=websecure \
  --label traefik.http.routers.<strong>APPNAME</strong>.middlewares=globalHeaders@file,secureHeaders@file \
  --label traefik.http.routers.<strong>APPNAME</strong>.rule=Host\(\`<strong>APPNAME</strong>.yourdomain.com\`\) \
  --label traefik.http.routers.<strong>APPNAME</strong>.service=<strong>APPNAME</strong> \
  --label traefik.http.routers.<strong>APPNAME</strong>.tls.certresolver=cfdns \
  --label traefik.http.routers.<strong>APPNAME</strong>.tls.options=securetls@file \
  --label traefik.http.services.<strong>APPNAME</strong>.loadbalancer.server.port=<strong>APPLICATION_PORT</strong> \
  <strong>docker/image</strong>
</pre>

# Format (detailed)

Note: containers will not always use `/config`, nor will they necessarily use everything shown here.  The required volume maps and environment variables will vary by the docker image being used.

<pre>
docker run -d \
    --name <strong>APPNAME</strong> \
    --restart=unless-stopped \
    -e PGID=<strong>1000</strong> -e PUID=<strong>1000</strong> \
    --network=saltbox \
    --network-alias=<strong>APPNAME</strong> \
    -p <strong>host_port1</strong>:<strong>container_misc_port1</strong> \
    -p <strong>host_port2</strong>:<strong>container_misc_port2</strong> \
    -v /opt/<strong>APPNAME</strong>/:/config \
    -v /mnt/:/mnt/ \
    --label com.github.saltbox.saltbox_managed=true \
    --label traefik.enable=true \
    --label traefik.http.routers.<strong>APPNAME</strong>-http.entrypoints=web \
    --label traefik.http.routers.<strong>APPNAME</strong>-http.middlewares=globalHeaders@file,redirect-to-https,gzip \
    --label traefik.http.routers.<strong>APPNAME</strong>-http.rule=Host\(\`<strong>APPNAME</strong>.yourdomain.com\`\) \
    --label traefik.http.routers.<strong>APPNAME</strong>-http.service=<strong>APPNAME</strong> \
    --label traefik.http.routers.<strong>APPNAME</strong>.entrypoints=websecure \
    --label traefik.http.routers.<strong>APPNAME</strong>.middlewares=globalHeaders@file,secureHeaders@file \
    --label traefik.http.routers.<strong>APPNAME</strong>.rule=Host\(\`<strong>APPNAME</strong>.yourdomain.com\`\) \
    --label traefik.http.routers.<strong>APPNAME</strong>.service=<strong>APPNAME</strong> \
    --label traefik.http.routers.<strong>APPNAME</strong>.tls.certresolver=cfdns \
    --label traefik.http.routers.<strong>APPNAME</strong>.tls.options=securetls@file \
    --label traefik.http.services.<strong>APPNAME</strong>.loadbalancer.server.port=<strong>APPLICATION_PORT</strong> \
    <strong>docker-hub-user/repo-name</strong>
</pre>

# Examples

Tautulli listens on port 8181
<pre>
docker run -d \
    --name <strong>tautulli</strong> \
    --restart=unless-stopped \
    -e PGID=<strong>1000</strong> -e PUID=<strong>1000</strong> \
    --network=saltbox \
    --network-alias=<strong>tautulli</strong> \
    -v /opt/<strong>tautulli</strong>/:/config \
    -v /opt/<strong>tautulli/transcode</strong>:/transcode \
    -v /mnt/:/mnt/ \
    -v /etc/localtime:/etc/localtime:ro \
    -v /opt/plex/Library/Application Support/Plex Media Server/Logs:/logs \
    -v /opt:/opt \
    --label com.github.saltbox.saltbox_managed=true \
    --label traefik.enable=true \
    --label traefik.http.routers.<strong>tautulli</strong>-http.entrypoints=web \
    --label traefik.http.routers.<strong>tautulli</strong>-http.middlewares=globalHeaders@file,redirect-to-https,gzip \
    --label traefik.http.routers.<strong>tautulli</strong>-http.rule=Host\(\`<strong>tautulli.yourdomain.com</strong>\`\) \
    --label traefik.http.routers.<strong>tautulli</strong>-http.service=<strong>tautulli</strong> \
    --label traefik.http.routers.<strong>tautulli</strong>.entrypoints=websecure \
    --label traefik.http.routers.<strong>tautulli</strong>.middlewares=globalHeaders@file,secureHeaders@file \
    --label traefik.http.routers.<strong>tautulli</strong>.rule=Host\(\`<strong>tautulli.yourdomain.com</strong>\`\) \
    --label traefik.http.routers.<strong>tautulli</strong>.service=<strong>tautulli</strong> \
    --label traefik.http.routers.<strong>tautulli</strong>.tls.certresolver=cfdns \
    --label traefik.http.routers.<strong>tautulli</strong>.tls.options=securetls@file \
    --label traefik.http.services.<strong>tautulli</strong>.loadbalancer.server.port=<strong>8181</strong> \
    <strong>linuxserver/tautulli</strong>
</pre>

Speedtest listens on port 80, doesn't have a config dir
<pre>
docker run -d  \
  --name=<strong>speedtest</strong>  \
  --restart=unless-stopped  \
  -e PGID=<strong>1000</strong> -e PUID=<strong>1000</strong>  \
  -v /opt/speedtest:/var/www/html \
  --network=saltbox \
  --network-alias=<strong>speedtest</strong>  \
  --label com.github.saltbox.saltbox_managed=true \
  --label traefik.enable=true \
  --label traefik.http.routers.<strong>speedtest</strong>-http.entrypoints=web \
  --label traefik.http.routers.<strong>speedtest</strong>-http.middlewares=globalHeaders@file,redirect-to-https,gzip \
  --label traefik.http.routers.<strong>speedtest</strong>-http.rule=Host\(\`<strong>speedtest.yourdomain.com</strong>\`\) \
  --label traefik.http.routers.<strong>speedtest</strong>-http.service=<strong>speedtest</strong> \
  --label traefik.http.routers.<strong>speedtest</strong>.entrypoints=websecure \
  --label traefik.http.routers.<strong>speedtest</strong>.middlewares=globalHeaders@file,secureHeaders@file \
  --label traefik.http.routers.<strong>speedtest</strong>.rule=Host\(\`<strong>speedtest.yourdomain.com</strong>\`\) \
  --label traefik.http.routers.<strong>speedtest</strong>.service=<strong>speedtest</strong> \
  --label traefik.http.routers.<strong>speedtest</strong>.tls.certresolver=cfdns \
  --label traefik.http.routers.<strong>speedtest</strong>.tls.options=securetls@file \
  --label traefik.http.services.<strong>speedtest</strong>.loadbalancer.server.port=<strong>80</strong> \
  <strong>satzisa/html5-speedtest</strong>
</pre>

Plex-Patrol doesn't need to be behind the proxy, but you want it on the saltbox network and you want saltbox to take it down for backups.
<pre>
docker run -d  \
  --name=<strong>plex_patrol</strong>  \
  --restart=unless-stopped  \
  -e PGID=<strong>1000</strong> -e PUID=<strong>1000</strong>  \
  -v /opt/<strong>plex_patrol</strong>:<strong>/config</strong>  \
  --network=saltbox \
  --network-alias=<strong>plex_patrol</strong>  \
  --label com.github.saltbox.saltbox_managed=true \
  --label traefik.enable=false \
  <strong>cloudb0x/plex_patrol:latest</strong>
</pre>

Autoscan exposing an alternate port for perhaps a second instance, but only visible on the host [not outside]
<pre>
docker run -d  \
  --name=<strong>autoscan</strong>  \
  --restart=unless-stopped  \
  -e PGID=<strong>1000</strong> -e PUID=<strong>1000</strong>  \
  -p <strong>127.0.0.1:3033</strong>:<strong>3030</strong> \
  -v /etc/localtime:/etc/localtime:ro \
  -v /opt/autoscan:/config \
  -v /mnt:/mnt \
  --network=saltbox \
  --network-alias=<strong>autoscan</strong>  \
  --label com.github.saltbox.saltbox_managed=true \
  --label traefik.enable=false \
  <strong>cloudb0x/autoscan:master</strong>
</pre>

# Details

## Notes

- Replace all `<tags>` with your info.

- All `<container_*>` items are specified by the Docker container.

- Ideally, you want all `<name>` items to have the same name.

- Pick docker images that allow you to specify the PUID/PGID.

- You can break a command into multiple lines with a backslash (`\`) at the end of all the lines except the last one.

## Basics

- `--name=<name>`

- `--restart=unless-stopped`

  - To have it startup automatically, unless the container was previously stopped.

- `-v /etc/localtime:/etc/localtime:ro`

  - To set the docker container's timezone to your host timezone.

- `-e PUID=<your_user_ID> -e PGID=<your_group_ID>`

  - Replace `<user>` and `<group>` to match yours (see [here](../faq/System.md#find-your-user-id-uid-and-group-id-gid)).
- `--label com.github.saltbox.saltbox_managed=true`

  - Is used to determine whether the container is shut down or not during Saltbox backup and other tasks. If you want this container to not be shut down, leave the label out or set it to `false`.

  - If you do decide leave this out or set this to `false`, it will probably be a good idea to store the config files at another location other than `/opt` as a running container could cause issues during Saltbox Backup.

## Mount Paths

  Mount paths are in the format of `path/on/host:path/within/container`. You may change the path on host (left side), but not the path set for the container, internally (right side).

- `-v /opt/<name>:<container_config_path>`

  - This is where your config files will go

  - You will need to:

    - Create the folder: `mkdir /opt/<name>`

    - Set ownership: `sudo chown -R <user>:<group> /opt/<name>`

      - Replace `<user>` and `<group>` to match yours' (see [here](../faq/System.md#find-your-user-id-uid-and-group-id-gid))

    - Set permissions: `sudo chmod -R ugo+X /opt<name>`

- `-v /mnt/local/downloads/<name>:/downloads/<name>`

  - Only required if your Docker app needs a path for downloads.

  - You will need to set `/downloads/<name>` as the downloads path in your app.

  - This path will be accessible to Sonarr and Radarr.

  - You will need to:

    - Create the folder: `mkdir /mnt/local/downloads/<name>`

    - Set ownership: `sudo chown -R <user>:<group> /mnt/local/downloads/<name>`

      - Replace `<user>` and `<group>` to match yours' (see [here](../faq/System.md#find-your-user-id-uid-and-group-id-gid))

    - Set permissions: `sudo chmod -R ugo+X /mnt/local/downloads/<name>`

## Network

Note: These are important, but leave them out if your docker run command requires `--net=host`.

- `--network=saltbox`

- `--network-alias=<name>`   (aliases are shortcuts to communicate across dockers)

## Ports

  Ports are in the format of `host_port:container_port`.

- For the main, web admin/page port (e.g. 32400 in Plex):

  - You do not need to specify this port with `-p`. Since this port will not be accessible over the net or from the host. Instead, Traefik will redirect the subdomain to it.

  - If you do want the port accessible from the host (but not from the net), simply add `127.0.0.1:` to it and specify it via:

      `-p 127.0.0.1:<host_port>:<container_webadmin_port>`

      If you expose ports to the host like this, make sure they don't conflict with another one on that host.

- For all other ports:

  - `-p <host_port>:<container_other_ports>`

    - These are accessible from the net.

- If this is a home install, you will probably need to forward the port to the Saltbox machine.

## Traefik Proxy

``` { .sh .annotate }
  --label traefik.enable=true
  --label traefik.http.routers.<name>-http.entrypoints=web \
  --label traefik.http.routers.<name>-http.middlewares=globalHeaders@file,authelia@docker,redirect-to-https,gzip \
  --label traefik.http.routers.<name>-http.rule=Host\(\`<name>.yourdomain.com\`\) \
  --label traefik.http.routers.<name>-http.service=<name> \
  --label traefik.http.routers.<name>.entrypoints=websecure \
  --label traefik.http.routers.<name>.middlewares=globalHeaders@file,secureHeaders@file,authelia@docker \ # (1)
  --label traefik.http.routers.<name>.rule=Host\(\`<name>.yourdomain.com\`\) \
  --label traefik.http.routers.<name>.service=<name> \
  --label traefik.http.routers.<name>.tls.certresolver=cfdns \
  --label traefik.http.routers.<name>.tls.options=securetls@file \
  --label traefik.http.services.<name>.loadbalancer.server.port=<container_webpage_port> # (2)
```

1. Omit `authelia@docker` to disable SSO. If your Authelia master instance is on another server (i.e. split feederbox/mediabox setup) modify this to be `authelia` only.
2. The port for the web admin page for the container.

You'll need to add the subdomain manually at your DNS provider if you're not using wild-card DNS.

## Docker Compose

Here is the example in compose format and connecting to the `saltbox` Docker network to be served by Traefik.

As noted above, you will have to create the `APPNAME.domain.tld` subdomain at cloudflare [or wherever your DNS is] and create any required `/opt/APPNAME` directory tree manually.  Creating the container using `docker-compose` will not do those things automatically the way an `sb install APPNAME` Ansible run would.

```yaml
version: "3"
services:
  APPNAME:
    restart: unless-stopped
    container_name: APPNAME
    image: docker/image:tag
    hostname: APPNAME
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    networks:
      - saltbox
    labels:
      com.github.saltbox.saltbox_managed: true 
      traefik.enable: true
      traefik.http.routers.APPNAME-http.entrypoints: web
      traefik.http.routers.APPNAME-http.middlewares: globalHeaders@file,authelia@docker,redirect-to-https,gzip
      traefik.http.routers.APPNAME-http.rule: Host(`APPNAME.yourdomain.com`)
      traefik.http.routers.APPNAME-http.service: APPNAME
      traefik.http.routers.APPNAME.entrypoints: websecure
      traefik.http.routers.APPNAME.middlewares: globalHeaders@file,secureHeaders@file,authelia@docker
      traefik.http.routers.APPNAME.rule: Host(`APPNAME.yourdomain.com`)
      traefik.http.routers.APPNAME.service: APPNAME
      traefik.http.routers.APPNAME.tls.certresolver: cfdns
      traefik.http.routers.APPNAME.tls.options: securetls@file
      traefik.http.services.APPNAME.loadbalancer.server.port: APPLICATION_PORT
    volumes:
      - /opt/APPNAME:/CONFIG
      - /etc/localtime:/etc/localtime:ro
networks:
  saltbox:
    external: true
```
