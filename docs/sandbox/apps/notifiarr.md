# Notifiarr Client

## What is it?

[Notifiarr Client](https://notifiarr.com/){: target=_blank rel="noopener noreferrer" } is the unified client for Notifiarr.com. The client enables content requests from Media Bot in your Discord Server. It also provides reports for Plex usage and system health. Other features can be [configured on the Notifiarr website.](https://notifiarr.com/){: target=_blank rel="noopener noreferrer" }

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://notifiarr.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://notifiarr.wiki/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Notifiarr/notifiarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/golift/notifiarr){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-notifiarr

```

### 2. URL

- The Notifiarr url will only display the app status `https://notifiarr._yourdomain.com_`

### 3. Setup

You will need a notifiar account api key to use notifiarr. You can get one by [signing up for a free account.](https://notifiarr.com/register.php){: .header-icons target=_blank rel="noopener noreferrer" }

After logging in, you should be redirected to your profile screen.

  - Click on Generate API Key (This needs to be done)
  - Select your Country
  - Select your Timezone
  - Change your Time Format to your liking
  - Select your Site Theme
  - Select your Notification Language
  - **Don't forget to Save your changes**

Add your API key to the **[Sandbox settings file](../../sandbox/settings.md)**

Now run the installer

``` shell

sb install sandbox-notifiarr

```

Now go to the Notifiarr website and configure your integrations and discord server.
Refer to the [Notifiarr documentation](https://notifiarr.wiki/) for more information.

The role will attempt to configure sonarr, radarr, plex, and tautulli. Other apps can be edited in the config file which can be found at `"/opt/notifiarr/notifiarr.conf"` in a standard install. From time to time new options will be added and an [example config file can be found here.](https://github.com/Notifiarr/notifiarr/blob/main/examples/notifiarr.conf.example){: target=_blank rel="noopener noreferrer" }

A quickstart guide can be found on the [Trash Guides website.](https://trash-guides.info/Notifiarr/Quick-Start/){: target=_blank rel="noopener noreferrer" }

- [:octicons-link-16: Documentation: Notifiarr Client Docs](https://notifiarr.wiki/){: .header-icons target=_blank rel="noopener noreferrer" }
