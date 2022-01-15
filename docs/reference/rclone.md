## Rclone
This step will take you through the configuration of Rclone.

If you're migrating from Cloudbox you probably want the [Cloudbox migrations instructions](https://docs.saltbox.dev/community/guides/cloudbox/)

### Overview

The steps that need to be done to set up rclone are:

1. Create a Google project

1. Create a Google group

1. Create a bunch of service accounts

1. Put all the service accounts JSON files into `/opt/sa`

1. Add all those service accounts to the Google group you just created.

1. Create three new shared drives in the Google Drive UI. [Movies, Music, TV]

1. Add your Google Group to each of those drives as a "Manager"

1. Create rclone remotes pointing to each of those shared drives, authenticated using one of those service files.

1. Create a `union` rclone remote called "google", with the components set to the three td remotes you just created.

### Instructions:

With Saltbox we ultimately want to mnake this process as automatic as it can be, but that software is still under construction.  

For now, please follow this [partially scripted version of this process](rclone-manual.md).
