---
hide:
  - tags
tags:
  - recyclarr
  - sonarr
  - radarr
---

# Recyclarr

## What is it?

[Recyclarr](https://github.com/recyclarr/recyclarr) automatically synchronizes recommended settings from TRaSH guides to your Sonarr/Radarr instances.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/recyclarr/recyclarr){: .header-icons } | [:octicons-link-16: Docs](https://recyclarr.dev/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/recyclarr/recyclarr){: .header-icons } | [:material-docker: Docker](https://ghcr.io/recyclarr/recyclarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-recyclarr

```

### 2. Setup

Edit the Recyclarr section in [sandbox `settings.yml`:](../settings.md) and enter your desired update schedule using standard cron syntax.

``` { .yaml }
     recyclarr:
       cron_schedule: "@daily"
```

!!! note
    If you change this value, you must re-run `sb install sandbox-recyclarr` for it take effect.

If a config file does not exist, a default config is generated but it is not functional out of the box. Edit the file `/opt/recyclarr/recyclarr.yml` to provision your Sonarr/Radarr details and preferred settings.

- Configure Sonarr section

  ``` { .yaml }
      sonarr:
        sonarr:
          base_url: http://sonarr:8989
          api_key: your_sonarr_api_key
  ```

- Configure Radarr section

  ``` { .yaml }
      radarr:
        radarr:
          base_url: http://radarr:7878
          api_key: your_radarr_api_key
  ```

Follow documentation to complete configuration

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
