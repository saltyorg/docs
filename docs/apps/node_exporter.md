---
icon: material/server-network-outline
title: Node Exporter
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
  app_links:
    - name: Manual
      url: https://prometheus.io/docs/guides/node-exporter
      type: documentation
    - name: Releases
      url: https://github.com/prometheus/node_exporter/releases
      type: github
    - name: Community
      url: https://prometheus.io/community
      type: community
  project_description:
    name: Node Exporter
    summary: |-
      a specialized monitoring agent designed for Prometheus that collects and exposes detailed system-level metrics from host machines in Kubernetes environments.
    link: https://github.com/prometheus/node_exporter
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Node Exporter

## Overview

[Node Exporter](https://github.com/prometheus/node_exporter) is a specialized monitoring agent designed for Prometheus that collects and exposes detailed system-level metrics from host machines in Kubernetes environments.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://prometheus.io/docs/guides/node-exporter){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/prometheus/node_exporter/releases){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://prometheus.io/community){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install node-exporter
```

## Usage

Node Exporter is installed directly on the host at `/opt/node_exporter/node_exporter` and runs as a systemd service. It exposes system metrics on port 9100 for Prometheus to scrape. Manage with `systemctl status/restart node_exporter`.

Note: Metrics are not password-protected by default. Consider firewall rules if exposing port 9100 externally.
