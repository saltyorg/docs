## Cloudbox wasn't this complicated!

You're correct, it wasn't.

The rclone setup on Cloudbox was simpler primarily because it:

1. was all manual
2. only described connecting to My Drive
3. didn't use service accounts

Here's a table of steps showing how the two processes differ.

| Step  | Cloudbox                                         | Saltbox optional rclone setup                                          |
| ----- | ------------------------------------------------ | ---------------------------------------------------------------------- |
|  1.   |                                                  | Verify account shared-drive permissions                                |
|  2.   | Create base project                              | Create base project                                                    |
|  3.   | Grant permissions to base project                | Grant permissions to base project                                      |
|  3a.  | Google Drive API                                 | Google Drive API                                                       |
|  3b.  |                                                  | Admin SDK API [needed for steps 9 and/or 10]                           |
|  3c.  |                                                  | Identity and Access Management API [needed for steps 9 and/or 10]      |
|  3d.  |                                                  | Cloud Resource Manager API [needed for steps 9 and/or 10]              |
|  3e.  |                                                  | Service Usage API [needed for steps 9 and/or 10]                       |
|  3f.  |                                                  | Service Management API [needed for steps 9 and/or 10]                  |
|  3g.  |                                                  | Google Sheets API [needed for steps 9 and/or 10]                       |
|  4.   | Create OAuth Credentials                         | Create OAuth Credentials [needed for steps 9 and/or 10]                |
|  5.   |                                                  | Download Credentials JSON [needed for steps 9 and/or 10]               |
|  6.   | Create rclone remote with ID/Secret from Step 4  |                                                                        |
|  7.   |                                                  | Create Google Group [needed for steps 9 and/or 10]                     |
|  8.   |                                                  | Set up Google SDK [needed for steps 9 and/or 10]                       |
|  9.   |                                                  | Run a script to generate 300 service accounts                          |
| 10.   |                                                  | Run a script to create and configure shared drives and rclone remotes  |

Steps 9 and 10 are what require steps 1, 3b-3g, 5, 7, and 8.


