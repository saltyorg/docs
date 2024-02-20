---
hide:
  - tags
tags:
  - cloudbox
  - cloud
---

## Cloudbox wasn't this complicated!

You're correct, it wasn't.

The rclone setup on Cloudbox was simpler primarily because it:

1. was all manual
2. only described connecting to My Drive
3. didn't use service accounts

Here's a table of ways in which the two processes differ.  Note that these "steps" are unique to this table; they aren't intended to match any other list of steps.

| Step  | Cloudbox                                         | Saltbox optional rclone setup                                          |
| ----- | ------------------------------------------------ | ---------------------------------------------------------------------- |
|  1.   |                                                  | Verify account shared-drive permissions                                |
|  2.   | Create base project                              | Create base project                                                    |
|  3.   | Grant permissions to base project                | Grant permissions to base project                                      |
|  3a.  | Google Drive API                                 | Google Drive API                                                       |
|  3b.  |                                                  | Admin SDK API                                                          |
|  3c.  |                                                  | Identity and Access Management API                                     |
|  3d.  |                                                  | Cloud Resource Manager API                                             |
|  3e.  |                                                  | Service Usage API                                                      |
|  3f.  |                                                  | Service Management API                                                 |
|  3g.  |                                                  | Google Sheets API                                                      |
|  4.   | Create OAuth Credentials                         | Create OAuth Credentials                                               |
|  5.   |                                                  | Download Credentials JSON                                              |
|  6.   | Create rclone remote with ID/Secret from Step 4  |                                                                        |
|  7.   |                                                  | Create Google Group                                                    |
|  8.   |                                                  | Set up Google SDK                                                      |
|  9.   |                                                  | Run a script to generate 300 service accounts                          |
| 10.   |                                                  | Add those 300 service accounts to the group from step 7                |
| 11.   |                                                  | Run a script to create and configure shared drives and rclone remotes  |

The scripts in 9 and 11 use the Google SDK, which is what drives all the extra permissions.


