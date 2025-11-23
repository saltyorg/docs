---
icon: material/server-network-outline
status: WIP
---

# UnionFS

## Overview

Installs and configures MergerFS to create a union filesystem merging local and remote storage paths, managing Docker services during mount operations.

UnionFS is a filesystem service for Linux, FreeBSD and NetBSD which implements a union mount for other file systems.

---

## Deployment

Saltbox dependency.

```shell
sb install mounts
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    local_mount_branch: "custom_value"
    ```

=== "Global"

    ??? variable string "`local_mount_branch`"

        ```yaml
        # Type: string
        local_mount_branch: "/mnt/local=RW:"
        ```

    ??? variable string "`custom_mount_branch`"

        ```yaml
        # Type: string
        custom_mount_branch: "" # Format: "/mnt/remote/someremote=NC"
        ```

    ??? variable bool "`mergerfs_override_service`"

        ```yaml
        # Type: bool (true/false)
        mergerfs_override_service: true
        ```

    ??? variable string "`mergerfs_service_name`"

        ```yaml
        # Type: string
        mergerfs_service_name: "saltbox_managed_mergerfs.service"
        ```

=== "MergerFS"

    ??? variable string "`mergerfs_version`"

        ```yaml
        # Type: string
        mergerfs_version: latest
        ```

    ??? variable string "`mergerfs_github_endpoint`"

        ```yaml
        # Type: string
        mergerfs_github_endpoint: "{{ 'latest' if (mergerfs_version == 'latest') else 'tags/' + mergerfs_version }}"
        ```

    ??? variable string "`mergerfs_releases_url`"

        ```yaml
        # Type: string
        mergerfs_releases_url: "{{ svm }}https://api.github.com/repos/trapexit/mergerfs/releases/{{ mergerfs_github_endpoint }}"
        ```

    ??? variable string "`mergerfs_releases_download_url`"

        ```yaml
        # Type: string
        mergerfs_releases_download_url: https://github.com/trapexit/mergerfs/releases/download
        ```

    ??? variable string "`mergerfs_release_distribution`"

        ```yaml
        # Type: string
        mergerfs_release_distribution: "{{ ansible_facts['distribution_release'] | lower }}"
        ```

    ??? variable string "`mergerfs_release_lookup_command`"

        ```yaml
        # Type: string
        mergerfs_release_lookup_command: |
          curl -s {{ mergerfs_releases_url }} \
            | jq -r ".assets[] | select(.name | test(\"{{ ansible_facts['distribution'] | lower }}-{{ mergerfs_release_distribution }}_amd64\")) \
            | .browser_download_url"
        ```

    ??? variable string "`mergerfs_download_backup_version`"

        ```yaml
        # Type: string
        mergerfs_download_backup_version: 2.40.2
        ```

    ??? variable string "`mergerfs_download_backup_url`"

        ```yaml
        # Type: string
        mergerfs_download_backup_url: "
          {{ mergerfs_releases_download_url }}/\
          {{ mergerfs_download_backup_version }}/\
          mergerfs_{{ mergerfs_download_backup_version }}.\
          {{ ansible_facts['distribution'] | lower }}-\
          {{ mergerfs_release_distribution }}_amd64.deb"
        ```

    ??? variable string "`mergerfs_mount_branches`"

        ```yaml
        # Type: string
        mergerfs_mount_branches: "{{ local_mount_branch }}{{ _remotes_list }}"
        ```

    ??? variable string "`mergerfs_branch_mode`"

        ```yaml
        # Type: string
        mergerfs_branch_mode: "NC"
        ```

    ??? variable string "`mergerfs_remote_branch_mode_lookup`"

        ```yaml
        # Type: string
        mergerfs_remote_branch_mode_lookup: "{{ lookup('vars', 'mergerfs_remote_' + rclone_remote_name + '_branch_mode', default=mergerfs_branch_mode) }}"
        ```

    ??? variable string "`mergerfs_mount_service_after`"

        ```yaml
        # Type: string
        mergerfs_mount_service_after: "network-online.target"
        ```

    ??? variable string "`mergerfs_mount_readdir_policy`"

        ```yaml
        # Type: string
        mergerfs_mount_readdir_policy: "seq"
        ```

    ??? variable string "`mergerfs_mount_policy_action`"

        ```yaml
        # Type: string
        mergerfs_mount_policy_action: "epall"
        ```

    ??? variable string "`mergerfs_mount_policy_create`"

        ```yaml
        # Type: string
        mergerfs_mount_policy_create: "ff"
        ```

    ??? variable string "`mergerfs_mount_policy_search`"

        ```yaml
        # Type: string
        mergerfs_mount_policy_search: "ff"
        ```

    ??? variable string "`mergerfs_mount_umask`"

        ```yaml
        # Type: string
        mergerfs_mount_umask: "002"
        ```

    ??? variable string "`mergerfs_mount_xattr`"

        ```yaml
        # Type: string
        mergerfs_mount_xattr: "nosys"
        ```

    ??? variable string "`mergerfs_mount_start_command`"

        ```yaml
        # Type: string
        mergerfs_mount_start_command: |-
          /usr/bin/mergerfs \
            -o category.create={{ mergerfs_mount_policy_create }},async_read=true,cache.files=partial \
            -o category.action={{ mergerfs_mount_policy_action }},category.search={{ mergerfs_mount_policy_search }} \
            -o dropcacheonclose=true,minfreespace=0,fsname=mergerfs \
            -o xattr={{ mergerfs_mount_xattr }},statfs=base,statfs_ignore=nc,umask={{ mergerfs_mount_umask }},noatime \
            -o func.readdir={{ mergerfs_mount_readdir_policy }} \
            "{{ mergerfs_mount_branches }}" /mnt/unionfs
        ```

    ??? variable string "`mergerfs_mount_stop_command`"

        ```yaml
        # Type: string
        mergerfs_mount_stop_command: /bin/fusermount3 -uz /mnt/unionfs
        ```

=== "Global Override Options"

    ??? variable bool "`unionfs_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        unionfs_role_autoheal_enabled: true
        ```

    ??? variable string "`unionfs_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        unionfs_role_depends_on: ""
        ```

    ??? variable string "`unionfs_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        unionfs_role_depends_on_delay: "0"
        ```

    ??? variable string "`unionfs_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        unionfs_role_depends_on_healthchecks:
        ```

    ??? variable bool "`unionfs_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        unionfs_role_diun_enabled: true
        ```

    ??? variable bool "`unionfs_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        unionfs_role_dns_enabled: true
        ```

    ??? variable bool "`unionfs_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        unionfs_role_docker_controller: true
        ```

    ??? variable bool "`unionfs_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        unionfs_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`unionfs_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        unionfs_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`unionfs_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        unionfs_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`unionfs_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        unionfs_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`unionfs_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        unionfs_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`unionfs_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        unionfs_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`unionfs_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        unionfs_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`unionfs_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        unionfs_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`unionfs_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        unionfs_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`unionfs_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        unionfs_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            unionfs_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "unionfs2.{{ user.domain }}"
              - "unionfs.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`unionfs_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        unionfs_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            unionfs_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'unionfs2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`unionfs_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        unionfs_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->