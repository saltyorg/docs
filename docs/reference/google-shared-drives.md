This guide will show you how to create default Saltbox Shared Drives and add your group of SAs to them.

It's assuming you're working through the steps from [here](rclone-manual.md) and have completed the following steps:

  - verified [account drive permissions](google-account-perms.md)
  - created the required [project](google-project-setup.md)
  - created the required [group](google-group-setup.md)
  - installed the [gcloud SDK tools](google-gcloud-tools-install.md)
  - created the expected [projects and service accounts](google-service-accounts.md)

NOTE: This guide is assuming a Google Gsuite Business/Workspace account.

IF YOU HAVE DONE THIS BEFORE, THERE IS NO REASON TO REPEAT IT.  THIS SCRIPT MAY PRODUCE A SECOND SET OF SHARED DRIVES, AND THERE IS NO REASON FOR THIS.

1. Retrieve the `sb-gd` code

    [copy-paste this into your terminal window]

    ```
    cd /opt && git clone https://github.com/chazlarson/sb_gd.git  && cd sb_gd
    ```

2. Create and activate a virtual environment:

    [copy-paste this into your terminal window]

    ```
    python3 -m venv sb_gd && source sb_gd/bin/activate
    ```

    <details>
    <summary>If that command produces an error:</summary>
    <br />

    If you see something like this:
    ```
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

    ```
    sudo COMMAND FROM ERROR ABOVE
    ```
    
    Then try the virtual-environment command in step 2 again.

    </details>

3. Install script requirements:

    [copy-paste this into your terminal window]

    ```
    python -m pip install -r requirements.txt
    ```

4. Edit the `config.py` script:

    [copy-paste this into your terminal window]

    ```
    nano config.py
    ```

    Edit as indicated by `<<<<` below:

    ```python
    prefix = 'akIhSwlKdf'                # <<<< the prefix you generated previously

    group_email = "all-sa@DOMAIN.com"    # <<<< the group you created previously

    sa_file = "/opt/sa/150.json"         # <<<< edit this path if required; 
                                         # if you've followed all previous steps correctly
                                         # it shouldn't be required.

    drive_data = {                       # <<<< add additional drives and media paths here if needed.  Media paths should be unique per drive.
        'Movies': '/Media/Movies',
        'Music': '/Media/Music',
        'TV': '/Media/TV'
    }
    ```

    Save the file with control-x, y, enter

5. Copy your credential JSON into this directory:

    [copy-paste this into your terminal window]

    ```
    cp  /opt/sa/project-creds.json client_secrets.json
    ```

    This is the credential file you downloaded a couple steps ago.  Recall that in that step I said I would later assume you'd put it at `/opt/sa/project_creds.json`.  Here's that assumption.

    If you've stored the file elsewhere, copy it from there via whatever means.  It just has to end up at `/opt/sb_gd/client_secrets.json`.


6. Run the `sb_sd.py` script:

    **IMPORTANT**: If you are running a server on your local machine that is listening for HTTP requests on port 8080, disable it before running this script.  This process will send you to a `localhost` URL, and is expecting that this will fail so you can copy the URL.  If you have a local server running on this port, you will probably see some other error instead.

    [copy-paste this into your terminal window]

    ```
    python sb_sd.py
    ```

    You will be asked a bunch of questions about the previous steps.  If the answers are not all "YES", you'll need to go complete those steps.  If you lie and answer YES when you haven't completed those steps, this script will fail in some way.  There is no way to avoid performing all the steps.

    You will be asked to authenticate in the usual Google way.  Follow the prompts.

    For the time being, due to changes in the Google OAuth process, this will try to redirect you to a `localhost` URL, which will fail.  The URL will look like:

    ```
    http://localhost:8000/oauth2callback?code=4/NUMBERS_AND_STUFF&scope=https://www.googleapis.com/auth/drive
    ```

    Copy the ENTIRE URL and paste it at the prompt where the script is waiting.

    We're working on making this a bit more friendly.

    This script will create three shared drives, add your group email as a manager, create mount files and ID folders on the root of each drive, build the folder structure as defined in the config, and create rclone remotes for the individual shared drives and a union rclone remote for use with Saltbox.

    You should see output similar to this:

    Note: the script uses `/opt/sa/150.json` in the rclone configuration for these remotes; that's not something you have to set or create [you'll note that it hasn't been mentioned much above].  That one is used because it's right in the middle of the SAs you just created, so it's unlikely that SA cycling in cloudplow will ever exhaust enough SAs to hit this one and possibly affect your mounts.

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
    service_account_file = /opt/sa/150.json
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
    service_account_file = /opt/sa/150.json
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
    service_account_file = /opt/sa/150.json
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

    The file will be useful later on when you need "is this disk mounted?" flags for things like `plex_autoscan` or `autoscan`.

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

7. You're done.  Deactivate the virtual env used by this script.

    ```
     deactivate
    ```

BEFORE YOU DO ANYTHING ELSE:

  - BACK UP `/opt/sa` TO YOUR LOCAL COMPUTER
  - BACK UP `/home/YOU/.config/rclone/rclone.conf` TO YOUR LOCAL COMPUTER

If for some reason you want to wipe your machine and start again OUTSIDE THE USUAL BACKUP/RESTORE you will need those files. You can just restore them rather than going through this whole process again.

If you are going through the manual rclone instructions, [continue with the next step](../rclone-manual#step-8-verify-that-the-union-remote-shows-you-the-expected-contents)
