---
icon: material/docker
hide:
  - tags
tags:
  - authelia
---

# Authelia

## Overview

[Authelia](https://www.authelia.com/) (Authelia) is an open-source authentication and authorization server and portal fulfilling the identity and access management (IAM) role of information security in providing multi-factor authentication and single sign-on (SSO) for your applications via a web portal.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://authelia.com){: .header-icons } | [:octicons-link-16: Docs](https://www.authelia.com/configuration/prologue/introduction/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/authelia/authelia){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/authelia/authelia){: .header-icons }|

## 2. URL

To access Authelia, visit <https://login.iYOUR_DOMAIN_NAMEi> or the subdomain set for Authelia in [settings.yml](../reference/accounts.md#options-in-settingsyml). This merely presents a simple login page where a user can configure Two Factor Authentication if Authelia is configured to accept/require 2FA.

## 3. Settings

Saltbox offers several options to customize the `configuration.yml` via the inventory system. We recommend reviewing the [configuration template](https://github.com/saltyorg/Saltbox/blob/master/roles/authelia/templates/configuration.yml.j2) and the [default variables](https://github.com/saltyorg/Saltbox/blob/master/roles/authelia/defaults/main.yml). It is highly recommended to review the upstream documentation for configuration options.

Some of the features that can be enabled are Two Factor Authentication, Duo notifications and SMTP notifications.

## 4. LDAP Authentication

Saltbox offers an optional LDAP authentication backend for Authelia. This can be enabled by setting `authelia_authentication_backend: "ldap"` in your inventory file. The LDAP is provisioned via OpenLDAP and includes phpLDAPadmin.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    authelia_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `authelia_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `authelia_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`authelia_name`"

        ```yaml
        # Type: string
        authelia_name: authelia
        ```

=== "Settings"

    This section is organized into multiple subsections

    === "Themes"

        ??? variable string "`authelia_role_theme`"

            ```yaml
            # Options are light, dark, grey or auto.
            # Type: string
            authelia_role_theme: "auto"
            ```

    === "Logs"

        ??? variable string "`authelia_role_log_max_backups`"

            ```yaml
            # Logrotate configuration variable
            # Type: string
            authelia_role_log_max_backups: "3"
            ```

        ??? variable string "`authelia_role_log_max_size`"

            ```yaml
            # Logrotate configuration variable
            # Type: string
            authelia_role_log_max_size: "10"
            ```

        ??? variable string "`authelia_role_log_level`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/logging/
            # Type: string
            authelia_role_log_level: "info"
            ```

        ??? variable string "`authelia_role_log_format`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/logging/
            # Type: string
            authelia_role_log_format: "text"
            ```

        ??? variable string "`authelia_role_log_file_path`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/logging/
            # Type: string
            authelia_role_log_file_path: "/config/authelia.log"
            ```

        ??? variable bool "`authelia_role_log_keep_stdout`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/logging/
            # Type: bool (true/false)
            authelia_role_log_keep_stdout: true
            ```

    === "Authentication Backend"

        ??? variable string "`authelia_role_authentication_backend`"

            ```yaml
            # Options are file or ldap
            # Type: string
            authelia_role_authentication_backend: "file"
            ```

        ??? variable bool "`authelia_role_authentication_backend_password_change_disable`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: bool (true/false)
            authelia_role_authentication_backend_password_change_disable: false
            ```

        ??? variable bool "`authelia_role_authentication_backend_password_reset_disable`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: bool (true/false)
            authelia_role_authentication_backend_password_reset_disable: false
            ```

        ??? variable string "`authelia_role_authentication_backend_password_reset_custom_url`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_password_reset_custom_url: ""
            ```

        ??? variable string "`authelia_role_authentication_backend_refresh_interval`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_refresh_interval: "5m"
            ```

        ??? variable string "`authelia_role_authentication_backend_file_path`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_path: "/config/users_database.yml"
            ```

        ??? variable bool "`authelia_role_authentication_backend_file_watch`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: bool (true/false)
            authelia_role_authentication_backend_file_watch: true
            ```

        ??? variable string "`authelia_role_authentication_backend_file_password_algorithm`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_password_algorithm: "argon2"
            ```

        ??? variable string "`authelia_role_authentication_backend_file_password_argon2_variant`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_password_argon2_variant: "argon2id"
            ```

        ??? variable string "`authelia_role_authentication_backend_file_password_argon2_iterations`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_password_argon2_iterations: "3"
            ```

        ??? variable string "`authelia_role_authentication_backend_file_password_argon2_memory`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_password_argon2_memory: "65536"
            ```

        ??? variable string "`authelia_role_authentication_backend_file_password_argon2_parallelism`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_password_argon2_parallelism: "4"
            ```

        ??? variable string "`authelia_role_authentication_backend_file_password_argon2_key_length`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_password_argon2_key_length: "32"
            ```

        ??? variable string "`authelia_role_authentication_backend_file_password_argon2_salt_length`"

            ```yaml
            # https://www.authelia.com/configuration/first-factor/introduction/
            # https://www.authelia.com/configuration/first-factor/file/
            # Type: string
            authelia_role_authentication_backend_file_password_argon2_salt_length: "16"
            ```

    === "Access Control"

        ??? variable string "`authelia_role_access_control_policy`"

            ```yaml
            # Setting for default Access Control Policy - recommended options one_factor or two_factor
            # Reference: https://www.authelia.com/configuration/security/access-control/#one_factor
            # Type: string
            authelia_role_access_control_policy: "one_factor"
            ```

        ??? variable bool "`authelia_role_access_control_whitelist_host`"

            ```yaml
            # Whitelists the host IPv4/IPv6 addresses depending on which are enabled
            # Type: bool (true/false)
            authelia_role_access_control_whitelist_host: false
            ```

        ??? variable bool "`authelia_role_access_control_whitelist_docker`"

            ```yaml
            # Whitelists the saltbox Docker network IP subnet
            # Type: bool (true/false)
            authelia_role_access_control_whitelist_docker: false
            ```

    === "Second Factor"

        ??? variable string "`authelia_role_default_2fa_method`"

            ```yaml
            # Type: string
            authelia_role_default_2fa_method: ""
            ```

    === "Second Factor - Duo"

        ??? variable bool "`authelia_role_duo_enabled`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/duo/
            # Type: bool (true/false)
            authelia_role_duo_enabled: false
            ```

        ??? variable string "`authelia_role_duo_hostname`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/duo/
            # Type: string
            authelia_role_duo_hostname: ""
            ```

        ??? variable string "`authelia_role_duo_integration_key`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/duo/
            # Type: string
            authelia_role_duo_integration_key: ""
            ```

        ??? variable string "`authelia_role_duo_secret_key`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/duo/
            # Type: string
            authelia_role_duo_secret_key: ""
            ```

        ??? variable bool "`authelia_role_duo_self_enrollment`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/duo/
            # Type: bool (true/false)
            authelia_role_duo_self_enrollment: true
            ```

    === "Second Factor - Webauthn"

        ??? variable bool "`authelia_role_webauthn_disable`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_disable: false
            ```

        ??? variable bool "`authelia_role_webauthn_enable_passkey_login`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_enable_passkey_login: false
            ```

        ??? variable string "`authelia_role_webauthn_display_name`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: string
            authelia_role_webauthn_display_name: "Authelia"
            ```

        ??? variable string "`authelia_role_webauthn_attestation_conveyance_preference`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: string
            authelia_role_webauthn_attestation_conveyance_preference: "indirect"
            ```

        ??? variable string "`authelia_role_webauthn_timeout`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: string
            authelia_role_webauthn_timeout: "60s"
            ```

        ??? variable bool "`authelia_role_webauthn_filtering_prohibit_backup_eligibility`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_filtering_prohibit_backup_eligibility: false
            ```

        ??? variable list "`authelia_role_webauthn_filtering_permitted_aaguids`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: list
            authelia_role_webauthn_filtering_permitted_aaguids: []
            ```

        ??? variable list "`authelia_role_webauthn_filtering_prohibited_aaguids`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: list
            authelia_role_webauthn_filtering_prohibited_aaguids: []
            ```

        ??? variable string "`authelia_role_webauthn_selection_criteria_attachment`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: string
            authelia_role_webauthn_selection_criteria_attachment: "cross-platform"
            ```

        ??? variable string "`authelia_role_webauthn_selection_criteria_discoverability`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: string
            authelia_role_webauthn_selection_criteria_discoverability: "discouraged"
            ```

        ??? variable string "`authelia_role_webauthn_selection_criteria_user_verification`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: string
            authelia_role_webauthn_selection_criteria_user_verification: "preferred"
            ```

        ??? variable bool "`authelia_role_webauthn_metadata_enabled`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_metadata_enabled: false
            ```

        ??? variable string "`authelia_role_webauthn_metadata_cache_policy`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: string
            authelia_role_webauthn_metadata_cache_policy: "strict"
            ```

        ??? variable bool "`authelia_role_webauthn_metadata_validate_trust_anchor`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_metadata_validate_trust_anchor: true
            ```

        ??? variable bool "`authelia_role_webauthn_metadata_validate_entry`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_metadata_validate_entry: true
            ```

        ??? variable bool "`authelia_role_webauthn_metadata_validate_entry_permit_zero_aaguid`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_metadata_validate_entry_permit_zero_aaguid: false
            ```

        ??? variable bool "`authelia_role_webauthn_metadata_validate_status`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: bool (true/false)
            authelia_role_webauthn_metadata_validate_status: true
            ```

        ??? variable list "`authelia_role_webauthn_metadata_validate_status_permitted`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: list
            authelia_role_webauthn_metadata_validate_status_permitted: []
            ```

        ??? variable list "`authelia_role_webauthn_metadata_validate_status_prohibited`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/second-factor/webauthn/
            # Type: list
            authelia_role_webauthn_metadata_validate_status_prohibited: []
            ```

    === "Notifier"

        ??? variable string "`authelia_role_notifier`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Options are filesystem or smtp. Options specific to smtp prefixed with smtp
            # Type: string
            authelia_role_notifier: "filesystem"
            ```

        ??? variable bool "`authelia_role_notifier_disable_startup_check`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: bool (true/false)
            authelia_role_notifier_disable_startup_check: false
            ```

        ??? variable string "`authelia_role_notifier_smtp_host`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_host: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_port`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_port: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_timeout`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_timeout: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_username`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_username: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_password`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_password: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_sender`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_sender: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_identifier`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_identifier: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_subject`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_subject: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_startup_check_address`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_startup_check_address: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_disable_require_tls`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_disable_require_tls: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_disable_html_emails`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_disable_html_emails: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_tls_server_name`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_tls_server_name: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_tls_skip_verify`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_tls_skip_verify: ""
            ```

        ??? variable string "`authelia_role_notifier_smtp_tls_minimum_version`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/notifications/introduction/
            # Type: string
            authelia_role_notifier_smtp_tls_minimum_version: ""
            ```

    === "Server"

        ??? variable string "`authelia_role_server_address`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_address: "0.0.0.0:9091"
            ```

        ??? variable string "`authelia_role_server_asset_path`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_asset_path: ""
            ```

        ??? variable bool "`authelia_role_server_disable_healthcheck`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: bool (true/false)
            authelia_role_server_disable_healthcheck: false
            ```

        ??? variable string "`authelia_role_server_buffers_read`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_buffers_read: "10485760"
            ```

        ??? variable string "`authelia_role_server_buffers_write`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_buffers_write: "10485760"
            ```

        ??? variable string "`authelia_role_server_timeouts_read`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_timeouts_read: "6s"
            ```

        ??? variable string "`authelia_role_server_timeouts_write`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_timeouts_write: "6s"
            ```

        ??? variable string "`authelia_role_server_timeouts_idle`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_timeouts_idle: "30s"
            ```

        ??? variable bool "`authelia_role_server_endpoints_enable_pprof`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: bool (true/false)
            authelia_role_server_endpoints_enable_pprof: false
            ```

        ??? variable bool "`authelia_role_server_endpoints_enable_expvars`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: bool (true/false)
            authelia_role_server_endpoints_enable_expvars: false
            ```

        ??? variable string "`authelia_role_server_headers_csp_template`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/miscellaneous/server/
            # Type: string
            authelia_role_server_headers_csp_template: "default-src 'self' *.{{ user.domain }} {{ user.domain }}; script-src 'self' *.{{ user.domain }} {{ user.domain }}; script-src-elem 'self' *.{{ user.domain }} {{ user.domain }}; script-src-attr 'self' *.{{ user.domain }} {{ user.domain }}; style-src 'self' *.{{ user.domain }} {{ user.domain }} 'nonce-${NONCE}'; style-src-elem 'self' *.{{ user.domain }} {{ user.domain }} 'nonce-${NONCE}'; style-src-attr 'self' *.{{ user.domain }} {{ user.domain }} 'nonce-${NONCE}'; img-src 'self' *.{{ user.domain }} {{ user.domain }}; font-src 'self' *.{{ user.domain }} {{ user.domain }}; connect-src 'self' *.{{ user.domain }} {{ user.domain }}; media-src 'self' *.{{ user.domain }} {{ user.domain }}; object-src 'self' *.{{ user.domain }} {{ user.domain }}; child-src 'self' *.{{ user.domain }} {{ user.domain }}; frame-src 'self' *.{{ user.domain }} {{ user.domain }}; worker-src 'self' *.{{ user.domain }} {{ user.domain }}; frame-ancestors 'self' *.{{ user.domain }} {{ user.domain }}; form-action 'self' *.{{ user.domain }} {{ user.domain }}; base-uri 'self'"
            ```

    === "Metrics"

        ??? variable bool "`authelia_role_telemetry_metrics_enabled`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/telemetry/metrics/
            # Type: bool (true/false)
            authelia_role_telemetry_metrics_enabled: false
            ```

        ??? variable string "`authelia_role_telemetry_metrics_address`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/telemetry/metrics/
            # Type: string
            authelia_role_telemetry_metrics_address: "tcp://0.0.0.0:9959"
            ```

        ??? variable string "`authelia_role_telemetry_metrics_buffers_read`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/telemetry/metrics/
            # Type: string
            authelia_role_telemetry_metrics_buffers_read: "4096"
            ```

        ??? variable string "`authelia_role_telemetry_metrics_buffers_write`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/telemetry/metrics/
            # Type: string
            authelia_role_telemetry_metrics_buffers_write: "4096"
            ```

        ??? variable string "`authelia_role_telemetry_metrics_timeouts_read`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/telemetry/metrics/
            # Type: string
            authelia_role_telemetry_metrics_timeouts_read: "6s"
            ```

        ??? variable string "`authelia_role_telemetry_metrics_timeouts_write`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/telemetry/metrics/
            # Type: string
            authelia_role_telemetry_metrics_timeouts_write: "6s"
            ```

        ??? variable string "`authelia_role_telemetry_metrics_timeouts_idle`"

            ```yaml
            # Reference: https://www.authelia.com/configuration/telemetry/metrics/
            # Type: string
            authelia_role_telemetry_metrics_timeouts_idle: "30s"
            ```

    === "Identity Validation"

        ??? variable string "`authelia_role_identity_validation_reset_password_jwt_lifespan`"

            ```yaml
            # Type: string
            authelia_role_identity_validation_reset_password_jwt_lifespan: "5m"
            ```

        ??? variable string "`authelia_role_identity_validation_reset_password_jwt_algorithm`"

            ```yaml
            # Type: string
            authelia_role_identity_validation_reset_password_jwt_algorithm: "HS256"
            ```

        ??? variable string "`authelia_role_identity_validation_elevated_session_code_lifespan`"

            ```yaml
            # Type: string
            authelia_role_identity_validation_elevated_session_code_lifespan: "5m"
            ```

        ??? variable string "`authelia_role_identity_validation_elevated_session_elevation_lifespan`"

            ```yaml
            # Type: string
            authelia_role_identity_validation_elevated_session_elevation_lifespan: "10m"
            ```

        ??? variable string "`authelia_role_identity_validation_elevated_session_characters`"

            ```yaml
            # Type: string
            authelia_role_identity_validation_elevated_session_characters: "8"
            ```

        ??? variable bool "`authelia_role_identity_validation_elevated_session_require_second_factor`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_identity_validation_elevated_session_require_second_factor: false
            ```

        ??? variable bool "`authelia_role_identity_validation_elevated_session_skip_second_factor`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_identity_validation_elevated_session_skip_second_factor: false
            ```

    === "JWT"

        ??? variable string "`authelia_role_jwt_secret`"

            ```yaml
            # Type: string
            authelia_role_jwt_secret: "{{ lookup('password', '/dev/null', chars=['ascii_letters', 'digits'], length=32) }}"
            ```

    === "TOTP"

        ??? variable bool "`authelia_role_totp_disable`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_totp_disable: false
            ```

        ??? variable string "`authelia_role_totp_issuer`"

            ```yaml
            # Type: string
            authelia_role_totp_issuer: "{{ lookup('role_var', '_web_subdomain', role='authelia') + '.' + lookup('role_var', '_web_domain', role='authelia') }}"
            ```

        ??? variable string "`authelia_role_totp_algorithm`"

            ```yaml
            # Type: string
            authelia_role_totp_algorithm: "SHA1"
            ```

        ??? variable string "`authelia_role_totp_digits`"

            ```yaml
            # Type: string
            authelia_role_totp_digits: "6"
            ```

        ??? variable string "`authelia_role_totp_period`"

            ```yaml
            # Type: string
            authelia_role_totp_period: "30"
            ```

        ??? variable string "`authelia_role_totp_skew`"

            ```yaml
            # Type: string
            authelia_role_totp_skew: "1"
            ```

        ??? variable string "`authelia_role_totp_secret_size`"

            ```yaml
            # Type: string
            authelia_role_totp_secret_size: "32"
            ```

        ??? variable list "`authelia_role_totp_allowed_algorithms`"

            ```yaml
            # Type: list
            authelia_role_totp_allowed_algorithms: ["SHA1"]
            ```

        ??? variable list "`authelia_role_totp_allowed_digits`"

            ```yaml
            # Type: list
            authelia_role_totp_allowed_digits: ["6"]
            ```

        ??? variable list "`authelia_role_totp_allowed_periods`"

            ```yaml
            # Type: list
            authelia_role_totp_allowed_periods: ["30"]
            ```

        ??? variable bool "`authelia_role_totp_disable_reuse_security_policy`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_totp_disable_reuse_security_policy: false
            ```

    === "Session"

        ??? variable string "`authelia_role_default_redirection_url`"

            ```yaml
            # Type: string
            authelia_role_default_redirection_url: ""
            ```

    === "NTP"

        ??? variable string "`authelia_role_ntp_address`"

            ```yaml
            # Type: string
            authelia_role_ntp_address: "time.cloudflare.com:123"
            ```

        ??? variable string "`authelia_role_ntp_version`"

            ```yaml
            # Type: string
            authelia_role_ntp_version: "3"
            ```

        ??? variable string "`authelia_role_ntp_max_desync`"

            ```yaml
            # Type: string
            authelia_role_ntp_max_desync: "3s"
            ```

        ??? variable bool "`authelia_role_ntp_disable_startup_check`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_ntp_disable_startup_check: false
            ```

        ??? variable bool "`authelia_role_ntp_disable_failure`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_ntp_disable_failure: false
            ```

    === "Password Policy"

        ??? variable bool "`authelia_role_password_policy_standard_enabled`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_password_policy_standard_enabled: false
            ```

        ??? variable string "`authelia_role_password_policy_standard_min_length`"

            ```yaml
            # Type: string
            authelia_role_password_policy_standard_min_length: "8"
            ```

        ??? variable string "`authelia_role_password_policy_standard_max_length`"

            ```yaml
            # Type: string
            authelia_role_password_policy_standard_max_length: "0"
            ```

        ??? variable bool "`authelia_role_password_policy_standard_require_uppercase`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_password_policy_standard_require_uppercase: true
            ```

        ??? variable bool "`authelia_role_password_policy_standard_require_lowercase`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_password_policy_standard_require_lowercase: true
            ```

        ??? variable bool "`authelia_role_password_policy_standard_require_number`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_password_policy_standard_require_number: true
            ```

        ??? variable bool "`authelia_role_password_policy_standard_require_special`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_password_policy_standard_require_special: true
            ```

        ??? variable bool "`authelia_role_password_policy_zxcvbn_enabled`"

            ```yaml
            # Type: bool (true/false)
            authelia_role_password_policy_zxcvbn_enabled: false
            ```

        ??? variable string "`authelia_role_password_policy_zxcvbn_min_score`"

            ```yaml
            # Type: string
            authelia_role_password_policy_zxcvbn_min_score: "3"
            ```

=== "Paths"

    ??? variable string "`authelia_role_paths_folder`"

        ```yaml
        # Type: string
        authelia_role_paths_folder: "{{ authelia_name }}"
        ```

    ??? variable string "`authelia_role_paths_location`"

        ```yaml
        # Type: string
        authelia_role_paths_location: "{{ server_appdata_path }}/{{ authelia_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`authelia_role_web_subdomain`"

        ```yaml
        # Type: string
        authelia_role_web_subdomain: "{{ authelia.subdomain }}"
        ```

    ??? variable string "`authelia_role_web_domain`"

        ```yaml
        # Type: string
        authelia_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`authelia_role_web_port`"

        ```yaml
        # Type: string
        authelia_role_web_port: "9091"
        ```

    ??? variable string "`authelia_role_web_url`"

        ```yaml
        # Type: string
        authelia_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='authelia') + '.' + lookup('role_var', '_web_domain', role='authelia')
                                if (lookup('role_var', '_web_subdomain', role='authelia') | length > 0)
                                else lookup('role_var', '_web_domain', role='authelia')) }}"
        ```

=== "DNS"

    ??? variable string "`authelia_role_dns_record`"

        ```yaml
        # Type: string
        authelia_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='authelia') }}"
        ```

    ??? variable string "`authelia_role_dns_zone`"

        ```yaml
        # Type: string
        authelia_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='authelia') }}"
        ```

    ??? variable bool "`authelia_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`authelia_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        authelia_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`authelia_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        authelia_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`authelia_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        authelia_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`authelia_role_traefik_certresolver`"

        ```yaml
        # Type: string
        authelia_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`authelia_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_traefik_enabled: true
        ```

    ??? variable bool "`authelia_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_traefik_api_enabled: false
        ```

    ??? variable string "`authelia_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        authelia_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`authelia_role_docker_container`"

        ```yaml
        # Type: string
        authelia_role_docker_container: "{{ authelia_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`authelia_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_image_pull: true
        ```

    ??? variable string "`authelia_role_docker_image_repo`"

        ```yaml
        # Type: string
        authelia_role_docker_image_repo: "authelia/authelia"
        ```

    ??? variable string "`authelia_role_docker_image_tag`"

        ```yaml
        # Type: string
        authelia_role_docker_image_tag: "4.39"
        ```

    ??? variable string "`authelia_role_docker_image`"

        ```yaml
        # Type: string
        authelia_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='authelia') }}:{{ lookup('role_var', '_docker_image_tag', role='authelia') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`authelia_role_docker_envs_default`"

        ```yaml
        # Type: dict
        authelia_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`authelia_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        authelia_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`authelia_role_docker_volumes_default`"

        ```yaml
        # Type: list
        authelia_role_docker_volumes_default:
          - "{{ authelia_role_paths_location }}:/config"
        ```

    ??? variable list "`authelia_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        authelia_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`authelia_role_docker_hostname`"

        ```yaml
        # Type: string
        authelia_role_docker_hostname: "{{ authelia_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`authelia_role_docker_networks_alias`"

        ```yaml
        # Type: string
        authelia_role_docker_networks_alias: "{{ authelia_name }}"
        ```

    ??? variable list "`authelia_role_docker_networks_default`"

        ```yaml
        # Type: list
        authelia_role_docker_networks_default: []
        ```

    ??? variable list "`authelia_role_docker_networks_custom`"

        ```yaml
        # Type: list
        authelia_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`authelia_role_docker_restart_policy`"

        ```yaml
        # Type: string
        authelia_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`authelia_role_docker_state`"

        ```yaml
        # Type: string
        authelia_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`authelia_role_depends_on`"

        ```yaml
        # Type: string
        authelia_role_depends_on: "{{ 'authelia-redis,lldap' if (lookup('role_var', '_authentication_backend', role='authelia') == 'ldap') else 'authelia-redis' }}"
        ```

    ??? variable string "`authelia_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        authelia_role_depends_on_delay: "0"
        ```

    ??? variable string "`authelia_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        authelia_role_depends_on_healthchecks: "{{ 'true' if (lookup('role_var', '_authentication_backend', role='authelia') == 'ldap') else 'false' }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`authelia_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        authelia_role_docker_blkio_weight:
        ```

    ??? variable int "`authelia_role_docker_cpu_period`"

        ```yaml
        # Type: int
        authelia_role_docker_cpu_period:
        ```

    ??? variable int "`authelia_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        authelia_role_docker_cpu_quota:
        ```

    ??? variable int "`authelia_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        authelia_role_docker_cpu_shares:
        ```

    ??? variable string "`authelia_role_docker_cpus`"

        ```yaml
        # Type: string
        authelia_role_docker_cpus:
        ```

    ??? variable string "`authelia_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        authelia_role_docker_cpuset_cpus:
        ```

    ??? variable string "`authelia_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        authelia_role_docker_cpuset_mems:
        ```

    ??? variable string "`authelia_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        authelia_role_docker_kernel_memory:
        ```

    ??? variable string "`authelia_role_docker_memory`"

        ```yaml
        # Type: string
        authelia_role_docker_memory:
        ```

    ??? variable string "`authelia_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        authelia_role_docker_memory_reservation:
        ```

    ??? variable string "`authelia_role_docker_memory_swap`"

        ```yaml
        # Type: string
        authelia_role_docker_memory_swap:
        ```

    ??? variable int "`authelia_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        authelia_role_docker_memory_swappiness:
        ```

    ??? variable string "`authelia_role_docker_shm_size`"

        ```yaml
        # Type: string
        authelia_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`authelia_role_docker_cap_drop`"

        ```yaml
        # Type: list
        authelia_role_docker_cap_drop:
        ```

    ??? variable string "`authelia_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        authelia_role_docker_cgroupns_mode:
        ```

    ??? variable list "`authelia_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        authelia_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`authelia_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        authelia_role_docker_device_read_bps:
        ```

    ??? variable list "`authelia_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        authelia_role_docker_device_read_iops:
        ```

    ??? variable list "`authelia_role_docker_device_requests`"

        ```yaml
        # Type: list
        authelia_role_docker_device_requests:
        ```

    ??? variable list "`authelia_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        authelia_role_docker_device_write_bps:
        ```

    ??? variable list "`authelia_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        authelia_role_docker_device_write_iops:
        ```

    ??? variable list "`authelia_role_docker_devices`"

        ```yaml
        # Type: list
        authelia_role_docker_devices:
        ```

    ??? variable string "`authelia_role_docker_devices_default`"

        ```yaml
        # Type: string
        authelia_role_docker_devices_default:
        ```

    ??? variable list "`authelia_role_docker_groups`"

        ```yaml
        # Type: list
        authelia_role_docker_groups:
        ```

    ??? variable bool "`authelia_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_privileged:
        ```

    ??? variable list "`authelia_role_docker_security_opts`"

        ```yaml
        # Type: list
        authelia_role_docker_security_opts:
        ```

    ??? variable string "`authelia_role_docker_user`"

        ```yaml
        # Type: string
        authelia_role_docker_user:
        ```

    ??? variable string "`authelia_role_docker_userns_mode`"

        ```yaml
        # Type: string
        authelia_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`authelia_role_docker_dns_opts`"

        ```yaml
        # Type: list
        authelia_role_docker_dns_opts:
        ```

    ??? variable list "`authelia_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        authelia_role_docker_dns_search_domains:
        ```

    ??? variable list "`authelia_role_docker_dns_servers`"

        ```yaml
        # Type: list
        authelia_role_docker_dns_servers:
        ```

    ??? variable string "`authelia_role_docker_domainname`"

        ```yaml
        # Type: string
        authelia_role_docker_domainname:
        ```

    ??? variable list "`authelia_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        authelia_role_docker_exposed_ports:
        ```

    ??? variable dict "`authelia_role_docker_hosts`"

        ```yaml
        # Type: dict
        authelia_role_docker_hosts:
        ```

    ??? variable bool "`authelia_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_hosts_use_common:
        ```

    ??? variable string "`authelia_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        authelia_role_docker_ipc_mode:
        ```

    ??? variable list "`authelia_role_docker_links`"

        ```yaml
        # Type: list
        authelia_role_docker_links:
        ```

    ??? variable string "`authelia_role_docker_network_mode`"

        ```yaml
        # Type: string
        authelia_role_docker_network_mode:
        ```

    ??? variable string "`authelia_role_docker_pid_mode`"

        ```yaml
        # Type: string
        authelia_role_docker_pid_mode:
        ```

    ??? variable list "`authelia_role_docker_ports`"

        ```yaml
        # Type: list
        authelia_role_docker_ports:
        ```

    ??? variable string "`authelia_role_docker_uts`"

        ```yaml
        # Type: string
        authelia_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`authelia_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_keep_volumes:
        ```

    ??? variable list "`authelia_role_docker_mounts`"

        ```yaml
        # Type: list
        authelia_role_docker_mounts:
        ```

    ??? variable dict "`authelia_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        authelia_role_docker_storage_opts:
        ```

    ??? variable list "`authelia_role_docker_tmpfs`"

        ```yaml
        # Type: list
        authelia_role_docker_tmpfs:
        ```

    ??? variable string "`authelia_role_docker_volume_driver`"

        ```yaml
        # Type: string
        authelia_role_docker_volume_driver:
        ```

    ??? variable list "`authelia_role_docker_volumes_from`"

        ```yaml
        # Type: list
        authelia_role_docker_volumes_from:
        ```

    ??? variable bool "`authelia_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_volumes_global:
        ```

    ??? variable string "`authelia_role_docker_working_dir`"

        ```yaml
        # Type: string
        authelia_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`authelia_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_auto_remove:
        ```

    ??? variable bool "`authelia_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_cleanup:
        ```

    ??? variable string "`authelia_role_docker_force_kill`"

        ```yaml
        # Type: string
        authelia_role_docker_force_kill:
        ```

    ??? variable dict "`authelia_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        authelia_role_docker_healthcheck:
        ```

    ??? variable int "`authelia_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        authelia_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`authelia_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_init:
        ```

    ??? variable string "`authelia_role_docker_kill_signal`"

        ```yaml
        # Type: string
        authelia_role_docker_kill_signal:
        ```

    ??? variable string "`authelia_role_docker_log_driver`"

        ```yaml
        # Type: string
        authelia_role_docker_log_driver:
        ```

    ??? variable dict "`authelia_role_docker_log_options`"

        ```yaml
        # Type: dict
        authelia_role_docker_log_options:
        ```

    ??? variable bool "`authelia_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_oom_killer:
        ```

    ??? variable int "`authelia_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        authelia_role_docker_oom_score_adj:
        ```

    ??? variable bool "`authelia_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_output_logs:
        ```

    ??? variable bool "`authelia_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_paused:
        ```

    ??? variable bool "`authelia_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_recreate:
        ```

    ??? variable int "`authelia_role_docker_restart_retries`"

        ```yaml
        # Type: int
        authelia_role_docker_restart_retries:
        ```

    ??? variable int "`authelia_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        authelia_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`authelia_role_docker_capabilities`"

        ```yaml
        # Type: list
        authelia_role_docker_capabilities:
        ```

    ??? variable string "`authelia_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        authelia_role_docker_cgroup_parent:
        ```

    ??? variable list "`authelia_role_docker_commands`"

        ```yaml
        # Type: list
        authelia_role_docker_commands:
        ```

    ??? variable int "`authelia_role_docker_create_timeout`"

        ```yaml
        # Type: int
        authelia_role_docker_create_timeout:
        ```

    ??? variable string "`authelia_role_docker_entrypoint`"

        ```yaml
        # Type: string
        authelia_role_docker_entrypoint:
        ```

    ??? variable string "`authelia_role_docker_env_file`"

        ```yaml
        # Type: string
        authelia_role_docker_env_file:
        ```

    ??? variable dict "`authelia_role_docker_labels`"

        ```yaml
        # Type: dict
        authelia_role_docker_labels:
        ```

    ??? variable bool "`authelia_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_labels_use_common:
        ```

    ??? variable bool "`authelia_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_read_only:
        ```

    ??? variable string "`authelia_role_docker_runtime`"

        ```yaml
        # Type: string
        authelia_role_docker_runtime:
        ```

    ??? variable list "`authelia_role_docker_sysctls`"

        ```yaml
        # Type: list
        authelia_role_docker_sysctls:
        ```

    ??? variable list "`authelia_role_docker_ulimits`"

        ```yaml
        # Type: list
        authelia_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable string "`authelia_role_authentication_backend`"

        ```yaml
        # Type: string
        authelia_role_authentication_backend:
        ```

    ??? variable bool "`authelia_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        authelia_role_autoheal_enabled: true
        ```

    ??? variable string "`authelia_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        authelia_role_depends_on: ""
        ```

    ??? variable string "`authelia_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        authelia_role_depends_on_delay: "0"
        ```

    ??? variable string "`authelia_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        authelia_role_depends_on_healthchecks:
        ```

    ??? variable bool "`authelia_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        authelia_role_diun_enabled: true
        ```

    ??? variable bool "`authelia_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        authelia_role_dns_enabled: true
        ```

    ??? variable bool "`authelia_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        authelia_role_docker_controller: true
        ```

    ??? variable string "`authelia_role_docker_image_repo`"

        ```yaml
        # Type: string
        authelia_role_docker_image_repo:
        ```

    ??? variable string "`authelia_role_docker_image_tag`"

        ```yaml
        # Type: string
        authelia_role_docker_image_tag:
        ```

    ??? variable bool "`authelia_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_docker_volumes_download:
        ```

    ??? variable string "`authelia_role_themepark_addons`"

        ```yaml
        # Type: string
        authelia_role_themepark_addons:
        ```

    ??? variable string "`authelia_role_themepark_app`"

        ```yaml
        # Type: string
        authelia_role_themepark_app:
        ```

    ??? variable string "`authelia_role_themepark_theme`"

        ```yaml
        # Type: string
        authelia_role_themepark_theme:
        ```

    ??? variable dict/omit "`authelia_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        authelia_role_traefik_api_endpoint:
        ```

    ??? variable string "`authelia_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        authelia_role_traefik_api_middleware:
        ```

    ??? variable string "`authelia_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        authelia_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`authelia_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        authelia_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`authelia_role_traefik_certresolver`"

        ```yaml
        # Type: string
        authelia_role_traefik_certresolver:
        ```

    ??? variable bool "`authelia_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        authelia_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`authelia_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        authelia_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`authelia_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        authelia_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`authelia_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        authelia_role_traefik_middleware_http:
        ```

    ??? variable bool "`authelia_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`authelia_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        authelia_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`authelia_role_traefik_priority`"

        ```yaml
        # Type: string
        authelia_role_traefik_priority:
        ```

    ??? variable bool "`authelia_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        authelia_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`authelia_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        authelia_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`authelia_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        authelia_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`authelia_role_web_domain`"

        ```yaml
        # Type: string
        authelia_role_web_domain:
        ```

    ??? variable list "`authelia_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        authelia_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            authelia_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "authelia2.{{ user.domain }}"
              - "authelia.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`authelia_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        authelia_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            authelia_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'authelia2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`authelia_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        authelia_role_web_http_port:
        ```

    ??? variable string "`authelia_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        authelia_role_web_http_scheme:
        ```

    ??? variable dict/omit "`authelia_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        authelia_role_web_http_serverstransport:
        ```

    ??? variable string "`authelia_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        authelia_role_web_scheme:
        ```

    ??? variable dict/omit "`authelia_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        authelia_role_web_serverstransport:
        ```

    ??? variable string "`authelia_role_web_subdomain`"

        ```yaml
        # Type: string
        authelia_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->