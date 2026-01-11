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

!!! note "Updates the Saltbox files *only*—*does not* update your containers."

    For example, if a new feature is added to Saltbox, `sb update` will get that new feature. If a new version of Sonarr is available, `sb update` *will not* update your Sonarr to that new version.

This command also updates the Saltbox CLI, Ansible, Sandbox, and migrates configuration files if required.

## Upgrading the server

A Saltbox update should generally be followed by a run of one of the [main tags](../../reference/modules/main_tags.md), or at
minimum:

```shell
sb install core
```

This ensures all dependencies and system configuration are current with the last commit.

## Updating apps

Generally, to update individual applications, run the tag for that application. For example:

```shell
sb install sonarr
```

This command pulls the latest Sonarr image and recreates the container, updating the application.

Include more applications in that process by running one of the top-level tags, such as:

```shell
sb install saltbox
```

The above updates the Saltbox selection of apps, along with core modules.

## Quick Reference

| Action         | Command              | Effect                                        |
|----------------|----------------------|-----------------------------------------------|
| Update Saltbox | `sb update`          | Updates Saltbox files                         |
| Upgrade core   | `sb install core`    | Updates core modules                          |
| Update an app  | `sb install sonarr`  | Updates Sonarr                                |
| Upgrade bundle | `sb install saltbox` | Updates core modules & Saltbox apps selection |

## Next

The following guide addresses [accessing the applications](accessing-apps.md).
