---
hide:
  - tags
tags:
  - comic
---

# ComiXed

## What is it?

[ComiXed](https://github.com/comixed/comixed) is an application for managing digital comics. It seeks to be the ultimate management tool for digital comic books. 

It does the following and more:

- Scrape metadata for comics from various sources, such as ComicVine.
- Update the ComicInfo.xml file within each comic with the current metadata.

It is NOT:

- A comic reading application.

!!!note
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/comixed/comixed){: .header-icons } | [:octicons-link-16: Docs](https://github.com/comixed/comixed/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/comixed/comixed){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/comixed/comixed){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-comixed

```

### 2. URL

- To access ComiXed, visit `https://comixed._yourdomain.com_`

### 3. Setup

!!!info
    📢 ComiXed has 2 default users created when you run the role. It is a good idea to change the passwords for each account from the default asap.

``` shell
Username: comixedadmin@localhost
Password: comixedadmin
```

``` shell
Username: comixedreader@localhost
Password: comixedreader
```

- [:octicons-link-16: Documentation: Comixed Docs](https://github.com/comixed/comixed/wiki){: .header-icons }
