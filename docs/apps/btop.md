---
icon: material/desktop-classic
hide:
  - tags
tags:
  - btop
  - monitoring
  - system
saltbox_automation:
  sections:
    inventory: false
  app_links:
  - name: Manual
    url:
    type: documentation
  - name: Releases
    url: https://github.com/aristocratos/btop/tags
    type: github
  - name: Community
    url: https://github.com/aristocratos/btop/discussions
    type: github
  project_description:
    name: btop
    summary: |
      a modern, real-time system monitoring tool for Linux that provides a visually appealing and interactive interface to monitor system resources such as CPU usage, memory consumption, disk activity, network bandwidth, and running processes.
    link: https://github.com/aristocratos/btop
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# btop

## Overview

[btop](https://github.com/aristocratos/btop) is a modern, real-time system monitoring tool for Linux that provides a visually appealing and interactive interface to monitor system resources such as CPU usage, memory consumption, disk activity, network bandwidth, and running processes.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/aristocratos/btop/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/aristocratos/btop/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install btop
```

## Usage

```shell
btop
```
