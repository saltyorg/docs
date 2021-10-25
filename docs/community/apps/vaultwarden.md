# vaultwarden

## What is it?

[vaultwarden](https://github.com/dani-garcia/vaultwarden){: target=_blank rel="noopener noreferrer" } is an alternative implementation of the Bitwarden server API written in Rust and compatible with upstream Bitwarden clients*, perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

!!! Note
      📢 This project was known as Bitwarden_RS and has been renamed to separate itself from the official Bitwarden server in the hopes of avoiding confusion and trademark/branding issues.

## Project Information

- [:material-home: vaultwarden ](https://github.com/dani-garcia/vaultwarden){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://github.com/dani-garcia/vaultwarden/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/dani-garcia/vaultwarden){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/vaultwarden/server){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-vaultwarden

```

### 2. URL

- To access vaultwarden, visit `https://vaultwarden._yourdomain.com_`

### 3. Setup

  1. Visit the vaultwarden site at `https://vaultwarden._yourdomain.com_`

  2. Sign up with any email address and password.

  3. To access the Admin Panel go to `https://vaultwarden._yourdomain.com_admin`

  4. You will need to enter an authentication key which you can find in `/opt/vaultwarden/env`. Look for `ADMIN_TOKEN=`.

- [:octicons-link-16: Documentation](https://github.com/dani-garcia/vaultwarden/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
