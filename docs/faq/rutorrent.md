---
hide:
  - tags
tags:
  - rutorrent
  - faq
---

# ruTorrent

IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## Change ruTorrent download path after installation

1. Stop ruTorrent Docker container:

   ```shell
   docker stop rutorrent
   ```

1. Edit the `rtorrent.rc` file:

   ```shell
   nano /opt/rutorrent/rtorrent/rtorrent.rc
   ```

1. Set the following options:

   ```ini
   directory = /downloads/rutorrent
   ```

1. Start ruTorrent Docker container:

   ```shell
   docker restart rutorrent
   ```

## Enable access to public torrent trackers

By default access to DHT, UDP, and PEX are disabled since most private trackers (and some server providers) do not allow this. Attempting to add a torrent from a public tracker would result in the torrent being stuck, like this:

![](../images/faq/rutorrent-01.png)

To enable access to public trackers, do the following:

1. Stop ruTorrent Docker container:

   ```shell
   docker stop rutorrent
   ```

2. Edit the `rtorrent.rc` file:

   ```shell
   nano /opt/rutorrent/rtorrent/rtorrent.rc
   ```

3. Set the following options:

   ```ini
   dht.mode.set = on
   ```

   ```ini
   trackers.use_udp.set = yes
   ```

   ```ini
   protocol.pex.set = yes
   ```

4. Start ruTorrent Docker container:

   ```shell
   docker start rutorrent
   ```
