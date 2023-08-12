# What is it?

[NZBGet](https://nzbget.net/) (by Andrey Prygunkov aka hugbug) is a very efficient, cross-platform usenet downloader.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://nzbget.net){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://nzbget.net/documentation){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/nzbget/nzbget){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/hotio/nzbget){: .header-icons target=_blank rel="noopener noreferrer" }|

## 1. Accessing NZBGet

- To access NZBGet, visit `https://nzbget._yourdomain.com_`

## 2. Settings

### Paths

- Download paths have already been specified, no need to change those.

### News-Servers

- Add your [news servers](../reference/usenet-torrent.md).

### Security

- Login settings are preset out of the box (`user` / `passwd` as set in [accounts.yml](../reference/accounts.md)).

### Download Queue

- Disk Space

  - By default, minimum disk space is set at _100000_ (i.e. 100GB). When space goes lower than this, NZBGet will pause the queue. If you have a smaller hard drive, you will need to lower this setting.

### Connection

- DailyQuota

  - If you are using Google Drive and set up the 300 [service accounts in Rclone](https://docs.saltbox.dev/reference/rclone-manual/) you can ignore this.
  - Otherwise, if you are using Google Drive, it's recommended you set this to `750000` (i.e. 750GB), to coincide with the Google Drive daily upload limit.

## 3. Extensions

- Location on server: `/opt/scripts/nzbget`.

- Location within NZBGet: `/scripts/nzbget`.

## 4. Next

Are you setting Saltbox up for the first time?  Continue to [ruTorrent](rutorrent.md).
