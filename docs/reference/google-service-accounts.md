This guide will show you how to create projects and service accounts using `sa-gen` and add them to a Google Group.

It's assuming you're working through the steps from [here](rclone-manual.md), have already created the required [project](google-project-setup.md), have already created the required [group](google-group-setup.md), and have installed the [gcloud SDK tools](google-gcloud-tools-install.md).

NOTE: This guide is assuming a Google Gsuite Business/Workspace account.

1. Make sure /opt/sa is writable by you.

    ```
    sudo chown -R <user>:<group> /opt/sa
    ```
    
    Enter the user from `accounts.yml`; group is the same as the user.

1. Retrieve the `sa-gen` code

    ```
    git clone https://github.com/88lex/sa-gen && cd sa-gen
    ```

1. Edit the `sa-gan` script:

    ```
    nano sa-gen
    ```

    Edit the beginning of the script as indicated by `<<<<` below:

    ```
    #!/bin/bash
    # Running this script requires gcloud command line tools. To install go to https://cloud.google.com/sdk/docs/quickstarts
    # See readme.md to understand the variables used in this script

    KEYS_DIR=/opt/sa/all   <<<<
    ORGANIZATION_ID=""     <<<<
    GROUP_NAME="mygroup@mydomain.com"   <<<< the group you created previously
    PROJECT_BASE_NAME="mgbtbnfkkt"  <<<< the prefix you generated previously
    FIRST_PROJECT_NUM=1
    LAST_PROJECT_NUM=3
    SA_EMAIL_BASE_NAME="mgbtbnfkkt"  <<<< the prefix you generated previously
    FIRST_SA_NUM=1
    NUM_SAS_PER_PROJECT=100
    ...
    ```

1. Run the `sa-gan` script:

    ```
    ./sa-gen
    ```

    `sa-gen` will create three projects, 300 SAs, and download them to `/opt/sa/all`:


    ```
    Total SA json keys before running sa-gen = 0
    Creating project = mgbtbnfkkt1
    ++ gcloud projects create mgbtbnfkkt1 --organization=
    Create in progress for [https://cloudresourcemanager.googleapis.com/v1/projects/mgbtbnfkkt1].
    Waiting for [operations/cp.5950654100828535641] to finish...done.
    Enabling service [cloudapis.googleapis.com] on project [mgbtbnfkkt1]...
    Operation "operations/acf.p2-672393700722-9443eda2-69db-46a9-8952-5cdaa3b6ed2f" finished successfully.
    ++ set +x
    ...
    Total SA json keys BEFORE running sa-gen = 0
    Total SA json keys AFTER running sa-gen  = 300
    Total SA jsons CREATED                   = 300
    ```
2. Download the `members.csv` file that sa-gen created next to the service account files to your local computer using sftp or whatever other means.

    ![](../images/google-service-account/01-all-members.png)
 
1. Open the Google Admin site: https://admin.google.com/ and login with your Google account.  Click on the groups heading:
   
    ![](../images/google-service-account/02-admin-top-level.png)

1. Click on your group:
   
    ![](../images/google-service-account/03-group-list.png)

2. Click on "BULK UPLOAD MEMBERS":
   
    ![](../images/google-service-account/04-bulk-upload.png)

3. Click on "ATTACH CSV", and find the `members.csv` you downloaded a moment ago:
   
    ![](../images/google-service-account/05-select-CSV.png)

4. Click "UPLOAD".  Status will appear in the upper right:
   
    ![](../images/google-service-account/06-choose-csv.png)

5. You're done.
