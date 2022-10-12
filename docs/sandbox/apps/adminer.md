# Adminer

## What is it?

[Adminer](https://www.adminer.org/){: target=_blank rel="noopener noreferrer" } is a popular and feature rich Open Source administration and development platform for PostgreSQL.

!!!info 
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself. 

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://www.adminer.org/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/vrana/adminer/#readme){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/vrana/adminer){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/_/adminer/){: .header-icons target=_blank rel="noopener noreferrer" }|


### 1. Installation

``` shell

sb install sandbox-Adminer

```

### 2. URL

- To access Adminer, visit `https://adminer._yourdomain.com_`

### 3. Setup

- Default login for [mariadb](../../saltbox/support%20apps/mariadb.md)
  ``` { .yaml}
  System: Mysql
  Server: mariadb:3306
  Username: root
  Password: password321
  ```

- Default login for [postgres](../../saltbox/support%20apps/postgres.md)
  ``` { .yaml}
  System: PostgreSQL
  Server: postgres:5432
  Username: your_saltbox_user
  Password: password4321
  ```

- [:octicons-link-16: Documentation: Adminer Docs](https://github.com/vrana/adminer/#readme){: .header-icons target=_blank rel="noopener noreferrer" }
