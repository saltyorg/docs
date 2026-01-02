---
status: draft
hide:
  - tags
tags:
  - upgrade
  - role-refactor
  - inventory
---

# Role Refactor
 
The role-refactor branch merge includes the following updates:

-   Enforces explicit Inventory [override levels](../inventory/index.md#override-levels) :warning:{ title="Breaking change — migration required" style="border-radius:unset;" }

    > Variables that previously applied to all instances of a role (e.g. `sonarr_docker_image`) now only apply to the instance with the exact name (e.g. `sonarr`).
    
    > **Role-scoped overrides must now include the `_role_` infix**{ style="color: var(--md-typeset-color);" } (e.g. `sonarr_role_docker_image`) **to persist as such.**{ style="color: var(--md-typeset-color);" }

-   Deprecates `_docker_network_mode_default` Inventory convention

    > `_docker_network_mode` is now natively supported across all roles.

-   Retires [Sandbox](../../reference/modules/sandbox.md) `settings.yml` :warning:{ title="Breaking change — migration required" style="border-radius:unset;" }

    > Settings no longer apply and must be migrated to their Inventory form to persist.

-   Removes a number of roles

    <blockquote class="grid" style="grid-template-columns: repeat(auto-fit, minmax(8rem, 1fr));" markdown>
    
    jaeger

    readarr

    sub_zero

    webtools

    alternatrr

    aria2_ng

    comicstreamer

    docspell

    rdtclient

    solr

    teamspeak

    watchtower

    </blockquote>

-   Python to Golang rewrites of tools: DNS manager, Docker controller

<div class="sb-cta" markdown>

Full changes:

<div markdown>

[:octicons-file-diff-24:**Saltbox diff**](../../static/saltbox.html){ .md-button }
[:octicons-file-diff-24:**Sandbox diff**](../../static/sandbox.html){ .md-button }

</div>

</div>

----

## Inventory Migration Guide

### Single-instance overrides

When a role only has a single instance, either variable form will achieve the same outcome. However, to align with the new convention, it is recommended to transition to the `_role_` infix.

!!! example

    ```yaml
    plex_dns_proxy: false
    ```
    
    Becomes:
    
    ```yaml
    plex_role_dns_proxy: false
    ```

### Multi-instance overrides

Multi-instance role variables must be converted to the appropriate override level for existing configuration to persist.

!!! example

    !!! tip "Specificity takes precedence"
    
        When determining which variable to use, remember the precedence order: Instance > Role > Global

    ```yaml
    bazarr_instances: ["bazarr", "bazarr4k"]
    bazarr_docker_volumes_custom: ["/opt/subcleaner:/subcleaner"]
    bazarr_themepark_theme: "nord"
    bazarr4k_themepark_theme: "maroon"
    ```
    
    Becomes:
    
    ```yaml
    bazarr_instances: ["bazarr", "bazarr4k"]
    bazarr_role_docker_volumes_custom: ["/opt/subcleaner:/subcleaner"] # (1)!
    bazarr_role_themepark_theme: "nord" # or bazarr_themepark_theme: "nord" (2)
    bazarr4k_themepark_theme: "maroon"
    ```
    
    1. Typically, you want external processing tools to be available to all instances, so keep role-scoped.
    
    2. This can go both ways depending on your goal. Previously, this override was role-scoped, but with only two instances defined and the `4k` instance individually overridden, the same outcome would be achieved.
    
        - `bazarr_role_themepark_theme: "nord"`: additional instances added later would inherit the `nord` theme unless individually overridden
        - `bazarr_themepark_theme: "nord"`: additional instances would inherit the `global_themepark_theme` value if enabled, or would not have theming applied.
