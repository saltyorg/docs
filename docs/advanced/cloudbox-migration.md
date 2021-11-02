# Notes on migrating from cloudbox

## Restoring a cloudbox backup

Start with a fresh install of Ubuntu 20.04

```
curl -sL https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox
```

Then copy your backup `rclone.conf` to `/srv/git/saltbox` and edit the configuration files as needed.

NOTE: ANSIBLE VAULT NO LONGER SUPPORTED

```
sb install preinstall
```

Now switch to the newly created user specified in your configuration.

```
sb install restore
```

Then you should be able to install tags as you want.

## Notes:

plex version now in inventory

plexdrive, unionfs gone

ansible vault no longer supported

