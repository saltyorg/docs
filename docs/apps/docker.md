---
icon: material/server-network-outline
title: Docker CE
saltbox_automation:
  inventory:
    show_sections:
      - Settings
      - Ports
  app_links:
    - name: Manual
      url: https://docs.docker.com
      type: documentation
      purpose: manual
    - name: Releases
      url: https://docs.docker.com/engine/release-notes
      type: releases
      purpose: release
    - name: Community
      url: https://forums.docker.com
      type: community
      purpose: community
  project_description:
    name: Docker CE
    summary: |-
      an open-source containerization technology for building and containerizing your applications.
    link: https://www.docker.com/community
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Docker CE

## Overview

[Docker CE](https://www.docker.com/community) is an open-source containerization technology for building and containerizing your applications.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.docker.com){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](https://docs.docker.com/engine/release-notes){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://forums.docker.com){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Saltbox dependency.

```shell
sb install docker
```

## Usage

```shell
docker
```

## FAQ

??? question "Why does Saltbox use the Docker network "saltbox" instead of bridge?"

    1. This keeps all Saltbox containers organized under one network
    2. the docker bridge network does not allow network aliases.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        docker_dns: ["item1", "item2"]
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `docker_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `docker_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Settings"

    ??? variable list "`docker_dns`"

        ```yaml
        # Format is ["8.8.8.8", "8.8.4.4"]
        # Type: list
        docker_dns: []
        ```

    ??? variable dict "`docker_config_custom`"

        ```yaml
        # YAML Dictionary that gets combined with the defaults and later converted to json
        # Example of how to remove an option:
        # docker_config_custom:
        # log-opts: "{{ omit }}"
        # Example of how to add options:
        # docker_config_custom:
        # debug: "true"
        # Type: dict
        docker_config_custom: {}
        ```

    ??? variable string "`docker_cpus_default`"

        ```yaml
        # CPU and Memory defaults
        # Type: string
        docker_cpus_default: ""
        ```

    ??? variable string "`docker_memory_default`"

        ```yaml
        # Type: string
        docker_memory_default: ""
        ```

    ??? variable bool "`docker_skip_start_during_meta_tag`"

        ```yaml
        # Skip Container startup during core, saltbox, mediabox or feederbox
        # If the kernel has been updated and a reboot will happen
        # Type: bool (true/false)
        docker_skip_start_during_meta_tag: "{{ saltbox_auto_reboot }}"
        ```

    ??? variable bool "`docker_create_image_prune`"

        ```yaml
        # Toggles pruning of dangling images after container creation.
        # Type: bool (true/false)
        docker_create_image_prune: true
        ```

    ??? variable bool "`docker_create_image_prune_delay`"

        ```yaml
        # Type: bool (true/false)
        docker_create_image_prune_delay: true
        ```

    ??? variable int "`docker_create_image_prune_delay_timeout`"

        ```yaml
        # Type: int
        docker_create_image_prune_delay_timeout: 10
        ```

=== "Ports"

    The role allocates the first available port within the inclusive low and high bounds and retains it while it remains within those bounds and free of conflicts.
    Override an instance's bounds to change the allowed range; set both bounds to the same value to require one exact port, including for an existing assignment.

    Existing assignments are stored in `/opt/saltbox/port-assignments.json`. On each role run, a saved port outside the current bounds or in conflict is reassigned within the current bounds, with a warning showing the old port, new port, and reason.
    These bounds also apply to ports manually changed in that file. If no port is available within the bounds, allocation fails without changing the registry.

    ??? variable int "`docker_dns_port_low_bound`"

        ```yaml
        # Type: int
        docker_dns_port_low_bound: 8190
        ```

    ??? variable int "`docker_dns_port_high_bound`"

        ```yaml
        # Type: int
        docker_dns_port_high_bound: 8280
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
