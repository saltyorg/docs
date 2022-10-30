# Omegabrr

## What is it?

[Omegabrr](https://github.com/autobrr/omegabrr){: target=_blank rel="noopener noreferrer" } syncs monitored titles from Radarr and Sonarr to assigned filters in [autobrr](https://docs.saltbox.dev/sandbox/apps/autobrr/){: target=_blank rel="noopener noreferrer" }.

| Details     |
|-------------|
| [:octicons-mark-github-16: Github](https://github.com/autobrr/omegabrr){: .header-icons target=_blank rel="noopener noreferrer" } |

Suitable install type: Feederbox

### 1. Installation

``` shell
sb install sandbox-omegabrr
```

### 2. Setup

The configuration file `/opt/omegabrr/config.yaml` will be pre-filled with your new API token and your Radarr and Sonarr details, but missing an autobrr API key which you must provide.

Add your filter IDs (inside the brackets–comma separated) to their corresponding *arr instance:
```yaml
      filters: [9,10,99,100]
```
Restart the Docker container for the changes to take effect.

### 3. URL

By default, the built-in HTTP server is not exposed to the web and can be queried locally via `http://omegabrr:7441`. If you wish to enable external access, add the following to your Saltbox inventory and redeploy the role:

```yaml
omegabrr_web_enabled: true
```
It will then be available at `https://omegabrr.domain.tld`.

### 4. Usage

Use the URL with the API token to trigger filter refreshes via webhook: [Service](https://github.com/autobrr/omegabrr#service){: .header-icons target=_blank rel="noopener noreferrer" }