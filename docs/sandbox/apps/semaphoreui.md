---
hide:
  - tags
tags:
  - semaphoreui
  - ansible
  - automation
---

# SemaphoreUI

## What is it?

[Semaphore UI](https://github.com/semaphoreui/semaphore) is a modern UI for Ansible, Terraform, OpenTofu and Pulumi. It lets you easily run Ansible playbooks, get notifications about fails, control access to deployment system.

If your project has grown and deploying from the terminal is no longer for you then Semaphore UI is what you need.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://semaphoreui.com){: .header-icons } | [:octicons-link-16: Docs](https://docs.semaphoreui.com/user-guide/projects){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/semaphoreui/semaphore?tab=readme-ov-file){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/semaphoreui/semaphore){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-semaphoreui

```

### 2. URL

- To access the Semaphore UI dashboard, visit `https://semaphoreui.xDOMAIN_NAMEx`

### 3. Setup

### 4. Additional Settings

The default installation utilises a seperate postgres database. There is an option for this package to utilise mariadb / mysql but this isnt what this guide will be based on.

To enable email notifications, set these [inventory](../../saltbox/inventory/index.md) entries to your desired values:

``` yaml title="Semaphoreui Email Settings"

SEMAPHORE_EMAIL_ALERT: "true" # (1)!
SEMAPHORE_EMAIL_SENDER: ""  # (2)!
SEMAPHORE_EMAIL_HOST: "localhost"  # (3)!¿˘˘˘˘˘˘˘˘˘¿¿˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘
SEMAPHORE_EMAIL_PORT: "25"  # (4)!¿˘˘˘˘˘˘
SEMAPHORE_EMAIL_USERNAME: ""  # (5)!
SEMAPHORE_EMAIL_PASSWORD: ""  # (6)!
SEMAPHORE_EMAIL_SECURE: ""  # (7)!
```

1. Flag which enables email alerts. Can be `true` or '`false`.
2. The email address you want to send to. Replace `""` with the email address you want to send to
3. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
4. Replace `25` with your email port. IE: `587`
5. Replace `""` with your email username if necessary.
6. Replace `""` with your email password if necessary.
7. Use `SSL` or `TLS` for communication with the SMTP server. Can be `true` or '`false`.

``` yaml title="Semaphoreui Telgram Settings"

SEMAPHORE_TELEGRAM_ALERT: ""  # (1)!
SEMAPHORE_TELEGRAM_CHAT: ""  # (2)!
SEMAPHORE_TELEGRAM_TOKEN: ""  # (3)!
```

1. Flag which enables telegram alerts. Can be `true` or '`false`.
2. The chat id of which you want to send the message to
3. Your Telegram bot token

``` yaml title="Semaphoreui Telgram Settings"

SEMAPHORE_SLACK_ALERT: ""  # (1)!
SEMAPHORE_SLACK_URL: ""  # (2)!
```

1. Flag which enables telegram alerts. Can be `true` or '`false`.
2. Your slack URL

Redeploy the Semaphoreui role to apply any of the above changes.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        semaphoreui_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `semaphoreui_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `semaphoreui_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    semaphoreui_name: semaphoreui

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    semaphoreui_role_postgres_deploy: true

    # Type: string
    semaphoreui_role_postgres_name: "{{ semaphoreui_name }}-postgres"

    # Type: string
    semaphoreui_role_postgres_user: "semaphoreui"

    # Type: string
    semaphoreui_role_postgres_password: "semaphoreui"

    # Type: string
    semaphoreui_role_postgres_docker_env_db: "semaphoreui"

    # Type: string
    semaphoreui_role_postgres_docker_image_tag: "15"

    # Type: string
    semaphoreui_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    semaphoreui_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='semaphoreui') }} -U {{ lookup('role_var', '_postgres_user', role='semaphoreui') }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    semaphoreui_role_postgres_paths_folder: "{{ semaphoreui_name }}"

    # Type: string
    semaphoreui_role_postgres_paths_location: "{{ server_appdata_path }}/{{ semaphoreui_role_postgres_paths_folder }}/postgres"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    semaphoreui_role_paths_folder: "{{ semaphoreui_name }}"

    # Type: string
    semaphoreui_role_paths_location: "{{ server_appdata_path }}/{{ semaphoreui_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    semaphoreui_role_web_subdomain: "{{ semaphoreui_name }}"

    # Type: string
    semaphoreui_role_web_domain: "{{ user.domain }}"

    # Type: string
    semaphoreui_role_web_port: "3000"

    # Type: string
    semaphoreui_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='semaphoreui') + '.' + lookup('role_var', '_web_domain', role='semaphoreui')
                               if (lookup('role_var', '_web_subdomain', role='semaphoreui') | length > 0)
                               else lookup('role_var', '_web_domain', role='semaphoreui')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    semaphoreui_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='semaphoreui') }}"

    # Type: string
    semaphoreui_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='semaphoreui') }}"

    # Type: bool (true/false)
    semaphoreui_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    semaphoreui_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    semaphoreui_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    semaphoreui_role_traefik_middleware_custom: ""

    # Type: string
    semaphoreui_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    semaphoreui_role_traefik_enabled: true

    # Type: bool (true/false)
    semaphoreui_role_traefik_api_enabled: true

    # Type: string
    semaphoreui_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    semaphoreui_role_docker_container: "{{ semaphoreui_name }}"

    # Image
    # Type: bool (true/false)
    semaphoreui_role_docker_image_pull: true

    # Type: string
    semaphoreui_role_docker_image_tag: "latest"

    # Type: string
    semaphoreui_role_docker_image_repo: "semaphoreui/semaphore"

    # Type: string
    semaphoreui_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='semaphoreui') }}:{{ lookup('role_var', '_docker_image_tag', role='semaphoreui') }}"

    # Envs
    # Type: dict
    semaphoreui_role_docker_envs_default: 
      SEMAPHORE_DB_USER: "{{ lookup('role_var', '_postgres_user', role='semaphoreui') }}"
      SEMAPHORE_DB_PASS: "{{ lookup('role_var', '_postgres_password', role='semaphoreui') }}"
      SEMAPHORE_DB_HOST: "{{ lookup('role_var', '_postgres_name', role='semaphoreui') }}"
      SEMAPHORE_DB_PORT: "5432"
      SEMAPHORE_DB_DIALECT: "postgres"
      SEMAPHORE_DB: "{{ lookup('role_var', '_postgres_docker_env_db', role='semaphoreui') }}"
      SEMAPHORE_PLAYBOOK_PATH: "{{ lookup('role_var', '_paths_location', role='semaphoreui') }}/playbooks"
      SEMAPHORE_ADMIN_PASSWORD: "{{ user.pass }}"
      SEMAPHORE_ADMIN_NAME: "{{ user.name }}"
      SEMAPHORE_ADMIN_EMAIL: "{{ user.email }}"
      SEMAPHORE_ADMIN: "{{ user.name }}"
      SEMAPHORE_ACCESS_KEY_ENCRYPTION: "{{ semaphoreui_saltbox_facts.facts.secret_key }}"
      TZ: "{{ timezone }}"

    # Type: dict
    semaphoreui_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    semaphoreui_role_docker_hostname: "{{ semaphoreui_name }}"

    # Networks
    # Type: string
    semaphoreui_role_docker_networks_alias: "{{ semaphoreui_name }}"

    # Type: list
    semaphoreui_role_docker_networks_default: []

    # Type: list
    semaphoreui_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    semaphoreui_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    semaphoreui_role_docker_state: started

    # Dependencies
    # Type: string
    semaphoreui_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='semaphoreui') }}"

    # Type: string
    semaphoreui_role_depends_on_delay: "0"

    # Type: string
    semaphoreui_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    semaphoreui_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    semaphoreui_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    semaphoreui_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    semaphoreui_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    semaphoreui_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    semaphoreui_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    semaphoreui_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    semaphoreui_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    semaphoreui_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    semaphoreui_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    semaphoreui_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    semaphoreui_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    semaphoreui_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    semaphoreui_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    semaphoreui_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    semaphoreui_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    semaphoreui_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        semaphoreui_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "semaphoreui2.{{ user.domain }}"
          - "semaphoreui.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        semaphoreui_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'semaphoreui2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
