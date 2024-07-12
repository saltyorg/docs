---
hide:
  - tags
tags:
  - authentik
---

# Authentik

## What is it?

[Authentik](https://goauthentik.io/) is an IdP (Identity Provider) and SSO (single sign on) that is built with security at the forefront of every piece of code, every feature, with an emphasis on flexibility and versatility. It supports all of the major providers, such as OAuth2, SAML, LDAP, and SCIM, so you can pick the protocol that you need for each application.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://goauthentik.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.goauthentik.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/goauthentik/authentik){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/beryju/authentik){: .header-icons }|

### 1. Installation

``` shell

sb install authentik

```

### 2. URL

- To access Authentik, visit `https://auth._yourdomain.com_`

!!! info

    ``` yaml title="Default Login"

        user: saltbox_user # (1)!
        password: saltbox_password # (2)!

    ```

    1. Replace `saltbox_user` with the username you set when installing Saltbox.
    2. Replace `saltbox_password` with the password you set when installing Saltbox.

### 3. Setup

To set up Authentik similarly to how we have [Authelia](../apps/authelia.md) set up, follow these steps:

After logging in, you will be greeted with the dashboard. Click on the `Admin Interface` button in the top right corner.

Click on the `Flows and Stages` drop down and select `Stages`.

Locate the `default-authentication-login` stage and click the `Edit` button. (Far right)

- Below you will see the default User Login Stage info.

    ![Defaults](../images/authentik-user-auth-default-screenshot.png)

You can change these values to anything you want, but for this example, we will change the `Session Duration` to `minutes=30` and the `Stay Signed in Offset` to `weeks=2`.

- Below you will see the updated User Login Stage info.

    ![Altered](../images/authentik-user-auth-updated-screenshot.png)

### 4. Additional Settings

To enable email notifications, set these [inventory](../saltbox/inventory/index.md) entries to your desired values:

``` yaml title="Authentik Email Settings"

authentik_email_host: "localhost" # (1)!
authentik_email_port: "25" # (2)!
authentik_email_username: "" # (3)!
authentik_email_password: "" # (4)!
authentik_email_tls: "false"
authentik_email_ssl: "false"
authentik_email_timeout: "10" # (5)!
authentik_email_from: "authentik@localhost" # (6)!

```

1. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
2. Replace `25` with your email port. IE: `587`
3. Replace `""` with your email username if necessary.
4. Replace `""` with your email password if necessary.
5. Replace `10` with your email timeout in seconds.
6. Replace `authentik@localhost` with your email from email address. IE: `Authentik <noreply@your_domain.com>`

Redeploy the Authentik role to apply these changes.

- [:octicons-link-16: Authentik Docs](https://docs.goauthentik.io/docs/){: .header-icons }
