# Notifiarr Client

## What is it?

[Notifiarr Client](https://notifiarr.com/) is the unified client for Notifiarr.com. The client enables content requests from Media Bot in your Discord Server. It also provides reports for Plex usage and system health. Other features can be [configured on the Notifiarr website.](https://notifiarr.com/)

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://notifiarr.com/){: .header-icons } | [:octicons-link-16: Docs](https://notifiarr.wiki/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Notifiarr/notifiarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/golift/notifiarr){: .header-icons }|

### 1. Setup

You will need a Notifiarr account api key to use Notifiarr. You can get one by [signing up for a free account.](https://notifiarr.com/guest/register){: .header-icons }

After logging in, you should be redirected to your profile screen.

- Click on Generate API Key (This needs to be done)
- Select your Country
- Select your Timezone
- Change your Time Format to your liking
- Select your Notification Language
- **Don't forget to Save your changes**

Add your API key to the **[Sandbox settings file](../../sandbox/settings.md)**

You also need to define a username and password for the Notifiarr client webui in the [Sandbox settings file](../../sandbox/settings.md). You can review the password requirements [here](https://github.com/Notifiarr/notifiarr#webui).

### 2. Installation

``` shell

sb install sandbox-notifiarr

```

### 3. URL

- The Notifiarr url will only display the app status `https://notifiarr._yourdomain.com_`

Now go to the Notifiarr website and configure your integrations and discord server.
Refer to the [Notifiarr documentation](https://notifiarr.wiki/) for more information.

The role will attempt to configure Sonarr, Radarr, Plex, and Tautulli. Other apps can be edited in the config file which can be found at `"/opt/notifiarr/notifiarr.conf"` in a standard install. From time to time new options will be added and an [example config file can be found here.](https://github.com/Notifiarr/notifiarr/blob/main/examples/notifiarr.conf.example)

A guide to setup and sync TRaSH guides with Radarr and Sonarr can be found on the [TRaSH Guides website](https://trash-guides.info/Guide-Sync/).

## Advanced

### Snapshot Feature Support

1. Add the following to your Inventory file to enable Privileged mode for Notifiarr and allow it access to system information

     ```yaml
     notifiarr_privileged: true
     ```

2. Run the Notifiarr role:

      ```shell
      sb install sandbox-notifiarr
      ```

[:octicons-link-16: Documentation: Notifiarr Client Docs](https://notifiarr.wiki/){: .header-icons }
