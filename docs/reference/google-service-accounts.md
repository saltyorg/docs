This guide will show you how to create projects and service accounts using `sa-gen` and add them to a Google Group.

It's assuming you're working through the steps from [here](rclone-manual.md).

NOTE: This guide is assuming a Google Gsuite Business/Workspace account.

1. Make sure /opt/sa is writable by you.

    ```
    sudo chown -R <user>:<group> /opt/sa
    ```

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

2. You're done.
