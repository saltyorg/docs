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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->