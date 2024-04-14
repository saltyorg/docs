# Creating an rclone remote

This article describes generally how to create an rclone remote for a random cloud storage provider.

There are also specific instructions for [Dropbox](rclone-remote-dropbox.md) and [Google](rclone-remote.md).

## Prerequisites

To go through this process, you will need the following:

   1. Whatever access details are required by your cloud storage; typically this is an appID/secret pair, or a token of some kind.  Details can be found at the [rclone site](https://rclone.org/overview/), or you can just work through the config process and go get the things you are asked for.
   2. `rclone` installed on your saltbox machine [which means the preinstall has been run]
   3. `rclone` [same or higher version as on the saltbox machine] and a web browser installed on a machine local to you [this machine needs a GUI].  NOTE: this should be the same machine on which you are sshed to the saltbox server, as you will have to copy-paste a very long token a bit later.

## Walkthrough

1. Run the following command:

    ```shell
    rclone config
    ```

2. Type `n` for "New remote" and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    $ rclone config
    2022/02/26 15:29:40 NOTICE: Config file "/Users/geezer/.config/rclone/rclone.conf" not found - using defaults
    No remotes found - make a new one
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    ```

3. For "name", type in the name of your choice and and press <kbd class="platform-all">Enter</kbd>. [This name is arbitrary, aside from rclone's limitations on name; we're using `cloudstorage` in this example]

    ```shell
    n/s/q> n
    name> cloudstorage
    ```

4. For "Type of storage", find your preovider in the list, then enter the name or number and press <kbd class="platform-all">Enter</kbd>.  Note that this list is constantly changing, will be much longer, and the numbers won't match what's shown here.  **Read what's on the screen.**

    For this example, we'll use some S3-compatible storage.  S3 storage requires an Access Key and a Secret Key, which I have already retrieved from my provider's website.

    ```shell
    Option Storage.
    Type of storage to configure.
    Choose a number from below, or type in your own value.
    1 / 1Fichier
    \ (fichier)
    2 / Akamai NetStorage
    \ (netstorage)
    3 / Alias for an existing remote
    \ (alias)
    4 / Amazon Drive
    \ (amazon cloud drive)
    5 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, ArvanCloud, Ceph, China Mobile, Cloudflare, GCS, DigitalOcean, Dreamhost, Huawei OBS, IBM COS, IDrive e2, IONOS Cloud, Leviia, Liara, Lyve Cloud, Minio, Netease, Petabox, RackCorp, Scaleway, SeaweedFS, StackPath, Storj, Synology, Tencent COS, Qiniu and Wasabi
    \ (s3)
    ...
    52 / premiumize.me
    \ (premiumizeme)
    53 / seafile
    \ (seafile)
    Storage> s3
    ```

5. Follow the prompts

    Each storage type will then produce a different set of questions as you go through the setup process.  **Read what's on the screen and follow the prompts**

    Eventually, you will get to the advanced config:
    
    ```shell
    Edit advanced config?
    y) Yes
    n) No (default)
    y/n> n
    ```

    type `n` and press <kbd class="platform-all">Enter</kbd>.
    
    Depending on your cloud provider, you may be asked to complete a signin process at this point.  **Read what's on the screen and follow the prompts**

6. Eventually, `rclone` will tell you the process is complete, and show you the configuration:

    ```shell
    Configuration complete.
    Options:
    - type: s3
    - provider: Wasabi
    - access_key_id: QI9..............2JU
    - secret_access_key: vty..................................fxd
    - endpoint: s3.wasabisys.com
    - acl: private
    Keep this "cloudstorage" remote?
    y) Yes this is OK (default)
    e) Edit this remote
    d) Delete this remote
    y/e/d>
    ```

    Confirm that the remote details look OK, type `y` and press <kbd class="platform-all">Enter</kbd>.

16. To exit, type `q` and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Current remotes:

    Name                 Type
    ====                 ====
    cloudstorage         s3

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q
    ```

If you wish to encrypt this remote, proceed with [creating a crypt remote](rclone-remote-encrypted.md).  That page is written with dropbox in mind, but the concepts apply to any cloud storage provider.

If you are doing this as part of the initial install, you will need the name of the remote you created [`cloudstorage` in this example] to enter into the settings file.
