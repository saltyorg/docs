This guide will show you how to create default Saltbox Shared Drives and add your group of SAs to them.

It's assuming you're working through the steps from [here](rclone-manual.md), have already created the required [project](google-project-setup.md), have already created the required [group](google-group-setup.md), have installed the [gcloud SDK tools](google-gcloud-tools-install.md), and have created the expected [projects and service accounts](google-service-accounts.md).

NOTE: This guide is assuming a Google Gsuite Business/Workspace account.

1. Retrieve the `sb-gd` code

    ```
    git clone https://github.com/chazlarson/sb_gd.git  && cd sb_gd
    ```

2. Create and activate a virtual environment:

    ```
    python3 -m venv sb_gd && source sb_gd/bin/activate
    ```

3. Install script requirements:

    ```
    python -m pip install -r requirements.txt
    ```

4. Edit the `config.py` script:

    ```
    nano config.py
    ```

    Edit as indicated by `<<<<` below:

    ```
    prefix = 'akIhSwlKdf'                <<<< the prefix you generated previously

    group_email = "all-sa@DOMAIN.com"    <<<< the group you created previously

    drive_data = {
        'Movies':'/Media/Movies',
        'Music':'/Media/Music',
        'TV':'/Media/TV'
    }
    ```

5. Copy your credential JSON into this directory:

    ```
    cp  /opt/sa/project-creds.json client_secrets.json
    ```

6. Run the `sb_sd.py` script:

    ```
    python sb_sd.py
    ```

    You will be asked to authenticate in the usual Google way.  Follow the prompts.

    This script will create three shared drives, add your group email as a manager, create mount files and ID folders on the root, build the folder structure as defined in the config, and create rclone remotes for the individual shared drives and a union rclone remote for use with Saltbox:

    ```
    ** Team Drive aZaSjsklaj-Movies created, ID: 123456789
    ** user all-sa@domain.com created as organizer, ID: 123456789
    ** Folder -- aZaSjsklaj-Movies Shared -- created, ID 123456789
    ** bin file created on root, ID 123456789
    ** Folder Media created, ID 123456789
    ** Folder Movies created, ID 123456789
    --------------------
    [aZaSjsklaj-Movies]
    type = drive
    scope = drive
    service_account_file = /opt/sa/all/150.json
    team_drive = 123456789
    --------------------
    0
    ** Team Drive aZaSjsklaj-Music created, ID: 123456789
    ** user all-sa@domain.com created as organizer, ID: 123456789
    ** Folder -- aZaSjsklaj-Music Shared -- created, ID 123456789
    ** bin file created on root, ID 123456789
    ** Folder Media created, ID 123456789
    ** Folder Music created, ID 123456789
    --------------------
    [aZaSjsklaj-Music]
    type = drive
    scope = drive
    service_account_file = /opt/sa/all/150.json
    team_drive = 123456789
    --------------------
    0
    ** Team Drive aZaSjsklaj-TV created, ID: 123456789
    ** user all-sa@domain.com created as organizer, ID: 123456789
    ** Folder -- aZaSjsklaj-TV Shared -- created, ID 123456789
    ** bin file created on root, ID 123456789
    ** Folder Media created, ID 123456789
    ** Folder TV created, ID 123456789
    --------------------
    [aZaSjsklaj-TV]
    type = drive
    scope = drive
    service_account_file = /opt/sa/all/150.json
    team_drive = 123456789
    --------------------
    0
    --------------------
    [google]
    type = union
    upstreams = aZaSjsklaj-Movies: aZaSjsklaj-Music: aZaSjsklaj-TV:
    --------------------
    ```

    Drive names and IDs will be written to `drive_create_log`.

    <details>
    <summary>What are those directories and files for?</summary>
    <br />

    This script creates an empty directory and a zero-byte file on the root of each shared drive.

    The file will be useful later on when you need "is this disk mounted?" flags for things like `plex_autoscan`.

    The directory is a belt-and-suspenders convenience you can use to see if your union remote and/or mergerfs config is including everything it should.  We create both a file and a dir so you will get this information whether you use `rclone ls REMOTE` or `rclone lsd REMOTE` or whatever other means:

    ```
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

7. You're done.

If you are going through the manual rclone instructions, [continue with the next step](rclone-manual/#new-rclone-setup)