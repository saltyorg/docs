---
extra_stylesheets:
  - stylesheets/roles_index.css
hide:
  - tags
tags:
  - module
  - role
---

# Modules Index

## Backup

|                                            |                                    :material-airplane-takeoff:{.xl}                                     |
|--------------------------------------------|:-------------------------------------------------------------------------------------------------------:|
| [Backup](../../saltbox/backup/backup.md)   | `backup` `restore-service` `saltbox-restore-service` `set-backup` `unset-backup` `wipe-restore-service` |
| [Backup2](../../saltbox/backup/backup2.md) |          `backup2` `restore-service2` `saltbox-restore-service2` `set-backup2` `unset-backup2`          |
| [Restore](../../saltbox/backup/restore.md) |                                    `restore` `opt-permissions-reset`                                    |

## Custom Deployment

|                                                   |                                  |
|---------------------------------------------------|:--------------------------------:|
| [Custom](custom.md)                               |             `custom`             |
| [Mount Templates](mount_templates.md)             |        `mount-templates`         |
| [Traefik File Template](traefik_file_template.md) | `generate-traefik-file-template` |
| [Traefik Template](traefik_template.md)           |   `generate-traefik-template`    |
| [Saltbox Mod](saltbox_mod.md)                     |          `saltbox-mod`           |

## Host Configuration

|                     |                                      |
|---------------------|:------------------------------------:|
| [Common](common.md) |               `common`               |
| [Kernel](kernel.md) |               `kernel`               |
| [MOTD](motd.md)     |    `motd` `motd-generate-config`     |
| [System](system.md) | `system` `set-locale` `set-timezone` |
| [Shell](shell.md)   |               `shell`                |
| [User](user.md)     |                `user`                |

## Filesystem

|                               |                                                                                                             |
|-------------------------------|:-----------------------------------------------------------------------------------------------------------:|
| [Hetzner NFS](hetzner_nfs.md) | `hetzner-nfs-server` `hetzner-nfs-server-uninstall` `hetzner-nfs-client-mount` `hetzner-nfs-client-unmount` |
| [Permissions](permissions.md) |                                              `fix-permissions`                                              |
| [Remote](remote.md)           |                                                  `mounts`                                                   |
| [UnionFS](unionfs.md)         |                                                  `mounts`                                                   |

## Misc

|                                         |                                             |
|-----------------------------------------|:-------------------------------------------:|
| [Diag](diag.md)                         |                   `diag`                    |
| [Hetzner VLAN](hetzner_vlan.md)         | `hetzner-vlan-deploy` `hetzner-vlan-remove` | 
| [Plex Auth Token](plex_auth_token.md)   |              `plex-auth-token`              |
| [Plex Fix Futures](plex_fix_futures.md) |             `plex-fix-futures`              | 
| [Reboot](reboot.md)                     |                  `system`                   |
| [Sandbox](sandbox.md)                   |                  `sandbox`                  |