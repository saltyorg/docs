---
hide:
  - tags
tags:
  - mqtt
  - automation
  - messaging
---

# MQTT

## What is it?

[MQTT](https://mosquitto.org/) (or Eclipse Mosquitto) is a lightweight messaging protocol that is designed for use in constrained devices and low-bandwidth, high-latency, or unreliable networks. It is commonly used in Internet of Things (IoT) devices/applications for efficient and reliable communication between devices.

Also, MQTT does not have a web interface, so you will need to use a client to interact with it.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://mosquitto.org/){: .header-icons } | [:octicons-link-16: Docs](https://mosquitto.org/man/mosquitto-conf-5.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/eclipse/mosquitto){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/eclipse-mosquitto){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-mqtt

```

### 2. Setup

You can connect MQTT to [Home Assistant](homeassistant.md) and [Node Red](node_red.md) via docker hostname. Add the MQTT integration in Home Assistant and use `mqtt` as the hostname/Broker, and 1883 as the port. In Node Red, you can use the `mqtt` node to connect to the MQTT server.

While MQTT can be set up to use a username and password, it is not recommended to expose it to the internet. So by default, MQTT is not exposed to the internet, nor does it have a username and password.

To add a username and password, you will need to edit the `mosquitto.conf` file. You can find the file in the `/opt/mqtt/config/` directory. You will need to add the following lines to the file:

``` shell title="mosquitto.conf"
allow_anonymous false # (1)!
user <username> # (2)!
password <password> # (3)!
```

1. This line will disable anonymous access to the MQTT server. It is currently set to `true` by default.
2. This line will add a username to the MQTT server. Replace `<username>` with your desired username.
3. This line will add a password to the MQTT server. Replace `<password>` with your desired password.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        mqtt_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `mqtt_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `mqtt_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`mqtt_name`"

        ```yaml
        # Type: string
        mqtt_name: mqtt
        ```

=== "Paths"

    ??? variable string "`mqtt_role_paths_folder`"

        ```yaml
        # Type: string
        mqtt_role_paths_folder: "{{ mqtt_name }}"
        ```

    ??? variable string "`mqtt_role_paths_location`"

        ```yaml
        # Type: string
        mqtt_role_paths_location: "{{ server_appdata_path }}/{{ mqtt_role_paths_folder }}"
        ```

    ??? variable string "`mqtt_role_paths_config_location`"

        ```yaml
        # Type: string
        mqtt_role_paths_config_location: "{{ mqtt_role_paths_location }}/config/mosquitto.conf"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`mqtt_role_docker_container`"

        ```yaml
        # Type: string
        mqtt_role_docker_container: "{{ mqtt_name }}"
        ```

    ##### Image

    ??? variable bool "`mqtt_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        mqtt_role_docker_image_pull: true
        ```

    ??? variable string "`mqtt_role_docker_image_tag`"

        ```yaml
        # Type: string
        mqtt_role_docker_image_tag: "latest"
        ```

    ??? variable string "`mqtt_role_docker_image_repo`"

        ```yaml
        # Type: string
        mqtt_role_docker_image_repo: "eclipse-mosquitto"
        ```

    ??? variable string "`mqtt_role_docker_image`"

        ```yaml
        # Type: string
        mqtt_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mqtt') }}:{{ lookup('role_var', '_docker_image_tag', role='mqtt') }}"
        ```

    ##### Envs

    ??? variable dict "`mqtt_role_docker_envs_default`"

        ```yaml
        # Type: dict
        mqtt_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`mqtt_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        mqtt_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`mqtt_role_docker_volumes_default`"

        ```yaml
        # Type: list
        mqtt_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='mqtt') }}/config:/mosquitto/config"
          - "{{ lookup('role_var', '_paths_location', role='mqtt') }}/data:/mosquitto/data"
          - "{{ lookup('role_var', '_paths_location', role='mqtt') }}/log:/mosquitto/log"
          - "/etc/localtime:/etc/localtime:ro"
        ```

    ??? variable list "`mqtt_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        mqtt_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`mqtt_role_docker_hostname`"

        ```yaml
        # Type: string
        mqtt_role_docker_hostname: "{{ mqtt_name }}"
        ```

    ##### Networks

    ??? variable string "`mqtt_role_docker_networks_alias`"

        ```yaml
        # Type: string
        mqtt_role_docker_networks_alias: "{{ mqtt_name }}"
        ```

    ??? variable list "`mqtt_role_docker_networks_default`"

        ```yaml
        # Type: list
        mqtt_role_docker_networks_default: []
        ```

    ??? variable list "`mqtt_role_docker_networks_custom`"

        ```yaml
        # Type: list
        mqtt_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`mqtt_role_docker_restart_policy`"

        ```yaml
        # Type: string
        mqtt_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`mqtt_role_docker_state`"

        ```yaml
        # Type: string
        mqtt_role_docker_state: started
        ```

    ##### User

    ??? variable string "`mqtt_role_docker_user`"

        ```yaml
        # Type: string
        mqtt_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`mqtt_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        mqtt_role_autoheal_enabled: true
        ```

    ??? variable string "`mqtt_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        mqtt_role_depends_on: ""
        ```

    ??? variable string "`mqtt_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        mqtt_role_depends_on_delay: "0"
        ```

    ??? variable string "`mqtt_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mqtt_role_depends_on_healthchecks:
        ```

    ??? variable bool "`mqtt_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        mqtt_role_diun_enabled: true
        ```

    ??? variable bool "`mqtt_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        mqtt_role_dns_enabled: true
        ```

    ??? variable bool "`mqtt_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        mqtt_role_docker_controller: true
        ```

    ??? variable bool "`mqtt_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        mqtt_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`mqtt_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        mqtt_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`mqtt_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        mqtt_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`mqtt_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        mqtt_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`mqtt_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        mqtt_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`mqtt_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        mqtt_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`mqtt_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        mqtt_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`mqtt_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        mqtt_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            mqtt_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mqtt2.{{ user.domain }}"
              - "mqtt.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`mqtt_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        mqtt_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            mqtt_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mqtt2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`mqtt_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        mqtt_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->