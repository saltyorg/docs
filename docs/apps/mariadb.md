# MariaDB

## What is it?

[MariaDB](https://mariadb.org/){: target=_blank rel="noopener noreferrer" } MariaDB Server is one of the most popular open source relational databases. It’s made by the original developers of MySQL and guaranteed to stay open source.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://mariadb.org/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://mariadb.org/documentation/#getting-started){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/docker-library/official-images/blob/master/library/mariadb){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/_/mariadb){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install mariadb

```

### 2. Setup

!!!info
    The default password for this container is `password321`
    To easily manage the db, consider [adminer](/sandbox/apps/adminer.md)

### Migration Notes

Saltbox recently swapped Docker images used for MariaDB. The migration path that is run for a default `mariadb` instance is roughly as follows:

1. Dump all data to a dump.sql file
2. Move `/opt/mariadb` to `/opt/mariadb_legacy`
3. Provision a new `mariadb` container
4. Import the dump.sql file

The dump file remains on disk at `/opt/mariadb_legacy/dump.sql` post-migration in the event manual intervention is required and the appdata for the legacy image remains on disk at `/opt/mariadb_legacy`.

- [:octicons-link-16: Documentation: MariaDB Docs](https://mariadb.org/documentation/#getting-started){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Documentation: Docker Image Docs](https://github.com/docker-library/docs/blob/master/mariadb/README.md){: .header-icons target=_blank rel="noopener noreferrer" }
