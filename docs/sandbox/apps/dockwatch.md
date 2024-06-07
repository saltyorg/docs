# Dockwatch

## What is it?

[Dockwatch](https://github.com/Notifiarr/dockwatch) is a simple UI driven way to manage updates & notifications for Docker containers.

- Link and control multiple servers
- Automatically locate and match container icons for non Unraid usage # (1)!
- Update schedules for container image tags by a container basis
- Notifications by a container basis
- Automatically try to restart unhealthy containers
- Mass prune orphan images, volumes & networks
- Mass actions for containers [(re-)start/stop, pull, update] # (2)!
- Group containers in a table view for easier management

1. If icon is available at [Notifiarr/images](https://github.com/Notifiarr/images).
2. Also includes generating a `docker run` command, `docker-compose.yml` and comparing mounts.

!!! warning
    By default, the role is protected behind your Authelia/SSO middleware.

    By default, Dockwatch is likely unable to take action on containers do the security posture of the Docker socket proxy. You can override this behavior to allow Dockwatch to take actions by adding `POST: "1"` to the socket proxy envs via the below inventory entry:
        ```yml
        dockwatch_docker_socket_proxy_envs:
          CONTAINERS: "1"
          IMAGES: "1"
          NETWORKS: "1"
          PORTS: "1"
          POST: "1"
          VOLUMES: "1"
        ```

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Notifiarr/dockwatch){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Notifiarr/dockwatch#environment-variables){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Notifiarr/dockwatch){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-dockwatch

```

### 2. URL

- To access dockwatch, visit `https://dockwatch._yourdomain.com_`

### 3. Setup

Set up the update options first, if you want to set them all at the same time use the `updates` or `frequency` button in the top right corner.

Add your notifiarr API key in the notification tab in order to set up notifications.

- [:octicons-link-16: Documentation: Dockwatch Docs](https://github.com/Notifiarr/dockwatch#environment-variables){: .header-icons }
