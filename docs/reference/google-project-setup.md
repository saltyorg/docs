This guide will show you how to set up a Google Project and create credentials that will work for sa-gen or similar tools.

It's assuming you're working through the steps from [here](rclone-manual.md) and have completed the following steps:

- verified [account drive permissions](google-account-perms.md)

This guide is assuming you are using a standard GSuite Business or GSuite Workspace account.

IF YOU HAVE DONE THIS BEFORE IN ANY OTHER CONTEXT [CLOUDBOX, PTS, ETC.], THERE IS NO REASON TO REPEAT IT.  You only need one of these projects.

1. Open Google APIs Console site: <https://console.developers.google.com> and login with your Google account.

    Click on the project or organization at the top:

    ![](../images/gdrive-project/01-dashboard.png)

2. Click "New Project":

    ![](../images/gdrive-project/02-new-project.png)

3. Name the project. Click "Create".

    ![](../images/gdrive-project/03-name-project.png)

    You'll see a progress dialog, when it's complete, click "Select Project"

    ![](../images/gdrive-project/04-progress.png)

4. Click "Go to APIs overview".

    ![](../images/gdrive-project/05-project-dash.png)

5. Click "ENABLE APIS AND SERVICES" at the top.

    ![](../images/gdrive-project/06-api-overview.png)

    You'll be taken to the "API Library":

    ![](../images/gdrive-project/07-API-library.png)

6. Search for "Admin". Click "Admin SDK API".

    ![](../images/gdrive-project/08-admin-sdk.png)

    Click the button to enable the API:

    ![](../images/gdrive-project/09-admin-enable.png)

    You'll go to a API Overview page.  Click the browser back button twice:

    ![](../images/gdrive-project/10-admin-enabled.png)

    Repeat this process for six more APIs:

        - Google Drive API
        - Identity and Access Management (IAM) API
        - Cloud Resource Manager API
        - Service Usage API
        - Service Management API
        - Google Sheets API

    You may find that some of these APIs have been enabled already as dependencies of others, like Service Management here:

    ![](../images/gdrive-project/16-service-management-enabled-already.png)

    In that case, click the website back arrow once and move on to the next one.

7. Now click "APIS and Services" then "Credentials" in the left column to go to the credentials dash:

    ![](../images/gdrive-project/17-credentials-sidebar.png)

8. Click "Configure consent screen" over on the right:

    ![](../images/gdrive-project/18-credentials-dash.png)

9. Choose "External" user type and click "Create":

    ![](../images/gdrive-project/19-consent-user-type.png)

10. On this screen:
    1. type in the App Name (e.g. Rclone)
    2. Enter a "User support email"
    3. Scroll to the bottom
    4. Enter an email address under "Developer contact information"
    5. Click "SAVE AND CONTINUE".

    ![](../images/gdrive-project/20-consent-app-name.png)

    ![](../images/gdrive-project/21-consent-app-name-bottom.png)

11. Click  "SAVE AND CONTINUE" on the scopes screen:

    ![](../images/gdrive-project/22-consent-scopes.png)

    And "BACK TO DASHBOARD" on the final summary:

    ![](../images/gdrive-project/23-consent-last.png)

12. Click  "SAVE AND CONTINUE" on the test users screen:

    ![](../images/gdrive-project/225-test-users.png)

    And "BACK TO DASHBOARD" on the final summary:

    ![](../images/gdrive-project/23-consent-last.png)

13. Click "PUBLISH APP" on the dashboard :

    ![](../images/gdrive-project/235-publish-app.png)

    Then "CONFIRM":

    ![](../images/gdrive-project/237-confirm.png)

14. Click "Credentials" in the sidebar:

    ![](../images/gdrive-project/24-consent-dash.png)

15. Click "Create Credentials", then "OAuth client ID":

    ![](../images/gdrive-project/25-credentials-dropdown.png)

16. Choose "Desktop App", give the app a name, and click "CREATE":

    ![](../images/gdrive-project/26-credentials-type-name.png)

17. You'll be presented with the Client ID and Secret.  Copy and save them somewhere; you may need them to configure other tools later.  Click on "DOWNLOAD JSON" to download the credential file:

    ![](../images/gdrive-project/27-credentials-done.png)

Later on, I'm going to assume you put it on the saltbox server in `/opt/sa/` and named it `project-creds.json`.
    
To do that you may need to create `/opt/sa` and make sure it's writable by you.

<details>
<summary>How do I do that?</summary>
```
sudo mkdir -p /opt/sa
sudo chown -R <user>:<group> /opt/sa
```
Where the two placeholders are the Saltbox user and group [by default `seed:seed`]
<br />
</details>

If you are going through the manual rclone instructions, [continue with the next step](rclone-manual.md#step-3-create-a-google-group-to-hold-service-accounts)
