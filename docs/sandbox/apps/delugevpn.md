---
hide:
  - tags
tags:
  - delugevpn
  - download
  - vpn
---

# DelugeVPN

## What is it?

[DelugeVPN](https://deluge-torrent.org/) is a VPN version of [Deluge](../../apps/deluge.md) with OpenVPN to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://deluge-torrent.org/){: .header-icons } | [:octicons-link-16: Docs](https://dev.deluge-torrent.org/wiki/UserGuide){: .header-icons } | [:octicons-mark-github-16: Github](https://www.github.com/binhex/arch-delugevpn){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/binhex/arch-delugevpn){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-delugevpn

```

### 2. URL

- To access DelugeVPN, visit `https://delugevpn._yourdomain.com_`

### 3. Setup

See the parent [Deluge](../../apps/deluge.md) role for app setup.

- Edit the DelugeVPN settings in the delugevpn section in [saltbox `settings.yml`:](../settings.md) as shown below.

   ``` { .yaml }
    delugevpn:
      vpn_endpoint: netherlands.ovpn
      vpn_pass: your_vpn_password
      vpn_prov: pia
      vpn_user: your_vpn_username
      vpn_client: wireguard # 'wireguard' or 'openvpn'
   ```

**For Private Internet Access** <br />

- Add your user name and password
- Change the vpn_endpoint to your chosen server.  Note that PIA occasionally changes which servers have port forwarding.  The Netherlands server no longer offers port forwarding.  See configuration section for more details.

**For other VPN providers** <br />

- Add your user name and password
- Change `vpn_prov` to `custom`
- Leave `vpn_endpoint` as `netherlands.ovpn`
- Follow step 2 below then immediately follow step 3

### Run the DelugeVPN Role

``` { .shell }

sb install sandbox-delugevpn

```

### Configuring Server for Custom VPN providers (only for non-pia)**

Why you need to do this

For custom VPN providers, delugevpn needs an ovpn file to complete the install properly. It can check for a custom file in the `/opt/delugevpn/openvpn` folder, but this folder does not yet exist. Therefore, we will first use PIA's `netherlands.ovpn` file, which we will modify later to have our own VPN provider details.

The steps above have created some files in `/opt/delugevpn/openvpn`.

- `ca.rsa.2048.crt`  - Leave this
- `crl.rsa.2048.pem` - Leave this
- `credentials.conf`  - Leave this. Your VPN username and password are stored here.
- `netherlands.ovpn`  - Your server details are stored here. We will change this.

```shell
docker stop delugevpn
cd /opt/delugevpn/openvpn
rm netherlands.ovpn
```

Now you can upload your own .ovpn file from your VPN provider, renamed as `netherlands.ovpn`. If your VPN provider has also included a `ca.crt` file, upload that file as well. Upload one or both files into `/opt/delugevpn/openvpn`.

### Note

Do not rename the original `netherlands.ovpn` file if you're using Filezilla. delugevpn will automatically use the renamed file instead of `netherlands.ovpn` and your newly uploaded .ovpn file will still be ignored.

Now you can restart the docker

```shell
docker start delugevpn
```

## Configuration

### FOR PIA

- **vpn_user:** Your PIA user name

- **vpn_pass:** Your PIA password

- **vpn_prov:** pia

- **vpn_endpoint:** netherlands.ovpn

**Included PIA OpenVPN end point options are.**

|  **Endpoint** | **Endpoint** |  **Endpoint** |  **Endpoint** |
|: ------------- |: ------------- |: ------------- |: ------------- |
| albania.ovpn | egypt.ovpn | monaco.ovpn | uk_london.ovp |
| algeria.ovpn | finland.ovpn | mongolia.ovpn | uk_manchester.ovpn |
| andorra.ovpn | france.ovpn | montenegro.ovpn | uk_southampton.ovpn |
| argentina.ovpn | georgia.ovpn | morocco.ovpn | ukraine.ovpn |
| armenia.ovpn | greece.ovpn | netherlands.ovpn | united_arab_emirates.ovpn |
| au_melbourne.ovpn | greenland.ovpn | new_zealand.ovpn | us_atlanta.ovpn |
| au_perth.ovpn | hong_kong.ovpn | nigeria.ovpn | us_california.ovpn |
| au_sydney.ovpn | hungary.ovpn | norway.ovpn | us_chicago.ovpn |
| austria.ovpn | iceland.ovpn | panama.ovpn | us_denver.ovpn |
| bahamas.ovpn | india.ovpn | philippines.ovpn | us_east.ovpn |
| bangladesh.ovpn | ireland.ovpn | poland.ovpn | us_florida.ovpn |
| belgium.ovpn | isle_of_man.ovpn | portugal.ovpn | us_houston.ovpn |
| brazil.ovpn | israel.ovpn | qatar.ovpn | us_las_vegas.ovpn |
| bulgaria.ovpn | italy.ovpn | romania.ovpn | us_new_york.ovpn |
| ca_montreal.ovpn | japan.ovpn | saudi_arabia.ovpn | us_seattle.ovpn |
| ca_ontario.ovpn | kazakhstan.ovpn | serbia.ovpn | us_silicon_valley.ovpn |
| ca_toronto.ovpn | latvia.ovpn | singapore.ovpn | us_texas.ovpn |
| ca_vancouver.ovpn | liechtenstein.ovpn | slovakia.ovpn | us_washington_dc.ovpn |
| cambodia.ovpn | lithuania.ovpn | south_africa.ovpn | us_west.ovpn |
| china.ovpn | luxembourg.ovpn | spain.ovpn | venezuela.ovpn |
| cyprus.ovpn | macao.ovpn | sri_lanka.ovpn | vietnam.ovpn |
| czech_republic.ovpn | macedonia.ovpn | sweden.ovpn |
| de_berlin.ovpn | malta.ovpn | switzerland.ovpn |
| de_frankfurt.ovpn | mexico.ovpn | taiwan.ovpn |
| denmark.ovpn | moldova.ovpn | turkey.ovpn |

As of July 4, 2020, the PIA servers that allow port forwarding, and DelugeVPN to work properly, are: CA Toronto, CA Montreal, CA Vancouver, Czech Republic, DE Berlin, DE Frankfurt, France, Israel, Romania, Spain, Switzerland, Sweden.  Check the PIA website for changes if these servers do not work.

### Tips

- If you run into issues check `settings.yml` modified during pre install setup.
- If your endpoint has spaces you can use single quotes in the settings.yml ex.)   `vpn_endpoint: 'CA Toronto.ovpn'`
- After checking/fixing `settings.yml` execute `sudo rm -rf /opt/delugevpn`
- **WARNING:** this will delete all files and folder in /opt/delugevpn, backup first if you need anything)
- Follow installation steps above again

### For app specific instructions refer to the parent role

- [Deluge](../../apps/deluge.md)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        delugevpn_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `delugevpn_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `delugevpn_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    delugevpn_name: delugevpn

    ```

??? example "Settings"

    ```yaml
    # Type: string
    delugevpn_role_log_level_daemon: info

    # Type: string
    delugevpn_role_log_level_web: info

    # Type: string
    delugevpn_role_name_servers: "84.200.69.80,1.1.1.1,84.200.70.40,1.0.0.1"

    # Type: string
    delugevpn_role_lan_network: "172.19.0.0/16"

    # Type: string
    delugevpn_role_vpn_user: ""

    # Type: string
    delugevpn_role_vpn_pass: ""

    # Type: string
    delugevpn_role_vpn_prov: "pia"

    # Type: string
    delugevpn_role_vpn_client: "wireguard"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    delugevpn_role_paths_folder: "{{ delugevpn_name }}"

    # Type: string
    delugevpn_role_paths_location: "{{ server_appdata_path }}/{{ delugevpn_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    delugevpn_role_web_subdomain: "{{ delugevpn_name }}"

    # Type: string
    delugevpn_role_web_domain: "{{ user.domain }}"

    # Type: string
    delugevpn_role_web_port: "8112"

    # Type: string
    delugevpn_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='delugevpn') + '.' + lookup('role_var', '_web_domain', role='delugevpn')
                             if (lookup('role_var', '_web_subdomain', role='delugevpn') | length > 0)
                             else lookup('role_var', '_web_domain', role='delugevpn')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    delugevpn_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='delugevpn') }}"

    # Type: string
    delugevpn_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='delugevpn') }}"

    # Type: bool (true/false)
    delugevpn_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    delugevpn_role_traefik_sso_middleware: ""

    # Type: string
    delugevpn_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    delugevpn_role_traefik_middleware_custom: ""

    # Type: string
    delugevpn_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    delugevpn_role_traefik_enabled: true

    # Type: bool (true/false)
    delugevpn_role_traefik_api_enabled: false

    # Type: string
    delugevpn_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    delugevpn_role_docker_container: "{{ delugevpn_name }}"

    # Image
    # Type: bool (true/false)
    delugevpn_role_docker_image_pull: true

    # Type: string
    delugevpn_role_docker_image_repo: "binhex/arch-delugevpn"

    # Type: string
    delugevpn_role_docker_image_tag: "latest"

    # Type: string
    delugevpn_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='delugevpn') }}:{{ lookup('role_var', '_docker_image_tag', role='delugevpn') }}"

    # Ports
    # Type: list
    delugevpn_role_docker_ports_defaults: 
      - "58112:58112"
      - "58846:58846"

    # Type: list
    delugevpn_role_docker_ports_custom: []

    # Envs
    # Type: dict
    delugevpn_role_docker_envs_default: 
      DEBUG: "false"
      DELUGE_DAEMON_LOG_LEVEL: "{{ lookup('role_var', '_log_level_daemon', role='delugevpn') }}"
      DELUGE_WEB_LOG_LEVEL: "{{ lookup('role_var', '_log_level_web', role='delugevpn') }}"
      ENABLE_PRIVOXY: "no"
      LAN_NETWORK: "{{ lookup('role_var', '_lan_network', role='delugevpn') }}"
      NAME_SERVERS: "{{ lookup('role_var', '_name_servers', role='delugevpn') }}"
      PGID: "{{ gid }}"
      PUID: "{{ uid }}"
      STRICT_PORT_FORWARD: "yes"
      TZ: "{{ tz }}"
      UMASK: "022"
      VPN_CLIENT: "{{ lookup('role_var', '_vpn_client', role='delugevpn') }}"
      VPN_ENABLED: "yes"
      VPN_PASS: "{{ lookup('role_var', '_vpn_pass', role='delugevpn') }}"
      VPN_PROV: "{{ lookup('role_var', '_vpn_prov', role='delugevpn') }}"
      VPN_USER: "{{ lookup('role_var', '_vpn_user', role='delugevpn') }}"

    # Type: dict
    delugevpn_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    delugevpn_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='delugevpn') }}:/config"
      - "/etc/localtime:/etc/localtime:ro"
      - "/opt/scripts:/scripts"

    # Type: list
    delugevpn_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    delugevpn_role_docker_hostname: "{{ delugevpn_name }}"

    # Networks
    # Type: string
    delugevpn_role_docker_networks_alias: "{{ delugevpn_name }}"

    # Type: list
    delugevpn_role_docker_networks_default: []

    # Type: list
    delugevpn_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    delugevpn_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    delugevpn_role_docker_state: started

    # Sysctls
    # Type: dict
    delugevpn_role_docker_sysctls: 
      net.ipv4.conf.all.src_valid_mark: "1"

    # Privileged
    # Type: bool (true/false)
    delugevpn_role_docker_privileged: true

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    delugevpn_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    delugevpn_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    delugevpn_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    delugevpn_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    delugevpn_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    delugevpn_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    delugevpn_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    delugevpn_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    delugevpn_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    delugevpn_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    delugevpn_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    delugevpn_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    delugevpn_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    delugevpn_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    delugevpn_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    delugevpn_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    delugevpn_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        delugevpn_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "delugevpn2.{{ user.domain }}"
          - "delugevpn.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        delugevpn_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'delugevpn2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

