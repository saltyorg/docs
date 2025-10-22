---
hide:
  - tags
tags:
  - fireflyiii
  - finance
  - budgeting
---

# Firefly III

[TOC]

## What is it?

[Firefly III](https://www.firefly-iii.org) is a (self-hosted) manager for your personal finances. It can help you keep track of your expenses and income, so you can spend less and save more. Firefly III supports the use of budgets, categories and tags. Using a bunch of external tools, you can import data. It also has many neat financial reports available.

Firefly III should give you insight into and control over your finances. Money should be useful, not scary. You should be able to see where it is going, to feel your expenses and to... wow, I'm going overboard with this aren't I?

But you get the idea: this is your money. These are your expenses. Stop them from controlling you.

If your project has grown and deploying from the terminal is no longer for you then Semaphore UI is what you need.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.firefly-iii.org){: .header-icons } | [:octicons-link-16: Docs](https://docs.firefly-iii.org/?mtm_campaign=firefly-iii-org&mtm_kwd=top-link){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/firefly-iii/firefly-iii/){: .header-icons } | [:material-docker: Docker](https://docs.firefly-iii.org/how-to/firefly-iii/installation/docker/){: .header-icons }|

## 1. Installation

``` shell

sb install sandbox-fireflyiii

```

## 2. URL

- To access the Firefly III, visit `https://fireflyiii.xDOMAIN_NAMEx`

## 3. Additional Settings

- The default installation utilises a seperate postgres database.
- This will install the fireflyiii core container and install the mariadb database
  - > **Note: It can be installed using postgresql and mysql**
- It will by default enable webhooks

> **Note: For all available settings please refer to the Firefly III [example env](https://raw.githubusercontent.com/firefly-iii/firefly-iii/main/.env.example)**

#### 3.1 Email Notifications
To enable email notifications, set the following [inventory](../../saltbox/inventory/index.md) entries to your desired values:

``` yaml title="Firefly III Email Settings"
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

### 3.2 Firefly III Authentication
By default this utilises the authelia authentication and utilises its own authentication mechanism

This can be changed to do 1 of the following:

- [Remove Authelia authentication (Not Recommended)](#321-remove-authelia-authentication-not-recommended)
- ~~Remove Firefly III built-in authentication~~ ***Not Understood***

#### 3.2.1 Remove Authelia Authentication (Not Recommended)

``` yaml title="Firefly III Remove Authelia"
fireflyiii_traefik_sso_middleware: ""
```

Redeploy the Firefly III role to apply the above changes.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        fireflyiii_role_mariadb_docker_image_tag: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `fireflyiii_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `fireflyiii_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    fireflyiii_name: fireflyiii

    ```

??? example "Settings"

    ```yaml
    # Type: string
    fireflyiii_role_mariadb_name: "{{ fireflyiii_name }}-mariadb"

    # Type: string
    fireflyiii_role_mariadb_paths_folder: "{{ fireflyiii_name }}"

    # Type: string
    fireflyiii_role_mariadb_paths_location: "{{ server_appdata_path }}/{{ lookup('role_var', '_paths_folder', role='mariadb') }}/mariadb"

    # Type: string
    fireflyiii_role_mariadb_docker_image_tag: "lts"

    # Type: string
    fireflyiii_role_mariadb_docker_env_password: "{{ fireflyiii_db_password_saltbox_facts.facts.secret_key }}"

    # Type: string
    fireflyiii_role_mariadb_docker_env_db: "{{ fireflyiii_name }}-mariadb"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    fireflyiii_role_paths_folder: "{{ fireflyiii_name }}"

    # Type: string
    fireflyiii_role_paths_location: "{{ server_appdata_path }}/{{ fireflyiii_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    fireflyiii_role_web_subdomain: "{{ fireflyiii_name }}"

    # Type: string
    fireflyiii_role_web_domain: "{{ user.domain }}"

    # Type: string
    fireflyiii_role_web_port: "8080"

    # Type: string
    fireflyiii_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='fireflyiii') + '.' + lookup('role_var', '_web_domain', role='fireflyiii')
                              if (lookup('role_var', '_web_subdomain', role='fireflyiii') | length > 0)
                              else lookup('role_var', '_web_domain', role='fireflyiii')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    fireflyiii_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='fireflyiii') }}"

    # Type: string
    fireflyiii_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='fireflyiii') }}"

    # Type: bool (true/false)
    fireflyiii_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    fireflyiii_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    fireflyiii_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    fireflyiii_role_traefik_middleware_custom: ""

    # Type: string
    fireflyiii_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    fireflyiii_role_traefik_enabled: true

    # Type: bool (true/false)
    fireflyiii_role_traefik_api_enabled: true

    # Type: string
    fireflyiii_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    fireflyiii_role_docker_container: "{{ fireflyiii_name }}"

    # Image
    # Type: bool (true/false)
    fireflyiii_role_docker_image_pull: true

    # Type: string
    fireflyiii_role_docker_image_repo: "fireflyiii/core"

    # Type: string
    fireflyiii_role_docker_image_tag: "latest"

    # Type: string
    fireflyiii_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='fireflyiii') }}:{{ lookup('role_var', '_docker_image_tag', role='fireflyiii') }}"

    # Envs
    # Type: dict
    fireflyiii_role_docker_envs_default: 
      APP_ENV: "production"
      SITE_OWNER: "{{ user.email }}"
      APP_KEY: "{{ fireflyiii_appkey_saltbox_facts.facts.secret_key }}"
      DEFAULT_LANGUAGE: "en_US"
      DEFAULT_LOCALE: "equal"
      TZ: "{{ tz }}"
      TRUSTED_PROXIES: "**"
      LOG_CHANNEL: "stack"
      APP_LOG_LEVEL: "notice"
      AUDIT_LOG_LEVEL: "emergency"
      DB_CONNECTION: "mysql"
      DB_HOST: "{{ fireflyiii_name }}-mariadb"
      DB_PORT: "3306"
      DB_DATABASE: fireflyiii
      DB_USERNAME: "root"
      DB_PASSWORD: "{{ fireflyiii_db_password_saltbox_facts.facts.secret_key }}"
      AUTHENTICATION_GUARD: "web"
      APP_URL: "{{ lookup('role_var', '_web_url', role='fireflyiii') }}"
      ALLOW_WEBHOOKS: "True"

    # Type: dict
    fireflyiii_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    fireflyiii_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='fireflyiii') }}/upload:/var/www/html/storage/upload"
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro

    # Type: list
    fireflyiii_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    fireflyiii_role_docker_hostname: "{{ fireflyiii_name }}"

    # Networks
    # Type: string
    fireflyiii_role_docker_networks_alias: "{{ fireflyiii_name }}"

    # Type: list
    fireflyiii_role_docker_networks_default: []

    # Type: list
    fireflyiii_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    fireflyiii_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    fireflyiii_role_docker_state: started

    # Dependencies
    # Type: string
    fireflyiii_role_depends_on: "{{ fireflyiii_name }}-mariadb"

    # Type: string
    fireflyiii_role_depends_on_delay: "0"

    # Type: string
    fireflyiii_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    fireflyiii_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    fireflyiii_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    fireflyiii_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    fireflyiii_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    fireflyiii_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    fireflyiii_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    fireflyiii_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    fireflyiii_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    fireflyiii_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    fireflyiii_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    fireflyiii_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    fireflyiii_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    fireflyiii_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    fireflyiii_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    fireflyiii_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    fireflyiii_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    fireflyiii_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        fireflyiii_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "fireflyiii2.{{ user.domain }}"
          - "fireflyiii.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        fireflyiii_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'fireflyiii2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
