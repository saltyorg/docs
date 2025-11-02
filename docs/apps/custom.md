---
icon: material/ansible
hide:
  - tags
tags:
  - custom
---

# Custom

## Overview

The Custom role allows you to install additional software packages (APT, DEB, and pip modules) that are not included in the default Saltbox installation. This role gives you the flexibility to add tools and dependencies specific to your needs.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/saltyorg/Saltbox){: .header-icons } | [:octicons-link-16: Docs](https://docs.saltbox.dev){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/saltyorg/Saltbox){: .header-icons } | :material-docker: Docker |

### 1. Installation

``` shell

sb install custom

```

### 2. Setup

Before running the custom role, configure the packages you want to install in your Saltbox inventory:

**APT packages:**

```yaml
custom_apt:
  - package_name_1
  - package_name_2
```

**DEB packages (direct URLs):**

```yaml
custom_deb:
  - https://example.com/package.deb
```

**pip modules (Ubuntu 22.04 and earlier only):**

```yaml
custom_pip:
  - module_name
```

!!! info
    The custom role is useful for installing system utilities, development tools, or dependencies required by other applications in your setup.

!!! warning
    pip installation via this role is only available on Ubuntu 22.04 and earlier.
