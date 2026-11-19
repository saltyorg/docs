---
hide:
  - tags
tags:
  - cloudflare
saltbox_automation:
  project_description:
    name: "Cloudflare"
    summary: "TODO: Add description"
    link: "https://cloudflare.com"
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Cloudflare

## Overview

[Cloudflare](https://cloudflare.com) is TODO: Add description

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install cloudflare
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        cloudflare_server_hostname_enabled: "custom_value"
        ```

=== "DNS"

    ??? variable string "`cloudflare_server_hostname_enabled`"

        ```yaml
        # Manages an unproxied hostname for the server ("saltbox", "mediabox" or "feederbox" subdomain)
        # pointing at its public IP addresses, for use in place of IP addresses (for example in rclone remotes)
        # When disabled, the hostname is not created and its existing A and AAAA records are removed
        # Defaults to disabled when DNS proxying is enabled, since enabling it exposes the server's IP addresses
        # Type: string
        cloudflare_server_hostname_enabled: "{{ not dns_proxied }}"
        ```

=== "Global Override Options"

    ??? variable bool "`cloudflare_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        cloudflare_role_dns_enabled: true
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
