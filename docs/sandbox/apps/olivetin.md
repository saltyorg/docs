---
hide:
  - tags
tags:
  - olivetin
  - automation
  - admin
---

# OliveTin

## What is it?

[OliveTin](https://olivetin.app/) gives safe and simple access to predefined shell commands from a web interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://olivetin.app/){: .header-icons } | [:octicons-link-16: Docs](https://docs.olivetin.app/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/OliveTin/OliveTin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jamesread/olivetin){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-olivetin

```

### 2. URL

- To access OliveTin, visit `https://olivetin._yourdomain.com_`

### 3. Configuration

- A barebones configuration is imported by the role to `/opt/olivetin/config.yaml` provisioning a default "Hello world!" item

- Check out [the configuration section of the documentation](https://docs.olivetin.app/config.html) to start building your actions.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->