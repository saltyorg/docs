## Dependencies
``` shell
curl -sL https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox
```
## Configuration

Make sure you fill out the following configuration files before proceeding. Each file will be located in /srv/git/saltbox

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
apprise: # (9)
```

1. Username that will be created (if it doesn't exist) during the installation and apps that have automatic user configuration.

    Required.

2. Password used for username account during the installation and apps that have automatic user configuration.

    Required.

3. Domain that you want to use for the server.

    Required.

4. Email address used for Let's Encrypt SSL certificates.

    Required.

5. Email used for the Cloudflare account.

6. Cloudflare API Token. (insert link to cloudflare guide when created)

7. Plex.tv username or email address on the account.

8. Plex.tv password for the account.

9. apprise url. See <https://github.com/caronc/apprise#popular-notification-services> for more information.


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

4. Rclone version that Saltbox will install. Valid options are latest, beta or a specific version (1.55).

5. Rclone remote that Saltbox will mount by default and use in any automated configuration.

6. Shell used by the system. Valid options are bash or zsh.

## Preinstall

!!! warning
    Make sure that you have setup the configuration correctly before proceeding.

This step will create the specified user account if needed and add it to sudoers, update the kernel, edit GRUB configuration if needed and install Rclone.

``` shell
sb install preinstall
```

At this point you'll want to make sure you run commands as the user specified in the accounts.yml

You can either run 'su username' to switch user or reconnect to SSH as the newly created user.

## Rclone
This step will take you through the configuration of Rclone.

Insert really clever rclone guide xD


## Install Saltbox

=== "Saltbox"
    Some text about Saltbox

=== "Mediabox"
    Some text about Mediabox

=== "Feederbox"
    Some text about Feederbox

=== "Core"
    Some text about Core

## Reboot

You're now ready to install and tweak the setup as you see fit. After rebooting!