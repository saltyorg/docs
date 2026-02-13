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
  inventory:
    hide_sections:
      - Template Variables
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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        traefik_file_template_file: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `traefik_file_template_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `traefik_file_template_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Settings"

    ??? variable string "`traefik_file_template_file`"

        ```yaml
        # Type: string
        traefik_file_template_file: "/tmp/traefik-app.yml"
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
