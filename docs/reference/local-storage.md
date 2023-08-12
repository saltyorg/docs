# Local Storage

You may want to set saltbox up to use "local storage".  This article is assuming you ware doing this as part of the initial setup, not switching from cloud to local.

"Local storage" can mean a couple different things.

## Truly *Local* storage, as in a physical disk or disks installed in the Saltbox server machine

In this setup, the absolute simplest thing would be to mount the root of your media storage, whether it's a single disk or a RAID array or whatever, at `/mnt/local/Media`

If this disk is faster than your boot disk, maybe you want to mount it at `/mnt/local`, which would mean that all your download activity will happen on it.  

If you are downloading from Usenet and this disk is not solid state, you don't want to do that.  If your boot disk is a small HD and you're adding a giant NVME, then you probably _DO_ want to do that.

Then leave the rclone remote entry in the settings blank:

```ini
rclone:
  version: latest 
  remote: 
```

Saltbox will not do any of the remote mount setup when you run the install.

Once everything is installed and configured, Sonarr/Radarr/etc will move your completed downloads to `/mnt/local/Media/WHATEVER`, which will be on that physical disk.

As you will recall from the earlier "How does Saltbox Work" lesson, this means everything shows up in the union at `/mnt/unionfs/` for application use.

## *Local to your site* storage, as in a NAS or the like on your network

In this case, it's best to use the same rclone + cloudplow model that the standard cloud storage setup uses.

First, create an rclone remote pointing to your NAS using whatever connection scheme you wish; SMB, SFTP, etc.  Call it whatever you like.  `google` would be fine if you don't want to change any other settings.

If you give it a name other than `google`, change the rclone remote entry in the settings to match:

```ini
rclone:
  version: latest 
  remote: THE_NAME_OF_THE_REMOTE_YOU_JUST_CREATED
```
It should go without saying that you need to change `THE_NAME_OF_THE_REMOTE_YOU_JUST_CREATED` to whatevcer you called the rclone remote you created pointing at the NAS.

Then run the regular saltbox install.  Your NAS [or whatever] will be mounted at `/mnt/remote`, added to the unionfs, and Cloudplow will handle moving from your local disk to the NAS.

You may want to examine the rclone_vfs service file at `/etc/systemd/system/rclone_vfs.service` to adjust the rclone flags to suit your connection scheme, since the defaults are intended for Google Drive.
