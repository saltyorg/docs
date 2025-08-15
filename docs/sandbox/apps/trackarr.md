---
hide:
  - tags
tags:
  - trackarr
  - automation
  - tracker
---

# Trackarr

## What is it?

[Trackarr](https://gitlab.com/cloudb0x/trackarr) monitors tracker announce IRC channel, parses the announcements, and forwards those announcements to ARR PVRs (eg Sonarr/Radarr).

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will have to log into the app itself (basic auth).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://gitlab.com/cloudb0x/trackarr){: .header-icons } | [:octicons-link-16: Docs](https://gitlab.com/cloudb0x/trackarr/-/wikis/Configuration){: .header-icons } | [:octicons-mark-github-16: Gitlab](https://gitlab.com/cloudb0x/trackarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/cloudb0x/trackarr){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-trackarr
```

### 2. Setup

- Default login:

  ``` { .yaml}
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

The `trackarr` role will provision a config file with your pvr and server info. After you run the role, you will need to set up your config. [Here](https://gitlab.com/cloudb0x/trackarr/-/wikis/Configuration/Sample) is an example config from the wiki that has a broader example of possible options and tracker configuration.

### 3. URL

- To access Trackarr, visit `https://trackarr._yourdomain.com_`

- [:octicons-link-16: Documentation: Trackarr Docs](https://gitlab.com/cloudb0x/trackarr/-/wikis/Configuration){: .header-icons }
