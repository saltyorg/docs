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


Note: If you just want to install a container into the Saltbox system without creating a role, see [this article](../advanced/your-own-containers.md).

That work will also help you determine what you will need to do in a Community role, so starting there would not be wasted effort.

If you want to create a Community role to allow others to install your role, keep reading.

#### Editing an existing role:

If you want to make a change to an existing role [for example, changing the docker image it uses], you don't have [or want to] to create a new role. You make changes like this for either core or community roles using the [inventory system](../saltbox/inventory/index.md)

#### Preparatory work:

Start by making your own fork of the community repo by clicking on the "Fork" button up and to the right.

This will take you to your own copy of the community repo.

On your development machine [which should probably be a machine running saltbox, as it makes things easier with regard to testing]:

clone your community fork:

```
git clone https://github.com/YOURNAMEHERE/Community.git community
```

go into that local community dir:

```
cd community
```

make sure your local repo is up-to-date:

```
git pull
```

create your feature branch:

```
git checkout -b my-cool-role
```

#### Creating a role:

Now you're ready to start work on your new role.

A good starting point is to find a role that is similar to the one you want to add and use it as a starting point. For example, if your container requires mariadb and you want to create a database during setup, bookstack does that.

copy the "starting point" role to your role:

```
cp -R roles/bookstack roles/my-cool-role
```

[of course, substitute whatever role you're using as your prototype for "bookstack"]

Next step is to create the role. At a minimum, you will need to modify:

```
roles
└── my-cool-role
    ├── defaults
    │   └── main.yml
    └── tasks
        └── main.yml
community.yml
```

There may be other things required; there may be templates or sub-tasks or what have you. Those three files are the absolute bare minimum that would need to be created to add a new role.

What are those things?

```
roles/my-cool-role/defaults/main.yml
```

This file contains various details for your role; the docker image, the name, subdomain, that sort of thing. The stuff in there should be self-explanatory or understandable with comparisons to existing roles; if it's not, then with all respect you probably shouldn't be creating a role right now.

```
roles/my-cool-role/tasks/main.yml
```

This file drives the install of your role. The stuff in there should be self-explanatory or understandable with comparisons to existing roles; if it's not, then again, with all respect you probably shouldn't be creating a role right now.

There is a wiki article on adding new containers [here](../advanced/your-own-containers.md); this may be of some use.

Don't forget the header in both these files:

```
#########################################################################
# Title:            Community: my-cool-role                             #
# Author(s):        some-guy, salty                                     #
# URL:              https://github.com/saltyorg/Community               #
# --                                                                    #
#########################################################################
#                   GNU General Public License v3.0                     #
#########################################################################
---
```

Be sure you edit this to reflect your role, name, and such depending on what's there in your prototype

```
community.yml
```
This file drives the ansible install system by providing the valid tags that you can use with:

```
sb install cm-TAG
```

Again, it's a simple file, and it should be quite apparent what needs to be added for a new role.

##### Other files you may need to edit:

```
defaults
└── settings.yml.default
```

This file provides the prototype settings file; if your role requires some new settings, add them to this file.  When the community repo is updated, your new settings will be added to the user's current settings file and they will be prompted to review it. 

```
templates
└── my-cool-role.j2
```

Perhaps you need to create a config file, or a service file, or the like.  Create templates for them here and fill them in at install time.  THere are lots of examples in the existing roles.

##### Testing:

!!! warning
    BE SURE TO TEST YOUR ROLE.

You want to make sure that your role works, so be sure you run it several times. Run it on fresh installs, reinstalls, enlist someone else to run it for you. The point of doing this is to add something to community for others to use; if you don't verify that it works, why are you doing it?

#### Creating the Pull Request:

Now it's complete, and tested, and you want it to be added to community for other users to enjoy.

First, commit your changes to your fork.

!!! warning
    BE SURE YOU DO NOT COMMIT FILES CONTAINING SECRETS LIKE API KEYS OR TOKENS.

This will involve adding the files you changed or added and doing a git commit and git push.

This is standard git stuff, and again, with all respect, if you don't know these git basics you probably shouldn't be creating a role right now.

Back at github.com, create a pull request against the "master" branch of the community repo.

You do this by switching to your feature branch in your repo and clicking "Pull request" at the top where it says something like: "This branch is 2 commits ahead of Community:master."

This is a request for the Saltbox team to "pull" your changes into their repo.

If there are special instructions or details that your role needs, add them to the pull request comments. If needed, create a doc page [which will be its own pull request] for the role.

!!! warning
    BE SURE YOU DO NOT COMMIT FILES CONTAINING SECRETS LIKE API KEYS OR TOKENS.

Your pull request will be reviewed eventually, and may generate comments or change requests.

You can address those change requests by making further commits to your feature branch; they will automatically be added to this pull request.

Eventually, if deemed a good or just reasonable fit, your pull request will be accepted and it will appear in the source community repo.
