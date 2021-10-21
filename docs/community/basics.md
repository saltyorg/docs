# Basics

The [Saltbox Community](https://github.com/saltyorg/Community){: target=_blank rel="noopener noreferrer" } repository is installed with [Saltbox](https://github.com/saltyorg/Saltbox){: target=_blank rel="noopener noreferrer" } as part of a standard install. The Saltbox Community application installers are provided and maintained by the community but subject to approval. The applications are not part of a standard Saltbox install, but they are tested and confirmed to be compatible with the Saltbox ecosystem.

Community Guides are written by the community to help others make the most of their system.

### Update

To update Saltbox Community run a standard saltbox update and both community and saltbox will be updated

``` shell

sb update

```

To force update Saltbox Community settings.yml file run:

``` shell

sb install cm-settings

```

### How to Install Community Apps

For most apps it is as simple as running the `sb install` command in a shell followed by the name of the role. For example, to install a jellyfin server you would run the jellyfin role:-

``` shell

sb install cm-jellyfin

```
Before running any role you should first carefully read through the docs to see if there are any additional steps or pre configuration settings required.

A list of roles can be called from the terminaL via:-

```shell

sb cm-list

```


### Contributing to Community Apps
