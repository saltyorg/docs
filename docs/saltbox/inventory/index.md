# Inventory

Advanced use cases that would normally require editing roles can now be handled through the inventory system instead. 

Any variables defined in `/srv/git/saltbox/roles/<role_name>/defaults/main.yml` are intended to be changeable by the user. This implementation avoids git merge conflicts when updating Saltbox.   **NOTE: This does not mean that file is intended to be edited.**  See below for details on how to override the standard values with your own.  Use these default files as a catalog of things you **can** change.

Should you require additional functionality then by all means create an issue on the [main repository](https://github.com/saltyorg/Saltbox/) and we'll look at accommodating it.

Overrides are done in the file `"/srv/git/saltbox/inventories/host_vars/localhost.yml"` [which does not exist by default].

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

If you wanted to change the name of the Sonarr app to BingBangBoing, you'd create a file at `/srv/git/saltbox/inventories/host_vars/localhost.yml` and put this into it:

``` yaml
sonarr_name: BingBangBoing
```

When you next run the `sonarr` tag, everything that's based off that name will change:

- docker container name => BingBangBoing
- subdomain => BingBangBoing.DOMAIN.TLD
- app data folder => /opt/BingBangBoing
- and so on.

A common use for these overrides will probably be changing the version of the docker container being used.

Looking further down in that defaults file:

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

We see again the name flowing through down here. but look at `sonarr_docker_image_tag: "release"`

By default, for Sonarr, Saltbox will use the docker image `hotio/sonarr:release`.

If you wanted to change that to "nightly", you'd add this line to `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

``` yaml
radarr_docker_image_tag: nightly
```

Which would override the default and result in Saltbox using `hotio/sonarr:nightly`.