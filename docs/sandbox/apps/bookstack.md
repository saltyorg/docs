---
hide:
  - tags
tags:
  - bookstack
  - wiki
  - documentation
---

# BookStack

## What is it?

[BookStack](https://www.bookstackapp.com/) is a simple, self-hosted, easy-to-use platform for organising and storing information.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.bookstackapp.com/){: .header-icons } | [:octicons-link-16: Docs](https://www.bookstackapp.com/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/BookStackApp/BookStack){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/bookstack){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-bookstack

```

### 2. URL

- To access BookStack, visit `https://bookstack._yourdomain.com_`

### 3. Setup

- Log in using the default admin details `admin@admin.com` with a password of `password`. You should change these details **immediately** after logging in for the first time.

- Optional configuration such as SMTP can be done by editing the `.env` file located at: 

```
/opt/bookstack/www/.env
```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
