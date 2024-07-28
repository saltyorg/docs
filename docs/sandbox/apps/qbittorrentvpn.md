# qBittorrentvpn

## What is it?

[qbittorrentvpn](https://github.com/binhex/arch-qbittorrentvpn) is a qbittorrent container which includes OpenVPN and WireGuard to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down. It also includes Privoxy to allow unfiltered access to index sites.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:octicons-link-16: Docs](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/binhex/arch-qbittorrentvpn){: .header-icons }|

### 1. Installation

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

    ``` shell

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

    ``` shell

    sb install sandbox-qbittorrentvpn

    ```
    While the above command runs, go to this directory `/opt/qbittorrentvpn/wireguard` (Use FTP file manager like WinSCP)
    if you don't see this directory wait for few seconds, while the previous command creates this.

    Now copy & paste your `wg0.conf' file (Refer Step 05) in this directory & Wait for the command line to complete.
    If everything went well, you should see `Playbook /opt/sandbox/sandbox.yml executed successfully.`

### 2. URL

- To access qbittorrentvpn, visit `https://qbittorrentvpn._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation: qBittorrentvpn Docs](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons }
