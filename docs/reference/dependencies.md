!!! warning
    This is a reference discussing an aspect of the [install process](../saltbox/install/install.md#step-1-dependencies).
    If you are looking for the steps to follow to install, they are [here](../saltbox/install/install.md).

If you want to examine the dependencies script before running it:

``` shell
curl -sL https://install.saltbox.dev | more
```

This script will:

1. install `git`
2. delete an existing repo
3. clone the saltbox repo to the system [default location `/srv/git/sb`]
4. create some script aliases
5. run [`sb_dep.sh`](https://github.com/saltyorg/sb/blob/master/sb_dep.sh)
6. run [`sb_repo.sh`](https://github.com/saltyorg/sb/blob/master/sb_repo.sh)

At the end of this you will have a local copy of the Saltbox repo, and all the things that Saltbox relies on to install will be available.

Go [back to the install process](../saltbox/install/install.md#dependencies).
