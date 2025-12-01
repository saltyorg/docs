---
icon: material/server-network-outline
hide:
  - tags
tags:
  - node-exporter
  - prometheus
  - monitoring
  - metrics
saltbox_automation:
  sections:
    inventory: false
---

# Node Exporter

## Overview

Node Exporter is a Prometheus exporter for hardware and OS metrics. It exposes system-level metrics such as CPU usage, memory, disk I/O, network statistics, and more, which can be scraped by Prometheus for monitoring and alerting.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://prometheus.io/docs/guides/node-exporter){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/prometheus/node_exporter/releases){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](https://prometheus.io/community){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install node-exporter
```

## Usage

Node Exporter is installed directly on the host at `/opt/node_exporter/node_exporter` and runs as a systemd service. It exposes system metrics on port 9100 for Prometheus to scrape. Manage with `systemctl status/restart node_exporter`.

Note: Metrics are not password-protected by default. Consider firewall rules if exposing port 9100 externally.

- [:octicons-link-16: Documentation: Node Exporter Guide](https://prometheus.io/docs/guides/node-exporter){: .header-icons }
