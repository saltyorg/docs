---
hide:
  - tags
tags:
  - install
  - customize
  - inventory
  - root
  - domain
  - pin version
  - version tag
  - specify version
---

# Inventory

The inventory system offers a centralized approach to customizing roles, allowing manipulation of variables without directly editing the roles themselves. This ensures persistent configurations while avoiding conflicts during git merge operations.

## Modifying Variables

Enter your new values in:

!!! tip inline end "Shell Shortcut"

    ```sh
    sb edit inventory
    ```

```
/srv/git/saltbox/inventories/host_vars/localhost.yml
```

Changes take effect after deploying the affected role(s) using `sb install`.

## Finding Available Variables

Variables that can be used for customization within the Inventory are listed under ***Role Defaults*** at the end of role documentations. Find roles by using search or browsing the indexes:

[Apps](../../apps/index.md){ .md-button }
[Modules](../../reference/modules/index.md){ .md-button }

## Data Types

Inventory syntax follows [YAML specifications](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html). You will encounter five data types in the defaults:

| Data Type       | Token          | Syntax Template                                                                  | Saltbox Example                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| boolean         | `true`/`false` | <pre><code>bool_key: true</code></pre>                                           | <pre><code>use_cloudplow: false</code></pre>                                                                                      |
| integer         |                | <pre><code>int_key: 123</code></pre>                                             | <pre><code>emby_role_config_cache_size: 2048</code></pre>                                                                         |
| string          | `""`           | <pre><code>str_key: "value"</code></pre>                                         | <pre><code>global_themepark_theme: "overseerr"</code></pre>                                                                       |
| <br/>list       | <br/>`[]`      | <pre><code>list_key:<br/>  - item0<br/>  - "item1"</code></pre>                  | <pre><code>gluetun_docker_networks_alias_custom:<br/>  - "plex"<br/>  - "plex2"</code></pre>                                      |
| <br/>dictionary | <br/>`{}`      | <pre><code>dict_key:<br/>  STR_KEY: "value"<br/>  BOOL_KEY: "false"</code></pre> | <pre><code>kometasw_docker_envs_custom:<br/>  KOMETA_RUN_COLLECTIONS: "Star Wars"<br/>  KOMETA_DELETE_LABELS: "true"</code></pre> |

## Default and Custom Patterns

Saltbox variable files are a combination of static and dynamic configuration. Many variable assignments are integral to how the component is deployed, and if modified, can break functionality or cause conflicts during updates. Some keywords and contents can help identify which variables may be customized:

<div class="md-table--heatmap" markdown>

| Pattern                      | Purpose                                                               |
|------------------------------|-----------------------------------------------------------------------|
| Ends in `_custom`            | Extend configuration by adding items without removing existing ones   |
| Empty or blank string        | Optional setting that is reasonably safe to configure                 |
| Non-empty string or boolean  | Sane default that should only be changed if you understand the impact |
| Ends in `_default`           | Internal configuration required by the component—do not override      |
| Contains dynamic expressions | Internal configuration required by the component—do not override      |

</div>

## Role and Instance Patterns

If the role supports multiple instances, you can choose to apply a configuration across all instances (role-level) or to a specified instance only (instance-level). This is done by shaping the variable name as follows:

<div class="grid" markdown>

<div markdown>

:material-rhombus: **Role-level**

```yaml
rolename_role_setting_enabled: false # (1)!
```

1.  Variable name unchanged

:material-arrow-right-bottom-bold: Applies to all instances of the role

</div>

<div markdown>

:material-rhombus-split: **Instance-level**

```yaml
instancename_setting_enabled: true # (1)!
```

1.  -   `_role` segment removed
    -   name of role replaced with name of instance

:material-arrow-right-bottom-bold: Applies to the specified instance

</div>

</div>

## Demo

Let's explore two example use cases for customizing roles using variables in the Saltbox Inventory.

### Replacing a Default Value

A common use for overrides will be specifying the version of the Docker image to be used. Let's see how that's done by navigating to [Sonarr: Role Defaults](../../apps/sonarr.md#role-defaults) and in the ***Docker*** tab, scrolling down to:

???+ variable string "`sonarr_role_docker_image_tag`"

    === "Role-level"

        ```yaml
        # Type: string
        sonarr_role_docker_image_tag: "release"
        ```

    === "Instance-level"
   
        ```yaml
        # Type: string
        sonarr2_docker_image_tag: "release"
        ```

In light of this default, Saltbox will use `ghcr.io/hotio/sonarr:release` as the Sonarr Docker image.

Opting to switch to "nightly" versions across all Sonarr instances, we can add the following line to `localhost.yml`:

```yaml
sonarr_role_docker_image_tag: "nightly"
```

This will cause Saltbox to use the `ghcr.io/hotio/sonarr:nightly` Docker image, overriding the default: `release`. When we update Saltbox, our tag change to `nightly` will remain in effect.

### Adding an Item to a List

A common use for lists to specify extra Docker mappings or flags. Let's examine how to give our [code-server](../../sandbox/apps/code_server.md#role-defaults) container access to more locations on the host. In the ***Docker*** section yet again, we find:

??? variable list "`code_server_role_docker_volumes_default`"

    ```yaml
    # Type: list
    code_server_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/project:/home/coder/project"
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.config:/home/coder/.config"
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.local:/home/coder/.local"
      - "{{ server_appdata_path }}:/host_opt"
    ```

???+variable list "`code_server_role_docker_volumes_custom`"

    ```yaml
    # Type: list
    code_server_role_docker_volumes_custom: []
    ```

Note the list syntax. Since we want the container to preserve existing volumes, the `_docker_volumes_default` list should not be overridden. Instead, we use the `_docker_volumes_custom` list.

To expose additional host locations (in this case, `/srv` and our home directory), we can add custom volumes to the list using the following syntax in the Inventory:

```yaml
code_server_role_docker_volumes_custom:
  - "/srv:/host_srv"
  - "/home:/host_home"
```

The container will then be created with the new volumes included, and the target locations will be accessible to code-server at `/host_srv` and `/host_home`.

## Additional Examples

```yaml title="Various"
##### Enabling different media servers, downloaders and indexers #####
media_servers_enabled: ["emby"]
download_clients_enabled: ["deluge", "nzbget"]
download_indexers_enabled: ["prowlarr"]

##### Plex Ports for local access #####
plex_open_main_ports: true
plex_open_local_ports: true

##### Plex Container Variables ####
plex_docker_image_pull: false # (1)!
plex_docker_image_tag: beta # (2)!

#### Examples of specified container images: ####
radarr_docker_image_tag: nightly
sonarr_docker_image_tag: nightly
petio_docker_image_tag: nightly

#### Configure Sonarr 4k/Radarr 4k Instance Name (assumed instances defined as `sonarr4k` and `radarr4k`)
sonarr4k_docker_envs_custom:
  SONARR__APP__INSTANCENAME: "Sonarr4k" # Must start or end with the word Sonarr
radarr4k_docker_envs_custom:
  RADARR__APP__INSTANCENAME: "Radarr4k" # Must start or end with the word Radarr

#### Bandwidth and rate limiting  ####
#### along with multiple env vars ####
transfer_docker_envs_custom:
  MAX_UPLOAD_SIZE: "104857546"
  RATE_LIMIT: "60"

#### Specify Overseerr DNS server - can fix name resolution issue with TMDb ####
overseerr_docker_dns_servers:
  - 8.8.8.8
  - 8.8.4.4

#### Add custom aliases to bash shell ####
#### Note the syntax - a pipe and two space indentation for the contents ####
shell_bash_bashrc_block_custom: |
  alias sbu='sb update'
  alias sbi='sb install'

#### Add custom aliases to zsh shell ###
#### Note the syntax - a pipe and two space indentation for the contents ####
shell_zsh_zshrc_block_custom: |
  alias sbu='sb update'
  alias sbi='sb install'
```

1. Can be used to version-pin the image to the current container's version (as long as the image is never pulled by other means)

2. Will version-lock if the tag designates a specific version.

### Authelia App Bypass

!!! danger "While we generally allow users to override pretty much anything this is not a supported configuration so keep that in mind when going this road."

Some users may not want the additional layer of security that Authelia provides. The good news is that it can be disabled through a simple override.

!!! tip ""
    To determine which apps are included in Authelia by default, you can run this command or a similar one:

    ```shell
    grep -Ril '_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"' /srv/git/saltbox/roles /opt/sandbox/roles | awk 'BEGIN{RS="roles/"; FS="/defaults"}NF>1{print $1}' | sort -u
    ```

!!! danger "Before proceeding, ensure that fallback measures are in place to prevent unauthorized access to any of your apps."

```yaml title="Override Example"
### Authelia App Bypass ###
sonarr_traefik_sso_middleware: ""
tautulli_traefik_sso_middleware: ""
radarr_traefik_sso_middleware: ""
nzbget_traefik_sso_middleware: ""
prowlarr_traefik_sso_middleware: ""
```

After making this change in the Inventory file, simply run the appropriate role command to disable Authelia on that specific app. Remember, you can run multiple tags at once.

Should you wish to enable Authelia on an application that did not previously use it you do something similar as above but use a different value to enable it:

```yaml
appname_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
```

It should be noted that we take care of whitelisting any API endpoints when enabling Authelia for you so ask on the discord if you have trouble with enabling Authelia on an application that needs to have its API whitelisted and the below example isn't enough.

```yaml
appname_traefik_api_enabled: true
appname_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"
```

### Authorize with App Credentials

__Inject an Authorization header - Traefik performs basic auth with the backend app__

This will allow you to keep basic auth enabled within apps while avoiding the hassle of entering the credentials manually. The authorization header is only inserted if the request is authorized through the SSO middleware (Authelia) and is not applied to the API endpoint(s).

You can use [this tool](https://www.blitter.se/utils/basic-authentication-header-generator/) to generate the header contents based on your credentials.

```yaml
sonarr_docker_labels_custom:
  traefik.http.middlewares.appAuth.headers.customrequestheaders.Authorization: "Basic <base64 header>"
sonarr_traefik_middleware_custom: "appAuth"
```

### Subdomain Customization

=== "Overrides"

    ```yaml
    #### Make Organizr available only at the base domain ####
    organizr_web_subdomain: ""
    
    #### Make Tautulli available only at `stats.xYOUR_DOMAIN_NAMEx` ####
    tautulli_web_subdomain: "stats"
    ```

=== "Additions"

    !!! warning ""
        DNS records for the following examples won't be set up by Saltbox. You can add them manually or if using Cloudflare, have the `ddns` service handle it.
    
    ```yaml
    #### Make Organizr available at `organizr.xYOUR_DOMAIN_NAMEx`, `xYOUR_DOMAIN_NAMEx` and `example.com` ####
    organizr_web_fqdn_override:
      - "{{ traefik_host }}"
      - "{{ organizr_web_domain }}"
      - "example.com"

    #### Make Overseerr available at both `overseerr.xYOUR_DOMAIN_NAMEx` and `requests.xYOUR_DOMAIN_NAMEx` ####
    overseerr_web_fqdn_override:
      - "{{ traefik_host }}"
      - "requests.{{ overseerr_web_domain }}"
  
    ```

### Domain Customization

```yaml
#### Make Organizr available at a different base domain ####
organizr_web_domain: "example.com"  # set all organizr instances to NAME.example.com

organizr02_web_domain: "bing.com"  # override this one organizr instance to NAME.bing.com
```

`organizr_web_subdomain` would apply the new base domain to any instances of organizr.

`organizr02_web_subdomain` would apply the new base domain to just that one instance.


### Tag Customization

```yaml
#### Customize the saltbox tag (sb install saltbox) - No sandbox roles
saltbox_roles: ["media_server", "download_clients", "download_indexers", "autoscan", "tautulli", "overseerr", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "glances", "btop"]

#### Customize the mediabox tag (sb install mediabox) - No sandbox roles
mediabox_roles: ["media_server", "autoscan", "iperf3", "glances", "btop"]

#### Customize the feeerbox tag (sb install feederbox) - No sandbox roles
feederbox_roles: ["download_clients", "download_indexers", "portainer", "organizr", "sonarr", "radarr", "iperf3", "glances", "btop"]

#### Customize the sandbox-roles tag (sb install sandbox-sandbox-roles)
sandbox_roles: ["jellyseerr", "jellystat"]
```
