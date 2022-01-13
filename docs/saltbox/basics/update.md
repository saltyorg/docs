# Update

To update Saltbox run:

``` shell

sb update

```

This will also upgrade Ansible as needed and migrate the configuration files as additional options are added over time.

This updates the saltbox files *only*;  It *does not* update your containers.

For example, if a new feature is added to saltbox, `sb update` will get that new feature.  If a new version of Radarr is available, `sb update` *will not* update your Radarr to that new version.

Next, let's discuss how you will [access the applications](accessing_apps.md).
