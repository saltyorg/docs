---
hide:
  - tags
tags:
  - cloudflare
---

# Cloudflare

---

## API request not authenticated

If you get this error during SB Install:

```text
fatal: [localhost]: FAILED! => {"changed": false, "msg": "API request not authenticated; Status: 403; Method: GET: Call: /zones?name=; Error details: code: 9103, error: Unknown X-Auth-Key or X-Auth-Email; "}
```

For scoped-token authentication, make sure:

- `cloudflare.scoped_token` is configured without `cloudflare.api` or `cloudflare.email`.
- The token includes the exact section and permission combinations in the [Cloudflare credential instructions](../reference/domain.md#get-cloudflare-credentials) and is scoped to the zone containing your configured domain.
- The token is active and has not expired.

For the preferred Global API Key authentication, make sure the account email and Global API Key in [accounts.yml](../reference/accounts.md) are both configured and belong to the account managing the domain.

## Configuration Rule quota

Saltbox attempts to maintain a Cloudflare Configuration Rule for HTTP certificate challenges. When DNS certificate validation is active, this rule is optional. A full rule quota or another rule-management error is reported as a warning and the installation continues.

When `traefik.cert.http_validation` is explicitly enabled, the rule is required for HTTP-01 challenges. Saltbox stops the installation if Cloudflare does not create and return the rule successfully.

## Nested subdomain proxying

Free Cloudflare accounts cannot proxy nested records such as `app.test-a.example.com`. Saltbox rejects a nested record before changing Cloudflare when proxying is requested and `cloudflare_allow_nested_proxy` is false.

Nested DNS-only records are supported. Set `cloudflare_allow_nested_proxy: true` only when the Cloudflare zone's plan supports proxied nested subdomains.

## TLD domain not supported

If you get this error during SB Install:

```text
fatal: [localhost]: FAILED! => {"changed": false, "msg": "API request not authenticated; Status: 403; Method: POST: Call: /zones/BINGBANGBOING/dns_records"}
```

It's probably due to using a top-level domain that isn't supported by the Cloudflare API. Refer to [this page](https://support.cloudflare.com/hc/en-us/articles/360020296512-DNS-Troubleshooting-FAQ#h_84167303211544035341531).

As of 2022/11/03:  "DNS API cannot be used for domains with .cf, .ga, .gq, .ml, or .tk TLDs."
