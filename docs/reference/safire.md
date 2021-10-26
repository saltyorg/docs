Saltbox defaults to using service accounts for uploading to multiple teamdrives to allow for future growth.

To make the setup more straightforward, this guide will leverage safire to generate as much infrastructure as possible.

This will set up three Shared Drives ["td_movies", "td_tv", "td_music"] and setup all the infrastructure you need for Saltbox to use them.

Don't change those names; they're referenced a few places below, so things will break if you change them.

## Google Project and Group Setup

There are two pieces that can't be scripted.

1. You will need to create a new project and generate a credential file:

    [Instructions here](../reference/google-project-setup.md)

2. You will need to create a Google Group to hold service accounts:

    [Instructions here](../reference/google-group-setup.md)

## `safire` Setup:

1. SSH into your server, then copy-paste these commands one by one, changing the ALL_CAPS BITS as appropriate:

    ```
    export g_group=INSERT_YOUR_GOOGLE_GROUP_ADDRESS
    cd /opt
    git clone https://github.com/88lex/safire
    cd safire
    python3 -m venv safire-venv
    safire-venv/bin/activate
    pip install -r requirements.yml
    mkdir -p /opt/sa/all
    mkdir -p ~/safire/creds
    prefix=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c6 ;)
    sed "s/project_prefix = \"\"/project_prefix = \"$prefix\"/" safire/default_config.py | sed "s/email_prefix = \".*\"/email_prefix = \"$prefix\"/" > ~/safire/config.py
    ```

1. Copy the credential JSON you downloaded earlier to `~/safire/creds/creds.json` on your server
   
    You can do this in a variety of ways; if you are running a linux-like system locally

    ```
    scp /LOCAL/PATH/TO/creds.json USER@DOMAIN.TLD:~/safire/creds/creds.json
    ```

    For example:
   
    ```
    scp /Users/nacl/Downloads/safire-credentials.json nacl@111.222.333.444:~/safire/creds/creds.json
    ``` 

2. Authorize safire

    ```
    cd /opt/safire/safire
    ./safire.py auth all
    ```

    You'll be walked through a process twice.  Each time:

        1. Don't use the local server
        2. Click the URL
        3. Sign into Google
        4. copy-paste the token into the terminal

3. Create three Shared Drives and store their IDs:

    ```
     eval $(./safire.py add drives td_movies td_tv td_music | awk -F' ' '{print "export " $4"="$6}')
    ```

    You'll see three errors during this; they can be ignored.

4. Create projects and SAs:

    ```
    ./safire.py add projects 3
    ./safire.py add sas
    ```

5. add all the generated SAs to the group you created earlier and give that group access to all the Shared Drives:

    ```
    ./safire.py add members $prefix $g_group
    ./safire.py add user $g_group td_
    ```

6. Download JSON files for all the generated SAs and copy them to a directory in `/opt`:

    ```
    ./safire.py add jsons
    rsync -av ~/safire/svcaccts/ /opt/sa/all
    ```

7. Create all the required rclone remotes.  The last remote is a union remote that will combine all three of these Shared Drives.

    ```
    rclone config create td_movies drive scope=drive service_account_file=/opt/sa/all/000150.json team_drive=$td_movies
    rclone config create td_music drive scope=drive service_account_file=/opt/sa/all/000150.json team_drive=$td_music
    rclone config create td_tv drive scope=drive service_account_file=/opt/sa/all/000150.json team_drive=$td_tv
    rclone config create google union upstreams="td_movies: td_music: td_tv:"
    ```

8. Finally create some mount files for use later with autoscan and the like.

    ```
    rclone touch td_movies:/movies.bin
    rclone touch td_tv:/tv.bin
    rclone touch td_music:/music.bin
    ```
