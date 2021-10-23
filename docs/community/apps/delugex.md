# DelugeX

## What is it?

[DelugeX](https://deluge-torrent.org/){: target=_blank rel="noopener noreferrer" } is an [arrX role](../../community/apps/arrx.md) for [Deluge](../../community/apps/deluge.md).

## Project Information

- [:material-home: Deluge ](https://deluge-torrent.org/){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://dev.deluge-torrent.org/wiki/UserGuide){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://git.deluge-torrent.org/deluge){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://registry.hub.docker.com/r/linuxserver/deluge){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-delugex

```

### 2. URL

- To access DelugeX, visit `https://delugex._yourdomain.com_`

### 3. Setup

1. Read through the general [arrX role instructions](../../community/apps/arrx.md).

2. Add your X instance names to the DelugeX section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

   ``` { .yaml }
    delugex:
      roles:
        - 1080webdl
        - 1080remux
   ```

- For app specific instructions refer to the parent role,
     - [deluge](../../community/apps/deluge.md) <br />
     - and the upstream documentation <br />
       [:octicons-link-16: Documentation ](https://dev.deluge-torrent.org/wiki/UserGuide){: .header-icons target=_blank rel="noopener noreferrer" }
