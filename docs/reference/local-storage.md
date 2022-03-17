# Local Storage

Saltbox can be configured to forego the cloud storage requirements discussed [here](cloud.md).

This article will discuss the simplest case.  There are of course a bunch of ways you could possibly do this that you may want to choose based on performance or whatever other requirements you may have, but this is the Simplest Thing That Could Possibly Work.

I'm assuming you are using some local NAS for storage and running saltbox on a different machine.

First, mount your NAS storage at `/mnt/local/Media`.  Make sure that the user running the saltbox containers has full access to read and write.

Then leave the rclone remote entry in the settings blank:

```
rclone:
  version: latest 
  remote: 
```

Saltbox will not do any of the remote mount setup.

Once everything is installed and configured, Sonarr/Radarr/etc will move your completed downloads to `/mnt/local/Media/WHATEVER`, which will be on the NAS.

You'll probably need to come up with a strategy for managing seeding torrents; perhaps you want to move those to the NAS as well.
