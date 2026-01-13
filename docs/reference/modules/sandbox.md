---
hide:
  - tags
tags:
  - sandbox
  - community
saltbox_automation:
  sections:
    inventory: false
  project_description:
    name: Sandbox
    summary: |-
      a repository that serves as a community-driven space for unofficial Saltbox enhancements and is included in a standard Saltbox installation.
    link: https://github.com/saltyorg/Sandbox
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Update

To pull repository changes, run a standard Saltbox update:

```shell
sb update
```

## Usage

Sandbox roles are listed under [Applications](../../apps/index.md) and by running:

```shell
sb list
```

To deploy a Sandbox role, use `sb install`, prepending `sandbox-` to the role tag. For example, to deploy [Kometa](../../sandbox/apps/kometa.md):

```shell
sb install sandbox-kometa
```

Before deploying a Sandbox role, it is recommended to review its documentation for any required configuration.

!!! info "App Default Login Credentials"

    Where possible, the username and password configured in your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) are used to create a default user and password for logging in.

### Custom Roles

Tags are validated against cached data. To bypass validation if developing your own role, use the `--no-cache` flag:

```shell
sb install sandbox-myapp --no-cache
```
