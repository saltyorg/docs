# qBit Management

## What is it?

[qBit Management](https://github.com/StuffAnThings/qbit_manage) is a program used to manage your qBittorrent instance.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: qBit Management](https://github.com/StuffAnThings/qbit_manage){: .header-icons } | [:octicons-link-16: Docs](https://github.com/StuffAnThings/qbit_manage/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/StuffAnThings/qbit_manage){: .header-icons } | [:material-docker: Docker:](https://hotio.dev/containers/qbitmanage/){: .header-icons } |

**Functions include:-** <br />

- Tag torrents based on tracker and then set seed goals/limit upload speed by tag.

- Update categories based on save directory.

- Remove unregistered torrents (delete data & torrent if it is not being cross-seeded, otherwise it will just remove the torrent).

- Automatically add cross-seed torrents in paused state. <br />
    *Note: cross-seed now allows for torrent injections directly to qBit, making this feature obsolete.*

- Recheck paused torrents sorted by lowest size and resume if completed.

- Remove orphaned files from your root directory that are not referenced by qBittorrent.

- Tag any torrents that have no hard links and allows optional cleanup to delete these torrents and contents based on maximum ratio and/or time seeded.

- RecycleBin function to move files into a RecycleBin folder instead of deleting the data directly when deleting a torrent.

- Built-in scheduler to run the script every x minutes. (Can use --run command to run without the scheduler).

- Webhook notifications with Notifiarr and Apprise API integration.

### 1. Installation

Before installing qBit Management, you should have a **[qBittorrent](../../apps/qbittorrent.md)** instance running on your local machine.

``` shell

sb install sandbox-qbit-manage

```

After installation has finished, stop the qbit-manage docker container and edit the config file that will have been created at `/opt/qbit-manage/config.yml`

```shell
docker stop qbit-manage
```

Minimally you will need to change the following items in order to connect with your qBittorrent instance:-

```yaml
    qbt:
      host: "qbittorrent:8080"
      user: "qbittorrent_username"
      pass: "qbittorrent_password"

    directory:
      cross_seed: "/your/path/here/"
      root_dir: "/mnt/unionfs/downloads/torrents/qbittorrent/completed/"
      remote_dir: "/mnt/unionfs/torrents/your/path/here/"
```

An indepth explanation of the config file settings can [be found here.](https://github.com/StuffAnThings/qbit_manage/wiki/Config-Setup#config-file)

The config file is full of examples that more than likely will not work for you, sections you aren't using can be safely commented out or left blank. An up to date example configuration file [can be found here](https://github.com/StuffAnThings/qbit_manage/blob/master/config/config.yml.sample) when you wish to add newer features or restore a self mangled section. YAML spacing matters.

After making adjustments to the config file, you can start the docker container again.

```shell
docker start qbit-manage
```

Either tail the log ( `tail -f "/opt/qbit-manage/logs/activity.log"` ) or open the log file after a few minutes to check for any errors or behaviour that may have been unexpected. The container has been deliberately set to **DRY RUN MODE** initially so you can see what the script will do without actually moving deleting, tagging, or categorising anything.. Once you are happy your life's work will not be destroyed and any errors have been resolved you can edit the qbit_manage variables in the sandbox settings.yml file and then run the role again. Set `qbt_dry_run: false` to run in live mode. This will delete and move files according to your settings.

Apply the changes to the sandbox settings file with:

``` shell

sb install sandbox-qbit-manage

```

### 3. Setup

The following variables are available to set in the sandbox settings.yml file. An explanation of [these settings can be found here](https://github.com/StuffAnThings/qbit_manage/wiki/Docker-Installation).

```yaml
qbit_manage:
  qbt_run: "false" # Default is "false"
  qbt_schedule: "30" # Default is "30"
  qbt_config: "config.yml" # Default is "config.yml"
  qbt_logfile: "activity.log" # Default is "activity.log"
  qbt_cross_seed: "false" # Default is "false"
  qbt_recheck: "false" # Default is "false"
  qbt_cat_update: "false" # Default is "false"
  qbt_tag_update: "false" # Default is "false"
  qbt_rem_unregistered: "false" # Default is "false"
  qbt_rem_orphaned: "false" # Default is "false"
  qbt_tag_nohardlinks: "false" # Default is "false"
  qbt_skip_recycle: "false" # Default is "false"
  qbt_dry_run: "true" # Default is "false"
  qbt_log_level: "INFO" # Default is "INFO"
  qbt_divider: "=" # Default is "="
  qbt_width: "100" # Default is "100"
```

- [:octicons-link-16: Documentation: qBit Management Docs](https://github.com/StuffAnThings/qbit_manage/wiki){: .header-icons }
