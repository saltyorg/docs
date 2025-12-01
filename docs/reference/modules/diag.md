---
icon: material/play
hide:
  - tags
tags:
  - diag
  - diagnostics
  - troubleshooting
---

# Diag

## Overview

A diagnostic role that displays important Saltbox configuration information and system state. This role gathers and displays critical information about your Saltbox installation, including repository status, Cloudflare configuration, DNS settings, and filesystem mounts.

---

This is a diagnostic role that doesn't install any services. When run, it displays:

### Repository Information
- Current Saltbox branch
- Current commit hash
- Upstream commit hash

### Cloudflare Configuration
- Cloudflare enabled status
- Cloudflare SSL mode (if enabled)
- IPv4 DNS automation status
- IPv6 DNS automation status
- Cloudflare virtual environment deployment status

### General Settings
- Plex account configuration status
- Rclone remote configuration status
- Cloudplow usage setting
- Remote storage usage setting
- Authelia master instance status
- ZeroSSL configuration
- Traefik challenge provider and certificate resolver settings
- Docker volume legacy mode status
- DNS skip setting

### System Information
- Filesystem mounts and types
- Currently skipped Ansible tags

The output will help with troubleshooting configuration issues and understanding your current Saltbox setup.

---

## Deployment

```shell
sb install diag
```
