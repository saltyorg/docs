# I can’t see my media!
[in Plex, Emby, Radarr, Sonarr, etc]

Usually this is a simple problem, but there are several places where it could be.

There are several layers between your Google Drive and Plex [or other app].

  - rclone remote, which provides the link to your Google Drive.  This is where you sign into your Google account.
  - rclone_vfs service, which makes that rclone remote visible at `/mnt/remote`
  - mergerfs service which combines that mount point with a local “staging” directory at `/mnt/unionfs`.
  - mapping of the mergerfs into the various docker containers.

If any layer is having problems, Plex isn’t going to see your media.

For purposes of these notes, I’m assuming your setup is based on the current standard Saltbox configuration:

  - rclone remote is mounted via `rclone_vfs` [this used to be done by plexdrive]
  - /mnt/unionfs directory is created using `merger_fs` [used to be done by unionfs]

I’m further assuming that you are using the default file structure as suggested in the Saltbox wiki.

See the end of this doc for some notes on how to tell if 1 and 2 are true.

<span style="color: red;">MY FOLDERS AND FILES IN THESE SCREENSHOTS WILL NOT MATCH YOURS.  THAT’S FINE AND EXPECTED.</span>

When I refer to a shell command throughout, you’re typing the part highlighted in blue and looking for the part highlighted in orange.

In most cases, running the mounts tag will clear up any problems you may be having with the various auto-generated service files.


```
cd ~/cloudbox && sudo ansible-playbook cloudbox.yml --tags mounts
```

## A quick look

The df command can give you a quick look at things:

```
➜  ~ df -h
Filesystem   Size   Used  Avail  Use%  Mounted on
...
local:remote  6.1P  107T   224G  100%  /mnt/unionfs
google:       1.0P  107T   1.0P   10%  /mnt/remote
➜  ~
```

That shows a device called “google” [created by rclone config] mounted at `/mnt/remote` [done by rclone_vfs.service], and then two directories [local and remote, which are both inside the /mnt directory] combined into `/mnt/unionfs` [that’s done by mergerfs.service]

If this looks good, your problem is most likely in the bind mounts within the containers.

Now we’ll step through the various layers involved in this and check them one at a time.

## rclone remote
The rclone config command should show you the google remote you defined during setup:

```
➜  ~ rclone config
Current remotes:

Name             	Type
====             	====
google           	drive

e) Edit existing remote
...
e/n/d/r/c/s/q> q
```

You should be able to get a file listing from that remote:

```
➜  ~ rclone lsd google:/Media
      	-1 2018-12-01 20:16:06    	-1 Music
      	-1 2019-03-15 19:26:14    	-1 Movies
      	-1 2018-12-01 20:14:35    	-1 TV
➜  ~
```

That file listing should match what’s displayed on the Google Drive website.

Yours will probably contain “Movies” and “TV”.

If it doesn’t, step one is to fix that.  Recreate or edit that google: rclone remote until the file listings match.

Do not continue until those two file listings match.  They won’t match mine; they should both show the same files from YOUR gdrive.

Now that the rclone remote is known good, let’s move to the next layer, the rclone_vfs mount.

## rclone_vfs mount
First, let’s check that the service is running:

```
➜  ~ sudo systemctl status rclone_vfs.service
● rclone_vfs.service - Rclone VFS Mount
   Loaded: loaded (/etc/systemd/system/rclone_vfs.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2019-11-02 06:45:34 EET; 10h ago
  Process: 1053 ExecStartPre=/bin/sleep 10 (code=exited, status=0/SUCCESS)
 Main PID: 1247 (rclone)
	Tasks: 23 (limit: 4915)
   CGroup: /system.slice/rclone_vfs.service
       	└─1247 /usr/bin/rclone mount --config=/home/seed/.config/rclone/rclone.conf --user-agent . . .

Nov 02 06:45:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Starting Rclone VFS Mount...
Nov 02 06:45:34 Ubuntu-1804-bionic-64-minimal rclone[1247]: Serving remote control on http://127.0.0.1:5572/
Nov 02 06:45:34 Ubuntu-1804-bionic-64-minimal systemd[1]: Started Rclone VFS Mount.
```
You want to see “`active (running)`” there.

You can look at the log to find out what’s wrong if it’s not “`active (running)`”

```
➜  ~ sudo journalctl -fu rclone_vfs.service
-- Logs begin at Mon 2019-08-05 16:56:44 EEST. --
Nov 02 06:42:44 Ubuntu-1804-bionic-64-minimal rclone[9625]: Serving remote control on http://127.0.0.1:5572/
Nov 02 06:42:44 Ubuntu-1804-bionic-64-minimal systemd[1]: Started Rclone VFS Mount.
Nov 02 06:44:09 Ubuntu-1804-bionic-64-minimal systemd[1]: Stopping Rclone VFS Mount...
Nov 02 06:44:09 Ubuntu-1804-bionic-64-minimal rclone[9625]: Fatal error: failed to umount FUSE fs: exit status 1: fusermount: entry for /mnt/remote not found in /etc/mtab
Nov 02 06:44:09 Ubuntu-1804-bionic-64-minimal systemd[1]: rclone_vfs.service: Main process exited, code=exited, status=1/FAILURE
Nov 02 06:44:09 Ubuntu-1804-bionic-64-minimal systemd[1]: rclone_vfs.service: Failed with result 'exit-code'.
Nov 02 06:44:09 Ubuntu-1804-bionic-64-minimal systemd[1]: Stopped Rclone VFS Mount.
-- Reboot --
Nov 02 06:45:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Starting Rclone VFS Mount...
Nov 02 06:45:34 Ubuntu-1804-bionic-64-minimal rclone[1247]: Serving remote control on http://127.0.0.1:5572/
Nov 02 06:45:34 Ubuntu-1804-bionic-64-minimal systemd[1]: Started Rclone VFS Mount.
```


In that log you can see an error from last night when my server ran out of disk space, the rclone_vfs service died, then a reboot [after clearing space]  and it came back up.

If there are errors there, first try restarting the service:

```
sudo systemctl restart rclone_vfs
```

If that doesn’t get you to an “`active (running)`” state, try a reboot of the machine.

If that doesn’t work, the problem is deeper; maybe a config problem or a failed install?  Read the log.  Chances are the specific problem is called out [missing directory, perhaps].  You’re running a server.  Learn to read logs.  If all fails, take the log information to the Discord, but be prepared to describe what you’ve done and provide details.  Don’t come in with “Shit’s busted, my dudes!  What’s wrong?”

Now that the service is running, let’s make sure the files are showing up where they are supposed to be.

You can extract the location where the rclone_vfs service is mounting your google storage with a quick egrep command:

```
➜  ~ egrep -i -e "/mnt/" /etc/systemd/system/rclone_vfs.service
  google: /mnt/remote
ExecStop=/bin/fusermount -uz /mnt/remote
```

You can see in that output that rclone_vfs is mounting your google: remote at /mnt/remote.

That means that the content of your google drive should also appear at that location.  Let’s check that:

```
➜  ~ ls -al /mnt/remote/Media
total 0
drwxrwxr-x 1 seed seed 0 Dec  1  2018 Music
drwxrwxr-x 1 seed seed 0 Mar 15  2019 Movies
drwxrwxr-x 1 seed seed 0 Dec  1  2018 TV
➜  ~
```

Note that that matches the file listing from the Google Drive web UI above.

If it doesn’t, there’s a problem running the rclone_vfs.service.  Perhaps try running the mounts tag.

Do not continue until those two file listings match.  They won’t match mine; they should both show the same files from YOUR gdrive.

We’ve established that the rclone remote is good, and the rclone_vfs service is mounting it as a file system at the expected location.

The next step is the mergerfs mount where all the apps look for your files.

## Mergerfs service

Just like we did with the rclone_vfs service, check the mergerfs status:

```
➜  ~ sudo systemctl status mergerfs.service
● mergerfs.service - MergerFS Mount
   Loaded: loaded (/etc/systemd/system/mergerfs.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2019-11-02 06:45:24 EET; 11h ago
  Process: 1034 ExecStart=/usr/bin/mergerfs -o category.create=ff,minfreespace=0,allow_other -o dropcacheonclose=true,security_capability=false,xattr=nosys -o statfs_ignore=ro,use_ino,auto_
	Tasks: 9 (limit: 4915)
   CGroup: /system.slice/mergerfs.service
       	└─1074 /usr/bin/mergerfs -o category.create=ff,minfreespace=0,allow_other -o dropcacheonclose=true,security_capability=false,xattr=nosys -o statfs_ignore=ro,use_ino,auto_cache,um

Nov 02 06:45:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Starting MergerFS Mount...
Nov 02 06:45:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Started MergerFS Mount.
```

As before, if not “`active (running)`”, you can check the mergerfs log for some clue:

```
➜  ~ sudo journalctl -fu mergerfs.service
-- Logs begin at Mon 2019-08-05 16:56:44 EEST. --
Oct 13 17:00:11 Ubuntu-1804-bionic-64-minimal systemd[1]: Starting MergerFS Mount...
Oct 13 17:00:11 Ubuntu-1804-bionic-64-minimal systemd[1]: Started MergerFS Mount.
-- Reboot --
Nov 02 06:42:54 Ubuntu-1804-bionic-64-minimal systemd[1]: Stopping MergerFS Mount...
Nov 02 06:42:56 Ubuntu-1804-bionic-64-minimal systemd[1]: Stopped MergerFS Mount.
Nov 02 06:43:06 Ubuntu-1804-bionic-64-minimal systemd[1]: Starting MergerFS Mount...
Nov 02 06:43:06 Ubuntu-1804-bionic-64-minimal systemd[1]: Started MergerFS Mount.
Nov 02 06:44:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Stopping MergerFS Mount...
Nov 02 06:44:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Stopped MergerFS Mount.
-- Reboot --
Nov 02 06:45:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Starting MergerFS Mount...
Nov 02 06:45:24 Ubuntu-1804-bionic-64-minimal systemd[1]: Started MergerFS Mount.
```

If everything looks good, you can check the contents of the filesystem:

```
➜  ~ ls -al /mnt/unionfs/Media
total 0
drwxrwxr-x 1 seed seed   120 Sep 28 18:32 .
drwxrwxr-x 1 seed seed	  62 Sep 28 18:31 ..
drwxrwxr-x 1 seed seed   338 Oct 18 20:21 Music
drwxrwxr-x 1 seed seed    78 May  3  2019 Movies
drwxrwxr-x 1 seed seed 28196 Nov  2 01:42 TV
➜  ~
```

Again, this should match all the file listings you’ve looked at so far, at least.

There may be some extra folders here depending on a variety of things; other mounts that are included in the mergerfs and so forth.  Probably not, given my assumption that you are using the default configuration.

Do not continue until those two file listings match.  They won’t match mine; they should both show the same files from YOUR gdrive.

So at this point we know that all the layers on the host are working, so the last step is to check the views inside the containers.

## Docker volume maps

All the docker containers that need to access your media files have the relevant directories mapped inside them.  You can have a look at specifically how with the docker inspect command:


```
➜  ~ docker inspect plex | head -n 90
[
	{
    	"Id": "070d5fc16d4372156c39a6cf2923e6edb2e8576817cbcf9b6432f88f2237a2e8",
    	"Created": "2019-10-16T19:45:29.93111423Z",
    	"Path": "/init",
    	"Args": [],
    	"State": {
        	"Status": "running",
...
    	"HostConfig": {
        	"Binds": [
            	"/mnt/unionfs/Media:/data:rw",
            	"/tmp:/tmp:rw",
            	"/mnt/local/transcodes/plex:/transcode:rw",
            	"/opt/plex:/config:rw",
            	"/mnt:/mnt:rw",
            	"/opt/scripts:/scripts:rw",
            	"/dev/shm:/dev/shm:rw"
        	],
...
➜  ~
```

I’ve trimmed some stuff out there particularly on the top].  If the “Binds” section isn’t visible, try scrolling up, or increase the “90” to display more lines.  It should be right around the same place as mine, though.

Take a look at the “`Binds`” section.  Each entry there shows a path on the host [on the left] and the location where those files appear inside the container.

## Media-related defaults:


| Container/Application |  INSIDE CONTAINER  |  ON HOST                  |
|:----------------------|:------------------:|:-------------------------:|
| sonarr                |  `/tv`             | `/mnt/unionfs/Media/TV`     |
| radarr                | `/movies`            | `/mnt/unionfs/Media/Movies` |
| lidarr                | `/music`             | `/mnt/unionfs/Media/Music` |
| plex                  | `/data`              | `/mnt/unionfs/Media`       |  



For example, that plex line shows that `/mnt/unionfs/Media` appears inside the container at `/data`.  Let’s check that:

```
➜  ~ docker exec plex ls -al /data
total 4
drwxrwxr-x 1 plex plex   120 Sep 28 18:32 .
drwxr-xr-x 1 root root  4096 Oct 16 22:45 ..
drwxrwxr-x 1 plex plex   338 Oct 18 20:21 Music
drwxrwxr-x 1 plex plex    78 May  3  2019 Movies
drwxrwxr-x 1 plex plex 28196 Nov  2 01:42 TV
```

Again, all the same files as always.

If that doesn’t show your files as expected, chances are something happened to the mounts while the container was running and the map has broken.  First restart the container and if that doesn’t work restart the server.


```
➜  ~ docker restart plex
plex
➜  ~
```

Then try the “`docker exec plex ls -al /data`” command again.

You may notice above that the /mnt directory is passed through to the container, as well.  This means that, inside the container, 
	`/data` and `/mnt/unionfs/Media`
point to the very same location, so these two directory listings should look the same:


```
➜  ~ docker exec plex ls -al /data
...
drwxrwxr-x 1 plex plex   338 Oct 18 20:21 Music
drwxrwxr-x 1 plex plex    78 May  3  2019 Movies
drwxrwxr-x 1 plex plex 28196 Nov  2 01:42 TV
```
```
➜  ~ docker exec plex ls -al /mnt/unionfs/Media
total 4
...
drwxrwxr-x 1 plex plex   338 Oct 18 20:21 Music
drwxrwxr-x 1 plex plex    78 May  3  2019 Movies
drwxrwxr-x 1 plex plex 28196 Nov  2 01:42 TV
```

On my own servers, I typically don’t use the “`/data`” style mounts.  Since the `/mnt` directory is mapped into all the containers that use it, I point Radarr, Sonarr, Plex, etc.  all at `/mnt/unionfs/Media/BLAH` directly.  I do this so that I never have to translate any paths in things like Plex AutoScan.  A given movie file is at `/mnt/unionfs/Media/Movies/Whatever (2019)` no matter the context.

Some common problems are:

`/mnt/unionfs` not empty when the mergerfs service starts.

The log in that case will look something like this:

```
ubuntu systemd[1]: Starting MergerFS Mount...
Ubuntu mergerfs[10803]: fuse: mountpoint is not empty
ubuntu mergerfs[10803]: fuse: if you are sure this is safe, use the 'nonempty' mount option
ubuntu systemd[1]: mergerfs.service: Control process exited, code=exited status=1
ubuntu systemd[1]: mergerfs.service: Failed with result 'exit-code'.
ubuntu systemd[1]: Failed to start MergerFS Mount.
```

If you see this, rerunning the mounts tag, with or without rebuild, actually checks for non empty paths left there as part of a previous failure, and moves the folder to `/mnt/unionfs_<date>` before mounting again.

```
cd ~/cloudbox && sudo ansible-playbook cloudbox.yml --tags mounts
```

If this is the result of something writing into that directory while the mergerfs service was down, the mounts tag won’t address it.  You’ll have to clean out `/mnt/unionfs` yourself first.

## HOW DO I KNOW IF I AM USING RCLONE_VFS AND MERGERFS?

There are a few things you can look at:

If you installed recently, rclone_vfs and mergerfs have become the default, so you’re probably using them.  If you installed over a year ago, you’re probably using plexdrive/unionfs.

In the following examples, you’re typing the part in blue and looking for the part highlighted in orange.

Look at the settings file:

```
➜  cloudbox git:(master) head adv_settings.yml
---
System:
  timezone: auto
Mounts:
  unionfs: mergerfs     <<<< RIGHT
  remote: rclone_vfs    <<<< HERE
Plex:
  open_port: no
  force_auto_adjust_quality: no
  force_high_output_bitrates: no
➜  cloudbox git:(master)
```

Check the status of the services
```
➜  cloudbox git:(master) service rclone_vfs status
● rclone_vfs.service - Rclone VFS Mount
   Loaded: loaded (/etc/systemd/system/rclone_vfs.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2019-06-16 22:41:58 EEST; 1 day 18h ago
…

➜  cloudbox git:(master) service mergerfs status
● mergerfs.service - MergerFS Mount
   Loaded: loaded (/etc/systemd/system/mergerfs.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2019-06-16 22:41:48 EEST; 1 day 18h ago
…
```

If you’re not using either rclone_vfs or mergerfs you’ll see errors there instead.


Check the filesystem behind the mounts:

```
➜  cloudbox git:(master) sudo mount | egrep "remote"
local:remote on /mnt/unionfs type fuse.mergerfs …  <<<< Mergerfs
google: on /mnt/remote type fuse.rclone …          <<<< RClone
➜  cloudbox git:(master)
```

