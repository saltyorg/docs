---
hide:
  - tags
tags:
  - nvidia
---

# Enabling Nvidia Support in Saltbox

Saltbox provides support for Nvidia GPUs, allowing you to leverage hardware acceleration for various tasks. This guide will walk you through the process of enabling Nvidia support by modifying specific variables in your [inventory](../saltbox/inventory/index.md).

## Overview

This process has a couple steps:

1. get the Nvidia driver installed
2. enabled Nvidia support in Saltbox
3. recreate containers to enable that Nvidia support once the driver is installed

## Configuration Variables

To enable Nvidia support, you need to modify at least one of the following variables in your [inventory](../saltbox/inventory/index.md) file:

```yaml
# Set to true to enable Nvidia
nvidia_enabled: false

# Fetches the latest supported driver version supported by the keylase patch when set to "latest"
# If set to "ignore" then driver installation will be ignored and only patching will run.
# Otherwise specify a valid driver like this (it being a quoted string is important):
# nvidia_driver_version: "555.58.02"
nvidia_driver_version: "latest"
```

### Enabling Nvidia Support

To enable Nvidia support, change the `nvidia_enabled` variable to `true`:

```yaml
nvidia_enabled: true
```

### Specifying Driver Version

The `nvidia_driver_version` variable allows you to control which driver version is installed:

- Set to `"latest"` to automatically fetch and install the latest supported driver version compatible with the keylase patch.
- Set to `"ignore"` to skip driver installation and only run the patching process.
- Specify a particular driver version as a quoted string, e.g., `"555.58.02"`.

## Installation and Upgrade Process

The installation and upgrade process for Nvidia support depends on which Saltbox tags you run:

### Main Tags (core, saltbox, mediabox, feederbox)

When running any of the main tags (core, saltbox, mediabox, feederbox), Saltbox will:

1. Install the Nvidia driver if it's missing.
2. Install the Nvidia Docker toolkit.

However, these tags will not upgrade or downgrade an existing driver installation.

### Nvidia Tag

To upgrade or downgrade, you need to run the `nvidia` tag specifically:

```
sb install nvidia
```

This tag will:

1. Install the specified driver version (or the latest if set to "latest").
2. Upgrade or downgrade the driver if a different version is already installed.
3. Install and configure the Nvidia Docker toolkit.

**If you run this tag to install the driver**, you also need to run a tag to reinstall any containers you want to use the nvidia card with, like `saltbox`, or `plex`, or the like.  Merely installing the driver does not configure Plex (for example) to use it.

## Important Notes

- Always ensure your `nvidia_enabled` is set to `true` before running the `nvidia` tag or any of the main tags if you want Nvidia support.
- If you're upgrading or downgrading your driver, make sure to update the `nvidia_driver_version` in your inventory before running the `nvidia` tag.
- Running the main tags will not affect an existing driver installation. To change the driver version, you must use the `nvidia` tag.


By following these guidelines, you can effectively enable and manage Nvidia support in your Saltbox installation, allowing you to take advantage of GPU acceleration for compatible applications and services.
