---
hide:
  - tags
tags:
  - filebrowser
  - file-management
  - admin
---

# File Browser

## What is it?

[File Browser](https://filebrowser.org/) is is a create-your-own-cloud-kind of software where you can install it on a server, direct it to a path and then access your files through a nice web interface. You have many available features!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://filebrowser.org/){: .header-icons } | [:octicons-link-16: Docs](https://filebrowser.org/features){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/filebrowser/filebrowser){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/filebrowser/filebrowser){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-filebrowser

```

### 2. URL

- To access File Browser, visit `https://filebrowser._yourdomain.com_`

!!! info
    The initial `admin` user has a randomly generated password. You may retrieve this password in the container logs via `docker logs filebrowser`. We recommend changing the credentials promptly upon deployment.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
