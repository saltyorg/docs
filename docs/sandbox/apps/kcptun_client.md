---
icon: material/docker
hide:
  - tags
tags:
  - kcptun-client
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
    name: kcptun client
    summary: |
      a Stable & Secure Tunnel based on KCP with N:M multiplexing and FEC.
    link: https://github.com/xtaci/kcptun
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-kcptun-client
```

## Usage
