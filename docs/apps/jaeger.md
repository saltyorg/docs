---
hide:
  - tags
tags:
  - jaeger
  - tracing
  - monitoring
  - observability
---

# Jaeger

## What is it?

Jaeger is an open-source, end-to-end distributed tracing system. It's used for monitoring and troubleshooting microservices-based distributed systems, including distributed context propagation, distributed transaction monitoring, root cause analysis, service dependency analysis, and performance/latency optimization.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.jaegertracing.io/){: .header-icons } | [:octicons-link-16: Docs](https://www.jaegertracing.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jaegertracing/jaeger){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jaegertracing/all-in-one){: .header-icons }|

### 1. Installation

``` shell

sb install jaeger

```

### 2. URL

- To access Jaeger, visit `https://jaeger._yourdomain.com_`

### 3. Setup

Jaeger provides distributed tracing for monitoring microservices. The all-in-one container includes UI, Collector, Query, and Agent components. Configure your applications to send traces to `http://jaeger:14268/api/traces` or use the Zipkin-compatible endpoint at `http://jaeger:9411`.

Note: Data is stored in-memory by default and will be lost when the container restarts.

- [:octicons-link-16: Documentation: Jaeger Documentation](https://www.jaegertracing.io/docs/){: .header-icons }
