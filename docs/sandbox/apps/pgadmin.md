---
hide:
  - tags
tags:
  - pgadmin
  - database
  - admin
---

# pgadmin

## What is it?

[pgadmin](https://www.pgadmin.org/) is a popular and feature rich Open Source administration and development platform for PostgreSQL.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.pgadmin.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.pgadmin.org/docs/pgadmin4/6.14/getting_started.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pgadmin-org/pgadmin4){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/dpage/pgadmin4/){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-pgadmin

```

### 2. URL

- To access pgadmin, visit `https://pgadmin._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: "your email from accounts.yml"
  Password: your_normal_password
  ```

- [:octicons-link-16: Documentation: pgadmin Docs](https://www.pgadmin.org/docs/){: .header-icons }
