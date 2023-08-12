# Google Shared Drives

This guide will show you how to create default Saltbox Shared Drives and add your group of SAs to them.

It's assuming you're working through the steps from [here](rclone-manual.md) and have completed the following steps:

- verified [account drive permissions](google-account-perms.md)
- created the required [project](google-project-setup.md)
- created the required [group](google-group-setup.md)
- installed the [gcloud SDK tools](google-gcloud-tools-install.md)
- created the expected [projects and service accounts](google-service-accounts.md)

NOTE: This guide is assuming a Google Gsuite Business/Workspace account.

If you already have media on Google Drive [My Drive OR Shared Drives] from your time with Cloudbox or PlexGuide or the like, you most likely DO NOT WANT TO DO THIS.  This process is assuming you are starting from scratch without any of this already set up.  It may overwrite aspects of an existing rclone setup with no undo.

1. Retrieve the `sb-gd` code

    [copy-paste this into your terminal window]

    ```shell
    cd /opt && git clone https://github.com/chazlarson/sb_gd.git  && cd sb_gd
    ```

2. Create and activate a virtual environment:

    [copy-paste this into your terminal window]

    ```shell
    python3 -m venv sb_gd && source sb_gd/bin/activate
    ```

    <details>
    <summary>If that command produces an error:</summary>
    <br />

    If you see something like this:

    ```text
    The virtual environment was not created successfully because ensurepip is not
    available.  On Debian/Ubuntu systems, you need to install the python3-venv
    package using the following command.

        apt install python3.8-venv

    You may need to use sudo with that command.  After installing the python3-venv
    package, recreate your virtual environment.

    Failing command: ['/home/YOU/sb_gd/sb_gd/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']
    ```

    run the suggested command with `sudo`:

    [copy-paste the command from the error into your terminal window]

    ```shell
    sudo COMMAND FROM ERROR ABOVE
    ```

    Then try the virtual-environment command in step 2 again.

    </details>

3. Install script requirements:

    [copy-paste this into your terminal window]

    ```shell
    python -m pip install -r requirements.txt
    ```

4. Create and edit the `config.py` file:

    [copy-paste this into your terminal window]

    ```shell
    cp config.py.example config.py
    nano config.py
    ```

    Edit as indicated by `<<<<` below:

    ```python
    prefix = 'aZaSjsklaj'                # <<<< the prefix you generated previously

    group_email = "all-sa@bing.bang"     # <<<< the group you created previously

    sa_file = "/opt/sa/all/150.json"     # <<<< edit this path if required;
                                         # if you've followed all previous steps correctly
                                         # it shouldn't be required.

    backup_drive = "automatic"           # <<<< edit this if desired
                                         # If this is set to "automatic", the backup drive
                                         # will be the last shared drive the script sees.
                                         # Enter one of the names below to use that one.
                                         # Enter anything else to disable.
                                         # backup discussed below.

    # `drive name`: '/directory/on/this/drive`
    drive_data = {                       # <<<< add additional drives and media paths here.  Media paths must be unique per drive.
        'Anime': '/Media/Anime',
        'Books': '/Media/Books',
        'Movies': '/Media/Movies',
        'Movies-4K': '/Media/Movies-4K',
        'Music': '/Media/Music',
        'TV': '/Media/TV',
        'TV-4K': '/Media/TV-4K'
    }
    ```

    If you noticed and deleted some empty JSON files in the previous step, verify that `/opt/sa/all/150.json` exists; if it doesn't, change that line in `config.py` to any other JSON file that *does* exist.   There's nothing magic about `150.json`.

    If you don't want to create some of those shared drives, remove the line.  It's safe to go ahead and create them for simplicity later in the event you want to start using them.  The list should not have a comma at the end, as shown above.

    Save the file with control-x, y, enter

5. Copy your credential JSON into this directory:

    [copy-paste this into your terminal window]

    ```shell
    cp  /opt/sa/project-creds.json client_secrets.json
    ```

    This is the credential file you downloaded a couple steps ago.  Recall that in that step I said I would later assume you'd put it at `/opt/sa/project_creds.json`.  Here's that assumption.

    If you've stored the file elsewhere, copy it from there via whatever means.  It just has to end up at `/opt/sb_gd/client_secrets.json`.

6. Run the `sb_sd.py` script:

    **IMPORTANT**: If you are running a server on your local machine that is listening for HTTP requests on port 8080, disable it before running this script.  This process will send you to a `localhost` URL, and is expecting that this will fail so you can copy the URL.  If you have a local server running on this port, you will probably see some other error instead.

    [copy-paste this into your terminal window]

    ```shell
    python sb_sd.py
    ```

    You will be asked a bunch of questions about the previous steps.  If the answers are not all "YES", you'll need to go complete those steps.  If you lie and answer YES when you haven't completed those steps, this script will fail in some way.  There is no way to avoid performing all the steps.

    You will be asked to authenticate in the usual Google way.  Follow the prompts.

    For the time being, due to changes in the Google OAuth process, this will try to redirect you to a `localhost` URL, which will fail.  The URL will look like:

    `http://localhost:8000/oauth2callback?code=4/NUMBERS_AND_STUFF&scope=https://www.googleapis.com/auth/drive`

    Copy the ENTIRE URL and paste it at the prompt where the script is waiting.

    We're working on making this a bit more friendly.

    This script will create shared drives as listed in the config, add your group email as a manager, create mount files and ID folders on the root of each drive, build the folder structure as defined in the config, and create rclone remotes for the individual shared drives and a union rclone remote for use with Saltbox.

    It will fill in anything that is missing; if the shared drives are there but the media folders haven't been created, those will be created.  If everything has been created but the rclone remotes are missing; those will be filled in.
    
    NOTE: It will not touch any shared drives which it didn't create itself, and it does not delete data from any shared drives.

    If you defined a "backup_drive" in the config [or left it as "automatic"], then script will zip up:

    1. All your service account JSON files
    1. Your rclone config file
    1. Your `client_secret.json` file
    1. Your `storage.json` file
    1. The log file of shared drives created and IDs

    It will zip those files up and upload them to `BACKUP_DRIVE\saltbox_sd_backup\backup.zip`

    Future runs will delete the current backup and overwrite the remote file.

    This of course takes the place of the BEFORE YOU DO ANYTHING ELSE admonition at the bottom of this page:

    You should see output similar to this [of course, you will see more than one shared drive creation; the rest are left out here for space]:

    ```text
    [previous shared drive creations removed]
    
    ** Team Drive heilung-TV-4K created, ID: AAAAAAAAAAAAAAAAAAA
    ** user all-sa@XXXXXXXX.com set as organizer, ID: BBBBBBBBBBBBBBBBBBBB
    ** Created folder -- heilung-TV-4K Shared --, ID CCCCCC-CCCCCCCCCCCCCCCCCCCCCCCCCC
    ** Created file -- heilung-TV-4K Shared --, ID D-DDDDDDDDDDDD-DDDDDDDDDDDDDDDDDD
    ** Created folder Media, ID EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    ** Created folder TV-4K, ID FFFFFFFFFFFFFFF-FFFFFFFFFFFFFFFFF
    Creating rclone remote: heilung-TV-4K
    rclone remote definition ========
    [heilung-TV-4K]
    type = drive
    scope = drive
    service_account_file = /opt/sa/all/150.json
    team_drive = AAAAAAAAAAAAAAAAAAA

    Creating rclone union remote 'google':
    rclone remote definition ========
    [google]
    type = union
    upstreams = heilung-Anime:/ heilung-Books:/ heilung-Movies:/ heilung-Movies-4K:/ heilung-Music:/ heilung-TV:/ heilung-TV-4K:/ 
    Deleting previous backup files...
    Preparing backup files...
    Creating backup archive...
    Uploading backup archive to heilung-TV-4K/saltbox_sd_backup...
    Upload Complete!
    All done.
    ```

    Note: the script uses `/opt/sa/all/150.json` in the rclone configuration for these remotes; that's not something you have to set or create [you'll note that it hasn't been mentioned much above].  That one is used because it's right in the middle of the SAs you just created, so it's unlikely that SA cycling in cloudplow will ever exhaust enough SAs to hit this one and possibly affect your mounts.

    Drive names and IDs will be written to `drive_create_log`.

    <details>
    <summary>What are those directories and files for?</summary>
    <br />

    This script creates an empty directory and a zero-byte file on the root of each shared drive.

    The file will be useful later on when you need "is this disk mounted?" flags for things like `plex_autoscan` or `autoscan`.

    The directory is a belt-and-suspenders convenience you can use to see if your union remote and/or mergerfs config is including everything it should.  We create both a file and a dir so you will get this information whether you use `rclone ls REMOTE` or `rclone lsd REMOTE` or whatever other means:

    ```shell
     $ rclone lsd google:
          -1 2021-11-21 17:09:13        -1 -- aZaSjsklaj-Movies Shared --
          -1 2021-11-21 17:11:50        -1 -- aZaSjsklaj-Music Shared --
          -1 2021-11-21 17:12:09        -1 -- aZaSjsklaj-TV Shared --
          -3 2021-11-21 17:12:11        -1 Media

     $ rclone ls google:
            0 azasjsklaj-movies_mounted.bin
            0 azasjsklaj-tv_mounted.bin
            0 azasjsklaj-music_mounted.bin
    ```

    </details>

7. You're done.  Deactivate the virtual env used by this script.

    ```shell
     deactivate
    ```

BEFORE YOU DO ANYTHING ELSE:

- BACK UP `/opt/sa` TO YOUR LOCAL COMPUTER
- BACK UP `/home/YOU/.config/rclone/rclone.conf` TO YOUR LOCAL COMPUTER

The automatic backup above would have done this for you.  If for some reason you want to wipe your machine and start again OUTSIDE THE USUAL BACKUP/RESTORE you will need those files. You can just restore them rather than going through this whole process again.

If you are going through the manual rclone instructions, [continue with the next step](rclone-manual.md#step-8-verify-that-the-union-remote-shows-you-the-expected-contents)

IF YOU WANT TO RUN THIS AGAIN TO ADD MORE SHARED DRIVES:

1. Go to the directory and activate the virtual environment:

    [copy-paste this into your terminal window]

    ```shell
    cd /opt/sb_gd && source sb_gd/bin/activate
    ```

2. Edit the `config.py` script to add the additional shared drives:

3. Run the script:

    [copy-paste this into your terminal window]

    ```shell
    python sb_sd.py
    ```

4. Deactivate the virtual env used by this script.

    ```shell
    deactivate
    ```

5. Rerun the cloudplow setup script if desired. [notes](cloudplow-config.md#updating-cloudplow-config-for-additional-shared-drives)

6. Reboot your server

    ```shell
    sudo reboot
    ```
