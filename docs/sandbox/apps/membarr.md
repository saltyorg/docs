# Membarr

## What is it?

[Membarr](https://github.com/Yoruio/Membarr) is a fork of Invitarr that invites discord users to Plex and Jellyfin. You can also automate this bot to invite discord users to a media server once a certain role is given to a user or the user can also be added manually.

***Features*** are:

- Ability to invite users to Plex and Jellyfin from discord
- Fully automatic invites using roles
- Ability to kick users from plex if they leave the discord server or if their role is taken away.
- Ability to view the database in discord and to edit it.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Yoruio/Membarr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Yoruio/Membarr){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Yoruio/Membarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/yoruio/membarr){: .header-icons }|

## Setup Membarr

### 1. Create Discord bot

1. Create the Discord server that your users will get member roles or use an existing discord that you can assign roles from.
2. Log into the [Discord Developer Portal] and click 'New Application'
3. Add a short description and an icon for the bot. Save changes. *(Optional)*
4. Go to **Bot** section in the side menu.
5. Uncheck 'Public Bot' under **Authorization Flow**
6. Check all 3 boxes under Privileged Gateway Intents: **Presence Intent**, **Server Members Intent**, and **Message Content Intent**. Save changes.
7. Copy the token under the username or reset it to copy. This is the token used in the docker image.
8. Go to **OAuth2** section in the side menu, then click **URL Generator**.
9. Under **Scopes**, check **bot** and **applications.commands**.
10. Copy the **Generated URL** and paste into your browser and add it to your discord server from Step 1.
11. The bot will come online after the docker container is running with the correct Bot Token.

  [Discord Developer Portal]: https://discord.com/developers/applications

### 2. Installation

``` shell

sb install sandbox-membarr

```

### 3. Set up Plex parameters

When you install the role, it will create 2 files, an `app.db` file and `config.ini`. You will need to edit the `config.ini` file with your preferred editing program. (ie `nano` or `vim` etc) Add your Plex credentials like so:

``` toml
[bot_envs]
plex_user =
plex_pass =
plex_server_name = ServerFriendlyName
plex_roles =
plex_token = token
plex_base_url = https://plex.domain.tld
plex_enabled = True
```

Now restart the Membarr container `docker restart membarr`.

???+ Success "Plex Token"
    To get the Plex token, you will run the following command: `sb install plex-auth-token`
    Look for the **Display Plex Auth Token** task in the log.
