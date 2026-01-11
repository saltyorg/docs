---
icon: material/docker
hide:
  - tags
tags:
  - varken
  - monitoring
  - analytics
saltbox_automation:
  sections:
    inventory: false
  app_links:
  - name: Manual
    url:
    type: documentation
  - name: Releases
    url: https://github.com/thezak48/Varken/pkgs/container/varken
    type: github
  - name: Community
    url:
    type: community
  project_description:
     name: Varken
     summary: |
        a standalone application to aggregate data from the Plex ecosystem into InfluxDB using Grafana for a frontend.
     link: https://github.com/thezak48/Varken
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Varken

## Overview

[Varken](https://github.com/thezak48/Varken) is a standalone application to aggregate data from the Plex ecosystem into InfluxDB using Grafana for a frontend.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/thezak48/Varken/pkgs/container/varken){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-varken
```

## Usage

Visit <https://grafana.iYOUR_DOMAIN_NAMEi>.

## Basics

1. Run the Saltbox varken role to install varken/influxdb/telegraf/grafana:

    ```shell
    sb install sandbox-varken
    ```

2. Add your Maxmind API key to varken.ini:

    ```shell
    nano /opt/varken/varken.ini
    ```

3. Restart Varken:

    ```shell
    docker restart varken
    ```

4. Visit grafana <https://grafana.iYOUR_DOMAIN_NAMEi>

      - The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

5. Add data source InfluxDB named InfluxDB:

      1. **HTTP**: URL = `http://influxdb:8086`

      2. **InfluxDB Details**: Database = varken

      3. Save & Test

6. Add data source InfluxDB named Telegraf:

      1. **HTTP**: URL = `http://influxdb:8086`

      2. **InfluxDB Details**: Database = telegraf

      3. Save & Test

7. You can find an example dashboard [here](https://raw.githubusercontent.com/thezak48/Varken/develop/dashboard_overseerr.json) which can be uploaded or pasted into Grafana to import.

- For app specific instructions refer to the [grafana role](../../apps/grafana.md) and the upstream documentation
