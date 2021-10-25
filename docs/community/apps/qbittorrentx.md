# qBittorrent**X**

## What is it?

[qBittorrent**X**](https://www.qbittorrent.org/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [qBittorrent](../../community/apps/qbittorrent.md).

## Project Information

- [:material-home: qBittorrent ](https://www.qbittorrent.org/){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://github.com/qbittorrent/qBittorrent/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/qbittorrent/qBittorrent){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/saltydk/qbittorrent){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-qBittorrentX

```

### 2. URL

- To access qBittorrent**X**, visit `https://qbittorrentX._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the qBittorrent**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

   ``` { .yaml }
    qbittorrentx:
      roles:
        - longtermseed
        - educational
   ```

- For app specific instructions refer to the parent role,
     - [qBittorrent](../../community/apps/qbittorrent.md)<Br/>
     - and the upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://github.com/qbittorrent/qBittorrent/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
