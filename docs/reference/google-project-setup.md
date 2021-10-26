This guide will show you how to set up a Google Project and create credentials that will work for safire.

This guide is assuming you are using a standard GSuite Business or GSuite Workspace account.

1. Open Google APIs Console site: https://console.developers.google.com and login with your Google account.

    Click on the project or organization at the top:

    ![](https://i.ibb.co/yhJMgnk/01-dashboard.png)

2. Click "New Project":

    ![](https://i.ibb.co/C19NJRJ/02-new-project.png)

3. Name the project. Click "Create".

    ![](https://i.ibb.co/LPqQsqX/03-name-project.png)

    You'll see a progress dialog, when it's complete, click "Select Project"

    ![](https://i.ibb.co/7XM68zT/04-progress.png)
    
4. Click "Go to APIs overview".

    ![](https://i.ibb.co/fpFyP0p/05-project-dash.png)

5. Click "ENABLE APIS AND SERVICES" at the top.

    ![](https://i.ibb.co/xC86WQ2/06-api-overview.png)

    You'll be taken to the "API Library":

    ![](https://i.ibb.co/kKC554k/07-API-library.png)

6. Search for "Admin". Click "Admin SDK API".

    ![](https://i.ibb.co/kBCmqgG/08-admin-sdk.png)

    Click the button to enable the API:

    ![](https://i.ibb.co/KzwsZVx/09-admin-enable.png)

    You'll go to a API Overview page.  Click the browser back button twice:

    ![](https://i.ibb.co/N9CMJVf/10-admin-enabled.png)

    Repeat this process for six more APIs:
    
        - Google Drive API
        - Identity and Access Management (IAM) API
        - Cloud Resource Manager API
        - Service Usage API
        - Service Management API
        - Google Sheets API

    You may find that some of these APIs have been enabled already as dependencies of others, like Service Management here:

    ![](https://i.ibb.co/28PSwdd/16-service-management-enabled-already.png)
    
    In that case, click the website back arrow once and move on to the next one.

7. Now click "APIS and Services" then "Credentials" in the left column to go to the credentials dash:

    ![](https://i.ibb.co/vztHtfv/17-credentials-sidebar.png)

8. Click "Configure consent screen" over on the right:
   
    ![](https://i.ibb.co/4d5dfPj/18-credentials-dash.png)

9. Choose "Internal" user type and click "Create":
   
    ![](https://i.ibb.co/QNJ5dpP/19-consent-user-type.png)

10. On this screen:
    1. type in the App Name (e.g. Rclone)
    2. Enter a "User support email"
    3. Scroll to the bottom
    4. Enter an email address under "Developer contact information"
    5. Click "SAVE AND CONTINUE".
   
    ![](https://i.ibb.co/sF2wG3c/20-consent-app-name.png)

    ![](https://i.ibb.co/vq9SDmY/21-concent-app-name-bottom.png)

11. Click  "SAVE AND CONTINUE" on the scopes screen:
   
    ![](https://i.ibb.co/Mndqdrm/22-consent-scopes.png)

    And "BACK TO DASHBOARD" on the final summary:
   
    ![](https://i.ibb.co/VgcsyjH/23-concent-last.png)

12. Click "Credentials" in the sidebar:
   
    ![](https://i.ibb.co/L1SxccM/24-concent-dash.png)

13. Click "Create Credentials", then "OAuth client ID":
   
    ![](https://i.ibb.co/k8PgzbZ/25-credentials-dropdown.png)

14. Choose "Desktop App", give the app a name, and click "CREATE":
   
    ![](https://i.ibb.co/8xLLyy6/26-credentials-type-name.png)

15. You'll be presented with the Client ID and Secret.  Copy and save them if you like.  Click on "DOWNLOAD JSON" to download the credential file:
   
    ![](https://i.ibb.co/WFbr8b1/27-credentials-done.png)
