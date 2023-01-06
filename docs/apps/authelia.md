# What is it?

[Authelia](https://www.authelia.com/) (Authelia) is an open-source authentication and authorization server and portal fulfilling the identity and access management (IAM) role of information security in providing multi-factor authentication and single sign-on (SSO) for your applications via a web portal.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://authelia.com){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://www.authelia.com/configuration/prologue/introduction/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/authelia/authelia){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/authelia/authelia){: .header-icons target=_blank rel="noopener noreferrer" }|

## 2. URL

To access Tautulli, visit `https://login._yourdomain_.com` or the subdomain set for Authelia in [settings.yml](../reference/accounts.md#step-2-configuration). This merely presents a simple login page where a user can configure Two Factor Authentication if Authelia is configured to accept/require 2FA.

## 3. Settings

Saltbox offers several options to customize the `configuration.yml` via the inventory system. We recommend reviewing the [configuration template](https://github.com/saltyorg/Saltbox/blob/master/roles/authelia/templates/configuration.yml.j2) and the [default variables](https://github.com/saltyorg/Saltbox/blob/master/roles/authelia/defaults/main.yml). It is highly recommended to review the upstream documentation for configuration options.

Some of the features that can be enabled are Two Factor Authentication, Duo notifications and SMTP notifications.

## 4. LDAP Authentication

Saltbox offers an optional LDAP authentication backend for Authelia. This can be enabled by setting `authelia_authentication_backend: "ldap"` in your inventory file. The LDAP is provisioned via OpenLDAP and includes phpLDAPadmin.
