# MediaButler API Server

# **NOT YET INTEGRATED - SOON**
## What is it?

[MediaButler](https://github.com/MediaButler/Server){: target=_blank rel="noopener noreferrer" } is aimed as your personal media companion, providing a unified experience for several applications that you may be using. Do you have a Plex Server in your network? Then MediaButler is precisely for you, featuring a full experience for you and your users. Security conscious so private information stays private. The API Server serves as the hub for everything. Open Sourced to allow you/others to implement features which can simplify and automate processes to help make life easier.

## Project Information

- [:material-home: MediaButler ](https://github.com/MediaButler/Server){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://github.com/MediaButler/Wiki/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/MediaButler/Server){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/mediabutler/server){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-mediabutler

```
### 3. Setup

1. Mediabutler settings file can be configured at `/opt/mediabutler/settings.json`

2. Invite bot to your server: <br />
   https://discord.com/api/oauth2/authorize?client_id=354733331717554179&permissions=8&scope=bot

3. Enter `!login`

4. Then `!server`  (select your server by reacting)

5. The list of permissions the bot requires are as follows: <br />
   ``` { .shell }
   Manage Roles, Manage Channels, Change Nickname, Manage Emojis, Read Messages, Send TTS Messages, Embed Links, Read Message History, Use External Emojis, Attach Files, Mention @everyone, Add Reactions, Voice View Channel, Voice Connect, Voice Speak, Use Voice Activity
   ```

6. For an overview of available discord commands see [the discord documentation](https://github.com/MediaButler/Server/blob/master/docs/DISCORD.md){: target=_blank rel="noopener noreferrer" }.

- [:octicons-link-16: Documentation](https://github.com/MediaButler/Wiki/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
