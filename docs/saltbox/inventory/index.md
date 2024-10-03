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

```shell
/srv/git/saltbox/inventories/host_vars/localhost.yml
```

For convenient shell access, you can use the `sb inventory` command.

Changes take effect after running the affected tag(s) using the `sb install` command prefix.

!!! example "Examples for reference. Not necessarily what you will have to run for your changes to apply!"

    <div class="grid" markdown>

    ```shell
    sb install sonarr # (1)!
    ```

    1. The tag to run will usually match the variable prefix. In this case, `sonarr` for when you have added lines that start with `sonarr_`, such as the one shown in the [Override Demo](#override).

    ```shell
    sb install sonarr,sandbox-code-server,shell # (1)!
    ```

    2. - We recommend grouping tags for when you need to deploy multiple roles.
        - For global variables, you may want to use a higher-level tag such as `core`, `feederbox`, `mediabox`, `saltbox`, or others as appropriate.
        - The `shell` tag affects custom bash or zsh additions such as the ones shown [further down](#additional-examples).

    </div>

## Finding Available Variables

The variables that can be used for customization within the Inventory are listed in the following locations:

=== "GitHub File View"

    Saltbox: &nbsp; &nbsp; [:fontawesome-solid-folder-tree: https://github.com/saltyorg/Saltbox/tree/master/roles/](https://github.com/saltyorg/Saltbox/tree/master/roles)<span style="color: #9397b1;">**&lt;role_name&gt;</span><span style="color: #e6695b;">/defaults/main.yml**</span>

    Sandbox: &nbsp; [:fontawesome-solid-folder-tree: https://github.com/saltyorg/Sandbox/tree/master/roles/](https://github.com/saltyorg/Sandbox/tree/master/roles)<span style="color: #9397b1;">**&lt;role_name&gt;</span><span style="color: #e6695b;">/defaults/main.yml**</span>

=== "File Path on Saltbox Host"

    !!! warning inline end "Never Edit These Files"
    
        Updates will overwrite your changes. Use the inventory system instead.

    ```shell
    /srv/git/saltbox/roles/<role_name>/defaults/main.yml
    ```

    ```shell
    /opt/sandbox/roles/<role_name>/defaults/main.yml
    ```

=== "Docker Parameters Reference"

    !!! example inline end "Example"
    
        To obtain a `shm_size` variable for Plex, simply prepend `plex_docker_` to the parameter name: 
      
        ```yaml
        plex_docker_shm_size
        ```

    For use cases involving Docker parameters beyond those exposed in the role files, it is still possible to construct usable Saltbox variables. The following resources provide the required syntax elements:

    <sub><https://github.com/saltyorg/Saltbox/blob/master/resources/tasks/docker/create_docker_container.yml></sub>

    <sub><https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html></sub>

=== "Something Missing?"

    In some cases, usually resulting from incomplete role migration, certain settings may not be exposed for use in the Inventory system. 

    Should you require additional functionality, feel free to create an issue on the [main repository](https://github.com/saltyorg/Saltbox/) and we will consider accommodating it.

## Demo

Let's explore two example use cases for customizing roles using variables in the Saltbox Inventory.

### Override

A common use for overrides will be specifying the version of the Docker image to be used. Let's see how that's done by looking into `/srv/git/saltbox/roles/sonarr/defaults/main.yml` around line 89:

```yaml linenums="83" hl_lines="10" title="https://github.com/saltyorg/Saltbox/blob/master/roles/sonarr/defaults/main.yml#L89"
# Docker
################################

# Container
sonarr_docker_container: "{{ sonarr_name }}"

# Image
sonarr_docker_image_pull: true
sonarr_docker_image_repo: "ghcr.io/hotio/sonarr"
sonarr_docker_image_tag: "release"
sonarr_docker_image: "{{ lookup('vars', sonarr_name + '_docker_image_repo', default=sonarr_docker_image_repo)
                         + ':' + lookup('vars', sonarr_name + '_docker_image_tag', default=sonarr_docker_image_tag) }}"
```
<div class="result" markdown>
!!! info "\`default\` Variables"
    Variables suffixed with `_default` and variables predefined with non-empty values (specifically, not followed by a blank, an empty string `""`, list `[]` or dictionary `{}`) fall under this category. Using the Inventory to define one of these variables is therefore considered an override, as it will cause the value(s) originally stored in it to be discarded.
</div>

Note: `sonarr_docker_image_tag: "release"`. 

By default, Saltbox will use `ghcr.io/hotio/sonarr:release` as the Sonarr Docker image.

Should we choose to switch to "nightly" versions, we can add the following line to `localhost.yml`:

```yaml
sonarr_docker_image_tag: "nightly"
```

This will cause Saltbox to use the `ghcr.io/hotio/sonarr:nightly` Docker image, overriding the default: `release`. When we update Saltbox, our tag change to `nightly` will remain in effect.

### Addition

A common use for additions is to specify extra Docker mappings or flags. Let's examine how to give our [code-server](../../sandbox/apps/code-server.md) container access to more locations on the host:

```yaml linenums="87" hl_lines="7" title="https://github.com/saltyorg/Sandbox/blob/master/roles/code_server/defaults/main.yml#L87"
# Volumes
code_server_docker_volumes_default:
  - "{{ code_server_paths_location }}/project:/home/coder/project"
  - "{{ code_server_paths_location }}/.config:/home/coder/.config"
  - "{{ code_server_paths_location }}/.local:/home/coder/.local"
  - "{{ server_appdata_path }}:/host_opt"
code_server_docker_volumes_custom: []
```
<div class="result" markdown>
!!! info "\`custom\` Variables"
    Variables suffixed with `_custom` and variables defined with an empty string fall under this category. Respectively, this is used to add custom values to a list or a dictionary without discarding existing values, and to assign a value to an exposed role-specific setting.
</div>

Note the list syntax. Since we want the container to preserve existing volumes, the `_docker_volumes_default` list should not be overridden. Instead, we use the `_docker_volumes_custom` list.

To expose additional host locations (in this case, `/srv` and our home directory), we can add custom volumes to the list using the following syntax in the Inventory:

```yaml
code_server_docker_volumes_custom:
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

#### Bandwidth limiting ####
transfer_docker_envs_custom:
  MAX_UPLOAD_SIZE: "104857546"

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
    
    #### Make Tautulli available only at `stats.domain.tld` ####
    tautulli_web_subdomain: "stats"
    ```

=== "Additions"

    !!! warning ""
        DNS records for the following examples won't be set up by Saltbox. You can add them manually or if using Cloudflare, have the `ddns` service handle it.
    
    ```yaml
    #### Make Organizr available at `organizr.domain.tld`, `domain.tld` and `example.com` ####
    organizr_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ organizr_web_domain }}`) || Host(`example.com`)"
    
    #### Make Overseerr available at both `overseerr.domain.tld` and `requests.domain.tld` ####
    overseerr_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'requests.' + overseerr_web_domain }}`)"
    ```

### Domain Customization

```yaml
#### Make Organizr available at a different base domain ####
organizr_web_domain: "example.com"
```

`organizr_web_subdomain` would then apply to the new base domain.

