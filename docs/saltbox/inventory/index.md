# Inventory

Advanced use cases that would normally require editing roles can now be handled through the inventory system instead. 

Any variables defined in `/srv/git/saltbox/roles/<role_name>/defaults/main.yml` or `/opt/sandbox/roles/<role_name>/defaults/main.yml` are available to be overridden by the user in: 

`/srv/git/saltbox/inventories/host_vars/localhost.yml`

This implementation avoids git merge conflicts when updating Saltbox.

Should you require additional functionality then by all means create an issue on the [main repository](https://github.com/saltyorg/Saltbox/) and we'll look at accommodating it.

For example, an excerpt from `/srv/git/saltbox/roles/sonarr/defaults/main.yml`:

``` yaml
################################
# Basics
################################

sonarr_name: sonarr

################################
# Paths
################################

sonarr_paths_folder: "{{ sonarr_name }}"
sonarr_paths_location: "{{ server_appdata_path }}/{{ sonarr_paths_folder }}"
sonarr_paths_folders_list:
  - "{{ sonarr_paths_location }}"
sonarr_paths_config_location: "{{ sonarr_paths_location }}/config.xml"
...
```

We can see there that Sonarr gets the name "sonarr", and that name then flows through to those next four settings.

If you wanted to change the name of the Sonarr app to BingBangBoing, you'd add this to `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

``` yaml
sonarr_name: BingBangBoing
```

When you next run the `sonarr` tag, everything that's based off that name will change:

- docker container name => BingBangBoing
- subdomain => BingBangBoing.DOMAIN.TLD
- app data folder => /opt/BingBangBoing
- and so on.

A common use for these overrides will be specifying the version of the docker image to be used, so let's see how that's done by looking further down in the defaults file:

``` yaml
################################
# Docker
################################

# Container
sonarr_docker_container: "{{ sonarr_name }}"

# Image
sonarr_docker_image_pull: true
sonarr_docker_image_tag: "release"
sonarr_docker_image: "hotio/sonarr:{{ sonarr_docker_image_tag }}"
```

We see again the name flowing through down here, but look at `sonarr_docker_image_tag: "release"`

For Example, for Sonarr, Saltbox will use the docker image `hotio/sonarr:release` by default.

If you wanted to change that to "nightly", you'd add this line to `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

``` yaml
sonarr_docker_image_tag: "nightly"
```

Which would override the default and result in Saltbox using `hotio/sonarr:nightly` docker image instead.

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

#### Docker Service Variable ####
docker_service_sleep: 0
```

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
