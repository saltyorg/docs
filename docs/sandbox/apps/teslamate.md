# Teslamate

## What is it?

[Teslamate](https://github.com/teslamate-org/teslamate) is a powerful, self-hosted data logger for your Tesla.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/teslamate-org/teslamate){: .header-icons } | [:octicons-link-16: Docs](https://github.com/teslamate-org/teslamate){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/teslamate-org/teslamate){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/teslamate/teslamate){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-teslamate

```

### 2. URL

- To access Teslamate, visit `https://teslamate._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation: Teslamate Docs](https://docs.teslamate.org/docs/installation/docker){: .header-icons }

To use a custom subdomain, add a custom value for `teslamate_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

### 4. Grafana Setup

Once installation is finished, you will need to add the teslamate data source in grafana under connections.

Host URL: This is based upon the `{{ teslamate_name }}-postgres` variable. Default is `teslamate-postgres:5432`
Table: `teslamate`

Authentication for Postgres: Run the command below to have saltbox output the DB password.

``` shell

sb install sandbox-teslamate-grafana

```


Save and Test
