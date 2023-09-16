# Doplarr

## What is it?

[Doplarr](https://github.com/kiranshila/doplarr) is a chatbot used to simplify using services like Sonarr/Radarr/Overseer via the use of chat. Current platform is Discord only.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/kiranshila/doplarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/kiranshila/doplarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/kiranshila/doplarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://ghcr.io/kiranshila/doplarr){: .header-icons target=_blank rel="noopener noreferrer" }|

## Setup Doplarr

### 1. Create Discord bot

1. Create a new [Application](https://discord.com/developers/applications) in Discord
2. Go to the Bot tab and add a new bot
3. Copy out the token and paste it in `/opt/sandbox/settings.yaml` in the `doplarr.discord_token` field.
4. Go to OAuth2 and under "OAuth2 URL Generator", enable `applications.commands` and `bot`
5. Copy the resulting URL and open it in your browser in order to invite your bot to your discord channel.

### 2. Set up overseer parameters

1. In `/opt/sandbox/settings.yaml` : set up the overseer url in the corresponding field `doplarr.overseerr_url` according to your setings. If you have not customize saltbox settings, the default url `http://overseerr:5055` should be correct.
2. In `/opt/sandbox/settings.yaml` : set up the overseer API key in the corresponding field `doplarr.overseerr_api` according to your overseer settings.
You can get your api keys in your main setting page in overseer: `https://overseerr._yourdomain.com_/settings`

### 3. Installation

``` shell

sb install sandbox-doplarr

```

!!! Note
      📢 You may also override the default setting of Doplarr working with overseer, to work with Sonarr and Radarr. Additional informations here [:octicons-link-16: Documentation](https://github.com/kiranshila/Doplarr/blob/main/README.md#sonarrradarr) .
      The recommended way to customize these parameters is to use the [inventory](https://docs.saltbox.dev/saltbox/inventory/) :
      You should edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section:

  ```yaml
      ### Custom settings for Doplarr ###
      doplarr_docker_envs_defaults:
        SONARR__URL: "http://sonarr:8989"
        RADARR__URL: "http://radarr:7878"
        SONARR__API: sonarr_api
        RADARR__API: radarr_api
        DISCORD__TOKEN: your_discord_bot_token
      ```
