## Rclone
This step will take you through the configuration of Rclone.

This is the same process as you went through with [Cloudbox](https://github.com/Cloudbox/Cloudbox/wiki/Install%3A-Rclone).

If you're migrating from Cloudbox you probably want the [Cloudbox migrations instructions](https://docs.saltbox.dev/community/guides/cloudbox/)

THe manual steps that the script below will try to perform:
1. Create a [Google project](https://docs.saltbox.dev/reference/google-project-setup/)
1. Create a [Google group](https://docs.saltbox.dev/reference/google-group-setup/)
1. Create a bunch of service accounts
1. Put all the service accounts JSON files into `/opt/sa`
1. Add all those service accounts to the Google group you just created.
1. Create three new shared drives in the Google Drive UI. [Movies, Music, TV]
1. Add your Google Group to each of those drives as a "Manager"
1. Create rclone remotes pointing to each of those shared drives, authenticated using one of those service files.
1. Create a `union` rclone remote called "google", with the components set to the three td remotes you just created.

With Saltbox we want to set up multiple teamdrives and service accounts form the get-go, with as few manual steps as possible.

That process is still under construction.  Please take a look at the [automated version of this process](../reference/safire.md).
