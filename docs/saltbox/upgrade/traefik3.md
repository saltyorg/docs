# Traefik 3.0 Upgrade

Saltbox has undergone some major breaking changes which land with the release and integration of Traefik 3.0. Those changes include

1. Upgrade Traefik to version 3.0
    1. HTTP validation for certificates is no longer enabled by default.
        1. Enable it in adv_settings.yml if not using Cloudflare or with `traefik_enable_http_validation: true` if wanting to use it without making it the default.
2. Remote mount changes - **Breaking Changes**
    1. Add support for specifying multiple remote mounts using different predefined templates (Google, Dropbox, SFTP).
    2. Moved remote mounts from `/mnt/remote` to `/mnt/remote/<remote_name>`
    3. Changed behavior to overwrite mount service files by default.
        1. The previous default was to not touch existing services. This was a necessary change to allow the addition and removal of extra mounts.
        2. As a result the old rclone_vfs.service will get removed so preserve a copy if you want to keep any tweaks you made to it.

3. Database role changes - **Breaking Changes**
    1. Added multi-instance support to database roles.
    2. Moved roles requiring databases to provision a unique database instance for each app instance.
        1. This is still being worked on and most of this was moved to a separate branch for now.
4. Authelia changes
    1. Added greater configurability to Authelia using the inventory.
    2. Added LDAP backend to Authelia as an option.

5. Add support to restoring the appdata of a single app from backup
    1. `sb install restore -e restore_tar=plex.tar` but it assumes are past any steps restore would require.
6. Changed default torrent client to qBittorrent
7. Changed default usenet client to SABnzbd
8. Add new custom container (ddns role) for keeping a dynamic IP on Cloudflare in sync with all containers using Traefik (not just Saltbox installed once).
9. Changed the rutorrent image since the previously used one was no longer getting updates.
    1. No longer includes autodl
