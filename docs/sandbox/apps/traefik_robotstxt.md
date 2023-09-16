# Robotstxt

## What is it?

[Robotstxt](https://github.com/mstroecker/zig-robotstxt) is a lightweight http-server, just serving a disallow-robots.txt file using the Zig programming language([https://ziglang.org/](https://ziglang.org/)).

__Robots.txt__ basically works like a “No Trespassing” sign. It actually, tells robots whether we want them to crawl the website or not. With this role, we are disallowing all robots to crawl and avoid indexing in search engines.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/mstroecker/zig-robotstxt){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/mstroecker/zig-robotstxt){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/mstroecker/zig-robotstxt){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/mstroecker/zig-robotstxt){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell
sb install sandbox-traefik_robotstxt
```

### 2. Result

```text
HTTP/1.1 200 OK
Content-Length: 26

User-agent: *
Disallow: /
```

When you want to reach `*.yourdomain.tld/robots.txt`
