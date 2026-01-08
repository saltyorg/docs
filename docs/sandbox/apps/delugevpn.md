---
icon: material/docker
hide:
  - tags
tags:
  - delugevpn
  - download
  - vpn
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url: https://dev.deluge-torrent.org/wiki/UserGuide
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/binhex/arch-delugevpn/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: DelugeVPN
    summary: |
      a VPN version of [Deluge](../../apps/deluge.md) with OpenVPN to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down.
    link: https://deluge-torrent.org/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# DelugeVPN

## Overview

[DelugeVPN](https://deluge-torrent.org/) is a VPN version of [Deluge](../../apps/deluge.md) with OpenVPN to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://dev.deluge-torrent.org/wiki/UserGuide){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/binhex/arch-delugevpn/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-delugevpn
```

## Usage

Visit <https://delugevpn.iYOUR_DOMAIN_NAMEi>.

## Basics

See the parent [Deluge](../../apps/deluge.md) role for app setup.

- Edit the DelugeVPN settings in the delugevpn section in Sandbox `settings.yml` as shown below.

   ```yaml
    delugevpn:
      vpn_endpoint: netherlands.ovpn
      vpn_pass: your_vpn_password
      vpn_prov: pia
      vpn_user: your_vpn_username
      vpn_client: wireguard # 'wireguard' or 'openvpn'
   ```

**For Private Internet Access** <br />

- Add your user name and password
- Change the vpn_endpoint to your chosen server. Note that PIA occasionally changes which servers have port forwarding. The Netherlands server no longer offers port forwarding. See configuration section for more details.

**For other VPN providers** <br />

- Add your user name and password
- Change `vpn_prov` to `custom`
- Leave `vpn_endpoint` as `netherlands.ovpn`
- Follow step 2 below then immediately follow step 3

### Run the DelugeVPN Role

```shell
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

As of July 4, 2020, the PIA servers that allow port forwarding, and DelugeVPN to work properly, are: CA Toronto, CA Montreal, CA Vancouver, Czech Republic, DE Berlin, DE Frankfurt, France, Israel, Romania, Spain, Switzerland, Sweden. Check the PIA website for changes if these servers do not work.

### Tips

- If you run into issues check `settings.yml` modified during pre install setup.
- If your endpoint has spaces you can use single quotes in the settings.yml ex.)   `vpn_endpoint: 'CA Toronto.ovpn'`
- After checking/fixing `settings.yml` execute `sudo rm -rf /opt/delugevpn`
- **WARNING:** this will delete all files and folder in /opt/delugevpn, backup first if you need anything)
- Follow installation steps above again

### For app specific instructions refer to the parent role

- [Deluge](../../apps/deluge.md)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        delugevpn_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `delugevpn_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `delugevpn_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`delugevpn_name`"

        ```yaml
        # Type: string
        delugevpn_name: delugevpn
        ```

=== "Settings"

    ??? variable string "`delugevpn_role_log_level_daemon`"

        ```yaml
        # https://github.com/binhex/arch-delugevpn for options
        # Type: string
        delugevpn_role_log_level_daemon: info
        ```

    ??? variable string "`delugevpn_role_log_level_web`"

        ```yaml
        # Type: string
        delugevpn_role_log_level_web: info
        ```

    ??? variable string "`delugevpn_role_name_servers`"

        ```yaml
        # Type: string
        delugevpn_role_name_servers: "84.200.69.80,1.1.1.1,84.200.70.40,1.0.0.1"
        ```

    ??? variable string "`delugevpn_role_lan_network`"

        ```yaml
        # Type: string
        delugevpn_role_lan_network: "172.19.0.0/16"
        ```

    ??? variable string "`delugevpn_role_vpn_user`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_user: ""
        ```

    ??? variable string "`delugevpn_role_vpn_pass`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_pass: ""
        ```

    ??? variable string "`delugevpn_role_vpn_prov`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_prov: "pia"
        ```

    ??? variable string "`delugevpn_role_vpn_client`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_client: "wireguard"
        ```

=== "Web"

    ??? variable string "`delugevpn_role_web_subdomain`"

        ```yaml
        # Type: string
        delugevpn_role_web_subdomain: "{{ delugevpn_name }}"
        ```

    ??? variable string "`delugevpn_role_web_domain`"

        ```yaml
        # Type: string
        delugevpn_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`delugevpn_role_web_port`"

        ```yaml
        # Type: string
        delugevpn_role_web_port: "8112"
        ```

    ??? variable string "`delugevpn_role_web_url`"

        ```yaml
        # Type: string
        delugevpn_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='delugevpn') + '.' + lookup('role_var', '_web_domain', role='delugevpn')
                                 if (lookup('role_var', '_web_subdomain', role='delugevpn') | length > 0)
                                 else lookup('role_var', '_web_domain', role='delugevpn')) }}"
        ```

=== "DNS"

    ??? variable string "`delugevpn_role_dns_record`"

        ```yaml
        # Type: string
        delugevpn_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='delugevpn') }}"
        ```

    ??? variable string "`delugevpn_role_dns_zone`"

        ```yaml
        # Type: string
        delugevpn_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='delugevpn') }}"
        ```

    ??? variable bool "`delugevpn_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`delugevpn_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`delugevpn_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`delugevpn_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`delugevpn_role_traefik_certresolver`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`delugevpn_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_traefik_enabled: true
        ```

    ??? variable bool "`delugevpn_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_traefik_api_enabled: false
        ```

    ??? variable string "`delugevpn_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`delugevpn_role_docker_container`"

        ```yaml
        # Type: string
        delugevpn_role_docker_container: "{{ delugevpn_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`delugevpn_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_image_pull: true
        ```

    ??? variable string "`delugevpn_role_docker_image_repo`"

        ```yaml
        # Type: string
        delugevpn_role_docker_image_repo: "binhex/arch-delugevpn"
        ```

    ??? variable string "`delugevpn_role_docker_image_tag`"

        ```yaml
        # Type: string
        delugevpn_role_docker_image_tag: "latest"
        ```

    ??? variable string "`delugevpn_role_docker_image`"

        ```yaml
        # Type: string
        delugevpn_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='delugevpn') }}:{{ lookup('role_var', '_docker_image_tag', role='delugevpn') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`delugevpn_role_docker_ports_default`"

        ```yaml
        # Type: list
        delugevpn_role_docker_ports_default:
          - "58112:58112"
          - "58846:58846"
        ```

    ??? variable list "`delugevpn_role_docker_ports_custom`"

        ```yaml
        # Type: list
        delugevpn_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`delugevpn_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`delugevpn_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        delugevpn_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`delugevpn_role_docker_volumes_default`"

        ```yaml
        # Type: list
        delugevpn_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='delugevpn') }}:/config"
          - "/etc/localtime:/etc/localtime:ro"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`delugevpn_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        delugevpn_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`delugevpn_role_docker_hostname`"

        ```yaml
        # Type: string
        delugevpn_role_docker_hostname: "{{ delugevpn_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`delugevpn_role_docker_networks_alias`"

        ```yaml
        # Type: string
        delugevpn_role_docker_networks_alias: "{{ delugevpn_name }}"
        ```

    ??? variable list "`delugevpn_role_docker_networks_default`"

        ```yaml
        # Type: list
        delugevpn_role_docker_networks_default: []
        ```

    ??? variable list "`delugevpn_role_docker_networks_custom`"

        ```yaml
        # Type: list
        delugevpn_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`delugevpn_role_docker_restart_policy`"

        ```yaml
        # Type: string
        delugevpn_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`delugevpn_role_docker_state`"

        ```yaml
        # Type: string
        delugevpn_role_docker_state: started
        ```

    <h5>Sysctls</h5>

    ??? variable dict "`delugevpn_role_docker_sysctls`"

        ```yaml
        # Type: dict
        delugevpn_role_docker_sysctls:
          net.ipv4.conf.all.src_valid_mark: "1"
        ```

    <h5>Privileged</h5>

    ??? variable bool "`delugevpn_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_privileged: true
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`delugevpn_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        delugevpn_role_docker_blkio_weight:
        ```

    ??? variable int "`delugevpn_role_docker_cpu_period`"

        ```yaml
        # Type: int
        delugevpn_role_docker_cpu_period:
        ```

    ??? variable int "`delugevpn_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        delugevpn_role_docker_cpu_quota:
        ```

    ??? variable int "`delugevpn_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        delugevpn_role_docker_cpu_shares:
        ```

    ??? variable string "`delugevpn_role_docker_cpus`"

        ```yaml
        # Type: string
        delugevpn_role_docker_cpus:
        ```

    ??? variable string "`delugevpn_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        delugevpn_role_docker_cpuset_cpus:
        ```

    ??? variable string "`delugevpn_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        delugevpn_role_docker_cpuset_mems:
        ```

    ??? variable string "`delugevpn_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        delugevpn_role_docker_kernel_memory:
        ```

    ??? variable string "`delugevpn_role_docker_memory`"

        ```yaml
        # Type: string
        delugevpn_role_docker_memory:
        ```

    ??? variable string "`delugevpn_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        delugevpn_role_docker_memory_reservation:
        ```

    ??? variable string "`delugevpn_role_docker_memory_swap`"

        ```yaml
        # Type: string
        delugevpn_role_docker_memory_swap:
        ```

    ??? variable int "`delugevpn_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        delugevpn_role_docker_memory_swappiness:
        ```

    ??? variable string "`delugevpn_role_docker_shm_size`"

        ```yaml
        # Type: string
        delugevpn_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`delugevpn_role_docker_cap_drop`"

        ```yaml
        # Type: list
        delugevpn_role_docker_cap_drop:
        ```

    ??? variable string "`delugevpn_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        delugevpn_role_docker_cgroupns_mode:
        ```

    ??? variable list "`delugevpn_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        delugevpn_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`delugevpn_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        delugevpn_role_docker_device_read_bps:
        ```

    ??? variable list "`delugevpn_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        delugevpn_role_docker_device_read_iops:
        ```

    ??? variable list "`delugevpn_role_docker_device_requests`"

        ```yaml
        # Type: list
        delugevpn_role_docker_device_requests:
        ```

    ??? variable list "`delugevpn_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        delugevpn_role_docker_device_write_bps:
        ```

    ??? variable list "`delugevpn_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        delugevpn_role_docker_device_write_iops:
        ```

    ??? variable list "`delugevpn_role_docker_devices`"

        ```yaml
        # Type: list
        delugevpn_role_docker_devices:
        ```

    ??? variable string "`delugevpn_role_docker_devices_default`"

        ```yaml
        # Type: string
        delugevpn_role_docker_devices_default:
        ```

    ??? variable list "`delugevpn_role_docker_groups`"

        ```yaml
        # Type: list
        delugevpn_role_docker_groups:
        ```

    ??? variable list "`delugevpn_role_docker_security_opts`"

        ```yaml
        # Type: list
        delugevpn_role_docker_security_opts:
        ```

    ??? variable string "`delugevpn_role_docker_user`"

        ```yaml
        # Type: string
        delugevpn_role_docker_user:
        ```

    ??? variable string "`delugevpn_role_docker_userns_mode`"

        ```yaml
        # Type: string
        delugevpn_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`delugevpn_role_docker_dns_opts`"

        ```yaml
        # Type: list
        delugevpn_role_docker_dns_opts:
        ```

    ??? variable list "`delugevpn_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        delugevpn_role_docker_dns_search_domains:
        ```

    ??? variable list "`delugevpn_role_docker_dns_servers`"

        ```yaml
        # Type: list
        delugevpn_role_docker_dns_servers:
        ```

    ??? variable string "`delugevpn_role_docker_domainname`"

        ```yaml
        # Type: string
        delugevpn_role_docker_domainname:
        ```

    ??? variable list "`delugevpn_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        delugevpn_role_docker_exposed_ports:
        ```

    ??? variable dict "`delugevpn_role_docker_hosts`"

        ```yaml
        # Type: dict
        delugevpn_role_docker_hosts:
        ```

    ??? variable bool "`delugevpn_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_hosts_use_common:
        ```

    ??? variable string "`delugevpn_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        delugevpn_role_docker_ipc_mode:
        ```

    ??? variable list "`delugevpn_role_docker_links`"

        ```yaml
        # Type: list
        delugevpn_role_docker_links:
        ```

    ??? variable string "`delugevpn_role_docker_network_mode`"

        ```yaml
        # Type: string
        delugevpn_role_docker_network_mode:
        ```

    ??? variable string "`delugevpn_role_docker_pid_mode`"

        ```yaml
        # Type: string
        delugevpn_role_docker_pid_mode:
        ```

    ??? variable string "`delugevpn_role_docker_uts`"

        ```yaml
        # Type: string
        delugevpn_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`delugevpn_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_keep_volumes:
        ```

    ??? variable list "`delugevpn_role_docker_mounts`"

        ```yaml
        # Type: list
        delugevpn_role_docker_mounts:
        ```

    ??? variable dict "`delugevpn_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        delugevpn_role_docker_storage_opts:
        ```

    ??? variable list "`delugevpn_role_docker_tmpfs`"

        ```yaml
        # Type: list
        delugevpn_role_docker_tmpfs:
        ```

    ??? variable string "`delugevpn_role_docker_volume_driver`"

        ```yaml
        # Type: string
        delugevpn_role_docker_volume_driver:
        ```

    ??? variable list "`delugevpn_role_docker_volumes_from`"

        ```yaml
        # Type: list
        delugevpn_role_docker_volumes_from:
        ```

    ??? variable bool "`delugevpn_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_volumes_global:
        ```

    ??? variable string "`delugevpn_role_docker_working_dir`"

        ```yaml
        # Type: string
        delugevpn_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`delugevpn_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_auto_remove:
        ```

    ??? variable bool "`delugevpn_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_cleanup:
        ```

    ??? variable string "`delugevpn_role_docker_force_kill`"

        ```yaml
        # Type: string
        delugevpn_role_docker_force_kill:
        ```

    ??? variable dict "`delugevpn_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        delugevpn_role_docker_healthcheck:
        ```

    ??? variable int "`delugevpn_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        delugevpn_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`delugevpn_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_init:
        ```

    ??? variable string "`delugevpn_role_docker_kill_signal`"

        ```yaml
        # Type: string
        delugevpn_role_docker_kill_signal:
        ```

    ??? variable string "`delugevpn_role_docker_log_driver`"

        ```yaml
        # Type: string
        delugevpn_role_docker_log_driver:
        ```

    ??? variable dict "`delugevpn_role_docker_log_options`"

        ```yaml
        # Type: dict
        delugevpn_role_docker_log_options:
        ```

    ??? variable bool "`delugevpn_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_oom_killer:
        ```

    ??? variable int "`delugevpn_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        delugevpn_role_docker_oom_score_adj:
        ```

    ??? variable bool "`delugevpn_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_output_logs:
        ```

    ??? variable bool "`delugevpn_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_paused:
        ```

    ??? variable bool "`delugevpn_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_recreate:
        ```

    ??? variable int "`delugevpn_role_docker_restart_retries`"

        ```yaml
        # Type: int
        delugevpn_role_docker_restart_retries:
        ```

    ??? variable int "`delugevpn_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        delugevpn_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`delugevpn_role_docker_capabilities`"

        ```yaml
        # Type: list
        delugevpn_role_docker_capabilities:
        ```

    ??? variable string "`delugevpn_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        delugevpn_role_docker_cgroup_parent:
        ```

    ??? variable list "`delugevpn_role_docker_commands`"

        ```yaml
        # Type: list
        delugevpn_role_docker_commands:
        ```

    ??? variable int "`delugevpn_role_docker_create_timeout`"

        ```yaml
        # Type: int
        delugevpn_role_docker_create_timeout:
        ```

    ??? variable string "`delugevpn_role_docker_entrypoint`"

        ```yaml
        # Type: string
        delugevpn_role_docker_entrypoint:
        ```

    ??? variable string "`delugevpn_role_docker_env_file`"

        ```yaml
        # Type: string
        delugevpn_role_docker_env_file:
        ```

    ??? variable dict "`delugevpn_role_docker_labels`"

        ```yaml
        # Type: dict
        delugevpn_role_docker_labels:
        ```

    ??? variable bool "`delugevpn_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_labels_use_common:
        ```

    ??? variable bool "`delugevpn_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_read_only:
        ```

    ??? variable string "`delugevpn_role_docker_runtime`"

        ```yaml
        # Type: string
        delugevpn_role_docker_runtime:
        ```

    ??? variable list "`delugevpn_role_docker_ulimits`"

        ```yaml
        # Type: list
        delugevpn_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`delugevpn_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        delugevpn_role_autoheal_enabled: true
        ```

    ??? variable string "`delugevpn_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        delugevpn_role_depends_on: ""
        ```

    ??? variable string "`delugevpn_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        delugevpn_role_depends_on_delay: "0"
        ```

    ??? variable string "`delugevpn_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        delugevpn_role_depends_on_healthchecks:
        ```

    ??? variable bool "`delugevpn_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        delugevpn_role_diun_enabled: true
        ```

    ??? variable bool "`delugevpn_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        delugevpn_role_dns_enabled: true
        ```

    ??? variable bool "`delugevpn_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        delugevpn_role_docker_controller: true
        ```

    ??? variable string "`delugevpn_role_docker_image_repo`"

        ```yaml
        # Type: string
        delugevpn_role_docker_image_repo:
        ```

    ??? variable string "`delugevpn_role_docker_image_tag`"

        ```yaml
        # Type: string
        delugevpn_role_docker_image_tag:
        ```

    ??? variable bool "`delugevpn_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_docker_volumes_download:
        ```

    ??? variable string "`delugevpn_role_lan_network`"

        ```yaml
        # Type: string
        delugevpn_role_lan_network:
        ```

    ??? variable string "`delugevpn_role_log_level_daemon`"

        ```yaml
        # Type: string
        delugevpn_role_log_level_daemon:
        ```

    ??? variable string "`delugevpn_role_log_level_web`"

        ```yaml
        # Type: string
        delugevpn_role_log_level_web:
        ```

    ??? variable string "`delugevpn_role_name_servers`"

        ```yaml
        # Type: string
        delugevpn_role_name_servers:
        ```

    ??? variable string "`delugevpn_role_paths_location`"

        ```yaml
        # Type: string
        delugevpn_role_paths_location:
        ```

    ??? variable string "`delugevpn_role_themepark_addons`"

        ```yaml
        # Type: string
        delugevpn_role_themepark_addons:
        ```

    ??? variable string "`delugevpn_role_themepark_app`"

        ```yaml
        # Type: string
        delugevpn_role_themepark_app:
        ```

    ??? variable string "`delugevpn_role_themepark_theme`"

        ```yaml
        # Type: string
        delugevpn_role_themepark_theme:
        ```

    ??? variable dict "`delugevpn_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        delugevpn_role_traefik_api_endpoint:
        ```

    ??? variable string "`delugevpn_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_api_middleware:
        ```

    ??? variable string "`delugevpn_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`delugevpn_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        delugevpn_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`delugevpn_role_traefik_certresolver`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_certresolver:
        ```

    ??? variable bool "`delugevpn_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        delugevpn_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`delugevpn_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        delugevpn_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`delugevpn_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        delugevpn_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`delugevpn_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_middleware_http:
        ```

    ??? variable bool "`delugevpn_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`delugevpn_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        delugevpn_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`delugevpn_role_traefik_priority`"

        ```yaml
        # Type: string
        delugevpn_role_traefik_priority:
        ```

    ??? variable bool "`delugevpn_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        delugevpn_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`delugevpn_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        delugevpn_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`delugevpn_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        delugevpn_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`delugevpn_role_vpn_client`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_client:
        ```

    ??? variable string "`delugevpn_role_vpn_pass`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_pass:
        ```

    ??? variable string "`delugevpn_role_vpn_prov`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_prov:
        ```

    ??? variable string "`delugevpn_role_vpn_user`"

        ```yaml
        # Type: string
        delugevpn_role_vpn_user:
        ```

    ??? variable string "`delugevpn_role_web_domain`"

        ```yaml
        # Type: string
        delugevpn_role_web_domain:
        ```

    ??? variable list "`delugevpn_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        delugevpn_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            delugevpn_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "delugevpn2.{{ user.domain }}"
              - "delugevpn.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`delugevpn_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        delugevpn_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            delugevpn_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'delugevpn2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`delugevpn_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        delugevpn_role_web_http_port:
        ```

    ??? variable string "`delugevpn_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        delugevpn_role_web_http_scheme:
        ```

    ??? variable dict "`delugevpn_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        delugevpn_role_web_http_serverstransport:
        ```

    ??? variable string "`delugevpn_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        delugevpn_role_web_scheme:
        ```

    ??? variable dict "`delugevpn_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        delugevpn_role_web_serverstransport:
        ```

    ??? variable string "`delugevpn_role_web_subdomain`"

        ```yaml
        # Type: string
        delugevpn_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->