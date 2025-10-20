---
hide:
  - tags
tags:
  - tvheadend
  - tv
  - streaming
---

# Tvheadend

## What is it?

[Tvheadend](https://tvheadend.org/) is a TV streaming server and digital video recorder.

It supports the following inputs:

- DVB-C(2)
- DVB-T(2)
- DVB-S(2)
- ATSC
- SAT>IP
- HDHomeRun
- IPTV
  - UDP
  - HTTP

It supports the following outputs:

HTTP
HTSP (own protocol)
SAT>IP

!!! info
    By default, the role **IS** protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://tvheadend.org/){: .header-icons } | [:octicons-link-16: Docs](https://docs.tvheadend.org/documentation){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/tvheadend/tvheadend){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/thealhu/tvheadend){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-tvheadend

```

### 2. URL

- To access Tvheadend, visit `https://tvheadend._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->