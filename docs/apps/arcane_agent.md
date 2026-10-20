---
icon: material/docker
title: Arcane Agent
hide:
  - tags
tags:
  - arcane
  - agent
saltbox_automation:
  app_links:
    - name: Manual
      url: https://getarcane.app/docs/remote/environments
      type: documentation
      purpose: manual
    - name: Image tags
      url: https://github.com/getarcaneapp/agent/pkgs/container/agent
      type: github
      purpose: release
    - name: Community
      url: https://discord.gg/WyXYpdyV3Z
      type: community
      purpose: community
  project_description:
    name: Arcane Agent
    summary: a lightweight, headless process that runs on a remote Docker host to allow the central Arcane Manager to manage that host’s containers, images, volumes, and networks through a single unified interface.
    link: https://getarcane.app
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install arcane-agent
```

## Usage

Access [Arcane Manager](arcane.md) and register the agent as a remote environment.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
