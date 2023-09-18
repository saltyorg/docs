# Omegabrr

## What is it?

[Omegabrr](https://github.com/autobrr/omegabrr) is a companion app to [autobrr](../../apps/autobrr.md). It syncs monitored titles from Radarr and Sonarr to assigned filters in autobrr.

| Details     |
|-------------|
| [:octicons-mark-github-16: Github](https://github.com/autobrr/omegabrr){: .header-icons } |

Recommended install types: Feederbox, Saltbox, Core

### 1. Installation

```shell
sb install sandbox-omegabrr
```

### 2. URL (API)

Local applications may query the Omegabrr server via `http://omegabrr:7441/api/webhook/trigger`. For external use, `https://omegabrr._yourdomain.com_/api/webhook/trigger` is available.

### 3. Setup

The configuration file `/opt/omegabrr/config.yaml` will be pre-filled with your new API token and your Radarr and Sonarr details, but missing an autobrr API key which you must provide.

Add your filter IDs (inside the brackets—comma + whitespace separated) to their corresponding Radarr or Sonarr instance:

```yaml
      filters: [9, 10, 99, 100]
```

Restart the Docker container for the changes to take effect.

### 4. Usage

If desired, use the URL with the provided API token to trigger filter refreshes via webhook: [Service](https://github.com/autobrr/omegabrr#service){: .header-icons }
