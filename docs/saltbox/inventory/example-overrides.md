---
show:
  - footer.previous
hide:
  - tags
tags:
  - customize
  - domain
  - inventory
  - override
  - pin
  - root
  - specify
  - subdomain
  - version
---

# Example Overrides

Recommended or frequently requested configuration patterns.

## Tags

```yaml
##### Enabling different media servers, downloaders and indexers #####
media_servers_enabled: ["emby"]
download_clients_enabled: ["deluge", "nzbget"]
download_indexers_enabled: ["prowlarr"]
```

```yaml
#### Customize the saltbox tag (sb install saltbox) - No sandbox roles
saltbox_roles: ["media_server", "download_clients", "download_indexers", "autoscan", "tautulli", "seerr", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "glances", "btop"]
```

```yaml
#### Customize the mediabox tag (sb install mediabox) - No sandbox roles
mediabox_roles: ["media_server", "autoscan", "iperf3", "glances", "btop"]
```

```yaml
#### Customize the feeerbox tag (sb install feederbox) - No sandbox roles
feederbox_roles: ["download_clients", "download_indexers", "portainer", "organizr", "sonarr", "radarr", "iperf3", "glances", "btop"]
```

```yaml
#### Customize the sandbox-roles tag (sb install sandbox-roles)
sandbox_roles: ["jellyseerr", "jellystat"]
```

## Routing

=== "Substitution"

    ```yaml
    #### Make Organizr available only at the base domain ####
    organizr_role_web_subdomain: ""
    ```

    ```yaml
    #### Make Seerr available only at `xCUSTOM_SUBDOMAIN_NAMEx.xYOUR_DOMAIN_NAMEx` ####
    seerr_role_web_subdomain: "xCUSTOM_SUBDOMAIN_NAMEx"
    ```

    ```yaml
    #### Make Seerr available at a different base domain ####
    seerr_role_web_domain: "example.com" # (1)!
    ```

    1.  Combined with the above subdomain override, this sets all Seerr instances without instance-level domain or subdomain overrides to `xCUSTOM_SUBDOMAIN_NAMEx.example.com`.

        Be aware that multiple instances cannot have the same FQDN.

    ```yaml
    #### Make specified Seerr instance available at a different base domain ####
    seerrxINSTANCE_SUFFIXx_web_domain: "bing.com" # (1)!
    ```

    1. Combined with the above subdomain override, this sets this specific Seerr instance to `xCUSTOM_SUBDOMAIN_NAMEx.bing.com`, always superseding the role-level domain value.

=== "Extension"

    !!! warning ""
        Extra DNS records for the following examples will not be set up by Saltbox. Your options: create them manually, run [DDNS](../../apps/ddns.md) (Cloudflare only), or use a wildcard DNS record.

    ```yaml
    #### Make Organizr available at `organizr.xYOUR_DOMAIN_NAMEx`, `xYOUR_DOMAIN_NAMEx` and `example.com` ####
    organizr_role_web_fqdn_override:
      - "{{ traefik_host }}"
      - "{{ organizr_role_web_domain }}"
      - "example.com"
    ```

    ```yaml
    #### Make specified Seerr instance available at both `seerr.xYOUR_DOMAIN_NAMEx` and `xCUSTOM_SUBDOMAIN_NAMEx.xYOUR_DOMAIN_NAMEx` ####
    seerr_web_fqdn_override:
      - "{{ traefik_host }}"
      - "xCUSTOM_SUBDOMAIN_NAMEx.{{ seerr_role_web_domain }}"
    ```

```yaml
#### Disable Cloudflare proxy per-app ####
xROLE_NAMEx_dns_proxy: false
```

## Docker Common

```yaml
##### Container overrides ####
plex_docker_image_pull: false # (1)!
plex_docker_image_tag: beta # (2)!
```

1. Can be used to version-pin the image to the current container's version (as long as the image is never pulled by other means)

2. Will version-lock if the tag designates a specific version.

```yaml
#### Examples of specified container images: ####
radarr_role_docker_image_tag: nightly
sonarr_role_docker_image_tag: nightly
petio_role_docker_image_tag: nightly
```

```yaml
#### Specify Seerr DNS server - can fix name resolution issue with TMDb ####
seerr_role_docker_dns_servers:
  - 8.8.8.8
  - 8.8.4.4
```

## Role-specific

```yaml
#### Plex Ports for private access ####
#### To avoid port conflicts, do not enable on more than one instance ####
plex_open_main_ports: true
plex_open_local_ports: true
```

```yaml
#### Configure Sonarr xINSTANCE_SUFFIXx/Radarr xINSTANCE_SUFFIXx Instance Name (assumed instances defined as `sonarrxINSTANCE_SUFFIXx` and `radarrxINSTANCE_SUFFIXx`)
sonarrxINSTANCE_SUFFIXx_docker_envs_custom:
  SONARR__APP__INSTANCENAME: "SonarrxINSTANCE_SUFFIXx" # Must start or end with the word Sonarr
radarrxINSTANCE_SUFFIXx_docker_envs_custom:
  RADARR__APP__INSTANCENAME: "RadarrxINSTANCE_SUFFIXx" # Must start or end with the word Radarr
```

```yaml
#### Bandwidth and rate limiting  ####
#### along with multiple env vars ####
transfer_role_docker_envs_custom:
  MAX_UPLOAD_SIZE: "104857546"
  RATE_LIMIT: "60"
```

=== "Bash"

    ```yaml
    #### Add custom aliases to bash shell ####
    #### Note the syntax - a pipe and two space indentation for the contents ####
    shell_bash_bashrc_block_custom: |
      alias sbu='sb update'
      alias sbi='sb install'
      sb-upgrade() { sb install saltbox,sandbox-roles "$@" }
    ```

=== "Zsh"

    ```yaml
    #### Add custom aliases to zsh shell ###
    #### Note the syntax - a pipe and two space indentation for the contents ####
    shell_zsh_zshrc_block_custom: |
      alias sbu='sb update'
      alias sbi='sb install'
      sb-upgrade() { sb install saltbox,sandbox-roles "$@" }
    ```
