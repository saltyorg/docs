---
hide:
  - tags
tags:
  - authelia
---

# Authelia

# What is it?

[Authelia](https://www.authelia.com/) (Authelia) is an open-source authentication and authorization server and portal fulfilling the identity and access management (IAM) role of information security in providing multi-factor authentication and single sign-on (SSO) for your applications via a web portal.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://authelia.com){: .header-icons } | [:octicons-link-16: Docs](https://www.authelia.com/configuration/prologue/introduction/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/authelia/authelia){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/authelia/authelia){: .header-icons }|

## 2. URL

To access Authelia, visit `https://login._yourdomain_.com` or the subdomain set for Authelia in [settings.yml](../reference/accounts.md#options-in-settingsyml). This merely presents a simple login page where a user can configure Two Factor Authentication if Authelia is configured to accept/require 2FA.

## 3. Settings

Saltbox offers several options to customize the `configuration.yml` via the inventory system. We recommend reviewing the [configuration template](https://github.com/saltyorg/Saltbox/blob/master/roles/authelia/templates/configuration.yml.j2) and the [default variables](https://github.com/saltyorg/Saltbox/blob/master/roles/authelia/defaults/main.yml). It is highly recommended to review the upstream documentation for configuration options.

Some of the features that can be enabled are Two Factor Authentication, Duo notifications and SMTP notifications.

## 4. LDAP Authentication

Saltbox offers an optional LDAP authentication backend for Authelia. This can be enabled by setting `authelia_authentication_backend: "ldap"` in your inventory file. The LDAP is provisioned via OpenLDAP and includes phpLDAPadmin.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        authelia_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    authelia_name: authelia

    ```

??? example "Settings"

    ```yaml
    # Options are light, dark, grey or auto.
    # Type: string
    authelia_role_theme: "auto"

    # Logs
    # Type: string
    authelia_role_log_max_backups: "3"

    # Type: string
    authelia_role_log_max_size: "10"

    # Options are file or ldap
    # Type: string
    authelia_role_authentication_backend: "file"

    # Type: bool (true/false)
    authelia_role_authentication_backend_password_change_disable: false

    # Type: string
    authelia_role_authentication_backend_password_reset_disable: "false"

    # Type: string
    authelia_role_authentication_backend_password_reset_custom_url: ""

    # Type: string
    authelia_role_authentication_backend_refresh_interval: "5m"

    # Type: string
    authelia_role_authentication_backend_file_path: "/config/users_database.yml"

    # Type: string
    authelia_role_authentication_backend_file_watch: "true"

    # Type: string
    authelia_role_authentication_backend_file_password_algorithm: "argon2"

    # Type: string
    authelia_role_authentication_backend_file_password_argon2_variant: "argon2id"

    # Type: string
    authelia_role_authentication_backend_file_password_argon2_iterations: "3"

    # Type: string
    authelia_role_authentication_backend_file_password_argon2_memory: "65536"

    # Type: string
    authelia_role_authentication_backend_file_password_argon2_parallelism: "4"

    # Type: string
    authelia_role_authentication_backend_file_password_argon2_key_length: "32"

    # Type: string
    authelia_role_authentication_backend_file_password_argon2_salt_length: "16"

    # Setting for default Access Control Policy - recommended options one_factor or two_factor
    # Reference: https://www.authelia.com/configuration/security/access-control/#one_factor
    # Type: string
    authelia_role_access_control_policy: "one_factor"

    # Settings for Duo
    # Reference: https://www.authelia.com/configuration/second-factor/duo/
    # Type: bool (true/false)
    authelia_role_duo_enabled: false

    # Type: string
    authelia_role_duo_hostname: ""

    # Type: string
    authelia_role_duo_integration_key: ""

    # Type: string
    authelia_role_duo_secret_key: ""

    # Type: string
    authelia_role_duo_self_enrollment: "true"

    # Settings for Webauthn
    # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
    # Type: bool (true/false)
    authelia_role_webauthn_disable: false

    # Type: bool (true/false)
    authelia_role_webauthn_enable_passkey_login: false

    # Type: string
    authelia_role_webauthn_display_name: "Authelia"

    # Type: string
    authelia_role_webauthn_attestation_conveyance_preference: "indirect"

    # Type: string
    authelia_role_webauthn_timeout: "60s"

    # Type: bool (true/false)
    authelia_role_webauthn_filtering_prohibit_backup_eligibility: false

    # Type: list
    authelia_role_webauthn_filtering_permitted_aaguids: []

    # Type: list
    authelia_role_webauthn_filtering_prohibited_aaguids: []

    # Type: string
    authelia_role_webauthn_selection_criteria_attachment: "cross-platform"

    # Type: string
    authelia_role_webauthn_selection_criteria_discoverability: "discouraged"

    # Type: string
    authelia_role_webauthn_selection_criteria_user_verification: "preferred"

    # Type: bool (true/false)
    authelia_role_webauthn_metadata_enabled: false

    # Type: string
    authelia_role_webauthn_metadata_cache_policy: "strict"

    # Type: bool (true/false)
    authelia_role_webauthn_metadata_validate_trust_anchor: true

    # Type: bool (true/false)
    authelia_role_webauthn_metadata_validate_entry: true

    # Type: bool (true/false)
    authelia_role_webauthn_metadata_validate_entry_permit_zero_aaguid: false

    # Type: bool (true/false)
    authelia_role_webauthn_metadata_validate_status: true

    # Type: list
    authelia_role_webauthn_metadata_validate_status_permitted: []

    # Type: list
    authelia_role_webauthn_metadata_validate_status_prohibited: []

    # Settings for Notifier
    # Reference: https://www.authelia.com/configuration/notifications/introduction/
    # Options are filesystem or smtp. Options specific to smtp prefixed with smtp
    # Type: string
    authelia_role_notifier: "filesystem"

    # Type: string
    authelia_role_notifier_disable_startup_check: "false"

    # Type: string
    authelia_role_notifier_smtp_host: ""

    # Type: string
    authelia_role_notifier_smtp_port: ""

    # Type: string
    authelia_role_notifier_smtp_timeout: ""

    # Type: string
    authelia_role_notifier_smtp_username: ""

    # Type: string
    authelia_role_notifier_smtp_password: ""

    # Type: string
    authelia_role_notifier_smtp_sender: ""

    # Type: string
    authelia_role_notifier_smtp_identifier: ""

    # Type: string
    authelia_role_notifier_smtp_subject: ""

    # Type: string
    authelia_role_notifier_smtp_startup_check_address: ""

    # Type: string
    authelia_role_notifier_smtp_disable_require_tls: ""

    # Type: string
    authelia_role_notifier_smtp_disable_html_emails: ""

    # Type: string
    authelia_role_notifier_smtp_tls_server_name: ""

    # Type: string
    authelia_role_notifier_smtp_tls_skip_verify: ""

    # Type: string
    authelia_role_notifier_smtp_tls_minimum_version: ""

    # Settings for Authelia's server
    # Reference: https://www.authelia.com/configuration/miscellaneous/server/
    # Type: string
    authelia_role_server_address: "0.0.0.0:9091"

    # Type: string
    authelia_role_server_asset_path: ""

    # Type: string
    authelia_role_server_disable_healthcheck: "false"

    # Type: string
    authelia_role_server_buffers_read: "10485760"

    # Type: string
    authelia_role_server_buffers_write: "10485760"

    # Type: string
    authelia_role_server_timeouts_read: "6s"

    # Type: string
    authelia_role_server_timeouts_write: "6s"

    # Type: string
    authelia_role_server_timeouts_idle: "30s"

    # Type: string
    authelia_role_server_endpoints_enable_pprof: "false"

    # Type: string
    authelia_role_server_endpoints_enable_expvars: "false"

    # Type: string
    authelia_role_server_headers_csp_template: "default-src 'self' *.{{ user.domain }} {{ user.domain }}; script-src 'self' *.{{ user.domain }} {{ user.domain }}; script-src-elem 'self' *.{{ user.domain }} {{ user.domain }}; script-src-attr 'self' *.{{ user.domain }} {{ user.domain }}; style-src 'self' *.{{ user.domain }} {{ user.domain }} 'nonce-${NONCE}'; style-src-elem 'self' *.{{ user.domain }} {{ user.domain }} 'nonce-${NONCE}'; style-src-attr 'self' *.{{ user.domain }} {{ user.domain }} 'nonce-${NONCE}'; img-src 'self' *.{{ user.domain }} {{ user.domain }}; font-src 'self' *.{{ user.domain }} {{ user.domain }}; connect-src 'self' *.{{ user.domain }} {{ user.domain }}; media-src 'self' *.{{ user.domain }} {{ user.domain }}; object-src 'self' *.{{ user.domain }} {{ user.domain }}; child-src 'self' *.{{ user.domain }} {{ user.domain }}; frame-src 'self' *.{{ user.domain }} {{ user.domain }}; worker-src 'self' *.{{ user.domain }} {{ user.domain }}; frame-ancestors 'self' *.{{ user.domain }} {{ user.domain }}; form-action 'self' *.{{ user.domain }} {{ user.domain }}; base-uri 'self'"

    # Settings for Logging
    # Reference: https://www.authelia.com/configuration/miscellaneous/logging/
    # Type: string
    authelia_role_log_level: "info"

    # Type: string
    authelia_role_log_format: "text"

    # Type: string
    authelia_role_log_file_path: "/config/authelia.log"

    # Type: string
    authelia_role_log_keep_stdout: "true"

    # Settings for Telemetry/Metrics
    # Reference: https://www.authelia.com/configuration/telemetry/metrics/
    # Type: bool (true/false)
    authelia_role_telemetry_metrics_enabled: false

    # Type: string
    authelia_role_telemetry_metrics_address: "tcp://0.0.0.0:9959"

    # Type: string
    authelia_role_telemetry_metrics_buffers_read: "4096"

    # Type: string
    authelia_role_telemetry_metrics_buffers_write: "4096"

    # Type: string
    authelia_role_telemetry_metrics_timeouts_read: "6s"

    # Type: string
    authelia_role_telemetry_metrics_timeouts_write: "6s"

    # Type: string
    authelia_role_telemetry_metrics_timeouts_idle: "30s"

    # Identity Validation Settings
    # Reset password flow
    # Type: string
    authelia_role_identity_validation_reset_password_jwt_lifespan: "5m"

    # Type: string
    authelia_role_identity_validation_reset_password_jwt_algorithm: "HS256"

    # Elevated session flows
    # Type: string
    authelia_role_identity_validation_elevated_session_code_lifespan: "5m"

    # Type: string
    authelia_role_identity_validation_elevated_session_elevation_lifespan: "10m"

    # Type: string
    authelia_role_identity_validation_elevated_session_characters: "8"

    # Type: bool (true/false)
    authelia_role_identity_validation_elevated_session_require_second_factor: false

    # Type: bool (true/false)
    authelia_role_identity_validation_elevated_session_skip_second_factor: false

    # JWT
    # Type: string
    authelia_role_jwt_secret: "{{ lookup('password', '/dev/null', chars=['ascii_letters', 'digits'], length=32) }}"

    # TOTP
    # Type: bool (true/false)
    authelia_role_totp_disable: false

    # Type: string
    authelia_role_totp_issuer: "{{ lookup('role_var', '_web_subdomain', role='authelia') + '.' + lookup('role_var', '_web_domain', role='authelia') }}"

    # Type: string
    authelia_role_totp_algorithm: "SHA1"

    # Type: string
    authelia_role_totp_digits: "6"

    # Type: string
    authelia_role_totp_period: "30"

    # Type: string
    authelia_role_totp_skew: "1"

    # Type: string
    authelia_role_totp_secret_size: "32"

    # Type: list
    authelia_role_totp_allowed_algorithms: ["SHA1"]

    # Type: list
    authelia_role_totp_allowed_digits: ["6"]

    # Type: list
    authelia_role_totp_allowed_periods: ["30"]

    # Type: bool (true/false)
    authelia_role_totp_disable_reuse_security_policy: false

    # Default redirection
    # Type: string
    authelia_role_default_redirection_url: ""

    # Default 2FA Method
    # Type: string
    authelia_role_default_2fa_method: ""

    # NTP
    # Type: string
    authelia_role_ntp_address: "time.cloudflare.com:123"

    # Type: string
    authelia_role_ntp_version: "3"

    # Type: string
    authelia_role_ntp_max_desync: "3s"

    # Type: string
    authelia_role_ntp_disable_startup_check: "false"

    # Type: string
    authelia_role_ntp_disable_failure: "false"

    # Password Policy
    # Type: string
    authelia_role_password_policy_standard_enabled: "false"

    # Type: string
    authelia_role_password_policy_standard_min_length: "8"

    # Type: string
    authelia_role_password_policy_standard_max_length: "0"

    # Type: string
    authelia_role_password_policy_standard_require_uppercase: "true"

    # Type: string
    authelia_role_password_policy_standard_require_lowercase: "true"

    # Type: string
    authelia_role_password_policy_standard_require_number: "true"

    # Type: string
    authelia_role_password_policy_standard_require_special: "true"

    # Type: string
    authelia_role_password_policy_zxcvbn_enabled: "false"

    # Type: string
    authelia_role_password_policy_zxcvbn_min_score: "3"

    # Access Control
    # Type: bool (true/false)
    authelia_role_access_control_whitelist_host: false

    # Type: string
    authelia_role_access_control_default_policy: "deny"

    # Type: list
    authelia_role_access_control_rules: 
      - domain:
          - "{{ '*.' + user.domain | lower }}"
          - "{{ user.domain | lower }}"
        policy: "{{ lookup('role_var', '_access_control_policy', role='authelia') }}"

    # Type: string
    authelia_role_access_control_whitelist_rules_lookup: "{{ lookup('role_var', '_access_control_whitelist_rules', role='authelia') if lookup('role_var', '_access_control_whitelist_host', role='authelia') and (dns_ipv4_enabled or dns_ipv6_enabled) else [] }}"

    # Type: list
    authelia_role_access_control_whitelist_rules: 
      - domain:
          - "{{ '*.' + user.domain }}"
          - "{{ user.domain }}"
        policy: bypass
        networks: "{{ lookup('role_var', '_access_control_whitelist_networks', role='authelia') | unique | reject('equalto', omit) | list }}"

    # Type: list
    authelia_role_access_control_whitelist_networks: 
      - "{{ (ip_address_public + '/32') if dns_ipv4_enabled else omit }}"
      - "{{ (ipv6_address_public + '/128') if dns_ipv6_enabled else omit }}"

    # Type: list
    authelia_role_response_headers: 
      - "Remote-User"
      - "Remote-Groups"
      - "Remote-Name"
      - "Remote-Email"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    authelia_role_paths_folder: "{{ authelia_name }}"

    # Type: string
    authelia_role_paths_location: "{{ server_appdata_path }}/{{ authelia_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    authelia_role_web_subdomain: "{{ authelia.subdomain }}"

    # Type: string
    authelia_role_web_domain: "{{ user.domain }}"

    # Type: string
    authelia_role_web_port: "9091"

    # Type: string
    authelia_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='authelia') + '.' + lookup('role_var', '_web_domain', role='authelia')
                            if (lookup('role_var', '_web_subdomain', role='authelia') | length > 0)
                            else lookup('role_var', '_web_domain', role='authelia')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    authelia_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='authelia') }}"

    # Type: string
    authelia_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='authelia') }}"

    # Type: bool (true/false)
    authelia_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    authelia_role_traefik_sso_middleware: ""

    # Type: string
    authelia_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    authelia_role_traefik_middleware_custom: ""

    # Type: string
    authelia_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    authelia_role_traefik_enabled: true

    # Type: bool (true/false)
    authelia_role_traefik_api_enabled: false

    # Type: string
    authelia_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    authelia_role_docker_container: "{{ authelia_name }}"

    # Image
    # Type: bool (true/false)
    authelia_role_docker_image_pull: true

    # Type: string
    authelia_role_docker_image_repo: "authelia/authelia"

    # Type: string
    authelia_role_docker_image_tag: "4.39"

    # Type: string
    authelia_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='authelia') }}:{{ lookup('role_var', '_docker_image_tag', role='authelia') }}"

    # Envs
    # Type: dict
    authelia_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    authelia_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    authelia_role_docker_volumes_default: 
      - "{{ authelia_role_paths_location }}:/config"

    # Type: list
    authelia_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    authelia_role_docker_hostname: "{{ authelia_name }}"

    # Networks
    # Type: string
    authelia_role_docker_networks_alias: "{{ authelia_name }}"

    # Type: list
    authelia_role_docker_networks_default: []

    # Type: list
    authelia_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    authelia_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    authelia_role_docker_state: started

    # Dependencies
    # Type: string
    authelia_role_depends_on: "{{ 'authelia-redis,lldap' if (lookup('role_var', '_authentication_backend', role='authelia') == 'ldap') else 'authelia-redis' }}"

    # Type: string
    authelia_role_depends_on_delay: "0"

    # Type: string
    authelia_role_depends_on_healthchecks: "{{ 'true' if (lookup('role_var', '_authentication_backend', role='authelia') == 'ldap') else 'false' }}"


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    authelia_role_docker_blkio_weight:

    # Type: int
    authelia_role_docker_cpu_period:

    # Type: int
    authelia_role_docker_cpu_quota:

    # Type: int
    authelia_role_docker_cpu_shares:

    # Type: string
    authelia_role_docker_cpus:

    # Type: string
    authelia_role_docker_cpuset_cpus:

    # Type: string
    authelia_role_docker_cpuset_mems:

    # Type: string
    authelia_role_docker_kernel_memory:

    # Type: string
    authelia_role_docker_memory:

    # Type: string
    authelia_role_docker_memory_reservation:

    # Type: string
    authelia_role_docker_memory_swap:

    # Type: int
    authelia_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    authelia_role_docker_cap_drop:

    # Type: list
    authelia_role_docker_device_cgroup_rules:

    # Type: list
    authelia_role_docker_device_read_bps:

    # Type: list
    authelia_role_docker_device_read_iops:

    # Type: list
    authelia_role_docker_device_requests:

    # Type: list
    authelia_role_docker_device_write_bps:

    # Type: list
    authelia_role_docker_device_write_iops:

    # Type: list
    authelia_role_docker_devices:

    # Type: string
    authelia_role_docker_devices_default:

    # Type: bool (true/false)
    authelia_role_docker_privileged:

    # Type: list
    authelia_role_docker_security_opts:


    # Networking
    # Type: list
    authelia_role_docker_dns_opts:

    # Type: list
    authelia_role_docker_dns_search_domains:

    # Type: list
    authelia_role_docker_dns_servers:

    # Type: dict
    authelia_role_docker_hosts:

    # Type: string
    authelia_role_docker_hosts_use_common:

    # Type: string
    authelia_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    authelia_role_docker_keep_volumes:

    # Type: list
    authelia_role_docker_mounts:

    # Type: string
    authelia_role_docker_volume_driver:

    # Type: list
    authelia_role_docker_volumes_from:

    # Type: string
    authelia_role_docker_volumes_global:

    # Type: string
    authelia_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    authelia_role_docker_healthcheck:

    # Type: bool (true/false)
    authelia_role_docker_init:

    # Type: string
    authelia_role_docker_log_driver:

    # Type: dict
    authelia_role_docker_log_options:

    # Type: bool (true/false)
    authelia_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    authelia_role_docker_auto_remove:

    # Type: list
    authelia_role_docker_capabilities:

    # Type: string
    authelia_role_docker_cgroup_parent:

    # Type: string
    authelia_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    authelia_role_docker_cleanup:

    # Type: list
    authelia_role_docker_commands:

    # Type: string
    authelia_role_docker_create_timeout:

    # Type: string
    authelia_role_docker_domainname:

    # Type: string
    authelia_role_docker_entrypoint:

    # Type: string
    authelia_role_docker_env_file:

    # Type: list
    authelia_role_docker_exposed_ports:

    # Type: string
    authelia_role_docker_force_kill:

    # Type: list
    authelia_role_docker_groups:

    # Type: int
    authelia_role_docker_healthy_wait_timeout:

    # Type: string
    authelia_role_docker_ipc_mode:

    # Type: string
    authelia_role_docker_kill_signal:

    # Type: dict
    authelia_role_docker_labels:

    # Type: string
    authelia_role_docker_labels_use_common:

    # Type: list
    authelia_role_docker_links:

    # Type: bool (true/false)
    authelia_role_docker_oom_killer:

    # Type: int
    authelia_role_docker_oom_score_adj:

    # Type: bool (true/false)
    authelia_role_docker_paused:

    # Type: string
    authelia_role_docker_pid_mode:

    # Type: list
    authelia_role_docker_ports:

    # Type: bool (true/false)
    authelia_role_docker_read_only:

    # Type: bool (true/false)
    authelia_role_docker_recreate:

    # Type: int
    authelia_role_docker_restart_retries:

    # Type: string
    authelia_role_docker_runtime:

    # Type: string
    authelia_role_docker_shm_size:

    # Type: int
    authelia_role_docker_stop_timeout:

    # Type: dict
    authelia_role_docker_storage_opts:

    # Type: list
    authelia_role_docker_sysctls:

    # Type: list
    authelia_role_docker_tmpfs:

    # Type: list
    authelia_role_docker_ulimits:

    # Type: string
    authelia_role_docker_user:

    # Type: string
    authelia_role_docker_userns_mode:

    # Type: string
    authelia_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    authelia_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    authelia_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    authelia_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    authelia_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    authelia_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    authelia_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    authelia_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    authelia_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    authelia_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    authelia_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    authelia_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    authelia_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    authelia_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    authelia_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: string
    authelia_role_web_fqdn_override:

    # Override the Traefik web host configuration for the container
    # Type: string
    authelia_role_web_host_override:

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    authelia_role_web_scheme:

    ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
