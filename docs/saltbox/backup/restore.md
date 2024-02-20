---
hide:
  - tags
tags:
  - restore
---

# Restore

???+ info
    Just like the initial install, these instructions are assuming you are running as `root` until told otherwise below.

## Dependencies

Start by installing dependencies.

=== "curl"

    ```shell
    curl -sL https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox
    ```

=== "wget"

    ```shell
    wget -qO- https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox
    ```

=== "curl (verbose)"

    ```shell
    curl -sL https://install.saltbox.dev | sudo -H bash -s -- -v; cd /srv/git/saltbox
    ```

=== "wget (verbose)"

    ```shell
    wget -qO- https://install.saltbox.dev | sudo -H bash -s -- -v; cd /srv/git/saltbox
    ```


## Configuration files

Next retrieve the configuration files from a backup by following the instructions below.  Note that the instructions are different if you used the restore service or not.

??? note "How do I know if this applies?  What's the "restore service"?"
    

    When you set up the backup, you may have entered values in these two fields in the backup config file:
        
    ```yaml
    ---
    backup:
    ...
    restore_service:
        user: SOMEUSERNAME
        pass: SOMEPASSWORD
    ```

    If you did so, you used the restore service.  If you didn't, you did not the restore service.

    If those values are provided, the saltbox backup stores encrypted copies of your config files on a saltbox-controlled server, so they can be retrieved and restored for you in this step.

    Those values would be things you made up.  Nobody but you knows what they are.  If you do not know them, or have misplaced them, you will have to proceed without the restore service.

=== "I used the Restore Service"

    === "curl"

        ```{ .sh .annotate }
        curl -sL https://restore.saltbox.dev | sudo bash -s 'USERNAME' 'PASSWORD' # (1)!
        ```

        1. Use the username and password defined for the service when last backup was executed.

            Must wrap the username and password in quotes.

    === "wget"

        ```{ .sh .annotate }
        wget -qO- https://restore.saltbox.dev | sudo bash -s 'USERNAME' 'PASSWORD' # (1)!
        ```

        1. Use the username and password defined for the service when last backup was executed.

            Must wrap the username and password in quotes.

=== "I did not use the Restore Service"

    Retrieve the following configuration files from your backup manually and place them in `/srv/git/saltbox`:

    * `accounts.yml`
    * `settings.yml`
    * `adv_settings.yml`
    * `backup_config.yml`
    * `providers.yml`
    * `hetzner_nfs.yml`
    * `rclone.conf`
    * `localhost.yml`

    !!! info
        Don't copy any other files; they will be dealt with in a couple minutes.

## Base Ansible config
To ensure that future ansible commands work correctly, copy the default config into place:
```
cp /srv/git/saltbox/defaults/ansible.cfg.default /srv/git/saltbox/ansible.cfg
```

## Settings
To insure that your configuration files are up to date run:
```shell
sb install settings
```

This will migrate any changes that may have been made to the current settings format if needed. Look over the files after this and adapt anything you want to change.

## Preinstall

Next run `preinstall` which will setup the user account and a few other dependencies for the restore.

```shell
sb install preinstall
```

Now log out of the `root` account and log in as the user defined in `accounts.yml`

This is important and should not be ignored:

**Now log out of the `root` account and log in as the user defined in `accounts.yml`**

## Backup files

The restore process expects that the backup tar archives will be accessible in either the rclone destination or the local destination as defined in `backup_config.yml`:

default contents:
```
---
backup:
  local:
    enable: true
    destination: /mnt/local/Backups/Saltbox
  rclone:
    enable: true
    destination: google:/Backups/Saltbox
...
```

=== "I want to pull the backup from the rclone location"

    You have just restored the rclone config files which contains the rclone remote mentioned in your `backup_config.yml`
    
    The only thing you need to ensure is that this machine can access that remote to copy files from it, and typically the only complication here is if you are using a service account to authenticate that remote.

    run:
    ```shell
    rclone lsd google:/Backups/Saltbox
    ```
    
    [where that path is the one in the rclone section of your `backup_config.yml`]
    
    You should see something like:
    ```shell
    $ rclone lsd google:/Backups/Saltbox
          -1 2023-03-16 19:26:19        -1 archived
          -1 2023-03-16 19:27:26        -1 opt
    ```
    if instead you see something like:
    ```shell
    $ rclone lsd google:/Backups/Saltbox
    2023/06/07 16:41:09 Failed to create file system for "google:/Backups/Saltbox": drive: failed when making oauth client: error opening service account credentials file...
    ```
    
    Then you are authenticating with a service account and will have to copy that service account file onto this machine to the location shown in the error.
    
    ???+ info
        If you are restoring from an rclone backup and you are using a service account to authenticate the rclone remote that holds the backup, you will need to put that SA JSON file in place manually so that the restore process can authenticate the remote to download the rest of the backup.

    ??? note "What's this about service accounts?"
        Open `rclone.conf` in a text editor and look through the remotes defined in there.

        If the remote you're using for the backup looks like this:

        ```text
        [SOME REMOTE]
        type = drive
        scope = drive
        service_account_file = /opt/sa/all/1500.json
        team_drive = OZZY
        root_folder_id =
        ```

        You will need to make sure that service account file [`/opt/sa/all/1500.json`] is available on the new saltbox machine at that same path in order to authenticate against google and download the backup files you're about to restore.

    Once `rclone lsd google:/Backups/Saltbox` shows you the expected `opt` directory, you are clear to continue.

=== "I want to pull the backup from the local location"

    You will need to make sure that the tar archives are available in `/mnt/local/Backups/Saltbox/opt` [or whatever path is specicfied in *your* `backup_config.yml` if you've changed it]:
    ```
    /mnt/local/Backups/Saltbox/
    ├── opt
    │   ├── authelia.tar
    │   ├── autoscan.tar
    ...
    ```
    If those files are not available at that local path or at the rclone location, the restore will not be able to find them.

    For example, with rclone disabled and nothing in `/mnt/local/Backups/Saltbox/opt`:
    ```
    fatal: [localhost]: FAILED! => {"changed": false, "msg": ["Rclone is not enabled and no local backup exists.", "You must either enable rclone, in the backup settings, or provide backup tarball files locally, to perform a restore."]}
    ```

    Copy your backup tar files from wherever they are now to that location.  Once you have done this and the backup tar archives are present in `/mnt/local/Backups/Saltbox/opt` [or whatever path *you* set that to], you are clear to continue.

## Restore

???+ info
    From this point you'll want to **make sure** you run commands as the user specified in the `accounts.yml`; this means you should log out and log back in as `seed` [or the user in `accounts.yml` if you changed it]

Start the restore process.

```shell
sb install restore
```

Saltbox will retrieve and extract the tar archives.

## Next Steps

Once successfully completed you can now continue:

If you are migrating from one server to another, return to the [migration guide](migrate.md)

If you are restoring to the same server, you can now follow the installation guide from this [step](../../saltbox/install/install.md#step-5-saltbox).
