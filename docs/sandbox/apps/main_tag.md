---
icon: material/tag
status: draft
---

# Main Tag

## Overview

Ansible tag for deploying your Sandbox apps stack.

---

Perhaps you have a standard set of sandbox tags that you install.  To avoid installing all these individually, you can define a value for this role to allow you to install/update a set of sandbox roles in a similar manner to `sb install saltbox`

## Deployment

```shell
sb install sandbox-roles
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    : 
    ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->