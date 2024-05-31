---
hide:
  - tags
tags:
  - VPN
  - server
---

# Wireguard

## What is it?

[Wireguard](https://wireguard.com) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography.

The Wireguard server is deployed using the [WG-Easy](https://github.com/WeeJeWel/wg-easy) image with a simple Web UI for management.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Wireguard](https://www.wireguard.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/WeeJeWel/wg-easy){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/wg-easy/wg-easy){: .header-icons } | [:material-docker: Docker:](https://ghcr.io/wg-easy/wg-easy){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-wireguard

```

### 2. URL

- To access Wireguard, visit `https://wireguard._yourdomain.com_`

The password provisioned is your Saltbox password.

### 3. Setup

- Use the Web UI to configure your clients.

- [:octicons-link-16: Documentation: Wireguard Docs](https://github.com/wg-easy/wg-easy){: .header-icons }
