Saltbox defaults to using service accounts for uploading to multiple teamdrives to allow for future growth.

To make the setup more straightforward, this guide will leverage `safire` to generate as much infrastructure as possible.

This will set up three Shared Drives ["sb_movies", "sb_tv", "sb_music"] and setup all the infrastructure you need for Saltbox to use them.

Don't change those names; they're referenced a few places below, so things will break if you change them.

## Google Project and Group Setup

There are two pieces that can't be scripted.

1. You will need to create a new project and generate a credential file:

    [Instructions here](../reference/google-project-setup.md)

2. You will need to create a Google Group to hold service accounts:

    [Instructions here](../reference/google-group-setup.md)

## `safire` Setup:

1. SSH into your server, then copy-paste these commands one by one:

    ```
    curl -fLvO https://gist.githubusercontent.com/chazlarson/63e2dfb274a3e3178fb88485fe62943f/raw/ecb9edd3f4ba355cb5c058ca615259a82e602a2e/sb_gd.sh
    chmod +x sb_gd.sh
    ./sb_gd.sh
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

1. Run the script again.

    You will be prompted to authenticate to google and copy-paste a token twice at the beginning.
    
    ```
    ./sb_gd.sh
    ```

1. You should now have three new shared drives ready for use with Saltbox.

