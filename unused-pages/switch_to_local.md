# Switching to Local Storage

This article discusses what to do if you have media on Google or Dropbox or something and you want to convert to using all local storage.

Conceptually, this is simple.

1. Set up your local storage

   Maybe this is a NAS, or a bunch of disks in the Saltbox machine, or something else.  Step one is going to be setting this up.

2. Copy your media from the cloud to that local storage

   This is probably going to be an rclone copy and will mostly be waiting.

3. Point your Saltbox server at that local storage.

   This would include things like:
  
   - adding the local storage to the mergerfs
   - modifying cloudplow to send new stuff there

4. Cancel the cloud storage

The specifics depend on the timetable and how you want to go about it.

## I want to cut the cord and switch to local all in one fell swoop:

### Set up your local storage

Describing how to do this is out of scope for these docs.  There are many options here and only you can decide which fit your needs and budget.

One thing's for sure; you're buying a lot of disks.

### Copy your media from the cloud to that local storage

First, halt all downloading on your Saltbox machine; you don't need anything getting changed or added while you go through this exercise.

Depoending on you personal situation, you may or may not want to copy everything down from your cloud storage.  If you do, though, this is going to be some variation on:

```
rclone copy CLOUD_STORAGE_REMOTE:/PATH LOCATION_OF_LOCAL_STORAGE:/PATH
```

Probably with some rclone flags to improve performance for your specific cloud storage provider.

For example, if you have a standard Saltbox setup, and you have mounted your local storage at `/mnt/nas`, maybe something like:

```
rclone copy google:/Media /mnt/nas/Media --drive-chunk-size 128M --transfers 8 --checkers 8 --tpslimit 8 --fast-list --checksum --progress
```

### Point your Saltbox server at that local storage.

Since in this case you just copied everything down, `/mnt/nas/Media` is now a mirror of `/mnt/remote/Media`

The simplest thing here is to use the same rclone + cloudbox setup as Saltbox does normally.

Stop all your docker containers.

Unmount `/mnt/nas` and remove the entry in fstab

Enter `rclone config`

Rename your `google` remote to `google-original`

Create a new remote named `google` that points to your local storage

   - adding the local storage to the mergerfs
   - modifying cloudplow to send new stuff there

### Cancel the cloud storage
