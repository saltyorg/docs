# Resilio Sync

## What is it?

[Resilio Sync](https://www.resilio.com/) uses peer-to-peer technology to provide fast, private file sharing for teams and individuals. By skipping the cloud, transfers can be significantly faster because files take the shortest path between devices. Sync does not store your information on servers in the cloud, avoiding cloud privacy concerns.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.resilio.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://help.resilio.com/hc/en-us/categories/200140177-Get-started-with-Sync){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/resilio/sync){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-resiliosync

```

### 2. URL

- To access Resilio Sync, visit `https://resiliosync._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation: Resilio Sync Docs](https://help.resilio.com/hc/en-us/articles/204754939-Comprehensive-guide-to-syncing-Desktop-Desktop-){: .header-icons target=_blank rel="noopener noreferrer" }

- Note: The default data port for this container is 55555. Sync will try to use this port for data transfer, if the port is not open Sync will automatically use a [relay server](https://help.resilio.com/hc/en-us/articles/204754779-What-is-a-Relay-Server-) to make your connection. For best performance, please ensure this port is opened in your firewall.
- Sync's data port can be customized by changing the [Sync settings](https://help.resilio.com/hc/en-us/articles/204762669-Sync-Preferences) as well as adding the following to `/srv/git/saltbox/inventories/host_vars/localhost.yml` and rerunning the installation tag:

 ``` yaml
resiliosync_data_port: "#####"
```
