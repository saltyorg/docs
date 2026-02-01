---
hide:
  - tags
tags:
  - radarrx
  - radarr4k
  - sonarrx
  - sonarr4k
  - multiple
---

# Multiple App Instances

Apps that used to be supported by the "ArrX" system which allowed the user to define a set of instances of a given app (as opposed to installing multiple instances one at a time) are being transitioned to a new generalized, inventory-driven approach.

The general idea is to move all the configuration into the `/srv/git/saltbox/inventories/host_vars/localhost.yml` along with [other customizations](../saltbox/inventory/index.md).

**As of 01-23-2024** the roles supported are:

```yaml
autoscan
bazarr
calibre
deluge
emby
gluetun
jellyfin
jellyseerr
lgsm
lidarr
mariadb
mcrouter
minecraft
mongodb
nginx
node_red
ombi
overseerr
plex
postgres
qbittorrent
qbittorrentvpn
radarr
redis
requestrr
rflood
sonarr
tautulli
traktarr
transmission
watchstate
whisparr
```

IMPORTANT: if you ware reading this after the date mentioned above, this list may not be complete.

There is a command at the end of this page you can use to get an updated list of roles that support this method.

Again, that list shows what roles supported this system as of the date shown above; if you are reading this after that date, there is a non-zero chance that additional roles have been added.

## Overview

Define a list of all the instances of the container you want to create; if you don't want to customize them beyond that, this is all that's required.

Add the list to the [inventory file](../saltbox/inventory/index.md) at `/srv/git/saltbox/inventories/host_vars/localhost.yml`, formatted as so:

```yaml
sonarr_instances: ["sonarr", "sonarr4k", "sonarranime", "sonarrkids"]
```

Run the standard app tag (in this case `sb install sonarr`) to set up all the instances you've defined. If you attempt to run any of your new instance names as tags, the install will fail with an error. Run ONLY the standard app tag. If one or more of the instances already exist, their existing configurations *TYPICALLY* will not be touched or overwritten, though this is dependent on the specific role. If the standard role overwrites or modifies the configuration, then so will this, since it's calling the standard role for each instance.

!!! info

    While the first entry in the list is `sonarr` in the above example, you are not required to include an instance named `sonarr`. The list should include *all* instances of the app you want to end up with, regardless of their names. If an instance is not listed here, it will be skipped by actions that iterate through this list.

    For example:

    ```yaml
    sonarr_instances: ["sonarrhd", "sonarr4k", "sonarranime", "sonarrkids"]
    ```

    is valid if you want `sonarrhd` to be your primary instance instead of `sonarr`.

    ```yaml
    sonarr_instances: ["sonarr4k", "sonarranime", "sonarrkids"]
    ```

    would shift the primary instance to `sonarr4k` and create only those three instances.

Given the first example, `sb install sonarr` would install:

| List entry  | Container Name | Config Directory   | Subdomain                      |
|-------------|----------------|--------------------|--------------------------------|
| sonarr      | sonarr         | `/opt/sonarr`      | sonarr.xYOUR_DOMAIN_NAMEx      |
| sonarr4k    | sonarr4k       | `/opt/sonarr4k`    | sonarr4k.xYOUR_DOMAIN_NAMEx    |
| sonarranime | sonarranime    | `/opt/sonarranime` | sonarranime.xYOUR_DOMAIN_NAMEx |
| sonarrkids  | sonarrkids     | `/opt/sonarrkids`  | sonarrkids.xYOUR_DOMAIN_NAMEx  |

Those names have to be unique across all of your containers, so it is suggested that you keep with the `rolename+suffix` pattern for these additional instances.

### Per-instance customization

You can edit the following set of variables on a per instance basis in `localhost.yml`:

!!! note
    Replacing "instance" with the actual **instance name**, of course, i.e. `sonarr4k_web_subdomain`, etc.

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

Then if you wanted a second at `photoprism_again.xYOUR_DOMAIN_NAMEx`:

```shell
sb install sandbox-photoprism  -e photoprism_name=photoprism_again
```
