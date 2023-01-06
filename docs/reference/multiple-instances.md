---
hide:
  - tags
tags:
  - radarrx
  - radarr4k
  - sonarrx
  - sonarr4k
---

# Multiple App Instances

Apps that used to be supported by the "ArrX" system which allowed the user to define a set of instances of a given app [as opposed to installing multiple instances one at a time] are being transitioned to a new generalized, inventory-driven approach.

The general idea is to move all the configuration into the `/srv/git/saltbox/inventories/host_vars/localhost.yml` along with [other customizations](../saltbox/inventory/index.md).

As of 01-24-2023 the roles supported are:

```yaml
autoscan
bazarr
deluge
emby
jellyfin
jellyseerr
lidarr
mcrouter
minecraft
nginx
node_red
overseerr
plex
qbittorrent
qbittorrentvpn
radarr
readarr
sonarr
tautulli
mariadb
postgres
mongodb
redis
traktarr
whisparr
```

There is a command at the end of this page you can use to get an updated list of roles that support this method.

## Overview

Define a list of all the instances of the container you want to create; if you don't want to customize them beyond that, this is all that's required.

Add the list to the [inventory file](../saltbox/inventory/index.md) at `/srv/git/saltbox/inventories/host_vars/localhost.yml`, formatted as so:

```yaml
sonarr_instances: ["sonarr", "sonarrbing", "sonarrbang", "sonarrboing"]
```

Run the standard app tag [in this case `sb install sonarr`] to set up all the instances you've defined.  If you attempt to run any of your new instance names as tags, the install will fail with an error.  Run ONLY the standard app tag.  If one or more of the instances already exist, their existing configurations *TYPICALLY* will not be touched or overwritten, though this is dependent on the specific role.  If the standard role overwrites or modifies the configuration, then so will this, since it's calling the standard role for each instance.

!!! info
    Note that the first entry in the list is `sonarr`, the standard instance of the app.  You probably want to follow this pattern, since other tags might iterate through this list of "sonarr"s to take some action and if an instance is not listed here it will be skipped in that case.

    This list should include *all* instances of the app that you want to end up with, *including* the stock one if you are retaining it.

    ```yaml
    sonarr_instances: ["sonarr", "sonarrbing", "sonarrbang", "sonarrboing"]
    ```
    not
    ```yaml
    sonarr_instances: ["sonarrbing", "sonarrbang", "sonarrboing"]
    ```

Given the example above, `sb install sonarr` would install:

| List entry    | Container Name | Config Directory   | Subdomain                    |
| ------------- | -------------- | ------------------ | ---------------------------- |
| sonarr        | sonarr         | `/opt/sonarr`      | sonarr.YOURDOMAIN.TLD        |
| sonarrbing    | sonarrbing     | `/opt/sonarrbing`  | sonarrbing.YOURDOMAIN.TLD    |
| sonarrbang    | sonarrbang     | `/opt/sonarrbang`  | sonarrbang.YOURDOMAIN.TLD    |
| sonarrboing   | sonarrboing    | `/opt/sonarrboing` | sonarrboing.YOURDOMAIN.TLD   |

Those names have to be unique across all of your containers, so it is suggested that you keep with the `rolename+suffix` pattern for these additional instances.

### Per-instance customization

You can edit the following set of variables on a per instance basis in `localhost.yml`:

!!! note
    Replacing "instance" with the actual **instance name**, of course, i.e. `sonarrbing_web_subdomain`, etc.

!!! note
    For instances that contain a dash (`-`) in the name, the variables will replace the instance name's dash with an underscore (`_`). i.e. instead of `sonarr-bong_web_subdomain` the variable would be `sonarr_bong_web_subdomain`.

```text
instance_web_subdomain
instance_web_domain
instance_web_port
instance_traefik_sso_middleware
instance_docker_image_repo
instance_docker_image_tag
instance_docker_ports_defaults
instance_docker_ports_ui
instance_docker_ports_custom
instance_themepark_enabled
instance_themepark_domain
instance_themepark_theme
instance_docker_envs_default
instance_docker_envs_custom
instance_docker_commands_default
instance_docker_commands_custom
instance_docker_volumes_default
instance_docker_volumes_custom
instance_docker_volumes_theme
instance_docker_devices_default
instance_docker_devices_custom
instance_docker_hosts_default
instance_docker_hosts_custom
instance_docker_labels_default
instance_docker_labels_custom
instance_docker_network_mode_default
instance_docker_networks_default
instance_docker_networks_custom
instance_docker_capabilities_default
instance_docker_capabilities_custom
instance_docker_security_opts_default
instance_docker_security_opts_custom
```

### Getting an updated list of supported roles

You can find roles that support this new method with the following command:

```shell
grep -Ril "_instances:" /srv/git/saltbox/roles /opt/sandbox/roles | awk 'BEGIN{RS="roles/"; FS="/defaults"}NF>1{print $1}' | sort -u
```

### What about roles that aren't listed here?

You can create multiple instances of nearly any role with an environment variable:

For example, this will install a single standard instance of photoprism:

```shell
sb install sandbox-photoprism
```

Then if you wanted a second at `photoprism_again.DOMAIN.TLD`:

```shell
sb install sandbox-photoprism  -e photoprism_name=photoprism_again
```


