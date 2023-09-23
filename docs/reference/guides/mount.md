# Mounting a disk persistently on your saltbox server

Perhaps you want to mount a disk partition persistently in the file system like a media drive at `/mnt/local/Media` or a fast SSD for usenet at `/mnt/local/downloads`.

## Gathering details

First find out the device reference:

```shell
lsblk
```

this will display something like:
```
/srv/git/saltbox$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                    8:0    0 12.7T  0 disk
└─sda1                 8:1    0 12.7T  0 part
sr0                   11:0    1 1024M  0 rom
nvme0n1              259:0    0  1.8T  0 disk
├─nvme0n1p1          259:1    0  512M  0 part /boot/efi
├─nvme0n1p2          259:2    0    1G  0 part /boot
└─nvme0n1p3          259:3    0  1.8T  0 part
  └─ubuntu--vg-lv--0 253:0    0  1.8T  0 lvm  /
```
I want to mount that 12.7T partition, `sda1`.

Now let's get the UUID of that partition:

```shell
sudo blkid
```

That will display something like:
```shell
/srv/git/saltbox$ sudo blkid
[sudo] password for seed:
/dev/nvme0n1p3: UUID="Br73Mj-1hiQ-DpPX-7rwb-Q2E1-4Rdb-HQBezw" TYPE="LVM2_member" PARTUUID="a5ed9aed-da7f-43ad-b1a2-c9b35017e00a"
/dev/nvme0n1p1: UUID="5524-9590" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="af869940-c4de-4562-844d-2a46bd8c5680"
/dev/nvme0n1p2: UUID="ecc24163-8465-4983-9676-7d85f9cdb31a" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="aff553a3-ad14-4d7c-8e08-7c6d87e59429"
/dev/mapper/ubuntu--vg-lv--0: UUID="1956420b-8d19-4573-abdf-10126ede727c" BLOCK_SIZE="4096" TYPE="ext4"
/dev/sda1: UUID="9d4c3257-8e05-4228-b970-15ddbc99e86f" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="cf6ca88f-498f-3f41-86bd-e891de24466c"
```

We can see the UUID and filesystem of that device in the table:

```
/dev/sda1: 
UUID="9d4c3257-8e05-4228-b970-15ddbc99e86f" 
...
TYPE="ext4"
...
```

## Editing `fstab` file for persistent mount.

Now you need to edit the `fstab` file, which controls what gets mounted at system startup.

```shell
sudo nano /etc/fstab
```

You want to add a line to the bottom of that file. Don't edit anything in the file already.

In my case I want to mount that 12.7T partition at `/mnt/hdd`.

The line you need to add should look something like this (details may differ):

```
/dev/disk/by-uuid/9d4c3257-8e05-4228-b970-15ddbc99e86f /mnt/hdd ext4 defaults  0      2
                  |                                    |        └ format from blkid output
                  |                                    └ directory where you want to mount this partition
                  └ UUID from blkid output
```

In my case, `/etc/fstab` starts looking like this:

```
/srv/git/saltbox$ cat /etc/fstab
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/ubuntu-vg/lv-0 during curtin installation
/dev/disk/by-id/dm-uuid-LVM-087oBvV8gi2gDtJZBPmc0owcPXPdkpzTdwtdNt8jU3SNavox61p3nyq1gfaIRzz0 / ext4 defaults 0 1
# /boot was on /dev/nvme0n1p2 during curtin installation
/dev/disk/by-uuid/ecc24163-8465-4983-9676-7d85f9cdb31a /boot ext4 defaults 0 1
# /boot/efi was on /dev/nvme0n1p1 during curtin installation
/dev/disk/by-uuid/5524-9590 /boot/efi vfat defaults 0 1
/swap.img	none	swap	sw	0	0
```

And I add one line at the end so it looks like this:
```
/srv/git/saltbox$ cat /etc/fstab
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/ubuntu-vg/lv-0 during curtin installation
/dev/disk/by-id/dm-uuid-LVM-087oBvV8gi2gDtJZBPmc0owcPXPdkpzTdwtdNt8jU3SNavox61p3nyq1gfaIRzz0 / ext4 defaults 0 1
# /boot was on /dev/nvme0n1p2 during curtin installation
/dev/disk/by-uuid/ecc24163-8465-4983-9676-7d85f9cdb31a /boot ext4 defaults 0 1
# /boot/efi was on /dev/nvme0n1p1 during curtin installation
/dev/disk/by-uuid/5524-9590 /boot/efi vfat defaults 0 1
/swap.img	none	swap	sw	0	0
/dev/disk/by-uuid/9d4c3257-8e05-4228-b970-15ddbc99e86f /mnt/hdd ext4 defaults  0      2
```

Then save the file.

Now go create the directory and set the ownership:

```shell
/srv/git/saltbox$ sudo mkdir /mnt/hdd
/srv/git/saltbox$ sudo chown -R seed:seed /mnt/hdd
```
[assuming you are using the saltbox default `seed` user]

Then mount the partition:
```shell
/srv/git/saltbox$ sudo mount -a
```

That command produces no output if it succeeds.

You can verify that the disk was mounted with `df`:

```shell
/srv/git/saltbox$ df -h
```

```shell
/srv/git/saltbox$ df -h
Filesystem                    Size  Used Avail Use% Mounted on
tmpfs                         1.6G  1.7M  1.6G   1% /run
/dev/mapper/ubuntu--vg-lv--0  1.8T  8.5G  1.7T   1% /
tmpfs                         7.8G     0  7.8G   0% /dev/shm
tmpfs                         5.0M     0  5.0M   0% /run/lock
/dev/nvme0n1p2                974M  224M  683M  25% /boot
/dev/nvme0n1p1                511M  6.1M  505M   2% /boot/efi
tmpfs                         1.6G  4.0K  1.6G   1% /run/user/1000
/dev/sda1                      13T   11T  1.4T  89% /mnt/hdd
```

There it is at the end of the list.

That partition will now be mounted there at system startup automatically.

If you compare the lsblk output *now* to waht it was:

```shell
/srv/git/saltbox$ lsblk
NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                    8:0    0 12.7T  0 disk
└─sda1                 8:1    0 12.7T  0 part /mnt/hdd
sr0                   11:0    1 1024M  0 rom
nvme0n1              259:0    0  1.8T  0 disk
├─nvme0n1p1          259:1    0  512M  0 part /boot/efi
├─nvme0n1p2          259:2    0    1G  0 part /boot
└─nvme0n1p3          259:3    0  1.8T  0 part
  └─ubuntu--vg-lv--0 253:0    0  1.8T  0 lvm  /
```

You can see that the `sda1` device now has a mountpoint listed in the last column.
