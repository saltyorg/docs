# Migrating from arbitrary setups to Saltbox

If you are coming from some other similar system, perhaps something you set up manually, you may be able to migrate to saltbox without too much trouble, but it's not practical to provide detailed documentation on what you might need to do.

Here are some general notes on things you will probably need to address.  This article will describe what saltbox needs, but it will be up to you to determine how to get from where you are now to Saltbox.

## Rclone

Saltbox assumes that your cloud storage is accessible through an rclone remote called `google`.  The saltbox setup describes creating Google projects and so forth to support this, but if you already have this running somewhere, you have already done all that and can just use what you have.

In the rclone install step, copy your `rclone.conf` into place at `/home/seed/.config/rclone/rclone.conf` [substitute `seed` with your username if you've changed that].  If you are using service accounts to authenticate your rclone remote[s], copy them to the appropriate location.

If your cloud storage remote is not called `google`, you can either rename it, or change the `remote` in settings.yml:

```yml
rclone:
  version: latest
  remote: google    ## << HERE
```

## Paths

Saltbox is assuming that your media is stored in particular [paths](../../saltbox/basics/paths.md) on your cloud storage.  Changing those paths is not trivial, so you will be best served to nove your media to match the expected folder hierarchy.

## Application Data

You may be able to import the data from your various applications, depending on the versions of the applications that generated it and perhaps the specific containers.

You will need to address paths, most likely.  There are a variety of ways to do this.

Saltbox stores application data in the `/opt` directory.
