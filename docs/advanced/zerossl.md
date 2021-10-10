# ZeroSSL

In order to utilize ZeroSSL with Traefik you will need to create an account with them and generate "EAB Credentials for ACME Clients" in the developer section of their control panel.

To enable this new certificate resolver in a container or globally you will have to override the following using the [inventory](../saltbox/inventory/index.md) system. Current implementation assumes that you have cloudflare credentials entered as it will use DNS validation. Will add more flexibility later if the need should arise.

Globally:

``` yaml

traefik_zerossl_kid: ""
traefik_zerossl_hmacencoded: ""
traefik_default_certresolver: "zerossl"

```

Specific Role (Plex):

``` yaml

traefik_zerossl_kid: ""
traefik_zerossl_hmacencoded: ""
plex_traefik_certresolver: "zerossl"

```

Enter the credentials you saved from the ZeroSSL control panel.
