---
icon: material/docker
status: draft
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url: https://doc.traefik.io/traefik
      type: documentation
    - name: Releases
      url: https://hub.docker.com/_/traefik/tags
      type: docker
    - name: Community
      url: https://community.traefik.io
      type: community
  project_description:
    name: Traefik Proxy
    summary: |
      an open-source, dynamic reverse proxy and load balancer designed for modern, distributed, and microservices architectures.
    link: https://traefik.io/traefik
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Traefik Proxy

## Overview

[Traefik Proxy](https://traefik.io/traefik) is an open-source, dynamic reverse proxy and load balancer designed for modern, distributed, and microservices architectures.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://doc.traefik.io/traefik){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/traefik/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://community.traefik.io){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Saltbox dependency.

```shell
sb install traefik
```

## Usage

Visit <https://dash.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        traefik_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `traefik_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `traefik_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`traefik_name`"

        ```yaml
        # Type: string
        traefik_name: traefik
        ```

=== "Config"

    ??? variable string "`traefik_trusted_ips`"

        ```yaml
        # Type: string
        traefik_trusted_ips: ""
        ```

    ??? variable bool "`traefik_plugin_cloudflarewarp_enabled`"

        ```yaml
        # Type: bool (true/false)
        traefik_plugin_cloudflarewarp_enabled: true
        ```

    ??? variable string "`traefik_file_watch`"

        ```yaml
        # Type: string
        traefik_file_watch: "true"
        ```

    ??? variable string "`traefik_x_robots`"

        ```yaml
        # Type: string
        traefik_x_robots: "none,noarchive,nosnippet,notranslate,noimageindex"
        ```

    ??? variable bool "`traefik_http3`"

        ```yaml
        # HTTP3 can cause issues with some apps
        # Type: bool (true/false)
        traefik_http3: false
        ```

    ??? variable bool "`traefik_tailscale_enabled`"

        ```yaml
        # Type: bool (true/false)
        traefik_tailscale_enabled: false
        ```

    ??? variable string "`traefik_entrypoint_web_port`"

        ```yaml
        # traefik_tailscale_bind_ip: "" # Set to override the WAN IP port binding when server is not connected directly to the Internet.
        # traefik_tailscale_bind_ipv6: "" # Same but IPv6
        # Type: string
        traefik_entrypoint_web_port: "80"
        ```

    ??? variable string "`traefik_entrypoint_web_readtimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_readtimeout: "600"
        ```

    ??? variable string "`traefik_entrypoint_web_writetimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_writetimeout: "0"
        ```

    ??? variable string "`traefik_entrypoint_web_idletimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_idletimeout: "180"
        ```

    ??? variable string "`traefik_entrypoint_web_request_maxheaderbytes`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_request_maxheaderbytes: "1048576"
        ```

    ??? variable string "`traefik_entrypoint_websecure_port`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_port: "443"
        ```

    ??? variable string "`traefik_entrypoint_websecure_readtimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_readtimeout: "600"
        ```

    ??? variable string "`traefik_entrypoint_websecure_writetimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_writetimeout: "0"
        ```

    ??? variable string "`traefik_entrypoint_websecure_idletimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_idletimeout: "180"
        ```

    ??? variable string "`traefik_entrypoint_websecure_request_maxheaderbytes`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_request_maxheaderbytes: "1048576"
        ```

    ??? variable dict "`traefik_entrypoint_custom`"

        ```yaml
        # Type: dict
        traefik_entrypoint_custom: {}
        ```

    ??? variable string "`traefik_dns_resolvers`"

        ```yaml
        # Format is as follows (address can be empty string "" to bind on every interface):
        # Type options are tcp, udp or both.
        # traefik_entrypoint_custom:
        # tcp-entrypoint:
        # address: "IP"
        # port: "81"
        # tls: false
        # type: tcp
        # tcp-and-udp-entrypoint-with-tls:
        # address: "IP"
        # port: "444"
        # tls: true
        # type: both
        # Type: string
        traefik_dns_resolvers: "1.1.1.1:53,1.0.0.1:53"
        ```

    ??? variable bool "`traefik_disable_propagation_check`"

        ```yaml
        # Type: bool (true/false)
        traefik_disable_propagation_check: false
        ```

    ??? variable string "`traefik_enable_http_validation`"

        ```yaml
        # Type: string
        traefik_enable_http_validation: "{{ traefik_http or (traefik.cert.http_validation | bool) }}"
        ```

    ??? variable bool "`traefik_enable_zerossl`"

        ```yaml
        # Type: bool (true/false)
        traefik_enable_zerossl: true
        ```

    ??? variable string "`traefik_crowdsec_ban_filepath`"

        ```yaml
        # Path is internal to the container, so a host path of /opt/traefik/ban.html becomes /etc/traefik/ban.html
        # Type: string
        traefik_crowdsec_ban_filepath: "/etc/traefik/ban.html"
        ```

    ??? variable bool "`traefik_sanitize_path`"

        ```yaml
        # Entrypoint Path Sanitization Settings
        # Type: bool (true/false)
        traefik_sanitize_path: true
        ```

    ??? variable bool "`traefik_encoded_allow_slash`"

        ```yaml
        # Entrypoint Encoded characters settings (applied to all entrypoints)
        # Type: bool (true/false)
        traefik_encoded_allow_slash: true
        ```

    ??? variable bool "`traefik_encoded_allow_backslash`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_backslash: true
        ```

    ??? variable bool "`traefik_encoded_allow_null`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_null: true
        ```

    ??? variable bool "`traefik_encoded_allow_semicolon`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_semicolon: true
        ```

    ??? variable bool "`traefik_encoded_allow_percent`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_percent: true
        ```

    ??? variable bool "`traefik_encoded_allow_question_mark`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_question_mark: true
        ```

    ??? variable bool "`traefik_encoded_allow_hash`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_hash: true
        ```

=== "Templates"

    ??? variable list "`traefik_entrypoint_template`"

        ```yaml
        # Type: list
        traefik_entrypoint_template:
          - "--entrypoints.{{ item.key }}.address={{ item.value.address + ':' + (item.value.port | string) }}"
        ```

    ??? variable list "`traefik_entrypoint_tls_template`"

        ```yaml
        # Type: list
        traefik_entrypoint_tls_template:
          - "--entrypoints.{{ item.key }}.address={{ item.value.address + ':' + (item.value.port | string) }}"
          - "--entrypoints.{{ item.key }}.http.tls.certResolver={{ traefik_default_certresolver }}"
        ```

    ??? variable list "`traefik_entrypoint_http3_template`"

        ```yaml
        # Type: list
        traefik_entrypoint_http3_template:
          - "--entrypoints.{{ item.key }}.http3"
          - "--entrypoints.{{ item.key }}.http3.advertisedport={{ item.value.port }}"
        ```

    ??? variable list "`traefik_entrypoint_ports_tcp_template`"

        ```yaml
        # Type: list
        traefik_entrypoint_ports_tcp_template:
          - "{{ item.value.port }}:{{ item.value.port }}/tcp"
        ```

    ??? variable list "`traefik_entrypoint_ports_udp_template`"

        ```yaml
        # Type: list
        traefik_entrypoint_ports_udp_template:
          - "{{ item.value.port }}:{{ item.value.port }}/udp"
        ```

    ??? variable list "`traefik_entrypoint_ports_both_template`"

        ```yaml
        # Type: list
        traefik_entrypoint_ports_both_template:
          - "{{ item.value.port }}:{{ item.value.port }}/tcp"
          - "{{ item.value.port }}:{{ item.value.port }}/udp"
        ```

    ??? variable list "`traefik_entrypoint_http_settings_template`"

        ```yaml
        # Type: list
        traefik_entrypoint_http_settings_template:
          - "--entrypoints.{{ item.key }}.http.sanitizePath={{ traefik_sanitize_path | string | lower }}"
          - "--entrypoints.{{ item.key }}.http.encodedCharacters.allowEncodedSlash={{ traefik_encoded_allow_slash | string | lower }}"
          - "--entrypoints.{{ item.key }}.http.encodedCharacters.allowEncodedBackSlash={{ traefik_encoded_allow_backslash | string | lower }}"
          - "--entrypoints.{{ item.key }}.http.encodedCharacters.allowEncodedNullCharacter={{ traefik_encoded_allow_null | string | lower }}"
          - "--entrypoints.{{ item.key }}.http.encodedCharacters.allowEncodedSemicolon={{ traefik_encoded_allow_semicolon | string | lower }}"
          - "--entrypoints.{{ item.key }}.http.encodedCharacters.allowEncodedPercent={{ traefik_encoded_allow_percent | string | lower }}"
          - "--entrypoints.{{ item.key }}.http.encodedCharacters.allowEncodedQuestionMark={{ traefik_encoded_allow_question_mark | string | lower }}"
          - "--entrypoints.{{ item.key }}.http.encodedCharacters.allowEncodedHash={{ traefik_encoded_allow_hash | string | lower }}"
        ```

    ??? variable string "`traefik_trusted_ips_template`"

        ```yaml
        # Type: string
        traefik_trusted_ips_template: "{{ traefik_trusted_ips
                                       if (traefik_trusted_ips | length > 0)
                                       else '' }}"
        ```

=== "Lookups"

    ??? variable string "`traefik_zerossl_file_ini`"

        ```yaml
        # Type: string
        traefik_zerossl_file_ini: "{{ server_appdata_path }}/saltbox/zerossl.ini"
        ```

=== "Booleans"

    ??? variable string "`traefik_role_authelia_enabled`"

        ```yaml
        # Type: string
        traefik_role_authelia_enabled: "{{ 'authelia' in traefik_default_sso_middleware }}"
        ```

    ??? variable string "`traefik_role_authentik_enabled`"

        ```yaml
        # Type: string
        traefik_role_authentik_enabled: "{{ 'authentik' in traefik_default_sso_middleware }}"
        ```

    ??? variable string "`traefik_role_metrics_enabled`"

        ```yaml
        # Type: string
        traefik_role_metrics_enabled: "{{ traefik.metrics | bool }}"
        ```

=== "Web"

    ??? variable string "`traefik_role_web_subdomain`"

        ```yaml
        # Type: string
        traefik_role_web_subdomain: "{{ traefik.subdomains.dash }}"
        ```

    ??? variable string "`traefik_role_web_domain`"

        ```yaml
        # Type: string
        traefik_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`traefik_role_metrics_subdomain`"

        ```yaml
        # Type: string
        traefik_role_metrics_subdomain: "{{ traefik.subdomains.metrics }}"
        ```

    ??? variable string "`traefik_role_metrics_domain`"

        ```yaml
        # Type: string
        traefik_role_metrics_domain: "{{ user.domain }}"
        ```

=== "Logging"

    ??? variable string "`traefik_role_log_level`"

        ```yaml
        # Type: string
        traefik_role_log_level: "ERROR"
        ```

    ??? variable bool "`traefik_role_log_file`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_file: true
        ```

    ??? variable string "`traefik_role_log_max_size`"

        ```yaml
        # Type: string
        traefik_role_log_max_size: "10"
        ```

    ??? variable string "`traefik_role_log_max_backups`"

        ```yaml
        # Type: string
        traefik_role_log_max_backups: "3"
        ```

    ??? variable string "`traefik_role_log_max_age`"

        ```yaml
        # Type: string
        traefik_role_log_max_age: "3"
        ```

    ??? variable string "`traefik_role_log_compress`"

        ```yaml
        # Type: string
        traefik_role_log_compress: "true"
        ```

    ??? variable bool "`traefik_role_access_log`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_access_log: true
        ```

    ??? variable int "`traefik_role_access_buffer`"

        ```yaml
        # Type: int
        traefik_role_access_buffer: 100
        ```

=== "DNS"

    ??? variable string "`traefik_role_dns_record`"

        ```yaml
        # Type: string
        traefik_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='traefik') }}"
        ```

    ??? variable string "`traefik_role_dns_zone`"

        ```yaml
        # Type: string
        traefik_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='traefik') }}"
        ```

    ??? variable bool "`traefik_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_dns_proxy: "{{ dns_proxied }}"
        ```

    ??? variable string "`traefik_role_metrics_dns_record`"

        ```yaml
        # Type: string
        traefik_role_metrics_dns_record: "{{ lookup('role_var', '_metrics_subdomain', role='traefik') }}"
        ```

    ??? variable string "`traefik_role_metrics_dns_zone`"

        ```yaml
        # Type: string
        traefik_role_metrics_dns_zone: "{{ lookup('role_var', '_metrics_domain', role='traefik') }}"
        ```

    ??? variable bool "`traefik_role_metrics_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_metrics_dns_proxy: "{{ dns_proxied }}"
        ```

=== "DNS Provider"

    ??? variable dict "`traefik_dns_provider_cloudflare_tmp`"

        ```yaml
        # Type: dict
        traefik_dns_provider_cloudflare_tmp:
          CLOUDFLARE_EMAIL: "{{ cloudflare.email }}"
          CLOUDFLARE_API_KEY: "{{ cloudflare.api }}"
        ```

    ??? variable string "`traefik_dns_provider_cloudflare`"

        ```yaml
        # Type: string
        traefik_dns_provider_cloudflare: "{{ traefik_dns_provider_cloudflare_tmp
                                          if cloudflare_is_enabled
                                          else {} }}"
        ```

    ??? variable dict "`traefik_dns_provider_cloudns`"

        ```yaml
        # Type: dict
        traefik_dns_provider_cloudns:
          CLOUDDNS_CLIENT_ID: "{{ cloudns.client_id }}"
          CLOUDDNS_EMAIL: "{{ cloudns.email }}"
          CLOUDDNS_PASSWORD: "{{ cloudns.password }}"
        ```

    ??? variable dict "`traefik_dns_provider_duckdns`"

        ```yaml
        # Type: dict
        traefik_dns_provider_duckdns:
          DUCKDNS_TOKEN: "{{ duckdns.token }}"
        ```

    ??? variable dict "`traefik_dns_provider_dynu`"

        ```yaml
        # Type: dict
        traefik_dns_provider_dynu:
          DYNU_API_KEY: "{{ dynu.api_key }}"
        ```

    ??? variable dict "`traefik_dns_provider_godaddy`"

        ```yaml
        # Type: dict
        traefik_dns_provider_godaddy:
          GODADDY_API_KEY: "{{ godaddy.api_key }}"
          GODADDY_API_SECRET: "{{ godaddy.api_secret }}"
        ```

    ??? variable dict "`traefik_dns_provider_hetzner`"

        ```yaml
        # Type: dict
        traefik_dns_provider_hetzner:
          HETZNER_API_KEY: "{{ hetzner.api_key }}"
        ```

    ??? variable dict "`traefik_dns_provider_linode`"

        ```yaml
        # Type: dict
        traefik_dns_provider_linode:
          LINODE_TOKEN: "{{ linode.token }}"
        ```

    ??? variable dict "`traefik_dns_provider_namecheap`"

        ```yaml
        # Type: dict
        traefik_dns_provider_namecheap:
          NAMECHEAP_API_USER: "{{ namecheap.api_user }}"
          NAMECHEAP_API_KEY: "{{ namecheap.api_key }}"
        ```

    ??? variable dict "`traefik_dns_provider_namedotcom`"

        ```yaml
        # Type: dict
        traefik_dns_provider_namedotcom:
          NAMECOM_USERNAME: "{{ namedotcom.username }}"
          NAMECOM_API_TOKEN: "{{ namedotcom.api_token }}"
          NAMECOM_SERVER: "{{ namedotcom.server }}"
        ```

    ??? variable dict "`traefik_dns_provider_netcup`"

        ```yaml
        # Type: dict
        traefik_dns_provider_netcup:
          NETCUP_CUSTOMER_NUMBER: "{{ netcup.customer_number }}"
          NETCUP_API_KEY: "{{ netcup.api_key }}"
          NETCUP_API_PASSWORD: "{{ netcup.api_password }}"
        ```

    ??? variable dict "`traefik_dns_provider_porkbun`"

        ```yaml
        # Type: dict
        traefik_dns_provider_porkbun:
          PORKBUN_API_KEY: "{{ porkbun.api_key }}"
          PORKBUN_SECRET_API_KEY: "{{ porkbun.secret_key }}"
        ```

    ??? variable dict "`traefik_dns_provider_powerdns`"

        ```yaml
        # Type: dict
        traefik_dns_provider_powerdns:
          PDNS_API_KEY: "{{ powerdns.api_key }}"
          PDNS_API_URL: "{{ powerdns.api_url }}"
        ```

=== "Traefik"

    ??? variable string "`traefik_traefik_sso_middleware`"

        ```yaml
        # Type: string
        traefik_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`traefik_traefik_certresolver`"

        ```yaml
        # Type: string
        traefik_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`traefik_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        traefik_traefik_enabled: true
        ```

    ??? variable bool "`traefik_traefik_autodetect_enabled`"

        ```yaml
        # Type: bool (true/false)
        traefik_traefik_autodetect_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`traefik_role_docker_container`"

        ```yaml
        # Type: string
        traefik_role_docker_container: "{{ traefik_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`traefik_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_image_pull: true
        ```

    ??? variable string "`traefik_role_docker_image_repo`"

        ```yaml
        # Type: string
        traefik_role_docker_image_repo: "traefik"
        ```

    ??? variable string "`traefik_role_docker_image_tag`"

        ```yaml
        # Type: string
        traefik_role_docker_image_tag: "v3.6"
        ```

    ??? variable string "`traefik_role_docker_image`"

        ```yaml
        # Type: string
        traefik_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='traefik') }}:{{ lookup('role_var', '_docker_image_tag', role='traefik') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`traefik_role_docker_ports_default`"

        ```yaml
        # Type: list
        traefik_role_docker_ports_default:
          - "{{ traefik_entrypoint_web_port }}:{{ traefik_entrypoint_web_port }}/tcp"
          - "{{ traefik_entrypoint_websecure_port }}:{{ traefik_entrypoint_websecure_port }}/tcp"
          - "{{ traefik_entrypoint_websecure_port }}:{{ traefik_entrypoint_websecure_port }}/udp"
        ```

    ??? variable list "`traefik_role_docker_ports_tailscale_ipv4_default`"

        ```yaml
        # Type: list
        traefik_role_docker_ports_tailscale_ipv4_default:
          - "{{ lookup('vars', 'traefik_tailscale_bind_ip', default=ip_address_public) + ':' + traefik_entrypoint_web_port }}:{{ traefik_entrypoint_web_port }}/tcp"
          - "{{ lookup('vars', 'traefik_tailscale_bind_ip', default=ip_address_public) + ':' + traefik_entrypoint_websecure_port }}:{{ traefik_entrypoint_websecure_port }}/tcp"
          - "{{ lookup('vars', 'traefik_tailscale_bind_ip', default=ip_address_public) + ':' + traefik_entrypoint_websecure_port }}:{{ traefik_entrypoint_websecure_port }}/udp"
          - "{{ tailscale_ipv4 + ':' + traefik_entrypoint_web_port }}:81/tcp"
          - "{{ tailscale_ipv4 + ':' + traefik_entrypoint_websecure_port }}:444/tcp"
          - "{{ tailscale_ipv4 + ':' + traefik_entrypoint_websecure_port }}:444/udp"
        ```

    ??? variable list "`traefik_role_docker_ports_tailscale_ipv6_default`"

        ```yaml
        # Type: list
        traefik_role_docker_ports_tailscale_ipv6_default:
          - "{{ '[' + lookup('vars', 'traefik_tailscale_bind_ipv6', default=ipv6_address_public) + ']:' + traefik_entrypoint_web_port }}:{{ traefik_entrypoint_web_port }}/tcp"
          - "{{ '[' + lookup('vars', 'traefik_tailscale_bind_ipv6', default=ipv6_address_public) + ']:' + traefik_entrypoint_websecure_port }}:{{ traefik_entrypoint_websecure_port }}/tcp"
          - "{{ '[' + lookup('vars', 'traefik_tailscale_bind_ipv6', default=ipv6_address_public) + ']:' + traefik_entrypoint_websecure_port }}:{{ traefik_entrypoint_websecure_port }}/udp"
          - "{{ '[' + tailscale_ipv6 + ']:' + traefik_entrypoint_web_port }}:81/tcp"
          - "{{ '[' + tailscale_ipv6 + ']:' + traefik_entrypoint_websecure_port }}:444/tcp"
          - "{{ '[' + tailscale_ipv6 + ']:' + traefik_entrypoint_websecure_port }}:444/udp"
        ```

    ??? variable list "`traefik_role_docker_ports_custom`"

        ```yaml
        # Type: list
        traefik_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`traefik_role_docker_envs_default`"

        ```yaml
        # Type: dict
        traefik_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`traefik_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        traefik_role_docker_envs_custom: {}
        ```

    <h5>Commands</h5>

    ??? variable list "`traefik_role_docker_commands_default`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_default:
          - "--global.sendanonymoususage=false"
          - "--providers.file.directory=/etc/traefik"
          - "--providers.file.watch={{ traefik_file_watch }}"
          - "--providers.docker=true"
          - "--providers.docker.exposedbydefault=false"
          - "--entrypoints.internal.address=:8080"
          - "--entrypoints.internal.http.sanitizePath={{ traefik_sanitize_path | string | lower }}"
          - "--entrypoints.internal.http.encodedCharacters.allowEncodedSlash={{ traefik_encoded_allow_slash | string | lower }}"
          - "--entrypoints.internal.http.encodedCharacters.allowEncodedBackSlash={{ traefik_encoded_allow_backslash | string | lower }}"
          - "--entrypoints.internal.http.encodedCharacters.allowEncodedNullCharacter={{ traefik_encoded_allow_null | string | lower }}"
          - "--entrypoints.internal.http.encodedCharacters.allowEncodedSemicolon={{ traefik_encoded_allow_semicolon | string | lower }}"
          - "--entrypoints.internal.http.encodedCharacters.allowEncodedPercent={{ traefik_encoded_allow_percent | string | lower }}"
          - "--entrypoints.internal.http.encodedCharacters.allowEncodedQuestionMark={{ traefik_encoded_allow_question_mark | string | lower }}"
          - "--entrypoints.internal.http.encodedCharacters.allowEncodedHash={{ traefik_encoded_allow_hash | string | lower }}"
          - "--entrypoints.web.address=:{{ traefik_entrypoint_web_port }}"
          - "{{ ('--entrypoints.web.forwardedheaders.trustedIPs=' + traefik_trusted_ips_template) if (traefik_trusted_ips_template | length > 0) else omit }}"
          - "{{ ('--entrypoints.web.proxyprotocol.trustedIPs=' + traefik_trusted_ips_template) if (traefik_trusted_ips_template | length > 0) else omit }}"
          - "--entrypoints.web.transport.respondingTimeouts.readTimeout={{ traefik_entrypoint_web_readtimeout }}"
          - "--entrypoints.web.transport.respondingTimeouts.writeTimeout={{ traefik_entrypoint_web_writetimeout }}"
          - "--entrypoints.web.transport.respondingTimeouts.idleTimeout={{ traefik_entrypoint_web_idletimeout }}"
          - "--entrypoints.web.http.maxheaderbytes={{ traefik_entrypoint_web_request_maxheaderbytes }}"
          - "--entrypoints.web.http.sanitizePath={{ traefik_sanitize_path | string | lower }}"
          - "--entrypoints.web.http.encodedCharacters.allowEncodedSlash={{ traefik_encoded_allow_slash | string | lower }}"
          - "--entrypoints.web.http.encodedCharacters.allowEncodedBackSlash={{ traefik_encoded_allow_backslash | string | lower }}"
          - "--entrypoints.web.http.encodedCharacters.allowEncodedNullCharacter={{ traefik_encoded_allow_null | string | lower }}"
          - "--entrypoints.web.http.encodedCharacters.allowEncodedSemicolon={{ traefik_encoded_allow_semicolon | string | lower }}"
          - "--entrypoints.web.http.encodedCharacters.allowEncodedPercent={{ traefik_encoded_allow_percent | string | lower }}"
          - "--entrypoints.web.http.encodedCharacters.allowEncodedQuestionMark={{ traefik_encoded_allow_question_mark | string | lower }}"
          - "--entrypoints.web.http.encodedCharacters.allowEncodedHash={{ traefik_encoded_allow_hash | string | lower }}"
          - "--entrypoints.websecure.address=:{{ traefik_entrypoint_websecure_port }}"
          - "{{ ('--entrypoints.websecure.forwardedheaders.trustedIPs=' + traefik_trusted_ips_template) if (traefik_trusted_ips_template | length > 0) else omit }}"
          - "{{ ('--entrypoints.websecure.proxyprotocol.trustedIPs=' + traefik_trusted_ips_template) if (traefik_trusted_ips_template | length > 0) else omit }}"
          - "--entrypoints.websecure.transport.respondingTimeouts.readTimeout={{ traefik_entrypoint_websecure_readtimeout }}"
          - "--entrypoints.websecure.transport.respondingTimeouts.writeTimeout={{ traefik_entrypoint_websecure_writetimeout }}"
          - "--entrypoints.websecure.transport.respondingTimeouts.idleTimeout={{ traefik_entrypoint_websecure_idletimeout }}"
          - "--entrypoints.websecure.http.maxheaderbytes={{ traefik_entrypoint_websecure_request_maxheaderbytes }}"
          - "--entrypoints.websecure.http.sanitizePath={{ traefik_sanitize_path | string | lower }}"
          - "--entrypoints.websecure.http.encodedCharacters.allowEncodedSlash={{ traefik_encoded_allow_slash | string | lower }}"
          - "--entrypoints.websecure.http.encodedCharacters.allowEncodedBackSlash={{ traefik_encoded_allow_backslash | string | lower }}"
          - "--entrypoints.websecure.http.encodedCharacters.allowEncodedNullCharacter={{ traefik_encoded_allow_null | string | lower }}"
          - "--entrypoints.websecure.http.encodedCharacters.allowEncodedSemicolon={{ traefik_encoded_allow_semicolon | string | lower }}"
          - "--entrypoints.websecure.http.encodedCharacters.allowEncodedPercent={{ traefik_encoded_allow_percent | string | lower }}"
          - "--entrypoints.websecure.http.encodedCharacters.allowEncodedQuestionMark={{ traefik_encoded_allow_question_mark | string | lower }}"
          - "--entrypoints.websecure.http.encodedCharacters.allowEncodedHash={{ traefik_encoded_allow_hash | string | lower }}"
          - "--entrypoints.websecure.http.tls.certResolver={{ traefik_default_certresolver }}"
          - "--api.dashboard=true"
          - "--api=true"
          - "--log.level={{ lookup('role_var', '_log_level', role='traefik') }}"
          - "{{ ('--log.filepath=/etc/traefik/traefik.log') if lookup('role_var', '_log_file', role='traefik') else omit }}"
          - "{{ ('--log.maxsize=' + lookup('role_var', '_log_max_size', role='traefik')) if lookup('role_var', '_log_file', role='traefik') else omit }}"
          - "{{ ('--log.maxbackups=' + lookup('role_var', '_log_max_backups', role='traefik')) if lookup('role_var', '_log_file', role='traefik') else omit }}"
          - "{{ ('--log.maxage=' + lookup('role_var', '_log_max_age', role='traefik')) if lookup('role_var', '_log_file', role='traefik') else omit }}"
          - "{{ ('--log.compress=' + lookup('role_var', '_log_compress', role='traefik')) if lookup('role_var', '_log_file', role='traefik') else omit }}"
          - "{{ '--log.nocolor=true' if lookup('role_var', '_log_file', role='traefik') else omit }}"
          - "--accesslog={{ lookup('role_var', '_access_log', role='traefik') }}"
          - "--accesslog.fields.names.StartUTC=drop"
          - "--accesslog.fields.headers.names.User-Agent=keep"
          - "--accesslog.fields.headers.names.Content-Type=keep"
          - "--accesslog.filepath=/etc/traefik/access.log"
          - "--accesslog.bufferingsize={{ lookup('role_var', '_access_buffer', role='traefik') }}"
          - "--certificatesresolvers.cfdns.acme.dnschallenge.provider={{ traefik_challenge_provider }}"
          - "{{ ('--certificatesresolvers.cfdns.acme.dnschallenge.resolvers=' + traefik_dns_resolvers) if (traefik_dns_resolvers | length > 0) else omit }}"
          - "--certificatesresolvers.cfdns.acme.email={{ user.email }}"
          - "--certificatesresolvers.cfdns.acme.storage=/etc/traefik/acme.json"
          - "{{ '--certificatesresolvers.cfdns.acme.dnschallenge.propagation.delayBeforeChecks=60s' if traefik_disable_propagation_check else omit }}"
          - "{{ '--certificatesresolvers.cfdns.acme.dnschallenge.propagation.disableChecks=true' if traefik_disable_propagation_check else omit }}"
        ```

    ??? variable list "`traefik_role_docker_commands_zerossl_acme`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_zerossl_acme:
          - "--certificatesresolvers.zerossl.acme.dnschallenge.provider={{ traefik_challenge_provider }}"
          - "{{ '--certificatesresolvers.zerossl.acme.dnschallenge.resolvers=' + traefik_dns_resolvers if (traefik_dns_resolvers | length > 0) else omit }}"
          - "--certificatesresolvers.zerossl.acme.email={{ user.email }}"
          - "--certificatesresolvers.zerossl.acme.caserver=https://acme.zerossl.com/v2/DV90"
          - "--certificatesresolvers.zerossl.acme.eab.kid={{ traefik_zerossl_kid | default('') }}"
          - "--certificatesresolvers.zerossl.acme.eab.hmacencoded={{ traefik_zerossl_hmacencoded | default('') }}"
          - "--certificatesresolvers.zerossl.acme.storage=/etc/traefik/acme.json"
          - "{{ '--certificatesresolvers.zerossl.acme.dnschallenge.propagation.delayBeforeChecks=60s' if traefik_disable_propagation_check else omit }}"
          - "{{ '--certificatesresolvers.zerossl.acme.dnschallenge.propagation.disableChecks=true' if traefik_disable_propagation_check else omit }}"
        ```

    ??? variable list "`traefik_role_docker_commands_http_validation_acme`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_http_validation_acme:
          - "--certificatesresolvers.httpresolver.acme.httpchallenge.entrypoint=web"
          - "--certificatesresolvers.httpresolver.acme.email={{ user.email }}"
          - "--certificatesresolvers.httpresolver.acme.storage=/etc/traefik/acme.json"
        ```

    ??? variable list "`traefik_role_docker_commands_http_validation_acme_zerossl`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_http_validation_acme_zerossl:
          - "--certificatesresolvers.zerosslhttp.acme.httpchallenge.entrypoint=web"
          - "--certificatesresolvers.zerosslhttp.acme.email={{ user.email }}"
          - "--certificatesresolvers.zerosslhttp.acme.caserver=https://acme.zerossl.com/v2/DV90"
          - "--certificatesresolvers.zerosslhttp.acme.eab.kid={{ traefik_zerossl_kid | default('') }}"
          - "--certificatesresolvers.zerosslhttp.acme.eab.hmacencoded={{ traefik_zerossl_hmacencoded | default('') }}"
          - "--certificatesresolvers.zerosslhttp.acme.storage=/etc/traefik/acme.json"
        ```

    ??? variable list "`traefik_role_docker_commands_google_acme`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_google_acme:
          - "--certificatesresolvers.google.acme.dnschallenge.provider={{ traefik_challenge_provider }}"
          - "{{ ('--certificatesresolvers.google.acme.dnschallenge.resolvers=' + traefik_dns_resolvers) if (traefik_dns_resolvers | length > 0) else omit }}"
          - "--certificatesresolvers.google.acme.email={{ user.email }}"
          - "--certificatesresolvers.google.acme.caserver=https://dv.acme-v02.api.pki.goog/directory"
          - "--certificatesresolvers.google.acme.eab.kid={{ traefik_google_kid | default('') }}"
          - "--certificatesresolvers.google.acme.eab.hmacencoded={{ traefik_google_hmacencoded | default('') }}"
          - "--certificatesresolvers.google.acme.storage=/etc/traefik/acme.json"
          - "{{ '--certificatesresolvers.google.acme.dnschallenge.propagation.delayBeforeChecks=60s' if traefik_disable_propagation_check else omit }}"
          - "{{ '--certificatesresolvers.google.acme.dnschallenge.propagation.disableChecks=true' if traefik_disable_propagation_check else omit }}"
        ```

    ??? variable list "`traefik_role_docker_commands_google_acme_http`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_google_acme_http:
          - "--certificatesresolvers.googlehttp.acme.httpchallenge.entrypoint=web"
          - "--certificatesresolvers.googlehttp.acme.email={{ user.email }}"
          - "--certificatesresolvers.googlehttp.acme.caserver=https://dv.acme-v02.api.pki.goog/directory"
          - "--certificatesresolvers.googlehttp.acme.eab.kid={{ traefik_google_kid | default('') }}"
          - "--certificatesresolvers.googlehttp.acme.eab.hmacencoded={{ traefik_google_hmacencoded | default('') }}"
          - "--certificatesresolvers.googlehttp.acme.storage=/etc/traefik/acme.json"
        ```

    ??? variable list "`traefik_role_docker_commands_metrics`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_metrics:
          - "--metrics.prometheus=true"
          - "--metrics.prometheus.addentrypointslabels=true"
          - "--metrics.prometheus.addrouterslabels=true"
          - "--metrics.prometheus.addserviceslabels=true"
          - "--metrics.prometheus.manualrouting=true"
        ```

    ??? variable list "`traefik_role_docker_commands_cloudflarewarp_plugin`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_cloudflarewarp_plugin:
          - "--experimental.plugins.cloudflarewarp.modulename=github.com/saltyorg/cloudflarewarp"
          - "--experimental.plugins.cloudflarewarp.version=v1.0.0"
        ```

    ??? variable list "`traefik_role_docker_commands_themepark_plugin`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_themepark_plugin:
          - "--experimental.plugins.themepark.modulename=github.com/packruler/traefik-themepark"
          - "--experimental.plugins.themepark.version=v1.4.2"
        ```

    ??? variable list "`traefik_role_docker_commands_http3`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_http3:
          - "--entrypoints.websecure.http3.advertisedport={{ traefik_entrypoint_websecure_port }}"
        ```

    ??? variable list "`traefik_role_docker_commands_tailscale`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_tailscale:
          - "--entrypoints.tailscale-web.address=:81"
          - "--entrypoints.tailscale-web.http.sanitizePath={{ traefik_sanitize_path | string | lower }}"
          - "--entrypoints.tailscale-web.http.encodedCharacters.allowEncodedSlash={{ traefik_encoded_allow_slash | string | lower }}"
          - "--entrypoints.tailscale-web.http.encodedCharacters.allowEncodedBackSlash={{ traefik_encoded_allow_backslash | string | lower }}"
          - "--entrypoints.tailscale-web.http.encodedCharacters.allowEncodedNullCharacter={{ traefik_encoded_allow_null | string | lower }}"
          - "--entrypoints.tailscale-web.http.encodedCharacters.allowEncodedSemicolon={{ traefik_encoded_allow_semicolon | string | lower }}"
          - "--entrypoints.tailscale-web.http.encodedCharacters.allowEncodedPercent={{ traefik_encoded_allow_percent | string | lower }}"
          - "--entrypoints.tailscale-web.http.encodedCharacters.allowEncodedQuestionMark={{ traefik_encoded_allow_question_mark | string | lower }}"
          - "--entrypoints.tailscale-web.http.encodedCharacters.allowEncodedHash={{ traefik_encoded_allow_hash | string | lower }}"
          - "--entrypoints.tailscale-websecure.address=:444"
          - "--entrypoints.tailscale-websecure.http.sanitizePath={{ traefik_sanitize_path | string | lower }}"
          - "--entrypoints.tailscale-websecure.http.encodedCharacters.allowEncodedSlash={{ traefik_encoded_allow_slash | string | lower }}"
          - "--entrypoints.tailscale-websecure.http.encodedCharacters.allowEncodedBackSlash={{ traefik_encoded_allow_backslash | string | lower }}"
          - "--entrypoints.tailscale-websecure.http.encodedCharacters.allowEncodedNullCharacter={{ traefik_encoded_allow_null | string | lower }}"
          - "--entrypoints.tailscale-websecure.http.encodedCharacters.allowEncodedSemicolon={{ traefik_encoded_allow_semicolon | string | lower }}"
          - "--entrypoints.tailscale-websecure.http.encodedCharacters.allowEncodedPercent={{ traefik_encoded_allow_percent | string | lower }}"
          - "--entrypoints.tailscale-websecure.http.encodedCharacters.allowEncodedQuestionMark={{ traefik_encoded_allow_question_mark | string | lower }}"
          - "--entrypoints.tailscale-websecure.http.encodedCharacters.allowEncodedHash={{ traefik_encoded_allow_hash | string | lower }}"
        ```

    ??? variable list "`traefik_role_docker_commands_crowdsec`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_crowdsec:
          - "--experimental.plugins.bouncer.modulename=github.com/maxlerebourg/crowdsec-bouncer-traefik-plugin"
          - "--experimental.plugins.bouncer.version=v1.4.4"
        ```

    ??? variable list "`traefik_role_docker_commands_custom`"

        ```yaml
        # Type: list
        traefik_role_docker_commands_custom: []
        ```

    <h5>Volumes</h5>

    ??? variable list "`traefik_role_docker_volumes_default`"

        ```yaml
        # Type: list
        traefik_role_docker_volumes_default:
          - "/var/run/docker.sock:/var/run/docker.sock"
          - "{{ traefik_role_paths_location }}:/etc/traefik"
        ```

    ??? variable list "`traefik_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        traefik_role_docker_volumes_custom: []
        ```

    <h5>Hosts</h5>

    ??? variable dict "`traefik_role_docker_hosts_default`"

        ```yaml
        # Type: dict
        traefik_role_docker_hosts_default:
          host.docker.internal: "172.19.0.1"
        ```

    ??? variable dict "`traefik_role_docker_hosts_custom`"

        ```yaml
        # Type: dict
        traefik_role_docker_hosts_custom: {}
        ```

    <h5>Labels</h5>

    ??? variable bool "`traefik_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_labels_use_common: false
        ```

    ??? variable dict "`traefik_role_docker_labels_default`"

        ```yaml
        # Type: dict
        traefik_role_docker_labels_default:
          traefik.enable: "true"
          traefik.http.routers.traefik-internal.rule: "Host(`{{ traefik_name }}`)"
          traefik.http.routers.traefik-internal.entrypoints: "internal"
          traefik.http.routers.traefik-internal.service: "api@internal"
          traefik.http.routers.traefik-http.rule: "Host(`{{ lookup('role_var', '_web_subdomain', role='traefik') }}.{{ lookup('role_var', '_web_domain', role='traefik') }}`)"
          traefik.http.routers.traefik-http.entrypoints: "{{ traefik_entrypoint_web }}"
          traefik.http.routers.traefik-http.middlewares: "{{ traefik_default_middleware_http }}"
          traefik.http.routers.traefik-http.priority: "20"
          traefik.http.routers.traefik.rule: "Host(`{{ lookup('role_var', '_web_subdomain', role='traefik') }}.{{ lookup('role_var', '_web_domain', role='traefik') }}`)"
          traefik.http.routers.traefik.entrypoints: "{{ traefik_entrypoint_websecure }}"
          traefik.http.routers.traefik.tls: "true"
          traefik.http.routers.traefik.tls.options: "securetls@file"
          traefik.http.routers.traefik.middlewares: "{{ traefik_default_middleware }}"
          traefik.http.routers.traefik.priority: "20"
          traefik.http.routers.traefik.service: "api@internal"
          traefik.http.middlewares.traefik-auth.basicauth.usersfile: "/etc/traefik/auth"
          traefik.http.middlewares.gzip.compress: "true"
          traefik.http.middlewares.autodetect.contenttype: "true"
          traefik.http.middlewares.redirect-to-https.redirectscheme.scheme: "https"
          traefik.http.middlewares.redirect-to-https.redirectscheme.permanent: "true"
          traefik.http.middlewares.authelia.forwardauth.address: "{{ 'http://' + authelia_name + ':9091/api/verify?rd=' + lookup('role_var', '_web_url', role='authelia') + '/'
                                                                  if authelia_is_master
                                                                  else lookup('role_var', '_web_url', role='authelia') + '/api/verify?rd=' + lookup('role_var', '_web_url', role='authelia') + '/' }}"
          traefik.http.middlewares.authelia.forwardauth.trustForwardHeader: "true"
          traefik.http.middlewares.authelia.forwardauth.authResponseHeaders: "{{ lookup('role_var', '_response_headers', role='authelia') | join(',') }}"
          traefik.http.middlewares.authelia-basic.forwardauth.address: "{{ 'http://' + authelia_name + ':9091/api/verify?auth=basic&rd=' + lookup('role_var', '_web_url', role='authelia') + '/'
                                                                        if authelia_is_master
                                                                        else lookup('role_var', '_web_url', role='authelia') + '/api/verify?auth=basic&rd=' + lookup('role_var', '_web_url', role='authelia') + '/' }}"
          traefik.http.middlewares.authelia-basic.forwardauth.trustForwardHeader: "true"
          traefik.http.middlewares.authelia-basic.forwardauth.authResponseHeaders: "{{ lookup('role_var', '_response_headers', role='authelia') | join(',') }}"
          traefik.http.middlewares.authentik.forwardauth.address: "{{ 'http://' + authentik_name + ':9000/outpost.goauthentik.io/auth/traefik'
                                                                   if authentik_is_master
                                                                   else lookup('role_var', '_web_url', role='authentik') + '/outpost.goauthentik.io/auth/traefik' }}"
          traefik.http.middlewares.authentik.forwardauth.trustForwardHeader: "true"
          traefik.http.middlewares.authentik.forwardauth.authResponseHeaders: "{{ lookup('role_var', '_response_headers', role='authentik') | join(',') }}"
        ```

    ??? variable dict "`traefik_role_docker_labels_cloudflare`"

        ```yaml
        # Type: dict
        traefik_role_docker_labels_cloudflare:
          traefik.http.middlewares.cloudflarewarp.plugin.cloudflarewarp.disableDefault: "false"
        ```

    ??? variable dict "`traefik_role_docker_labels_dns_validation`"

        ```yaml
        # Type: dict
        traefik_role_docker_labels_dns_validation:
          traefik.http.routers.traefik.tls.certresolver: "{{ traefik_default_certresolver }}"
          traefik.http.routers.traefik.tls.domains[0].main: "{{ user.domain }}"
          traefik.http.routers.traefik.tls.domains[0].sans: "{{ '*.' + user.domain }}"
        ```

    ??? variable dict "`traefik_role_docker_labels_http_validation`"

        ```yaml
        # Type: dict
        traefik_role_docker_labels_http_validation:
          traefik.http.routers.traefik.tls.certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable dict "`traefik_role_docker_labels_metrics`"

        ```yaml
        # Type: dict
        traefik_role_docker_labels_metrics:
          traefik.http.routers.metrics-http.rule: "Host(`{{ lookup('role_var', '_metrics_subdomain', role='traefik') }}.{{ lookup('role_var', '_metrics_domain', role='traefik') }}`) && Path(`/prometheus`)"
          traefik.http.routers.metrics-http.service: prometheus@internal
          traefik.http.routers.metrics-http.entrypoints: "{{ traefik_entrypoint_web }}"
          traefik.http.routers.metrics-http.middlewares: "traefik-auth,{{ traefik_default_middleware_http_api }}"
          traefik.http.routers.metrics-http.priority: "20"
          traefik.http.routers.metrics.rule: "Host(`{{ lookup('role_var', '_metrics_subdomain', role='traefik') }}.{{ lookup('role_var', '_metrics_domain', role='traefik') }}`) && Path(`/prometheus`)"
          traefik.http.routers.metrics.service: prometheus@internal
          traefik.http.routers.metrics.entrypoints: "{{ traefik_entrypoint_websecure }}"
          traefik.http.routers.metrics.tls: "true"
          traefik.http.routers.metrics.tls.options: "securetls@file"
          traefik.http.routers.metrics.middlewares: "traefik-auth,{{ traefik_default_middleware_api }}"
          traefik.http.routers.metrics.priority: "20"
        ```

    ??? variable dict "`traefik_role_docker_labels_crowdsec`"

        ```yaml
        # Type: dict
        traefik_role_docker_labels_crowdsec:
          traefik.http.middlewares.crowdsec.plugin.bouncer.enabled: "true"
          traefik.http.middlewares.crowdsec.plugin.bouncer.crowdseclapikey: "{{ traefik_crowdsec_bouncer_key | default('') }}"
          traefik.http.middlewares.crowdsec.plugin.bouncer.crowdseclapischeme: "http"
          traefik.http.middlewares.crowdsec.plugin.bouncer.crowdseclapihost: "172.19.0.1:{{ traefik_crowdsec_port }}"
          traefik.http.middlewares.crowdsec.plugin.bouncer.forwardedheaderstrustedips: "{{ traefik_trusted_ips_template if (traefik_trusted_ips_template | length > 0) else omit }}"
          traefik.http.middlewares.crowdsec.plugin.bouncer.banhtmlfilepath: "{{ traefik_crowdsec_ban_filepath }}"
        ```

    ??? variable dict "`traefik_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        traefik_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`traefik_role_docker_hostname`"

        ```yaml
        # Type: string
        traefik_role_docker_hostname: "{{ traefik_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`traefik_role_docker_networks_alias`"

        ```yaml
        # Type: string
        traefik_role_docker_networks_alias: "{{ traefik_name }}"
        ```

    ??? variable list "`traefik_role_docker_networks_default`"

        ```yaml
        # Type: list
        traefik_role_docker_networks_default: []
        ```

    ??? variable list "`traefik_role_docker_networks_custom`"

        ```yaml
        # Type: list
        traefik_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`traefik_role_docker_restart_policy`"

        ```yaml
        # Type: string
        traefik_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`traefik_role_docker_state`"

        ```yaml
        # Type: string
        traefik_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`traefik_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        traefik_role_docker_blkio_weight:
        ```

    ??? variable int "`traefik_role_docker_cpu_period`"

        ```yaml
        # Type: int
        traefik_role_docker_cpu_period:
        ```

    ??? variable int "`traefik_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        traefik_role_docker_cpu_quota:
        ```

    ??? variable int "`traefik_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        traefik_role_docker_cpu_shares:
        ```

    ??? variable string "`traefik_role_docker_cpus`"

        ```yaml
        # Type: string
        traefik_role_docker_cpus:
        ```

    ??? variable string "`traefik_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        traefik_role_docker_cpuset_cpus:
        ```

    ??? variable string "`traefik_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        traefik_role_docker_cpuset_mems:
        ```

    ??? variable string "`traefik_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        traefik_role_docker_kernel_memory:
        ```

    ??? variable string "`traefik_role_docker_memory`"

        ```yaml
        # Type: string
        traefik_role_docker_memory:
        ```

    ??? variable string "`traefik_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        traefik_role_docker_memory_reservation:
        ```

    ??? variable string "`traefik_role_docker_memory_swap`"

        ```yaml
        # Type: string
        traefik_role_docker_memory_swap:
        ```

    ??? variable int "`traefik_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        traefik_role_docker_memory_swappiness:
        ```

    ??? variable string "`traefik_role_docker_shm_size`"

        ```yaml
        # Type: string
        traefik_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`traefik_role_docker_cap_drop`"

        ```yaml
        # Type: list
        traefik_role_docker_cap_drop:
        ```

    ??? variable string "`traefik_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        traefik_role_docker_cgroupns_mode:
        ```

    ??? variable list "`traefik_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        traefik_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`traefik_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        traefik_role_docker_device_read_bps:
        ```

    ??? variable list "`traefik_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        traefik_role_docker_device_read_iops:
        ```

    ??? variable list "`traefik_role_docker_device_requests`"

        ```yaml
        # Type: list
        traefik_role_docker_device_requests:
        ```

    ??? variable list "`traefik_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        traefik_role_docker_device_write_bps:
        ```

    ??? variable list "`traefik_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        traefik_role_docker_device_write_iops:
        ```

    ??? variable list "`traefik_role_docker_devices`"

        ```yaml
        # Type: list
        traefik_role_docker_devices:
        ```

    ??? variable string "`traefik_role_docker_devices_default`"

        ```yaml
        # Type: string
        traefik_role_docker_devices_default:
        ```

    ??? variable list "`traefik_role_docker_groups`"

        ```yaml
        # Type: list
        traefik_role_docker_groups:
        ```

    ??? variable bool "`traefik_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_privileged:
        ```

    ??? variable list "`traefik_role_docker_security_opts`"

        ```yaml
        # Type: list
        traefik_role_docker_security_opts:
        ```

    ??? variable string "`traefik_role_docker_user`"

        ```yaml
        # Type: string
        traefik_role_docker_user:
        ```

    ??? variable string "`traefik_role_docker_userns_mode`"

        ```yaml
        # Type: string
        traefik_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`traefik_role_docker_dns_opts`"

        ```yaml
        # Type: list
        traefik_role_docker_dns_opts:
        ```

    ??? variable list "`traefik_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        traefik_role_docker_dns_search_domains:
        ```

    ??? variable list "`traefik_role_docker_dns_servers`"

        ```yaml
        # Type: list
        traefik_role_docker_dns_servers:
        ```

    ??? variable string "`traefik_role_docker_domainname`"

        ```yaml
        # Type: string
        traefik_role_docker_domainname:
        ```

    ??? variable list "`traefik_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        traefik_role_docker_exposed_ports:
        ```

    ??? variable bool "`traefik_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_hosts_use_common:
        ```

    ??? variable string "`traefik_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        traefik_role_docker_ipc_mode:
        ```

    ??? variable list "`traefik_role_docker_links`"

        ```yaml
        # Type: list
        traefik_role_docker_links:
        ```

    ??? variable string "`traefik_role_docker_network_mode`"

        ```yaml
        # Type: string
        traefik_role_docker_network_mode:
        ```

    ??? variable string "`traefik_role_docker_pid_mode`"

        ```yaml
        # Type: string
        traefik_role_docker_pid_mode:
        ```

    ??? variable string "`traefik_role_docker_uts`"

        ```yaml
        # Type: string
        traefik_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`traefik_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_keep_volumes:
        ```

    ??? variable list "`traefik_role_docker_mounts`"

        ```yaml
        # Type: list
        traefik_role_docker_mounts:
        ```

    ??? variable dict "`traefik_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        traefik_role_docker_storage_opts:
        ```

    ??? variable list "`traefik_role_docker_tmpfs`"

        ```yaml
        # Type: list
        traefik_role_docker_tmpfs:
        ```

    ??? variable string "`traefik_role_docker_volume_driver`"

        ```yaml
        # Type: string
        traefik_role_docker_volume_driver:
        ```

    ??? variable list "`traefik_role_docker_volumes_from`"

        ```yaml
        # Type: list
        traefik_role_docker_volumes_from:
        ```

    ??? variable bool "`traefik_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_volumes_global:
        ```

    ??? variable string "`traefik_role_docker_working_dir`"

        ```yaml
        # Type: string
        traefik_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`traefik_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_auto_remove:
        ```

    ??? variable bool "`traefik_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_cleanup:
        ```

    ??? variable string "`traefik_role_docker_force_kill`"

        ```yaml
        # Type: string
        traefik_role_docker_force_kill:
        ```

    ??? variable dict "`traefik_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        traefik_role_docker_healthcheck:
        ```

    ??? variable int "`traefik_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        traefik_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`traefik_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_init:
        ```

    ??? variable string "`traefik_role_docker_kill_signal`"

        ```yaml
        # Type: string
        traefik_role_docker_kill_signal:
        ```

    ??? variable string "`traefik_role_docker_log_driver`"

        ```yaml
        # Type: string
        traefik_role_docker_log_driver:
        ```

    ??? variable dict "`traefik_role_docker_log_options`"

        ```yaml
        # Type: dict
        traefik_role_docker_log_options:
        ```

    ??? variable bool "`traefik_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_oom_killer:
        ```

    ??? variable int "`traefik_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        traefik_role_docker_oom_score_adj:
        ```

    ??? variable bool "`traefik_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_output_logs:
        ```

    ??? variable bool "`traefik_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_paused:
        ```

    ??? variable bool "`traefik_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_recreate:
        ```

    ??? variable int "`traefik_role_docker_restart_retries`"

        ```yaml
        # Type: int
        traefik_role_docker_restart_retries:
        ```

    ??? variable int "`traefik_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        traefik_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`traefik_role_docker_capabilities`"

        ```yaml
        # Type: list
        traefik_role_docker_capabilities:
        ```

    ??? variable string "`traefik_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        traefik_role_docker_cgroup_parent:
        ```

    ??? variable int "`traefik_role_docker_create_timeout`"

        ```yaml
        # Type: int
        traefik_role_docker_create_timeout:
        ```

    ??? variable string "`traefik_role_docker_entrypoint`"

        ```yaml
        # Type: string
        traefik_role_docker_entrypoint:
        ```

    ??? variable string "`traefik_role_docker_env_file`"

        ```yaml
        # Type: string
        traefik_role_docker_env_file:
        ```

    ??? variable bool "`traefik_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_read_only:
        ```

    ??? variable string "`traefik_role_docker_runtime`"

        ```yaml
        # Type: string
        traefik_role_docker_runtime:
        ```

    ??? variable list "`traefik_role_docker_sysctls`"

        ```yaml
        # Type: list
        traefik_role_docker_sysctls:
        ```

    ??? variable list "`traefik_role_docker_ulimits`"

        ```yaml
        # Type: list
        traefik_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`traefik_role_access_buffer`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_access_buffer:
        ```

    ??? variable bool "`traefik_role_access_log`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_access_log:
        ```

    ??? variable bool "`traefik_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        traefik_role_autoheal_enabled: true
        ```

    ??? variable string "`traefik_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        traefik_role_depends_on: ""
        ```

    ??? variable string "`traefik_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        traefik_role_depends_on_delay: "0"
        ```

    ??? variable string "`traefik_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        traefik_role_depends_on_healthchecks:
        ```

    ??? variable bool "`traefik_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        traefik_role_diun_enabled: true
        ```

    ??? variable bool "`traefik_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        traefik_role_dns_enabled: true
        ```

    ??? variable bool "`traefik_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        traefik_role_docker_controller: true
        ```

    ??? variable string "`traefik_role_docker_image_repo`"

        ```yaml
        # Type: string
        traefik_role_docker_image_repo:
        ```

    ??? variable string "`traefik_role_docker_image_tag`"

        ```yaml
        # Type: string
        traefik_role_docker_image_tag:
        ```

    ??? variable bool "`traefik_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_volumes_download:
        ```

    ??? variable bool "`traefik_role_log_compress`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_compress:
        ```

    ??? variable bool "`traefik_role_log_file`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_file:
        ```

    ??? variable bool "`traefik_role_log_level`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_level:
        ```

    ??? variable bool "`traefik_role_log_max_age`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_max_age:
        ```

    ??? variable bool "`traefik_role_log_max_backups`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_max_backups:
        ```

    ??? variable bool "`traefik_role_log_max_size`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_max_size:
        ```

    ??? variable string "`traefik_role_metrics_domain`"

        ```yaml
        # Type: string
        traefik_role_metrics_domain:
        ```

    ??? variable string "`traefik_role_metrics_subdomain`"

        ```yaml
        # Type: string
        traefik_role_metrics_subdomain:
        ```

    ??? variable string "`traefik_role_response_headers`"

        ```yaml
        # Type: string
        traefik_role_response_headers:
        ```

    ??? variable string "`traefik_role_themepark_addons`"

        ```yaml
        # Type: string
        traefik_role_themepark_addons:
        ```

    ??? variable string "`traefik_role_themepark_app`"

        ```yaml
        # Type: string
        traefik_role_themepark_app:
        ```

    ??? variable string "`traefik_role_themepark_theme`"

        ```yaml
        # Type: string
        traefik_role_themepark_theme:
        ```

    ??? variable dict "`traefik_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        traefik_role_traefik_api_endpoint:
        ```

    ??? variable string "`traefik_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        traefik_role_traefik_api_middleware:
        ```

    ??? variable string "`traefik_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        traefik_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`traefik_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`traefik_role_traefik_certresolver`"

        ```yaml
        # Type: string
        traefik_role_traefik_certresolver:
        ```

    ??? variable bool "`traefik_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`traefik_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`traefik_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`traefik_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        traefik_role_traefik_middleware_http:
        ```

    ??? variable bool "`traefik_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`traefik_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`traefik_role_traefik_priority`"

        ```yaml
        # Type: string
        traefik_role_traefik_priority:
        ```

    ??? variable bool "`traefik_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`traefik_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        traefik_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`traefik_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        traefik_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`traefik_role_web_domain`"

        ```yaml
        # Type: string
        traefik_role_web_domain:
        ```

    ??? variable list "`traefik_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        traefik_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            traefik_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "traefik2.{{ user.domain }}"
              - "traefik.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`traefik_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        traefik_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            traefik_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'traefik2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`traefik_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        traefik_role_web_http_port:
        ```

    ??? variable string "`traefik_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        traefik_role_web_http_scheme:
        ```

    ??? variable dict "`traefik_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        traefik_role_web_http_serverstransport:
        ```

    ??? variable string "`traefik_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        traefik_role_web_scheme:
        ```

    ??? variable dict "`traefik_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        traefik_role_web_serverstransport:
        ```

    ??? variable string "`traefik_role_web_subdomain`"

        ```yaml
        # Type: string
        traefik_role_web_subdomain:
        ```

    ??? variable string "`traefik_role_web_url`"

        ```yaml
        # Type: string
        traefik_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->