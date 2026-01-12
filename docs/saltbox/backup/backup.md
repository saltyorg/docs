---
title: Standard Backup
hide:
  - tags
tags:
  - backup
saltbox_automation:
  project_description:
    name: Standard Backup
    summary: |
      a Saltbox module that performs a backup of your Saltbox managed data.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Standard Backup

## Overview

Standard Backup is a Saltbox module that performs a backup of your Saltbox managed data.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

With Saltbox you can either run a backup task manually or schedule it to run automatically.

!!! important
    A successful backup will require free space (in `/mnt/local/Backups/Saltbox` by default) *at least* equal to the aggregate size of `/opt`. The backup creates tar archives from the directories in `/opt` and then uploads the tar archives to any destinations that you have set up in the [backup config](../../saltbox/backup/settings.md). These archives are not compressed, so there needs to be enough space for a second copy of `/opt`.

    `sudo ncdu -x /` is one way to verify the size of `/opt`.

    `df -h` is one way to verify the amount of free space available.

This backup will take some time, likely hours, and all your containers may be down the entire time depending on your disk setup.

??? note "Why so long, why are the containers down, and what can I do about this?"

    It stops all containers, creates tar archives of all directories in `/opt`, restarts all containers, then uploads the tar archives to any destinations that you have set up in the [backup config](../../saltbox/backup/settings.md). All your containers will be down for the duration of the `tar` process.

    The containers are down to prevent any applications from writing to their databases or the like while the tar process is ongoing, which could corrupt the backup and the active files. You may ask, "Why not do them one at a time?"  This is effectively impossible since there is no fixed relationship between container and appdata folder, especially with custom containers defined by the user.

    If your `/opt` directory is on a `BTRFS` volume, the containers are down for a few seconds as a snapshot is taken, then they are brought back up and the `tar` operation works from the snapshot. The entire process still takes as long as before, but the containers aren't down the entire time.

    This applies regardless of whether you are running the backup manually or on a schedule.

??? note "My rclone destination has too many saved backups! What can I do about this?"

    You can control the number of backups stored on the rclone destination using the inventory. The inventory variables you would use to do this are described on the [backup config](../../saltbox/backup/settings.md) page.

## Manual Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

    Specifically, you should make sure you have defined and enabled your desired destination(s) for the backup.

=== "Without Screen"

    ```shell
    sb install backup
    ```

    This will begin the backup in the active terminal; you will not be able to close the terminal or disconnect from your server while the backup proceeds. If you do so (deliberately or accidentally), the backup will be aborted.

=== "With Screen"

    Running the backup in `screen` will allow you to disconnect the SSH session and let the backup continue, or send it to the background while you are doing other things.

    !!! note
        This is a minimal example of using `screen`; it is not intended to teach you what `screen` is or how to use it generally.

    ```shell
    screen -dmS saltbox-backup sb install backup
    ```

    The backup is now running in the background.

    If you want to get a look at what's going on, this command will bring it to the foreground and show you the ongoing output. (this is assuming you have a single thing running in a single `screen`; see the note above about not teaching `screen` generally)

    ```shell
    screen -r
    ```

    To send it to the background again, type:
    ```
    CTRL A + D
    ```

    There are of course alternatives to `screen` that you may prefer.

## Scheduled Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

    Specifically, you should make sure you have defined and enabled your desired destination(s) for the backup **and** defined a desired cron_time:

    ```yaml
    cron:
      cron_time: weekly
    ```

    Options are: `reboot`, `yearly`, `annually`, `monthly`, `weekly`, `daily`, `hourly`.

=== "Have Saltbox configure cron"

    ```shell
    sb install set-backup
    ```

=== "Configure cron manually"

    Open your crontab file for editing:

    ```shell
    crontab -e
    ```

    Then add this line to the file. This example will run the backup every day at 4AM.

    ```shell
    0 4 * * * sudo PATH='/usr/bin:/bin:/usr/local/bin' env ANSIBLE_CONFIG='/srv/git/saltbox/ansible.cfg' '/usr/local/bin/ansible-playbook' '/srv/git/saltbox/backup.yml' '--tags' 'backup' >> '/srv/git/saltbox/saltbox_backup.log' 2>&1
    ```

    !!! note
        Visit [crontab.guru](https://crontab.guru/) for help with the scheduling format.

    Save and close the file and the schedule will be applied going forward.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        backup_size_exclude_folders: ["item1", "item2"]
        ```

=== "Size Check"

    ??? variable list "`backup_size_exclude_folders`"

        ```yaml
        # Type: list
        backup_size_exclude_folders:
          - "{{ server_appdata_path }}/plex/Library/Application Support/Plex Media Server/Cache/PhotoTranscoder"
          - "{{ server_appdata_path }}/plex/Library/Application Support/Plex Media Server/Cache/Transcode"
        ```

=== "Notifications"

    ??? variable bool "`backup_notify_stop_docker_containers`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_stop_docker_containers: true
        ```

    ??? variable bool "`backup_notify_start_docker_containers`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_start_docker_containers: true
        ```

    ??? variable bool "`backup_notify_size`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_size: true
        ```

    ??? variable bool "`backup_notify_rclone_complete`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_rclone_complete: true
        ```

    ??? variable bool "`backup_notify_rsync_complete`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_rsync_complete: true
        ```

=== "Templates"

    ??? variable string "`backup_google_template`"

        ```yaml
        # Type: string
        backup_google_template: '--drive-chunk-size="{{ backup_rclone_drive_chunk_size }}"'
        ```

    ??? variable string "`backup_dropbox_template`"

        ```yaml
        # Type: string
        backup_dropbox_template: '--dropbox-chunk-size="{{ backup_rclone_dropbox_chunk_size }}" --disable-http2 --dropbox-pacer-min-sleep=250ms'
        ```

    ??? variable string "`backup_sftp_template`"

        ```yaml
        # Type: string
        backup_sftp_template: ""
        ```

    ??? variable string "`backup_user_agent`"

        ```yaml
        # Type: string
        backup_user_agent: "{{ 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' if backup.rclone.template != 'sftp' else '' }}"
        ```

=== "Cleanup"

    ??? variable int "`backup_cleanup_number`"

        ```yaml
        # Defines how many of the archived backups to keep, so current backup is not counted in this
        # Type: int
        backup_cleanup_number: 99
        ```

    ??? variable bool "`backup_cleanup_enabled`"

        ```yaml
        # Type: bool (true/false)
        backup_cleanup_enabled: false
        ```

    ??? variable string "`backup_cleanup_custom_rclone_flags`"

        ```yaml
        # Type: string
        backup_cleanup_custom_rclone_flags: ""
        ```

=== "Snapshot Defaults"

    ??? variable string "`snapshot_type`"

        ```yaml
        # Type: string
        snapshot_type: ""
        ```

    ??? variable string "`backup_opt_path`"

        ```yaml
        # Type: string
        backup_opt_path: "{{ server_appdata_path }}/"
        ```

    ??? variable bool "`use_snapshot`"

        ```yaml
        # Type: bool (true/false)
        use_snapshot: false
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`backup_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        backup_role_docker_blkio_weight:
        ```

    ??? variable int "`backup_role_docker_cpu_period`"

        ```yaml
        # Type: int
        backup_role_docker_cpu_period:
        ```

    ??? variable int "`backup_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        backup_role_docker_cpu_quota:
        ```

    ??? variable int "`backup_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        backup_role_docker_cpu_shares:
        ```

    ??? variable string "`backup_role_docker_cpus`"

        ```yaml
        # Type: string
        backup_role_docker_cpus:
        ```

    ??? variable string "`backup_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        backup_role_docker_cpuset_cpus:
        ```

    ??? variable string "`backup_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        backup_role_docker_cpuset_mems:
        ```

    ??? variable string "`backup_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        backup_role_docker_kernel_memory:
        ```

    ??? variable string "`backup_role_docker_memory`"

        ```yaml
        # Type: string
        backup_role_docker_memory:
        ```

    ??? variable string "`backup_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        backup_role_docker_memory_reservation:
        ```

    ??? variable string "`backup_role_docker_memory_swap`"

        ```yaml
        # Type: string
        backup_role_docker_memory_swap:
        ```

    ??? variable int "`backup_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        backup_role_docker_memory_swappiness:
        ```

    ??? variable string "`backup_role_docker_shm_size`"

        ```yaml
        # Type: string
        backup_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`backup_role_docker_cap_drop`"

        ```yaml
        # Type: list
        backup_role_docker_cap_drop:
        ```

    ??? variable string "`backup_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        backup_role_docker_cgroupns_mode:
        ```

    ??? variable list "`backup_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        backup_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`backup_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        backup_role_docker_device_read_bps:
        ```

    ??? variable list "`backup_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        backup_role_docker_device_read_iops:
        ```

    ??? variable list "`backup_role_docker_device_requests`"

        ```yaml
        # Type: list
        backup_role_docker_device_requests:
        ```

    ??? variable list "`backup_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        backup_role_docker_device_write_bps:
        ```

    ??? variable list "`backup_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        backup_role_docker_device_write_iops:
        ```

    ??? variable list "`backup_role_docker_devices`"

        ```yaml
        # Type: list
        backup_role_docker_devices:
        ```

    ??? variable string "`backup_role_docker_devices_default`"

        ```yaml
        # Type: string
        backup_role_docker_devices_default:
        ```

    ??? variable list "`backup_role_docker_groups`"

        ```yaml
        # Type: list
        backup_role_docker_groups:
        ```

    ??? variable bool "`backup_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_privileged:
        ```

    ??? variable list "`backup_role_docker_security_opts`"

        ```yaml
        # Type: list
        backup_role_docker_security_opts:
        ```

    ??? variable string "`backup_role_docker_user`"

        ```yaml
        # Type: string
        backup_role_docker_user:
        ```

    ??? variable string "`backup_role_docker_userns_mode`"

        ```yaml
        # Type: string
        backup_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`backup_role_docker_dns_opts`"

        ```yaml
        # Type: list
        backup_role_docker_dns_opts:
        ```

    ??? variable list "`backup_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        backup_role_docker_dns_search_domains:
        ```

    ??? variable list "`backup_role_docker_dns_servers`"

        ```yaml
        # Type: list
        backup_role_docker_dns_servers:
        ```

    ??? variable string "`backup_role_docker_domainname`"

        ```yaml
        # Type: string
        backup_role_docker_domainname:
        ```

    ??? variable list "`backup_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        backup_role_docker_exposed_ports:
        ```

    ??? variable string "`backup_role_docker_hostname`"

        ```yaml
        # Type: string
        backup_role_docker_hostname:
        ```

    ??? variable dict "`backup_role_docker_hosts`"

        ```yaml
        # Type: dict
        backup_role_docker_hosts:
        ```

    ??? variable bool "`backup_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_hosts_use_common:
        ```

    ??? variable string "`backup_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        backup_role_docker_ipc_mode:
        ```

    ??? variable list "`backup_role_docker_links`"

        ```yaml
        # Type: list
        backup_role_docker_links:
        ```

    ??? variable string "`backup_role_docker_network_mode`"

        ```yaml
        # Type: string
        backup_role_docker_network_mode:
        ```

    ??? variable list "`backup_role_docker_networks`"

        ```yaml
        # Type: list
        backup_role_docker_networks:
        ```

    ??? variable string "`backup_role_docker_pid_mode`"

        ```yaml
        # Type: string
        backup_role_docker_pid_mode:
        ```

    ??? variable list "`backup_role_docker_ports`"

        ```yaml
        # Type: list
        backup_role_docker_ports:
        ```

    ??? variable string "`backup_role_docker_uts`"

        ```yaml
        # Type: string
        backup_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`backup_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_keep_volumes:
        ```

    ??? variable list "`backup_role_docker_mounts`"

        ```yaml
        # Type: list
        backup_role_docker_mounts:
        ```

    ??? variable dict "`backup_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        backup_role_docker_storage_opts:
        ```

    ??? variable list "`backup_role_docker_tmpfs`"

        ```yaml
        # Type: list
        backup_role_docker_tmpfs:
        ```

    ??? variable string "`backup_role_docker_volume_driver`"

        ```yaml
        # Type: string
        backup_role_docker_volume_driver:
        ```

    ??? variable list "`backup_role_docker_volumes`"

        ```yaml
        # Type: list
        backup_role_docker_volumes:
        ```

    ??? variable list "`backup_role_docker_volumes_from`"

        ```yaml
        # Type: list
        backup_role_docker_volumes_from:
        ```

    ??? variable bool "`backup_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_volumes_global:
        ```

    ??? variable string "`backup_role_docker_working_dir`"

        ```yaml
        # Type: string
        backup_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`backup_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_auto_remove:
        ```

    ??? variable bool "`backup_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_cleanup:
        ```

    ??? variable string "`backup_role_docker_force_kill`"

        ```yaml
        # Type: string
        backup_role_docker_force_kill:
        ```

    ??? variable dict "`backup_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        backup_role_docker_healthcheck:
        ```

    ??? variable int "`backup_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        backup_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`backup_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_init:
        ```

    ??? variable string "`backup_role_docker_kill_signal`"

        ```yaml
        # Type: string
        backup_role_docker_kill_signal:
        ```

    ??? variable string "`backup_role_docker_log_driver`"

        ```yaml
        # Type: string
        backup_role_docker_log_driver:
        ```

    ??? variable dict "`backup_role_docker_log_options`"

        ```yaml
        # Type: dict
        backup_role_docker_log_options:
        ```

    ??? variable bool "`backup_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_oom_killer:
        ```

    ??? variable int "`backup_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        backup_role_docker_oom_score_adj:
        ```

    ??? variable bool "`backup_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_output_logs:
        ```

    ??? variable bool "`backup_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_paused:
        ```

    ??? variable bool "`backup_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_recreate:
        ```

    ??? variable string "`backup_role_docker_restart_policy`"

        ```yaml
        # Type: string
        backup_role_docker_restart_policy:
        ```

    ??? variable int "`backup_role_docker_restart_retries`"

        ```yaml
        # Type: int
        backup_role_docker_restart_retries:
        ```

    ??? variable int "`backup_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        backup_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`backup_role_docker_capabilities`"

        ```yaml
        # Type: list
        backup_role_docker_capabilities:
        ```

    ??? variable string "`backup_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        backup_role_docker_cgroup_parent:
        ```

    ??? variable list "`backup_role_docker_commands`"

        ```yaml
        # Type: list
        backup_role_docker_commands:
        ```

    ??? variable string "`backup_role_docker_container`"

        ```yaml
        # Type: string
        backup_role_docker_container:
        ```

    ??? variable int "`backup_role_docker_create_timeout`"

        ```yaml
        # Type: int
        backup_role_docker_create_timeout:
        ```

    ??? variable string "`backup_role_docker_entrypoint`"

        ```yaml
        # Type: string
        backup_role_docker_entrypoint:
        ```

    ??? variable string "`backup_role_docker_env_file`"

        ```yaml
        # Type: string
        backup_role_docker_env_file:
        ```

    ??? variable dict "`backup_role_docker_envs`"

        ```yaml
        # Type: dict
        backup_role_docker_envs:
        ```

    ??? variable string "`backup_role_docker_image`"

        ```yaml
        # Type: string
        backup_role_docker_image:
        ```

    ??? variable bool "`backup_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_image_pull:
        ```

    ??? variable dict "`backup_role_docker_labels`"

        ```yaml
        # Type: dict
        backup_role_docker_labels:
        ```

    ??? variable bool "`backup_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_labels_use_common:
        ```

    ??? variable bool "`backup_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        backup_role_docker_read_only:
        ```

    ??? variable string "`backup_role_docker_runtime`"

        ```yaml
        # Type: string
        backup_role_docker_runtime:
        ```

    ??? variable list "`backup_role_docker_sysctls`"

        ```yaml
        # Type: list
        backup_role_docker_sysctls:
        ```

    ??? variable list "`backup_role_docker_ulimits`"

        ```yaml
        # Type: list
        backup_role_docker_ulimits:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
