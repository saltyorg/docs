---
hide:
  - tags
tags:
  - remove
  - install
  - installer
---

# Install

If you're migrating from Cloudbox you probably want the [Cloudbox migration instructions](../../reference/guides/cloudbox.md)

!!! warning
    The Saltbox install is expecting a fresh new install of Ubuntu. DO NOT try to install it on your existing Cloudbox, PTS or other system-wide setup.

Please read through these steps prior to executing any of them, just to get a grounding in what is going to happen through out the process. It could be that things in later steps inform your decisions in earlier steps.

Broadly, the base install consists of six steps:

1. Installing [dependencies](#step-1-dependencies)
2. Preparing your [configuration file(s)](#step-2-configuration)
3. Running a [pre-install script](#step-3-preinstall)
4. Configuring your [cloud storage](#step-4-rclone)
5. Running the [install script](#step-5-saltbox)
6. Configuring installed [applications](#step-6-app-setup)

ALL STEPS ARE REQUIRED

!!! warning
    There is no "uninstall" available. To uninstall Saltbox entirely, you will need to wipe the machine and reinstall the OS. You can remove all the containers, services, data, and the like, but there is no tracking of applications and packages that are installed in the OS.

However, it is safe to run any saltbox tag[s] [including the install tags] at will. Existing configurations are not overwritten [except for some "reset" tags and the "mounts" tag].

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

<details>
<summary>What will I see in the terminal?</summary>
<br />

Something like this:

```
~$ curl -sL https://install.saltbox.dev | sudo -H bash && cd /srv/git/saltbox
jammy is currently supported.
x86_64 is currently supported.
Installing Saltbox Dependencies.
/srv/git/saltbox$
```
</details>

!!! info
    See [here](../../reference/dependencies.md) for more information about the dependencies.


## Step 2: Configuration

Make sure you fill out the following configuration files before proceeding. Each file will be located in `/srv/git/saltbox`

???+ info
    The following steps assumes you are still logged in as root or using sudo with the following commands.

To edit any of the following configuration files use the command written in the config title.

=== "accounts.yml"

    ``` yaml title="nano /srv/git/saltbox/accounts.yml"
    ---
    apprise: # (1)!
    cloudflare:
      email: # (2)!
      api: # (3)!
    dockerhub:
      user: # (4)!
      token: # (5)!
    user:
      name: seed # (6)!
      pass: password1234 # (7)!
      domain: testsaltbox.ml # (8)!
      email: your@email.com # (9)!
      ssh_key: # (10)!
    ```

    1. apprise url. See <https://github.com/caronc/apprise#popular-notification-services> for more information.

        ```yaml

        apprise: discord://webhook_id/webhook_token

        ```

    2. Email used for the Cloudflare account.

    3. Cloudflare Global API Key.

    4. Docker Hub account name. Entering these credentials will at least double your image pull capacity from 100 every 6 hours to 200. <https://www.docker.com/blog/checking-your-current-docker-pull-rate-limits-and-status/>

    5. Docker Hub account token. *Not your password.*  A token can be created in the Security tab of your Docker Hub account.

    6. Username that will be created (if it doesn't exist) during the installation and apps that have automatic user configuration.

        Do not use root.

        Required.

    7. Password used for username account during the installation and apps that have automatic user configuration.

        See the [password considerations.](../../reference/accounts.md#password-considerations)

        Required.

    8. Domain that you want to use for the server.

        Required.

    9. Email address used for Let's Encrypt SSL certificates.

        Required.

    10. SSH Public Key. The key will be added to your configured user's `authorized_keys` file. This parameter accepts either the public key or a GitHub url (i.e. [https://github.com/charlie.keys](https://github.com/charlie.keys)) which will pull the keys you have added to your GitHub account.

=== "settings.yml"

    Note that you will likely not be able to fill in the rclone remote information until *after* you've completed the upcoming "Step 4: Rclone"  This is fine and expected.

    ``` yaml title="nano /srv/git/saltbox/settings.yml"
    ---
    authelia:
        master: yes # (1)!
        subdomain: login # (2)!
    downloads: /mnt/unionfs/downloads # (3)!
    rclone:
      enabled: yes # (4)!
      remotes: # (5)!
        - remote: google # (6)!
          settings:
            enable_refresh: yes # (18)!
            mount: yes # (7)!
            template: google # (8)!
            union: yes # (9)!
            upload: yes # (10)!
            upload_from: /mnt/local/Media # (11)!
            vfs_cache:
              enabled: no # (12)!
              max_age: 504h # (13)!
              size: 50G # (14)!
        - remote: dropbox
          settings:
            enable_refresh: yes
            mount: yes
            template: dropbox
            union: yes
            upload: no
            upload_from: /mnt/local/Media
            vfs_cache:
              enabled: no
              max_age: 504h
              size: 50G
        - remote: feeder
          settings:
            enable_refresh: yes
            mount: yes
            template: sftp
            union: yes
            upload: no
            upload_from: /mnt/local/Media
            vfs_cache:
              enabled: no
              max_age: 504h
              size: 50G
      version: latest # (15)!
    shell: bash # (16)!
    transcodes: /mnt/local/transcodes # (17)!
    ```

    1. If the current server should have Authelia installed or use one installed elsewhere. For a multi-server setup, review the [considerations](../basics/install_types.md#feederboxmediabox-setup-considerations) listed for your Authelia setup.

    2. Subdomain used for Authelia.

        Use different values here when using a Mediabox + Feederbox setup if deploying multiple Authelia instances.

        On a Feederbox where you want to use Authelia on the Mediabox just put in the same subdomain the Mediabox uses for Authelia (master having been set to no on the Feederbox). Review the [considerations](../basics/install_types.md#feederboxmediabox-setup-considerations) listed for your Authelia setup.

    3. Folder used for docker /downloads volume. Does not affect mergerfs (/mnt/unionfs).

    4. Toggle to enable/disable Rclone related deployments like mounts and cloudplow.

    5. This variable takes a list of dictonaries formatted like the example.

        Add as many remotes as you want.

    6. The name of the Rclone remote you want to use.

        You can also specify a path to use for the remote.

        ```yaml
        remote: "google:Media"
        ```
        or
        ```yaml
        remote: "my-sftp:/path/to/my/files"
        ```

    7. Toggles whether you wqant this remote mounted into the file system.

    8. The name of the template you want to use for the mount.

        Currently Saltbox supports 4 options:

        `google`, `dropbox`, `sftp` and alternatively a path to a file ("/opt/mount-templates/custom/remote.j2") containing either jinja2 template or an actual copy of a systemd service file.
        
        We recommend having the template file in a folder in /opt so that it moves with your install after a restore.

    9. Toggles whether you want this remote mount included in the union at `/mnt/unionfs`. This requires that `mount` be enabled.

    10. Toggles whether you intend to upload to this remote using Cloudplow.

    11. Defines the local path Cloudplow will use to upload from if the remote was upload enabled.

    12. Toggle for using Rclone VFS file cache.

    13. Defines the max age of files in the cache.

    14. Defines the max size of the cache.

        The cache can grow above this value in actual usage (polls the cache once a minute) so leave some headroom when using this.

    15. Rclone version that Saltbox will install.

        Valid options are **latest**, **beta** or a specific version "**1.55**".

        If specifying a version make sure to quote it as Ansible will convert the value into a float otherwise.

    16. Shell used by the system. Valid options are bash or zsh.

    17. Folder used for temporary transcode files.

    18. Does this remote type require a refresh service to find new files?  For example, `sftp`

=== "adv_settings.yml"

    ``` yaml title="nano /srv/git/saltbox/adv_settings.yml"
    ---
    dns:
      ipv4: yes # (1)!
      ipv6: no # (2)!
      proxied: no # (3)!
    docker:
      json_driver: no # (4)!
    gpu:
      intel: yes # (5)!
    mounts:
      ipv4_only: no # (6)!
    system:
      timezone: auto # (7)!
    traefik:
      cert:
        http_validation: no # (8)!
        zerossl: no # (9)!
      error_pages: no # (10)!
      hsts: no # (11)!
      metrics: no # (12)!
      provider: cloudflare # (13)!
      subdomains:
        dash: dash # (14)!
        metrics: metrics # (15)!
    ```

    1. Toggles Saltbox management of IPv4 A records with Cloudflare.

        DNS management can be disabled on a per role basis with:

        ```yaml
        rolename_dns_enabled: false
        ```

        Options are true or false

    2. Toggles Saltbox management of IPv6 AAAA records with Cloudflare.

        Additionally this toggle will enable Docker IPv6 networking when enabled.

        DNS management can be disabled on a per role basis with:

        ```yaml
        rolename_dns_enabled: false
        ```

        Options are true or false

    3. Toggles the Cloudflare A or AAAA record proxy state (CDN) when records are changed.

        This setting can be overridden on a per role basis using the inventory like this:
        
        ```yaml
        rolename_dns_proxy: false
        ```

        Options are true or false

    4. Changes the logging driver used by the Docker daemon from local to json-file.

        More information can be found [here](https://docs.docker.com/config/containers/logging/configure/)

    5. Toggles any tasks related to using Intel GPUs.

    6. Toggles whether Rclone should be limited to IPv4 in case routing over IPv6 is bad to the destination of your configured remotes.

    7. Configures the timezone used for the server and containers.

        Default is `auto` which will attempt to pick the timezone based on Geolocation of the server.

        For entering a manual value you can find supported values by using:
        ```shell
        timedatectl list-timezones
        ```
        Alternatively you can find a table on [Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

    8. Toggles whether Traefik is configured to use HTTP-01 certificate validation.

        This toggle is only useful for those using any of the supported DNS validation methods as this will be enabled by default otherwise.

    9. Toggles whether certificates will be issued by ZeroSSL instead of Let's Encrypt.

    10. Toggles custom Traefik error pages.

        See [here](../../advanced/styled-error-pages.md) for configuration details.

    11. Toggles the use of [HSTS](https://developer.mozilla.org/en-US/docs/Glossary/HSTS).

    12. Toggles the use of Traefik's Prometheus metrics endpoint, accessible at `https://metrics.domain.tld/prometheus` assuming default settings.

    13. Allows alternate DNS validation providers supported by Traefik.

        Implemented ones are listed [here](https://github.com/saltyorg/Saltbox/blob/master/defaults/providers.yml.default).

    14. Defines which subdomain the Traefik dashboard will be accessible at.

    15. Defines which subdomain the Traefik Prometheus metrics endpoint will be accessible at.

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
    From this point you'll want to make sure you run commands as the user specified in the `accounts.yml`

If the server rebooted due to a kernel update, reconnect via SSH **as the user specified in `accounts.yml`.** 

If your server did not need to reboot, **and the user in `accounts.yml` is different from the user as whom you are currently connected to the server** you can run `su username` to switch user or disconnect and reconnect to SSH as the newly created user. Everything after this point will assume you are running as the user entered in `accounts.yml`

!!! info
    If you are installing on a machine where you created a user as part of the ubuntu install, you are currently logged in as that user, and you entered that same user into `accounts.yml`, you **do not** have to run `su username` or reconnect to SSH as that user, and probably should not. You are already logged in as the "saltbox user", and you can just move on to the next step. The `su username` or reconnect are typically required only on remote systems where you may be currently connected as `root`.

!!! info
    See [here](../../reference/preinstall.md) for more information about the preinstall.

## Step 4: Rclone

!!! warning
    As noted in the previous step, from this point you'll want to make sure you are logged into the server as the user specified in the `accounts.yml`.

    TO BE PERFECTLY CLEAR: FORGET THAT THE ROOT USER EXISTS. DO NOT LOG INTO YOUR SALTBOX MACHINE AS ROOT ANY MORE.

    IF YOU THINK THIS DOESN'T APPLY TO YOU, THINK HARD ABOUT WHY YOU HAVE THAT IMPRESSION. ALMOST CERTAINLY YOU ARE MISTAKEN.

!!! info
    THIS IS AN OPTIONAL STEP, required only if you plan to use cloud storage [Google Drive, for instance]

    If you do not plan to use cloud storage, set the `rclone -> enabled: false` setting in your `settings.yml`, and skip this step.

If you already know how to set up an rclone remote pointing at cloud storage, do so with your usual methods. If not, here are five options.

Note that generally speaking these five options are mutually exclusive.

=== "Cloudbox User"
    This option is aimed at you if you are migrating your cloudbox setup.
    
    You already have the required setup complete. You should use your existing Google setup at least to start with.
    
    Generally, migrating from Cloudbox to Saltbox involves restoring a Cloudbox backup. If you do not have a Cloudbox backup, but *do* have data on Google Drive from Cloudbox, go to the "Media on Google Drive" tab to the right.

    [Cloudbox migration instructions](../../reference/guides/cloudbox.md)

=== "I have media on cloud storage"
    This option is aimed at you if you are using some other setup with an rclone-based connection to cloud storage.
    
    You probably already have the required setup complete. You should use your existing setup at least to start with.

    You will need to enter details of your remote[s] into `settings.yml`. If you have custom mount services, you can use them instead of one of the supplied templates. If not, perhaps start with the `google` template to see if it's "good enough".

    If you have lost your rclone config and need to recreate it, go to the "minimal setup" tab to the right. In step one, you can probably download the existing credential.

    [Other migration notes](../../reference/guides/other.md)

=== "Basic setup, please"
    IF YOU ARE MIGRATING FROM ANY OTHER RCLONE-BASED SETUP THIS IS PROBABLY NOT WHAT YOU WANT.

    === "Google Drive"

        The simplest possible case is:

        1. Set up a Google Project and OAuth Credential file if you don't already have one.
        This process is described [here](../../reference/google-project-setup.md). You will need the ID and Secret from that process in step 3 below. That link takes you to one step in a multi-step process. Don't continue to follow that. Follow the steps on that page and then come back here.
        2. Create a Shared Drive in the Google Web UI. [optional]
        If you don't want to use a shared drive, skip this step, but know that some pieces of saltbox [notably drive monitoring in autoscan] won't work.
        This process is described [here](../../reference/guides/google-shared-drive.md). If your Google account doesn't let you create shared drives, it's not the type af account we are assuming, and other things may not work as well.
        3. Create an rclone remote with those credentials.
        This process is described [here](../../reference/guides/rclone-remote.md).
        4. enter details about that remote in `settings.yml`

        Note: that mentions shared drives since that's our recommendation. If you want to point that remote at My Drive you can of course do so.
        
        Note: This is the SIMPLEST POSSIBLE CASE as noted above; it doesn't discuss service accounts or multiple disks because it's the SIMPLEST POSSIBLE CASE.

    === "Dropbox"

        1. Create rclone remote[s] pointing at Dropbox as described [here](../../reference/guides/rclone-remote-dropbox.md)
        2. enter remote details in `settings.yml`

    === "Other Cloud Storage"

        Rclone supports a variety of [cloud storage providers](https://rclone.org/overview/).  This does not imply that any or all cloud storage providers are suitable for the saltbox use case.

        You will need to perform two steps:
        
        1. Create an rclone remote pointing at your cloud storage as described [here](../../reference/guides/rclone-remote-generic.md)
        2. enter those remote details in `settings.yml`

Once you have set up your rclone remote[s], enter their details in `settings.yml` as discussed above in Step 2.

!!! warning
    Do not proceed until you have fully configured your rclone remote[s] as described above or disabled cloud storage in the settings.

## Step 5: Saltbox

!!! info
    You must run at least `core` prior to *any other* Saltbox tag; if you run any other tag prior to running `core`, you will see a variety of odd errors. You need to run one of these options as shown below before moving on or installing any other tags/apps.

!!! warning
    Have you either disabled rclone OR set up your remotes in both `rclone config` and `settings.yml`?  If not, go back and fix that.

If you are installing a [Feederbox/Mediabox setup](../basics/install_types.md) [if your reaction to this question is "huh?" then you are not, and should probably use the `saltbox` install], set up the Feederbox first, then add the [feeder mount](../../advanced/feeder.md) to the mediabox prior to install.

You can get a list of available install tags with `sb list`.

=== "Saltbox"

    `saltbox` is an all-in-one media server for downloading and playback. It installs `core` and a set of application as described [here](../basics/install_types.md)
    
    ```shell
    sb install saltbox

    ```

=== "Mediabox [playback]"

    `mediabox` is just the parts required for playback. It installs `core` and a set of application as described [here](../basics/install_types.md)
    
    ```shell
    sb install mediabox

    ```

=== "Feederbox [downloading]"

    `feederbox` is just the parts required for downloading. It installs `core` and a set of application as described [here](../basics/install_types.md)
    
    ```shell
    sb install feederbox

    ```

=== "Core [minimal]"

    `core` is the bare minimum required for saltbox. It installs the basics as described [here](../basics/install_types.md)
    
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

If you would like to configure cloudplow to use service accounts to exceed Google's 750G daily upload limit, and you went through the scripted rclone setup above, you can do this now. Instructions are [here](../../reference/cloudplow-config.md).

Go through these one at a time in order; some of the setups depend on previous setups.

!!! info
    This list is what's installed if you've run the `saltbox` tag. If you ran `core`, none of these are installed; if you ran `feederbox` or `mediabox` you have a subset of these.

1. [SABnzbd](../../apps/sabnzbd.md)
1. [qBittorrent](../../apps/qbittorrent.md)
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
    These are not all the available applications, just the core set that are installed by the `saltbox` tag. Click on the "Apps" header at the top for a full listing of applications available in Saltbox. Click the "Sandbox" heading for a listing of commmunity-supplied applications.

Next, some tasks to perform [after installation is complete](after.md).
