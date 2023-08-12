# Calibre

## What is it?

[Calibre](https://calibre-ebook.com/){: target=_blank rel="noopener noreferrer" } is a powerful and easy to use e-book manager. Users say it’s outstanding and a must-have. It’ll allow you to do nearly everything and it takes things a step beyond normal e-book software. It’s also completely free and open source and great for both casual users and computer experts.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://calibre-ebook.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://manual.calibre-ebook.com/){: .header-icons target=_blank rel="noopener noreferrer" } |  | [:material-docker: Docker](https://registry.hub.docker.com/r/linuxserver/calibre){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-calibre

```

### 2. URL

- To access Calibre, visit `https://calibre._yourdomain.com_`

### 3. Setup

- The username is `abc` . The configured password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#configuration) file located in `/srv/git/saltbox/accounts.yml`

- Calibre is ready for use. If you added your pre-existing Calibre library to /mnt/local/Media/Books then you should see your library is ready to go. If not, then you have a blank library ready for you to fill.

!!! info
    Running Calibre on a headless server is not very fun. If at all possible, run Calibre on your local, home computer. Use rclone to sync the files from home to google drive, and then another sync from google drive to your server so that Calibre-Web can use it.

    A local database file is required. This means you cannot run either Calibre or Calibre-Web from a mounted teamdrive, and this is the biggest pain for many of us. The easiest solution is to simply have your database and book files all located in /mnt/local/Media/Books.

    Both Calibre and Calibre-Web expect to find your library in `/mnt/unionfs/Media/Books`. Note that per standard Saltbox setup, `/mnt/local` is included inside `/mnt/unionfs`. However, both dockers also include access to anything in your `/mnt` directory.

### 4. Handy commands for managing your calibre docker

You can access advanced features of the Guacamole remote desktop using ctrl+alt+shift enabling you to use remote copy/paste and different languages.

- Shell access whilst the container is running: <br />
  `docker exec -it calibre /bin/bash`

- To monitor the logs of the container in realtime: <br />
  `docker logs -f calibre`

- Container version number: <br />
  `docker inspect -f '{{ index .Config.Labels "build_version" }}' calibre`

- Image version number: <br />
  `docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/calibre`

- [:octicons-link-16: Documentation](https://manual.calibre-ebook.com/){: .header-icons target=_blank rel="noopener noreferrer" }
