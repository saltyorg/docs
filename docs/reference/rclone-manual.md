---
hide:
  - tags
tags:
  - rclone
  - scripted
---

# Rclone Manual

<script>
   document$.subscribe(function() {
    var length           = 10;
    var result           = '';
    var characters       = 'abcdefghijklmnopqrstuvwxyz';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() *
 charactersLength));
   }
   var paragraph = document.getElementById("prefix");

   paragraph.textContent = result;

});

</script>

[Rclone](https://rclone.org) (by Nick Craig-Wood) is "rsync for the cloud". Basically, it is used to transfer data to or from a variety of supported cloud storage providers (eg Google Drive).

Rclone is used by [Cloudplow](cloudplow.md) and [Backup](modules/backup.md) to upload media and backup Saltbox, respectively.

The guide below assumes you are using Google Drive.

Further, it is assuming you are starting from nothing; a new Google account with no existing media on Google Drive.

!!! info
    IMPORTANT: This guide was written *before* Google began cracking down on storage usage on workspace accounts; it's assuming that you have effectively unlimited storage. Now that this is not the case, you should evaluate whether you actually need or want to go through this for little to no benefit generally.

    This process creates 300 service accounts and multiple Google projects to enable you to upload more than 750Gb per day; now that the total storage available to workspace accounts is in the tens of TB, this is not as important or useful as it used to be.

    This process creates multiple shared drives to help you avoid hitting file-count limitations; again, now that the total storage available to workspace accounts is in the tens of TB, this is not as important or useful as it used to be, as you're unlikely to have hundreds of thousands of files.

    Take the time to consider whether this process holds value for you.

THIS PROCESS IS OPTIONAL. THIS IS NOT A REQUIRED PART OF THE SALTBOX INSTALL.

IF YOU ARE USING A BACKEND OTHER THAN GOOGLE DRIVE (say, Dropbox), THIS DOES NOT APPLY TO YOU.

Rclone supports many cloud provider backends, but the only one routinely used by the Saltbox team is Google Drive.

This process will use various scripts to do as much of this for you as possible, but there are some things that can't be scripted easily, like steps 1 and 2 below.

It also assumes you are using a [Google Workspace](https://workspace.google.com/) account, since it assumes you can create shared drives. You can do some of this without a Workspace account, but the differences are not documented here. You won't be able to directly follow the steps below, and most of the scripts won't work for you.

!!! warning
    IF YOU ARE HERE TO DO THIS A SECOND TIME, RETHINK THAT. IF YOU SUCCESSFULLY RAN THROUGH THIS PROCESS ONCE, YOU HAVE EVERYTHING YOU NEED TO SET SALTBOX UP AND SHOULD REUSE THOSE SHARED DRIVES, SERVICE ACCOUNTS, AND GROUP. THERE'S NO REASON TO CREATE A SECOND SET USING THE SAME GOOGLE ACCOUNT.

If you already have Rclone configured, you can jump directly to the [relevant section](#existing-rclone-setup).

If you already have media on Google Drive (My Drive OR Shared Drives) from your time with Cloudbox or the like, you DO NOT WANT TO DO THIS. This process is assuming you are starting from scratch without any of this already set up. It will overwrite aspects of an existing rclone setup with no undo.

That said, let's proceed.

## New Rclone Setup

!!! warning
    YOU CANNOT SKIP STEPS HERE: EACH OF THESE STEPS IS ASSUMING YOU HAVE PERFORMED THE PREVIOUS ONE.

!!! info
    IF YOU HAVE EXISTING GOOGLE DRIVES FROM ANOTHER CONTEXT (Cloudbox, PG, etc) USE THAT CONFIG (NOTABLY THE RCLONE CONFIG AND ANY SERVICE ACCOUNTS) IN A MIGRATION.

!!! warning
    THIS PROCESS DOES NOT ACCOUNT FOR USING YOUR OWN TEAMDRIVES.

### Step 1: Verify that the Shared Drive permissions are correct on your Google account

[Detailed instructions here](google-account-perms.md)

### Step 2: Create a new project and generate a credential file

[Detailed instructions here](google-project-setup.md)

Save that credential file on your server at `/opt/sa/project-creds.json`. You may need to create `/opt/sa` and make sure it's writable by you.

<details>
<summary>How do I do that?</summary>
```
sudo mkdir -p /opt/sa
sudo chown -R <user>:<group> /opt/sa
```
Where the two placeholders are the Saltbox user and group (by default `seed:seed`)
<br />
</details>

### Step 3: Create a Google Group to hold service accounts

[Detailed instructions here](google-group-setup.md)

### Step 4: Set up the GCloud SDK

[Detailed instructions here](google-gcloud-tools-install.md)

### Step 5: Generate a random prefix

Your randomly-generated prefix is:

<p id="prefix">10 RANDOM CHARACTERS SHOULD APPEAR HERE</p>

<details>
<summary>That says '10 RANDOM CHARACTERS SHOULD APPEAR HERE'</summary>
<br />
Apparently the Javascript didn't work or you have Javascript disabled.

Try reloading the page. If that doesn't work, generate it manually:

[Type this at a command prompt on your server]

```shell
prefix=$(head /dev/urandom | tr -dc a-z | head -c10 ;) && echo $prefix
```

</details>

Make a note of that prefix; you will use it in the next two steps.

!!! info
    There is nothing special about that prefix; it is ten random characters. It's not tied to *you* literally. When you reload this page, the prefix will change. That's fine. The specific prefix doesn't matter; just pick one and use it.

<details>
<summary>Why do I need this?</summary>
<br />
This prefix is used for two purposes:<br /><br />

  1. Project names need to be unique across all of Google; a random prefix helps ensure this (the error that results in this case is non-obvious).<br /><br />

  2. It helps these scripts unambiguously identify things that they have created, so they don't affect any projects, service accounts, or drives you may already have created.

</details>

### Step 6: Generate 300 service accounts

[Detailed instructions here](google-service-accounts.md)

### Step 7: Create Shared Drives and related infrastructure

[Detailed instructions here](google-shared-drives.md)

### Step 8: Verify that the union remote shows you the expected contents

!!! warning
    IF YOU HAVE SKIPPED ANY OF THE PREVIOUS STEPS THIS VALIDATION WILL NOT WORK.

```shell
rclone tree google:/
```

This should display something like (the number and names of the files and folders may vary somewhat depending on your config):

```text
/
├── -- aZaSjsklaj-Movies Shared --
├── -- aZaSjsklaj-Music Shared --
├── -- aZaSjsklaj-TV Shared --
├── Media
│   ├── Movies
│   ├── Music
│   └── TV
├── azasjsklaj-movies_mounted.bin
├── azasjsklaj-music_mounted.bin
└── azasjsklaj-tv_mounted.bin

7 directories, 3 files
```

<details>
<summary>What if I don't see that?</summary>
<br />
If you see an error like this:

```text
Failed to tree: 3 errors: aZaSjsklaj-Movies: failed to get Shared Drive info: googleapi: Error 404: Shared drive not found: BINGBANGBOING, notFound; aZaSjsklaj-Music: failed to get Shared Drive info: googleapi: Error 404: Shared drive not found: BANGBOINGBING, notFound; aZaSjsklaj-TV: failed to get Shared Drive info: googleapi: Error 404: Shared drive not found: BOINGBINGBANG, notFound
```

The most likely cause is that something went wrong in the group setup. Perhaps all the service accounts didn't get added to the group.
Repeat the last part of [this step](google-group-setup.md) where you upload the members.csv and verify that the group shows at least 300 members after you're done.

</details>

You now have shared drives and and a union combining them; the saltbox install will merge this with your local drive and cloudplow will upload to the union remote, which will distribute media to the shared drives by path.

## After the Final Rose

US-centric trash-TV reference aside, there is one thing you may wish to do after the saltbox install is complete.

The "saltbox install" is the full installation of saltbox using `sb install saltbox` or the like, not the process you just completed above.

You will still be limited to the 750GB/day Google upload limit until you configure cloudplow to upload directly to the individual shared drives. Eventually this will be automated, but for now there is [this guide](cloudplow-config.md). The script described there operates on the default cloudplow config file, which does not exist yet if you are going through this for the first time.

For now, go [back to the install process](../saltbox/install/install.md#step-5-saltbox).

## Existing Rclone Setup

The default remote specified in [settings.yml](accounts.md) is `google` for Google Drive. If the Rclone remote in your config has the same name, then you are OK to skip this page and go on to the next.

If you are using Google Drive and the Rclone remote in your config has a different name, then you will need to either:

- Rename your current Rclone remote to the default one (i.e. `google`). Instructions for this are below.

  Or

- Edit the Rclone remote entry in [settings.yml](accounts.md) to reflect yours.

If you prefer to use another cloud storage provider, you can add the name of the Rclone remote in to [settings.yml](accounts.md).

### Rename Existing Rclone Remote

To rename the Google Drive remote to `google`:

1. Find and edit your Rclone configuration file.

   ```shell
   nano $(rclone config file | tail -n 1)
   ```

1. Rename the Google Drive drive remote (name between the brackets) to `google`.

1. It will now look like this:

   ```ini
   [google]
   type = drive
   client_id = JOHNNY.apps.googleusercontent.com
   client_secret = JOEY
   token = {"access_token":"ya30.DEEDEE-38ikRIxZvimyoxyKdse$
   ```

1. Save the file and exit: <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd>.

1. Copy the config file to `~/.config/rclone/rclone.conf` (if it isn't there already):

   ```shell
   cp -n $(rclone config file | tail -n 1) ~/.config/rclone/rclone.conf
   ```

1. Give it the proper ownership and permissions. Replace `user` and `group` to match yours (see [here](../faq/system.md#find-your-user-id-uid-and-group-id-gid)):

   ```shell
   sudo chown user:group ~/.config/rclone/rclone.conf
   sudo chmod 755 ~/.config/rclone/rclone.conf
   ```
