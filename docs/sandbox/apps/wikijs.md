# Wikijs

## What is it?

[Wikijs](https://js.wiki/) is a modern, lightweight and powerful wiki app built on NodeJS.

- Manage all aspects of your wiki using the extensive and intuitive admin area.
- Fully customize the appearance of your wiki, including a light and dark mode.
- Make your wiki public, completely private or a mix of both.

!!!info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into Wikijs with the email and password you set up upon instalation.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://js.wiki/){: .header-icons } | [:octicons-link-16: Docs](https://docs.requarks.io/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/requarks/wiki){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/requarks/wiki){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-wikijs

```

### 2. URL

- To access wikijs, visit `https://wikijs._yourdomain.com_`

### 3. Setup

!!!info
    📢 No default user is configured until you run through the setup screen, so you should ideally run through setup as soon as the container is deployed to secure the site. It is not behind authelia by default.

- [:octicons-link-16: Documentation: Wikijs Docs](https://docs.requarks.io/){: .header-icons }
