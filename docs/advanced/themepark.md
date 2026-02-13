---
status: outdated
hide:
  - tags
tags:
  - themepark
---

# Themepark Styles

Saltbox can apply themes from [ThemePark](https://docs.theme-park.dev/theme-options/) to supported applications through the inventory. Themes are applied via the [Traefik Plugin](https://github.com/packruler/traefik-themepark) which performs CSS replacement at the reverse proxy (rather than application) level.

Plugin note: You must run `sb install traefik` once after setting `global_themepark_plugin_enabled: true` in order to provision the theme middlewares.

For example:

NZBGet default appearance:

![NZBGet interface showing default appearance before theme application](images/nzbget-before.png)

NZBGet with the "nord" theme:

![NZBGet interface with nord theme applied showing dark color scheme](images/nzbget-nord.png)

Sonarr with the "hotline" theme:

![Sonarr interface with hotline theme showing bright pink and dark styling](images/sonarr-hotline.png)

Choose the theme and apply it to containers in in inventory:

```yaml
# global theme
global_themepark_theme: "nord"

# enable Traefik plugin
global_themepark_plugin_enabled: true

# apps using global theme:
container_name_themepark_enabled: true

# different theme for an app:
container_name_themepark_theme: hotline
container_name_themepark_enabled: true

# addons for compatible apps
container_name_themepark_addons: ["addon1", "addon2"]
```

for example, in `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

```yaml
# Instructions on how to utilize this file can be found here https://docs.saltbox.dev/saltbox/inventory/

# global theme
global_themepark_theme: "nord"

# apps using global theme:
nzbget_themepark_enabled: true

# different theme for an app:
sonarr_themepark_theme: "hotline"
sonarr_themepark_enabled: true

# sonarr 4k logo for `sonarr4k` instance
sonarr4k_themepark_addons: ["sonarr-4k-logo"]

# enable Traefik plugin
global_themepark_plugin_enabled: true

# apps using Traefik plugin
plex_themepark_enabled: true
nzbhydra2_themepark_enabled: true
```

Available themes can be found in the [Theme Park documentation](https://docs.theme-park.dev/theme-options/) and [Community](https://docs.theme-park.dev/community-themes/). Refer to them in the inventory file by name:

```text
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

Note: If you are utilizing Theme.Park on any roles, you must run `sb install traefik` after changing any themes via inventory variables.

List of roles that support Theme.Park on the Saltbox side can be found by running:

```shell
(grep -Ril "_themepark_enabled: false" /srv/git/saltbox/roles | cut -d/ -f6; grep -Ril "_themepark_enabled: false" /opt/sandbox/roles | cut -d/ -f5) | sort -u
```
