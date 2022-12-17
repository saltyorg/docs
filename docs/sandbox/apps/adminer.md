# Adminer

## What is it?

[Adminer](https://www.adminer.org/){: target=_blank rel="noopener noreferrer" } Adminer (formerly phpMinAdmin) is a full-featured database management tool written in PHP. Adminer is available for MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Elasticsearch, MongoDB and others via plugin.

!!!info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.adminer.org/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/vrana/adminer/#readme){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/vrana/adminer){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/_/adminer/){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-adminer

```

### 2. URL

- To access Adminer, visit `https://adminer._yourdomain.com_`

### 3. Setup

- Default login for [mariadb](../../apps/mariadb.md)

```yaml
  System: Mysql
  Server: mariadb:3306
  Username: root
  Password: password321
  ```

- Default login for [postgres](../../apps/postgres.md)
  
``` { .yaml}
  System: PostgreSQL
  Server: postgres:5432
  Username: your_saltbox_user
  Password: password4321
  ```

- [:octicons-link-16: Documentation: Adminer Docs](https://github.com/vrana/adminer/#readme){: .header-icons target=_blank rel="noopener noreferrer" }
