---
hide:
  - tags
tags:
  - node-exporter
  - prometheus
  - monitoring
  - metrics
---

# Node Exporter

## Overview

Node Exporter is a Prometheus exporter for hardware and OS metrics. It exposes system-level metrics such as CPU usage, memory, disk I/O, network statistics, and more, which can be scraped by Prometheus for monitoring and alerting.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://prometheus.io/){: .header-icons } | [:octicons-link-16: Docs](https://prometheus.io/docs/guides/node-exporter/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/prometheus/node_exporter){: .header-icons } | [:material-docker: Docker](https://github.com/prometheus/node_exporter){: .header-icons }|

### 1. Installation

``` shell

sb install node_exporter

```

### 2. Setup

Node Exporter is installed directly on the host at `/opt/node_exporter/node_exporter` and runs as a systemd service. It exposes system metrics on port 9100 for Prometheus to scrape. Manage with `systemctl status/restart node_exporter`.

Note: Metrics are not password-protected by default. Consider firewall rules if exposing port 9100 externally.

- [:octicons-link-16: Documentation: Node Exporter Guide](https://prometheus.io/docs/guides/node-exporter/){: .header-icons }
