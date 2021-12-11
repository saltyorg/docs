# Petio

## What is it?

[Petio](https://petio.tv/){: target=_blank rel="noopener noreferrer" } is a third party companion app available to Plex server owners to allow their users to request, review and discover content. The app is built to appear instantly familiar and intuitive to even the most tech-agnostic users. Petio will help you manage requests from your users, connect to other third party apps such as Sonarr and Radarr, notify users when content is available and track request progress. Petio also allows users to discover media both on and off your server, quickly and easily find related content and review to leave their opinion for other users.

Petio is an ongoing, forever free, always evolving project currently in alpha prototype stage and now available!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://petio.tv/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://docs.petio.tv/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/petio-team/petio){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/hotio/petio){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-petio

```

### 2. URL

- To access Petio, visit `https://petio._yourdomain.com_`

### 3. Setup

- Click Login With Plex and follow the steps to log in.

- After you log in with Plex you will need to specify your Petio specific admin credentials, by default it uses your Plex username and email but you still need to specify your own password.

- After setting up your credentials, you need to pick your Plex server.

- Leave MongoDB settings as default.

- Once the last step is finished, you will be presented with a login screen. Use your Plex username and the password you set up on Step 2. You can now get started with configuring Radarr, Sonarr and start requesting!

- See the Petio documentation for more information.

- [:octicons-link-16: Documentation](https://docs.petio.tv/){: .header-icons target=_blank rel="noopener noreferrer" }
