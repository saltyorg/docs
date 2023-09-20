---
hide:
  - tags
tags:
  - mount
  - teamdrive
  - shared drive
  - rclone_vfs
  - mergerfs
  - unionfs
---

# How do I mount a cloud drive?

You have a cloud drive you want to add to your Saltbox server so Plex can see it.  In this article I’m assuming that’s ALL you want to do.

If you want to set up a Google Teamdrive and upload to it, see the [“Tip #44” document](tip44.md)

Here, I’m assuming you have access to a cloud drive, and you want to set it up so you can point Plex or Emby at it.  No more than that.

IMPORTANT NOTE: SALTBOX NOW HAS A MODULAR APPROACH TO MOUNTING THAT LETS YOU DEFINE THESE THINGS IN YOUR SETTINGS RATHER THAN DOING THEM MANUALLY.  IT IS RECOMMENDED THAT YOU USE THAT METHOD RATHER THAN THIS.

## Overview

There are three steps:

1. Create an rclone remote [this tells rclone about the teamdrive]
2. Create the rclone_vfs service files [this makes rclone mount the teamdrive at `/mnt/WHATEVER`]
3. Modify your mergerfs service file [this will include the contents of the new teamdrive in `/mnt/unionfs` for use in your apps]
   This step is actually optional, but it makes app configuration a little more straightforward since all your media files are in the same directory rather then some in `/mnt/unionfs` and some in `/mnt/bing-bang-boing`

## Not “Teamdrive” specific

The concepts here are not specific to teamdrives.  It’s described in terms of Teamdrives since this is aimed at Saltbox users who use Google Drive almost exclusively.  You can go through this exercise with any rclone backend that supports the relevant setup, of course modifying the rclone setup described to suit your OneDrive or Box or whatever other backend.

## Prerequisites

1. Access to a teamdrive
2. Either one of these for an account with access to the teamdrive
    1. ClientID/Secret
    2. Service Account JSON file[s]
       Put this/these in some fixed location like `/opt/sa`
3. Basic linux knowledge

    Like all of these docs and guides, we are assuming basic familiarity with Linux systems and concepts.  You are going to be copying files, editing files, etc.  This guide is not here to explain how to do those things.

Everything in this doc that appears in ALL_CAPS is a placeholder that needs to be replaced with something that applies to your situation.  For example, if I were to say “Enter YOUR_PASSWORD”, I don’t mean for you to enter “YOUR_PASSWORD”; I mean you should enter your password, whatever it is.  I think that should be obvious on its face, but here we are.

Let’s go!

1. Create the [rclone remote](../rclone-remote.md)

    After saving the remote and exiting rclone, and before you continue, verify that the remote is working correctly.

    Type `rclone lsd NAME_OF_THE_REMOTE_YOU_JUST_CREATED:/`

    ```text
     $ rclone lsd teamdrive-movies:/
           -1 2019-03-21 10:59:48     -1 Media
    ```

    It should show you the directories on the root level of the teamdrive you are adding.  Verify this with the Google Drive Web UI if necessary.  If the teamdrive is empty, create a folder and verify that rclone shows that folder.  Nothing after this will work if this connection is not set up correctly.

    If it doesn’t show you what you’re expecting, go back over the rclone remote setup.  Take your time.  Something isn’t right.  Perhaps you chose the wrong teamdrive.

    DO NOT PROCEED UNTIL YOU HAVE VERIFIED THAT THIS RCLONE COMMAND SHOWS YOU THE EXPECTED THING.

2. Get that remote mounted in the filesystem

    Now you have an rclone remote.  You can use this with rclone commands like `rclone copy` or `rclone move` or what have you.

    To use it with Plex/Emby/whatever other application, you need to create service files to “mount” the teamdrive in your filesystem.  Saltbox does this with your Google Drive at `/mnt/remote`.

    You’re going to create an analogous setup that does the same thing for that teamdrive remote you just created.

    First, you need to create the folder where you want the teamdrive contents to appear.  Generally, I recommend using the same name as the remote for clarity:

    1. Create a mount point for the teamdrive

        Create a directory where you want to mount this teamdrive under the /mnt directory: for example: `/mnt/NAME_OF_THE_REMOTE_YOU_JUST_CREATED`

        You may have to use sudo to create the directory:
        `sudo mkdir /mnt/NAME_OF_THE_REMOTE_YOU_JUST_CREATED`

        It should be on the root level of `/mnt`; not within any other remote mount directory.
        NOT, for example, `/mnt/remote/NAME_OF_THE_REMOTE_YOU_JUST_CREATED` OR `/mnt/unionfs/NAME_OF_THE_REMOTE_YOU_JUST_CREATED` OR `/mnt/local/NAME_OF_THE_REMOTE_YOU_JUST_CREATED` etc.

        Make sure it has the same ownership and permissions as the existing `/mnt/remote`:

        ```text
        ➜  ~ ls -al /mnt
        total 16
        drwxr-xr-x 1 root root 168 May  8 18:35 .
        drwxr-xr-x 1 root root 334 May 18 18:53 ..
        drwxrwxr-x 1 seed seed  48 May  8 19:08 local
        drwxrwxr-x 1 seed seed   0 May 20 23:16 remote
        drwxrwxr-x 1 seed seed  48 May  8 19:08 unionfs
        ```

        To do this:

        ```shell
        sudo chown -R seed:seed /mnt/NAME_OF_THE_REMOTE_YOU_JUST_CREATED
        sudo chmod -R g+w /mnt/NAME_OF_THE_REMOTE_YOU_JUST_CREATED
        ```

        Of course, `seed:seed` is YOUR USER AND GROUP if it differs from `seed:seed`

        You will use this mountpoint when you configure the rclone_vfs service.

    2. Create service files which will accomplish the mounting:

        Make copies of the rclone_vfs service file: `/etc/systemd/system/rclone_vfs.service`

        ```shell
        sudo cp /etc/systemd/system/rclone_vfs.service /etc/systemd/system/NAME_OF_THE_REMOTE_YOU_JUST_CREATED_vfs.service
        ```

        Edit /etc/systemd/system/NAME_OF_THE_REMOTE_YOU_JUST_CREATED_vfs.service:

        Change the port [5572] in two lines [lines 27 and 42 at this writing]:

        ```text
          --url=http://localhost:5572 \
          ...
          ExecStartPost=/usr/bin/rclone rc vfs/refresh recursive=true --url http://localhost:5572 _async=true
        ```

        The specific port you use doesn’t matter, but maybe just use 5573.

        ```text
          --url=http://localhost:5573 \
          ...
          ExecStartPost=/usr/bin/rclone rc vfs/refresh recursive=true --url http://localhost:5573 _async=true
        ```

        Change the remote name and mount directory in this line [line 41 at this writing]:

        ````text
          NAME_OF_THE_REMOTE_YOU_JUST_CREATED: /mnt/NAME_OF_THE_REMOTE_YOU_JUST_CREATED
        ````

        The first bit before the colon is the name of the rclone remote from step 1.
        The path is the mount point directory you created a moment ago.
        For example, you *might* end up with something like this:

        ```text
          teamdrive-movies: /mnt/teamdrive-movies
        ```

        What you will enter specifically depneds entirely on how *you* just configured the remote and moutn directory above.  This example is almost certainly *not* what you should enter.

        Change the next line to match the path you just entered:

        ```text
        ExecStop=/bin/fusermount -uz /mnt/remote
        ```

        For example:

        ```text
        ExecStop=/bin/fusermount -uz /mnt/NAME_OF_THE_REMOTE_YOU_JUST_CREATED
        ```

        Lastly enable and start that new service:
        Reload all the services

        ```shell
        sudo systemctl daemon-reload
        ```

        Start/restart the service

        ```shell
        sudo systemctl restart NAME_OF_THE_REMOTE_YOU_JUST_CREATED_vfs.service
        ```

        Enable the new service you created

        ```shell
        sudo systemctl enable NAME_OF_THE_REMOTE_YOU_JUST_CREATED_vfs.service
        ```

    Now, before you continue, verify that the mount is working correctly.

    Type `ls -haltr /mnt/NAME_OF_THE_REMOTE_YOU_JUST_CREATED`.  It should show you the same thing that you saw in the `rclone lsd`, and the same stuff you see in the Google Drive Web UI:

    ```text
    ➜  ~ ls -haltr /mnt/teamdrive-movies
    total 14M
    drwxrwxr-x 1 seed seed   0 Mar 21  2019  Media
    -rw-rw-r-- 1 seed seed   0 Dec  3 16:14  mounted-movies.bin
    ➜  ~
    ```

    As before,
    DO NOT PROCEED UNTIL YOU HAVE VERIFIED THAT THIS LS COMMAND SHOWS YOU THE EXPECTED THING.

3. Add that teamdrive to the mergerfs

    Last step; you’re going to add the teamdrive to the mergerfs configuration so that the files from it show up under /mnt/unionfs with the rest of your files.

    Add the following to the inventory file at `/srv/git/saltbox/inventories/host_vars/localhost.yml`:

    ```
    mergerfs_mount_branches: "{{ local_mount_branch }}=RW:/mnt/remote=NC:/mnt/YOUR_NEW_MOUNT=NC"
    ```
    then run the `mounts` tag:
    ```
    sb install mounts
    ```
    
    Now, verify that the mergerfs is working correctly.

    Type `ls -haltr /mnt/unionfs`.  The files from your teamdrive should now be included in the listing.  Depending on how busy the root of your drive[s] are, this listing may be pretty long, but look through it to verify that the files you expect as shown in the previous two steps are there [I’ve edited my listing for space]:

    ```text
    ➜  ~ ls -haltr /mnt/unionfs/
    total 1.4G
    ...
    -rwxrwxr-x  1 seed seed  0 Dec  3 16:14  mounted-movies.bin
    ...
    ➜  ~
    ```

    If they don’t show up, go back over the mergerfs config.

    Assuming they do, you’re done.  Now Plex and Emby and any other application that already sees /mnt/unionfs will be able to see those files.

    You may have to restart the server, or the containers, before they can see the newly-merged files.

## OMG I have so many teamdrives, this will take forever

There’s a set of scripts for that:

[https://github.com/maximuskowalski/smount](https://github.com/maximuskowalski/smount)

Those scripts will automate creating all the rclone entries [which you then copy and paste into your rclone config file], automate creating all the service files, and leave you with all the drives mounted, ready for the mergerfs step.  The develop branch ALSO generates the mergerfs config for you.

The other day, using those scripts, I had 21 teamdrives set up and mounted in a few minutes.

Personally, I think the wiki over there is very clear, but you will need to know some linux.

## OMG this is so complicated, isn’t there an easier way?

No.  I’m afraid there isn’t.

With the smount scripts, you need to rename a file or two [perhaps], make simple edits to maybe 2 files, run a script, copy and paste some output to another file, then run another script.

Honestly, if that’s too much this really isn’t for you.
