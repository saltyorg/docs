# code-server

## What is it?

[code-server](https://github.com/coder/code-server){: target=_blank rel="noopener noreferrer" }. Run [VS Code](https://github.com/Microsoft/vscode){: target=_blank rel="noopener noreferrer" } on any machine anywhere and access it in the browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/coder/code-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://code.visualstudio.com/docs){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/coder/code-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://registry.hub.docker.com/r/codercom/code-server){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-code_server

```

### 2. URL

- To access code-server, visit `https://code-server._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: VS Code Documentation](https://code.visualstudio.com/docs){: .header-icons target=_blank rel="noopener noreferrer" }

## Migration from the old `coder` role

The old `coder` role was renamed to `code-server` on Dec 19th 2022.
In order to migrate to the new role, if you aren't using a custom folder for `coder`, rename the inventory variables if you have any, then run:

``` shell

sb install sandbox-code_server -e 'code_server_migrate_coder=true'

```

The `coder` role is currently deprecated and won't receive any updates, so please run the migration to the new role as soon as possible.
