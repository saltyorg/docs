---
hide:
  - tags
tags:
  - paperless-ngx
  - productivity
  - documents
---

# Paperless NGX

## What is it?

[Paperless NGX](https://github.com/paperless-ngx/paperless-ngx#paperless-ngx) is a simple Django application running in two parts: a Consumer (the thing that does the indexing) and the Web server (the part that lets you search & download already-indexed documents).

Paperless-NGX is forked from paperless-ng to continue the great work and distribute responsibility of supporting and advancing the project among a team of people.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/paperless-ngx/paperless-ngx#paperless-ngx){: .header-icons } | [:octicons-link-16: Docs](https://paperless-ngx.readthedocs.io/en/latest/index.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/paperless-ngx/paperless-ngx){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/paperlessngx/paperless-ngx){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-paperless-ngx

```

### 2. URL

- To access pgadmin, visit `https://paperless._yourdomain.com_`

### 3. Setup

!!! info
    Please refer to [this](https://github.com/saltyorg/docs/issues/116#issuecomment-1278733921) comment on the initial PR for questions about google storage!

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->