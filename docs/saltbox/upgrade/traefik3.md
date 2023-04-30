# Traefik 3.0 Upgrade

Saltbox has undergone some major breaking changes which land with the release and integration of Traefik 3.0. Those changes include

- Upgrade Traefik to version 3.0
- Remote mount changes - **Breaking Changes**

    - Add support for specifying multiple remote mounts using different predefined templates (Google, Dropbox, SFTP)
    - Moved remote mounts from `/mnt/remote` to `/mnt/remote/<remote_name>`
    - Changed behavior to overwrite mount service files by default. The previous default was to not touch existing services. Set `mounts_override: false` in Inventory to override/disable this behavior.

- Database role changes - **Breaking Changes**

    - Added multi-instance support to database roles
    - Moved roles requiring databases to provision a unique database instance for each app instance

- Authelia changes

    - Added greater configurability to Authelia
    - Added LDAP backend to Authelia

- Add support to restoring the appdata of a single app from backup
- Moved default torrent client to qBittorrent
- Add new custom container for keeping a dynamic IP on Cloudflare in sync with all containers
