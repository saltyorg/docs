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

Saltbox uses a modular approach to rclone mounts.

## Overview

There are three steps:

1. Create an rclone remote [this tells rclone about the teamdrive]
2. Add details of the remote to your `settings.yml`
3. Run the `mounts` tag [or another tag that also runs it, like `saltbox`]

## Prerequisites

1. Access to the storage including whatever credentials are required.
2. Basic linux knowledge

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

    It should show you the directories on the root level of the teamdrive you are adding.  Verify this with the storage system's web UI or other non-rclone tool if necessary.  If the drive is empty, create a folder and verify that rclone shows that folder.  Nothing after this will work if this connection is not set up correctly.

    If it doesn’t show you what you’re expecting, go back over the rclone remote setup.  Take your time.  Something isn’t right.  Perhaps you chose the wrong teamdrive, or entered the wrong credentials.

    DO NOT PROCEED UNTIL YOU HAVE VERIFIED THAT THIS RCLONE COMMAND SHOWS YOU THE EXPECTED THING.

2. Enter details about that remote in `settings.yml`.

   Under `remotes` copy and paste [one of] the existing remotes you find there and edit it to suit this new remote.  Notably, change `NAME_OF_THE_REMOTE_YOU_JUST_CREATED` to the name of the remote you just created and `MOUNT_TEMPLATE` to either a valid saltbox-provided template [`google`, `dropbox`, `sftp`], a path to a Jinja template mount service [`/mnt/templates/box.j2`], or a path to a full rclone_vfs mount service file [`/mnt/templates/my_custom_ceph_mount.service`].  The two latter options are not provided by saltbox, theses are files you create.

   If you are mounting a folder instead of the root of the cloud storage, specify that in the `remote` value: `remote: NAME_OF_THE_REMOTE_YOU_JUST_CREATED:/bing` or `remote: "NAME_OF_THE_REMOTE_YOU_JUST_CREATED:/Bang Boing"`.  Generally, we recommend avoiding spaces in the name of a directory you are planning to mount.

   Edit the other settings [`upload` and so forth] to suit your requirements.

   Details on the meanings of these fields can be found [here](../../accounts/#options-in-settingsyml)
   
    ```yaml
    rclone:
      enabled: true
      remotes:
        - remote: NAME_OF_THE_REMOTE_YOU_JUST_CREATED
          template: MOUNT_TEMPLATE
          upload: false # true to configure cloudplow upload for this remote
          upload_from: /mnt/local/Media
          vfs_cache:
            enabled: false
            max_age: 504h
            size: 50G
      version: latest
    ```

  Save the file.

3. Run the `mounts` tag.

    ```
    sb install mounts
    ```
    
    This will create rclone vfs mount services for all the remotes defined in your settings, and add them all to the unionfs.

    Now, verify that the mergerfs is working correctly.

    Type `ls -haltr /mnt/unionfs`.  The files from all the remotes defined in the `settings.yml` should now be included in the listing.  Depending on how busy the root of your drive[s] are, this listing may be pretty long, but look through it to verify that the files you expect as shown in the previous two steps are there [I’ve edited my listing for space]:

    ```text
    ➜  ~ ls -haltr /mnt/unionfs/
    total 1.4G
    ...
    -rwxrwxr-x  1 seed seed  0 Dec  3 16:14  mounted-movies.bin
    ...
    ➜  ~
    ```

    If they don’t show up, go back over the process; something is missing.

    Restart the relevant containers so they update their internal mounts and thereby see the newly-merged files.
