[Rclone](https://rclone.org) (by Nick Craig-Wood) is "rsync for the cloud". Basically, it is used to transfer data to or from a variety of supported cloud storage providers (eg Google Drive).

Rclone is used by [Cloudplow](cloudplow.md) and [Backup](../saltbox/backup/backup.md) to upload media and backup Saltbox, respectively.

The guide below assumes you are using Google Drive. 

If you would like to set this up with another cloud storage provider, but have not setup Rclone yet, then follow the guide [below](#new-rclone-setup) and replace all mentions of "Google Drive" with your preferred cloud storage provider's name. [Note that this does not mean that any arbitrary rclone backend will actually work in this context]

If you already have Rclone configured, you can jump directly to the [relevant section](#existing-rclone-setup). 

## New Rclone Setup

1. Create a new project and generate a credential file:

    [Instructions here](google-project-setup.md)

    Save that credential file at `/opt/sa/project-creds.json`

2. Create a Google Group to hold service accounts:

    [Instructions here](google-group-setup.md)

3. Set up the GCloud SDK:
    
    [Instructions here](google-gcloud-tools-install.md)

4. Generate a random prefix

    ```
    prefix=$(head /dev/urandom | tr -dc a-z | head -c10 ;) && echo $prefix
    ```

    Make a note of that prefix; you will use it in the next two steps.

5. generate some service accounts

    [Instructions here](google-service-accounts.md)

6. Create some Shared Drives

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

8. Done.


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
