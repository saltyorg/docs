If you're migrating from Cloudbox you probably want the [Cloudbox migrations instructions](https://docs.saltbox.dev/reference/guides/cloudbox/)

If you're migrating from PlexGuide there are some rudimentary notes provided by a user [here](https://docs.saltbox.dev/reference/guides/plexguide/).  Expansions to those notes would be welcome.

Please read through these steps prior to executing any of them, just to get a grounding in what is going to happen through out the process.  It could be that things in later steps inform your decisions in earlier steps.

Broadly, the base install consists of six steps:

1. Installing [dependencies](#dependencies)
2. Preparing your [configuration file(s)](#configuration)
3. Running a [pre-install script](#preinstall)
4. Configuring your [cloud storage](#rclone)
5. Running the [install script](#saltbox)
6. Configuring installed [applications](#app-setup)

## Dependencies

=== "curl"
    ``` shell
    curl -sL https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox
    ```

=== "wget"
    ``` shell
    wget -qO- https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox
    ```

=== "curl (verbose)"
    ``` shell
    curl -sL https://install.saltbox.dev | sudo -H bash -s -- -v; cd /srv/git/saltbox
    ```

=== "wget (verbose)"
    ``` shell
    wget -qO- https://install.saltbox.dev | sudo -H bash -s -- -v; cd /srv/git/saltbox
    ```

!!! info
    See [here](../../reference/dependencies.md) for more information about the dependencies.


## Configuration

Make sure you fill out the following configuration files before proceeding. Each file will be located in `/srv/git/saltbox`

`accounts.yml`

To edit [assuming you are still logged in as `root`]:

```
nano /srv/git/saltbox/accounts.yml
```

Contents:

``` { .yaml .annotate }
---
user:
  name: seed # (1)!
  pass: password123 # (2)!
  domain: testsaltbox.ml # (3)!
  email: your@email.com # (4)!
cloudflare:
  email: # (5)!
  api: # (6)!
plex:
  user: # (7)!
  pass: # (8)!
  tfa: no # (9)!
dockerhub:
  user: # (10)!
  token: # (11)!
apprise: # (12)!
```

1. Username that will be created (if it doesn't exist) during the installation and apps that have automatic user configuration.

    Do not use root.

    Required.

2. Password used for username account during the installation and apps that have automatic user configuration.

    Required.

3. Domain that you want to use for the server.

4. Email address used for Let's Encrypt SSL certificates.

    Required.

5. Email used for the Cloudflare account.

6. Cloudflare Global API Key.

7. Plex.tv username or email address on the account.

8. Plex.tv password for the account.

9. Enable if you want to use the Two Factor Authentication [TFA] compatible Plex account login.

10. Docker Hub account name. Entering these credentials will at least double your image pull capacity from 100 every 6 hours to 200. <https://www.docker.com/blog/checking-your-current-docker-pull-rate-limits-and-status/>

11. Docker Hub account token

12. apprise url. See <https://github.com/caronc/apprise#popular-notification-services> for more information.


`settings.yml`

To edit [assuming you are still logged in as `root`]:

```
nano /srv/git/saltbox/settings.yml
```

Contents:


``` { .yaml .annotate }
---
downloads: /mnt/unionfs/downloads # (1)!!
rclone:
  version: latest # (3)!
  remote: google # (4)!
shell: bash # (5)!
authelia:
  master: yes # (6)!
  subdomain: login # (7)!
```

1. Folder used for downloads.


2. Folder used for temporary transcode files.

3. Rclone version that Saltbox will install.

    Valid options are **latest**, **beta** or a specific version (**1.55**).

4. Name of the rclone remote that Saltbox will mount by default and use in any automated configuration.

    Optional - Leave empty to avoid remote mount setup.

5. Shell used by the system. Valid options are bash or zsh.

6. If the current server should have Authelia installed or use one installed elsewhere.

7. Subdomain used for Authelia.

    Use different values here when using a Mediabox + Feederbox setup if deploying multiple Authelia instances.

    On a Feederbox where you want to use Authelia on the Mediabox just put in the same subdomain the Mediabox uses for Authelia (master having been set to no on the Feederbox).

!!! info
    See [here](../../reference/accounts.md) for more information about these settings.

## Preinstall

!!! warning
    Make sure that you have set up the configuration correctly before proceeding.

This step will create the user account specified in `accounts.yml`, add it to sudoers, update the kernel, edit GRUB configuration, install Rclone, and reboot the server if needed.

``` shell
sb install preinstall
```

!!! warning
    From this point you'll want to make sure you run commands as the user specified in the accounts.yml

If your server did not need to reboot you can run `su username` to switch user or reconnect to SSH as the newly created user. Everything after this point will assume you are running as the user entered in accounts.yml

!!! info
    See [here](../../reference/preinstall.md) for more information about the preinstall.

## Rclone
Saltbox assumes an rclone remote pointed at your google storage named `google` [as shown in the settings.yml above].

There is nothing special about saltbox's implementation of this setup, aside from its opinions about the media paths.

You may already have this remote configured or know how to do it if you are coming from a similar setup like Cloudbox or PlexGuide.

If you do, you are probably best served to use your existing setup.

If you are coming from Cloudbox, you *can and should* use your existing rclone setup rather than going through the setup again.

If you are starting from scratch, the process is documented [here](../../reference/rclone.md).

!!! warning
    Do not proceed until you have configured your rclone remote[s] or disabled cloud storage in the settings.

## Saltbox

If you are installing a [Feederbox/Mediabox setup](../basics/install_types.md) [if your reaction to this question is "huh?" then you are not, and should use the `saltbox` install], set up the Feederbox first, then add the [feeder mount](../../advanced/feeder.md) to the mediabox prior to install.

=== "Saltbox"
    ``` shell
    sb install saltbox
    ```

=== "Mediabox"
    ``` shell
    sb install mediabox
    ```

=== "Feederbox"
    ``` shell
    sb install feederbox
    ```

=== "Core"
    ``` shell
    sb install core
    ```

!!! info
    See [here](../../reference/install.md) for more information about the install.

## Reboot

After rebooting, you're now ready to go through the basic setup for the apps!

## App Setup

Go through these one at a time in order; some of the setups depend on previous setups.

1. [NZBGet](../../apps/nzbget.md)
1. [ruTorrent](../../apps/rutorrent.md)
1. [NZBHydra2](../../apps/nzbhydra2.md)
1. [Jackett](../../apps/jackett.md)
1. [Plex Media Server](../../apps/plex.md)
1. [Autoscan](../../apps/autoscan.md)
1. [Sonarr](../../apps/sonarr.md)
1. [Radarr](../../apps/radarr.md)
1. [Lidarr](../../apps/lidarr.md)
1. [Tautulli](../../apps/tautulli.md)
1. [Overseerr](../../apps/overseerr.md)
1. [Portainer](../../apps/portainer.md)
1. [Organizr](../../apps/organizr.md)

Next, some tasks to perform [after installation is complete](after.md).
