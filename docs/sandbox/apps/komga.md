# Komga

## What is it?

[Komga](https://komga.org/) is a free and open source comics/mangas server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://komga.org/){: .header-icons } | [:octicons-link-16: Docs](https://komga.org/installation/docker.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/gotson/komga){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gotson/komga){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-komga

```

### 2. URL

- To access Komga, visit `https://komga._yourdomain.com_`

### 3. Setup

- On first opening you will be asked to create a user account. <br />
  Choose an email and password, then click on Create User Account.

- Komga expects comics to be stored in `/mnt/unionfs/Media/Comics`.

- `/mnt` is accessible to the container as well.

- [:octicons-link-16: Documentation: Komga Docs](https://komga.org/installation/docker.html){: .header-icons }
