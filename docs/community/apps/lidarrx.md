# Lidarr**X**

## What is it?

[Lidarr**X**](https://lidarr.audio/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [Lidarr](../../apps/lidarr.md).

Lidarr is a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new albums from your favorite artists and will interface with clients and indexers to grab, sort, and rename them. It can also be configured to automatically upgrade the quality of existing files in the library when a better quality format becomes available.

## Project Information

- [:material-home: Lidarr ](https://lidarr.audio/#home){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://wiki.servarr.com/lidarr){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/Lidarr/Lidarr){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/hotio/lidarr){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-lidarrx

```

### 2. URL

- To access Lidarr**X**, visit `https://lidarrX._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the Lidarr**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

   ``` { .yaml }
    lidarrx:
      roles:
        - flac
        - mp3
   ```

- For app specific instructions refer to the parent role,
     - [Lidarr](../../apps/lidarr.md)<Br/>
     - and the upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://wiki.servarr.com/lidarr){: .header-icons target=_blank rel="noopener noreferrer" }
