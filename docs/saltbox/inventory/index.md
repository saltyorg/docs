# Inventory

Advanced use cases that would normally require editing roles can now be handled through the inventory system instead. 

Any variables defined in `/srv/git/saltbox/roles/<role_name>/defaults/main.yml` or `/opt/sandbox/roles/<role_name>/defaults/main.yml` are available to be overridden by the user in: 

`/srv/git/saltbox/inventories/host_vars/localhost.yml`

This implementation avoids git merge conflicts when updating Saltbox.

Should you require additional functionality then by all means create an issue on the [main repository](https://github.com/saltyorg/Saltbox/) and we'll look at accommodating it.

A common use for these overrides will be specifying the version of the docker image to be used, so let's see how that's done by looking into `/srv/git/saltbox/roles/sonarr/defaults/main.yml` around line 85:

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

For Sonarr, Saltbox will use the docker image `cr.hotio.dev/hotio/sonarr:release` by default.

If you wanted to change that to "nightly", you'd add this line to `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

``` yaml
sonarr_docker_image_tag: "nightly"
```

Which would override the default [`release`] and result in Saltbox using the `cr.hotio.dev/hotio/sonarr:nightly` docker image instead, wihtout you modifying this file.  If you update Saltbox and this file is replaced, your tag change to `nightly` remains in effect.

Previously undefined variables may be added as well. Typical use would be to pass new Docker parameters under variables with the name ending in `custom`:

```yaml
jackett_docker_labels_custom:
  com.centurylinklabs.watchtower.enable: "true"
```

# Additional Examples
## Various
```yaml
### Open Specified Ports for the specified container ###
##### Plex Ports for local access#####
plex_docker_ports:
  - "32400:32400/tcp"
  - "3005:3005/tcp"
  - "8324:8324/tcp"
  - "33400:33400/tcp"
  - "33443:33443/tcp"

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
# Authelia App Bypass
Some may not want the additional layer of security that Autheli supplies, good news is that it can be disabled with an simple override. To determine which apps by default are included in Authelia, one can run this command or similar:

`grep -Ril "_traefik_sso_middleware:" /srv/git/saltbox/roles /opt/sandbox/roles | awk 'BEGIN{RS="roles/"; FS="/defaults"}NF>1{print $1}' | sort -u`

### Override example:
```
### Authelia App Bypass ###
sonarr_traefik_sso_middleware: ""
tautulli_traefik_sso_middleware: ""
radarr_traefik_sso_middleware: ""
nzbget_traefik_sso_middleware: ""
prowlarr_traefik_sso_middleware: ""`
```
After making this change in the inventory file, simply run the appropriate role command in order to disable Authelia on that specific app. Reminder you can run multiple tags at once.

## Subdomain Customization
### Overrides:
```yaml
#### Make Organizr available only at the base domain ####
organizr_web_subdomain: ""

#### Make Tautulli available only at `stats.domain.tld` ####
tautulli_web_subdomain: "stats"
```
### Additions:
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
Note that this last set of examples requires you to add DNS records manually.
