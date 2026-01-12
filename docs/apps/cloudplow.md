---
icon: material/server-network-outline
hide:
  - tags
tags:
  - cloudplow
saltbox_automation:
  sections:
    inventory: false
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url:
      type: releases
    - name: Community
      url:
      type: community
  project_description:
    name: Cloudplow
    summary: |
      an automatic rclone remote uploader designed to transfer files from local storage to cloud storage providers, such as Google Drive, with support for multiple remote/folder pairings.
    link: https://github.com/l3uddz/cloudplow
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Cloudplow

## Overview

[Cloudplow](https://github.com/l3uddz/cloudplow) is an automatic rclone remote uploader designed to transfer files from local storage to cloud storage providers, such as Google Drive, with support for multiple remote/folder pairings.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install cloudplow
```

## Remote Uploader Function

As setup for Saltbox, Cloudplow uploads all the content in `/mnt/local/Media/` (see [Paths](../saltbox/basics/paths.md#cloudplow)) to your cloud storage provider (e.g. Google Drive), after the folder reaches a `200` GB size threshold, when checked every `30` minutes.

_Note: The size threshold and the check interval can be changed via steps mentioned on this page._

<details>
<summary> Drive Daily Upload Limit (click to expand)</summary><br />

Google Drive has a max upload limit of about 750GB per day. When this limit is reached, Google Drive will put you in a 24 hour soft ban. When Cloudplow detects this (with the phrase `Failed to copy: googleapi: Error 403: User rate limit exceeded`), uploading will be suspended for 25 hours (i.e. a 25 hour ban sleep), and upon waking up, it will resume its checking and uploading tasks. This feature is enabled by default. This method is better than running Rclone task with a `bwlimit`, because you can just upload in bursts when the uploading resumes.

_Note: The keywords or phrases that are used to monitor the ban, and the duration of the sleep time, can be changed at any time by editing the `config.json` file._

Cloudplow can also use service accounts to upload and work around this limitation.

</details>

## Config

Note that this is an extract from the cloudplow docs and does not cover everything that cloudplow can do. Please refer to the Cloudplow github for complete details on available options.

### Default config.json file

See [Example Cloudplow configs](../reference/cloudplow.md).

### Location

```text
/opt/cloudplow/config.json
```

Note: Config changes require a restart: `sudo systemctl restart saltbox_managed_cloudplow.service`.

### Editing

Edit in your favorite code editor (with json highlighting) or even a unix editor like nano.

```shell
nano /opt/cloudplow/config.json
```

Note: The cloudplow config file is a JSON file. JSON files have a particular format and syntax. If you are unfamiliar with JSON formatting and syntax, don't edit this file until you have gained that familiarity. Here's a [random YouTube video](https://www.youtube.com/watch?v=GpOO5iKzOmY) that will give you a ten-minute overview.

### Modify Upload Threshold and Interval

```json
    "uploader": {
        "google": {
            "check_interval": 30,
            "exclude_open_files": false,
            "max_size_gb": 200,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": [
                "downloads/*"
            ]
        }
```

`"check_interval":` How often (in minutes) Cloudplow checks the size of `/mnt/local/Media`.

`"max_size_gb":` Max size (in GB) Cloudplow allows `/mnt/local/Media` to get before starting an upload task.

- Note: `max_size_gb` is rounded up, so it is advised to have it minimum `2GB` or else it would attempt upload at each interval. Explanation below.

    - Setting this to `1GB` will trigger on anything in the upload directory, since Cloudplow will round, say, 200MB usage up to 1G and trigger an upload.

    - Setting this to `2GB` will trigger on a little more than 1GB of data in the upload directory, since there needs to be more than 1G there for the value to get rounded up to 2G and trigger the upload.

    - THIS IS ONLY A SIGNIFICANT ISSUE WITH THESE SMALL NUMBERS. It's not a general "Cloudplow triggers at half the threshold". This rounding means that the default 200G threshold will actually trigger at 199+G, since 199.2G would get rounded up to 200G.

### Plex Integration

Cloudplow can throttle Rclone uploads during active, playing Plex streams (paused streams are ignored).

```json
  "plex": {
      "enabled": false,
      "url": "https://plex.domain.com",
      "token": "YOUR_TOKEN_HERE",
      "poll_interval": 60,
      "max_streams_before_throttle": 1,
      "rclone": {
          "throttle_speeds": {
              "0": "1000M",
              "1": "50M",
              "2": "40M",
              "3": "30M",
              "4": "20M",
              "5": "10M"
          },
          "url": "http://localhost:7949"
      }
  }
```

`enabled` - Change `false` to `true` to enable.

`url` - Your Plex URL.

`token` - Your [Plex Access Token](../reference/plex_auth_token.md).

`poll_interval` - How often (in seconds) Plex is checked for active streams.

`max_streams_before_throttle` - How many playing streams are allowed before enabling throttling.

`rclone`

- `url` - Leave as default.

- `throttle_speeds` - Categorized option to configure upload speeds for various stream counts (where `5` represents 5 or more streams). `M` is MB/s.

  - Format:

       ```json
       "STREAM COUNT": "THROTTLED UPLOAD SPEED",
       ```

### NZBget Integration

Cloudplow can pause the NZBGet download queue when an upload starts; and then resume it upon the upload finishing.

```json
"nzbget": {
    "enabled": false,
    "url": "https://user:pass@nzbget.domain.com"
},
```

`enabled` - `true` to enable.

### Sabnzbd Integration

Cloudplow can pause the Sabnzbd download queue when an upload starts; and then resume it upon the upload finishing.

```json
"sabnzbd": {
    "enabled": false,
    "url": "https://sabnzbd.domain.com"
    "apikey": "1314234234"
},
```

`enabled` - `true` to enable.

### Service account uploading

You can tell cloudplow to use a set of service accounts when uploading to Google Drive to go past the daily 750G upload limit. Details are available in the [cloudplow uploader documentation](https://github.com/l3uddz/cloudplow#uploader), but in a nutshell you will add the `service_account_path` to the uploader:

```json
"uploader": {
    "google": {
        "check_interval": 30,
        "exclude_open_files": true,
        "max_size_gb": 500,
        "opened_excludes": [
            "/downloads/"
        ],
        "size_excludes": [
            "downloads/*"
        ],
        "service_account_path":"/home/user/config/cloudplow/service_accounts/"
      }
}
```

If you used the saltbox scripted rclone setup, there is a script that will make these changes for you described in the [cloudplow configuration guide](../reference/cloudplow-config.md).

### Restart

Restart Cloudplow to apply the changes to the config.

```shell
sudo systemctl restart saltbox_managed_cloudplow.service
```

## Logs and status

[Details here](../reference/logs.md?h=logs#cloudplow)

## CLI

You can run a manual Cloudplow task from anywhere by just using the `cloudplow` command.

### Manual Upload

To start uploading right away, regardless of what the folder size is:

```shell
cloudplow upload
```
