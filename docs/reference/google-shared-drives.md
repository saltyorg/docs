This guide will show you how to create default Saltbox Shared Drives and add your group of SAs to them.

NOTE: This guide is assuming a Google Gsuite Business/Workspace account.

1. Retrieve the `sb-gd` code

    ```
    git clone https://github.com/chazlarson/sb_gd.git  && cd sb_gd
    ```

1. Create and activate a virtual environment:

    ```
    python3 -m venv sb_gd && source sb_gd/bin/activate
    ```
    
2. Install script requirements:

    ```
    python -m pip install -r requirements.txt
    ```

3. Edit the `config.py` script:

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

4. Copy your credential JSON into this directory:

    ```
    cp  /opt/sa/project-creds.json client_secrets.json
    ```

5. Run the `sb_sd.py` script:

    ```
    python sb_sd.py
    ```

    You will be asked to authenticate in the usual Google way.  Follow the prompts.

    `sa-gen` will create three shared drives, add your group email as a manager, create mount files and ID folders on the root, build the folder structure as defined in the config, and create rclone remotes for the individual shared drives and a union rclone remote for use with Saltbox :

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

6. You're done.
