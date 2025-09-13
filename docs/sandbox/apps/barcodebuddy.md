---
hide:
  - tags
tags:
  - barcodebuddy
  - grocy
  - inventory
---

# BarcodeBuddy

## What is it?

[BarcodeBuddy](https://github.com/Forceu/barcodebuddy) is a barcode system for Grocy that enables barcode scanning and product management. It automatically handles known and unknown barcodes, integrating seamlessly with Grocy's inventory management system.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will need to configure authentication within the application.

| Details     |             |             |
|-------------|-------------|-------------|
| [:octicons-mark-github-16: Github](https://github.com/Forceu/barcodebuddy){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/f0rc3/barcodebuddy){: .header-icons } | [:octicons-link-16: Docs](https://barcodebuddy-documentation.readthedocs.io/){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-barcodebuddy
```

### 2. URL

- To access BarcodeBuddy, visit `https://barcodebuddy._yourdomain.com_`

### 3. Setup

Configure the connection to your Grocy instance through the application settings and set up user authentication.