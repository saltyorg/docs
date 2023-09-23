# Migrating from Cloudbox to Saltbox

Saltbox is a continuation of the Cloudbox project and is mostly compatible out of the box. Very little has to be done to bring your old Cloudbox data into Saltbox. Any customisations you have made or special roles are going to require extra work as Saltbox uses Traefik instead of nginx.

IMPORTANT: Migration has the same requirements as a new install; Saltbox still expects a clean install of the OS; this means that you *cannot* upgrade an existing Cloudbox setup to Saltbox *in place*.  You will have to back up, reinstall the OS fresh on the machine, then start the migration.  Do not upgrade your Ubuntu 18.04 Cloudbox machine to Ubuntu 20.04 and try to run this migration.  It won't work.

## Before Migration

Backup from Cloudbox as you normally would. You will need to make the backup drive available to your new saltbox install via rclone just as you would with a Cloudbox restore. We are really only interested in keeping the data stored in `/opt` and not the Cloudbox configuration files. We will be using the data from the configuration files so you may find it handy to download those locally to use as a reference. If you have community containers set up you should make a copy of those files as well. We are more interested in the data stored in these files so it is perfectly fine to just copy and paste the information into a text file for your reference as part of the installation process.

- **Cloudbox files to keep handy (these files should be found in `~/cloudbox/`):**

  ``` yaml

  accounts.yml

  ```

  You may need to decrypt your `accounts.yml` file if you used the encryption option. Do this before you shut down or wipe your old server.

  ``` yaml

  adv_settings.yml
  ansible.cfg
  backup_config.yml

  ```

  If you are using a service account to authenticate your rclone backup remote, you will need to put that service account file in place on the saltbox server before you run the restore.
  
  This trips people up frequently, so it bears repeating:

  If you are using a service account to authenticate your rclone backup remote, you will need to put that service account file in place on the saltbox server before you run the restore.

  This warning applies **specifically and only** to the rclone remote from which you are going to retrieve your cloudbox backup; if that one is authenticated with a client ID/secret and others are authenticated with a service account, this does not apply.
  
  If you don't understand what this means, ask on the Discord before you attempt this migration; doing so will save you a failure that will drive you to the Discord anyway.

- **Community files to keep handy (these files should be found in `/opt/community/`):**

  ``` yaml
  ansible.cfg
  hetzner_nfs.yml
  settings.yml
  telly.yml
  ```

- **Rclone configuration file**

  The rclone.conf file located in `~/.config/rclone/rclone.conf` if your configuration uses service accounts to authenticate the remotes you will need make sure the service accounts are accessible. <br />

  ``` yaml

  rclone.conf

  ```

  <details>
  <summary>What's this about service accounts?</summary>
  <br />

  On your cloudbox machine, run:

  ```shell
  rclone config show REMOTENAME
  ```

  Using an SA:

  ```text
  ➜  ~ rclone config show REMOTE
  [REMOTE]
  type = drive
  scope = drive
  service_account_file = /opt/sa/all/1500.json
  team_drive = OZZY
  root_folder_id =
  ```

  Using clientid:

  ```text
  ➜  ~ rclone config show REMOTE:
  [REMOTE]
  type = drive
  client_id = OZZY.apps.googleusercontent.com
  client_secret = TONY
  server_side_across_configs = true
  scope = drive
  token = {"access_token":"GEEZER","token_type":"Bearer","refresh_token":"BILL","expiry":"2022-04-30T17:37:41.485179628-05:00"}
  root_folder_id = RONNIE
  ```

  If the rclone remote contains `service_account_file`, you will need to make sure that service account file is available on the saltbox machine at that same path.
  </details>

## Migration

IMPORTANT: Migration has the same requirements as a new install; Saltbox still expects a clean install of the OS; this means that you *cannot* upgrade an existing Cloudbox setup to Saltbox *in place*.  You will have to back up, reinstall the OS fresh on the machine, then start the migration.  Do not upgrade your Ubuntu 18.04 Cloudbox machine to Ubuntu 20.04 and try to run this migration.  It won't work.

Do not proceed unless the machine you're using is a fresh install of Ubuntu 20.04 or 22.04.

- Install the saltbox dependencies

  ``` shell

  curl -sL https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox

  ```

- Copy `rclone.conf` to `/srv/git/saltbox` <Br/> and edit the configuration files as needed. You can follow the [saltbox install instructions for saltbox for this](../../saltbox/install/install.md)<Br/>
  
  Saltbox is going to move this file into the correct location; you're putting it here only so saltbox knows where to find it.

  You can refer to your Cloudbox configuration files and copy relevant settings over from them, but do not just copy your existing Cloudbox config files into place.  Direct compatibility with Cloudbox config files is not guaranteed and will not be maintained going forward.

IMPORTANT: DO NOT use your cloudbox configuration files.  You can copy and paste individual values [values like your plex username and token, not sections like the entire plex section] from your cloudbox files, but DO NOT use the originals.  Things have moved from file to file compared to Cloudbox, there are new values that are required, there are values that have been deprecated.  Work on the new default settings files and edit them using your cloudbox files as a reference.

- Run the preinstall command.

  This step will create the specified user account, add it to sudoers, update the kernel, edit GRUB configuration, install Rclone, and reboot the server if needed. <br />

  ``` shell

    sb install preinstall

  ```

- switch to the newly created user specified in your configuration. <br />

- If you are restoring a Cloudbox backup, you should change the default rclone backup path in `/srv/git/saltbox/backup_config.yml` to point to your Cloudbox backup.  Once you've done this initial restore, change it back to the location of your choice.

  ```yaml
  ---
  backup:
  ...
    rclone:
      enable: true
      destination: google:/Backups/Saltbox               <<<  THIS ONE HERE
   ...
  ```

- run the restore command. <br />

  ``` shell

    sb install restore

  ```

  Remember that if you use a service account file to authenticate an rclone remote, you need to manually put that file into place before running the restore.

  If you still use the legacy /data, /tv or /movies docker volumes you will want to set this using the [inventory](../../saltbox/inventory/index.md)
  ```yaml
  docker_legacy_volume: true
  ```

  Then you should be able to install tags as you want.

- install top-level tag [as appropriate] <br />
  
  Note: These are options, not a list of commands to run.

  ``` shell

    sb install saltbox

  ```
  ``` shell

    sb install feederbox

  ```
  ``` shell

    sb install mediabox

  ```
  At a minimum [if you don't want all the apps that those tags install] you need to run:

  ``` shell

    sb install core

  ```

- install individual tags [if required] <br />

  ``` shell

    sb install emby

  ```

- install sandbox tags [if required] <br />

  ``` shell

    sb install sandbox-nextcloud

  ```
As with a Cloudbox restore, any non-standard service files will be present in `/opt/service-files`, but you will need to copy them into `/etc/systemd/system`, then activate and start them.  If you used the "tip44" method for adding teamdrives, for example, you'll need to do this.
