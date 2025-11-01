---
hide:
  - tags
tags:
  - elasticsearch
  - search
  - analytics
---

# Elasticsearch

## Overview

[Elasticsearch](https://www.elastic.co/elasticsearch) is an open source distributed, RESTful search and analytics engine, scalable data store, and vector database capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data for lightning-fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.

!!! info
    Elasticsearch is typically not a standalone app, it is run in tandem with another role to enable features.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.elastic.co/elasticsearch){: .header-icons } | [:octicons-link-16: Docs](https://www.elastic.co/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/elastic/elasticsearch){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/elasticsearch){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-elasticsearch

```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    elasticsearch_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `elasticsearch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `elasticsearch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`elasticsearch_name`"

        ```yaml
        # Type: string
        elasticsearch_name: elasticsearch
        ```

=== "Settings"

    ??? variable string "`elasticsearch_role_docker_env_password`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_password: "elastic789"
        ```

    ??? variable string "`elasticsearch_role_docker_env_http_port`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_http_port: "9200"
        ```

    ??? variable string "`elasticsearch_role_docker_env_transport_port`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_env_transport_port: "9300"
        ```

    ??? variable string "`elasticsearch_role_sysctl_vm_max_map_count`"

        ```yaml
        # Type: string
        elasticsearch_role_sysctl_vm_max_map_count: "262144"
        ```

=== "Paths"

    ??? variable string "`elasticsearch_role_paths_folder`"

        ```yaml
        # Type: string
        elasticsearch_role_paths_folder: "{{ elasticsearch_name }}"
        ```

    ??? variable string "`elasticsearch_role_paths_location`"

        ```yaml
        # Type: string
        elasticsearch_role_paths_location: "{{ server_appdata_path }}/{{ elasticsearch_role_paths_folder }}"
        ```

    ??? variable bool "`elasticsearch_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_paths_recursive: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`elasticsearch_role_docker_container`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_container: "{{ elasticsearch_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`elasticsearch_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_docker_image_pull: true
        ```

    ??? variable string "`elasticsearch_role_docker_image_repo`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image_repo: "docker.elastic.co/elasticsearch/elasticsearch"
        ```

    ??? variable string "`elasticsearch_role_docker_image_tag`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image_tag: "8.11.0"
        ```

    ??? variable string "`elasticsearch_role_docker_image`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='elasticsearch') }}:{{ lookup('role_var', '_docker_image_tag', role='elasticsearch') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`elasticsearch_role_docker_envs_default`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_envs_default: 
          TZ: "{{ tz }}"
          discovery.type: "single-node"
          node.name: "{{ elasticsearch_name }}"
          xpack.security.enabled: "false"
          ELASTIC_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='elasticsearch') }}"
        ```

    ??? variable dict "`elasticsearch_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        elasticsearch_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`elasticsearch_role_docker_volumes_default`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='elasticsearch') }}:/usr/share/elasticsearch/data"
        ```

    ??? variable list "`elasticsearch_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`elasticsearch_role_docker_hostname`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_hostname: "{{ elasticsearch_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`elasticsearch_role_docker_networks_alias`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_networks_alias: "{{ elasticsearch_name }}"
        ```

    ??? variable list "`elasticsearch_role_docker_networks_default`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_networks_default: []
        ```

    ??? variable list "`elasticsearch_role_docker_networks_custom`"

        ```yaml
        # Type: list
        elasticsearch_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`elasticsearch_role_docker_restart_policy`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`elasticsearch_role_docker_state`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`elasticsearch_role_docker_user`"

        ```yaml
        # Type: string
        elasticsearch_role_docker_user: "{{ uid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`elasticsearch_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        elasticsearch_role_autoheal_enabled: true
        ```

    ??? variable string "`elasticsearch_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        elasticsearch_role_depends_on: ""
        ```

    ??? variable string "`elasticsearch_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        elasticsearch_role_depends_on_delay: "0"
        ```

    ??? variable string "`elasticsearch_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        elasticsearch_role_depends_on_healthchecks:
        ```

    ??? variable bool "`elasticsearch_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        elasticsearch_role_diun_enabled: true
        ```

    ??? variable bool "`elasticsearch_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        elasticsearch_role_dns_enabled: true
        ```

    ??? variable bool "`elasticsearch_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        elasticsearch_role_docker_controller: true
        ```

    ??? variable bool "`elasticsearch_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        elasticsearch_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`elasticsearch_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        elasticsearch_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`elasticsearch_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        elasticsearch_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`elasticsearch_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        elasticsearch_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`elasticsearch_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`elasticsearch_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        elasticsearch_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`elasticsearch_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        elasticsearch_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`elasticsearch_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        elasticsearch_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`elasticsearch_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        elasticsearch_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`elasticsearch_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        elasticsearch_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            elasticsearch_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "elasticsearch2.{{ user.domain }}"
              - "elasticsearch.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`elasticsearch_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        elasticsearch_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            elasticsearch_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'elasticsearch2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`elasticsearch_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        elasticsearch_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->