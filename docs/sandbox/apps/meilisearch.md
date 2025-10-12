---
hide:
  - tags
tags:
  - meilisearch
  - search
  - database
---

# Meilisearch

[Meilisearch](https://www.meilisearch.com/) Meilisearch is an AI powered search tool.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Home](https://www.meilisearch.com/){ .md-button .md-button--stretch }

[:material-git: GitHub Repo](https://github.com/meilisearch/meilisearch){ .md-button .md-button--stretch }

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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        meilisearch_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `meilisearch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `meilisearch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    meilisearch_name: meilisearch

    ```

??? example "Paths"

    ```yaml
    # Type: string
    meilisearch_role_paths_folder: "{{ meilisearch_name }}"

    # Type: string
    meilisearch_role_paths_location: "{{ server_appdata_path }}/{{ meilisearch_role_paths_folder }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    meilisearch_role_docker_container: "{{ meilisearch_name }}"

    # Image
    # Type: bool (true/false)
    meilisearch_role_docker_image_pull: true

    # Type: string
    meilisearch_role_docker_image_repo: "getmeili/meilisearch"

    # Type: string
    meilisearch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='meilisearch') }}:{{ lookup('role_var', '_docker_image_tag', role='meilisearch') }}"

    # Type: string
    meilisearch_role_docker_image_tag: "v1.11.1"

    # Envs
    # Type: dict
    meilisearch_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      MEILI_NO_ANALYTICS: "true"
      MEILI_MASTER_KEY: "{{ meilisearch_saltbox_facts.facts.secret_key }}"

    # Type: dict
    meilisearch_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    meilisearch_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='meilisearch') }}/data:/meili_data"

    # Type: list
    meilisearch_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    meilisearch_role_docker_hostname: "{{ meilisearch_name }}"

    # Networks
    # Type: string
    meilisearch_role_docker_networks_alias: "{{ meilisearch_name }}"

    # Type: list
    meilisearch_role_docker_networks_default: []

    # Type: list
    meilisearch_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    meilisearch_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    meilisearch_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    meilisearch_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    meilisearch_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    meilisearch_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    meilisearch_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    meilisearch_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    meilisearch_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    meilisearch_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    meilisearch_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    meilisearch_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    meilisearch_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    meilisearch_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    meilisearch_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    meilisearch_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    meilisearch_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    meilisearch_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    meilisearch_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    meilisearch_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        meilisearch_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "meilisearch2.{{ user.domain }}"
          - "meilisearch.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        meilisearch_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'meilisearch2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
