---
hide:
  - tags
tags:
  - krusader
  - file-management
  - admin
---

# Krusader

## What is it?

[Krusader](http://www.krusader.org/) is an advanced orthodox file manager for KDE and other desktops in the Unix world. It is similar to the console-based GNU Midnight Commander, GNOME Commander for the GNOME desktop environment, or Total Commander for Windows, all of which can trace their paradigmatic features to the original Norton Commander for DOS. It supports extensive archive handling, mounted filesystem support, FTP, advanced search, viewer/editor, directory synchronisation, file content comparisons, batch renaming, etc.

This is a Docker container for Krusader.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://www.krusader.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/binhex/arch-krusader){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/binhex/arch-krusader){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/binhex/arch-krusader){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-krusader

```

### 2. URL

- To access Krusader, visit `https://krusader._yourdomain.com_`
- Now you can click on vnc.html or vnc_lite.html

### 3. Setup

- The configured password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`
- /mnt is already mounted to /mnt

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
