---
hide:
  - tags
tags:
  - nginx
  - web-server
  - reverse-proxy
---

# Nginx

## What is it?

Nginx is a high-performance web server, reverse proxy, and load balancer. This role deploys Nginx using the LinuxServer.io container, providing a simple way to host static websites or act as a reverse proxy for your applications.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://nginx.org/){: .header-icons } | [:octicons-link-16: Docs](https://nginx.org/en/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nginx/nginx){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/nginx){: .header-icons }|

### 1. Installation

``` shell

sb install nginx

```

### 2. URL

- To access Nginx, visit `https://nginx._yourdomain.com_`

### 3. Setup

Nginx is deployed using the LinuxServer.io container with configuration files at `/opt/nginx/`. Place website files in `/opt/nginx/www/` and edit site configs in `/opt/nginx/nginx/site-confs/`. Multiple instances are supported via the `nginx_instances` variable in your [Saltbox inventory](../../saltbox/inventory/index.md). Restart with `docker restart nginx` to apply changes.

- [:octicons-link-16: Documentation: Nginx Documentation](https://nginx.org/en/docs/){: .header-icons }
