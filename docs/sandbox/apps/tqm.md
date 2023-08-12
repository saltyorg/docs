# tqm

## What is it?

[tqm](https://github.com/l3uddz/tqm){: target=_blank rel="noopener noreferrer" } is a CLI tool to manage your torrent client queues. Primary focus is on removing torrents that meet specific criteria.

- The tqm binary is downloaded and a service and timer file created when the config is identified.

!!! Note
      📢 You will need to have `config.yaml` in place (`/opt/tqm/`) for the role to run successfully.  [Here](https://github.com/l3uddz/tqm#example-configuration) is an example config you can grab and fill in with your own details.

| Details     |
|-------------|
| [:octicons-mark-github-16: Github](https://github.com/l3uddz/tqm){: .header-icons target=_blank rel="noopener noreferrer" }|

Recommended install types: Feederbox, Saltbox, Core

### 1. Setup

Edit in your favorite code editor  (with yaml highlighting) or even a unix editor like nano.

``` shell

nano /opt/tqm/config.yaml

```

### Modify "Client" section

!!! Note
      📢 As setup for Saltbox, tqm uses this path to find your downloaded files:  `/mnt/unionfs/downloads/...` (see [Paths](../../saltbox/basics/paths.md#media))

Client Example:

```yaml

...
  deluge:
    enabled: false
    filter: default
    download_path: /mnt/unionfs/downloads/torrents/deluge
    free_space_path: /mnt/local/downloads/torrents/deluge
    download_path_mapping:
      /downloads/torrents/deluge: /mnt/unionfs/downloads/torrents/deluge
    host: deluge
    login: localclient
    password: password-from-/opt/deluge/auth
    port: 58846
    type: deluge
    v2: true
  qbt:
    download_path: /mnt/unionfs/downloads/torrents/qbittorrent/completed
    free_space_path: /mnt/local/downloads/torrents/qbittorrent/completed
    download_path_mapping:
      /mnt/unionfs/downloads/torrents/qbittorrent/completed: /mnt/unionfs/downloads/torrents/qbittorrent/completed
    enabled: true
    filter: default
    type: qbittorrent
    url: http://qbittorrent:8080
    user: seed
    password: super_strong_password
...

```

`download_path:` Where your downloaded files are stored.

`free_space_path:` Typically the local mergerfs path to show available space.

`enabled:` Set to boolean value (true, false) depending on the client you use.

`url:` Set to the examples equivalent of your client.

`user:` your default user from **accounts.yml**

`password:` your default password from **accounts.yml**

### Modify "Filter" section

Filter Example:

```yaml

...
filters:
  default:
    ignore:
      - TrackerName contains "sportscult"
      - TrackerStatus contains "Tracker is down"
      - Label contains "upload"
      - Downloaded == false && !IsUnregistered()
    remove:
      - IsUnregistered()
      - Label contains "-imported" && TrackerName contains "avistaz.to" && (Ratio > 2.0 || SeedingDays >= 21.0)
      - Label contains "-imported" && TrackerName contains "nebulance.io" && SeedingDays >= 6.0
      - Label in ["readarr-imported", "lidarr-imported"] && (Ratio > 5.0 || SeedingDays >= 25.0)
      - Label in ["autoremove-btn"] && (Ratio > 3.0 || SeedingDays >= 15.0)
...

```

`ignore:` Instructs **tqm** to ignore anything defined.

`remove:` Instructs **tqm** what files to delete based on what is defined in the **filter**.

Note: There are many ways to do the same thing. Check the **language definitions** for an explanation [here](https://github.com/antonmedv/expr/blob/586b86b462d22497d442adbc924bfb701db3075d/docs/Language-Definition.md){: .header-icons target=_blank rel="noopener noreferrer" }

### Modify "Label" section

Label Example:

```yaml

...
    label:
      # Permaseed Animebytes torrents (all must evaluate to true)
      - name: permaseed-AB
        update:
          - SeedingSeconds > 1000.0
          - Label contains "-imported"
          - TrackerName contains "animebytes.tv"
      # cleanup btn season packs to autoremove-btn (all must evaluate to true)
      - name: autoremove-btn
        update:
          - Label == "sonarr-imported"
          - TrackerName == "landof.tv"
          - not (Name contains "1080p")
          - len(Files) >= 3
...

```

!!! Note
      📢 tqm will not create a category for you, so be sure to create the category first. If you
      want the file moved as well, you will need to set **Default Torrent Management Mode: Automatic**.

`name:` The category (label) you want the torrent changed to.

`update:` Define what is to be moved by tqm.

### Modify the "Settings" file

You can edit the **settings.yml** file in `/opt/sandbox/`. The default is `qbt`, for qbittorrent. If you want to use deluge, change that entry. Once you set your download client, run the role again and it will update the service.

Shortened example of **settings.yml**:

```yaml

...
tandoor:
  secret_key:
tqm:
  download_client: "qbt" # Change this to deluge or whatever you specify in config.yaml
transmissionvpn:
  vpn_user:
  vpn_pass:
  vpn_prov:
...

```

### 2. Installation

``` shell

sb install sandbox-tqm

```

To check the status of the service, you can run:

```shell

sudo systemctl status tqm.service

```

You can also follow the logs with:

```shell

tail -f /opt/tqm/activity.log

```

- [:octicons-link-16: Documentation](https://github.com/l3uddz/tqm#tqm){: .header-icons target=_blank rel="noopener noreferrer" }
