---
hide:
  - tags
tags:
  - tailscale
---

# Tailscale

Saltbox can serve selected apps through [Tailscale](https://tailscale.com) using Traefik. You continue to use each app's normal HTTPS hostname, such as `https://netdata.example.com`, while connecting through the server's Tailscale address.

Enabling Tailscale for an app moves its standard Traefik routes to listeners on the Tailscale address. The public and LAN listeners stop serving those routes. Other apps keep their existing routes. The app's certificates and authentication settings still apply.

This controls access through Traefik. It does not restrict ports that an app publishes separately, such as a media server's direct streaming port.

## Before you start

- Install and connect Tailscale on the Saltbox host using the [Tailscale Linux instructions](https://tailscale.com/docs/install/linux). Saltbox does not install Tailscale or join your tailnet for you.
- Connect your client device to Tailscale and allow it to reach the server's web ports in your tailnet's access policy. The default ports are TCP 80 and 443.
- Configure DNS validation for Traefik-managed certificates if the app's public DNS points to a Tailscale address. If you supply certificates yourself, they must cover the app hostname. See [DNS and HTTPS](#dns-and-https).

With Tailscale mode enabled, Traefik setup runs [`tailscale ip -4`](https://tailscale.com/docs/reference/tailscale-cli#ip) to discover the host's Tailscale IPv4 address. Run the same command on the Saltbox host to check it:

```shell
tailscale ip -4
```

Saltbox uses IPv4 by default. IPv6 publishing is optional and follows `dns.ipv6` in [adv_settings.yml](../reference/accounts.md#options-in-adv_settingsyml), which defaults to `no`. When enabled, Saltbox also queries the Tailscale IPv6 address:

```shell
tailscale ip -6
```

Saltbox only queries and requires the Tailscale IPv6 address when IPv6 is enabled. You do not need to enable IPv6 for this integration.

Tailscale must run on the host so Docker can bind to its addresses. A Tailscale installation confined to another container or using only userspace proxying does not provide the host bindings this integration needs.

## Configure access

Add the following overrides to your [inventory](../saltbox/inventory/index.md#overriding-variables) at `/srv/git/saltbox/inventories/host_vars/localhost.yml`. You can open it with:

```shell
sb edit inventory
```

This example enables the Tailscale listeners and moves the Traefik dashboard and Netdata onto them:

```yaml
traefik_tailscale_enabled: true
traefik_traefik_tailscale_enabled: true
netdata_traefik_tailscale_enabled: true
```

All three switches default to `false`. Save the changes, configure any required [bind overrides](#public-and-lan-bind-addresses), then [apply the configuration](#apply-the-configuration).

### `traefik_tailscale_enabled`

Setting this to `true` creates Traefik's `tailscale-web` and `tailscale-websecure` entrypoints. An entrypoint is a listener that receives requests for the apps assigned to it. Saltbox discovers the host's Tailscale addresses and publishes separate Docker port bindings for normal and Tailscale traffic.

With the default web ports, the IPv4 bindings are:

| Host address and port | Traefik container port | Entrypoint |
| --- | --- | --- |
| Public or LAN IPv4 address, TCP 80 | 80 | `web` |
| Public or LAN IPv4 address, TCP 443 | 443 | `websecure` |
| Tailscale IPv4 address, TCP 80 | 81 | `tailscale-web` |
| Tailscale IPv4 address, TCP 443 | 444 | `tailscale-websecure` |

Clients still connect to ports 80 and 443. Ports 81 and 444 are internal to the Traefik container. The port configuration also publishes UDP 443 to the corresponding HTTPS container ports. When `dns.ipv6` is `yes`, Saltbox adds equivalent bindings for IPv6 addresses.

This switch alone does not move any app onto the Tailscale entrypoints. Enable each app separately using its own switch below.

Keep the global switch enabled while any app uses Tailscale. If an app requests Tailscale DNS while the global switch is disabled, Saltbox stops the deployment before changing that app's DNS records.

Setting it to `false` removes the Tailscale entrypoints and restores Traefik's normal Docker port bindings when you redeploy Traefik. Those bindings use all host addresses by default. First return any affected apps to their normal entrypoints as described under [Disable the integration](#disable-the-integration).

### `traefik_traefik_tailscale_enabled`

With the global switch enabled, setting this to `true` moves the Traefik dashboard's HTTP and HTTPS routes to the Tailscale entrypoints. It also moves the metrics routes if Traefik metrics are enabled. Their hostnames and authentication settings stay the same.

Setting it to `false` returns these routes to `web` and `websecure`. Where Saltbox manages DNS, the dashboard and metrics records also follow the selected mode. See [DNS and HTTPS](#dns-and-https). Redeploy Traefik after changing this value.

### `netdata_traefik_tailscale_enabled`

With the global switch enabled, setting this to `true` moves Netdata's standard HTTP and HTTPS routes to the Tailscale entrypoints. Visit the same Netdata hostname from a client with tailnet access. Netdata's configured authentication still applies.

Setting it to `false` returns Netdata's routes to `web` and `websecure`. Redeploy Netdata after changing this value. Where Saltbox manages DNS, this switch also changes which addresses it uses for Netdata's records. See [DNS and HTTPS](#dns-and-https).

### Other apps and instances

Use the same `_traefik_tailscale_enabled` suffix for other apps. The [inventory guide explains role and instance overrides](../saltbox/inventory/index.md#override-scope). For example, this inventory override selects Tailscale for all Sonarr instances:

```yaml
sonarr_role_traefik_tailscale_enabled: true
```

An instance override such as `sonarr2_traefik_tailscale_enabled` takes precedence over the role setting. Saltbox uses that instance's setting for both Traefik routing and managed DNS.

For example, if you have a `sonarr2` instance, these [inventory overrides](../saltbox/inventory/index.md#override-scope) make only that instance use Tailscale:

```yaml
sonarr_role_traefik_tailscale_enabled: false
sonarr2_traefik_tailscale_enabled: true
```

After running `sb install sonarr`, Sonarr2's routes use the Tailscale entrypoints and its managed DNS records point to the Tailscale addresses. Other Sonarr instances use the normal routes and DNS settings unless they have their own overrides.

The Netdata and dashboard examples above use the default instance names. Their role equivalents are `netdata_role_traefik_tailscale_enabled` and `traefik_role_traefik_tailscale_enabled`.

## Public and LAN bind addresses

When Tailscale mode is enabled, Saltbox binds the normal `web` and `websecure` entrypoints to the detected public IPv4 address. It also uses the detected public IPv6 address if `dns.ipv6` is enabled. On a server behind a router, the public IPv4 address usually belongs to the router. Set the IPv4 bind override to the Saltbox host's LAN address before redeploying Traefik.

These [inventory overrides](../saltbox/inventory/index.md#overriding-variables) select the addresses for the normal listeners. Saltbox gets the Tailscale listener addresses from Tailscale itself.

| Variable | If omitted | Effect when set |
| --- | --- | --- |
| `traefik_tailscale_bind_ip` | Uses the detected public IPv4 address. | Binds normal HTTP and HTTPS traffic to the specified host IPv4 address. Use the host's LAN address when it is behind a router. |
| `traefik_tailscale_bind_ipv6` | Uses the detected public IPv6 address only when `dns.ipv6` is enabled. | Overrides that IPv6 binding. Enter a host IPv6 address without square brackets. This variable has no effect when `dns.ipv6` is `no`. |

For example, if the Saltbox host's LAN address is `192.168.1.10`, add this to your [inventory](../saltbox/inventory/index.md#overriding-variables):

```yaml
traefik_tailscale_bind_ip: "192.168.1.10"
```

Use an address assigned to the host. You can list those addresses with `ip -brief address`. Do not use the router's address, the host's Tailscale address, or an all-address binding such as `0.0.0.0` or `::` for these overrides. An all-address binding overlaps the separate Tailscale bindings on the same ports.

Leave `traefik_tailscale_bind_ipv6` unset for an IPv4-only setup. IPv6 bindings, including the Tailscale IPv6 bindings, are only published when `dns.ipv6` is enabled in [adv_settings.yml](../reference/accounts.md#options-in-adv_settingsyml). Setting the bind override alone does not enable them.

Omit overrides you do not need. For an enabled binding, an empty string causes port validation to fail. Removing an override restores the detected address on the next Traefik deployment. Both overrides only affect port bindings while `traefik_tailscale_enabled` is `true`.

## Apply the configuration

After saving the [inventory changes](../saltbox/inventory/index.md#overriding-variables), deploy Traefik to create the listeners and update its dashboard routes:

```shell
sb install traefik
```

Then deploy each app whose Tailscale setting changed. For the Netdata example:

```shell
sb install netdata
```

The app deployment updates its Traefik routes and managed DNS records. Redeploying only Traefik does not update another app's container labels.

For later changes, redeploy Traefik after changing its global switch, dashboard switch, or bind addresses. Redeploy the affected app after changing its app switch. For multiple instances, run the base role's tag, such as `sb install sonarr`, as described in the [multiple-instance guide](../reference/multiple-instances.md).

## DNS and HTTPS

When Saltbox manages an app's Cloudflare records and that app uses Tailscale, the record types follow the DNS settings in [adv_settings.yml](../reference/accounts.md#options-in-adv_settingsyml):

| Setting | Default | Managed DNS behavior for a Tailscale app |
| --- | --- | --- |
| `dns.ipv4` | `yes` | When enabled, writes the Tailscale IPv4 address to the A record. |
| `dns.ipv6` | `no` | When enabled, writes the Tailscale IPv6 address to the AAAA record. When disabled, skips AAAA creation and removes an existing AAAA record during managed DNS updates. |

The default configuration uses an A record and IPv4 bindings. It does not publish IPv6 bindings or create an AAAA record.

Saltbox sets these records to **DNS only**, even if Cloudflare proxying is otherwise enabled. The client connects to the Tailscale address directly. Returning an app's switch to `false` makes its DNS tasks use the normal addresses and configured proxy setting again.

Redeploying the app also updates existing managed records when you change its Tailscale setting. This includes records that previously pointed to a public address with Cloudflare proxying disabled.

If you manage DNS yourself, configure the app's hostname to resolve to the server's Tailscale address. You can use public DNS records or a DNS server available to your tailnet clients. Remove or correct any old A or AAAA records that direct clients to an address where the app no longer listens.

Continue to use the app's configured hostname, such as `https://netdata.example.com`. Traefik uses that hostname to select the app. A bare Tailscale IP or the server's MagicDNS name does not match the app's default route. [MagicDNS](https://tailscale.com/docs/features/magicdns) provides device names. It does not create records for your app subdomains.

Tailscale mode keeps Traefik's existing certificate configuration. If the app's public DNS records point to Tailscale addresses, public certificate authorities cannot reach it for HTTP-01 validation on port 80. Use DNS-01 for automatically issued certificates, or supply a certificate valid for the app hostname. DNS-01 can issue certificates for servers without public web access. See the [Traefik certificate settings](../reference/accounts.md#options-in-adv_settingsyml) and [Let's Encrypt challenge types](https://letsencrypt.org/docs/challenge-types/).

## Verify access

From a client connected to your tailnet, check the app's A record for the default IPv4 configuration. Replace `netdata.example.com` with your configured hostname:

```shell
dig +short netdata.example.com A
```

It should return the server's Tailscale IPv4 address shown by `tailscale ip -4` on the server.

If you enabled `dns.ipv6`, also check the AAAA record:

```shell
dig +short netdata.example.com AAAA
```

With IPv6 enabled, this should return the Tailscale IPv6 address shown by `tailscale ip -6` on the server. With IPv6 disabled, the app should have no AAAA record directing clients to an IPv6 listener. After changing DNS, cached answers can persist until their TTL expires.

Open `https://netdata.example.com` in a browser. A redirect to your configured login page is expected if the app uses single sign-on. Tailscale does not bypass that login.

If access fails:

- For a connection timeout, check that both devices are connected to Tailscale, that your tailnet policy allows the web ports, and that DNS returns the Tailscale address.
- For a Traefik 404, check the app hostname, the global switch, and the app switch. Confirm that you redeployed both Traefik and the app after enabling the integration.
- For a certificate error, check the hostname and Traefik's certificate configuration. Existing certificates can hide an HTTP-01 problem until renewal.
- For a Docker port-binding error during deployment, check that each bind override contains a nonempty address assigned to the host.

## Disable the integration

To return an app to its normal public or LAN route, set its switch to `false` in the [inventory](../saltbox/inventory/index.md#overriding-variables) and redeploy that app. For Netdata:

```yaml
netdata_traefik_tailscale_enabled: false
```

```shell
sb install netdata
```

Check that its DNS records point to the normal address again. If you manage DNS manually, restore those records yourself. This restores the normal Traefik route, so the app can become publicly accessible if your network permits it.

To disable the entire integration, first return every app and the dashboard to their normal routes. Set their switches to `false` and redeploy them while the global switch is still enabled. Then set `traefik_tailscale_enabled: false` in the [inventory](../saltbox/inventory/index.md#overriding-variables) and run `sb install traefik` again.

Turning off only the global switch leaves any app still configured for Tailscale pointing at entrypoints that no longer exist.

Disabling this integration does not stop Tailscale on the host. Traefik's normal bindings may still accept traffic sent to the host's Tailscale address.
