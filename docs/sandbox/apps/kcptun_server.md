---
icon: material/docker
hide:
  - tags
tags:
  - kcptun-server
  - tunnel
  - networking
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url: https://github.com/xtaci/kcptun
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/horjulf/kcptun/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: kcptun Server
    summary: |
      a Stable & Secure Tunnel based on KCP with N:M multiplexing and FEC.
    link: https://github.com/xtaci/kcptun
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# kcptun Server

## Overview

[kcptun Server](https://github.com/xtaci/kcptun) is a Stable & Secure Tunnel based on KCP with N:M multiplexing and FEC.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/xtaci/kcptun){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/horjulf/kcptun/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-kcptun-server
```

## Usage
