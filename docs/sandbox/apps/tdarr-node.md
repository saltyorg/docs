---
hide:
  - tags
tags:
  - tdarr-node
  - media
  - encoding
---

# Tdarr Node

## What is it?

[Tdarr Node](https://tdarr.io/) is a cross-platform conditional based transcoding application for automating media library transcode/remux management in order to process your media files as required.

- Node is described as: Processes running same/other devices which collect tasks from the Server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://tdarr.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.tdarr.io/docs/installation/getting-started){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/HaveAGitGat/Tdarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/haveagitgat/tdarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-tdarr-node

```

### 2. Usage

The Tdarr Node is configured with the following defaults which can be modified via the inventory system.

``` yaml
tdarr_node_server_ip: "tdarr"
tdarr_node_server_port: "8266"
tdarr_node_node_id: "MainNode"
tdarr_node_node_port: "8267"
tdarr_node_external: false
```

By switching `tdarr_node_external` to `true` the node will be accessible externally via the specified `tdarr_node_node_port` on any hostname or IP address pointing directly to the server.

To connect the Tdarr node to a Tdarr server, set `tdarr_node_server_ip` and `tdarr_node_server_port` to the IP/hostname and port of the exposed Tdarr server.

### 3. Setup

- [:octicons-link-16: Documentation: Tdarr Node Docs](https://docs.tdarr.io/docs/installation/getting-started){: .header-icons }
