# Local Storage

"Local storage" can mean a couple differnet things.

## Truly *Local* storage, as in a physical disk or disks installed in the Saltbox server machine

In this setup, the absolute simplest thing would be to mount the root of your media storage, whether it's a single disk or a RAID array or whatever, at `/mnt/local/Media`

If this disk is faster than your boot disk, maybe you want to mount it at `/mnt/local/Media`, which would mean that all your downlaod activity will happen on it.  IF you are downloading from Usent and this disk is not solid state, you don't want to do that.  If your boot disk is a small HD and you're adding a giant NVME, then you probably _DO_ want to do that.

Then leave the rclone remote entry in the settings blank:

```ini
rclone:
  version: latest 
  remote: 
```

Saltbox will not do any of the remote mount setup.

Once everything is installed and configured, Sonarr/Radarr/etc will move your completed downloads to `/mnt/local/Media/WHATEVER`, which will be on that physical disk.

## *Local to your site* storage, as in a NAS or the like on your network

In this case, it's best to use the same rclone + cloudplow model that the standard cloud storage setup uses.

First, create an rclone remote pointing to your NAS using whatever connection scheme you wish; NFS, SMB, SFTP, etc.  Call it whatever you like.  `google` would be fine if you don't want to change any other settings.

If you give it a name other than `google`, change the rclone remote entry in the settings to match:

Then leave the rclone remote entry in the settings blank:

```ini
rclone:
  version: latest 
  remote: THE_NAME_OF_THE_REMOTE_YOU_JUST_CREATED
```

Then run the regular saltbox install.  Your NAS [or whatever] will be mounted at `/mnt/remote`, added to the unionfs, and Cloudplow will handle moving from your local disk to the NAS.
