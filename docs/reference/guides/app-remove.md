# App Removal

Perhaps you want to remove one of the apps that Saltbox installed for you.

Maybe you're not planning to ever use qbittorrent, or you want to install it fresh, or some other reason.

This page describes doing this for something that was installed as a docker container.

## THIS MAY DESTROY DATA; BACK UP FIRST IF YOU ARE UNSURE WHAT YOU'RE DOING

First, stop and remove the docker container:

```shell
docker stop CONTAINER_NAME
docker rm CONTAINER_NAME
```

At this point, the container has been removed; it's not longer running, no longer consuming CPU or RAM resources.

Its configuration is still on disk in `/opt`, however.

If you reinstall using the standard saltbox install mechanism, it will come back up with your existing configuration.

If you want to remove that configuration for whatever reason [will never use it, want to start fresh, etc.]:

```shell
rm -fr /opt/CONTAINER_NAME
```

Now it's as if that app was never installed on this machine.

Now you can reinstall the container using the standard saltbox tag:

```shell
sb install TAG_GOES_HERE
```

This will create a brand new `/opt/CONTAINERNAME`

The same concepts apply to sandbox apps.

If you're not planning to reinstall and want to save a tiny bit of disk space [or you want to be sure you pull a new image when you reinstall]:

```shell
docker image prune
```

That will delete the local copy of the image used to create the now-deleted container.
