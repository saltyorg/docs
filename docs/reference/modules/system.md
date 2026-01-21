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

    ??? variable dict "`sysctl_settings`"

        ```yaml
        # Type: dict
        sysctl_settings:
          fs.inotify.max_user_watches: "{{ system_inotify }}"
          net.core.default_qdisc: fq
          net.core.netdev_budget: 50000
          net.core.netdev_max_backlog: 100000
          net.core.rmem_max: 67108864
          net.core.somaxconn: 4096
          net.core.wmem_max: 67108864
          net.ipv4.conf.all.accept_redirects: 0
          net.ipv4.conf.all.accept_source_route: 0
          net.ipv4.conf.all.secure_redirects: 0
          net.ipv4.tcp_adv_win_scale: 2
          net.ipv4.tcp_congestion_control: bbr
          net.ipv4.tcp_fin_timeout: 10
          net.ipv4.tcp_max_syn_backlog: 30000
          net.ipv4.tcp_max_tw_buckets: 2000000
          net.ipv4.tcp_mtu_probing: 1
          net.ipv4.tcp_rfc1337: 1
          net.ipv4.tcp_rmem: "4096 87380 33554432"
          net.ipv4.tcp_sack: 1
          net.ipv4.tcp_slow_start_after_idle: 0
          net.ipv4.tcp_tw_reuse: 1
          net.ipv4.tcp_window_scaling: 1
          net.ipv4.tcp_wmem: "4096 87380 33554432"
          net.ipv4.udp_rmem_min: 8192
          net.ipv4.udp_wmem_min: 8192
          vm.dirty_background_ratio: 10
          vm.dirty_ratio: 15
          vm.swappiness: 10
          net.ipv4.neigh.default.gc_thresh1: 1024
          net.ipv4.neigh.default.gc_thresh2: 2048
          net.ipv4.neigh.default.gc_thresh3: 4096
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
