---
icon: material/cogs
status: WIP
---

# System

## Overview

Configures system-wide settings including APT updates, network optimizations, sysctl tunings, CPU performance mode, timezone, locale, and log rotation.

---

Saltbox dependency.

## Deployment

```shell
sb install system
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
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

=== "Global Override Options"

    ??? variable bool "`system_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        system_role_autoheal_enabled: true
        ```

    ??? variable string "`system_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        system_role_depends_on: ""
        ```

    ??? variable string "`system_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        system_role_depends_on_delay: "0"
        ```

    ??? variable string "`system_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        system_role_depends_on_healthchecks:
        ```

    ??? variable bool "`system_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        system_role_diun_enabled: true
        ```

    ??? variable bool "`system_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        system_role_dns_enabled: true
        ```

    ??? variable bool "`system_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        system_role_docker_controller: true
        ```

    ??? variable bool "`system_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        system_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`system_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        system_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`system_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        system_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`system_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        system_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`system_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        system_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`system_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        system_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`system_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        system_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`system_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        system_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`system_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        system_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`system_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        system_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            system_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "system2.{{ user.domain }}"
              - "system.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`system_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        system_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            system_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'system2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`system_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        system_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->