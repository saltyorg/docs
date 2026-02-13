---
hide:
  - tags
tags:
  - upgrade
  - role-refactor
  - inventory
---

# Role Refactor

The role-refactor branch merge includes the following updates:

-   Refactors application role variables as follows ([breaking](#inventory-migration-guide "Manual migration required"){ .alert-link }):

    -   [Override scope](../inventory/index.md#override-scope) is now clearly differentiated using explicit variable naming conventions

    -   Some `_default` + `_custom` variable pairs assigned an empty value by default were replaced with a single unsuffixed variable

-   **Sandbox**: `settings.yml` removed ([breaking](#sandbox-app-settings-migration-guide "Manual migration required"){ .alert-link })

-   Removes roles:

    <div class="grid" style="grid-template-columns:repeat(auto-fit, minmax(8rem, 1fr))" markdown>

    jaeger

    readarr

    settings

    sub_zero

    webtools

    alternatrr

    aria2_ng

    booksonic

    comicstreamer

    docspell

    goplaxt

    maybe_finance

    rdtclient

    solr

    teamspeak

    watchtower

    </div>

-   Replaces Python tools with Go rewrites: DNS manager, Docker controller

-   **Tandoor Recipes**: updated to use a dedicated database container ([breaking](../../sandbox/apps/tandoor.md#overview "Manual migration required"){ .alert-link }):

-   **ruTorrent**: role preserved but moved to Sandbox

<div class="sb-cta" markdown>

Full changes:

<div markdown>

[:octicons-file-diff-24:**Saltbox diff**](../../static/saltbox.html){ .md-button }

[:octicons-file-diff-24:**Sandbox diff**](../../static/sandbox.html){ .md-button }

</div>

</div>

----

## Inventory Migration Guide

???+ abstract "Summary for people who don't like reading a lot of text"

    -   Variables that previously applied to all instances of a role (e.g. `sonarr_docker_image`) now only apply to the instance with the exact name (e.g. `sonarr`).

    -   To apply to all instances of a role, variables must now include the `_role_` infix (e.g. `sonarr_role_docker_image`).

    -   If a role you've customized with a `_default` or `_custom` variable isn't working as expected following the upgrade, the solution is typically to remove that suffix from the variable name.

The following sections must be followed sequentially.

### Single-instance overrides

When a role only has a single instance, either variable name pattern will achieve the same outcome. However, to align with the new convention, it is recommended to switch to the `_role_` infix, which is now the default pattern.

???+example

    !!! warning ""

        ```yaml
        plex_dns_proxy: false
        ```

    :material-arrow-down-bold: changes to :material-arrow-down-bold:

    !!! success ""

        ```yaml
        plex_role_dns_proxy: false
        ```

### Multi-instance overrides

Multi-instance role variables must be changed to the appropriate override scope for existing configuration to persist.

???+example

    Note: When choosing which variable to use, remember the precedence order: Instance > Role > Global (specificity takes precedence)

    !!! bug ""

        ```yaml
        bazarr_instances: ["bazarr", "bazarr4k"]
        bazarr_docker_volumes_custom: ["/opt/subcleaner:/subcleaner"] # (1)!
        bazarr_themepark_theme: "nord" # (2)!
        bazarr4k_themepark_theme: "maroon"
        ```

        1.  Reminder: variables in this pattern were considered role-scoped prior to Role Refactor, since the prefix matches the role name.

        2.  Reminder: variables in this pattern were considered role-scoped prior to Role Refactor, since the prefix matches the role name.

    :material-arrow-down-bold: changes to :material-arrow-down-bold:

    !!! success ""

        ```yaml
        bazarr_instances: ["bazarr", "bazarr4k"]
        bazarr_role_docker_volumes_custom: ["/opt/subcleaner:/subcleaner"] # (1)!
        bazarr_role_themepark_theme: "nord" # or bazarr_themepark_theme: "nord" (2)
        bazarr4k_themepark_theme: "maroon" # (3)!
        ```

        1.  Typically, you want external processing tools to be available to all instances, so keep role-scoped.

        2.  This can go both ways depending on your goal. Previously, this override was role-scoped, but with only two instances defined and the `4k` instance individually overridden, the same outcome would be achieved.

            - `bazarr_role_themepark_theme: "nord"`: additional instances added later would inherit the `nord` theme unless individually overridden
            - `bazarr_themepark_theme: "nord"`: additional instances would inherit the `global_themepark_theme` value if enabled, or would not have theming applied.

        3.  No change needed here, as variables in this pattern were already considered instance-scoped and remain so.

### `default` / `custom` overrides { data-toc-label="“Default” / “Custom” overrides" }

!!! info "This section assumes you have already completed the override scope migration steps above"

Variables affected by this change are typically moved to the *Docker+* Role Defaults category.

1.  Check whether your override is affected by looking up the variable name in the app's documentation.

1.  If you find the corresponding variable unsuffixed, match it by removing `_default`/`_custom` from the variable name in your inventory.

1.  If you find the corresponding variable pair still exists and your override has `_default`, change it to `_custom`.

???+example

    !!! bug ""

        ```yaml
        plex_docker_network_mode_default: "container:gluetun" # (1)!

        firefox_role_docker_commands_custom:
          - "/usr/lib/firefox/firefox"
          - "--headless"

        wireguard_role_docker_ports_default:
          - "1234:1234"
        ```

        1.  Not to be confused with the similarly named list variable `plex_docker_networks_default`, which is still available as such (assuming an instance named `plex`).

    :material-arrow-down-bold: changes to :material-arrow-down-bold:

    !!! success ""

        ```yaml
        plex_docker_network_mode: "container:gluetun"

        firefox_role_docker_commands:
          - "/usr/lib/firefox/firefox"
          - "--headless"

        wireguard_role_docker_ports_custom:
          - "1234:1234"
        ```

## Sandbox App Settings Migration Guide

Settings in `/opt/sandbox/settings.yml` no longer apply and must be migrated to their Inventory equivalent to persist.

!!! note ""

    For convenience, Sandbox roles that previously read settings from `/opt/sandbox/settings.yml` were updated to expose those settings as scalar Inventory variables instead. If you encounter a role missing this update, please report it on Discord or open an issue in the Sandbox repository.

As always, check how the settings you use are represented in the role by looking up the variables in the app's documentation under _Role Defaults_ and transfer the values accordingly.

???+example

    !!! bug ""

        ```yaml title="/opt/sandbox/settings.yml"
        your_spotify:
          public_key: "3e3ce6e568f6e9a8894c835b34f1701a"
          secret_key: "0593b2fec4867575d741e93a6cff3580"
        ```

    :material-arrow-down-bold: changes to :material-arrow-down-bold:

    !!! success ""

        ```yaml title="Inventory"
        your_spotify_role_public_key: "3e3ce6e568f6e9a8894c835b34f1701a"
        your_spotify_role_secret_key: "0593b2fec4867575d741e93a6cff3580"
        ```
