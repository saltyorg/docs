# System

## Can I install this on an ARM machine?

No. ARM is not supported.

## Find your User ID (UID) and Group ID (GID)

Use the following commands to find out your account's user name and group info:

```shell
id
```

or

```shell
id `whoami`
```

You'll see a line like the following:

```text
uid=XXXX(yourusername) gid=XXXX(yourgroup) groups=XXXX(yourgroup)
```

## How to create a user account

- Run the following commands line by line:

   ```bash
   sudo useradd -m <username>
   sudo usermod -aG sudo <username>
   sudo passwd <username>
   sudo chsh -s /bin/bash <username>
   su <username>
   ```

## Change shell of user account to bash

The generally correcct way to do this is to change the setting and run `sb install shell`

If you want to do this outside the saltbox context, carry on.

How to check current shell:

```shell
echo $0
-sh
```

or

```shell
echo ${SHELL}
/bin/sh
```

Run this command to set bash as your shell (where `<user>` is replaced with your username):

```shell
sudo chsh -s /bin/bash <user>
sudo reboot
```

## How to fix permission issues

 /opt folder

1. Stop all docker containers

   ```shell
   docker stop $(docker ps -a -q)
   ```

2. Change ownership of /opt. Replace `user` and `group` to match yours' (see [here](System.md#find-your-user-id-uid-and-group-id-gid)).

   ```shell
   sudo chown -R user:group /opt
   ```

3. Change permission inheritance of /opt.

   ```shell
   sudo chmod -R ugo+X /opt
   ```

4. Start all docker containers

   ```shell
   docker start $(docker ps -a -q)
   ```

 /mnt folder

1. Run the `mounts` tag

   ```shell
   sb install mounts
   ```
