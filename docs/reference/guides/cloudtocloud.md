# Migrating from one cloud provider to another

This article discusses adding a new cloud provider into your setup.

A typical scenario is moving from Google to Dropbox.  However, this article will cover this in a generalized manner, since the concepts are universal.  Maybe you're transitioning from Google to Dropbox.  Maybe you're adding Box but keeping Dropbox.  Conceptually that part dioesn't matter.  You need to do basically the same things either way.

Throughout, I will refer to "Cloud A" and "Cloud B", where "A" is your current provider and "B" is the new one.

In the basic case, you need to:

1. create remote[s] for Cloud B
   [this might be just one, or base + encrypted, or base + encrypted + chunker, depending on what *you* want to do.]
2. create mount service for that last remote in the chain.
   [this mounts it in the file system]
3. add that mount point to the mergerfs
   [this makes the files appear in `/mnt/unionfs` where the apps are looking]

Steps 1-3 are covered [here](chazguides/teamdrive.md).

_Optionally_, if you want to upload to Cloud B:

1. point cloudplow at remote you created in step 1 above instead of the original.
   Cloudplow uplaods diretly to rcone remotes; it does nothing with the mounts you set up above.

There are Cloudplow config examples [here](../cloudplow/md).

_Optionally_, if you want to abandon Cloud A:

5. copy all or some of your data from Cloud A to Cloud B.
   YOu can do this all at once, or over time at your leisure, provided of course you keep Cloud A active.

## Scenarios

=== "Add Cloud B but keep uploading to Cloud A"

    1. create remote[s] for cloud storage
    2. create mount service for cloud storage
    3. add that mount point to the mergerfs

    Steps 1-3 are covered [here](chazguides/teamdrive.md).

=== "Add Cloud B and upload to it"

    1. create remote[s] for cloud storage
    2. create mount service for cloud storage
    3. add that mount point to the mergerfs

    Steps 1-3 are covered [here](chazguides/teamdrive.md).
    
    4. point cloudplow at remote from step 1 instead of the original.

    Basically, this involves changing the target remote in your cloudplow `config.json`.

    ASSUMING YOU HAVE A SINGLE REMOTE DEFINED:

    Your Cloudplow `config.json` will contain a couple lines like this:

    ```
        "sync_remote": "google:/Media",
        "upload_remote": "google:/Media"
    ```
    `google` is the name of the rclone remote that points to Cloud A.
    
    change that to: 
    ```
        "sync_remote": "cloud_b_remote:/Media",
        "upload_remote": "cloud_b_remote:/Media"
    ```
    where `cloud_b_remote` is the name of the rclone remote you created up in step 1.
    and restart Cloudplow.

    If you have multiple remotes defined in cloudplow, you probably want to remove all but one and make that one look like this.

    OPTIONAL:

    Change `google` to `cloud_b_remote` wherever else it appears in the file
    
    Aside from the two instances mentioned above, THAT NAME IS TOTALLY INTERNAL TO CLOUDPLOW.  YOU DO NOT NEED TO CHANGE IT.

    If you want, change these:
    ```
            "rclone_extras": {
                "--checkers": 16,
                "--drive-chunk-size": "64M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1
            },
    ```
    to flags that are optimized for Cloud B

    If you want, change this trigger:
    ```
            "rclone_sleeps": {
                "Failed to copy: googleapi: Error 403: User rate limit exceeded": {
                    "count": 5,
                    "sleep": 25,
                    "timeout": 3600
                }
            },
    ```
    to something that will tell Cloudplow to cool it on uploading to Cloud B, whatever those triggers might be [assuming that's needed].

    If you have multiple remotes defined or some other more complicated setup, you'll need to look into the cloudplow docs, but basically you will be replacing whatever remote or remotes you currntly have targeting Cloud A with one or more targeting Cloud B.

## Transferring data

This is just an `rclone copy` command, nothing special.
