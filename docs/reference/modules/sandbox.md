---
status: draft
hide:
  - tags
tags:
  - sandbox
  - community
---

# Sandbox

## Overview

The Sandbox repository serves as a community-driven space for unofficial Saltbox enhancements.

---

## Update

To pull repository changes, run a standard Saltbox update:

```shell
sb update
```

## Deployment

!!! info inline end "Installed By Default"

```shell
sb install sandbox
```

## Usage

Sandbox roles are listed via the `sb list` command and under [Apps](../../apps/index.md).

To deploy a Sandbox role, use `sb install`, prepending `sandbox-` to the role tag. For example, to deploy [Kometa](../../sandbox/apps/kometa.md):

```shell
sb install sandbox-kometa
```

Before deploying a Sandbox role, it is recommended to review its documentation for any required configuration.

!!! tip

    Where possible the configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml` and used to create a default user a password for logging in.
