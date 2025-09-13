---
hide:
  - tags
tags:
  - solr
  - search
  - apache
---

# Solr

## What is it?

[Apache Solr](https://solr.apache.org/) is a blazing-fast, open source, multi-modal search platform built on Apache Lucene. It's highly reliable, scalable and fault-tolerant enterprise search platform that powers search for many large internet sites.

!!! info
    This role is typically deployed as a backend service for other applications and may not have web access configured by default.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://solr.apache.org/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/apache/solr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/solr){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-solr
```

### 2. Setup

Solr is automatically configured with a default core. This service is typically used as a backend for other applications requiring search functionality.