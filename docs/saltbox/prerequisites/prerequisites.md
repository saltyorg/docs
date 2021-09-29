## Presumptions
Saltbox presumes you have a basic understanding of Linux, Docker containers, BitTorrent, and Usenet, and are also familiar with Sonarr, Radarr, NZBGet, rTorrent/ruTorrent, and Plex/Emby.

The Saltbox setup is all done on the command line in the linux shell.  There is no GUI and there are no plans to add one.  If you want to run Saltbox, you *will* need to be familiar with Linux.

The guides in this wiki are only meant to setup Saltbox specific settings into the various apps that are installed with Saltbox (e.g. Sonarr, Radarr, Plex, etc) and are not meant to be a full setup for, or an introduction to, the workings of these apps. However, you may pickup a few things as you go thru the guides. 

If you wish to learn more about them in detail, you can easily find a ton of guides for them online (e.g. [HTPC Guides](https://www.htpcguides.com){target=_blank}, [YouTube](https://www.youtube.com){target=_blank}, etc).

## Server
### Getting a Server

Some points below:

- You will need a dedicated server, from a server provider (e.g. Hetzner, kimsufi, OVH, etc), installed with Ubuntu Server [20.04](https://releases.ubuntu.com/20.04/).

- Best results are seen with an actual dedicated server, not a VPS like those available from Linode, Vultr, or the like.  Linodes, Vultr "Cloud Compute", Hetzner "Cloud Servers", and probably others like them, in particular, are known to _not_ work in at least one significant way; NZBGet reports 0 available disk space while Sonarr, Radarr, and tools like `df` and `du` report disk space as expected.

- You will need root access to install Saltbox.

- Server should be a completely fresh OS install. Do not try to install any dependencies on your own, Saltbox will do that for you. 

- Saltbox only supports x64 (i.e. Intel or AMD 64) machines. ARM based hardware [such as the Raspberry Pi] is not supported.

- Get a server with at least 100GB+ of hard disk space. Even though media is uploaded to the cloud, there is still a need local storage for things like app data and backups. 

  Practically, you should have more like 500GB of space available _at a minimum_.

  Cloudplow's default folder size threshold, to upload media to the cloud, is set at 200GB. To lower that, you'll need to go [here](../../apps/cloudplow.md){target=_blank}

  If you are planning to use Usenet, SSD should be considered required, and NVME highly recommended.  Usenet is extremely disk I/O intensive.

  If you are planning to use torrents, you should have much more disk space than that available for seeding.  Your seeding torrents will not be moved to your cloud storage; they will consume local disk space as long as they are seeding. 

  If you are installing as a Feederbox/Mediabox setup rather than the all-in-one Saltbox, the disk requirements change a bit. Downloading drives disk requirements on the Feederbox [as discussed above] and primarily the Plex/Emby metadata drives the disk requirements on the Mediabox.  Depending on the size of your library, that metadata can be quite large.

-  If you are setting this up on a home server, verify, **before installing Saltbox**:
   1. Make sure your ISP doesn't block ports 80 and 443 [if your ISP blocks these ports, it won't work.]
   1. Make sure that your router supports hairpin NAT [if this isn't supported, you won't be able to access apps via subdomain from inside your network]
   1. Open the relevant [ports](../../reference/ports.md){target=_blank} (eg `80`, `443`, etc) in your [router](https://portforward.com/router.htm)/firewall and forward them to the IP of the box on which you want to install Saltbox, **before installing Saltbox**.
   1. Point your domain at your home IP and configure some dynamic DNS software to keep it updated.  Saltbox has a dynamic dns client available [it's not installed by default], but there are many ways to set this up.  Make sure that DNS has propagated and your domain returns your home IP via `ping` or something like it, **before installing Saltbox**.

### Tips

#### Ubuntu 20.04

- If you get an option like below, select choose `ubuntu-2004-focal-64-minimal`.

  ![fix me - new image](https://i.imgur.com/DcZAAWM.png)

- Install OpenSSH server if asked. 

#### Partitioning:
- If you have multiple hard drives on the server (eg. 2 x 4 TB), put them in RAID 0 to maximize space and speed (you don't need redundancy as you can schedule backups of Saltbox).

- Set all available space to `/` (remove `/home` and `/data` partitions).

- Leave ample space in `/boot` (e.g. 2+ GB).

- putting the `/opt` directory on a `btrfs` partition can dramatically reduce the amount of time your containers are down during backup.

- Examples

   - Online.net

     ![](../../images/online-net-partitioning.png)

   - OVH

     ![](../../images/ovh-partitioning.png)

     ![](../../images/ovh-partitioning2.png)

   - Hetzner installimage
     ``` bash
     # Hetzner Online GmbH - installimage
     #
     # This file contains the configuration used to install this
     # system via installimage script. Comments have been removed.
     #
     # More information about the installimage script and
     # automatic installations can be found in our wiki:
     #
     # http://wiki.hetzner.de/index.php/Installimage
     #
     
     DRIVE1 /dev/nvme0n1
     DRIVE2 /dev/nvme1n1
     SWRAID 1
     SWRAIDLEVEL 0
     HOSTNAME sb.domain.com
     PART /boot  ext4     512M
     PART lvm    vg0       all
     LV vg0   swap   swap      swap         8G
     LV vg0   root    /     ext4      all
     IMAGE /root/.oldroot/nfs/install/../images/Ubuntu-2004-focal-64-minimal.tar.gz
     ```

   - Hetzner installimage (with a separate 250G partition for `/opt` utilizing BTRFS for snapshot backups)

     ``` bash
     # Hetzner Online GmbH - installimage
     #
     # This file contains the configuration used to install this
     # system via installimage script. Comments have been removed.
     #
     # More information about the installimage script and
     # automatic installations can be found in our wiki:
     #
     # http://wiki.hetzner.de/index.php/Installimage
     #
     
     DRIVE1 /dev/nvme0n1
     DRIVE2 /dev/nvme1n1
     SWRAID 1
     SWRAIDLEVEL 0
     HOSTNAME sb.domain.com
     PART /boot  ext4     512M
     PART lvm    vg0       all
     LV vg0   swap   swap      swap         8G
     LV vg0   opt   /opt     btrfs         250G
     LV vg0   root    /     ext4      all
     IMAGE /root/.oldroot/nfs/install/../images/Ubuntu-2004-focal-64-minimal.tar.gz
     ```


## Domain Name

## Cloudflare

## Cloud Storage

## Plex or Emby Account

## Usenet vs Bittorrent

