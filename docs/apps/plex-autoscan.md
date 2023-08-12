# Plex Autoscan

## What is it?

[Plex Autoscan](https://github.com/l3uddz/plex_autoscan/) (by [l3uddz](https://github.com/l3uddz/)) is a script that assists Plex with the adding media files, that were imported by Sonarr / Radarr, by only scanning the folder that has been imported (vs the entire section library folder), thereby preventing excessive cloud storage activity.

Plex Autoscan comes configured out of the box (as related to Saltbox). However, there a few things that need to be set by you.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| :material-home: Project home | :octicons-link-16: Docs | [:octicons-mark-github-16: Github](https://github.com/l3uddz/plex_autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | :material-docker: Docker |

### 1. Installation

``` shell

sb install plex_autoscan

```

### 2. Setup

The role will configure Plex Autoscan, which should leave it ready to go.  However, there are some details you may need to tweak yourself.

#### Do a One-Time, Manual Scan in Plex

- For Plex Autoscan to work, at least one item needs to exist in each library before new items can show up.

- If you already have media, simply add it to the library and do a manual scan within Plex, for each library you have, to build the DB.

- If you currently don’t have any media, continue on with the setup, and when you have acquired some media, you will then perform a do a manual scan within Plex, for each library, to build the DB.

- For more info, see [this](plex.md).

#### Add Your Plex Access Token into Plex Autoscan Config

_You can skip this step if you entered in your Plex credentials in [accounts.yml](../reference/accounts.md) during setup._

_Note: For Mediabox / Feederbox setups, the following will be done on the Mediabox._

   1. Get your Plex Autoscan Token [here](../reference/plex_auth_token.md).

   2. On the server's shell, run the following command:

      ```shell
      nano /opt/plex_autoscan/config/config.json
      ```

   3. Add the Plex Access Token to `"PLEX_TOKEN":` so that it now appears as:

      ```json
      "PLEX_TOKEN": "xxxxxxxxxxxxxx",
      ```

      Note: Make sure it is within the quotes (`"`) and there is a comma (`,`) after it.

   4. <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd> to save.

#### Obtaining the Plex Autoscan URL

_Note: For Mediabox / Feederbox setup, the following will be done on the Mediabox._

The Plex Autoscan URL is needed during the setup of [Sonarr](sonarr.md#plex-autoscan), [Radarr](radarr.md#plex-autoscan), and [Lidarr](lidarr.md#plex-autoscan).

To get your Plex Autoscan URL, run the following command:

 ```shell
 /opt/scripts/plex_autoscan/plex_autoscan_url.sh
 ```

This will be in the format of:
`http://subdomain.domain.com:plex_autoscan_port/plex_autoscan_pass`

or

`http://server_ip_address:plex_autoscan_port/plex_autoscan_pass`

Example:

`http://plex.domain.com:3468/aiG7Uwie9iodTTlaisahcieNaeVonu6I`

_Note 1: The url will not use `plex.domain.com` if the IP address it points to does not match the server's IP address (e.g. Cloudflare CDN enabled)._

_Note 2: If the url is `plex.domain.com`, but you decide to enable Cloudflare proxy for the `plex` subdomain later, you will need to generate another Plex Autoscan URL and add that into Sonarr/Radarr/Lidarr instead, as the scan request will need to go to you server's actual IP and not a Cloudflare one._

_Note 3: For Mediabox setups, make sure that the port is open in the firewall and/or router._

_Note 4: The PAS URL is not meant to be accessed via a browser by default (i.e. going there will give you a `401 Unauthorized` error). However, you can enable a web UI for manual scan requests, see [here](../reference/plex-autoscan-extras.md#web-app)._

#### Upload Control File to Cloud Storage

The following step is important so that Plex Autoscan can remove missing/replaced media files out of Plex (i.e. empty trash). Without it, Plex will be left with "unavailable" media that can't play (i.e. media posters with trash icons on them).

For more details on what the control file is, see [here](../faq/Plex-Autoscan.md#purpose-of-a-control-file-in-plex-autoscan).

If you used the [scripted rclone setup](../reference/rclone-manual.md); these control files were created for you, and you can skip this step.

To upload the mounted.bin control file, run the following command:

```shell
rclone touch google:/mounted.bin
```

_Note 1: If your Rclone remote config has a different name for your cloud storage remote, replace `google:` with yours._

_Note 2: Above command requires Rclone version 1.39+._

#### Edit the control files in the Plex Autoscan config file

If you did step 4; you can skip this step.

   1. On the server's shell, run the following command:

      ```shell
      ls /mnt/remote/*.bin
      ```

      To get the file names that you will need to enter into the Plex-autoscan config.

      They'll look like: `aarsqytesx-movies_mounted.bin`, and in the default case there will be three of them.

   2. On the server's shell, run the following command:

      ```shell
      nano /opt/plex_autoscan/config/config.json
      ```

   3. Find the following:

      ```json
      "PLEX_EMPTY_TRASH_CONTROL_FILES": [
        "/mnt/unionfs/mounted.bin"
      ],
      ```

      Change it to [of course, these should match the file names you found in step 2]:

      ```json
      "PLEX_EMPTY_TRASH_CONTROL_FILES": [
          "/mnt/unionfs/aarsqytesx-movies_mounted.bin",
          "/mnt/unionfs/aarsqytesx-music_mounted.bin",
          "/mnt/unionfs/aarsqytesx-tv_mounted.bin"
      ],
      ```

      Note: Make sure there is a comma (`,`) after each line except the last.

   4. <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd> to save.

#### Enabling Google Drive Monitoring in Plex Autoscan

See the [Plex-autoscan Extras page](../reference/plex-autoscan-extras.md#google-drive-monitoring)

### Invoking a manual scan in Plex Autoscan

See the [Plex-autoscan Extras page](../reference/plex-autoscan-extras.md#make-plex-scan-a-specific-file-or-folder)

### Plex Autoscan and its Virtual Environment

To make this transparent to the user, saltbox installs a wrapper script that accounts for this.  This means that you can run Plex Autoscan manually like this:

```shell
plex_autoscan COMMAND
```

For example, if some documentation says you should run:

```shell
python scan.py sections
```

In saltbox you'd run:

```shell
plex_autoscan sections
```

If this doesn't work for you, update saltbox and rerun the plex-autoscan role:

```shell
sb update
sb install plex-autoscan
```
