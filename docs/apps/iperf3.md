---
icon: material/desktop-classic
title: iPerf3
hide:
  - tags
tags:
  - iperf3
  - network
  - performance
  - bandwidth
saltbox_automation:
  sections:
    inventory: false
  app_links:
  - name: Manual
    url: https://software.es.net/iperf/invoking.html#iperf3-manual-page
    type: documentation
  - name: Releases
    url: https://software.es.net/iperf/news.html
    type: releases
  - name: Community
    url: https://github.com/esnet/iperf/discussions
    type: github
  project_description:
    name: iPerf3
    summary: |
      a tool for active measurements of the maximum achievable bandwidth on IP networks, supporting TCP, UDP, and SCTP protocols over both IPv4 and IPv6.
    link: https://software.es.net/iperf
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# iPerf3

## Overview

[iPerf3](https://software.es.net/iperf) is a tool for active measurements of the maximum achievable bandwidth on IP networks, supporting TCP, UDP, and SCTP protocols over both IPv4 and IPv6.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://software.es.net/iperf/invoking.html#iperf3-manual-page){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](https://software.es.net/iperf/news.html){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/esnet/iperf/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install iperf3
```

## Usage

```shell
iperf3 --help
```

The binary built from source and installed to `/usr/local/bin/iperf3`. Run it manually from the command line in server mode (`iperf3 -s`) or client mode (`iperf3 -c <server_ip>`) as needed for network testing.
