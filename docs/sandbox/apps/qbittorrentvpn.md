---
icon: material/docker
title: arch-qbittorrentvpn
hide:
  - tags
tags:
  - qbittorrentvpn
  - download
  - vpn
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/binhex/arch-qbittorrentvpn
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/binhex/arch-qbittorrentvpn/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: arch-qbittorrentvpn
    summary: |-
      a qbittorrent container which includes OpenVPN and WireGuard to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down. It also includes Privoxy to allow unfiltered access to index sites.
    link: https://github.com/binhex/arch-qbittorrentvpn
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# arch-qbittorrentvpn

## Overview

[arch-qbittorrentvpn](https://github.com/binhex/arch-qbittorrentvpn) is a qbittorrent container which includes OpenVPN and WireGuard to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down. It also includes Privoxy to allow unfiltered access to index sites.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/binhex/arch-qbittorrentvpn){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/binhex/arch-qbittorrentvpn/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

=== "PIA VPN"

    In `/opt/sandbox/settings.yml`, adjust the following:

    ```
    qbittorrentvpn:
      vpn_pass: your_vpn_password
      vpn_prov: pia
      vpn_user: your_vpn_username
      vpn_client: wireguard
    ```

    As described in the github readme linked above, then run the role:

    ```shell
    sb install sandbox-qbittorrentvpn
    ```

=== "Proton VPN (Wireguard)"

    Step 01 - Please login in to [ProtonVPN-Account](https://account.protonvpn.com/account)
    Step 02 - Under "OpenVPN / IKEv2 username" section —> Copy this OpenVPN / IKEv2 username [Yeah, somehow this username is required for Wireguard]
    Step 03 - Go to [ProtonVPN-Downloads](https://account.protonvpn.com/downloads)
    Step 04 - Scroll down to "WireGuard configuration" - Please fill/select your desired settings for the configuration.
    Step 05 - Under "3. Select VPN options" —> Turn on "NAT-PMP (Port Forwarding)" —> Now download the config file and rename it to `wg0.conf`

    Now, In `/opt/sandbox/settings.yml`, adjust the following:

    ```
    qbittorrentvpn:
      vpn_pass: "protonvpn-account-password"
      vpn_prov: "protonvpn"
      vpn_user: "<OpenVPN / IKEv2 username>+pmp" #which we've copied from Step 02
      vpn_client: "wireguard"
    ```
    Example for reference
    ```
    qbittorrentvpn:
      vpn_pass: "xdfasdicmb"
      vpn_prov: "protonvpn"
      vpn_user: "zuqWGtyy7SMGQM8C+pmp"
      vpn_client: "wireguard"
    ```
    As described in the github readme linked above, then run the role:

    ```shell
    sb install sandbox-qbittorrentvpn
    ```

    While the above command runs, go to this directory `/opt/qbittorrentvpn/wireguard` (Use FTP file manager like WinSCP)
    if you don't see this directory wait for few seconds, while the previous command creates this.

    Now copy & paste your `wg0.conf' file (Refer Step 05) in this directory & Wait for the command line to complete.
    If everything went well, you should see `Playbook /opt/sandbox/sandbox.yml executed successfully.`

## Usage

Visit <https://qbittorrentvpn.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override level"><input type="checkbox" name="scope" hidden/></label>

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `qbittorrentvpn_instances`.**

    !!! example "Example override"

        === "Role-level"

            ```yaml
            qbittorrentvpn_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of qbittorrentvpn

        === "Instance-level"

            ```yaml
            qbittorrentvpn2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named qbittorrentvpn2

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `qbittorrentvpn_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `qbittorrentvpn_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`qbittorrentvpn_instances`"

        ```yaml
        # Type: list
        qbittorrentvpn_instances: ["qbittorrentvpn"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            qbittorrentvpn_instances: ["qbittorrentvpn", "qbittorrentvpn2"]
            ```

=== "Settings"

    ??? variable string "`qbittorrentvpn_log_level_daemon`{ .sb-show-on-unchecked }`qbittorrentvpn2_log_level_daemon`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_log_level_daemon: info
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_log_level_daemon: info
        ```

    ??? variable string "`qbittorrentvpn_log_level_web`{ .sb-show-on-unchecked }`qbittorrentvpn2_log_level_web`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_log_level_web: info
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_log_level_web: info
        ```

    ??? variable string "`qbittorrentvpn_name_servers`{ .sb-show-on-unchecked }`qbittorrentvpn2_name_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_name_servers: "84.200.69.80,1.1.1.1,84.200.70.40,1.0.0.1"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_name_servers: "84.200.69.80,1.1.1.1,84.200.70.40,1.0.0.1"
        ```

    ??? variable string "`qbittorrentvpn_lan_network`{ .sb-show-on-unchecked }`qbittorrentvpn2_lan_network`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_lan_network: "172.19.0.0/16"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_lan_network: "172.19.0.0/16"
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_user`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_user: "your_vpn_username"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_user: "your_vpn_username"
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_pass`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_pass`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_pass: "your_vpn_password"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_pass: "your_vpn_password"
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_prov`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_prov`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_prov: "pia"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_prov: "pia"
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_client`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_client`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_client: "wireguard"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_client: "wireguard"
        ```

=== "Web"

    ??? variable string "`qbittorrentvpn_role_web_subdomain`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_web_subdomain: "{{ qbittorrentvpn_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_web_subdomain: "{{ qbittorrentvpn_name }}"
        ```

    ??? variable string "`qbittorrentvpn_role_web_domain`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`qbittorrentvpn_role_web_port`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_web_port: "8080"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_web_port: "8080"
        ```

    ??? variable string "`qbittorrentvpn_role_web_url`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') + '.' + lookup('role_var', '_web_domain', role='qbittorrentvpn')
                                      if (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') | length > 0)
                                      else lookup('role_var', '_web_domain', role='qbittorrentvpn')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') + '.' + lookup('role_var', '_web_domain', role='qbittorrentvpn')
                                  if (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') | length > 0)
                                  else lookup('role_var', '_web_domain', role='qbittorrentvpn')) }}"
        ```

=== "DNS"

    ??? variable string "`qbittorrentvpn_role_dns_record`{ .sb-show-on-unchecked }`qbittorrentvpn2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrentvpn') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrentvpn') }}"
        ```

    ??? variable string "`qbittorrentvpn_role_dns_zone`{ .sb-show-on-unchecked }`qbittorrentvpn2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrentvpn') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrentvpn') }}"
        ```

    ??? variable bool "`qbittorrentvpn_role_dns_proxy`{ .sb-show-on-unchecked }`qbittorrentvpn2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`qbittorrentvpn_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_middleware_default`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_middleware_custom: ""
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_certresolver`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_enabled: true
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_api_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_api_enabled: true
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`qbittorrentvpn_role_docker_container`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_container: "{{ qbittorrentvpn_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_container: "{{ qbittorrentvpn_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`qbittorrentvpn_role_docker_image_pull`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_image_pull: true
        ```

    ??? variable string "`qbittorrentvpn_role_docker_image_repo`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_image_repo: "binhex/arch-qbittorrentvpn"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_image_repo: "binhex/arch-qbittorrentvpn"
        ```

    ??? variable string "`qbittorrentvpn_role_docker_image_tag`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_image_tag: "latest"
        ```

    ??? variable string "`qbittorrentvpn_role_docker_image`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrentvpn') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrentvpn') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrentvpn') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrentvpn') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`qbittorrentvpn_role_docker_envs_default`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          VPN_ENABLED: "yes"
          VPN_USER: "{{ lookup('role_var', '_vpn_user', role='qbittorrentvpn') }}"
          VPN_PASS: "{{ lookup('role_var', '_vpn_pass', role='qbittorrentvpn') }}"
          VPN_PROV: "{{ lookup('role_var', '_vpn_prov', role='qbittorrentvpn') }}"
          VPN_CLIENT: "{{ lookup('role_var', '_vpn_client', role='qbittorrentvpn') }}"
          STRICT_PORT_FORWARD: "yes"
          ENABLE_PRIVOXY: "no"
          LAN_NETWORK: "{{ qbittorrentvpn_lan_network }}"
          NAME_SERVERS: "{{ qbittorrentvpn_name_servers }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          VPN_ENABLED: "yes"
          VPN_USER: "{{ lookup('role_var', '_vpn_user', role='qbittorrentvpn') }}"
          VPN_PASS: "{{ lookup('role_var', '_vpn_pass', role='qbittorrentvpn') }}"
          VPN_PROV: "{{ lookup('role_var', '_vpn_prov', role='qbittorrentvpn') }}"
          VPN_CLIENT: "{{ lookup('role_var', '_vpn_client', role='qbittorrentvpn') }}"
          STRICT_PORT_FORWARD: "yes"
          ENABLE_PRIVOXY: "no"
          LAN_NETWORK: "{{ qbittorrentvpn_lan_network }}"
          NAME_SERVERS: "{{ qbittorrentvpn_name_servers }}"
        ```

    ??? variable dict "`qbittorrentvpn_role_docker_envs_custom`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`qbittorrentvpn_role_docker_volumes_default`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='qbittorrentvpn') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='qbittorrentvpn') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`qbittorrentvpn_role_docker_volumes_custom`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`qbittorrentvpn_role_docker_hostname`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_hostname: "{{ qbittorrentvpn_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_hostname: "{{ qbittorrentvpn_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`qbittorrentvpn_role_docker_networks_alias`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_networks_alias: "{{ qbittorrentvpn_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_networks_alias: "{{ qbittorrentvpn_name }}"
        ```

    ??? variable list "`qbittorrentvpn_role_docker_networks_default`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_networks_default: []
        ```

    ??? variable list "`qbittorrentvpn_role_docker_networks_custom`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`qbittorrentvpn_role_docker_capabilities_default`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_capabilities_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_capabilities_default:
          - NET_ADMIN
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_capabilities_default:
          - NET_ADMIN
        ```

    ??? variable list "`qbittorrentvpn_role_docker_capabilities_custom`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_capabilities_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_capabilities_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_capabilities_custom: []
        ```

    <h5>Sysctls</h5>

    ??? variable dict "`qbittorrentvpn_role_docker_sysctls`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_sysctls:
          net.ipv4.conf.all.src_valid_mark: "1"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_sysctls:
          net.ipv4.conf.all.src_valid_mark: "1"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`qbittorrentvpn_role_docker_restart_policy`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`qbittorrentvpn_role_docker_stop_timeout`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_stop_timeout: 900
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_stop_timeout: 900
        ```

    <h5>State</h5>

    ??? variable string "`qbittorrentvpn_role_docker_state`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_state: started
        ```

    <h5>Privileged</h5>

    ??? variable bool "`qbittorrentvpn_role_docker_privileged`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_privileged: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_privileged: true
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`qbittorrentvpn_role_docker_blkio_weight`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_blkio_weight:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_cpu_period`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_cpu_period:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_cpu_quota`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_cpu_quota:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_cpu_shares`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_cpu_shares:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_cpus`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_cpus:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_cpuset_cpus:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_cpuset_mems:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_kernel_memory`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_kernel_memory:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_memory`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_memory:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_memory_reservation`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_memory_reservation:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_memory_swap`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_memory_swap:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_memory_swappiness:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_shm_size`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`qbittorrentvpn_role_docker_cap_drop`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_cap_drop:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_cgroupns_mode:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_device_cgroup_rules:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_device_read_bps`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_device_read_bps:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_device_read_iops`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_device_read_iops:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_device_requests`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_device_requests:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_device_write_bps`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_device_write_bps:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_device_write_iops`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_device_write_iops:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_devices`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_devices:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_devices_default`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_devices_default:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_groups`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_groups:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_security_opts`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_security_opts:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_user`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_user:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_userns_mode`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`qbittorrentvpn_role_docker_dns_opts`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_dns_opts:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_dns_search_domains:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_dns_servers`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_dns_servers:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_domainname`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_domainname:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_exposed_ports`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_exposed_ports:
        ```

    ??? variable dict "`qbittorrentvpn_role_docker_hosts`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_hosts:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_hosts_use_common:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_ipc_mode`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_ipc_mode:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_links`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_links:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_network_mode`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_network_mode:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_pid_mode`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_pid_mode:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_ports`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_ports:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_uts`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`qbittorrentvpn_role_docker_keep_volumes`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_keep_volumes:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_mounts`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_mounts:
        ```

    ??? variable dict "`qbittorrentvpn_role_docker_storage_opts`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_storage_opts:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_tmpfs`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_tmpfs:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_volume_driver`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_volume_driver:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_volumes_from`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_volumes_from:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_volumes_global`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_volumes_global:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_working_dir`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`qbittorrentvpn_role_docker_auto_remove`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_auto_remove:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_cleanup`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_cleanup:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_force_kill`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_force_kill:
        ```

    ??? variable dict "`qbittorrentvpn_role_docker_healthcheck`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_healthcheck:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_init`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_init:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_kill_signal`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_kill_signal:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_log_driver`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_log_driver:
        ```

    ??? variable dict "`qbittorrentvpn_role_docker_log_options`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_log_options:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_oom_killer`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_oom_killer:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_oom_score_adj:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_output_logs`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_output_logs:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_paused`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_paused:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_recreate`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_recreate:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_restart_retries`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_restart_retries:
        ```

    <h5>Other Options</h5>

    ??? variable string "`qbittorrentvpn_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_cgroup_parent:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_commands`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_commands:
        ```

    ??? variable int "`qbittorrentvpn_role_docker_create_timeout`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrentvpn_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrentvpn2_docker_create_timeout:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_entrypoint`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_entrypoint:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_env_file`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_env_file:
        ```

    ??? variable dict "`qbittorrentvpn_role_docker_labels`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrentvpn_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrentvpn2_docker_labels:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_labels_use_common`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_labels_use_common:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_read_only`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_read_only:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_runtime`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_runtime:
        ```

    ??? variable list "`qbittorrentvpn_role_docker_ulimits`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrentvpn_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrentvpn2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`qbittorrentvpn_role_autoheal_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qbittorrentvpn_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qbittorrentvpn2_autoheal_enabled: true
        ```

    ??? variable string "`qbittorrentvpn_role_depends_on`{ .sb-show-on-unchecked }`qbittorrentvpn2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        qbittorrentvpn_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        qbittorrentvpn2_depends_on: ""
        ```

    ??? variable string "`qbittorrentvpn_role_depends_on_delay`{ .sb-show-on-unchecked }`qbittorrentvpn2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qbittorrentvpn_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qbittorrentvpn2_depends_on_delay: "0"
        ```

    ??? variable string "`qbittorrentvpn_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`qbittorrentvpn2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrentvpn_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrentvpn2_depends_on_healthchecks:
        ```

    ??? variable bool "`qbittorrentvpn_role_diun_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qbittorrentvpn_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qbittorrentvpn2_diun_enabled: true
        ```

    ??? variable bool "`qbittorrentvpn_role_dns_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qbittorrentvpn2_dns_enabled: true
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_controller`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qbittorrentvpn2_docker_controller: true
        ```

    ??? variable string "`qbittorrentvpn_role_docker_image_repo`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_image_repo:
        ```

    ??? variable string "`qbittorrentvpn_role_docker_image_tag`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_docker_image_tag:
        ```

    ??? variable bool "`qbittorrentvpn_role_docker_volumes_download`{ .sb-show-on-unchecked }`qbittorrentvpn2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_docker_volumes_download:
        ```

    ??? variable string "`qbittorrentvpn_role_paths_location`{ .sb-show-on-unchecked }`qbittorrentvpn2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_paths_location:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_paths_location:
        ```

    ??? variable string "`qbittorrentvpn_role_themepark_addons`{ .sb-show-on-unchecked }`qbittorrentvpn2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_themepark_addons:
        ```

    ??? variable string "`qbittorrentvpn_role_themepark_app`{ .sb-show-on-unchecked }`qbittorrentvpn2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_themepark_app:
        ```

    ??? variable string "`qbittorrentvpn_role_themepark_theme`{ .sb-show-on-unchecked }`qbittorrentvpn2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_themepark_theme:
        ```

    ??? variable dict "`qbittorrentvpn_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrentvpn_role_traefik_api_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrentvpn2_traefik_api_endpoint:
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_api_middleware`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_api_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_api_middleware:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_api_middleware:
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_api_middleware_http:
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_autodetect_enabled: false
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_certresolver`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_certresolver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_certresolver:
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_gzip_enabled: false
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_middleware_http`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_middleware_http:
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_middleware_http_insecure:
        ```

    ??? variable string "`qbittorrentvpn_role_traefik_priority`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_traefik_priority:
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_robot_enabled: true
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`qbittorrentvpn_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`qbittorrentvpn2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_wildcard_enabled: true
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_client`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_client`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_client:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_client:
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_pass`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_pass`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_pass:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_pass:
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_prov`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_prov`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_prov:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_prov:
        ```

    ??? variable string "`qbittorrentvpn_role_vpn_user`{ .sb-show-on-unchecked }`qbittorrentvpn2_vpn_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_vpn_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_vpn_user:
        ```

    ??? variable string "`qbittorrentvpn_role_web_api_http_port`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_api_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        qbittorrentvpn_role_web_api_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        qbittorrentvpn2_web_api_http_port:
        ```

    ??? variable string "`qbittorrentvpn_role_web_api_http_scheme`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_api_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        qbittorrentvpn_role_web_api_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        qbittorrentvpn2_web_api_http_scheme:
        ```

    ??? variable dict "`qbittorrentvpn_role_web_api_http_serverstransport`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_api_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrentvpn_role_web_api_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrentvpn2_web_api_http_serverstransport:
        ```

    ??? variable string "`qbittorrentvpn_role_web_api_port`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_api_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        qbittorrentvpn_role_web_api_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        qbittorrentvpn2_web_api_port:
        ```

    ??? variable string "`qbittorrentvpn_role_web_api_scheme`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_api_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        qbittorrentvpn_role_web_api_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        qbittorrentvpn2_web_api_scheme:
        ```

    ??? variable dict "`qbittorrentvpn_role_web_api_serverstransport`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_api_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrentvpn_role_web_api_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrentvpn2_web_api_serverstransport:
        ```

    ??? variable string "`qbittorrentvpn_role_web_domain`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_web_domain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_web_domain:
        ```

    ??? variable list "`qbittorrentvpn_role_web_fqdn_override`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qbittorrentvpn_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qbittorrentvpn2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            qbittorrentvpn_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrentvpn2.{{ user.domain }}"
              - "qbittorrentvpn.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            qbittorrentvpn2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrentvpn2.{{ user.domain }}"
              - "qbittorrentvpn.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`qbittorrentvpn_role_web_host_override`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        qbittorrentvpn_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        qbittorrentvpn2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            qbittorrentvpn_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrentvpn2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            qbittorrentvpn2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrentvpn2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`qbittorrentvpn_role_web_http_port`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        qbittorrentvpn_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        qbittorrentvpn2_web_http_port:
        ```

    ??? variable string "`qbittorrentvpn_role_web_http_scheme`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        qbittorrentvpn_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        qbittorrentvpn2_web_http_scheme:
        ```

    ??? variable dict "`qbittorrentvpn_role_web_http_serverstransport`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrentvpn_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrentvpn2_web_http_serverstransport:
        ```

    ??? variable string "`qbittorrentvpn_role_web_scheme`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qbittorrentvpn_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qbittorrentvpn2_web_scheme:
        ```

    ??? variable dict "`qbittorrentvpn_role_web_serverstransport`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrentvpn_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrentvpn2_web_serverstransport:
        ```

    ??? variable string "`qbittorrentvpn_role_web_subdomain`{ .sb-show-on-unchecked }`qbittorrentvpn2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrentvpn_role_web_subdomain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrentvpn2_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
