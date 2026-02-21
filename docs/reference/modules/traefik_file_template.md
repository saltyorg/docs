---
icon: material/play
title: Traefik File Template
status: draft
hide:
  - tags
tags:
  - custom
  - file
  - generate
  - template
  - traefik
saltbox_automation:
  sections:
    inventory: false
  project_description:
    name: Traefik File Template
    summary: |-
      a Saltbox module that generates a Traefik file template.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Traefik File Template

## Overview

Traefik File Template is a Saltbox module that generates a Traefik file template.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install generate-traefik-file-template
```

## Usage

1.  Run the tag and answer the prompts. The file will be saved as `/tmp/traefik-app.yml` by default.

1.  Edit the file as appropriate for your application.

1.  Deploy the file by moving it into `/opt/traefik`—Traefik will pick it up automatically.

1.  Assuming you have configured everything correctly, your application is now published at <https://iCUSTOM_APP_FQDNi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
