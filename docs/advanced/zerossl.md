# ZeroSSL

In order to utilize ZeroSSL with Traefik you will need to create an account with them and generate "EAB Credentials for ACME Clients" in the developer section of their control panel.

Once you have create and saved the credentials you need to create a configuration file for Traefik in `/opt/traefik` and call it `zerossl.yml`

Example using cloudflare:

``` yaml

certificatesResolvers:
  zerossl:
    acme:
      caServer: https://acme.zerossl.com/v2/DV90
      email: zerossl@example.com
      storage: zerossl.json
      dnsChallenge:
        provider: cloudflare
        resolvers:
          - "1.1.1.1:53"
          - "1.0.0.1:53"
      eab:
        kid: abc123xyz
        hmacEncoded: abc123xzy

```

In order to use this new certificate resolver in a container or globally you will have to override the following using the [inventory](../saltbox/inventory/index.md) system.

Globally:

``` yaml

traefik_default_certresolver: "zerossl"

```

Specific Role (Plex):

``` yaml

plex_traefik_certresolver: "zerossl"

```

While it is possible to use other DNS challenge providers that is currently outside of the scope of this guide.
