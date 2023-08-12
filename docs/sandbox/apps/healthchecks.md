# Healthchecks

## What is it?

[Healthchecks](https://healthchecks.io/){: target=_blank rel="noopener noreferrer" } is a watchdog for your cron jobs. It's a web server that listens for pings from your cron jobs, plus a web interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://healthchecks.io/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://healthchecks.io/docs/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/healthchecks/healthchecks){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/healthchecks){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-healthchecks

```

### 2. URL

- To access Healthchecks, visit `https://healthchecks._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#configuration) file located in `/srv/git/saltbox/accounts.yml`

- [:octicons-link-16: Documentation](https://healthchecks.io/docs/){: .header-icons target=_blank rel="noopener noreferrer" }
