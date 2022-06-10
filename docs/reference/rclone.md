## Rclone
This step will take you through the configuration of Rclone from a standing start with nothing set up already.

If you're migrating from Cloudbox you probably want the [Cloudbox migration instructions](https://docs.saltbox.dev/reference/guides/cloudbox/)

If you have an existing rclone setup from Cloudbox or PTS or something else you should NOT go through this process.  You should reuse that existing setup.  There is nothing saltbox specific about this setup aside from the various paths, and you do not need new projects or service accounts or shared drives to address that.

### Overview

The steps that need to be done to set up rclone are:

Note that this is a general overview of the things that have to happen, not a list of instructions  Paths and names referenced in this list are must examples.  Please refer to the actual instructions further down for specifics.

1. Create a Google project

1. Create a Google group

1. Create a bunch of service accounts

1. Put all the service accounts JSON files into some directory where all relevant software can see them.

1. Add all those service accounts to the Google group you just created.

2. Create new shared drives in the Google Drive UI.

3. Add your Google Group to each of those drives as a "Manager"

4. Create rclone remotes pointing to each of those shared drives, authenticated using one of those service files.

5. Create a `union` rclone remote called "google", with the components set to the shared drive remotes you just created.

### Instructions:

[Automated](rclone-auto.md).

[Partially scripted](rclone-manual.md).
