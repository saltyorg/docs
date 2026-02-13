---
hide:
  - tags
tags:
  - cloud
  - storage
---

# Cloud Storage

## Does Saltbox support encrypted data on the cloud?

It can, though any crypt-specific configuration will be up to you. Saltbox works with rclone remotes, and its various components will work fine if you correctly point them to encrypted remotes.

## Why does Saltbox not support encryption data on the cloud?

While there are pro's and cons for using either encrypted or unencrypted data on cloud services, we've decided to not deal with encryption for the out of box setup.

However, since Saltbox uses Rclone VFS to mount cloud data, you can tweak the mounts and remotes to do this yourself. But doing so comes with no support/help from us.

## Don't see your remote files in /mnt/remote?

[See here](../reference/guides/chazguides/no-media.md)
