---
hide:
  - tags
tags:
  - unifi
  - networking
  - wireless
---

# Unifi Network Application

## What is it?

[Unifi Network Application](https://www.ui.com/download/unifi/) software is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.ui.com/download/unifi/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/linuxserver/docker-unifi-network-application/blob/main/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/linuxserver/docker-unifi-network-application){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/unifi-network-application){: .header-icons }|

!!! warning
    This role is a replacement for the previous Unifi Controller role. This is not an in-place replacement. In order to migrate, you must perform a full backup from the Unifi web interface, and restore from that backup when running the setup wizard in a fresh instance of the Unifi Network Application. You must rename/remove the previous appdata from `/opt/unifi` before deploying the Unifi Network Application role.

### 1. Installation

``` shell

sb install sandbox-unifi-network-application

```

### 2. URL

- To access Unifi Network Application, visit `https://unifi._yourdomain.com_`

### 3. Setup

  1. Visit the Unifi Network Application site at `https://unifi._yourdomain.com_`

  2. For Unifi to adopt other devices, e.g. an Access Point, it is required to change the inform IP address. Because Unifi runs inside Docker by default it uses an IP address not accessible by other devices. To change this go to Settings > System Settings > Controller Configuration and set the Controller Hostname/IP to a hostname or IP address accessible by your devices. Additionally the checkbox "Override inform host with controller hostname/IP" has to be checked, so that devices can connect to the controller during adoption (devices use the inform-endpoint during adoption).

  In order to manually adopt a device take these steps:

  ```shell
  ssh ubnt@$AP-IP
  set-inform http://$address:8080/inform
  ```

  The default device password is `ubnt`. `$address` is the IP address of the host you are running this container on and `$AP-IP` is the Access Point IP address.

  When using a Security Gateway (router) it could be that network connected devices are unable to obtain an ip address. This can be fixed by setting "DHCP Gateway IP", under Settings > Networks > network_name, to a correct (and accessible) ip address.

- [:octicons-link-16: Documentation: Unifi Net App Docs](https://github.com/linuxserver/docker-unifi-network-application/blob/master/README.md){: .header-icons }

!!! note
      📢 The default setup only publish the 8080 tcp port, which is the bare minimum to allow communication between your network equipment and Unifi Network Application.
      Depending on your requirements, you may need additional ports according to the [:octicons-link-16: Documentation](https://github.com/linuxserver/docker-unifi-network-application#parameters) .

      The recommended way to customize these parameters is to use the [inventory](../../saltbox/inventory/index.md).

      Edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section:

      ```
      ### Open Specified Ports for the specified container ###
      ##### Unifi Ports for aditional services #####
      unifi_network_application_docker_ports_custom:
        - "1900:1900/udp" #Required for Make controller discoverable on L2 network option
        - "8843:8843/tcp" #Unifi guest portal HTTPS redirect port
        - "8880:8880/tcp" #Unifi guest portal HTTP redirect port
        - "6789:6789/tcp" #For mobile throughput test
        - "5514:5514/udp" #Remote syslog port
      ```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        unifi_network_application_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    unifi_network_application_name: unifi

    ```

??? example "Settings"

    ```yaml
    # Type: string
    unifi_network_application_mongo_user: "unifi"

    # Type: string
    unifi_network_application_mongo_pass: "password4321"

    # Type: string
    unifi_network_application_mongo_port: "27017"

    # Type: string
    unifi_network_application_mongo_dbname: "unifi"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    unifi_network_application_role_paths_folder: "{{ unifi_network_application_name }}"

    # Type: string
    unifi_network_application_role_paths_location: "{{ server_appdata_path }}/{{ unifi_network_application_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    unifi_network_application_role_web_subdomain: "{{ unifi_network_application_name }}"

    # Type: string
    unifi_network_application_role_web_domain: "{{ user.domain }}"

    # Type: string
    unifi_network_application_role_web_port: "8443"

    # Type: string
    unifi_network_application_role_web_scheme: "https"

    # Type: string
    unifi_network_application_role_web_serverstransport: "skipverify@file"

    # Type: string
    unifi_network_application_role_web_url: "{{ 'https://' + (unifi_network_application_role_web_subdomain + '.' + unifi_network_application_role_web_domain
                                             if (unifi_network_application_role_web_subdomain | length > 0)
                                             else unifi_network_application_role_web_domain) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    unifi_network_application_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='unifi_network_application') }}"

    # Type: string
    unifi_network_application_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='unifi_network_application') }}"

    # Type: bool (true/false)
    unifi_network_application_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    unifi_network_application_role_traefik_sso_middleware: ""

    # Type: string
    unifi_network_application_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    unifi_network_application_role_traefik_middleware_custom: ""

    # Type: string
    unifi_network_application_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    unifi_network_application_role_traefik_enabled: true

    # Type: bool (true/false)
    unifi_network_application_role_traefik_api_enabled: false

    # Type: string
    unifi_network_application_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    unifi_network_application_role_docker_container: "{{ unifi_network_application_name }}"

    # Image
    # Type: bool (true/false)
    unifi_network_application_role_docker_image_pull: true

    # Type: string
    unifi_network_application_role_docker_image_tag: "latest"

    # Type: string
    unifi_network_application_role_docker_image_repo: "lscr.io/linuxserver/unifi-network-application"

    # Type: string
    unifi_network_application_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='unifi_network_application') }}:{{ lookup('role_var', '_docker_image_tag', role='unifi_network_application') }}"

    # Ports
    # Type: list
    unifi_network_application_role_docker_ports_defaults: 
      - "8080:8080/tcp"
      - "3478:3478/udp"
      - "10001:10001/udp"

    # Type: list
    unifi_network_application_role_docker_ports_custom: []

    # Envs
    # Type: dict
    unifi_network_application_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      MONGO_USER: "{{ unifi_network_application_mongo_user }}"
      MONGO_PASS: "{{ unifi_network_application_mongo_pass }}"
      MONGO_HOST: "{{ unifi_network_application_name }}-mongo"
      MONGO_PORT: "{{ unifi_network_application_mongo_port }}"
      MONGO_DBNAME: "{{ unifi_network_application_mongo_dbname }}"

    # Type: dict
    unifi_network_application_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    unifi_network_application_role_docker_volumes_default: 
      - "{{ unifi_network_application_role_paths_location }}:/config"

    # Type: list
    unifi_network_application_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    unifi_network_application_role_docker_hostname: "{{ unifi_network_application_name }}"

    # Networks
    # Type: string
    unifi_network_application_role_docker_networks_alias: "{{ unifi_network_application_name }}"

    # Type: list
    unifi_network_application_role_docker_networks_default: []

    # Type: list
    unifi_network_application_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    unifi_network_application_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    unifi_network_application_role_docker_state: started

    # Dependencies
    # Type: string
    unifi_network_application_role_depends_on: "{{ unifi_network_application_name }}-mongo"

    # Type: string
    unifi_network_application_role_depends_on_delay: "0"

    # Type: string
    unifi_network_application_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    unifi_network_application_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    unifi_network_application_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    unifi_network_application_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    unifi_network_application_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    unifi_network_application_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    unifi_network_application_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    unifi_network_application_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    unifi_network_application_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    unifi_network_application_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    unifi_network_application_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    unifi_network_application_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    unifi_network_application_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    unifi_network_application_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    unifi_network_application_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    unifi_network_application_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    unifi_network_application_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    unifi_network_application_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        unifi_network_application_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "unifi_network_application2.{{ user.domain }}"
          - "unifi_network_application.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        unifi_network_application_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'unifi_network_application2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
