## Dependencies
``` shell
curl -sL https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox
```
## Configuration

Make sure you fill out the following configuration files before proceeding. Each file will be located in /srv/git/saltbox

accounts.yml

``` { .yaml .annotate }
---
user:
  name: seed # (1)
  pass: password123 # (2)
  domain: testsaltbox.ml # (3)
  email: your@email.com # (4)
cloudflare:
  email: # (5)
  api: # (6)
plex:
  user: # (7)
  pass: # (8)
apprise: # (9)
```

1. Username that will be created (if it doesn't exist) during the installation and apps that have automatic user configuration.

    Required.

2. Password used for username account during the installation and apps that have automatic user configuration.

    Required.

3. Domain that you want to use for the server.

    Required.

4. Email address used for Let's Encrypt SSL certificates.

    Required.

5. Email used for the Cloudflare account.

6. Cloudflare API Token. (insert link to cloudflare guide when created)

7. Plex.tv username or email address on the account.

8. Plex.tv password for the account.

9. apprise url. See <https://github.com/caronc/apprise#popular-notification-services> for more information.


settings.yml

``` { .yaml .annotate }
---
downloads:
  nzbs: /mnt/local/downloads/nzbs # (1)
  torrents: /mnt/local/downloads/torrents # (2)
transcodes: /mnt/local/transcodes # (3)
rclone:
  version: latest # (4)
  remote: google # (5)
shell: bash # (6)
```

1. Folder used for usenet downloads.

2. Folder used for torrent downloads.

3. Folder used for temporary transcode files.

4. Rclone version that Saltbox will install. Valid options are latest, beta or a specific version (1.55).

5. Rclone remote that Saltbox will mount by default and use in any automated configuration.

6. Shell used by the system. Valid options are bash or zsh.

## Preinstall

!!! warning
    Make sure that you have setup the configuration correctly before proceeding.

This step will create the specified user account if needed and add it to sudoers, update the kernel, edit GRUB configuration if needed and install Rclone.

``` shell
sb install preinstall
```

At this point you'll want to make sure you run commands as the user specified in the accounts.yml

You can either run 'su username' to switch user or reconnect to SSH as the newly created user. Everything after this point will assume you are running as the user entered in accounts.yml

## Rclone
This step will take you through the configuration of Rclone.

### New Rclone Setup

Run the following command:

``` shell
rclone config
```
Which should give you something like this.

``` shell
➜  ~ rclone config
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q>
```
Type in **n** (for new remote) and then name it **google**:

``` shell
➜  ~ rclone config
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> google
```
Afterwhich you will be presented with a list of all the remotes that Rclone supports but since this guide assumes you are using Google Drive so just enter **drive**:

``` shell

➜  ~ rclone config
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> google
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Citrix Sharefile
   \ "sharefile"
 9 / Compress a remote
   \ "compress"
10 / Dropbox
   \ "dropbox"
11 / Encrypt/Decrypt a remote
   \ "crypt"
12 / Enterprise File Fabric
   \ "filefabric"
13 / FTP Connection
   \ "ftp"
14 / Google Cloud Storage (this is not Google Drive)
   \ "google cloud storage"
15 / Google Drive
   \ "drive"
16 / Google Photos
   \ "google photos"
17 / Hadoop distributed file system
   \ "hdfs"
18 / Hubic
   \ "hubic"
19 / In memory object storage system.
   \ "memory"
20 / Jottacloud
   \ "jottacloud"
21 / Koofr
   \ "koofr"
22 / Local Disk
   \ "local"
23 / Mail.ru Cloud
   \ "mailru"
24 / Mega
   \ "mega"
25 / Microsoft Azure Blob Storage
   \ "azureblob"
26 / Microsoft OneDrive
   \ "onedrive"
27 / OpenDrive
   \ "opendrive"
28 / OpenStack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
   \ "swift"
29 / Pcloud
   \ "pcloud"
30 / Put.io
   \ "putio"
31 / QingCloud Object Storage
   \ "qingstor"
32 / SSH/SFTP Connection
   \ "sftp"
33 / Sugarsync
   \ "sugarsync"
34 / Tardigrade Decentralized Cloud Storage
   \ "tardigrade"
35 / Transparently chunk/split large files
   \ "chunker"
36 / Union merges the contents of several upstream fs
   \ "union"
37 / Webdav
   \ "webdav"
38 / Yandex Disk
   \ "yandex"
39 / Zoho
   \ "zoho"
40 / http Connection
   \ "http"
41 / premiumize.me
   \ "premiumizeme"
42 / seafile
   \ "seafile"
Storage> drive
```
Then you are presented with a request for a client ID which you can find out how to create by following the [link](https://rclone.org/drive/#making-your-own-client-id) in the below example.

``` shell
** See help for drive backend at: https://rclone.org/drive/ **

Google Application Client Id
Setting your own is recommended.
See https://rclone.org/drive/#making-your-own-client-id for how to create your own.
If you leave this blank, it will use an internal key which is low performance.
Enter a string value. Press Enter for the default ("").
client_id>
```
Afterwards you are prompted to enter the client secret that accompanies the client ID from above:

``` shell
OAuth Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_secret>
```
You will then be asked which scope to use and in this instance we want full access which is **drive**:

``` shell
Scope that rclone should use when requesting access from drive.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
 1 / Full access all files, excluding Application Data Folder.
   \ "drive"
 2 / Read-only access to file metadata and file contents.
   \ "drive.readonly"
   / Access to files created by rclone only.
 3 | These are visible in the drive website.
   | File authorization is revoked when the user deauthorizes the app.
   \ "drive.file"
   / Allows read and write access to the Application Data folder.
 4 | This is not visible in the drive website.
   \ "drive.appfolder"
   / Allows read-only access to file metadata but
 5 | does not allow any access to read or download file content.
   \ "drive.metadata.readonly"
scope> drive
```
Choose the default in this step as we want access to the whole drive:

``` shell
ID of the root folder
Leave blank normally.

Fill in to access "Computers" folders (see docs), or for rclone to use
a non root folder as its starting point.

Enter a string value. Press Enter for the default ("").
root_folder_id>
```
You should leave the next option blank as well unless you know what you're doing:

``` shell
Service Account Credentials JSON file path
Leave blank normally.
Needed only if you want use SA instead of interactive login.

Leading `~` will be expanded in the file name as will environment variables such as `${RCLONE_CONFIG_DIR}`.

Enter a string value. Press Enter for the default ("").
service_account_file>
```
When asked to edit advanced config just use the default (No):

``` shell
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n>
```
Enter **n** (No) here if on a headless machine:

``` shell
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes (default)
n) No
y/n> n
```
Go to the link shown in the output and post the verification code after logging into your Google Account.

``` shell
Please go to the following link: https://accounts.google.com/o/oauth2/xxxxxx
Log in and authorize rclone for access
Enter verification code>
```
When asked if you want to setup your remote as a shared drive (Team drive) it will depend on if you setup a team drive or not. List of shared drives will be shown if you go that route and then just choose the one you want.

``` shell
Configure this as a Shared Drive (Team Drive)?
y) Yes
n) No (default)
y/n>
```
Then you're hopefully presented with something akin to this:

``` shell
--------------------
[google]
type = drive
client_id = <snip>
client_secret = <snip>
scope = drive
token = {"some token"}
team_drive = <snip>
root_folder_id =
--------------------
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d>
```
After which you can hit enter and either type **q** to exit the configuration tool or setup additional drives which is outside the scope of this guide.

``` shell
Current remotes:

Name                 Type
====                 ====
google               drive

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q
```
### Existing Rclone Setup

You do not have to rename the remote you want to use to **google** but if you don't do that you will have to change the remote specified in the settings.yml


## Install Saltbox

=== "Saltbox"
    Some text about Saltbox

=== "Mediabox"
    Some text about Mediabox

=== "Feederbox"
    Some text about Feederbox

=== "Core"
    Some text about Core

## Reboot

You're now ready to install other apps and tweak the setup as you see fit. After rebooting!
