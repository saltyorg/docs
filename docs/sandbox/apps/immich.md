# Immich

## What is it?

[Immich](https://immich.app/) is a self-hosted photo and video backup tool, similar to google photos and apple photos.

### Features

- Bulk Upload (Using the CLI)
- Facial Recognition
- Hardware Transcoding (Experimental)
- Oauth and/or password login
- Libraries
- Mobile App
- Partner Sharing
- Reverse Geocoding
- Smart Search
- XMP Sidecars

!!!info
    By default, Immich is NOT protected behind your Authelia/SSO middleware. You have to create a user with an email and password for Immich upon start up. Its recommended that you use the email and password you set up upon instalation for consistencies sake.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://immich.app/){: .header-icons } | [:octicons-link-16: Docs](https://immich.app/docs/overview/introduction){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/immich-app/immich){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-immich

```

### 2. URL

- To access Immich, visit `https://immich._yourdomain.com_`

### 3. Setup

!!!info
    📢 Again, no default user is configured until you run through the setup screen, so you would ideally run through setup as soon as immich is deployed to secure the site. It is not behind authelia by default.

???tip
    In Administration > Settings is a button to copy the current admin configuration to your clipboard. So you can just grab it from there, and paste it into a file.

If you would like to have the config file available, create a new config file (e.g. immich.config, and the config format is `.json`) and map it in inventory; just keep in mind that this disallows you from configuring Immich admin settings from the web ui.

``` yaml

immich_docker_envs_custom:
  IMMICH_CONFIG_FILE: "/config/immich.config"

```

- [:octicons-link-16: Documentation: Immich Docs](https://immich.app/docs/overview/introduction){: .header-icons }
