# Install

If you're migrating from Cloudbox you probably want the [Cloudbox migration instructions](https://docs.saltbox.dev/reference/guides/cloudbox/)

If you're migrating from PlexGuide there are some rudimentary notes provided by a user [here](https://docs.saltbox.dev/reference/guides/plexguide/).  Expansions to those notes would be welcome.

!!! warning
    The Saltbox install is expecting a fresh new install of Ubunutu.  DO NOT try to install it on your existing Cloudbox, PTS< or other setup.

Please read through these steps prior to executing any of them, just to get a grounding in what is going to happen through out the process.  It could be that things in later steps inform your decisions in earlier steps.

Broadly, the base install consists of six steps:

1. Installing [dependencies](#step-1-dependencies)
2. Preparing your [configuration file(s)](#step-2-configuration)
3. Running a [pre-install script](#step-3-preinstall)
4. Configuring your [cloud storage](#step-4-rclone)
5. Running the [install script](#step-5-saltbox)
6. Configuring installed [applications](#step-6-app-setup)

!!! warning
    There is no "uninstall" available.  To uninstall Saltbox entirely, you will need to wipe the machine and reinstall the OS.  You can remove all the containers, services, data, and the like, but things that are installed in the OS, for example rclone, are not tracked in a way that would allow uninstalling them.

## Step 1: Dependencies

!!! info
    This is assuming you are logged into your freshly installed remote server as `root`.

=== "curl"

    ```shell
    curl -sL https://install.saltbox.dev | sudo -H bash && cd /srv/git/saltbox

    ```

=== "wget"

    ```shell
    wget -qO- https://install.saltbox.dev | sudo -H bash && cd /srv/git/saltbox

    ```

=== "curl (verbose)"

    ```shell
    curl -sL https://install.saltbox.dev | sudo -H bash -s -- -v && cd /srv/git/saltbox

    ```

=== "wget (verbose)"

    ```shell
    wget -qO- https://install.saltbox.dev | sudo -H bash -s -- -v && cd /srv/git/saltbox

    ```

!!! info
    See [here](../../reference/dependencies.md) for more information about the dependencies.

## Step 2: Configuration

Make sure you fill out the following configuration files before proceeding. Each file will be located in `/srv/git/saltbox`

???+ info
    The following steps assumes you are still logged in as root or using sudo with the following commands.

Run the following command to edit the configuration file.

``` shell
nano /srv/git/saltbox/accounts.yml
```

Content with explanations:

``` yaml title="accounts.yml"
---
user:
  name: seed # (1)!
  pass: password123 # (2)!
  domain: testsaltbox.ml # (3)!
  email: your@email.com # (4)!
  ssh_key: # (13)!
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

    See the [password considerations.](../../reference/accounts.md#password-considerations)

    Required.

3. Domain that you want to use for the server.

4. Email address used for Let's Encrypt SSL certificates.

    Required.

5. Email used for the Cloudflare account.

6. Cloudflare Global API Key.

7. Plex.tv username or email address on the account.

8. Plex.tv password for the account.  It should be wrapped in quotes if it contains any non alphanumeric characters.

9. Enable if you want to use the Two Factor Authentication [TFA] compatible Plex account login.

10. Docker Hub account name. Entering these credentials will at least double your image pull capacity from 100 every 6 hours to 200. <https://www.docker.com/blog/checking-your-current-docker-pull-rate-limits-and-status/>

11. Docker Hub account token. *Not your password.*  A token can be created in the Security tab of your Docker Hub account.

12. apprise url. See <https://github.com/caronc/apprise#popular-notification-services> for more information.

    ```yaml

    apprise: discord://webhook_id/webhook_token

    ```

13. SSH Public Key. The key will be added to your configured user's `authorized_keys` file. This parameter accepts either the public key or a GitHub url (i.e. [https://github.com/charlie.keys](https://github.com/charlie.keys)) which will pull the keys you have added to your GitHub account.

Run the following command to edit the configuration file.

``` shell
nano /srv/git/saltbox/settings.yml
```

Content with explanations:

``` yaml title="settings.yml"
---
downloads: /mnt/unionfs/downloads # (1)!!
transcodes: /mnt/local/transcodes # (2)!
rclone:
  version: latest # (3)!
  remote: google # (4)!
shell: bash # (5)!
authelia:
  master: yes # (6)!
  subdomain: login # (7)!
```

1. Folder used for docker /downloads volume. Does not affect mergerfs (/mnt/unionfs).

2. Folder used for temporary transcode files.

3. Rclone version that Saltbox will install.

    Valid options are **latest**, **beta** or a specific version (**1.55**).

4. Name of the rclone remote that Saltbox will mount by default and use in any automated configuration.

    Optional - Leave empty to avoid remote mount setup.

5. Shell used by the system. Valid options are bash or zsh.

6. If the current server should have Authelia installed or use one installed elsewhere. For a multi-server setup, review the [considerations](../basics/install_types.md#feederboxmediabox-setup-considerations) listed for your Authelia setup.

7. Subdomain used for Authelia.

    Use different values here when using a Mediabox + Feederbox setup if deploying multiple Authelia instances.

    On a Feederbox where you want to use Authelia on the Mediabox just put in the same subdomain the Mediabox uses for Authelia (master having been set to no on the Feederbox). Review the [considerations](../basics/install_types.md#feederboxmediabox-setup-considerations) listed for your Authelia setup.

!!! info
    See [here](../../reference/accounts.md) for more information about these settings.

## Step 3: Preinstall

!!! warning
    Make sure that you have set up the configuration correctly before proceeding.

This step will create the user account specified in `accounts.yml`, add it to sudoers, update the kernel, edit GRUB configuration, install Rclone, and reboot the server if needed.

```shell
sb install preinstall
```

!!! warning
    From this point you'll want to make sure you run commands as the user specified in the accounts.yml

If your server did not need to reboot you can run `su username` to switch user or reconnect to SSH as the newly created user. Everything after this point will assume you are running as the user entered in accounts.yml

!!! info
    See [here](../../reference/preinstall.md) for more information about the preinstall.

## Step 4: Rclone

!!! warning
    As noted in the previous step, from this point you'll want to make sure you are logged into the server as the user specified in the `accounts.yml`.

    TO BE PERFECTLY CLEAR: FORGET THAT THE ROOT USER EXISTS.  DO NOT LOG INTO YOUR SALTBOX MACHINE AS ROOT ANY MORE.

    IF YOU THINK THIS DOESN"T APPLY TO YOU, THINK HARD ABOUT WHY YOU HAVE THAT IMPRESSION.  ALMOST CERTAINLY YOU ARE MISTAKEN.

!!! info
    THIS IS AN OPTIONAL STEP, required only if you plan to use cloud storage [Google Drive, for instance]

    If you do not plan to use cloud storage, leave the `rclone -> remote:` setting blank in your `settings.yml`, and skip this step.

Saltbox defaults to an rclone remote pointed at your Google Drive named `google` [as shown in the settings.yml above].

There is nothing special about Saltbox's implementation of this setup, aside from its opinions about the media paths.

If you already know how to set that up, do so with your usual methods.  If not, here are five options.

Note that generally speaking these five options are mutually exclusive.

=== "Cloudbox User"
    This option is aimed at you if you are migrating your cloudbox setup.
    
    You already have the required setup complete.  You should use your existing Google setup at least to start with.
    
    Generally, migrating from Cloudbox to Saltbox involves restoring a Cloudbox backup.  If you do not have a Cloudbox backup, but *do* have data on Google Drive from Cloudbox, go to the "Media on Google Drive" tab to the right.

    [Cloudbox migration instructions](https://docs.saltbox.dev/reference/guides/cloudbox/)

=== "PlexGuide/PTS User"
    This option is aimed at you if you are migrating your PG/PTS/MHA setup.
    
    You already have the required setup complete.  You should use your existing Google setup at least to start with.

    The issues you will have to deal with will largely be around:

    1. Encrypted drives
    2. File system differences
    3. Service account files [PlexGuide removed the `.json` extension from what it calls "BlitzKeys", Saltbox expects them to be there]

    [Plexguide migration notes](https://docs.saltbox.dev/reference/guides/plexguide/)

=== "I have media on cloud storage"
    This option is aimed at you if you are using some other setup with an rclone-based connection to cloud storage.
    
    You probably already have the required setup complete.  You should use your existing setup at least to start with.

    You will likely need to account for differences in the names of remotes.  Saltbox assumes that you have an rclone remote named `google` pointing to the root of your cloud storage, so you can either rename your existing remote or change the remote name in the [settings](../../reference/accounts.md).

    If you have lost your rclone config and need to recreate it, go to the "minimal setup" tab to the right.  In step one, you can probably download the existing credential.

    [Other migration notes](https://docs.saltbox.dev/reference/guides/other/)

=== "I'm totally new to this"
    This option is aimed at you if you are starting totally from scratch and want to be walked through the whole setup.
    
    IF YOU ARE MIGRATING FROM ANY OTHER RCLONE-BASED GOOGLE SETUP YOU SHOULD NOT DO THIS.

    === "Google Drive"

        THIS IS ASSUMING YOU HAVE NO EXISTING MEDIA ON GOOGLE DRIVE OR ANYTHING ELSE.

        IF YOU ARE STARTING FRESH LATER THAN JUNE 2023 YOU PROBABLY DON'T WANT TO GO THROUGH THIS.  Changes to Google's "unlimited" offering have made this mostly needless and obsolete.

        If you have a brand new Google Drive account and want to be walked through all the steps you need to perform, start [here](../../reference/rclone.md)

        That's an eight-step process that is mostly copy-paste commands.  When you have completed it, come back here.

        That eight-step process will create seven shared drives, 300 service accounts, and will configure rclone for you.

        IF THAT IS MORE THAN YOU HAD IN MIND, TAKE A LOOK AT THE "MINIMAL SETUP" TO THE RIGHT.

        This should be enough capacity for quite a while for most users.

    === "Dropbox"

        Create rclone remote[s] pointing at Dropbox as described [here](../../reference/guides/rclone-remote-dropbox.md)

=== "Minimal setup, please"
    IF YOU ARE MIGRATING FROM ANY OTHER RCLONE-BASED SETUP THIS IS PROBABLY NOT WHAT YOU WANT.

    === "Google Drive"

        The simplest possible case is:

        1. Set up a Google Project and OAuth Credential file if you don't already have one.
        This process is described [here](../../reference/google-project-setup.md).  You will need the ID and Secret from that process in step 3 below.  That link takes you to one step in a multi-step process.  Don't continue to follow that.  Follow the steps on that page and then come back here.
        2. Create a Shared Drive in the Google Web UI. [optional]
        If you don't want to use a shared drive, skip this step, but know that some pieces of saltbox [notably drive monitoring in autoscan] won't work.
        This process is described [here](../../reference/guides/google-shared-drive.md).  If your Google account doesn't let you create shared drives, it's not the type af account we are assuming, and other things may not work as well.
        3. Create an rclone remote with those credentials.
        This process is described [here](../../reference/guides/rclone-remote.md).

        Note: that mentions shared drives since that's our recommendation.  If you want to point that remote at My Drive you can of course do so.
        
        Note: This is the SIMPLEST POSSIBLE CASE as noted above; it doesn't discuss service accounts or multiple disks because it's the SIMPLEST POSSIBLE CASE.

    === "Dropbox"

        Create rclone remote[s] pointing at Dropbox as described [here](../../reference/guides/rclone-remote-dropbox.md)

!!! warning
    Do not proceed until you have configured your rclone remote[s] or disabled cloud storage in the settings.

How do you know if your rclone remote[s] are configured?  `rclone lsd google:/` should show you the root of your cloud storage.

## Step 5: Saltbox

If you are installing a [Feederbox/Mediabox setup](../basics/install_types.md) [if your reaction to this question is "huh?" then you are not, and should probably use the `saltbox` install], set up the Feederbox first, then add the [feeder mount](../../advanced/feeder.md) to the mediabox prior to install.

!!! warning
    You must run at least `core` prior to any other Saltbox tag; if you run any other tag prior to running `core`, you will see a variety of odd errors.  You need to run one of these options as shown below before moving on or installing any other tags.

=== "Saltbox"

    `saltbox` is an all-in-one media server for downloading and playback.  It installs `core` and a set of application as described [here](../basics/install_types.md)
    
    ```shell
    sb install saltbox

    ```

=== "Mediabox [playback]"

    `mediabox` is just the parts required for playback.  It installs `core` and a set of application as described [here](../basics/install_types.md)
    
    ```shell
    sb install mediabox

    ```

=== "Feederbox [downloading]"

    `feederbox` is just the parts required for downloading.  It installs `core` and a set of application as described [here](../basics/install_types.md)
    
    ```shell
    sb install feederbox

    ```

=== "Core [minimal]"

    `core` is the bare minimum required for saltbox.  It installs the basics as described [here](../basics/install_types.md)
    
    ```shell
    sb install core

    ```

=== "Dealer's choice"

    If you want to install a personal selection of apps, install `core` and the app tags you want as listed [here](../basics/install_types.md)
    
    ```shell
    sb install core,plex,sonarr,radarr,jackett,qbittorrent

    ```

!!! info
    See [here](../../reference/install.md) for more information about the install.

## Reboot

After rebooting, you're now ready to go through the basic setup for the apps!

## Step 6: App Setup

If you would like to configure cloudplow to use service accounts to exceed Google's 750G daily upload limit, and you went through the scripted rclone setup above, you can do this now. Instructions are [here](https://docs.saltbox.dev/reference/cloudplow-config/).

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

!!! info
    These are not all the available applications, just the core set that are installed by the `saltbox` tag.  Click on the "Apps" header at the top for a full listing of applications available in Saltbox.  Click the "Sandbox" heading for a listing of commmunity-supplied applications.

Next, some tasks to perform [after installation is complete](after.md).
