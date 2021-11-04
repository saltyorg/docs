# Basics

The [Saltbox Community](https://github.com/saltyorg/Community){: target=_blank rel="noopener noreferrer" } repository is installed with [Saltbox](https://github.com/saltyorg/Saltbox){: target=_blank rel="noopener noreferrer" } as part of a standard install. The Saltbox Community application installers are provided and maintained by the community but subject to approval. The applications are not part of a standard Saltbox install, but they are tested and confirmed to be compatible with the Saltbox ecosystem.

Community Guides are written by the community to help others make the most of their system.

### Update

To update Saltbox Community run a standard saltbox update and both community and Saltbox will be updated

``` shell

sb update

```

To force update Saltbox Community settings.yml file run:

``` shell

sb install cm-settings

```

### How to Install Community Apps

For most apps it is as simple as running the `sb install` command in a shell with a `cm-` prefix followed by the name of the role.

``` shell

sb install cm-rolename

```

For example, to install a jellyfin server you would run the jellyfin role:-

``` shell

sb install cm-jellyfin

```
Before running any role you should first carefully read through the docs to see if there are any additional steps or pre configuration settings required.

A list of all roles available to Saltbox can be called from the terminal via:-

```shell

sb list

```

!!! Tip
    Where possible the configured username/password are taken from your Saltbox [`accounts.yml`](../../../saltbox/install/install/#configuration) file located in `/srv/git/saltbox/accounts.yml` and used to create a default user an password for logging in.


### Contributing to Community Apps
