This guide will show you how to set up a Google Project and create credentials that will work for safire or sa-gen or similar tools.

It's assuming you're working through the steps from [here](rclone-manual.md).

This guide is assuming you are using a standard GSuite Business or GSuite Workspace account.

1. Open Google APIs Console site: https://console.developers.google.com and login with your Google account.

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

9. Choose "Internal" user type and click "Create":

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

12. Click "Credentials" in the sidebar:

    ![](../images/gdrive-project/24-consent-dash.png)

13. Click "Create Credentials", then "OAuth client ID":

    ![](../images/gdrive-project/25-credentials-dropdown.png)

14. Choose "Desktop App", give the app a name, and click "CREATE":

    ![](../images/gdrive-project/26-credentials-type-name.png)

15. You'll be presented with the Client ID and Secret.  Copy and save them if you like.  Click on "DOWNLOAD JSON" to download the credential file:

    ![](../images/gdrive-project/27-credentials-done.png)

If you are going through the manual rclone instructions, [continue with the next step](rclone-manual#new-rclone-setup)
