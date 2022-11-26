# SAFire

Saltbox defaults to using service accounts for uploading to multiple teamdrives to allow for future growth.

To make the setup more straightforward, this guide will leverage `safire` to generate as much infrastructure as possible.

This will set up three Shared Drives and set up all the infrastructure you need for Saltbox to use them.

If you're here, you probably want to go [here](rclone-manual.md) instead.  `safire` has been acting inconsistently.

## This script is a work in progress; it probably has rough edges

## Assumptions and defaults

1. You have rclone installed

2. You are running python 3.8 and have run `sudo apt install python3.8-venv -y`
   Probably other python3 works, the assumption is that the script can create a venv

3. The script will generate a random prefix and use this for the shared drives, service accounts, and projects.

4. Default is to generate three shared drives:

   |  Drive            |  media dir        |
   |:-----------------:|:-----------------:|
   |  [PREFIX]_Movies  |  `/Media/Movies`  |
   |  [PREFIX]_Music   |  `/Media/Music`   |
   |  [PREFIX]_TV      |  `/Media/TV`      |

   This can be modified with a config file.  The first half of the script will display the details.

5. Default is to generate three projects with 100 service accounts each.  This can be modified at the beginning of the script itself.

   There are a couple other user settings at the beginning of the script.

## Google Project and Group Setup

There are two pieces that can't be scripted.

1. You will need to create a new project and generate a credential file:

    [Instructions here](../reference/google-project-setup.md)

2. You will need to create a Google Group to hold service accounts:

    [Instructions here](../reference/google-group-setup.md)

## `safire` Setup

1. SSH into your server, then copy-paste these commands one by one:

    ```shell
    curl -fLvO https://raw.githubusercontent.com/chazlarson/sb_gd/main/sb_gd.sh
    chmod +x sb_gd.sh
    ./sb_gd.sh
    ```

1. Copy the credential JSON you downloaded earlier to `~/safire/creds/creds.json` on your server
  
    You can do this in a variety of ways; if you are running a linux-like system locally

    ```shell
    scp /LOCAL/PATH/TO/creds.json USER@DOMAIN.TLD:~/safire/creds/creds.json
    ```

    For example:

    ```shell
    scp /Users/nacl/Downloads/safire-credentials.json nacl@111.222.333.444:~/safire/creds/creds.json
    ```

1. Run the script again.

    You will be prompted to authenticate to google and copy-paste a token [this will happen twice].

    If you didn't enter your google group email address into the script, you will be asked for it.

    ```shell
    ./sb_gd.sh
    ```

1. You should now have three new shared drives ready for use with Saltbox.
