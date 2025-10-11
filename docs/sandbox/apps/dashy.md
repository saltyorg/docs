---
hide:
  - tags
tags:
  - dashy
  - dashboard
  - homepage
---

# Dashy

## What is it?

[Dashy](https://dashy.to/) is the "Ultimate homepage for your homelab"

- **Theming**
  - With tons of built-in themes to choose form, plus a UI color palette editor, you can have a unique looking dashboard in no time. There is also support for custom CSS, and since all properties use CSS variables, it is easy to override.
- **Icons**
  - Dashy can auto-fetch icons from the favicon of each of your apps/ services. There is also native support for Font Awesome, Material Design Icons, emoji icons and of course normal images.
- **Status Indicators**
  - Get an instant overview of the health of each of your apps with status indicators. Once enabled, a small dot next to each app will show weather it is up and online, with more info like response time visible on hover.
- **Authentication**
  - Need to protect your dashboard, the simple auth feature is super quick to enable, and has support for multiple users with granular controls. Dashy also has built-in support for Keycloak and other SSO providers.
- **Widgets**
  - Display dynamic content from any API-enabled service. Dashy comes bundled with 50+ pre-built widgets for self-hosted services, productivity and monitoring.
- **Search & Shortcuts**
  - To search, just start typing, results will be filtered instantly. Use the arrow keys or tab to navigate through results, and press enter to launch. You can also create custom shortcuts for frequently used apps, or add custom tags for easier searching. Dashy can also be used to search the web using your favorite search engine.
- **Configuration**
  - Dashy's config is specified in a simple YAML file. But you can also configure the directly through the UI, and have changes written to, and backed up on disk. Real-time validation and hints are in place to help you.
- **Customizable Layouts**
  - Structure your dashboard to fit your use case. From the UI, you can choose between different layouts, item sizes, show/ hide components, switch themes plus more. You can customize pretty much every area of your dashboard. There are config options for custom header, footer, nav bar links, title etc. You can also choose to hide any elements you don't need.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://dashy.to/){: .header-icons } | [:octicons-link-16: Docs](https://dashy.to/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Lissy93/dashy){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/lissy93/dashy){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-dashy

```

### 2. URL

- To access dashy, visit `https://dashy._yourdomain.com_`

### 3. Setup

To edit your config, edit the `.yaml` file in dashys appdata folder, which is typically located at `/opt/dashy/`. You can also edit the config directly through the UI.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
