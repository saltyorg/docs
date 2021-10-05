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
