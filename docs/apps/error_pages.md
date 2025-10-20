---
hide:
  - tags
tags:
  - error-pages
  - traefik
  - error-handling
---

# Error Pages

## What is it?

Custom error pages that display when services return HTTP errors (400-599). Deployed automatically with Traefik.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/tarampampam/error-pages){: .header-icons } | [:octicons-link-16: Docs](https://github.com/tarampampam/error-pages){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/tarampampam/error-pages){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/tarampampam/error-pages){: .header-icons }|

## Installation

Enable in `adv_settings.yml`:

```yaml
traefik:
  error_pages: yes
```

Then install/update Traefik:

```shell
sb install traefik
```

## Configuration

### Change Template

Change the template in your [inventory](../saltbox/inventory/index.md):

```yaml
error_pages_role_template: "ghost"
```

Available templates: `l7` (default), `ghost`, `noise`, `hacker-terminal`, `shuffle`, `lost-in-space`, `app-down`, `connection`, and [more](https://github.com/tarampampam/error-pages).

Rebuild after changing:

```shell
sb install traefik
```

### Disable for Specific Apps

Disable error pages for specific apps in your [inventory](../saltbox/inventory/index.md):

```yaml
plex_role_traefik_error_pages_enabled: false
```

## Notes

- Error pages stored in `/opt/error-pages/`
- Pre-generated at install time from selected template
- Applied globally via Traefik middleware
- Manual edits overwritten on rebuild

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->