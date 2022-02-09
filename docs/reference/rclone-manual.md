[Rclone](https://rclone.org) (by Nick Craig-Wood) is "rsync for the cloud". Basically, it is used to transfer data to or from a variety of supported cloud storage providers (eg Google Drive).

Rclone is used by [Cloudplow](cloudplow.md) and [Backup](../saltbox/backup/backup.md) to upload media and backup Saltbox, respectively.

The guide below assumes you are using Google Drive.

Rclone supports many cloud provider backends, but the only one routinely used by the Saltbox team is Google Drive.

This process will use various scripts to do as much of this for you as possible, but there are some things that can't be scripted easily, like steps 1 and 2 below.

<details>
<summary>What about `safire`? Can't it do all this automatically?</summary>
<br />

  Sure, and the first version of this attempt at automation used safire to do everything from step 3 on with two runs of a script which asked a couple questions.  It always worked on the developer's machine, but failed half the time on not-the-developer's machine.  So this approach was built out to not use `safire`.

  Eventually there will be an app or script that will take care of all this, but until that day, there is this.

  If you have suggestions about how this can be made more clear, by all means open an issue.

</details>

Here's what you are going to do as you work through the instructions below:

[These are not the instructions, just an overview]

1. Create a Google project. [not scripted, you'll do this manually]

1. Create a Google group. [not scripted, you'll do this manually]

1. Install the Google SDK tools. [not scripted, you'll do this manually]

1. Create a bunch of service accounts and put all the service accounts' JSON files into a subdirectory of `/opt`. [scripted with minor config edits]

1. Add all those service accounts to the Google group you just created. [Starting here scripted with minor config edits to a single script]

1. Create three new shared drives in the Google Drive UI. [Movies, Music, TV]

1. Add your Google Group to each of those drives as a "Manager"

1. Create rclone remotes pointing to each of those shared drives, authenticated using one of those service files.

1. Create a union rclone remote called "google", with the components set to the three td remotes you just created.


If you already have Rclone configured, you can jump directly to the [relevant section](#existing-rclone-setup).

## New Rclone Setup

1. Verify that the Shared Drive permissions are correct on your Google account:

    [Instructions here](google-account-perms.md)

2. Create a new project and generate a credential file:

    [Instructions here](google-project-setup.md)

    Save that credential file on your server at `/opt/sa/project-creds.json`

3. Create a Google Group to hold service accounts:

    [Instructions here](google-group-setup.md)

4. Set up the GCloud SDK:

    [Instructions here](google-gcloud-tools-install.md)

5. Generate a random prefix

    ```
    prefix=$(head /dev/urandom | tr -dc a-z | head -c10 ;) && echo $prefix
    ```

    Make a note of that prefix; you will use it in the next two steps.

    This prefix is used for two purposes:

      1. Project names need to be unique across all of Google; a random prefix helps ensure this [the error that results in this case is non-obvious].

      1. It helps these scripts unambiguously identify things that they have created.

6. generate some service accounts

    [Instructions here](google-service-accounts.md)

7. Create some Shared Drives and related infrastructure

    [Instructions here](google-shared-drives.md)

7. Verify that the union remote shows you the expected contents:

    ```
    rclone tree google:/
    ```

    This should display something like:

    ```
    /
    ├── -- aZaSjsklaj-Movies Shared --
    ├── -- aZaSjsklaj-Music Shared --
    ├── -- aZaSjsklaj-TV Shared --
    ├── Media
    │   ├── Movies
    │   ├── Music
    │   └── TV
    ├── azasjsklaj-movies_mounted.bin
    ├── azasjsklaj-music_mounted.bin
    └── azasjsklaj-tv_mounted.bin

    7 directories, 3 files
    ```

9. You now have three shared drives and union combining them; the saltbox install will merge this with your local drive and cloudplow will upload to the union mount, which will distribute media to the three shared drives by path.  You will still be limited to the 750GB/day Google upload limit until you configure cloudplow to upload directly to the individual shared drives.  Eventually this will be automated, but for now there is [this guide](cloudplow-config.md).

9. If you want to use Plex Autoscan's Google Drive Monitoring, there are some changes that will be required in the configuration. See [this guide](plex-autoscan-config.md).

## Existing Rclone Setup

The default remote specified in [[settings.yml|Install: settings.yml]] is `google` for Google Drive. If the Rclone remote in your config has the same name, then you are OK to skip this page and go on to the next.

If you are using Google Drive and the Rclone remote in your config has a different name, then you will need to either:

- Rename your current Rclone remote to the default one (i.e. `google`). Instructions for this are below.

  Or

- Edit the Rclone remote entry in [[settings.yml|Install: settings.yml]] with yours.

If you prefer to use another cloud storage provider, you can add the name of the Rclone remote in to [[settings.yml|Install: settings.yml]].

### Rename Existing Rclone Remote

To rename the Google Drive remote to `google`:

1. Find and edit your Rclone configuration file.

   ```
   nano $(rclone config file | tail -n 1)
   ```
1. Rename the Google Drive drive remote (name between the brackets) to `google`.

1. It will now look like this:

   ```
   [google]
   type = drive
   client_id = 1234567890123-mjffsmxvendscftuvnyngkhegapovgnv.apps.googleusercontent.com
   client_secret = klflzftkrwuwuedesxzewsfz
   token = {"access_token":"ya30.gelftvrymioiilvdtfegfvhfgallrhocewjckdnnvmxdjpjzbdhkmgulvqhgbafkdtpottzthhnyzysxwlpf-38ikRIxZvimyoxyKdse$
   ```
1. Save the file and exit: <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd>.

1. Copy the config file to `~/.config/rclone/rclone.conf` (if it isn't there already):

   ```
   cp -n $(rclone config file | tail -n 1) ~/.config/rclone/rclone.conf
   ```

1. Give it the proper ownership and permissions. Replace `user` and `group` to match yours' (see [here](FAQ#find-your-user-id-uid-and-group-id-gid)):

   ```
   sudo chown user:group ~/.config/rclone/rclone.conf
   sudo chmod 755 ~/.config/rclone/rclone.conf
   ```
