# Beets

## What is it?

[Beets](https://beets.io/){: target=_blank rel="noopener noreferrer" } catalogs your collection, automatically improving its metadata as it goes using the MusicBrainz database. Then it provides a bouquet of tools for manipulating and accessing your music.

Beets is a music library manager and not, for the most part, a music player. It does include a simple player plugin and an experimental Web-based player, but it generally leaves actual sound-reproduction to specialized tools.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://beets.io/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](http://beets.readthedocs.org/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](http://github.com/beetbox/beets){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/beets){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

```  { .shell }

sb install sandbox-beets

```

### 2. URL

- To access Beets, visit `https://beets._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#configuration) file located in `/srv/git/saltbox/accounts.yml`
- When the role is run, a cron job is set to automatically import any music found at `/mnt/local/downloads/music` every hour.  <br />
  If a match is under 95% beets will skip the file and it will need manual importing.
- To run a manual import (which will help correct any matches under 95%) run the following command:

    ``` { .shell }
    rm /opt/beets/state.pickle && docker exec -it beets /bin/bash -c 'beet import /downloads'
    ```

- If you want to change the folder structure you should do so in the config file located at  <br />
  `/opt/beets/config.yaml` <br />
  [This link details the allowed options](https://beets.readthedocs.io/en/v1.4.7/reference/config.html#path-format-configuration){: target=_blank rel="noopener noreferrer" }

    If you already have imported music you will need to run an import using the following command:

    ``` { .shell }
    docker exec -it beets /bin/bash -c 'beet import /music'
    ```

- [:octicons-link-16: Documentation](http://beets.readthedocs.org/){: .header-icons target=_blank rel="noopener noreferrer" }
