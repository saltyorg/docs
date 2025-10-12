---
hide:
  - tags
tags:
  - teamspeak
  - voicechat
---

# TeamSpeak

Software for quality voice communication via the Internet.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://teamspeak.com){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/docker-library/docs/blob/master/teamspeak/README.md){ .md-button .md-button--stretch }

[:fontawesome-brands-docker: Releases&nbsp;&nbsp;](https://hub.docker.com/_/teamspeak/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-teamspeak: Community&nbsp;&nbsp;](https://community.teamspeak.com){ .md-button .md-button--stretch }

</div>

---

## Configuration

Settings are available as Docker environment variables[<sup>:octicons-link-external-16:</sup>][envs] which you may customize using the Saltbox Inventory[<sup>:octicons-link-24:</sup>][inventory].

## Deployment

```shell
sb install sandbox-teamspeak
```

## Usage

Connect to the server using a TeamSpeak client at `teamspeak._yourdomain.com_` using the default port 9987.

[envs]: https://github.com/docker-library/docs/blob/master/teamspeak/README.md#environment-variables "Access project Docker environment variables reference"
[inventory]: ../../saltbox/inventory/index.md "Access Inventory user guide"

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        teamspeak_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `teamspeak_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `teamspeak_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    teamspeak_name: "teamspeak"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    teamspeak_role_paths_folder: "{{ teamspeak_name }}"

    # Type: string
    teamspeak_role_paths_location: "{{ server_appdata_path }}/{{ teamspeak_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    teamspeak_role_web_subdomain: "{{ teamspeak_name }}"

    # Type: string
    teamspeak_role_web_domain: "{{ user.domain }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    teamspeak_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='teamspeak') }}"

    # Type: string
    teamspeak_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='teamspeak') }}"

    # Type: bool (true/false)
    teamspeak_role_dns_proxy: false

    ```

??? example "Ports"

    ```yaml
    # Type: string
    teamspeak_role_docker_ports_9987: "{{ port_lookup_voice.meta.port
                                       if (port_lookup_voice.meta.port is defined) and (port_lookup_voice.meta.port | trim | length > 0)
                                       else '9987' }}"

    # Type: string
    teamspeak_role_docker_ports_10011: "{{ port_lookup_webquery.meta.port
                                        if (port_lookup_webquery.meta.port is defined) and (port_lookup_webquery.meta.port | trim | length > 0)
                                        else '10011' }}"

    # Type: string
    teamspeak_role_docker_ports_30033: "{{ port_lookup_file.meta.port
                                        if (port_lookup_file.meta.port is defined) and (port_lookup_file.meta.port | trim | length > 0)
                                        else '30033' }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    teamspeak_role_docker_container: "{{ teamspeak_name }}"

    # Image
    # Type: bool (true/false)
    teamspeak_role_docker_image_pull: true

    # Type: string
    teamspeak_role_docker_image_repo: "teamspeak"

    # Type: string
    teamspeak_role_docker_image_tag: "latest"

    # Type: string
    teamspeak_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='teamspeak') }}:{{ lookup('role_var', '_docker_image_tag', role='teamspeak') }}"

    # Ports
    # Type: list
    teamspeak_role_docker_ports_defaults: 
      - "{{ lookup('role_var', '_docker_ports_9987', role='teamspeak') }}:9987/udp"
      - "{{ lookup('role_var', '_docker_ports_10011', role='teamspeak') }}:10011"
      - "{{ lookup('role_var', '_docker_ports_30033', role='teamspeak') }}:30033"

    # Type: list
    teamspeak_role_docker_ports_custom: []

    # Envs
    # Type: dict
    teamspeak_role_docker_envs_default: 
      TS3SERVER_DB_PLUGIN: "ts3db_mariadb"
      TS3SERVER_DB_SQLCREATEPATH: "create_mariadb"
      TS3SERVER_DB_HOST: "mariadb"
      TS3SERVER_DB_USER: "root"
      TS3SERVER_DB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
      TS3SERVER_DB_NAME: "{{ teamspeak_name }}"
      TS3SERVER_DB_WAITUNTILREADY: "30"
      TS3SERVER_LICENSE: "accept"

    # Type: dict
    teamspeak_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    teamspeak_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='teamspeak') }}:/var/ts3server"

    # Type: list
    teamspeak_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    teamspeak_role_docker_hostname: "{{ teamspeak_name }}"

    # Networks
    # Type: string
    teamspeak_role_docker_networks_alias: "{{ teamspeak_name }}"

    # Type: list
    teamspeak_role_docker_networks_default: []

    # Type: list
    teamspeak_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    teamspeak_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    teamspeak_role_docker_state: started

    # Dependencies
    # Type: string
    teamspeak_role_depends_on: "mariadb"

    # Type: string
    teamspeak_role_depends_on_delay: "0"

    # Type: string
    teamspeak_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    teamspeak_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    teamspeak_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    teamspeak_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    teamspeak_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    teamspeak_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    teamspeak_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    teamspeak_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    teamspeak_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    teamspeak_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    teamspeak_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    teamspeak_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    teamspeak_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    teamspeak_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    teamspeak_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    teamspeak_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    teamspeak_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    teamspeak_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        teamspeak_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "teamspeak2.{{ user.domain }}"
          - "teamspeak.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        teamspeak_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'teamspeak2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
