# Cloudflared

## What is it?

[Cloudflared] is a lightweight daemon and command-line tool developed by Cloudflare that plays a crucial role in connecting your infrastructure to Cloudflare's global network, enabling services like Cloudflare Tunnel. It allows for secure, outbound-only connections from your origin server to Cloudflare's edge network, facilitating remote access to services or private applications without exposing them directly to the internet.

Also, Cloudflared does not have a web interface, so you will need to use the cloudflared Zero Trust page to interact with it.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://developers.cloudflare.com/cloudflare-one/){: .header-icons } | [:octicons-link-16: Docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/cloudflare/cloudflared){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/cloudflare/cloudflared){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-cloudflared

```

### 2. Setup

Cloudflared requires a Cloudflated account, The only configuration that is required for Cloudflared role to create the tunnel is to provide it with a token in the settings file, Follow steps below to get this token

Sgn into your cloudflare account, Select Zero Trust

Select Network > Tunnels > Create a tunnel

Select Cloudflared > Name the tunnel > Save tunnel

Choose the environement > Select Docker > copy the token out of the auto generated docker run line

Enter this token value into the Sandbox settings file under Cloudflared:Token

After you have run the sandbox installation command you can check the status of the tunnel on the Cloudflare Zero Trust page that you got the token from, it shoudl list as healthy

From here you can create public hostnames to pass external requests to the internal containers via the tunnel

- [:octicons-link-16: Documentation: MQTT Docs](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide){: .header-icons }
