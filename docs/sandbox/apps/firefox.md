---
hide:
  - tags
tags:
  - firefox
  - browser
---

Implements a Docker container for Firefox. The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://jlesage.github.io/docker-apps){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/jlesage/docker-firefox/blob/master/README.md#usage){ .md-button .md-button--stretch }

[:fontawesome-brands-docker: Releases&nbsp;&nbsp;](https://hub.docker.com/r/jlesage/firefox/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github: Community&nbsp;&nbsp;](https://github.com/jlesage/docker-firefox/discussions){ .md-button .md-button--stretch }

</div>

---

## Configuration

Settings are available as environment variables[<sup>:octicons-link-external-16:</sup>][envs] in `/opt/firefox/.env`.

???+ question "Security"

    By default, web access is restricted by Authelia, and VNC access is secured through SSH authentication; hence, no VNC password is configured. To add this extra layer of security, the process is straightforward:

    1. Run the following command:
       ```shell
       $EDITOR /opt/firefox/.vncpass_clear
       ```
    
    2. Enter your desired password (up to 8 characters in length) and save the file.
    
    3. At a minimum, a container restart is required for changes to take effect.

## Deployment

``` shell
sb install sandbox-firefox
```

!!! info inline end "Downloads Save Location"
    ```
    /mnt/unionfs/downloads/firefox
    ```

## Usage

### <span class="icon-indent-right"></span> Web

Visit `https://firefox._yourdomain.com_`.

### <span class="icon-indent-right"></span> VNC

The role supports VNC access over an SSH tunnel (local port forwarding) to Saltbox.

!!! example "Example Command on Local Machine <span style="float:right;color:#00bfa5">:material-fire: Some VNC apps have this functionality built-in!</span>"
    ```shell
    ssh -L localhost:5900:firefox:5900 seed@203.0.113.1 -p 8843 # (1)!
    ```

    1. `-L localhost:5900:firefox:5900`: This part specifies local port forwarding. It tells SSH to listen on port 5900 on your local machine and forward any traffic to the firefox Docker container on port 5900 on the Saltbox host. In other words, it sets up a tunnel between your local port 5900 and the container's port 5900.

        Complete the command with your usual SSH info: `USERNAME@SALTBOX_EXTERNAL_IP -p SSH_PORT`.

While the tunnel is active, you can use a VNC client to access the GUI via the address `localhost:5900`.

  [envs]: https://github.com/jlesage/docker-firefox#environment-variables "Access project Docker environment variables breakdown"
