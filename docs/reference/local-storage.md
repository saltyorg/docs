# Local Storage

You may want to set saltbox up to use "local storage".  This article is assuming you are doing this as part of the initial setup, not switching from cloud to local.

!!! info
    This article is also assuming that you are using an all-in-one `saltbox` in your home, not something like multiple hetzner boxes pointed at a hetzner storage server.  That's not "local storage" for the purposes of this article.  As one specific example, the [Hetzner NFS stuff](../apps/hetzner_nfs.md) instructions are incompatible with the suggestions made here.

"Local storage" can mean a couple different things.

## Truly *Local* storage, as in a physical disk or disks installed in the Saltbox server machine

In this setup, the absolute simplest thing would be to mount the root of your media storage, whether it's a single disk or a RAID array or whatever, at `/mnt/local/Media`

If this disk is faster than your boot disk, maybe you want to mount it at `/mnt/local`, which would mean that all your download activity will happen on it.  

If you are downloading from Usenet and this disk is not solid state, you don't want to do that.  If your boot disk is a small HD and you're adding a giant NVME, then you probably _DO_ want to do that.

Then disable rclone in `settings.yml`:

```ini
rclone:
  enabled: false
  remotes:
...
```

Saltbox will not do any of the remote mount setup when you run the install.

Once everything is installed and configured, Sonarr/Radarr/etc will move your completed downloads to `/mnt/local/Media/WHATEVER`, which will be on that physical disk.

As you will recall from the earlier "How does Saltbox Work" lesson, this means everything shows up in the union at `/mnt/unionfs/` for application use.

## *Local to your site* storage, as in a NAS or the like on your network

In this case, it's best to use the same rclone + cloudplow model that the standard cloud storage setup uses.

First, create an rclone remote pointing to your NAS using whatever connection scheme you wish; SMB, SFTP, etc.  Call it whatever you like.  

Then fill out the remote details in `settings.yml`
```ini
rclone:
  enabled: true
  remotes:
    - remote: THE_NAME_OF_THE_REMOTE_YOU_JUST_CREATED
      template: sftp # whatever template or service file is appropriate
      upload: true
      upload_from: /mnt/local/Media
      vfs_cache:
        enabled: false
        max_age: 504h
        size: 50G
  version: latest
```
It should go without saying that you need to change `THE_NAME_OF_THE_REMOTE_YOU_JUST_CREATED` to whatevcer you called the rclone remote you created pointing at the NAS.

Then run the regular saltbox install.  Your NAS [or whatever] will be mounted at `/mnt/remote/THE_NAME_OF_THE_REMOTE_YOU_JUST_CREATED`, added to the unionfs, and Cloudplow will handle moving from your local disk to the NAS.
