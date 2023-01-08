# Hetzner & Google IPv6

From time to time Hetzner seems to have problems with IPv6 routing to Google so these are ways you can work around that problem.

## Disable IPv6 Temporarily

```bash
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1
```

## Disable IPv6 permanently

Add the following to `/etc/sysctl.conf`

```text
net.ipv6.conf.all.disable_ipv6=1
net.ipv6.conf.default.disable_ipv6=1
net.ipv6.conf.lo.disable_ipv6=1
```

Then run

```shell
sudo sysctl -p
```

Alternately you can disable IPv6 using GRUB by editing `/etc/default/grub` and adding the following to `GRUB_CMDLINE_LINUX_DEFAULT` and `GRUB_CMDLINE_LINUX`

```text
ipv6.disable=1
```

External resource: [here](https://itsfoss.com/disable-ipv6-ubuntu-linux/)

## Make Rclone use IPv4

For the mount this is done by toggling ipv4_only in `/srv/git/saltbox/adv_settings.yml` like so:

```yaml
mounts:
  remote: rclone_vfs
  ipv4_only: yes
  feeder: no
```

Then run

```shell
sb install mounts_override
```

For Cloudplow you could add something like:

```json
            "rclone_extras": {
                "--user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                "--checkers": 16,
                "--drive-chunk-size": "128M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1,
                "--skip-links": null,
                "--retries": 1,
                "--low-level-retries": 2,
                "--drive-stop-on-upload-limit": null,
                "--bind": "<Insert Your WAN IP>"
            },
```

For crop you would add the following to the global params that you are utilizing:

```yaml
- '--bind=<Insert Your WAN IP>'
```

After doing any changes to Cloudplow or crop configuration remember to restart their respective service.

## Use a script to bind traffic to Google API endpoints to a specific IP

Setup this [script](https://github.com/Nebarik/mediscripts-shared/blob/main/googleapis.sh) and let it modify your hosts file.

[Markschrik](https://github.com/markschrik) has created a version of the script that will do the required setup for you if you are using the default Saltbox setup; it can be found [here](https://raw.githubusercontent.com/markschrik/Saltbox-GoogleBandwith/main/bandwithtest.sh).  Download it, mark it executable, and run it.

```bash
wget https://raw.githubusercontent.com/markschrik/Saltbox-GoogleBandwith/main/bandwithtest.sh
chmod +x bandwithtest.sh
./bandwithtest.sh
```

You can also add this to your crontab to execute it automatically.
