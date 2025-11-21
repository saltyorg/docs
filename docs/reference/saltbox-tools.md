---
hide:
  - tags
tags:
  - tools
---

# Tools installed by Saltbox

<!-- TOC depthFrom:1 depthTo:2 withLinks:1 updateOnSave:0 orderedList:0 -->

- [Overview](#overview)
- [Details](#details)

<!-- /TOC -->

---

# Overview

Saltbox comes with some useful command line tools and scripts. Some are meant to be utilized by Saltbox, automatically (e.g. ncdu, torrentcleanup.py, etc), and some are for your usage.

|  <pre>                          </pre>  Name                 | <pre>     </pre>  Type       | <pre>                                                                    </pre> Description                                                                                    |    <pre>                                     </pre> Invoked by                        |  <pre>                                                                  </pre> Homepage                                                           |
|:---------------------- |:----------- |:---------------------------------------------------------------------------------------------- |:------------------------------------ |:------------------------------------------------------------------- |
| htop                   | application | Interactive process viewer for Unix.                                                           | `htop`                               | <http://hisham.hm/htop/>                                              |
| ctop                   | application | Top-like interface for container metrics.                                                      | `ctop`                               | <https://ctop.sh/>                                                    |
| iotop                  | application | Top like utility for disk I/O.                                                                 | `iotop`                              | <http://guichaz.free.fr/iotop/>                                       |
| nload                  | application | Monitor network traffic and bandwidth usage in real time.                                      | `nload`                              | <http://www.roland-riegel.de/nload/>                                  |
| vnstat                 | application | Network traffic monitor for that keeps a log of network traffic for the selected interface(s). | `vnstat`                             | <http://humdi.net/vnstat/>                                            |
| nethogs                | application | Small 'net top' tool that groups bandwidth by process.                                         | `nethogs`                            | <https://github.com/raboof/nethogs>                                   |
| ngrok                  | application | Secure tunnels to localhost.                                                                   | `ngrok`                              | <https://ngrok.com/>                                                  |
| ufw                    | application | UFW, or Uncomplicated Firewall, is a front-end to iptables.                                    | `ufw`                                | <https://launchpad.net/ufw>                                           |
| speedtest-cli          | application | Command line interface for testing internet bandwidth using speedtest.net                      | `speedtest`                          | <https://github.com/sivel/speedtest-cli>                              |
| Rclone                 | application | "rsync for cloud storage".                                                                     | `rclone`                             | <https://rclone.org/>                                                 |
| tree                   | application | Displays an indented directory tree, in color.                                                 | `tree`                               | <http://mama.indstate.edu/users/ice/tree/>                            |
| ncdu                   | application | Disk usage analyzer with an ncurses interface.                                                 | `ncdu`                               | <https://dev.yorhel.nl/ncdu>                                          |
| GNU Midnight Commander | application | A visual file manager.                                                                         | `mc`                                 | <https://midnight-commander.org/>                                     |
| hostess                | application | Tool for tweaking local DNS by managing your /etc/hosts file.                                  | `hostess`                            | <https://github.com/cbednarski/hostess>                               |
| logrotate              | application | Utility is designed to simplify the administration of log files.                               | `logrotate`                          | <https://fedorahosted.org/logrotate/>                                 |
| frontail               | application | Node.js application for streaming logs to the browser, like a tail -F with a UI.               | `frontail`                           | <https://github.com/mthenw/frontail>                                  |
| certbot                | application | Fetches and revokes certificates from Let’s Encrypt. Used by revoke_certs.sh.                  | `certbot`                            | <https://certbot.eff.org/>                                            |
| TorrentCleanup.py      | script      | Cleans up extracted media files in Rutorrent's downloads folder.                               | Sonarr / Radarr                      | Credit: <https://github.com/l3uddz>                                   |

# Details

-Work in progress-

## Torrent Cleanup Script

TorrentCleanup.py has been explained in the Sonarr section, but in a nutshell, sonarr/radarr launches this script if you set it up, and it will scan the folder of the file that was imported, if rars exist, delete the file that was imported. this is useful for torrent sites that allow rars, as it will only leave you with the imported file (before its uploaded to google) and just the rars for seeding, instead of also leaving the extracted file.

## NCDU

(`cd / && sudo ncdu -x`)

## Frontail - view logs over http

[frontail](https://github.com/mthenw/frontail) is a Node.js application for streaming logs to the browser (basically a tail -F with an UI).

This is useful in cases you need help and need to show someone from slack support channels your logs. You can mask your IP using ngrok (more on that later).

Steps to do so are as follows:

### Base command

```shell
frontail --ui-highlight --ui-highlight-preset /opt/scripts/frontail/frontail_custom_preset.json --theme dark --user seed --password seed <path of log file> &
```

- You may change the user and password.

- The `&` at the end sends it to the background.

- You can now see this log at <http://serveripaddress:9001>.

- To specify another port, just add: ` --port <port> `

### To create an alias for this

Determine your default shell in `settings.yml`

For your default shell, add `shell_<shell>_<shell>rc_block_custom:` to your [Inventory](../saltbox/inventory/index.md) file:
Example for Bash (default):

```yaml
shell_bash_bashrc_block_custom: |
  ## Custom frontail alias
  alias ftail='frontail --ui-highlight --ui-highlight-preset /opt/scripts/frontail/frontail_custom_preset.json --theme dark --user seed --password seed '
```

Example for ZSH:

```yaml
shell_zsh_zshrc_block_custom: |
  ## Custom frontail alias
  alias ftail='frontail --ui-highlight --ui-highlight-preset /opt/scripts/frontail/frontail_custom_preset.json --theme dark --user seed --password seed '
```

Run `sb install shell`

You can now use:

```shell
ftail --port <port number> <log path> &
```

### To quit the frontail

```shell
pkill -f frontail
```

### Examples

#### Plex Autoscan

```shell
frontail --port 9001 --ui-highlight --ui-highlight-preset /opt/scripts/frontail/frontail_custom_preset.json --theme dark --user seed --password seed /opt/plex_autoscan/plex_autoscan.log &
```

or via alias...

```shell
ftail --port 9001 /opt/plex_autoscan/plex_autoscan.log &
```

or via docker...

```shell
docker run --restart=always --name "frontail_plex_autoscan" -d -p 9001:9001 -v /opt/plex_autoscan:/logs -v /opt/scripts/frontail/frontail_custom_preset.json:/preset/custom.json mthenw/frontail --ui-highlight  --ui-highlight-preset /preset/custom.json --theme dark --user <user> --password <pass> /logs/plex_autoscan.log
```

Log: <http://serveripaddress:9001>

#### Cloudplow log

```shell
frontail --ui-highlight --port 9002 --ui-highlight-preset /opt/scripts/frontail/frontail_custom_preset.json --theme dark --user seed --password seed /opt/cloudplow/cloudplow.log &
```

Log: <http://serveripaddress:9002>

or via alias...

```shell
ftail --port 9002  /opt/cloudplow/cloudplow.log &
```

or via docker...

```shell
docker run --restart=always --name "frontail_cloudplow" -d -p 9002:9001 -v /opt/cloudplow:/logs -v /opt/scripts/frontail/frontail_custom_preset.json:/preset/custom.json mthenw/frontail --ui-highlight  --ui-highlight-preset /preset/custom.json --theme dark --user <user> --password <pass> /logs/cloudplow.log
```

Log: <http://serveripaddress:9002>

### Use ngrok to hide your IP

If you want to share your log with someone (forums, slack, etc), but don't want to reveal your IP address, you can use ngrok to hide your IP address.

```shell
ngrok http <port>
```

It will show you something like this...

![](https://i.imgur.com/74nNEdG.png)

You can now use the `http://XXXXXXXX.ngrok.io` address to share your log. This will be active as long as ngrok is running. To cancel, `ctrl-c`.
