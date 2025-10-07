---
hide:
  - tags
tags:
  - diag
  - diagnostics
  - troubleshooting
---

# Diag

## What is it?

A diagnostic role that displays important Saltbox configuration information and system state. This role gathers and displays critical information about your Saltbox installation, including repository status, Cloudflare configuration, DNS settings, and filesystem mounts.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/saltyorg/saltbox){: .header-icons } | [:octicons-link-16: Docs](https://docs.saltbox.dev){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/saltyorg/saltbox){: .header-icons } | [:material-docker: Docker](https://github.com/saltyorg/saltbox){: .header-icons }|

### 1. Installation

``` shell

sb install diag

```

### 2. Setup

This is a diagnostic role that doesn't install any services. When run, it displays:

#### Repository Information
- Current Saltbox branch
- Current commit hash
- Upstream commit hash

#### Cloudflare Configuration
- Cloudflare enabled status
- Cloudflare SSL mode (if enabled)
- IPv4 DNS automation status
- IPv6 DNS automation status
- Cloudflare virtual environment deployment status

#### General Settings
- Plex account configuration status
- Rclone remote configuration status
- Cloudplow usage setting
- Remote storage usage setting
- Authelia master instance status
- ZeroSSL configuration
- Traefik challenge provider and certificate resolver settings
- Docker volume legacy mode status
- DNS skip setting

#### System Information
- Filesystem mounts and types
- Currently skipped Ansible tags

#### Usage

Simply run the role to view diagnostic information:

```shell
sb install diag
```

The output will help with troubleshooting configuration issues and understanding your current Saltbox setup.
