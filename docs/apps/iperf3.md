---
icon: material/desktop-classic
hide:
  - tags
tags:
  - iperf3
  - network
  - performance
  - bandwidth
---

# iperf3

## Overview

iperf3 is a network performance measurement tool that can test TCP, UDP, and SCTP bandwidth. This role builds and installs the latest version of iperf3 from source on your Saltbox server, allowing you to perform network throughput testing.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://software.es.net/iperf/){: .header-icons } | [:octicons-link-16: Docs](https://iperf.fr/iperf-doc.php){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/esnet/iperf){: .header-icons } | [:material-docker: Docker](https://github.com/esnet/iperf){: .header-icons }|

### 1. Installation

``` shell

sb install iperf3

```

### 2. Setup

iperf3 is built from source and installed to `/usr/local/bin/iperf3`. Run it manually from the command line in server mode (`iperf3 -s`) or client mode (`iperf3 -c <server_ip>`) as needed for network testing.

- [:octicons-link-16: Documentation: iperf3 Documentation](https://iperf.fr/iperf-doc.php){: .header-icons }
