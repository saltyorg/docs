---
icon: material/server-network-outline
status: deprecated
saltbox_automation:
  project_description:
    name: Hetzner NFS VLAN
    summary: |-
      a Saltbox module that connects 2+ Hetzner servers using NFS and VLAN.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Hetzner NFS VLAN

## Overview

Hetzner NFS VLAN is a Saltbox module that connects 2+ Hetzner servers using NFS and VLAN.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! warning "Role Currently Disabled"

    **THIS INFORMATION IS OUTDATED AND DOES NOT WORK AS DOCUMENTED**

    **DO NOT FOLLOW THESE INSTRUCTIONS IF YOU DO NOT KNOW HOW TO ADAPT THEM TO RECENT CHANGES IN BOTH SALTBOX AND HETZNER**

_Note 1: This comes with no support other than the instructions provided here._

_Note 2: This setup has been tested to work with standard Unionfs/Rclone VFS setup. Using either MergerFS or any non-standard setup will require you to tweak the appropriate mounts. You can look at the roles to see what changes need to be done._

## 1. Installation

In this example, we'll set our Feederbox as the NFS server and our Mediabox as the NFS client - this is so that the feeder data can be available to the media server.

There are 3 phases to the setup. They are broken down below.

### Hetzner Robot

1. Log into [Hetzner Robot](https://robot.your-server.de/).

1. Create a VLAN (_vSwitch_) and add servers to it. Note the VLAN ID.

  ![](../../images/community/hetzner_vswitch.png)

1. Setup Firewall.

      - Mediabox:

      ![](../../images/community/hetzner_mbox.png)

      - Feederbox:

      ![](../../images/community/hetzner_fbox.png)

### NFS Server (Feederbox)

1. Setup the Ansible role config.

   1. Add `vlan_id`.

   2. `mount_client` setting is ignored for the NFS server (i.e. it will just use `2`).

      ```shell
      nano /srv/git/saltbox/hetzner_nfs.yml
      ```

      ```yaml
      hetzner_nfs:
        vlan_id: 4001
        mount_client: 3
      ```

1. Run Ansible role to configure the NFS server.

    ```shell
    sb install hetzner-nfs-server
    ```

### NFS Client (Mediabox)

1. Setup the Ansible role config.

   1. Add `vlan_id`.

   2. Add `mount_client`.

      Note: `mount_client` will need to be either `3` or a number > `250`.

      ```shell
      nano /srv/git/saltbox/hetzner_nfs.yml
      ```

      ```yaml
      hetzner_nfs:
        vlan_id: 4001
        mount_client: 3
      ```

2. Run Ansible role to configure the NFS client.

    ```shell
    sb install hetzner-nfs-client-mount
    ```

## Uninstall

Simply run the following commands on their respective servers:

### Uninstall NFS Server (Feederbox)

```shell
sb install hetzner-nfs-server-uninstall
```

### Uninstall NFS Client (Mediabox)

```shell
sb install hetzner-nfs-client-unmount
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        hetzner_nfs_init_overwrite_client: true
        ```

=== "General"

    ??? variable bool "`hetzner_nfs_init_overwrite_client`"

        ```yaml
        # Type: bool (true/false)
        hetzner_nfs_init_overwrite_client: true
        ```

    ??? variable bool "`hetzner_nfs_init_overwrite_server`"

        ```yaml
        # Type: bool (true/false)
        hetzner_nfs_init_overwrite_server: true
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
