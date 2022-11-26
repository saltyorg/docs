# Update

## Updating Saltbox

To update Saltbox run:

``` shell

sb update

```

This will also upgrade Ansible as needed and migrate the configuration files as additional options are added over time.

This updates the saltbox files *only*;  It *does not* update your containers.

For example, if a new feature is added to saltbox, `sb update` will get that new feature.  If a new version of Radarr is available, `sb update` *will not* update your Radarr to that new version.

## Updating apps

Generally, to update individual applications, run the tag for that application.  For example,

``` shell

sb install radarr

```

This will retrieve the current version of the radarr image and recreate the container, which will update the application version.

The same thing happens if you run one of the top-level tags:

``` shell

sb install saltbox

```

This will do as above for *all* the containers installed by the `saltbox` tag.

Next, let's discuss how you will [access the applications](accessing_apps.md).
