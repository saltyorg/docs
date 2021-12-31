# Mylar3

## What is it?

[Mylar3](https://github.com/mylar3/mylar3){: target=_blank rel="noopener noreferrer" } is an automated Comic Book downloader (cbr/cbz) for use with SABnzbd, NZBGet and torrents. Also provides an OPDS server distribution.

Mylar allows you to create a watchlist of series that it monitors for various things (new issues, updated information, etc). It will grab, sort, and rename downloaded issues. It will also allow you to monitor weekly pull-lists for items belonging to said watchlisted series to download, as well as being able to monitor and maintain story-arcs.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://github.com/mylar3/mylar3){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/mylar3/mylar3/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/mylar3/mylar3){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/hotio/mylar3){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-ROLENAME

```

### 2. URL

- To access Mylar3, visit `https://ROLENAME._yourdomain.com_`

### 3. Setup

1. It's highly unlikely your mylar install is up to date. <br />
  Press the Update link on the dialog in the bottom right hand corner. Mylar3 will update and then restart.

2. Enable some authentication. Add a `username` and `password` and set your preferred `login method`.

3. Make sure `Launch Browser on startup` is disabled.

4. You'll need a [ComicVine API](https://comicvine.gamespot.com/api/){: target=_blank rel="noopener noreferrer" } Key for Mylar to be useful. [Create an account](https://comicvine.gamespot.com/login-signup/){: target=_blank rel="noopener noreferrer" }, and your key will be at [the top of this page](https://comicvine.gamespot.com/api/){: target=_blank rel="noopener noreferrer" }.

5. Set the Comic Location path to `/comics`. It will already be mounted.

6. Uncheck `enforce permissions`

7. _Optional_: Enable `Series-Annual Integration`

8. Save and then restart the app

!!! Note
      If you enable to OPDS server, DO NOT ENABLE `OPDS Fetch MetaInfo`. It queries the file system.
### Download settings
(These instructions are for NZBGet. Adapt for other Download Apps)
#### Configure NZBGet

1. Log into `https://nzbget._youdomain_.com`

2. Go to `Settings > Categories`

3. Scroll to bottom, click `Add Another Category`

4. Name it `mylar`
#### Configure Mylar

1. Set Usenet client to NZBGet

1. Fill in the server stuff like it would be in sonarr / radarr / etc

1. Set values:

   1. Host: `nzbget`

   1. Port: `6789`

   2. Username:  `Your NZBGet Username`

   3. Password:  `Your NZBGet Password`

   4. Category: `mylar`

   5. Use SSL: `No`

   6. NZBGet Download Directory: Leave Blank

   7. Enable Completed Download Handling: `X`
### Search Providers

1. Click Add Indexer (`+`).

1. Select "Newznab".

1. Add the following:

      1. Use Newznab: `X`

      2. NewzNab Name: `NZBHydra2`

      3. NewzNab Host: `http://nzbhydra2:5076`

      4. Verify SSL: `Disabled`

      5. API Key: `Your NZBHydra2 API Key`

      6. Enabled: `X`

### Quality and Post Processing

1. Enable Failed Download Handling: `X`

1. Enable Automatic-Retry for Failed Downloads: `X`

1. Enable Post-Processing: `X`

1. When Post-Processing `move` the files

### Advanced Settings
These settings are up to the user

1. Rename Files: `X`

1. Folder Format: `$Series ($Year)` _(My recommendation)_

1. File Format: `$Series $Annual $Issue ($Year)` _(My recommendation)_

### See the Mylar Wiki for more information
- [:octicons-link-16: Documentation](https://github.com/mylar3/mylar3/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
