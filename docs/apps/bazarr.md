# Bazarr

## What is it?

[Bazarr](https://www.bazarr.media/) is a companion application to Sonarr and Radarr that manages and downloads subtitles based on your requirements.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.bazarr.media/){: .header-icons } | [:octicons-link-16: Docs](https://wiki.bazarr.media/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/hotio/bazarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/bazarr){: .header-icons }|

### 1. Installation

``` shell

sb install bazarr

```

### 2. URL

- To access Bazarr, visit `https://bazarr._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation](https://wiki.bazarr.media/){: .header-icons }

- [:octicons-link-16: TraSH Guides](https://trash-guides.info/Bazarr/)

There are some settings that - depending on your specific setup - should be adapted to reduce API calls down to a managable level.

[:octicons-link-16: Performance Tuning](https://wiki.bazarr.media/Additional-Configuration/Performance-Tuning/) contains some - especially of note:
`Settings` => `Subtitles` => `Performance / Optimization` Disable `Use Embedded Subtitles` Embedded subtitles are subtitles that are in the video container (mkv, mp4, etc) Bazarr needs to look inside the video container to know which subtitles are in it this can be resource intensive for some low powered devices and also give you issues with API Limits if you store your media on the cloud.

In addition:

- `Settings` => `Languages` => `Embedded Tracks Language` Disable `Deep analyze media file to get audio tracks language.`

- `Settings` => `Subtitles` => `Performance / Optimization` Enable `Skip video file hash calculation` - (Possibly depending on the cloud backend) it seems to trigger a full read by multiple API calls instead of just getting the hash

- `Settings` => `Subtitles` => `Post-Processing` Disable `Automatic Subtitles Synchronization` - This one hurts quite a bit to disable, but if you are downloading multiple subtitles (like you just downloaded multiple series and they got pushed to the cloud by cloudplow before Bazarr pulled subs; or subs got released for a whole series en block, etc.) it will trigger Bazarr to download and analyze a whole bunch of files possibly triggering tens of thousands of API-calls.
