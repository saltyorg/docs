# Autobrr

[Autobrr](https://autobrr.com/) is a modern autodl-irssi replacement.

!!!info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://autobrr.com){: .header-icons } | [:octicons-link-16: Docs](https://autobrr.com/introduction){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/autobrr/autobrr){: .header-icons } | [:material-docker: Docker](https://github.com/autobrr/autobrr/pkgs/container/autobrr){: .header-icons }|

---

## 1. Installation

``` shell

sb install sandbox-autobrr

```

## 2. URL

- To access pgadmin, visit `https://autobrr._yourdomain.com_`

## 3. Setup

- Autobrr will prompt you to create the initial user/password via the webui. The role is protected behind your default SSO provider (Authelia/Authentik) to avoid open access to the world. Once the user is provisioned, you can disable SSO protection by setting `autobrr_traefik_sso_middleware: ""` via the inventory system. Autobrr auto supports OIDC for authentication with either Authelia or Authentik. See [here](https://autobrr.com/configuration/authentication) for details.

- [:octicons-link-16: Documentation: pgadmin Docs](https://autobrr.com/introduction){: .header-icons }
