---
icon: material/docker
hide:
  - tags
tags:
  - plex-patrol
  - plex
  - monitoring
---

# Plex Patrol

## Overview

[Plex Patrol](https://github.com/l3uddz/plex_patrol) is a tool which can monitor a plex server to kick transcodes (audio or video or both), kick paused streams if not resumed within X minutes, kick specific players, e.g. Plex Web, etc.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/l3uddz/plex_patrol){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/cloudb0x/plex_patrol/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-plex-patrol
```

## Configuration

Plex Patrol has no UI; it's driven by a config file.

The role will fill in the Plex URL and token; aside from that the various settings are described in comments, with the defaults as below.

The settings file is found at:

```shell
/opt/plex_patrol/settings.ini
```

After editing the file, restart the container with `docker restart plex_patrol`.

default contents:

```ini
[settings]
# Show debug messages.
DEBUG = false
# Plex server url (e.g. http://ip:32400 or https://plex.reverse-proxy.com)
SERVER_URL = http://plex:32400
# Plex token for server.
SERVER_TOKEN = YOUR_TOKEN_WILL_BE_HERE
# Name of server (does not matter, its used in the logs).
SERVER_NAME = Saltbox
# How often to check the active streams in seconds.
CHECK_INTERVAL = 90
# instantly kick 4K transcodes?
KICK_4K_TRANSCODE = true
# instantly kick video transcodes?
KICK_VIDEO_TRANSCODES = false
# Instantly kick audio transcodes?
KICK_AUDIO_TRANSCODES = false
# Instantly kick any players from this , separated list?
KICK_CLIENT_PLAYERS =
# Instantly kick streams from users with multiple IPs
KICK_MULTIPLE_IP = true
# How many streams from unique IPs before kicking extra user streams if above is true.
KICK_MULTIPLE_IP_MAX = 1
# Delay kick paused transcodes (direct streams count too)?
KICK_PAUSED_TRANSCODES = true
# Delay kick paused direct plays?
KICK_PAUSED_DIRECTPLAY = true
# When the options above are true, the user has this many minutes to resume, otherwise kick.
KICK_PAUSED_GRACE_MINS = 15
# Messages to be displayed for different kick types.
KICK_4K_TRANSCODE_MESSAGE = You are not allowed to transcode 4K content, fix your settings!
KICK_PAUSED_MESSAGE = You are not allowed to pause a stream for that long... cya!
KICK_TRANSCODE_MESSAGE = You are not allowed to transcode streams, use a better client!
KICK_PLAYER_MESSAGE = You are not allowed to use this trash player. Use the official software from www.plex.tv/downloads -> Get An App!!!
KICK_MULTI_IP_MESSAGE = You are not allowed to stream from more than 1 IP address!
# User list separated by a , who are immune from all checks.
WHITELISTED_USERS =
```

PLEX_PATROL's log is found at `/opt/plex_patrol/status.log`:

```shell
2023-03-29 20:07:06,432 - INFO       - plex_patrol                              -  <module>                 -
       _                         _             _
 _ __ | | _____  __  _ __   __ _| |_ _ __ ___ | |
| '_ \| |/ _ \ \/ / | '_ \ / _` | __| '__/ _ \| |
| |_) | |  __/>  <  | |_) | (_| | |_| | | (_) | |
| .__/|_|\___/_/\_\ | .__/ \__,_|\__|_|  \___/|_|
|_|                 |_|

#########################################################################
# Author:   l3uddz                                                      #
# URL:      https://github.com/l3uddz/plex_patrol                       #
# --                                                                    #
# Part of the Cloudbox project: https://cloudbox.rocks                  #
#########################################################################
# GNU General Public License v3.0                                       #
#########################################################################

2023-03-29 20:07:06,433 - INFO       - plex_patrol                              -  <module>                 - Initializing
2023-03-29 20:07:06,433 - INFO       - plex_patrol                              -  <module>                 - Validating server 'http://plex:32400' with token 'YOUR_TOKEN_HERE'
2023-03-29 20:07:06,450 - INFO       - plex_patrol                              -  <module>                 - Server token was validated, proceeding to uphold the law!
...
```
