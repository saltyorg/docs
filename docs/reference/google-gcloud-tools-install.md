This guide will show you how to set up a Google SDK tools.

It's assuming you're working through the steps from [here](rclone-manual.md) and have already created the required [project](google-project-setup.md) and [group](google-group-setup.md).

Simplified extract from [here](https://cloud.google.com/sdk/docs/quickstart#deb):

1. Run the following commands, one at a time:

    ```
    sudo apt-get install apt-transport-https ca-certificates gnupg
    ```
    ```
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    ```
    ```
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
    ```
    ```
    sudo apt-get update && sudo apt-get install google-cloud-sdk -y
    ```

1. Run the following command:

    ```
    gcloud init
    ```
   
    Follow the prompts:

    ```
    Welcome! This command will take you through the configuration of gcloud.

    ...

    You must log in to continue. Would you like to log in (Y/n)?  Y

    Go to the following link in your browser:

    https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=32...X4&code_challenge_method=S256
    ```
1. Log into your Google account and approve the access request:
   
    ![](../images/gcloud-sdk/02-sdk-approve.png)

    Copy the verification code.

1. Continue in the terminal:

    ```
    Enter verification code: 4/1AX4XfWjkg8C8r...ujs332G8
    You are logged in as: [YOUR_GOOGLE_ACCOUNT].
    ```
    
    You will now be asked to choose a default project.  Choose the one you created earlier.

    ```
    Pick cloud project to use:
     [1] THE_PROJECT_YOUR_CREATED_FOR_SALTBOX
     [2] Create a new project
    Please enter numeric choice or text value (must exactly match list item):  1

    Your current project has been set to: [THE_PROJECT_YOUR_CREATED_FOR_SALTBOX].
    ```

    You may be asked to choose a default zone/region.  If so, you can choose the closest to you, but since we are not creating any location-specific objects, you can skip that.
    
1. Google SDK is installed and configured.

