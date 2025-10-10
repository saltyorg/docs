---
hide:
  - tags
tags:
  - scrutiny
  - smart
  - disk-monitoring
  - hardware-monitoring
---

# Scrutiny

## What is it?

Scrutiny is a hard drive health monitoring tool that tracks S.M.A.R.T. metrics for your drives. It provides a WebUI with historical data tracking, alerting, and beautiful visualizations to help you monitor drive health and predict failures before they happen.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/AnalogJ/scrutiny){: .header-icons } | [:octicons-link-16: Docs](https://github.com/AnalogJ/scrutiny/blob/master/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/AnalogJ/scrutiny){: .header-icons } | [:material-docker: Docker](https://github.com/AnalogJ/scrutiny/pkgs/container/scrutiny){: .header-icons }|

### 1. Installation

``` shell

sb install scrutiny

```

### 2. URL

- To access Scrutiny, visit `https://scrutiny._yourdomain.com_`

### 3. Setup

Scrutiny monitors hard drive health using S.M.A.R.T. metrics. The omnibus container includes WebUI, Collector, and InfluxDB. It automatically detects drives, collects metrics, and displays health status with historical tracking. Data persists in `/opt/scrutiny/`.

The container runs in privileged mode to access hardware S.M.A.R.T. data. Configuration is largely zero-config with settings available through the web interface.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
