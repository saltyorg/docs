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

Make sure:

- The `email` in [settings.yml](../reference/accounts.md) matches the one you have listed for your Cloudflare.com account.

- The `cloudflare_api_key` in  [settings.yml](../reference/accounts.md) matches your `domain`'s Cloudflare Global API Key.

## TLD domain not supported

If you get this error during SB Install:

```text
fatal: [localhost]: FAILED! => {"changed": false, "msg": "API request not authenticated; Status: 403; Method: POST: Call: /zones/BINGBANGBOING/dns_records"}
```

It's probably due to using a top-level domain that isn't supported by the Cloudflare API.  Refer to [this page](https://support.cloudflare.com/hc/en-us/articles/360020296512-DNS-Troubleshooting-FAQ#h_84167303211544035341531).

As of 2022/11/03:  "DNS API cannot be used for domains with .cf, .ga, .gq, .ml, or .tk TLDs."
