# Themepark Styles

Saltbox can apply themes from [ThemePark](https://docs.theme-park.dev/theme-options/) to supported applications through the inventory.

For example:

NZBGet default appearance:

![](images/nzbget-before.png)


NZBGet with the "nord" theme:

![](images/nzbget-nord.png)


Choose the theme and apply it to containers in in inventory:

```
# global theme
global_themepark_theme: "nord"

# apps using global theme:
container_name_themepark_enabled: "true"

# different theme for an app:
container_name_themepark_theme: "hotline"
container_name_themepark_enabled: "true"

```
for example, in `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

```
# Instructions on how to utilize this file can be found here https://docs.saltbox.dev/saltbox/inventory/

# global theme
global_themepark_theme: "nord"

# apps using global theme:
nzbget_themepark_enabled: "true"

# different theme for an app:
sonarr_themepark_theme: "hotline"
sonarr_themepark_enabled: "true"
```

Available themes can be found [here](https://docs.theme-park.dev/theme-options/).  Refer to them in the inventory file by name:

```
organizr
dark
dracula
aquamarine
space gray
plex
hotline
hotpink
overseerr
nord
maroon
```
