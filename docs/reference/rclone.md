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
Type in **n** (for new remote) and then name it `google`

``` shell
➜  ~ rclone config
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> google
```
After which you will be presented with a list of all the remotes that Rclone supports but since this guide assumes you are using Google Drive so just enter `drive`

``` shell
Type of storage to configure.
Enter a string value. Press Enter for the default ("").
Choose a number from below, or type in your own value
...
15 / Google Drive
   \ "drive"
...
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
You will then be asked which scope to use and in this instance we want full access which is `drive`

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
When asked to edit advanced config just use the default `n`

``` shell
Edit advanced config? (y/n)
y) Yes
n) No (default)
y/n>
```
Enter `n` (No) here if on a headless machine:

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
After which you can hit enter and either type `q` to exit the configuration tool or setup additional drives which is outside the scope of this guide.

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

You do not have to rename the remote you want to use to `google` but if you don't do that you will have to change the remote specified in the settings.yml

TODO: ADD DISCUSSION OF CREATING A UNION REMOTE