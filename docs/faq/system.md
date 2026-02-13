---
hide:
  - tags
tags:
  - system
  - faq
  - arm
---

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

   ```shell
   sudo useradd -m <username>
   sudo usermod -aG sudo <username>
   sudo passwd <username>
   sudo chsh -s /bin/bash <username>
   su <username>
   ```

## Change shell of user account to bash

The generally correct way to do this is to change the setting and run `sb install shell`

If you want to do this outside the Saltbox context, carry on.

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

```shell
sb install fix-permissions
```

This will set permissions on `/mnt/local`, `/opt` and `/home/<user>` (where `<user>` is replaced with your username) to match saltbox' requirements and expectations.

If you have installed software that requires unusual permissions within any of these locations, you will need to restore those permissions yourself, as required.
