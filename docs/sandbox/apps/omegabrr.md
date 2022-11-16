# Omegabrr

## What is it?

[Omegabrr](https://github.com/autobrr/omegabrr){: target=_blank rel="noopener noreferrer" } is a companion app to [autobrr](https://docs.saltbox.dev/sandbox/apps/autobrr/). It syncs monitored titles from Radarr and Sonarr to assigned filters in autobrr.

| Details     |
|-------------|
| [:octicons-mark-github-16: Github](https://github.com/autobrr/omegabrr){: .header-icons target=_blank rel="noopener noreferrer" } |

Recommended install types: Feederbox, Saltbox, Core

### 1. Installation

```shell
sb install sandbox-omegabrr
```

### 2. URL (API)

Local applications may reach the Omegabrr server via `http://omegabrr:7441`. For external use, `https://omegabrr._yourdomain.com_` is available.

### 3. Setup

The configuration file `/opt/omegabrr/config.yaml` will be pre-filled with your new API token and your Radarr and Sonarr details, but missing an autobrr API key which you must provide.

Add your filter IDs (inside the brackets–comma separated) to their corresponding *arr instance:
```yaml
      filters: [9,10,99,100]
```
Restart the Docker container for the changes to take effect.

### 4. Usage

Use the URL with the provided API token to trigger filter refreshes via webhook: [Service](https://github.com/autobrr/omegabrr#service){: .header-icons target=_blank rel="noopener noreferrer" }
