---
icon: material/tag
hide:
  - tags
tags:
  - custom
saltbox_automation:
  project_description:
    name: Custom
    summary: |-
      a Saltbox module that allows you to install additional software packages (APT, DEB, and pip modules) that are not included in the default Saltbox installation, giving you the flexibility to add tools and dependencies specific to your needs.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Custom

## Overview

Custom is a Saltbox module that allows you to install additional software packages (APT, DEB, and pip modules) that are not included in the default Saltbox installation, giving you the flexibility to add tools and dependencies specific to your needs.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

Before running the custom tag, configure the packages you want to install in your Saltbox inventory:

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

## Deployment

```shell
sb install custom
```

!!! info
    The custom role is useful for installing system utilities, development tools, or dependencies required by other applications in your setup.

!!! warning
    pip installation via this role is only available on Ubuntu 22.04 and earlier.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        custom_apt: ["item1", "item2"]
        ```

=== "General"

    ??? variable list "`custom_apt`"

        ```yaml
        # Type: list
        custom_apt: []
        ```

    ??? variable list "`custom_deb`"

        ```yaml
        # Type: list
        custom_deb: []
        ```

    ??? variable list "`custom_pip`"

        ```yaml
        # Type: list
        custom_pip: []
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
