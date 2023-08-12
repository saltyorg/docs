# Rclone

## Rclone error: Failed to save config file: open /home/\<user\>/.config/rclone/rclone.conf: permission denied

Replace `user` and `group` to match yours (see [here](System.md#find-your-user-id-uid-and-group-id-gid)).

```shell
sudo chown -R user:group ~/.config/rclone/
sudo chmod -R 0755 ~/.config/rclone/
```
