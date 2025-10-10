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

A customizable error page service that integrates with Traefik to display beautiful, themed error pages for HTTP errors (400-599). Instead of showing default browser error pages, this service provides professionally designed error pages that match your chosen template.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/tarampampam/error-pages){: .header-icons } | [:octicons-link-16: Docs](https://github.com/tarampampam/error-pages){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/tarampampam/error-pages){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/tarampampam/error-pages){: .header-icons }|

### 1. Installation

``` shell

sb install error_pages

```

### 2. Setup

#### Configuration

The error pages are automatically integrated with Traefik and will handle all HTTP errors (status codes 400-599) across your Saltbox services.

#### Template Selection

The default template is `l7`, but you can choose from various templates available in the [error-pages project](https://github.com/tarampampam/error-pages). To change the template, set the following in your inventory:

```yaml
error_pages_role_template: "ghost"  # or any other available template
```

Available templates include:
- `l7` (default)
- `ghost`
- `noise`
- `hacker-terminal`
- `shuffle`
- `lost-in-space`
- `app-down`
- `connection`
- And more (check the project repository for all options)

#### How It Works

When any service behind Traefik returns an HTTP error (4xx or 5xx):
1. Traefik intercepts the error response
2. The request is forwarded to the error-pages service
3. The error-pages service returns a styled HTML page matching the error code
4. The user sees a professional error page instead of a blank browser error

#### Error Pages Location

Static error pages are generated and stored in `/opt/error-pages/` on the host system.

#### Customization

If you want to customize the error pages further, you can:
1. Modify the files in `/opt/error-pages/`
2. Or rebuild the pages by reinstalling the role

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
