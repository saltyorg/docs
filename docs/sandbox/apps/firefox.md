# Firefox

[Mozilla Firefox](https://www.mozilla.org/firefox/) is a free and open-source web browser developed by Mozilla Foundation and its subsidiary, Mozilla Corporation.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Docs](https://github.com/jlesage/docker-firefox#readme){ .md-button .md-button--stretch }

[:material-git: GitHub Repo](https://github.com/jlesage/docker-firefox){ .md-button .md-button--stretch }

[:material-docker: Docker Hub](https://hub.docker.com/r/jlesage/firefox){ .md-button .md-button--stretch }

</div>

---

## Configuration

If needed, set environment variables[<sup>:octicons-link-external-16:</sup>][envs] by editing `/opt/firefox/.env` as appropriate, before deployment.

???+ question "Security"

    By default, web access is restricted by Authelia, and VNC access is secured through SSH authentication; hence, no VNC password is configured. If you wish to add this extra layer of security, the process is straightforward:

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

  [envs]: https://github.com/jlesage/docker-firefox#environment-variables "Head to the environment variables breakdown section of the project documentation"
