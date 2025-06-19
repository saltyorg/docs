# Guacamole

## What is it?

[Guacamole](https://guacamole.apache.org/) is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH.

We call it clientless because no plugins or client software are required.

Thanks to HTML5, once Guacamole is installed on a server, all you need to access your desktops is a web browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://guacamole.apache.org/){: .header-icons } | [:octicons-link-16: Docs](https://guacamole.apache.org/doc/gug/){: .header-icons } | [:octicons-mark-github-16: Github](https://www.github.com/jason-bean/docker-guacamole){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jasonbean/guacamole){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-guacamole

```

### 2. URL

- To access Guacamole, visit `https://guacamole._yourdomain.com_`

### 3. Setup

- Log in with user and password `guacadmin`. Change the default user and password immediately.

- [:octicons-link-16: Documentation: Guacamole Docs](https://guacamole.apache.org/doc/gug/){: .header-icons }

### 4. Enable 2FA (Optional, but recommended)

- Update your [Inventory](https://docs.saltbox.dev/saltbox/inventory/) and add the following (change `guacamole` to the name of your instance):

```yml 
guacamole_docker_envs_custom:
  OPT_TOTP: "Y"
```

Run `sb install sandbox-guacamole` again to apply changes.
