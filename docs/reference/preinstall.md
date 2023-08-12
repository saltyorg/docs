!!! warning
    This is a reference discussing an aspect of the [install process](../saltbox/install/install.md#preinstall).
    If you are looking for the steps to follow to install, they are [here](../saltbox/install/install.md).

## Preinstall

!!! warning
    Make sure that you have setup the configuration correctly before proceeding.

This step will create the specified user account, add it to sudoers, update the kernel, edit GRUB configuration and install Rclone and reboot the server if needed.

``` shell
sb install preinstall
```

!!! info
    From this point you'll want to make sure you run commands as the user specified in the accounts.yml

If your server did not need to reboot you can run `su username` to switch user or reconnect to SSH as the newly created user. Everything after this point will assume you are running as the user entered in accounts.yml
