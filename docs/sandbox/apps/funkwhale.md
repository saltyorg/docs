# Funkwhale

## What is it?

[Funkwhale](https://funkwhale.audio/) is a modern, self-hosted, free and open-source music server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://funkwhale.audio/){: .header-icons } | [:octicons-link-16: Docs](https://docs.funkwhale.audio/){: .header-icons } | [:octicons-mark-github-16: Github](https://dev.funkwhale.audio/funkwhale){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/funkwhale/all-in-one){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-funkwhale

```

### 2. URL

- To access Funkwhale, visit `https://funkwhale._yourdomain.com_`

### 3. Setup

- First create the superuser

- `docker exec -it funkwhale manage createsuperuser` <br />
   (for ease of access, set it as your Saltbox user and password.)
- enter the `exit` command when finished to return to your server's shell.

- Now configure these settings via the web GUI

- Access Funkwhale, visit `https://funkwhale._yourdomain.com_` and log in with the user and password you just created.
- Enter `Music->Add Content->Create a new Library` and fill out the information.
- Enter your new Library and Details. There will be a sharing link such as:
  `https://funkwhale.domain.com/federation/music/libraries/da8bd97b-3c3f-4e7b-92cb-6ba45721837b`
- Copy out the last portion: `da8bd97b-3c3f-4e7b-92cb-6ba45721837b`

- Return to the shell session to import music library

- `docker exec -it funkwhale /usr/bin/python3 /app/api/manage.py import_files da8bd97b-3c3f-4e7b-92cb-6ba45721837b "/music/Media/Audio/Music/**/**/*.flac" --in-place --async --recursive`

The above line explained:

- `docker exec -it funkwhale /usr/bin/python3 /app/api/manage.py import_files` tells funkwhale to import music.
- `da8bd97b-3c3f-4e7b-92cb-6ba45721837b` is your library id
- `"/music/Media/Audio/Music/**/**/*.flac"` is the path to your media.
- `--in-place` means do not copy the media into Funkwhale and leave it where it is.
- `--async` means it will import the music first and then pull the metadata`
- `--recursive` will recursively scan the folders

If everything goes as planned you'll get prompted like this:

``` { .shell }
> Checking imported paths against settings.MUSIC_DIRECTORY_PATH
> Import summary:
> - 149828 files found matching this pattern: ['/music/Media/Audio/Music/**/**/*.flac']

> - 0 files already found in database
> - 149828 new files
> Selected options: in place
> Are you sure you want to do this?
> Type 'yes' to continue, or 'no' to cancel:

```

- Answer yes at the prompt and the import will begin.

!!! info
    Useful URLs <br />
    Libraries URL: `https://funkwhale.domain.com/content/libraries/` <br />
    Admin Account Edit Page: `https://funkwhale.domain.com/api/admin/users/user/1/change/` <br />

!!! info
    If you want to use subsonic clients then you'll need to set a password here:  <br />
    `https://funkwhale.domain.com/settings`
    (subsonic protocol requires storing password in cleartext, so to avoid compromising your Funkwhale account, we use a different password).

**Additional Information:**

- [:octicons-link-16: Documentation](https://docs.funkwhale.audio/){: .header-icons }
