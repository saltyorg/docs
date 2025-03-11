# phpmyadmin

## What is it?

[phpmyadmin](https://www.phpmyadmin.net/) is a free software tool written in PHP, intended to handle the administration of MySQL over the Web. phpMyAdmin supports a wide range of operations on MySQL and MariaDB. Frequently used operations (managing databases, tables, columns, relations, indexes, users, permissions, etc) can be performed via the user interface, while you still have the ability to directly execute any SQL statement.

- Intuitive web interface
- Support for most MySQL features:
  - browse and drop databases, tables, views, fields and indexes
  - create, copy, drop, rename and alter databases, tables, fields and indexes
  - maintenance server, databases and tables, with proposals on server configuration
  - execute, edit and bookmark any SQL-statement, even batch-queries
  - manage MySQL user accounts and privileges
  - manage stored procedures and triggers
- Import data from CSV and SQL
- Export data to various formats: CSV, SQL, XML, PDF, ISO/IEC 26300 - OpenDocument Text and Spreadsheet, Word, LATEX and others
- Administering multiple servers
- Creating graphics of your database layout in various formats
- Creating complex queries using Query-by-example (QBE)
- Searching globally in a database or a subset of it
- Transforming stored data into any format using a set of predefined functions, like displaying BLOB-data as image or download-link

!!!info
    By default, the role **IS** protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.phpmyadmin.net/){: .header-icons } | [:octicons-link-16: Docs](https://www.phpmyadmin.net/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/phpmyadmin/phpmyadmin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/phpmyadmin/phpmyadmin/){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-phpmyadmin

```

### 2. URL

- To access phpmyadmin, visit `https://phpmyadmin._yourdomain.com_`

- [:octicons-link-16: Documentation: phpmyadmin Docs](https://www.phpmyadmin.net/docs/){: .header-icons }
