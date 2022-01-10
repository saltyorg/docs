# Migrating from Cloudbox to Saltbox

Saltbox is a continuation of the Cloudbox project and is mostly compatible out of the box. Very little has to be done to bring your old Cloudbox data into Saltbox. Any customisations you have made or special roles are going to require extra work as Saltbox uses Traefik instead of nginx.

## Before Migration

Backup from Cloudbox as you normally would. You will need to make the backup drive available to your new saltbox install via rclone just as you would with a Cloudbox restore. We are really only interested in keeping the data stored in `/opt` and not the Cloudbox configuration files. We will be using the data from the configuration files so you may find it handy to download those locally to use as a reference. If you have community containers set up you should make a copy of those files as well. We are more interested in the data stored in these files so it is perfectly fine to just copy and paste the information into a text file for your reference as part of the installation process.

-  **Cloudbox files to keep handy: <br />**
    **These files should be found in `~/cloudbox/`**

    ``` { .yaml }

      accounts.yml

    ```

       You may need to decrypt your `accounts.yml` file if you used the encryption option. Do this before you shut down or wipe your old server.

    ``` { .yaml }

      adv_settings.yml
      ansible.cfg
      backup_config.yml

    ```

    If you are using a service account to authenticate your rclone remote[s], you will need to put those files in place on the saltbox server before you run the restore.
    
- **Community files to keep handy: <br />**
  **These files should be found in `/opt/community/`**

    ``` { .yaml }

      ansible.cfg
      hetzner_nfs.yml
      settings.yml
      telly.yml

    ```

- **Rclone configuration file**
    The rclone.conf file located in `~/.config/rclone/rclone.conf` if your configuration uses service accounts to authenticate the remotes you will need make sure the service accounts are accessible. <br />

    ``` { .yaml }

      rclone.conf

    ```

## Migration

- Install the saltbox dependencies <br />

    ``` { .shell }

    curl -sL https://install.saltbox.dev | sudo -H bash; cd /srv/git/saltbox

    ```

- Copy `rclone.conf` to `/srv/git/saltbox` <Br/>
  and edit the configuration files as needed you can follow the [saltbox install instructions for saltbox for this](../../saltbox/install/install.md)<Br/>

- Run the preinstall command, this step will create the specified user account, add it to sudoers, update the kernel, edit GRUB configuration, install Rclone, and reboot the server if needed. <br />

    ``` { .shell }

      sb install preinstall`

    ```

- switch to the newly created user specified in your configuration. <br />

    ``` { .shell }

      sb install restore

    ```

    Remember that if you use a service account file to authenticate an rclone remote, you need to manually put that file into place before running the restore.
    
    Then you should be able to install tags as you want.
