---
hide:
  - tags
tags:
  - crowdsec
---

# Using the CrowdSec Role in Saltbox

This guide explains how to use and configure the CrowdSec role in Saltbox using the available inventory options.

## Overview

CrowdSec is a modern security solution that helps protect your systems from various threats. The Saltbox CrowdSec role allows you to easily deploy and configure CrowdSec on your Saltbox server.

## Configuration Options

### Toggle

To enable the CrowdSec role, use the following option in your inventory file:

```yaml
crowdsec_enabled: false
```

Set this to `true` to enable CrowdSec.

### Configuration Options

#### Console Enrollment Key (Required)

The CrowdSec Console enrollment key is required for the role to function properly. You must specify your enrollment key:

```yaml
crowdsec_console_enrollment_key: "your-enrollment-key-here"
```

To obtain an enrollment key:

1. Sign up for a free account at [https://app.crowdsec.net](https://app.crowdsec.net).
2. Once logged in, navigate to the "Security Engines" section.
3. Click on "Add Security Engine".
4. Copy the provided enrollment key, not the full command, from the "Enroll your CrowdSec Security Engine" box.

Make sure to replace "your-enrollment-key-here" with the actual key you obtained from the CrowdSec Console.

#### Collections

You can specify which CrowdSec collections to install or remove:

```yaml
crowdsec_collections_install_custom:
  - "crowdsecurity/somecollection"

crowdsec_collections_remove_custom:
  - "crowdsecurity/somecollection"
```

Add or remove collections from these lists as needed.

##### Authentik Collection

1. Add to `sb inventory`
```yaml
crowdsec_collections_install_custom:
  - "firix/authentik"
```
2. Create a new file in `/etc/crowdsec/acquis.d` called `authentik.yaml`
3. Add the below to `authentik.yaml`
```yaml
---
source: docker
container_name:
 - authentik
labels:
  type: authentik
```
4. Run `sb install crowdsec` to apply the collection

#### Scenarios, Parsers, and Postoverflows

Similarly, you can specify scenarios, parsers, and postoverflows to install or remove:

```yaml
crowdsec_scenarios_install_custom: []
crowdsec_scenarios_remove_custom: []
crowdsec_parsers_install_custom: []
crowdsec_parsers_remove_custom: []
crowdsec_postoverflows_install_custom: []
crowdsec_postoverflows_remove_custom: []
```

Add items to these lists as needed.

#### Prometheus Integration

CrowdSec can be integrated with Prometheus for monitoring. Configure it using these options:

```yaml
crowdsec_prometheus_enabled: false
crowdsec_prometheus_level: "full"
crowdsec_prometheus_listen_addr: "127.0.0.1"
crowdsec_prometheus_listen_port: "6060"
```

Set `crowdsec_prometheus_enabled` to `true` to enable Prometheus integration. Adjust the level, listen address, and port as needed.

Additionally to change configuration options or add new ones you should follow the upstream [documentation](https://docs.crowdsec.net/docs/next/configuration/crowdsec_configuration/#overriding-values).

Saltbox fully manages the default configuration files:

  - /etc/crowdsec/config.yaml
  - /etc/crowdsec/acquis.yaml

So any changes to these will be lost next time the role runs.

## Usage

1. Edit your Saltbox [inventory](../saltbox/inventory/index.md) file.
2. Configure the CrowdSec options as described above, ensuring you've added your CrowdSec Console enrollment key.
3. Run the Saltbox install command to apply the changes.
4. Navigate back to your CrowdSec console where you found your enrollment key and accept the the new security engine. 

Example:

```bash
sb install crowdsec
```

This will install CrowdSec with your specified configuration.

To have Traefik use the bouncer on any given application you will need to reinstall Traefik and all other applications in order to apply the new middleware to each container.

Remember to review the [official CrowdSec documentation](https://docs.crowdsec.net/) for more detailed information on collections, scenarios, and other configuration options.
