---
hide:
  - tags
tags:
  - dozzle
---

# Dozzle

## What is it?

[Dozzle](https://dozzle.dev/) is a small lightweight application with a web based interface to monitor Docker logs. It doesn’t store any log files. It is for live monitoring of your container logs only. Dozzle can only access logs written to stdout or stderr which is the same functionality as the `docker logs` command. See below for more info on that.

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

To view log files that are NOT written to stdout or stderr, use the following to setup a basic Alpine Linux container via Docker Compose that just tails a mounted log file (in this case, Cloudplow) which then exposes it to Dozzle. Adjust as needed for your circumstances.

``` yaml
  tail-cloudplow: # (1)!
    container_name: tail-cloudplow # (2)!
    image: alpine
    volumes:
      - /opt/cloudplow/cloudplow.log:/opt/cloudplow/cloudplow.log:ro # (3)!
    command:
      - tail
      - -F
      - /opt/cloudplow/cloudplow.log # (4)!
    network_mode: none
    restart: unless-stopped
    user: 1000:1000 # (5)!
```

1. You can pick any name for the container, but it is recommended to pick a memorable name that you will recognize in the Dozzle menu.
2. You can pick any name for the container, but it is recommended to pick a memorable name that you will recognize in the Dozzle menu.
3. The volume mount for the log file. This takes the format of `/host/path/to.log:/container/path/to.log:ro`. The `:ro` suffix is optional but recommended to give this container only read-only access to the log file.
4. The path inside of the container where the log file is accessible. This must be the same in the `volumes` section above and this `command` section. Matching the annotation example, this would be `/container/path/to.log`.
5. Provide your `uid:gid` if they are different. You can check these values by running the `id` command.

???+ note
    To get the container running, follow our docs on starting a docker container here; [Your Own Containers](../advanced/your-own-containers.md#creating-and-running-the-container).

### 4. Adding Additional Hosts

You can add additional hosts to Dozzle using the `dozzle_additional_hosts` inventory variable. This will append the additional host(s) to the default entry. You can review the upstream documentation [here](https://dozzle.dev/guide/remote-hosts) for the proper syntax. The initiai `,` will be added after the default entry, you must comma separate the hosts if you are adding multiple entries such as:

```yaml
dozzle_additional_hosts: "tcp://otherserver:2375|otherserver,tcp://thirdserver:2375|thirdserver"
```

- [:octicons-link-16: Documentation](https://dozzle.dev/guide/what-is-dozzle){: .header-icons }
