---
icon: material/docker
hide:
  - tags
tags:
  - authentik
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.goauthentik.io/docs
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/beryju/authentik/tags
      type: docker
    - name: Community
      url: https://goauthentik.io/discord
      type: discord
  project_description:
    name: Authentik
    summary: |
      an open-source Identity Provider (IdP) and Single Sign-On (SSO) platform designed for self-hosting, enabling organizations to manage user authentication, authorization, and access controls with full control over their identity infrastructure.
    link: https://goauthentik.io/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Authentik

## Overview

[Authentik](https://goauthentik.io/) is an open-source Identity Provider (IdP) and Single Sign-On (SSO) platform designed for self-hosting, enabling organizations to manage user authentication, authorization, and access controls with full control over their identity infrastructure.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.goauthentik.io/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/beryju/authentik/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://goauthentik.io/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

!!! info

    ```yaml title="Default Login"
        user: saltbox_user # (1)!
        password: saltbox_password # (2)!
    ```

    1. Replace `saltbox_user` with the username you set when installing Saltbox.
    2. Replace `saltbox_password` with the password you set when installing Saltbox.

To enable Authentik with a single container, or on a per role basis, set the following [inventory](../saltbox/inventory/index.md) entry:

```yaml title="Authentik Single Container Toggle"
radarr_traefik_sso_middleware: "authentik@docker"
```

To enable Authentik globally, set the following [inventory](../saltbox/inventory/index.md) entry:

```yaml title="Authentik Global Toggle"
traefik_default_sso_middleware: "authentik@docker"
```

You would use one or the other, the global toggle will install Authentik together with Traefik when it is being installed, the role toggle requires manually installing Authentik. Traefik needs to be reinstalled at least once after updating to deploy the Authentik middleware to enable use of it. If you are using the global toggle, you will need to reinstall all of the other roles you use to enable Authentik.

To set up Authentik similarly to how we have [Authelia](../apps/authelia.md) set up, follow these steps:

After logging in, you will be greeted with the dashboard. Click on the `Admin Interface` button in the top right corner.

Click on the `Flows and Stages` drop down and select `Stages`.

Locate the `default-authentication-login` stage and click the `Edit` button. (Far right)

- Below you will see the default User Login Stage info.

    ![Defaults](../images/authentik/authentik-user-auth-default-screenshot.png)

You can change these values to anything you want, but for this example, we will change the `Session Duration` to `minutes=30` and the `Stay Signed in Offset` to `weeks=2`.

- Below you will see the updated User Login Stage info.

    ![Altered](../images/authentik/authentik-user-auth-updated-screenshot.png)

### Additional Settings

To enable email notifications, set these [inventory](../saltbox/inventory/index.md) entries to your desired values:

```yaml title="Authentik Email Settings"
authentik_email_host: "localhost" # (1)!
authentik_email_port: "25" # (2)!
authentik_email_username: "" # (3)!
authentik_email_password: "" # (4)!
authentik_email_tls: "false"
authentik_email_ssl: "false"
authentik_email_timeout: "10" # (5)!
authentik_email_from: "authentik@localhost" # (6)!
```

1. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
2. Replace `25` with your email port. IE: `587`
3. Replace `""` with your email username if necessary.
4. Replace `""` with your email password if necessary.
5. Replace `10` with your email timeout in seconds.
6. Replace `authentik@localhost` with your email from email address. IE: `Authentik <noreply@iYOUR_DOMAIN_NAMEi>`

Redeploy the Authentik role to apply these changes.

## Deployment

```shell
sb install authentik
```

## Usage

Visit <https://auth.iYOUR_DOMAIN_NAMEi>.

## Basics

### IDP/OIDC Configuration

To configure Authentik as an IDP (Identity Provider) or OIDC (OpenID Connect) provider, follow these steps:

Click on the `Admin Interface` button in the top right corner.

Locate the `Applications` tab on the left panel and click on it.

Near the center of the screen select the blue `Create With Wizard` button.

- Below you will see the `Create Application` screen.

    ![Create Application](../images/authentik/authentik-create-application-screenshot.png)

On the next screen select the `Oauth2/OIDC` option. (This will be the first option)

In this example, on the `Configure OAuth2/OpenId Provider` screen, only the required fields will be filled.

- Below you will see the `Configure OAuth2` screen.

    ![Configure Oauth2](../images/authentik/authentik-configure-oauth2.png)

Under the `Protocol Settings` section, fill in the following fields:

- `Client ID`: `immich` (This can be anything you want, and is auto filled in. You can change it if you want)
- `Client Secret`: Its probably best to leave this as is, but you can change it if you want.
- `Redirect URI/Origins`:
  - `https://immich.xYOUR_DOMAIN_NAMEx/auth/login`
  - `https://immich.xYOUR_DOMAIN_NAMEx/user-settings`
  - `app.immich:/`

#### OIDC Configuration Example

In the screenshot below, you can see how the [Immich](../sandbox/apps/immich.md) application is configured to use Authentik as an OIDC provider.

![Authentik Oauth Example](../images/authentik/authentik-oauth-example.png)

The only other field you need to concern yourself with is the `Mobile Redirect URI`, which is `https://immich.xYOUR_DOMAIN_NAMEx/api/oauth/mobile-redirect`.

- [:octicons-link-16: Authentik Docs](https://docs.goauthentik.io/docs){: .header-icons }

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        authentik_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `authentik_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `authentik_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`authentik_name`"

        ```yaml
        # Type: string
        authentik_name: authentik
        ```

=== "Settings"

    ??? variable string "`authentik_role_email_host`"

        ```yaml
        # Type: string
        authentik_role_email_host: "localhost"
        ```

    ??? variable string "`authentik_role_email_port`"

        ```yaml
        # Type: string
        authentik_role_email_port: "25"
        ```

    ??? variable string "`authentik_role_email_username`"

        ```yaml
        # Type: string
        authentik_role_email_username: ""
        ```

    ??? variable string "`authentik_role_email_password`"

        ```yaml
        # Type: string
        authentik_role_email_password: ""
        ```

    ??? variable string "`authentik_role_email_tls`"

        ```yaml
        # Type: string
        authentik_role_email_tls: "false"
        ```

    ??? variable string "`authentik_role_email_ssl`"

        ```yaml
        # Type: string
        authentik_role_email_ssl: "false"
        ```

    ??? variable string "`authentik_role_email_timeout`"

        ```yaml
        # Type: string
        authentik_role_email_timeout: "10"
        ```

    ??? variable string "`authentik_role_email_from`"

        ```yaml
        # Type: string
        authentik_role_email_from: "authentik@localhost"
        ```

    ??? variable string "`authentik_role_access_token_validity`"

        ```yaml
        # Type: string
        authentik_role_access_token_validity: "24" # Hours, only fresh installs use this
        ```

=== "Postgres"

    ??? variable bool "`authentik_role_postgres_deploy`"

        ```yaml
        # Authentik will always require postgres, this just allows you to skip the one Saltbox deploys
        # Type: bool (true/false)
        authentik_role_postgres_deploy: true
        ```

    ??? variable string "`authentik_role_postgres_name`"

        ```yaml
        # Type: string
        authentik_role_postgres_name: "{{ authentik_name }}-postgres"
        ```

    ??? variable string "`authentik_role_postgres_user`"

        ```yaml
        # Type: string
        authentik_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`authentik_role_postgres_password`"

        ```yaml
        # Type: string
        authentik_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`authentik_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        authentik_role_postgres_docker_env_db: "authentik"
        ```

    ??? variable string "`authentik_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        authentik_role_postgres_docker_image_tag: "16-alpine"
        ```

    ??? variable string "`authentik_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        authentik_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`authentik_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        authentik_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='authentik') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

=== "Web"

    ??? variable string "`authentik_role_web_subdomain`"

        ```yaml
        # Type: string
        authentik_role_web_subdomain: "auth"
        ```

    ??? variable string "`authentik_role_web_domain`"

        ```yaml
        # Type: string
        authentik_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`authentik_role_web_port`"

        ```yaml
        # Type: string
        authentik_role_web_port: "9000"
        ```

    ??? variable string "`authentik_role_web_url`"

        ```yaml
        # Type: string
        authentik_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='authentik') + '.' + lookup('role_var', '_web_domain', role='authentik')
                                 if (lookup('role_var', '_web_subdomain', role='authentik') | length > 0)
                                 else lookup('role_var', '_web_domain', role='authentik')) }}"
        ```

    ??? variable string "`authentik_role_web_host`"

        ```yaml
        # Type: string
        authentik_role_web_host: "{{ (lookup('role_var', '_web_subdomain', role='authentik') + '.' + lookup('role_var', '_web_domain', role='authentik')
                                  if (lookup('role_var', '_web_subdomain', role='authentik') | length > 0)
                                  else lookup('role_var', '_web_domain', role='authentik')) }}"
        ```

=== "DNS"

    ??? variable string "`authentik_role_dns_record`"

        ```yaml
        # Type: string
        authentik_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='authentik') }}"
        ```

    ??? variable string "`authentik_role_dns_zone`"

        ```yaml
        # Type: string
        authentik_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='authentik') }}"
        ```

    ??? variable bool "`authentik_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`authentik_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        authentik_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`authentik_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        authentik_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`authentik_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        authentik_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`authentik_role_traefik_certresolver`"

        ```yaml
        # Type: string
        authentik_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`authentik_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_traefik_enabled: true
        ```

    ??? variable bool "`authentik_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_traefik_api_enabled: false
        ```

    ??? variable string "`authentik_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        authentik_role_traefik_api_endpoint: ""
        ```

    ??? variable bool "`authentik_role_traefik_outpost_catch_all`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_traefik_outpost_catch_all: false
        ```

=== "Setup"

    ??? variable string "`authentik_role_host`"

        ```yaml
        # Type: string
        authentik_role_host: "http://{{ authentik_name }}:{{ lookup('role_var', '_web_port', role='authentik') }}"
        ```

    ??? variable string "`authentik_role_default_user`"

        ```yaml
        # Type: string
        authentik_role_default_user: "akadmin"
        ```

    ??? variable list "`authentik_role_response_headers`"

        ```yaml
        # Type: list
        authentik_role_response_headers:
          - "X-authentik-username"
          - "X-authentik-groups"
          - "X-authentik-entitlements"
          - "X-authentik-email"
          - "X-authentik-name"
          - "X-authentik-uid"
          - "X-authentik-jwt"
          - "X-authentik-meta-jwks"
          - "X-authentik-meta-outpost"
          - "X-authentik-meta-provider"
          - "X-authentik-meta-app"
          - "X-authentik-meta-version"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`authentik_role_docker_container`"

        ```yaml
        # Type: string
        authentik_role_docker_container: "{{ authentik_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`authentik_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_image_pull: true
        ```

    ??? variable string "`authentik_role_docker_image_repo`"

        ```yaml
        # Type: string
        authentik_role_docker_image_repo: "ghcr.io/goauthentik/server"
        ```

    ??? variable string "`authentik_role_docker_image_tag`"

        ```yaml
        # Type: string
        authentik_role_docker_image_tag: "2025.10"
        ```

    ??? variable string "`authentik_role_docker_image`"

        ```yaml
        # Type: string
        authentik_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='authentik') }}:{{ lookup('role_var', '_docker_image_tag', role='authentik') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`authentik_role_docker_envs_default`"

        ```yaml
        # Type: dict
        authentik_role_docker_envs_default:
          AUTHENTIK_POSTGRESQL__HOST: "{{ lookup('role_var', '_postgres_name', role='authentik') }}"
          AUTHENTIK_POSTGRESQL__USER: "{{ lookup('role_var', '_postgres_user', role='authentik') }}"
          AUTHENTIK_POSTGRESQL__NAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='authentik') }}"
          AUTHENTIK_POSTGRESQL__PASSWORD: "{{ lookup('role_var', '_postgres_password', role='authentik') }}"
          AUTHENTIK_SECRET_KEY: "{{ authentik_saltbox_facts.facts.secret_key }}"
          AUTHENTIK_BOOTSTRAP_TOKEN: "{{ omit if authentik_data_folder.stat.exists else authentik_bootstrap_token }}"
          AUTHENTIK_EMAIL__HOST: "{{ lookup('role_var', '_email_host', role='authentik') }}"
          AUTHENTIK_EMAIL__PORT: "{{ lookup('role_var', '_email_port', role='authentik') }}"
          AUTHENTIK_EMAIL__USERNAME: "{{ lookup('role_var', '_email_username', role='authentik') }}"
          AUTHENTIK_EMAIL__PASSWORD: "{{ lookup('role_var', '_email_password', role='authentik') }}"
          AUTHENTIK_EMAIL__USE_TLS: "{{ lookup('role_var', '_email_tls', role='authentik') }}"
          AUTHENTIK_EMAIL__USE_SSL: "{{ lookup('role_var', '_email_ssl', role='authentik') }}"
          AUTHENTIK_EMAIL__TIMEOUT: "{{ lookup('role_var', '_email_timeout', role='authentik') }}"
          AUTHENTIK_EMAIL__FROM: "{{ lookup('role_var', '_email_from', role='authentik') }}"
          AUTHENTIK_LISTEN__TRUSTED_PROXY_CIDRS: "172.19.0.0/16"
        ```

    ??? variable dict "`authentik_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        authentik_role_docker_envs_custom: {}
        ```

    <h5>Commands</h5>

    ??? variable list "`authentik_role_docker_commands_default`"

        ```yaml
        # Type: list
        authentik_role_docker_commands_default:
          - "server"
        ```

    ??? variable list "`authentik_role_docker_commands_custom`"

        ```yaml
        # Type: list
        authentik_role_docker_commands_custom: []
        ```

    <h5>Volumes</h5>

    ??? variable list "`authentik_role_docker_volumes_default`"

        ```yaml
        # Type: list
        authentik_role_docker_volumes_default:
          - "{{ authentik_role_paths_location }}/media:/media"
          - "{{ authentik_role_paths_location }}/custom-templates:/templates"
        ```

    ??? variable list "`authentik_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        authentik_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`authentik_role_docker_labels_default`"

        ```yaml
        # Type: dict
        authentik_role_docker_labels_default:
          traefik.http.routers.authentik-outpost-http.entrypoints: "web"
          traefik.http.routers.authentik-outpost-http.service: "authentik-outpost-http"
          traefik.http.routers.authentik-outpost-http.rule: "PathPrefix(`/outpost.goauthentik.io/`)"
          traefik.http.routers.authentik-outpost-http.middlewares: "{{ traefik_default_middleware_http }}"
          traefik.http.routers.authentik-outpost-http.priority: "99"
          traefik.http.routers.authentik-outpost.entrypoints: "websecure"
          traefik.http.routers.authentik-outpost.service: "authentik-outpost"
          traefik.http.routers.authentik-outpost.rule: "PathPrefix(`/outpost.goauthentik.io/`)"
          traefik.http.routers.authentik-outpost.tls.options: "securetls@file"
          traefik.http.routers.authentik-outpost.tls.certresolver: "{{ authentik_role_traefik_certresolver }}"
          traefik.http.routers.authentik-outpost.middlewares: "{{ traefik_default_middleware }}"
          traefik.http.routers.authentik-outpost.priority: "99"
          traefik.http.services.authentik-outpost-http.loadbalancer.server.port: "{{ lookup('role_var', '_web_port', role='authentik') }}"
          traefik.http.services.authentik-outpost.loadbalancer.server.port: "{{ lookup('role_var', '_web_port', role='authentik') }}"
        ```

    ??? variable dict "`authentik_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        authentik_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`authentik_role_docker_hostname`"

        ```yaml
        # Type: string
        authentik_role_docker_hostname: "{{ authentik_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`authentik_role_docker_networks_alias`"

        ```yaml
        # Type: string
        authentik_role_docker_networks_alias: "{{ authentik_name }}"
        ```

    ??? variable list "`authentik_role_docker_networks_default`"

        ```yaml
        # Type: list
        authentik_role_docker_networks_default: []
        ```

    ??? variable list "`authentik_role_docker_networks_custom`"

        ```yaml
        # Type: list
        authentik_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`authentik_role_docker_restart_policy`"

        ```yaml
        # Type: string
        authentik_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`authentik_role_docker_state`"

        ```yaml
        # Type: string
        authentik_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`authentik_role_depends_on`"

        ```yaml
        # Type: string
        authentik_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='authentik') }}"
        ```

    ??? variable string "`authentik_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        authentik_role_depends_on_delay: "0"
        ```

    ??? variable string "`authentik_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        authentik_role_depends_on_healthchecks: "true"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`authentik_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        authentik_role_docker_blkio_weight:
        ```

    ??? variable int "`authentik_role_docker_cpu_period`"

        ```yaml
        # Type: int
        authentik_role_docker_cpu_period:
        ```

    ??? variable int "`authentik_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        authentik_role_docker_cpu_quota:
        ```

    ??? variable int "`authentik_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        authentik_role_docker_cpu_shares:
        ```

    ??? variable string "`authentik_role_docker_cpus`"

        ```yaml
        # Type: string
        authentik_role_docker_cpus:
        ```

    ??? variable string "`authentik_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        authentik_role_docker_cpuset_cpus:
        ```

    ??? variable string "`authentik_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        authentik_role_docker_cpuset_mems:
        ```

    ??? variable string "`authentik_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        authentik_role_docker_kernel_memory:
        ```

    ??? variable string "`authentik_role_docker_memory`"

        ```yaml
        # Type: string
        authentik_role_docker_memory:
        ```

    ??? variable string "`authentik_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        authentik_role_docker_memory_reservation:
        ```

    ??? variable string "`authentik_role_docker_memory_swap`"

        ```yaml
        # Type: string
        authentik_role_docker_memory_swap:
        ```

    ??? variable int "`authentik_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        authentik_role_docker_memory_swappiness:
        ```

    ??? variable string "`authentik_role_docker_shm_size`"

        ```yaml
        # Type: string
        authentik_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`authentik_role_docker_cap_drop`"

        ```yaml
        # Type: list
        authentik_role_docker_cap_drop:
        ```

    ??? variable string "`authentik_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        authentik_role_docker_cgroupns_mode:
        ```

    ??? variable list "`authentik_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        authentik_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`authentik_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        authentik_role_docker_device_read_bps:
        ```

    ??? variable list "`authentik_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        authentik_role_docker_device_read_iops:
        ```

    ??? variable list "`authentik_role_docker_device_requests`"

        ```yaml
        # Type: list
        authentik_role_docker_device_requests:
        ```

    ??? variable list "`authentik_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        authentik_role_docker_device_write_bps:
        ```

    ??? variable list "`authentik_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        authentik_role_docker_device_write_iops:
        ```

    ??? variable list "`authentik_role_docker_devices`"

        ```yaml
        # Type: list
        authentik_role_docker_devices:
        ```

    ??? variable string "`authentik_role_docker_devices_default`"

        ```yaml
        # Type: string
        authentik_role_docker_devices_default:
        ```

    ??? variable list "`authentik_role_docker_groups`"

        ```yaml
        # Type: list
        authentik_role_docker_groups:
        ```

    ??? variable bool "`authentik_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_privileged:
        ```

    ??? variable list "`authentik_role_docker_security_opts`"

        ```yaml
        # Type: list
        authentik_role_docker_security_opts:
        ```

    ??? variable string "`authentik_role_docker_user`"

        ```yaml
        # Type: string
        authentik_role_docker_user:
        ```

    ??? variable string "`authentik_role_docker_userns_mode`"

        ```yaml
        # Type: string
        authentik_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`authentik_role_docker_dns_opts`"

        ```yaml
        # Type: list
        authentik_role_docker_dns_opts:
        ```

    ??? variable list "`authentik_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        authentik_role_docker_dns_search_domains:
        ```

    ??? variable list "`authentik_role_docker_dns_servers`"

        ```yaml
        # Type: list
        authentik_role_docker_dns_servers:
        ```

    ??? variable string "`authentik_role_docker_domainname`"

        ```yaml
        # Type: string
        authentik_role_docker_domainname:
        ```

    ??? variable list "`authentik_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        authentik_role_docker_exposed_ports:
        ```

    ??? variable dict "`authentik_role_docker_hosts`"

        ```yaml
        # Type: dict
        authentik_role_docker_hosts:
        ```

    ??? variable bool "`authentik_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_hosts_use_common:
        ```

    ??? variable string "`authentik_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        authentik_role_docker_ipc_mode:
        ```

    ??? variable list "`authentik_role_docker_links`"

        ```yaml
        # Type: list
        authentik_role_docker_links:
        ```

    ??? variable string "`authentik_role_docker_network_mode`"

        ```yaml
        # Type: string
        authentik_role_docker_network_mode:
        ```

    ??? variable string "`authentik_role_docker_pid_mode`"

        ```yaml
        # Type: string
        authentik_role_docker_pid_mode:
        ```

    ??? variable list "`authentik_role_docker_ports`"

        ```yaml
        # Type: list
        authentik_role_docker_ports:
        ```

    ??? variable string "`authentik_role_docker_uts`"

        ```yaml
        # Type: string
        authentik_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`authentik_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_keep_volumes:
        ```

    ??? variable list "`authentik_role_docker_mounts`"

        ```yaml
        # Type: list
        authentik_role_docker_mounts:
        ```

    ??? variable dict "`authentik_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        authentik_role_docker_storage_opts:
        ```

    ??? variable list "`authentik_role_docker_tmpfs`"

        ```yaml
        # Type: list
        authentik_role_docker_tmpfs:
        ```

    ??? variable string "`authentik_role_docker_volume_driver`"

        ```yaml
        # Type: string
        authentik_role_docker_volume_driver:
        ```

    ??? variable list "`authentik_role_docker_volumes_from`"

        ```yaml
        # Type: list
        authentik_role_docker_volumes_from:
        ```

    ??? variable bool "`authentik_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_volumes_global:
        ```

    ??? variable string "`authentik_role_docker_working_dir`"

        ```yaml
        # Type: string
        authentik_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`authentik_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_auto_remove:
        ```

    ??? variable bool "`authentik_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_cleanup:
        ```

    ??? variable string "`authentik_role_docker_force_kill`"

        ```yaml
        # Type: string
        authentik_role_docker_force_kill:
        ```

    ??? variable dict "`authentik_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        authentik_role_docker_healthcheck:
        ```

    ??? variable int "`authentik_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        authentik_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`authentik_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_init:
        ```

    ??? variable string "`authentik_role_docker_kill_signal`"

        ```yaml
        # Type: string
        authentik_role_docker_kill_signal:
        ```

    ??? variable string "`authentik_role_docker_log_driver`"

        ```yaml
        # Type: string
        authentik_role_docker_log_driver:
        ```

    ??? variable dict "`authentik_role_docker_log_options`"

        ```yaml
        # Type: dict
        authentik_role_docker_log_options:
        ```

    ??? variable bool "`authentik_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_oom_killer:
        ```

    ??? variable int "`authentik_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        authentik_role_docker_oom_score_adj:
        ```

    ??? variable bool "`authentik_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_output_logs:
        ```

    ??? variable bool "`authentik_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_paused:
        ```

    ??? variable bool "`authentik_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_recreate:
        ```

    ??? variable int "`authentik_role_docker_restart_retries`"

        ```yaml
        # Type: int
        authentik_role_docker_restart_retries:
        ```

    ??? variable int "`authentik_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        authentik_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`authentik_role_docker_capabilities`"

        ```yaml
        # Type: list
        authentik_role_docker_capabilities:
        ```

    ??? variable string "`authentik_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        authentik_role_docker_cgroup_parent:
        ```

    ??? variable int "`authentik_role_docker_create_timeout`"

        ```yaml
        # Type: int
        authentik_role_docker_create_timeout:
        ```

    ??? variable string "`authentik_role_docker_entrypoint`"

        ```yaml
        # Type: string
        authentik_role_docker_entrypoint:
        ```

    ??? variable string "`authentik_role_docker_env_file`"

        ```yaml
        # Type: string
        authentik_role_docker_env_file:
        ```

    ??? variable bool "`authentik_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_labels_use_common:
        ```

    ??? variable bool "`authentik_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_read_only:
        ```

    ??? variable string "`authentik_role_docker_runtime`"

        ```yaml
        # Type: string
        authentik_role_docker_runtime:
        ```

    ??? variable list "`authentik_role_docker_sysctls`"

        ```yaml
        # Type: list
        authentik_role_docker_sysctls:
        ```

    ??? variable list "`authentik_role_docker_ulimits`"

        ```yaml
        # Type: list
        authentik_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`authentik_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        authentik_role_autoheal_enabled: true
        ```

    ??? variable string "`authentik_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        authentik_role_depends_on: ""
        ```

    ??? variable string "`authentik_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        authentik_role_depends_on_delay: "0"
        ```

    ??? variable string "`authentik_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        authentik_role_depends_on_healthchecks:
        ```

    ??? variable bool "`authentik_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        authentik_role_diun_enabled: true
        ```

    ??? variable bool "`authentik_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        authentik_role_dns_enabled: true
        ```

    ??? variable bool "`authentik_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        authentik_role_docker_controller: true
        ```

    ??? variable string "`authentik_role_docker_image_repo`"

        ```yaml
        # Type: string
        authentik_role_docker_image_repo:
        ```

    ??? variable string "`authentik_role_docker_image_tag`"

        ```yaml
        # Type: string
        authentik_role_docker_image_tag:
        ```

    ??? variable bool "`authentik_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_docker_volumes_download:
        ```

    ??? variable string "`authentik_role_email_from`"

        ```yaml
        # Type: string
        authentik_role_email_from:
        ```

    ??? variable string "`authentik_role_email_host`"

        ```yaml
        # Type: string
        authentik_role_email_host:
        ```

    ??? variable string "`authentik_role_email_password`"

        ```yaml
        # Type: string
        authentik_role_email_password:
        ```

    ??? variable string "`authentik_role_email_port`"

        ```yaml
        # Type: string (quoted number)
        authentik_role_email_port:
        ```

    ??? variable string "`authentik_role_email_ssl`"

        ```yaml
        # Type: string
        authentik_role_email_ssl:
        ```

    ??? variable string "`authentik_role_email_timeout`"

        ```yaml
        # Type: string (quoted number)
        authentik_role_email_timeout:
        ```

    ??? variable string "`authentik_role_email_tls`"

        ```yaml
        # Type: string
        authentik_role_email_tls:
        ```

    ??? variable string "`authentik_role_email_username`"

        ```yaml
        # Type: string
        authentik_role_email_username:
        ```

    ??? variable string "`authentik_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        authentik_role_postgres_docker_env_db:
        ```

    ??? variable string "`authentik_role_postgres_name`"

        ```yaml
        # Type: string
        authentik_role_postgres_name:
        ```

    ??? variable string "`authentik_role_postgres_password`"

        ```yaml
        # Type: string
        authentik_role_postgres_password:
        ```

    ??? variable string "`authentik_role_postgres_user`"

        ```yaml
        # Type: string
        authentik_role_postgres_user:
        ```

    ??? variable string "`authentik_role_themepark_addons`"

        ```yaml
        # Type: string
        authentik_role_themepark_addons:
        ```

    ??? variable string "`authentik_role_themepark_app`"

        ```yaml
        # Type: string
        authentik_role_themepark_app:
        ```

    ??? variable string "`authentik_role_themepark_theme`"

        ```yaml
        # Type: string
        authentik_role_themepark_theme:
        ```

    ??? variable dict "`authentik_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        authentik_role_traefik_api_endpoint:
        ```

    ??? variable string "`authentik_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        authentik_role_traefik_api_middleware:
        ```

    ??? variable string "`authentik_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        authentik_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`authentik_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        authentik_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`authentik_role_traefik_certresolver`"

        ```yaml
        # Type: string
        authentik_role_traefik_certresolver:
        ```

    ??? variable bool "`authentik_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        authentik_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`authentik_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        authentik_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`authentik_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        authentik_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`authentik_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        authentik_role_traefik_middleware_http:
        ```

    ??? variable bool "`authentik_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`authentik_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        authentik_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`authentik_role_traefik_priority`"

        ```yaml
        # Type: string
        authentik_role_traefik_priority:
        ```

    ??? variable bool "`authentik_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        authentik_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`authentik_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        authentik_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`authentik_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        authentik_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`authentik_role_web_domain`"

        ```yaml
        # Type: string
        authentik_role_web_domain:
        ```

    ??? variable list "`authentik_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        authentik_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            authentik_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "authentik2.{{ user.domain }}"
              - "authentik.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`authentik_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        authentik_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            authentik_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'authentik2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`authentik_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        authentik_role_web_http_port:
        ```

    ??? variable string "`authentik_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        authentik_role_web_http_scheme:
        ```

    ??? variable dict "`authentik_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        authentik_role_web_http_serverstransport:
        ```

    ??? variable string "`authentik_role_web_port`"

        ```yaml
        # Type: string (quoted number)
        authentik_role_web_port:
        ```

    ??? variable string "`authentik_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        authentik_role_web_scheme:
        ```

    ??? variable dict "`authentik_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        authentik_role_web_serverstransport:
        ```

    ??? variable string "`authentik_role_web_subdomain`"

        ```yaml
        # Type: string
        authentik_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->