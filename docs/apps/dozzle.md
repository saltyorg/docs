# Dozzle

## What is it?

[Dozzle](https://dozzle.dev/) is a small lightweight application with a web based interface to monitor Docker logs. It doesn’t store any log files. It is for live monitoring of your container logs only. Dozzle can only access logs written to sysout or syserr which is the same functionality as the `docker logs` command. See below for more info on that.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://dozzle.dev/){: .header-icons } | [:octicons-link-16: Docs](https://dozzle.dev/guide/what-is-dozzle){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/amir20/dozzle){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/amir20/dozzle){: .header-icons }|

### 1. Installation

``` shell

sb install dozzle

```

### 2. URL

- To access Dozzle, visit `https://dozzle._yourdomain.com_`

### 3. Setup

To view log files that are NOT written to sysout or syserr, use the following to setup a basic alpine container via compose that just tails a mounted log file (in this case, Cloudplow) which then exposes it to dozzle. Adjust as needed for your circumstances.

``` yaml
---
  tail-cloudplow:
    container_name: tail-cloudplow
    image: alpine
    volumes:
      - /opt/cloudplow/cloudplow.log:/opt/cloudplow/cloudplow.log:ro
    command:
      - tail
      - -F
      - /opt/cloudplow/cloudplow.log     
    network_mode: none
    restart: unless-stopped
    user: 1000:1001
```

- [:octicons-link-16: Documentation](https://dozzle.dev/guide/what-is-dozzle){: .header-icons }
