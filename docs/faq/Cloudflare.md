
---
IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## API request not authenticated

If you get this error during SB Install:

```
fatal: [localhost]: FAILED! => {"changed": false, "msg": "API request not authenticated; Status: 403; Method: GET: Call: /zones?name=; Error details: code: 9103, error: Unknown X-Auth-Key or X-Auth-Email; "}
```

Make sure:

- The `email` in [settings.yml](../reference/accounts.md) matches the one you have listed for your Cloudflare.com account.

- The `cloudflare_api_key` in  [settings.yml](../reference/accounts.md matches your `domain`'s Cloudflare [Global API Key]().

