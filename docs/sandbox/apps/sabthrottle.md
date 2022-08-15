# SABThrottle 

## What is it?

[SABThrottle](https://github.com/8a8al00ey/sabthrottle){: target=_blank rel="noopener noreferrer" } Sabthrottle was designed in order to dynamically control the bandwidth allocation when users are actively streaming from Plex to avoid unnecessary buffering while still allowing the user to download at the fastest rate possible. Remember nzbthrottle from daghaian, yes its exactly like that but for SABnzbd with some additional tweaks.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://github.com/8a8al00ey/sabthrottle){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/8a8al00ey/sabthrottle#installation){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/8a8al00ey/sabthrottle){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/8a8al00ey/sabthrottle){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-sabthrottle

```

### 2. Setup

- See [documentation](https://github.com/8a8al00ey/sabthrottle#installation){: target=_blank rel="noopener noreferrer" } for configuration and instructions see the sample configuration and description below it.

    - Running the role will autopopulate plex token and plex url.
    - If you require more then 5 stream count just follow the example and add more using proper yml formatting.
    - You can always check logs via 
        ``` shell
        docker logs -f sabthrottle
        ```

- [:octicons-link-16: Documentation](https://github.com/8a8al00ey/sabthrottle#installation){: .header-icons target=_blank rel="noopener noreferrer" }
