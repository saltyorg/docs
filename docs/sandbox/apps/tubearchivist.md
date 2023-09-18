# Tubearchivist

## What is it?

[Tubearchivist](https://www.tubearchivist.com/) is a self hosted Youtube media server.

- Subscribe to your favorite YouTube channels
- Download Videos using yt-dlp
- Index and make videos searchable
- Play videos
- Keep track of viewed and unviewed videos

!!!info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.tubearchivist.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/tubearchivist/tubearchivist/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/tubearchivist/tubearchivist){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/bbilly1/tubearchivist){: .header-icons }|

Recommended install types: Feederbox, Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-tubearchivist

```

### 2. URL

- To access tubearchivist, visit `https://tubearchivist._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}

  Username: "your user from accounts.yml"
  Password: your_normal_password

  ```

!!!note
   Tubearchivist adds the downloaded media to `/mnt/unionfs/downloads/tubearchivist/YT_CHANNEL_NAME`

- [:octicons-link-16: Documentation: tubearchivist Docs](https://github.com/tubearchivist/tubearchivist/wiki){: .header-icons }
