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

- To access the Firefly III, visit <https://fireflyiii.iYOUR_DOMAIN_NAMEi>

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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    fireflyiii_role_mariadb_docker_image_tag: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `fireflyiii_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `fireflyiii_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`fireflyiii_name`"

        ```yaml
        # Type: string
        fireflyiii_name: fireflyiii
        ```

=== "Settings"

    ??? variable string "`fireflyiii_role_mariadb_name`"

        ```yaml
        # Type: string
        fireflyiii_role_mariadb_name: "{{ fireflyiii_name }}-mariadb"
        ```

    ??? variable string "`fireflyiii_role_mariadb_paths_folder`"

        ```yaml
        # Type: string
        fireflyiii_role_mariadb_paths_folder: "{{ fireflyiii_name }}"
        ```

    ??? variable string "`fireflyiii_role_mariadb_paths_location`"

        ```yaml
        # Type: string
        fireflyiii_role_mariadb_paths_location: "{{ server_appdata_path }}/{{ lookup('role_var', '_paths_folder', role='mariadb') }}/mariadb"
        ```

    ??? variable string "`fireflyiii_role_mariadb_docker_image_tag`"

        ```yaml
        # Type: string
        fireflyiii_role_mariadb_docker_image_tag: "lts"
        ```

    ??? variable string "`fireflyiii_role_mariadb_docker_env_password`"

        ```yaml
        # Type: string
        fireflyiii_role_mariadb_docker_env_password: "{{ fireflyiii_db_password_saltbox_facts.facts.secret_key }}"
        ```

    ??? variable string "`fireflyiii_role_mariadb_docker_env_db`"

        ```yaml
        # Type: string
        fireflyiii_role_mariadb_docker_env_db: "{{ fireflyiii_name }}-mariadb"
        ```

=== "Paths"

    ??? variable string "`fireflyiii_role_paths_folder`"

        ```yaml
        # Type: string
        fireflyiii_role_paths_folder: "{{ fireflyiii_name }}"
        ```

    ??? variable string "`fireflyiii_role_paths_location`"

        ```yaml
        # Type: string
        fireflyiii_role_paths_location: "{{ server_appdata_path }}/{{ fireflyiii_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`fireflyiii_role_web_subdomain`"

        ```yaml
        # Type: string
        fireflyiii_role_web_subdomain: "{{ fireflyiii_name }}"
        ```

    ??? variable string "`fireflyiii_role_web_domain`"

        ```yaml
        # Type: string
        fireflyiii_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`fireflyiii_role_web_port`"

        ```yaml
        # Type: string
        fireflyiii_role_web_port: "8080"
        ```

    ??? variable string "`fireflyiii_role_web_url`"

        ```yaml
        # Type: string
        fireflyiii_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='fireflyiii') + '.' + lookup('role_var', '_web_domain', role='fireflyiii')
                                  if (lookup('role_var', '_web_subdomain', role='fireflyiii') | length > 0)
                                  else lookup('role_var', '_web_domain', role='fireflyiii')) }}"
        ```

=== "DNS"

    ??? variable string "`fireflyiii_role_dns_record`"

        ```yaml
        # Type: string
        fireflyiii_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='fireflyiii') }}"
        ```

    ??? variable string "`fireflyiii_role_dns_zone`"

        ```yaml
        # Type: string
        fireflyiii_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='fireflyiii') }}"
        ```

    ??? variable bool "`fireflyiii_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`fireflyiii_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        fireflyiii_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`fireflyiii_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        fireflyiii_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`fireflyiii_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        fireflyiii_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`fireflyiii_role_traefik_certresolver`"

        ```yaml
        # Type: string
        fireflyiii_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`fireflyiii_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_role_traefik_enabled: true
        ```

    ??? variable bool "`fireflyiii_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_role_traefik_api_enabled: true
        ```

    ??? variable string "`fireflyiii_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        fireflyiii_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`fireflyiii_role_docker_container`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_container: "{{ fireflyiii_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`fireflyiii_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_role_docker_image_pull: true
        ```

    ??? variable string "`fireflyiii_role_docker_image_repo`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_image_repo: "fireflyiii/core"
        ```

    ??? variable string "`fireflyiii_role_docker_image_tag`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_image_tag: "latest"
        ```

    ??? variable string "`fireflyiii_role_docker_image`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='fireflyiii') }}:{{ lookup('role_var', '_docker_image_tag', role='fireflyiii') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`fireflyiii_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`fireflyiii_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        fireflyiii_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`fireflyiii_role_docker_volumes_default`"

        ```yaml
        # Type: list
        fireflyiii_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='fireflyiii') }}/upload:/var/www/html/storage/upload"
          - /etc/timezone:/etc/timezone:ro
          - /etc/localtime:/etc/localtime:ro
        ```

    ??? variable list "`fireflyiii_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        fireflyiii_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`fireflyiii_role_docker_hostname`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_hostname: "{{ fireflyiii_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`fireflyiii_role_docker_networks_alias`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_networks_alias: "{{ fireflyiii_name }}"
        ```

    ??? variable list "`fireflyiii_role_docker_networks_default`"

        ```yaml
        # Type: list
        fireflyiii_role_docker_networks_default: []
        ```

    ??? variable list "`fireflyiii_role_docker_networks_custom`"

        ```yaml
        # Type: list
        fireflyiii_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`fireflyiii_role_docker_restart_policy`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`fireflyiii_role_docker_state`"

        ```yaml
        # Type: string
        fireflyiii_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`fireflyiii_role_depends_on`"

        ```yaml
        # Type: string
        fireflyiii_role_depends_on: "{{ fireflyiii_name }}-mariadb"
        ```

    ??? variable string "`fireflyiii_role_depends_on_delay`"

        ```yaml
        # Type: string
        fireflyiii_role_depends_on_delay: "0"
        ```

    ??? variable string "`fireflyiii_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        fireflyiii_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`fireflyiii_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        fireflyiii_role_autoheal_enabled: true
        ```

    ??? variable string "`fireflyiii_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        fireflyiii_role_depends_on: ""
        ```

    ??? variable string "`fireflyiii_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        fireflyiii_role_depends_on_delay: "0"
        ```

    ??? variable string "`fireflyiii_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        fireflyiii_role_depends_on_healthchecks:
        ```

    ??? variable bool "`fireflyiii_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        fireflyiii_role_diun_enabled: true
        ```

    ??? variable bool "`fireflyiii_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        fireflyiii_role_dns_enabled: true
        ```

    ??? variable bool "`fireflyiii_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        fireflyiii_role_docker_controller: true
        ```

    ??? variable bool "`fireflyiii_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        fireflyiii_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`fireflyiii_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        fireflyiii_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`fireflyiii_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        fireflyiii_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`fireflyiii_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        fireflyiii_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`fireflyiii_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`fireflyiii_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        fireflyiii_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`fireflyiii_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        fireflyiii_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`fireflyiii_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        fireflyiii_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`fireflyiii_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        fireflyiii_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`fireflyiii_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        fireflyiii_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            fireflyiii_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "fireflyiii2.{{ user.domain }}"
              - "fireflyiii.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`fireflyiii_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        fireflyiii_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            fireflyiii_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'fireflyiii2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`fireflyiii_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        fireflyiii_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->