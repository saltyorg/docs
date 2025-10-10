---
hide:
  - tags
tags:
  - mongodb
  - database
  - nosql
---

# MongoDB

## What is it?

MongoDB is a popular NoSQL document database that stores data in flexible, JSON-like documents. It's designed for scalability and developer productivity, and is used by many applications for data persistence.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.mongodb.com/){: .header-icons } | [:octicons-link-16: Docs](https://www.mongodb.com/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/mongodb/mongo){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/mongo){: .header-icons }|

### 1. Installation

``` shell

sb install mongodb

```

### 2. Setup

MongoDB 6 is deployed in a Docker container with data persisting to `/opt/mongo/`. Connect from other containers using `mongodb://mongo:27017/`. Multiple instances are supported via the `mongodb_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md).

Note: No authentication is configured by default.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
