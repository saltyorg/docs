---
hide:
  - tags
tags:
  - backup2
---

# Streamed Backup

The standard backup role will tar up all the directories in `/opt`, then once that operation is complete, transfer all those tar archives to an rclone/rsync destination.

Perhaps you are on a system that is space-constrained and does not allow this.

`backup2` supports only rclone targets, adn will do the tar operation straight to the rclone destination, directory by directory, without requiring the intermediate step of writing the archive to the local disk.

It will be far less performant than writing the tar archives to a local disk, but exists for use in the event that doing so is not possible.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->