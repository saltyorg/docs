---
icon: material/desktop-classic
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
---

# iperf3

## Overview

[iperf3](https://software.es.net/iperf) is a network performance measurement tool that can test TCP, UDP, and SCTP bandwidth. This role builds and installs the latest version of iperf3 from source on your Saltbox server, allowing you to perform network throughput testing.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://software.es.net/iperf/invoking.html#iperf3-manual-page){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](https://software.es.net/iperf/news.html){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](https://github.com/esnet/iperf/discussions){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install iperf3
```

## Usage

iperf3 is built from source and installed to `/usr/local/bin/iperf3`. Run it manually from the command line in server mode (`iperf3 -s`) or client mode (`iperf3 -c <server_ip>`) as needed for network testing.

- [:octicons-link-16: Documentation: iperf3 Documentation](https://iperf.fr/iperf-doc.php){: .header-icons }
