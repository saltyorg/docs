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

- To access Authentik, visit `https://authentik._yourdomain.com_`

!!! info

    ``` yaml title="Default Login"

        user: saltbox_user # (1)!
        password: saltbox_password # (2)!

    ```

    1. Replace `saltbox_user` with the username you set when installing Saltbox.
    2. Replace `saltbox_password` with the password you set when installing Saltbox.

### 3. Setup

- Change login password.

- Click Preferences in the top bar and on the Downloads section enter the following paths: <br />
  - Download to: <br />
    `/mnt/unionfs/downloads/torrents/Authentik/incoming`
  - Move completed to: <br />
    `/mnt/unionfs/downloads/torrents/Authentik/completed`
  - Autoadd `.torrent files` from: <br />
    `/mnt/unionfs/downloads/torrents/Authentik/watched`

- Select Network section, uncheck `Use Random Ports` under Incoming Ports and set both input fields to `58112`.

- Click the `Plugins` section
  - enable the `labels` plugin.
  - enable and the `Extractor` plugin. <br />
      In order for Sonarr or Radarr to import media packaged within .rar files, they will have to be extracted.
  - After clicking `"Apply"`, select the `Extractor`  plugin on the left. <br />
      Make sure the directory points to the `completed` folder within your Authentik data directory.  <br />
      `/mnt/unionfs/downloads/torrents/Authentik/completed` <br />
      Also, make sure that the Create torrent name sub-folder setting is checked.

### 4. Adding to Sonarr/Radarr



- [:octicons-link-16: Authentik Docs](https://docs.goauthentik.io/docs/){: .header-icons }
