# Varken

## What is it?

[Varken](https://github.com/Boerderij/Varken){: target=_blank rel="noopener noreferrer" } is Dutch for **PIG**. PIG is an Acronym for **P**lex/**I**nfluxDB/**G**rafana

Varken is a standalone application to aggregate data from the Plex ecosystem into InfluxDB using Grafana for a frontend

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Boerderij/Varken){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://wiki.cajun.pro/books/varken){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Boerderij/Varken){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/boerderij/varken){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-varken

```

### 2. URL

- To access the Varken dashboard, visit `https://grafana._yourdomain.com_`

### 3. Setup

1. Run the Saltbox varken role to install varken/influxdb/telegraf/grafana:

    ``` { .shell }

        sb install sandbox-varken

    ```

2. Add your Maxmind API key to varken.ini:

    ``` { .shell }

        nano /opt/varken/varken.ini

    ```

3. Restart Varken:

    ``` { .shell }

        docker restart varken

    ```

4. Visit grafana `https://grafana._yourdomain.com_`

      - The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#configuration) file located in `/srv/git/saltbox/accounts.yml`

5. Add data source InfluxDB named InfluxDB:

      1. **HTTP**: URL = `http://influxdb:8086`

      2. **InfluxDB Details**: Database = varken

      3. Save & Test

6. Add data source InfluxDB named Telegraf:

      1. **HTTP**: URL = `http://influxdb:8086`

      2. **InfluxDB Details**: Database = telegraf

      3. Save & Test

7. You can find an example dashboard [here](https://raw.githubusercontent.com/thezak48/Varken/develop/dashboard_overseerr.json) which can be uploaded or pasted into Grafana to import.

- For app specific instructions refer to the [grafana role](../../sandbox/apps/grafana.md) and the upstream documentation [:octicons-link-16: Documentation](https://wiki.cajun.pro/books/varken){: .header-icons target=_blank rel="noopener noreferrer" }
