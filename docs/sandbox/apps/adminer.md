# Adminer

## What is it?

[Adminer](https://www.adminer.org/) Adminer (formerly phpMinAdmin) is a full-featured database management tool written in PHP. Adminer is available for MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Elasticsearch, MongoDB and others via plugin.

!!!info "Protected Role"
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.adminer.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/vrana/adminer/#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/vrana/adminer){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/adminer/){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-adminer

```

### 2. URL

- To access Adminer, visit `https://adminer._yourdomain.com_`

### 3. Setup

- Default login for [MariaDB](../../apps/mariadb.md)

``` yaml title="Adminer Mariadb Login"
  System: Mysql
  Server: mariadb:3306
  Username: root
  Password: password321
```

- Default login for [Postgres](../../apps/postgres.md)

``` yaml title="Adminer Postgres Login"
  System: PostgreSQL
  Server: postgres:5432
  Username: your_saltbox_user
  Password: password4321
```

??? tip "Adminer Plugins"
    Adminer has a number of plugins available to extend its functionality. You can find them [here](https://www.adminer.org/en/plugins/).

- [:octicons-link-16: Documentation: Adminer Docs](https://github.com/vrana/adminer/#readme){: .header-icons }
