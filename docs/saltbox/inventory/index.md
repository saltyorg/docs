# Inventory

Advanced use cases that would normally require editing roles can now be handled through the inventory system instead.

Any variables defined in `/srv/git/saltbox/roles/<role_name>/defaults/main.yml` or `/opt/sandbox/roles/<role_name>/defaults/main.yml` are available to be overridden by the user in:

```shell
/srv/git/saltbox/inventories/host_vars/localhost.yml
```

This implementation avoids git merge conflicts when updating Saltbox.

Should you require additional functionality then by all means create an issue on the [main repository](https://github.com/saltyorg/Saltbox/) and we'll look at accommodating it.

## 'Default' variables

!!! info For the purpose of this guide, this refers to variables that are defined with actual data and are not empty (i.e., not followed by an empty string `""`, list `[]` or dictionary `{}`), as well as all variables suffixed with `_default` even if they are empty, in a given role's _defaults_ YAML file. Using the inventory to define one of these variables is therefore considered an override, as it will cause the value(s) originally stored in it to be omitted.

A common use for these overrides will be specifying the version of the Docker image to be used, so let's see how that's done by looking into `/srv/git/saltbox/roles/sonarr/defaults/main.yml` around line 85:

``` yaml
################################
# Docker
################################

# Container
sonarr_docker_container: "{{ sonarr_name }}"

# Image
sonarr_docker_image_pull: true
sonarr_docker_image_repo: "cr.hotio.dev/hotio/sonarr"
sonarr_docker_image_tag: "release"
sonarr_docker_image: "{{ lookup('vars', sonarr_name + '_docker_image_repo', default=sonarr_docker_image_repo)
                         + ':' + lookup('vars', sonarr_name + '_docker_image_tag', default=sonarr_docker_image_tag) }}"
```

Note: `sonarr_docker_image_tag: "release"`

For Sonarr, Saltbox will use the Docker image `cr.hotio.dev/hotio/sonarr:release` by default.

If you wanted to change that to "nightly", you'd add this line to `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

``` yaml
sonarr_docker_image_tag: "nightly"
```

Which would override the default [`release`] and result in Saltbox using the `cr.hotio.dev/hotio/sonarr:nightly` Docker image instead, without you modifying this file. If you update Saltbox and this file is replaced, your tag change to `nightly` remains in effect.

## 'Custom' variables

!!! info Suffixed with `_custom`, these are available in case you wish to add values to a list or dictionary type setting, without dropping existing values.

Typical use would be to pass new Docker parameters:

```yaml
#### Extra mounts for Sonarr containers ####
sonarr_docker_volumes_custom:
  - "/mnt/unionfs/Media/Anime:/anime"
  - "/mnt/unionfs/Media/Kids:/kids"
```

## Additional Examples

### Various

```yaml
##### Plex Ports for local access#####
plex_open_main_ports: true
plex_open_local_ports: true

##### Plex Container Variables ####
plex_docker_image_tag: beta
plex_open_main_ports: true
plex_db_cache_size: 30000000

#### Examples of specified container images: ####
radarr_docker_image_tag: nightly
sonarr_docker_image_tag: nightly
petio_docker_image_tag: nightly

#### BW Limiting speeds ####
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

### Authelia App Bypass

Some may not want the additional layer of security that Authelia supplies, good news is that it can be disabled with a simple override. To determine which apps by default are included in Authelia, one can run this command or similar:

```shell
grep -Ril "_traefik_sso_middleware:" /srv/git/saltbox/roles /opt/sandbox/roles | awk 'BEGIN{RS="roles/"; FS="/defaults"}NF>1{print $1}' | sort -u
```

#### Override example

```yaml
### Authelia App Bypass ###
sonarr_traefik_sso_middleware: ""
tautulli_traefik_sso_middleware: ""
radarr_traefik_sso_middleware: ""
nzbget_traefik_sso_middleware: ""
prowlarr_traefik_sso_middleware: ""`
```

After making this change in the Inventory file, simply run the appropriate role command in order to disable Authelia on that specific app. Reminder you can run multiple tags at once.

### Authorize with App Credentials

#### Inject an Authorization header - Traefik performs basic auth with the backend app

This allows you to keep basic auth enabled within apps but not have the hassle of entering the credentials manually. The authorization header is only inserted if the request is authorized through the SSO middleware (Authelia) and is not applied to the API endpoint(s).

Use [this tool](https://www.blitter.se/utils/basic-authentication-header-generator/) to generate the header contents based on your credentials.

```yaml
sonarr_docker_labels_custom:
  traefik.http.middlewares.appAuth.headers.customrequestheaders.Authorization: "Basic <base64 header>"
sonarr_traefik_middleware_custom: "appAuth"
```

### Subdomain Customization

#### Overrides

```yaml
#### Make Organizr available only at the base domain ####
organizr_web_subdomain: ""

#### Make Tautulli available only at `stats.domain.tld` ####
tautulli_web_subdomain: "stats"
```

#### Additions

!!! warning The following examples require adding DNS records manually.

```yaml
#### Make Organizr available at both `organizr.domain.tld` and `domain.tld` ####
organizr_docker_labels_custom:
  traefik.http.routers.organizr-http.rule: "Host(`{{ organizr_web_subdomain + '.' + organizr_web_domain }}`) || Host(`{{ organizr_web_domain }}`)"
  traefik.http.routers.organizr.rule: "Host(`{{ organizr_web_subdomain + '.' + organizr_web_domain }}`) || Host(`{{ organizr_web_domain }}`)"

#### Make Overseerr available at both `overseerr.domain.tld` and `requests.domain.tld` ####
overseerr_docker_labels_custom:
  traefik.http.routers.overseerr-http.rule: "Host(`{{ overseerr_web_subdomain + '.' + overseerr_web_domain }}`) || Host(`{{ 'requests.' + overseerr_web_domain }}`)"
  traefik.http.routers.overseerr.rule: "Host(`{{ overseerr_web_subdomain + '.' + overseerr_web_domain }}`) || Host(`{{ 'requests.' + overseerr_web_domain }}`)"
```
