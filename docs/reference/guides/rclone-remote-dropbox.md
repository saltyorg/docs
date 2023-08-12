# Creating an rclone remote for Dropbox

This article describes how to create an rclone remote for Dropbox

## NOTE: THIS ARTICLE IS A WORK IN PROGRESS; IT MAY NOT BE COMPLETE AND IS NOT INTENDED AS A COMPREHENSIVE GUIDE

## Prerequisites

To go through this process, you will need the following:

   1. App Key/App Secret from two applications you create at Dropbox. The process is described [here](https://rclone.org/dropbox/#get-your-own-dropbox-app-id).  Two are suggested here because you **may** want separate apps for mount and upload, and you may as well create both while you're there.  Using two is not required.
   2. rclone installed on your saltbox machine [which means the preinstall has been run]
   3. rclone [same or higher version as on the saltbox machine] and a web browser installed on a machine local to you [this machine needs a GUI].  NOTE: this should be the same machine on which you are sshed to the saltbox server, as you will have to copy-paste a very long token a bit later.

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

3. For "name", type in the name of your choice and and press <kbd class="platform-all">Enter</kbd>. [This name is arbitrary, aside from rclone's limitations on name; we're using `dropbox` in this example]

    ```shell
    n/s/q> n
    name> dropbox
    ```

4. For "Type of storage", type in `dropbox`, or the corresponding number, and press <kbd class="platform-all">Enter</kbd>.  Note that this list is constantly changing, will be much longer, and the numbers won't match what's shown here.  **Read what's on the screen.**

    ```shell
    Option Storage.
    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value.
    1 / 1Fichier
      \ "fichier"
    2 / Alias for an existing remote
      \ "alias"
     ...
    12 / Compress a remote
       \ (compress)
    13 / Dropbox
       \ (dropbox)
    14 / Encrypt/Decrypt a remote
       \ (crypt)
     ...
    48 / Zoho
       \ (zoho)
    49 / premiumize.me
       \ (premiumizeme)
    50 / seafile
       \ (seafile)
    Storage> dropbox
    ```

5. App Key and App Secret:

    Enter the App Key and App Secret from one of your applications when prompted.

    ```shell
    Storage> dropbox
    Option client_id.
    OAuth Client Id.
    Leave blank normally.
    Enter a value. Press Enter to leave empty.
    client_id> JOHNNYJOEYDEEDEE
    Option client_secret.
    OAuth Client Secret.
    Leave blank normally.
    Enter a value. Press Enter to leave empty.
    client_secret> OZZYTONYGEEZERBILL
    ```

6. For "Edit advanced config", type `n` and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Edit advanced config?
    y) Yes
    n) No (default)
    y/n> n
    ```

7. For "Use auto config?", type `n` for "...remote or headless machine" and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine

    y) Yes (default)
    n) No
    y/n> n
    ```

8. In the next section, follow the instructions on your local machine.

    ```shell
    Option config_token.
    For this to work, you will need rclone available on a machine that has
    a web browser available.
    For more help and alternate methods see: https://rclone.org/remote_setup/
    Execute the following on the machine with the web browser (same rclone
    version recommended):
     rclone authorize "dropbox" "eyJjbGllbnRfaWQiOiI2OTUx...cGUiOiJkcml2ZSJ9"
    Then paste the result.
    Enter a value.
    config_token>
    ```

9. If asked to login, use the Dropbox account you want to store your data in.

10. Give access by clicking through these two dialogs.

    ![](../../images/rclone-remote/dropbox-verification.png)

    ![](../../images/rclone-remote/dropbox-permission.png)

11. The browser should report success.

    ![](../../images/rclone-remote/dropbox-success.png)

12. And a token should show up in the terminal on your local computer:

    ```text
    2023/05/19 16:59:57 NOTICE: Waiting for code...
    2023/05/19 18:07:33 NOTICE: Got code
    Paste the following into your remote machine --->
    ROGERPETEJOHNKEITH
    <---End paste
    ```

13. Copy this token and paste it at the rclone prompt in the saltbox session and press Enter.

    ```text
    Enter a value.
    config_token>  ROGERPETEJOHNKEITH
    ```

14. Confirm that the remote details look OK, type `y` and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Configuration complete.
    Options:
    - type: dropbox
    - client_id: JOHNNYJOEYDEEDEE
    - client_secret: OZZYTONYGEEZERBILL
    - token: {"access_token":"sl.Beujz-1fB...PTCTBbPOGhTs","token_type":"bearer","refresh_token":"Fu9...EYpRr","expiry":"2023-05-19T22:07:34.356998-05:00"}
    Keep this "dropbox" remote?
    y) Yes this is OK (default)
    e) Edit this remote
    d) Delete this remote
    y/e/d> y
    ```

15. repeat steps 2-14 with your second App ID/App Secret, if you have one, which again is a totally optional thing that you may not want to do.  Give this one an appropriate name like `dropbox-upload`.  Letters are free, don't be stingy with them.

16. To exit, type `q` and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Current remotes:

    Name                 Type
    ====                 ====
    dropbox              dropbox
    dropbox-upload       dropbox

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q
    ```

If you wish to encrypt this remote, proceed with [creating a crypt remote](rclone-remote-encrypted.md).

## Dropbox Performance Guide

https://developers.dropbox.com/dbx-performance-guide

## Install considerations:

## NOTE: THIS ARTICLE IS A WORK IN PROGRESS; IT MAY NOT BE COMPLETE AND IS NOT INTENDED AS A COMPREHENSIVE GUIDE

### rclone remote in settings:

You will want to change the [rclone remote name in the settings](https://docs.saltbox.dev/reference/accounts/#__tabbed_2_3) to match the rclone remote you created here.  Use the encrypted remote if you created one:

```yaml
rclone:
  version: latest
  remote: dropbox
```
OR
```yaml
rclone:
  version: latest
  remote: dropbox-crypt
```

## NOTE: THIS ARTICLE IS A WORK IN PROGRESS; IT MAY NOT BE COMPLETE AND IS NOT INTENDED AS A COMPREHENSIVE GUIDE

### rclone vfs service

The default `rclone_vfs.service` [found at `/etc/systemd/system/rclone_vfs.service`] is intended and tuned for Google Drive; after the install completes you may want to update it to match this sample.

If you do a standard install with the settings as expected, this is not absolutely necessary, as the Google-specific stuff will just be ignored, but there may be some differences to adopt.

Changes to make:

1. Replace `YOUR_USER_NAME_GOES_HERE` with the user name you enterd in the settings [default is `seed`]
2. Replace `YOUR_REMOTE_NAME_GOES_HERE` with the rclone remote you created here.  Use the encrypted remote if you created one.

This example assumes your system is using ONLY DROPBOX.  If you are adding this mount to a system that already has Google Drive set up, change `/mnt/remote` to something else.

```
[Unit]
Description=Rclone VFS Mount
After=network-online.target

[Service]
User=YOUR_USER_NAME_GOES_HERE
Group=YOUR_USER_NAME_GOES_HERE
Type=notify
ExecStartPre=/bin/sleep 10
ExecStart=/usr/bin/rclone mount \
  --user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' \
  --config=/home/YOUR_USER_NAME_GOES_HERE/.config/rclone/rclone.conf \
  --allow-other \
  --async-read=true \
  --dir-cache-time=5000h \
  --buffer-size=32M \
  --poll-interval=15s \
  --rc \
  --rc-no-auth \
  --rc-addr=localhost:5729 \
  --use-mmap \
  --vfs-read-ahead=128M \
  --vfs-read-chunk-size=32M \
  --vfs-read-chunk-size-limit=2G \
  --vfs-cache-max-age=504h \
  --vfs-cache-mode=full \
  --vfs-cache-poll-interval=30s \
  --vfs-cache-max-size=50G \
  --disable-http2 \
  --tpslimit 12 \
  --tpslimit-burst 0 \
  --umask=002 \
  --syslog \
  -v \
  YOUR_REMOTE_NAME_GOES_HERE: /mnt/remote
ExecStartPost=/usr/bin/rclone rc vfs/refresh recursive=true --url http://localhost:5729 _async=true
ExecStop=/bin/fusermount -uz /mnt/remote
Restart=on-abort
RestartSec=5
StartLimitInterval=60s
StartLimitBurst=3

[Install]
WantedBy=default.target
```

Note that you may want to edit this value:
```
  --vfs-cache-max-size=50G \
```
This cache will be placed in your home directory by default, so make sure it is set to a value that wil not fill your disk.

## NOTE: THIS ARTICLE IS A WORK IN PROGRESS; IT MAY NOT BE COMPLETE AND IS NOT INTENDED AS A COMPREHENSIVE GUIDE

### cloudplow config

The default cloudplow config [found at `/opt/cloudplow/config.json`] contains "rclone_extras" targeted at Google Drive.  After install you can remove the Google-specific flags if you wish.

There's no compelling reason to remove them, since they will be ignored by rclone; they're listed here for completeness sake.

These two lines can be **removed** from any `rclone_extras` on a dropbox-targeting `remote`:
```
    "--drive-chunk-size": "128M",
    "--drive-stop-on-upload-limit": null,
```
And this line **added**:
```
    "--dropbox-chunk-size": "150M",
```

The cloudplow config has a set of "rclone_sleeps", which are the triggers cloudplow watches for to decide when to switch service accounts or halt uploading.  One of these is meaningless for dropbox, so you can remove it if you wish.

Before:
```
"rclone_sleeps": {
    " 0/s,": {
        "count": 16,
        "sleep": 25,
        "timeout": 62
    },
    "Failed to copy: googleapi: Error 403: User rate limit exceeded": {
        "count": 10,
        "sleep": 25,
        "timeout": 7200
    }
},
```
After:
```
"rclone_sleeps": {
    " 0/s,": {
        "count": 16,
        "sleep": 25,
        "timeout": 62
    }
},
```


LEX NOTES ABOUT ENCRYPTION AND PATHING TO INCORPORATE SOMEWHERE:

```
HOW THE FREAKING FRACK DO TEAM FOLDERS VS PERSONAL FOLDERS ON DROPBOX WORK WITH RCLONE REMOTES?
WITH ENCRYPTION? WTF?

# Start with two rclone remotes. One of type = dropbox and one type = crypt pointing at the dropbox remote.

` ``
rclone config show dbox

[dbox]
type = dropbox
token = {token}
client_id = <App1_ID>
client_secret = <App1_Secret>

rclone config show dbox-crypt

[dbox-cryptx]
type = crypt
password = *** ENCRYPTED ***
remote = dbox:
directory_name_encryption = TRUE
filename_encoding = base32768
` ``

# The account name is "88"
# The dropbox personal folder for user 88 has 0 folders and 2 files, one encrypted the other not
# The dropbox shared folders ( in / ) have many folders and files

Running lsd on dbox is empty as expected as there are no folders and 2 files in the personal area.
` ``
➜  rclone lsd dbox:
` ``

# Running lsd on dbox:/ shows both personal files under "88" and encrypted shared files in "☍觐觐駔觐觐駔" (fake)
# Note: dbox:/88 is equivalent to dbox: and contains personal files which are not visible by any team
` ``
➜  rclone lsd dbox:/
          -1 2023-05-23 14:22:17        -1 88
          -1 2023-05-23 14:22:17        -1 ☍觐觐駔觐觐駔
` ``

# rclone lsd on dbox-crypt: ( no slash / ) are both empty as expected
` ``
➜  rclone lsd dbox-crypt:
` ``

# rclone lsd on dbox-crypt:/  ( with slash / ) decrypts ☍觐觐駔觐觐駔 correctly as "media"
` ``
➜  rclone lsd dbox-crypt:/
          -1 2023-05-23 14:16:27        -1 media
` ``

# rclone ls on dbox: and on dbox:/88 are identical as expected
` ``
➜  rclone ls dbox:
          88.bin
          衟衟衟衟衟

➜  rclone ls dbox:/88
          88.bin
          衟衟衟衟衟
` ``

# rclone ls on dbox-crypt: decrypts 衟衟衟衟衟 correctly as 88.bin
` ``
➜  rclone ls dbox-crypt:
          88.bin
` ``

# rclone ls on dbox-crypt:/ will show all encrypted files in the shared folders, in their unencrypted form
` ``
➜  rclone ls dbox-crypt:/
          media/files1/a.txt
          media/files1/b.txt
          media/files2/c.txt
          ...
          media/files8/s.txt
` ``
```
