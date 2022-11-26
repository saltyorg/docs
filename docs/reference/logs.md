# Apps

## Autoscan

### Check Status

```
sudo systemctl status autoscan.service
```

### Restart Service

```
sudo systemctl restart autoscan.service
```

### Previous Activity

```
cat /opt/autoscan/activity.log
```

### Live Log

```
tail -F /opt/autoscan/activity.log
```

## Cloudplow

### Check Status

```
sudo systemctl status cloudplow.service
```

### Previous Activity

```
cat /opt/cloudplow/cloudplow.log
```

Older logs are named as cloudplow.log.1, cloudplow.log.2, etc.

### Live Log

```
tail -F /opt/cloudplow/cloudplow.log
```

or

```
sudo journalctl -o cat -fu cloudplow.service
```

Sometimes, debug-level logging can be useful.  To enable this, make this change in the service file and restart the service.

In this file: `/etc/systemd/system/cloudplow.service`, change the log level to "DEBUG":

```
...
WorkingDirectory=/opt/cloudplow/
ExecStart=/usr/bin/python3 /opt/cloudplow/cloudplow.py run --loglevel=DEBUG  <<<<< RIGHT THERE
ExecStopPost=/bin/rm -rf /opt/cloudplow/locks
Restart=always
...
```

You should only enable debug logging while you need it to track down a problem.

# Remote Mount

Pick one of these.

## Rclone VFS

### Check Status

```
sudo systemctl status rclone_vfs.service
```

### See a live log

```
sudo journalctl -o cat -fu rclone_vfs.service
```

## Rclone Cache

### Check Status

```
sudo systemctl status rclone_cache.service
```

### See a live log

```
sudo journalctl -o cat -fu rclone_cache.service
```

# Union Mount

### Check Status

```
sudo systemctl status mergerfs.service
```

### See a live log

```
sudo journalctl -o cat -fu mergerfs.service
```

# Docker

Find the container name: `docker ps -a`

## Live logs

### Live log (from the beginning of the log)

```
docker logs --follow <container_name>
```

### Live log (from the last 10 lines of the log)

```
docker logs --follow --tail 10 <container_name>
```

### Examples

```
docker logs -f plex
```

Note: `--follow` = `-f`
