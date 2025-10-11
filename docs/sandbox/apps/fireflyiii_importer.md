---
hide:
  - tags
tags:
  - fireflyiii-importer
  - finance
  - tools
---

# Firefly III Data Importer

[TOC]

## What is it?

[Firefly III](https://www.firefly-iii.org) is a (self-hosted) manager for your personal finances. The data importer is built to help you import transactions into Firefly III. It is separated from Firefly III for security and maintenance reasons.

The data importer does not connect to your bank directly. Instead, it uses Nordigen and SaltEdge to connect to over 6000 banks worldwide. These services are free for Firefly III users, but require registration. Keep in mind these services have their own privacy and data usage policies.

The data importer can import CSV files you've downloaded from your bank.

You can run the data importer once, for a bulk import. You can also run it regularly to keep up with new transactions.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.firefly-iii.org/explanation/data-importer/about/introduction/){: .header-icons } | [:octicons-link-16: Docs](https://docs.firefly-iii.org/explanation/data-importer/about/introduction/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/firefly-iii/data-importer){: .header-icons } | [:material-docker: Docker](hhttps://docs.firefly-iii.org/how-to/data-importer/installation/docker/){: .header-icons }|

## 1. Installation

``` shell
sb install sandbox-fireflyiii_importer
```

## 2. URL

- To access the Firefly III Data Importer, visit `https://fireflyiii-importer._yourdomain.com_`

## 3. Setup

### 3.1 Connection To Firefly III
The Required variables that should be defined in [inventory](../../saltbox/inventory/index.md):

To authenticate the Data Importer to Firefly III you require to use either:

- [Access Token](#311-access-token)
- [Client ID](#312-client-id) 

#### 3.1.1 Access Token

``` yaml title="Firefly III Data Importer Access Token Settings"
fireflyiii_importer_docker_envs_custom:
  - FIREFLY_III_ACCESS_TOKEN: ""  # (1)!
```

1. Your access token from your instance of Firefly III | Options | Profile | OAuth | Personal Access Tokens | Create New Token.

#### 3.1.2 Client ID

``` yaml title="Firefly III Data Importer Client ID Settings"
fireflyiii_importer_docker_envs_custom:
  - FIREFLY_III_CLIENT_ID: "1"  # (1)!
```

1. Your client id from your instance of Firefly III | Options | Profile | OAuth | OAuth Clients | Create New Client.
> Note: Your require to leave Confidential unticked

## 4. Import data

For the following methods, your data need to be formatted in CSV.

### 4.1 Web import

You can refer to the following documentation to execute import from the server: [web import](https://docs.firefly-iii.org/how-to/data-importer/import/csv/)

### 4.2 Server import

You can refer to the following documentation to execute import from the server: [CLI import](https://docs.firefly-iii.org/how-to/data-importer/advanced/cli/)

## 5. Additional Settings

> **Note: For all available settings please refer to the Firefly III Data Importer [example env](https://raw.githubusercontent.com/firefly-iii/docker/main/docker-compose-importer.yml)**

### 5.1 Email Notifications
To enable email notifications, set the following [inventory](../../saltbox/inventory/index.md) entries to your desired values:

``` yaml title="Firefly III Data Importer Email Settings"
MAIL_MAILER: "log"  # (1)!
MAIL_HOST: "localhost"  # (2)!
MAIL_PORT: "25"  # (3)!
MAIL_FROM: "fireflyiii@domain.com"  # (4)!
MAIL_USERNAME: ""  # (5)!
MAIL_PASSWORD: ""  # (6)!
MAIN_ENCRYPTION: ""  # (7)!
```

1. The MAIL_MAILER-setting indicates the system that is used for mailing. Firefly III supports the following mail systems: smtp, sendmail, mailgun, mandrill, sparkpost and log. [Here](https://docs.firefly-iii.org/how-to/firefly-iii/advanced/notifications/#email) is an explanation about each MAIL_MAILER option
2. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
4. Replace `25` with your email port. IE: `587`
3. The email address you want to send to. Replace `""` with the email address you want to send to
5. Replace `""` with your email username if necessary.
6. Replace `""` with your email password if necessary.
7. Use `SSL` or `TLS` for communication with the SMTP server. Can be `true` or '`false`.

Redeploy the Firefly III Importer Role role to apply the above changes.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        fireflyiii_importer_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    fireflyiii_importer_name: fireflyiii-importer

    ```

??? example "Paths"

    ```yaml
    # Type: string
    fireflyiii_importer_role_paths_folder: "{{ fireflyiii_name }}"

    # Type: string
    fireflyiii_importer_role_paths_location: "{{ server_appdata_path }}/{{ fireflyiii_importer_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    fireflyiii_importer_role_web_subdomain: "{{ fireflyiii_importer_name }}"

    # Type: string
    fireflyiii_importer_role_web_domain: "{{ user.domain }}"

    # Type: string
    fireflyiii_importer_role_web_port: "8080"

    # Type: string
    fireflyiii_importer_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='fireflyiii_importer') + '.' + lookup('role_var', '_web_domain', role='fireflyiii_importer')
                                       if (lookup('role_var', '_web_subdomain', role='fireflyiii_importer') | length > 0)
                                       else lookup('role_var', '_web_domain', role='fireflyiii_importer')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    fireflyiii_importer_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='fireflyiii_importer') }}"

    # Type: string
    fireflyiii_importer_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='fireflyiii_importer') }}"

    # Type: bool (true/false)
    fireflyiii_importer_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    fireflyiii_importer_role_traefik_sso_middleware: ""

    # Type: string
    fireflyiii_importer_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    fireflyiii_importer_role_traefik_middleware_custom: ""

    # Type: string
    fireflyiii_importer_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_enabled: true

    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_api_enabled: false

    # Type: string
    fireflyiii_importer_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    fireflyiii_importer_role_docker_container: "{{ fireflyiii_importer_name }}"

    # Image
    # Type: bool (true/false)
    fireflyiii_importer_role_docker_image_pull: true

    # Type: string
    fireflyiii_importer_role_docker_image_repo: "fireflyiii/data-importer"

    # Type: string
    fireflyiii_importer_role_docker_image_tag: "latest"

    # Type: string
    fireflyiii_importer_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='fireflyiii_importer') }}:{{ lookup('role_var', '_docker_image_tag', role='fireflyiii_importer') }}"

    # Envs
    # Type: dict
    fireflyiii_importer_role_docker_envs_default: 
      IMPORT_DIR_ALLOWLIST: /import
      FIREFLY_III_URL: "http://{{ fireflyiii_name }}:8080"
      VANITY_URL: "{{ lookup('role_var', '_web_url', role='fireflyiii') }}"
      TRUSTED_PROXIES: "**"
      TZ: "{{ tz }}"

    # Type: dict
    fireflyiii_importer_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    fireflyiii_importer_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='fireflyiii') }}/import:/import"
      - "/etc/timezone:/etc/timezone:ro"
      - "/etc/localtime:/etc/localtime:ro"

    # Type: list
    fireflyiii_importer_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    fireflyiii_importer_role_docker_hostname: "{{ fireflyiii_importer_name }}"

    # Networks
    # Type: string
    fireflyiii_importer_role_docker_networks_alias: "{{ fireflyiii_importer_name }}"

    # Type: list
    fireflyiii_importer_role_docker_networks_default: []

    # Type: list
    fireflyiii_importer_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    fireflyiii_importer_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    fireflyiii_importer_role_docker_state: started

    # Dependencies
    # Type: string
    fireflyiii_importer_role_depends_on: "{{ fireflyiii_name }}"

    # Type: string
    fireflyiii_importer_role_depends_on_delay: "0"

    # Type: string
    fireflyiii_importer_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    fireflyiii_importer_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    fireflyiii_importer_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    fireflyiii_importer_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    fireflyiii_importer_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    fireflyiii_importer_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    fireflyiii_importer_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    fireflyiii_importer_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    fireflyiii_importer_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    fireflyiii_importer_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        fireflyiii_importer_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "fireflyiii_importer2.{{ user.domain }}"
          - "fireflyiii_importer.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        fireflyiii_importer_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'fireflyiii_importer2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
