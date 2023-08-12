# Autoscan

## What is it?

[Autoscan](https://github.com/Cloudbox/autoscan){: target=_blank rel="noopener noreferrer" } replaces the default Plex, Emby, and Jellyfin behaviour for picking up file changes on the file system. Autoscan integrates with Sonarr, Radarr, Lidarr and Google Shared Drives to fetch changes in near real-time without relying on the file system.

Autoscan is a rewrite of the original Plex Autoscan written in the Go language. In addition, this rewrite introduces a more modular approach and should be easy to extend in the future.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/cloudb0x/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } |

## Setup

The Plex API is known to have trouble when scanning items into empty libraries.  You should add at least one item to each Plex library and perform a manual scan as a first step.  If you don't do this, things may not get scanned into Plex in response to autoscan's requests.

The Saltbox Autoscan role will attempt to partially configure your autoscan config file located at `/opt/autoscan/config.yml`. You should refer to the documentation and adjust this file as suits your own needs. The config generated is very minimal. [a-train](https://github.com/m-rots/a-train/pkgs/container/a-train){: target=_blank rel="noopener noreferrer" } is now replacing the bernard trigger.

The generated config file will look something like this:

```yaml
# <- processor ->

# Override the minimum age before a scan request is sent to the target (Default 10m):
minimum-age: 10m

# Override the delay between processed scans (Default 5s):
scan-delay: 5s

# Set anchor files for remote storage. If these are missing no scans will be sent to the target to avoid files being trashed when a mount fails
anchors:
  - /mnt/unionfs/mounted.bin

# <- triggers ->

# Optionally, protect your webhooks with authentication
authentication:
  username: USERNAME_FROM_SETTINGS
  password: PASSWORD_FROM_SETTINGS

# Port for Autoscan webhooks to listen on
port: 3030

triggers:
  a-train:
      priority: 5
      rewrite: # Global rewrites
        - from: ^/Media/
          to: /mnt/unionfs/Media/


  inotify:
    - priority: 0

      # Filter with regular expressions
      include:
        - ^/mnt/unionfs/Media/
      exclude:
        - '\.(srt|pdf)$'

      # rewrite inotify path to unified filesystem
      rewrite:
        - from: ^/mnt/local/Media/
          to: /mnt/unionfs/Media/

      # Local filesystem paths to monitor
      paths:
        - path: /mnt/local/Media

  sonarr:
    - name: sonarr # /triggers/sonarr
      priority: 2

  radarr:
    - name: radarr # /triggers/radarr
      priority: 2

  lidarr:
    - name: lidarr # /triggers/lidarr
      priority: 1

# <- targets ->

targets:
  plex:
    - url: https://plex.DOMAIN.TLD # plex
      token: YOUR_PLEX_TOKEN
```

Then edit the anchors section:

```yaml
anchors:
  - /mnt/unionfs/mounted.bin
```

To reflect your own configuration.

YOU POSSIBLY NEED TO CREATE THIS FILE OR FILES YOURSELF.  The regular saltbox install does not do it for you.

If you went through the OPTIONAL google-drive rclone setup process, these files *did* get created for you, and you'll need to enter something like:

```yaml
anchors:
  - /mnt/unionfs/bvoiwepopz-movies_mounted.bin
  - /mnt/unionfs/bvoiwepopz-tv_mounted.bin
  - /mnt/unionfs/bvoiwepopz-music_mounted.bin
  - /mnt/unionfs/bvoiwepopz-anime_mounted.bin
...
```

You should enter the entire list of bin files that were created by the automated script here.

If you didn't go through that process, use:
```
rclone touch NAME_OF_CLOUD_REMOTE:mounted.bin
```
To create one of these files on *each distinct element* of cloud storage.  If you're using Dropbox, there is just one.  If you have eleven OneDrive mounts, you need to create eleven of these.

Once you've done that, verify that they show up in the union mount with:

```
ls /mnt/unionfs/*.bin
```

then enter that list of files into the autoscan config as shown.

Everything else should be ready to go for standard usage.

<details>
<summary>What are those mount files?</summary>
<br />
<br />
Autoscan uses these to determine if your cloud storage is mounted and visible; if autoscan can't see these files, no scans will be sent to Plex since doing so would empty your library as Plex removed all the files it can no longer see [assuming that "empty trash on scan" is enabled].
<br />
<br />
There's nothing special about the contents of these files; autoscan just needs to see that they exist.  Typically they are empty.
<br />
<br />
If you went through the saltbox rclone setup, these files got created for you.  
<br />
<br />
</details>

<details>
<summary>Do I really need to include all seven or eight or however many?</summary>
<br />
<br />
Strictly speaking, no, not with the way saltbox sets up the mounts.  All those shared drives are part of a union remote, and the union remote is mounted, so there's really no possibility that some of those files would be present but not others.  Any one of them is probably sufficient.
<br />
<br />
However, there's no reason *not* to include them all as you can grab the list with a single command and a copy-paste.  You save a few keystrokes by not including all of them [you don't have to copy-paste `  - ` in front of those few lines], but in thinking about it at all you've spent the same amount of time.  Reading this question and answer have taken more time than it would have taken to include all of them as a belt-and-suspenders measure.
<br />
<br />
</details>

<details>
<summary>Is there something magic about the name `mounted.bin`?</summary>
<br />
<br />
No.  These files can be named whatever you want.  If you don't like `mounted.bin` and woudl rather use `black.sabbath` or whatever, go ahead.  Autoscan is just going to verify that the file you specify exists so autoscan knows it is safe to send scans to Plex.
<br />
<br />
</details>

You will set up the webhooks for radarr/sonarr/lidarr as part of their setup, so they aren't discussed here

### Manual Scan URL

The manual scan URL will be https://autoscan.YOUR_DOMAIN/triggers/manual.  Usage is described in the autoscan docs linked below.

### A-Train

Autoscan can monitor **Google Drive** changes via a trigger called "Bernard".  The code behind Bernard can sometimes get out of sync with the state of Google Drive and miss things, so now we are using A-Train.

**IMPORTANT**:
You only need to set this up if you are planning to add media to **Google Drive** directly, *outside* the usual Radarr/Sonarr channels, or if you are monitoring a Shared Drive where new media appears outside those channels.  If you are not planning to do that, you can skip this portion of the setup.

**IMPORTANT**:
A-Train does not support anything other than **Google Drive**, as it uses the Google Drive API to do its work.

"A-Train" is a rewrite of the Bernard concepts, and is currently available as a second docker image as part of Sandbox.  It will likely be integrated into autoscan at some point in the future.

!!! warning
    A-Train supports **only** *unencrypted* Google Shared Drives authenticated via Service Accounts.  It *does not* support encrypted drives, My Drive, or authentication via Client ID/Secret or other means.

Enter the names of the remotes you want to monitor in the [sandbox settings.yml](https://docs.saltbox.dev/sandbox/settings/). The Remotes can be either drive remotes or union remotes. You may use ```rclone listremotes``` to get your drive remotes.

Example:

```yaml
a_train:
  remotes: ["bvoiwepopz-Movies", "bvoiwepopz-TV"]
```

or

```yaml
a_train:
  remotes: ["google"]
```

Run the a-train tag to create the container:

```bash
sb install sandbox-a_train
```

Copy one of your service account files from its current location to `/opt/a-train/account.json`.  Remember to rename your service account file to "`account.json`".

Example:

```bash
cp /opt/sa/all/160.json /opt/a-train/account.json
```

Run the autoscan tag to rebuild the container:

```bash
sb install autoscan
```

Run the a-train tag to rebuild the container:

```bash
sb install sandbox-a_train
```

### Bernard

**IMPORTANT**:
Bernard does not support anything other than **Google Drive**, as it uses the Google Drive API to do its work.

If for some reason you still wanted to use Bernard, it would look like this:

```yaml
triggers:
  bernard:
    - account: /config/sa.json # Path inside the container where your SA is located
      cron: "*/5 * * * *" # every five minutes (the "" are important)
      priority: 0
      drives:
        - id: drive_id #Friendly title
      # Rewrite gdrive to the local filesystem
      rewrite:
        - from: ^/Media/
          to: /mnt/unionfs/Media/
      # Filter with regular expressions
      include:
        - ^/mnt/unionfs/Media/
      exclude:
        - '\.srt$'
```

Further documentation:

- [A-Train Docker page](https://github.com/users/m-rots/packages/container/package/a-train)

- [A-Train initial documentation](https://gist.github.com/m-rots/f345fd2cfc44585266b620feb9fbd612)

- [:octicons-link-16: Documentation](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" }

## Next

Are you setting Saltbox up for the first time?  Continue to [Sonarr](sonarr.md).
