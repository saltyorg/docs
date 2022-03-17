Setup instructions are separated based on the DNS Provider you use. 


# Cloudflare

Saltbox will automatically add subdomain on Cloudflare and point it to the correct IP address. 

_Note 1: Make sure the Cloudflare API Key is filled in [[settings.yml|Install: Settings]]) and the e-mail address matches the one you have in your account profile._ 

_Note 2: There may be some subdomains that you have to add in yourself if Saltbox doesn’t so it for you, such as the Saltbox type ones (eg `saltbox`, `feederbox`, `mediabox`)._ 

# Other Domain Hosting Sites

## Saltbox Install Type

### Allows Wildcards

You don't need to do anything.

### Does Not Allow Wildcards

You will need to add the subdomain via your domain's DNS provider's website.

## Mediabox / Feederbox Install Type

You will need to add the subdomain via your domain's DNS provider's website.

Make sure you use the correct IP address (Mediabox IP or Feederbox IP).
