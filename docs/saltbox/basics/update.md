---
hide:
  - tags
tags:
  - update
  - apps
---

# Update

## Updating Saltbox

To pull changes, run:

```shell
sb update
```

!!! info "Updates the Saltbox files *only*—*does not* update your containers."

    For example, if a new feature is added to Saltbox, `sb update` will get that new feature. If a new version of Radarr is available, `sb update` *will not* update your Radarr to that new version.

This will also update the Saltbox CLI, Ansible, and migrate the configuration files as needed.

## Upgrading Saltbox

Every `sb update` should be followed by one of the [main tags](../../apps/main_tags.md), or at a minimum:

```shell
sb install core
```

This ensures dependencies and system configuration are up to spec with the latest Saltbox changes.

## Updating apps

Generally, to update individual applications, run the tag for that application. For example,

```shell
sb install radarr
```

This will retrieve the current version of the Radarr image and recreate the container, which will update the application version.

The same thing happens if you run one of the top-level tags:

```shell
sb install saltbox
```

This will do as above for *all* the containers installed by the `saltbox` tag.

Next, let's discuss how you will [access the applications](accessing-apps.md).
