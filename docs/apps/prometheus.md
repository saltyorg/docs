---
hide:
  - tags
tags:
  - prometheus
  - monitoring
  - metrics
  - observability
---

# Prometheus

## What is it?

Prometheus is an open-source systems monitoring and alerting toolkit. It collects and stores metrics as time series data, providing a powerful query language (PromQL) for analyzing system behavior and setting up alerts.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://prometheus.io/){: .header-icons } | [:octicons-link-16: Docs](https://prometheus.io/docs/introduction/overview/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/prometheus/prometheus){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/prom/prometheus){: .header-icons }|

### 1. Installation

``` shell

sb install prometheus

```

### 2. URL

- To access Prometheus, visit `https://prometheus._yourdomain.com_`

### 3. Setup

Prometheus provides monitoring and alerting with automatic installation of Node Exporter and cAdvisor for system and container metrics. Configuration is at `/opt/prometheus/prometheus.yml`. Data retention defaults to 15 days but can be configured in your [Saltbox inventory](../saltbox/inventory/index.md) using `prometheus_role_retention` and `prometheus_role_size`.

Add custom scrape targets to the config file and restart with `docker restart prometheus`. Works excellently with Grafana using data source `http://prometheus:9090`.

- [:octicons-link-16: Documentation: Prometheus Documentation](https://prometheus.io/docs/introduction/overview/){: .header-icons }
