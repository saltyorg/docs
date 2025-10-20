---
hide:
  - tags
tags:
  - lldap
  - ldap
  - authentication
  - user-management
---

# LLDAP

## What is it?

LLDAP (Light LDAP) is a lightweight, simplified LDAP server for authentication. It provides a user-friendly interface for managing users and groups, with a simplified LDAP implementation that's easier to configure and maintain than traditional LDAP servers like OpenLDAP.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/lldap/lldap){: .header-icons } | [:octicons-link-16: Docs](https://github.com/lldap/lldap/blob/main/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/lldap/lldap){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nitnelave/lldap){: .header-icons }|

### 1. Installation

``` shell

sb install lldap

```

### 2. URL

- To access LLDAP, visit `https://lldap._yourdomain.com_`

### 3. Setup

LLDAP provides a lightweight LDAP server with a user-friendly web interface for managing users and groups. The configuration file is at `/opt/lldap/lldap_config.toml`. Optional SMTP settings for password resets can be configured in your [Saltbox inventory](../saltbox/inventory/index.md) using `lldap_role_smtp_*` variables.

Applications can connect using host `lldap`, port 3890 (LDAP) or 17170 (Web UI). To reset LLDAP, run `sb install lldap-reset`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->