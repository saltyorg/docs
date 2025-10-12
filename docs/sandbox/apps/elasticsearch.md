---
hide:
  - tags
tags:
  - elasticsearch
  - search
  - analytics
---

# Elasticsearch

## What is it?

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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        elasticsearch_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `elasticsearch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `elasticsearch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    elasticsearch_name: elasticsearch

    ```

??? example "Settings"

    ```yaml
    # Type: string
    elasticsearch_role_docker_env_password: "elastic789"

    # Type: string
    elasticsearch_role_docker_env_http_port: "9200"

    # Type: string
    elasticsearch_role_docker_env_transport_port: "9300"

    # Type: string
    elasticsearch_role_sysctl_vm_max_map_count: "262144"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    elasticsearch_role_paths_folder: "{{ elasticsearch_name }}"

    # Type: string
    elasticsearch_role_paths_location: "{{ server_appdata_path }}/{{ elasticsearch_role_paths_folder }}"

    # Type: bool (true/false)
    elasticsearch_role_paths_recursive: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    elasticsearch_role_docker_container: "{{ elasticsearch_name }}"

    # Image
    # Type: bool (true/false)
    elasticsearch_role_docker_image_pull: true

    # Type: string
    elasticsearch_role_docker_image_repo: "docker.elastic.co/elasticsearch/elasticsearch"

    # Type: string
    elasticsearch_role_docker_image_tag: "8.11.0"

    # Type: string
    elasticsearch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='elasticsearch') }}:{{ lookup('role_var', '_docker_image_tag', role='elasticsearch') }}"

    # Envs
    # Type: dict
    elasticsearch_role_docker_envs_default: 
      TZ: "{{ tz }}"
      discovery.type: "single-node"
      node.name: "{{ elasticsearch_name }}"
      xpack.security.enabled: "false"
      ELASTIC_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='elasticsearch') }}"

    # Type: dict
    elasticsearch_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    elasticsearch_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='elasticsearch') }}:/usr/share/elasticsearch/data"

    # Type: list
    elasticsearch_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    elasticsearch_role_docker_hostname: "{{ elasticsearch_name }}"

    # Networks
    # Type: string
    elasticsearch_role_docker_networks_alias: "{{ elasticsearch_name }}"

    # Type: list
    elasticsearch_role_docker_networks_default: []

    # Type: list
    elasticsearch_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    elasticsearch_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    elasticsearch_role_docker_state: started

    # User
    # Type: string
    elasticsearch_role_docker_user: "{{ uid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    elasticsearch_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    elasticsearch_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    elasticsearch_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    elasticsearch_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    elasticsearch_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    elasticsearch_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    elasticsearch_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    elasticsearch_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    elasticsearch_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    elasticsearch_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    elasticsearch_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    elasticsearch_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    elasticsearch_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    elasticsearch_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    elasticsearch_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    elasticsearch_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    elasticsearch_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        elasticsearch_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "elasticsearch2.{{ user.domain }}"
          - "elasticsearch.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        elasticsearch_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'elasticsearch2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
