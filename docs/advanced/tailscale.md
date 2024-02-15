# Tailscale

Saltbox can integrate its Traefik implementation with [Tailscale](https://tailscale.com) when you have setup Tailscale on the host.

!!! note
    Tailscale installation and setup on the server is a prerequisite and outside of the scope of this document. This document assumes you are familiar with Tailscale and have already deployed it on your server.

Saltbox can configure Traefik to listen on the server's Tailscale interface for specific roles. Configuration is as follows.

```yaml
traefik_tailscale_enabled: true # (1)!
traefik_traefik_tailscale_enabled: true # (2)!
netdata_traefik_tailscale_enabled: true # (3)!
```

  1. Global toggle for Tailscale entrypoint creation
  2. The toggle for the Traefik dashboard to listen on the Tailscale interface.
  3. The toggle for a specific role, in this case `netdata`, to listen on the Tailscale interface.

The following custom overrides are available as needed.

```yaml
traefik_tailscale_bind_ip: "" # (1)!
traefik_tailscale_bind_ipv6: "" # (2)!
```

  1. Set to override the IPv4 LAN IP port binding when server is not connected directly to the Internet or the WAN IP if it doesn't lookup the correct one.
  2. Set to override the IPv6 LAN IP port binding when server is not connected directly to the Internet or the WAN IP if it doesn't lookup the correct one.
