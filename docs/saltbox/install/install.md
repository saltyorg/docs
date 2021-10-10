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

accounts.yml

``` { .yaml .annotate }
---
user:
  name: seed # (1)
  pass: password123 # (2)
  domain: testsaltbox.ml # (3)
  email: your@email.com # (4)
cloudflare:
  email: # (5)
  api: # (6)
plex:
  user: # (7)
  pass: # (8)
  tfa: no # (9)
apprise: # (10)
```

1. Username that will be created (if it doesn't exist) during the installation and apps that have automatic user configuration.

    Do not use root.

    Required.

2. Password used for username account during the installation and apps that have automatic user configuration.

    Required.

3. Domain that you want to use for the server.

    Required.

4. Email address used for Let's Encrypt SSL certificates.

    Required.

5. Email used for the Cloudflare account.

6. Cloudflare API Token.

7. Plex.tv username or email address on the account.

8. Plex.tv password for the account.

9. Enable if using Two Factor Authentication with your Plex account.

10. apprise url. See <https://github.com/caronc/apprise#popular-notification-services> for more information.


settings.yml

``` { .yaml .annotate }
---
downloads:
  nzbs: /mnt/local/downloads/nzbs # (1)
  torrents: /mnt/local/downloads/torrents # (2)
transcodes: /mnt/local/transcodes # (3)
rclone:
  version: latest # (4)
  remote: google # (5)
shell: bash # (6)
```

1. Folder used for usenet downloads.

2. Folder used for torrent downloads.

3. Folder used for temporary transcode files.

4. Rclone version that Saltbox will install. 

    Valid options are **latest**, **beta** or a specific version (**1.55**).

5. Rclone remote that Saltbox will mount by default and use in any automated configuration.

    Optional - Leave empty to avoid remote mount setup.

6. Shell used by the system. Valid options are bash or zsh.

!!! info
    See [here](../../reference/accounts.md) for more information about these settings.

## Preinstall

!!! warning
    Make sure that you have set up the configuration correctly before proceeding.

This step will create the specified user account, add it to sudoers, update the kernel, edit GRUB configuration and install Rclone and reboot the server if needed.

``` shell
sb install preinstall
```

!!! info
    From this point you'll want to make sure you run commands as the user specified in the accounts.yml

If your server did not need to reboot you can run `su username` to switch user or reconnect to SSH as the newly created user. Everything after this point will assume you are running as the user entered in accounts.yml

!!! info
    See [here](../../reference/preinstall.md) for more information about the preinstall.

## Rclone
Saltbox assumes an rclone remote pointed at your google storage named `google` [as shown in the settings.yml above].

!!! info
    See [here](../../reference/rclone.md) for more information about creating this remote.  The walkthrough for creating the remote is found there to keep this page short.

## Install Saltbox

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

You're now ready to install other apps and tweak the setup as you see fit. After rebooting!
