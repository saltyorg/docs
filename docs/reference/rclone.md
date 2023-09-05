This will take you through the configuration of Rclone from a standing start with nothing set up already.

If you're migrating from Cloudbox you probably want the [Cloudbox migration instructions](https://docs.saltbox.dev/reference/guides/cloudbox/)

If you have an existing rclone setup from Cloudbox or PTS or something else you should NOT go through this process.  You should reuse that existing setup.  There is nothing saltbox specific about this setup aside from the various paths, and you do not need new projects or service accounts or shared drives to address that.

If you are not using Google Drive you should NOT go through this process.

If you are reinstalling saltbox there is no reason to do this again provided you have run a Saltbox backup or followed the instructions the first time you did this and have backed up the important files.

!!! warning
    Changes to Google's "unlimited" offering have made this process largely needless.  New Google accounts no longer come with enough storage to have the sort of limits that this setup is intended to address.


<details>
<summary>Overview of what this process is going to do</summary>
<br />

This process is going to perform, with your assistance, these tasks:<br /><br />

Note that this is a general overview of the things that are going to happen, not a list of instructions for you to follow.<br /><br />

1. Create a Google project<br /><br />

2. Create a Google group<br /><br />

3. Create 300 service accounts<br /><br />

4. Add those 300 service accounts to the Google group that was just created.<br /><br />

5. Create 3 new shared drives.<br /><br />

6. Add your Google Group to each of those drives as a "Manager"<br /><br />

7. Create rclone remotes pointing to each of those shared drives, authenticated using one of those service files.<br /><br />

8. Create a `union` rclone remote called "google", with the components set to the shared drive remotes you just created.<br /><br />

</details>

### Instructions

[Start here](rclone-manual.md).
