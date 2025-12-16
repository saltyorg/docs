---
status: draft
hide:
  - tags
tags:
  - upgrade
  - role-refactor
  - inventory
---

# Role Refactor
 
The merge of the role-refactor branches introduces the following changes:

- Explicit [override levels](../inventory/index.md/#override-levels)

    > Variables that previously applied to all instances of a role (e.g., `sonarr_docker_image`) now strictly apply only to the instance with that exact name (e.g., `sonarr`).
        
    > To apply a variable to all instances of a role, use the `_role_` infix (e.g., `sonarr_role_docker_image`). 
        
    > Docker Network Mode Variables such as `plex_docker_network_mode_default` have been deprecated in favor of direct assignment (e.g., `plex_docker_network_mode`).

- Sandbox settings.yml deprecation

    > All Sandbox settings.yml overrides must be converted to their inventory format to continue applying.

- Golang rewrites of Python tools: Docker Controller, DNS Manager
- Roles removed: jaeger, readarr, sub_zero, webtools, alternatrr, aria2_ng, comicstreamer, docspell, rdtclient, solr, teamspeak, watchtower
- Docs overhaul

## Inventory Migration Examples

### Single-instance overrides

When a role only has a single instance, either variable form will achieve the same outcome. However, to align with the new convention, it is recommended to transition to the `_role_` infix.

```yaml
plex_dns_proxy: false
```

Becomes:

```yaml
plex_role_dns_proxy: false
```

### Multi-instance overrides

Multi-instance role variables must be transitioned to the appropriate override level for existing configuration to persist.

```yaml
bazarr_instances: ["bazarr", "bazarr4k"]
bazarr_docker_volumes_custom: ["/opt/subcleaner:/subcleaner"]
bazarr4k_themepark_theme: "dracula"
```

Becomes:

```yaml
bazarr_instances: ["bazarr", "bazarr4k"]
bazarr_role_docker_volumes_custom: ["/opt/subcleaner:/subcleaner"]
bazarr4k_themepark_theme: "dracula"
```
