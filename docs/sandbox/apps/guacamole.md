---
hide:
  - tags
tags:
  - guacamole
  - networking
  - remote-access
---

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

### 4. Enable Extensions (Optional)

Guacamole supports various authentication extensions that can be enabled through your [Inventory](https://docs.saltbox.dev/saltbox/inventory/). Add any of the following options to enable specific extensions:

=== "TOTP (Two-Factor Authentication)"

    Enable time-based one-time passwords for enhanced security:

    ```yml
    guacamole_docker_envs_custom:
      OPT_TOTP: "Y"
    ```

=== "LDAP"

    Enable LDAP authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_LDAP: "Y"
    ```

=== "RADIUS"

    Enable RADIUS authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_RADIUS: "Y"
    ```

=== "Duo Security"

    Enable Duo two-factor authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_DUO: "Y"
    ```

=== "CAS"

    Enable Central Authentication Service:

    ```yml
    guacamole_docker_envs_custom:
      OPT_CAS: "Y"
    ```

=== "OpenID Connect"

    Enable OpenID Connect authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_OPENID: "Y"
    ```

=== "SAML"

    Enable SAML authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_SAML: "Y"
    ```

=== "Header Authentication"

    Enable HTTP header-based authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_HEADER: "Y"
    ```

After adding any extension options, run `sb install sandbox-guacamole` to apply changes.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
