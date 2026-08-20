---
hide:
  - tags
tags:
  - nvidia
---

# Enabling NVIDIA Support in Saltbox

Saltbox can install and validate an NVIDIA driver, configure the NVIDIA Container Toolkit, and add GPU access to supported containers. Driver selection is based on the NVIDIA GPUs detected in the server rather than only on a globally preferred version.

## Configuration

Enable NVIDIA support in your [inventory](../saltbox/inventory/index.md):

```yaml
nvidia_enabled: true
```

The default driver policy is suitable for most systems:

```yaml
nvidia_driver_version: "latest"
nvidia_driver_branch: "auto"
nvidia_driver_module_flavor: "auto"
nvidia_patch_enabled: true
```

### Driver Version

`nvidia_driver_version` is retained for compatibility with existing inventories and accepts the following values:

- `"latest"` selects a hardware-compatible driver using `nvidia_driver_branch`.
- `"ignore"` leaves driver installation to the user and validates the externally managed driver. Keylase patching is also skipped.
- A complete quoted version, such as `"580.95.05"`, pins that exact release.

Keep version and branch values quoted in the inventory.

### Driver Branch

`nvidia_driver_branch` controls branch selection when `nvidia_driver_version` is `"latest"`:

- `"auto"` prefers the newest compatible LTS branch. Saltbox falls back to the compatible production branch when the LTS release does not support the detected hardware.
- A quoted branch number, such as `"580"`, pins the newest compatible release in that branch.

An exact `nvidia_driver_version` may be combined with `nvidia_driver_branch: "auto"`, or with the same branch number. Conflicting exact-version and branch selections are rejected.

### Kernel Module Flavor

`nvidia_driver_module_flavor` accepts:

- `"auto"` to select an implementation supported by every detected NVIDIA GPU.
- `"open"` to require the NVIDIA open kernel modules.
- `"proprietary"` to require the proprietary kernel modules.

Saltbox stops before changing the driver if the selected module flavor is incompatible with any detected GPU.

### Keylase Patch

`nvidia_patch_enabled` defaults to `true`. The Keylase NVENC session-limit patch is considered only when a GeForce GPU is present. It is not applied to data-center-only systems because those cards do not have the GeForce session limit.

When the patch is enabled, automatic driver selection is limited to releases supported by the pinned Keylase patch. An unsupported exact version is rejected. Set the variable to `false` to use an otherwise compatible unpatched driver:

```yaml
nvidia_patch_enabled: false
```

## Hardware Validation

Before installing a managed driver, Saltbox:

1. Inventories every NVIDIA display-class PCI device.
2. Requires every device to be recognized by NVIDIA Driver Assistant.
3. Applies any hardware-specific driver branch ceiling.
4. Rejects legacy hardware that requires a branch older than R580.
5. Confirms that the selected release lists every detected GPU as supported.

On systems with more than one NVIDIA GPU, the selected driver and kernel module flavor must support all of them.

## Installation and Upgrades

Run the NVIDIA tag after enabling support:

```shell
sb install nvidia
```

The tag installs or reconciles the selected driver, validates the running driver and DKMS module, installs the NVIDIA Container Toolkit, registers the NVIDIA runtime with Docker, and installs `nvtop`.

The NVIDIA runtime is registered but is not made Docker's default runtime. Supported containers opt in with an explicit NVIDIA device request. Saltbox also mounts `/dev/dri` into an NVIDIA-enabled container when that path exists on the host.

If Saltbox disables a loaded `nouveau` driver, the server reboots before NVIDIA driver or container deployment. After reconnecting, run the original `sb install nvidia` command again from the beginning. Saltbox playbooks cannot be resumed partway through.

After a standalone NVIDIA driver installation or change, recreate each application that should use the GPU, for example:

```shell
sb install plex
```

The main `core`, `saltbox`, `mediabox`, and `feederbox` tags install a missing or unhealthy driver and configure the container toolkit. They do not replace an otherwise healthy driver merely because automatic policy now selects a different release; use `sb install nvidia` for an intentional upgrade, downgrade, branch change, or module-flavor change.

## Externally Managed Drivers

Use the following setting when the NVIDIA driver is installed and maintained outside Saltbox:

```yaml
nvidia_driver_version: "ignore"
```

Saltbox still inventories the GPUs, validates that the external driver and loaded kernel module are healthy, and configures the NVIDIA container integration. It does not install, replace, or patch the driver.

## Uninstalling NVIDIA Support

Set `nvidia_enabled` to `false`, then run:

```shell
sb install nvidia-purge
```

The purge tag removes the Saltbox-managed NVIDIA driver, packaged NVIDIA components, NVIDIA Container Toolkit, NVIDIA and `nvtop` repositories, Keylase patch and backup, `nvtop`, cached installers and metadata, and the role-managed `nouveau` blacklist. It also regenerates Docker configuration without the NVIDIA runtime. The purge tag can run while `nvidia_enabled` is `false`.

The purge may reboot at the end if NVIDIA kernel modules remain loaded. Recreate applications that previously used NVIDIA after the purge so their container configuration no longer requests the removed runtime.
