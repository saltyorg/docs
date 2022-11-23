# AdGuard Home

## What is it?

[AdGuard Home](https://hub.docker.com/r/adguard/adguardhome){: target=_blank rel="noopener noreferrer" } is a network-wide, open source software for blocking ads & tracking and for gaining control over all traffic in your home network. After you set it up, it'll cover ALL devices in your home Wi-Fi network, and you won't need any client-side software for that. At the same time, it provides a user-friendly web interface that allows you to easily manage the traffic, even from a mobile device.

There are some concerns with the security of running a DNS server remotely so just be aware of this if you choose to run it on a public network.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://adguard.com/en/adguard-home/overview.html){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://kb.adguard.com/en/home/overview){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/AdguardTeam/AdGuardHome){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/adguard/adguardhome){: .header-icons target=_blank rel="noopener noreferrer" }|

!!! info
    AdGuard Home is a latency sensitive DNS server, so it's discouraged to use it when your server is far away from you.

### 1. Installation

``` shell

sb install sandbox-adguardhome

```

### 2. URL

- To access AdGuard Home dashboard, visit `https://adguardhome._yourdomain.com_`

### 3. Usage

- Make sure you have an application that supports DNS over HTTPS, e.g. [Intra for Android](https://play.google.com/store/apps/details?id=app.intra){: target=_blank rel="noopener noreferrer" } or [DNSCloak for iOS](https://apps.apple.com/us/app/dnscloak-secure-dns-client/id1452162351){: target=_blank rel="noopener noreferrer" }
- Connect to AdGuard Home with one of the above applications using `https://adguardhome._yourdomain.com/dns-query`
