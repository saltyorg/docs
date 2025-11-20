---
icon: material/docker
hide:
  - tags
tags:
  - meilisearch
  - search
  - database
---

# Meilisearch

## Overview

[Meilisearch](https://www.meilisearch.com/) Meilisearch is an AI powered search tool.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf:**Project Home**](https://www.meilisearch.com/){ .md-button .md-button--stretch }

[:material-git:**GitHub Repo**](https://github.com/meilisearch/meilisearch){ .md-button .md-button--stretch }

</div>

This role is not externally exposed by default.

## Configuration

Use the ```sb inventory``` system to set any environment variables that are desired.

See [Meilisearch Environment Variables](https://www.meilisearch.com/docs/learn/self_hosted/configure_meilisearch_at_launch#environment) for supported variables

## Deployment

``` shell
sb install sandbox-meilisearch
```

## Usage

Port 7700 is open to the container by default. Also analytics are disabled by default.

Visit `https://www.meilisearch.com/docs`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    meilisearch_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `meilisearch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `meilisearch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`meilisearch_name`"

        ```yaml
        # Type: string
        meilisearch_name: meilisearch
        ```

=== "Paths"

    ??? variable string "`meilisearch_role_paths_folder`"

        ```yaml
        # Type: string
        meilisearch_role_paths_folder: "{{ meilisearch_name }}"
        ```

    ??? variable string "`meilisearch_role_paths_location`"

        ```yaml
        # Type: string
        meilisearch_role_paths_location: "{{ server_appdata_path }}/{{ meilisearch_role_paths_folder }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`meilisearch_role_docker_container`"

        ```yaml
        # Type: string
        meilisearch_role_docker_container: "{{ meilisearch_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`meilisearch_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_image_pull: true
        ```

    ??? variable string "`meilisearch_role_docker_image_repo`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image_repo: "getmeili/meilisearch"
        ```

    ??? variable string "`meilisearch_role_docker_image`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='meilisearch') }}:{{ lookup('role_var', '_docker_image_tag', role='meilisearch') }}"
        ```

    ??? variable string "`meilisearch_role_docker_image_tag`"

        ```yaml
        # Type: string
        meilisearch_role_docker_image_tag: "v1.11.1"
        ```

    <h5>Envs</h5>

    ??? variable dict "`meilisearch_role_docker_envs_default`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          MEILI_NO_ANALYTICS: "true"
          MEILI_MASTER_KEY: "{{ meilisearch_saltbox_facts.facts.secret_key }}"
        ```

    ??? variable dict "`meilisearch_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        meilisearch_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`meilisearch_role_docker_volumes_default`"

        ```yaml
        # Type: list
        meilisearch_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='meilisearch') }}/data:/meili_data"
        ```

    ??? variable list "`meilisearch_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        meilisearch_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`meilisearch_role_docker_hostname`"

        ```yaml
        # Type: string
        meilisearch_role_docker_hostname: "{{ meilisearch_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`meilisearch_role_docker_networks_alias`"

        ```yaml
        # Type: string
        meilisearch_role_docker_networks_alias: "{{ meilisearch_name }}"
        ```

    ??? variable list "`meilisearch_role_docker_networks_default`"

        ```yaml
        # Type: list
        meilisearch_role_docker_networks_default: []
        ```

    ??? variable list "`meilisearch_role_docker_networks_custom`"

        ```yaml
        # Type: list
        meilisearch_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`meilisearch_role_docker_restart_policy`"

        ```yaml
        # Type: string
        meilisearch_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`meilisearch_role_docker_state`"

        ```yaml
        # Type: string
        meilisearch_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`meilisearch_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        meilisearch_role_autoheal_enabled: true
        ```

    ??? variable string "`meilisearch_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        meilisearch_role_depends_on: ""
        ```

    ??? variable string "`meilisearch_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        meilisearch_role_depends_on_delay: "0"
        ```

    ??? variable string "`meilisearch_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        meilisearch_role_depends_on_healthchecks:
        ```

    ??? variable bool "`meilisearch_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        meilisearch_role_diun_enabled: true
        ```

    ??? variable bool "`meilisearch_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        meilisearch_role_dns_enabled: true
        ```

    ??? variable bool "`meilisearch_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        meilisearch_role_docker_controller: true
        ```

    ??? variable bool "`meilisearch_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_docker_volumes_download:
        ```

    ??? variable bool "`meilisearch_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        meilisearch_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`meilisearch_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        meilisearch_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`meilisearch_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        meilisearch_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`meilisearch_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        meilisearch_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`meilisearch_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`meilisearch_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        meilisearch_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`meilisearch_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        meilisearch_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`meilisearch_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        meilisearch_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`meilisearch_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        meilisearch_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`meilisearch_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        meilisearch_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            meilisearch_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "meilisearch2.{{ user.domain }}"
              - "meilisearch.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`meilisearch_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        meilisearch_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            meilisearch_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'meilisearch2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`meilisearch_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        meilisearch_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->