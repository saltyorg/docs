# TransmissionVPN

# **NOT INTEGRATED - MAKE SANDBOX REQUEST IF NEEDED**
## What is it?

[TransmissionVPN](https://transmissionbt.com/){: target=_blank rel="noopener noreferrer" } is a VPN version of [Transmission](../../community/apps/transmission.md) with OpenVPN to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down.

[Transmission](https://transmissionbt.com/){: target=_blank rel="noopener noreferrer" } is a fast, easy, and free BitTorrent client.


## Project Information

- [:material-home: Transmission ](https://transmissionbt.com/){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://github.com/transmission/transmission/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/transmission/transmission){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/haugene/transmission-openvpn){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-transmissionvpn

```

### 2. URL

- To access TransmissionVPN, visit `https://transmissionvpn._yourdomain.com_`

### 3. Setup

- Edit the TransmissionVPN settings in the TransmissionVPN section in [community `settings.yml`:](../../community/settings.md) as shown below.

   ``` { .yaml }
    transmissionvpn:
      vpn_endpoint: netherlands.ovpn
      vpn_user: your_vpn_username
      vpn_pass: your_vpn_password
      vpn_prov: pia
   ```

- Follow instructions for parent role [Transmission](../../community/apps/transmission.md)

- [:octicons-link-16: Documentation](https://github.com/transmission/transmission/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
