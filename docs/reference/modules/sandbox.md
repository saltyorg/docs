---
icon: material/source-repository
status: WIP
hide:
  - tags
tags:
  - sandbox
  - community
---

# Sandbox

## Overview

The Sandbox repository serves as a community-driven space for unofficial Saltbox enhancements.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-home:**Homepage**](https://github.com/saltyorg/Sandbox){ .md-button .md-button--stretch }

[:material-bookshelf:**Manual**](){ .md-button .md-button--stretch }

[:octicons-container-16:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/ugfKXpFND8){ .md-button .md-button--stretch }

</div>

---

## Deployment

!!! info inline end "Installed By Default"

```shell
sb install sandbox
```

## Update

To pull repository changes, run a standard Saltbox update:

```shell
sb update
```

## Usage

Sandbox roles are listed via the `sb list` command and under [Apps](../../apps/index.md).

To deploy a Sandbox role, use `sb install`, prepending `sandbox-` to the role tag. Example:

```shell title="To deploy Kometa"
sb install sandbox-kometa
```

!!! tip

    Where possible the configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml` and used to create a default user a password for logging in.
