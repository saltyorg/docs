---
icon: material/cogs
status: draft
saltbox_automation:
  project_description:
    name: System
    summary: |-
      a Saltbox module that configures system-wide settings including APT updates, network optimizations, sysctl tunings, CPU performance mode, timezone, locale, and log rotation.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# System

## Overview

System is a Saltbox module that configures system-wide settings including APT updates, network optimizations, sysctl tunings, CPU performance mode, timezone, locale, and log rotation.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Core Saltbox role.

```shell
sb install system
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        run_sysctl_tasks: true
        ```

=== "General"

    ??? variable bool "`run_sysctl_tasks`"

        ```yaml
        # Type: bool (true/false)
        run_sysctl_tasks: true
        ```

    ??? variable bool "`cpu_performance_mode`"

        ```yaml
        # Performance mode sets the CPU to run at its maximum frequency
        # Set to false to enable dynamic CPU frequency scaling instead
        # Type: bool (true/false)
        cpu_performance_mode: true
        ```

    ??? variable string "`system_inotify`"

        ```yaml
        # Type: string
        system_inotify: "524288"
        ```

    ??? variable string "`pam_limit_nofile`"

        ```yaml
        # Type: string
        pam_limit_nofile: "100000"
        ```

    ??? variable string "`timezone`"

        ```yaml
        # Type: string
        timezone: "{{ tz }}"
        ```

    ??? variable string "`timezone_string`"

        ```yaml
        # Type: string
        timezone_string: "Time zone: {{ timezone }}"
        ```

    ??? variable bool "`timezone_use_local_rtc`"

        ```yaml
        # Type: bool (true/false)
        timezone_use_local_rtc: false
        ```

    ??? variable string "`system_locale`"

        ```yaml
        # Type: string
        system_locale: "en_US.UTF-8"
        ```

    ??? variable string "`system_language`"

        ```yaml
        # Type: string
        system_language: "en_US.UTF-8"
        ```

    ??? variable string "`saltbox_max_log_size`"

        ```yaml
        # Type: string
        saltbox_max_log_size: 2M
        ```

    ??? variable string "`sysctl_netdev_budget_usecs`"

        ```yaml
        # Reminder to change the conditional in sysctl.yml if defaults change
        # Type: string
        sysctl_netdev_budget_usecs: "5000"
        ```

    ??? variable list "`sysctl_remove_settings`"

        ```yaml
        # Type: list
        sysctl_remove_settings:
          - fs.file-max
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
