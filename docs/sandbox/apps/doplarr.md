# Doplarr

## What is it?

[Doplarr](https://kiranshila.github.io/Doplarr/#/) is a chatbot used to simplify using services like Sonarr/Radarr/Overseer via the use of chat. Current platform is Discord only.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://kiranshila.github.io/Doplarr/#/){: .header-icons } | [:octicons-link-16: Docs](https://kiranshila.github.io/Doplarr/#/configuration){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/kiranshila/doplarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/doplarr){: .header-icons }|

## Setup Doplarr

### 1. Create Discord bot

1. Create a new [Application](https://discord.com/developers/applications) in Discord
2. Go to the Bot tab and add a new bot
3. Copy the token and paste it in `/opt/sandbox/settings.yml` in the `doplarr.discord_token` field:

    ```yaml hl_lines="3" title="/opt/sandbox/settings.yml"
    ...
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ...
    ```

4. Go to OAuth2 and under "OAuth2 URL Generator", enable `applications.commands` and `bot`
5. Copy the resulting URL and open it in your browser in order to invite your bot to your discord channel.

### 2. Set up overseer parameters

1. In `/opt/sandbox/settings.yml` : set up the overseer url in the corresponding field `doplarr.overseerr_url` according to your setings. If you have not customize saltbox settings, the default url `http://overseerr:5055` should be correct:

    ```yaml hl_lines="4" title="/opt/sandbox/settings.yml"
    ...
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ...
    ```

2. In `/opt/sandbox/settings.yml` : set up the overseer API key in the corresponding field `doplarr.overseerr_api` according to your overseer settings.
You can get your api keys in your main setting page in overseer: `https://overseerr._yourdomain.com_/settings`:

    ```yaml hl_lines="5" title="/opt/sandbox/settings.yml"
    ...
    doplarr:
      discord_token: your_discord_bot_token
      overseerr_url: "http://overseerr:5055"
      overseerr_api:
    ...
    ```

### 3. Installation

``` shell

sb install sandbox-doplarr

```

!!! Note
      📢 You may also override the default setting of Doplarr working with overseer, to work with Sonarr and Radarr.
      The recommended way to customize these parameters is to use the [inventory](../../saltbox/inventory/index.md). You should edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section.

<div markdown>
``` yaml title="Inventory"
doplarr_docker_envs_defaults:
  SONARR__URL: # (1)!
  RADARR__URL: # (2)!
  SONARR__API: # (3)!
  RADARR__API: # (4)!
  DISCORD__TOKEN: # (5)!
```

1. This line will set the Sonarr URL. Saltbox defaults to `"http://sonarr:8989"`.
2. This line will set the Radarr URL. Saltbox defaults to `"http://radarr:7878"`.
3. This line will set the Sonarr API key. Place your API key here. Wrap it in quotes.
4. This line will set the Radarr API key. Place your API key here. Wrap it in quotes.
5. This line will set the Discord token. Place your token here. Wrap it in quotes.
</div>

- [:octicons-link-16: Documentation: Doplarr Docs](https://kiranshila.github.io/Doplarr/#/configuration){: .header-icons }
