# JDownloader

## What is it?

[JDownloader](https://beta.jdownloader.org/){: target=_blank rel="noopener noreferrer" } is a free download-manager that makes downloading as easy, fast and automated as it should be. It's like your personal internet robot that does all the work for you. He will download whole photo albums, playlists or just about anything else with just one click. Go ahead and try it!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://beta.jdownloader.org/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://beta.jdownloader.org/support){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/jlesage/docker-jdownloader-2){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/jdownloader-2){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-jdownloader2

```

### 2. URL

- To access JDownloader, visit `https://jdownloader2._yourdomain.com_`

### 3. Setup

1. The configured password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#configuration) file located in `/srv/git/saltbox/accounts.yml`

2. Configure your myjdownloader account (Create at <https://my.jdownloader.org/> if needed) and name your instance so you can connect via web or browser extensions. Use clipboard for two step copy and paste if needed. Note that some settings are only accessible via `jdownloader2.yourdomain.com`. Premium accounts such as mega.nz can be added via web interface.

3. Use manual import from sonarr / radarr and navigate to `/mnt/local/downloads/myjdownloader/output/` to import your files, note they must be already added as wanted media for import to recognise and identify your downloaded media.

4. See <https://my.jdownloader.org/> for browser extensions and phone apps as desired.

- [:octicons-link-16: Documentation](https://beta.jdownloader.org/support){: .header-icons target=_blank rel="noopener noreferrer" }
