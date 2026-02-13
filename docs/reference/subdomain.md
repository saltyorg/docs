---
hide:
  - tags
tags:
  - subdomain
---

# Adding a Subdomain

Setup instructions are separated based on the DNS Provider you use and the type of install.

# Cloudflare

Saltbox will automatically add the subdomain on Cloudflare and point it to the correct IP address.

_Note 1: Make sure the Cloudflare API Key is filled in [settings.yml](accounts.md) and the e-mail address matches the one you have in your Cloudflare account profile._

_Note 2: There may be some subdomains that you have to add in yourself if Saltbox doesn’t so it for you, such as the Saltbox type ones (eg `saltbox`, `feederbox`, `mediabox`)._

# Other Domain Hosting Sites

## For the Saltbox Install Type

### If your DNS provider allows wildcards

You don't need to do anything.

### If your DNS provider DOES NOT allow wildcards

You will need to add the subdomain via your domain's DNS provider's website.

## For the Mediabox / Feederbox Install Type

You will need to add the subdomain via your domain's DNS provider's website.

Make sure you use the correct IP address (Mediabox IP or Feederbox IP).
