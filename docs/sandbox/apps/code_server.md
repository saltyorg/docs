---
hide:
  - tags
tags:
  - code-server
  - vscode
  - development
---

# code-server

## What is it?

[code-server](https://github.com/coder/code-server). Run [VS Code](https://github.com/Microsoft/vscode) on any machine anywhere and access it in the browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/coder/code-server){: .header-icons } | [:octicons-link-16: Docs](https://code.visualstudio.com/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/coder/code-server){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/codercom/code-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-code-server

```

### 2. URL

- To access code-server, visit `https://code-server._yourdomain.com_`

## Migration from the old `coder` role

The old `coder` role was renamed to `code-server` on Dec 19th 2022.
In order to migrate to the new role, if you aren't using a custom folder for `coder`, rename the inventory variables if you have any, then run:

``` shell

sb install sandbox-code-server -e 'code_server_migrate_coder=true'

```

The `coder` role is currently deprecated and won't receive any updates, so please run the migration to the new role as soon as possible.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->