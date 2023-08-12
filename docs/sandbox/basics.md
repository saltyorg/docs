# Basics

The [Saltbox Sandbox](https://github.com/saltyorg/Sandbox){: target=_blank rel="noopener noreferrer" } repository is installed with [Saltbox](https://github.com/saltyorg/Saltbox){: target=_blank rel="noopener noreferrer" } as part of a standard install. The Saltbox Sandbox application installers are provided and maintained by the community but are subject to approval. The applications are not part of a standard Saltbox install, but they should all be compatible with the Saltbox ecosystem. Sandbox is not a free-for-all no-rules repository but what will be accepted is a much broader range of applications which may not necessarily have anything to do with running a media server. Applications that are newly submitted or need testing will primarily land in the Sandbox repo and if relevant, stable, and maintained may end up in the Saltbox repo.

Saltbox documentation is written by community members to help others make the most of their systems.

Providing documentation for Sandbox applications is encouraged but not required.

All Saltbox applications **must** have documentation

## Install

``` shell

sb install sandbox

```

## Update

To update Saltbox Sandbox run a standard saltbox update; Sandbox and Saltbox will both be updated

``` shell

sb update

```

!!! info
    Note that `sb update` updates only the saltbox files themselves; it does not update any applications.  You will need to follow this with an `sb install <tags here>` command to update applications or installed components.

## How to Install Sandbox Apps

For most apps it is as simple as running the `sb install` command in a shell with a `sandbox-` prefix followed by the name of the role.

``` shell

sb install sandbox-rolename

```

For example, to install mkvtoolnix you would run the mkvtoolnix role:-

``` shell

sb install sandbox-mkvtoolnix

```

Before running any role you should first carefully read through any docs to see if there are any additional steps or pre configuration settings required.

A list of all roles available to Saltbox including Sandbox can be called from the terminal via:-

```shell

sb list

```

!!! Tip
    Where possible the configured username/password are taken from your Saltbox [`accounts.yml`](../saltbox/install/install.md#configuration) file located in `/srv/git/saltbox/accounts.yml` and used to create a default user an password for logging in.

### Requesting Sandbox Apps

If you have an idea for a container that you think fits into the Saltbox system but you don't feel you have the required skills to create a role, open an issue in the sandbox repo [here](https://github.com/saltyorg/Sandbox/issues).  Take a look at some other app requests and follow the same pattern.  If your suggestion catches a developer's interest, perhaps they will pick it up.

!!! note
    Requests are just that, *requests*.  Nobody is being paid for their work on this.  Requests may not be implemented in a timely manner or at all.

The person requesting is often the best person to implement it, since that person has the interest along with knowledge of the task and the test environment.  An arbitrary developer probably won't install and set up SomeRandomApp in order to fill a request for something that works alongside SomeRandomApp.

### Contributing to Sandbox Apps

Note: If you just want to install a container into the Saltbox system without creating a role, see [this article](../advanced/your-own-containers.md).

That work will also help you determine what you will need to do in a role, so starting there would not be wasted effort.

If you want to create a role to allow others to install your role, keep reading.

#### Editing an existing role

If you want to make a change to an existing role [for example, changing the docker image it uses], you don't have [or want to] to create a new role. You make changes like this for either core or sandbox roles using the [inventory system](../saltbox/inventory/index.md)

#### Preparatory work

Start by making your own fork of the Sandbox repo by clicking on the "Fork" button up and to the right.

This will take you to your own copy of the Sandbox repo.

On your development machine [which should probably be a machine running saltbox, as it makes things easier with regard to testing]:

clone your Sandbox fork:

```shell
git clone https://github.com/YOURNAMEHERE/Sandbox.git sandbox
```

go into that local sandbox dir:

```shell
cd sandbox
```

make sure your local repo is up-to-date:

```shell
git pull
```

create your feature branch:

```shell
git checkout -b my-cool-role
```

#### Creating a role

Now you're ready to start work on your new role.

A good starting point is to find a role that is similar to the one you want to add and use it as a starting point. For example, if your container requires mariadb and you want to create a database during setup, bookstack does that.

copy the "starting point" role to your role:

```shell
cp -R roles/bookstack roles/my-cool-role
```

[of course, substitute whatever role you're using as your prototype for "bookstack"]

Next step is to create the role. At a minimum, you will need to modify:

```text
roles
└── my-cool-role
    ├── defaults
    │   └── main.yml
    └── tasks
        └── main.yml
sandbox.yml
```

There may be other things required; there may be templates or sub-tasks or what have you. Those three files are the absolute bare minimum that would need to be created to add a new role.

What are those things?

```text
roles/my-cool-role/defaults/main.yml
```

This file contains various details for your role; the docker image, the name, subdomain, that sort of thing. The stuff in there should be self-explanatory or understandable with comparisons to existing roles; if it's not, then with all respect you probably shouldn't be creating a role right now.

```text
roles/my-cool-role/tasks/main.yml
```

This file drives the install of your role. The stuff in there should be self-explanatory or understandable with comparisons to existing roles; if it's not, then again, with all respect you probably shouldn't be creating a role right now.

There is a wiki article on adding new containers [here](../advanced/your-own-containers.md); this may be of some use.

Don't forget the header in both these files:

```text
#########################################################################
# Title:            Sandbox: my-cool-role                               #
# Author(s):        some-guy, salty                                     #
# URL:              https://github.com/saltyorg/Sandbox                 #
# --                                                                    #
#########################################################################
#                   GNU General Public License v3.0                     #
#########################################################################
---
```

Be sure you edit this to reflect your role, name, and such depending on what's there in your prototype

```text
sandbox.yml
```

This file drives the ansible install system by providing the valid tags that you can use with:

```shell
sb install sandbox-TAG
```

Again, it's a simple file, and it should be quite apparent what needs to be added for a new role.

##### Other files you may need to edit

```text
defaults
└── settings.yml.default
```

This file provides the prototype settings file; if your role requires some new settings, add them to this file.  When the sandbox repo is updated, your new settings will be added to the user's current settings file and they will be prompted to review it.

```text
templates
└── my-cool-role.j2
```

Perhaps you need to create a config file, or a service file, or the like.  Create templates for them here and fill them in at install time.  THere are lots of examples in the existing roles.

##### Testing

!!! warning
    BE SURE TO TEST YOUR ROLE.

You want to make sure that your role works, so be sure you run it several times. Run it on fresh installs, reinstalls, enlist someone else to run it for you. The point of doing this is to add something to sandbox for others to use; if you don't verify that it works, why are you doing it?

#### Creating the Pull Request

Now it's complete, and tested, and you want it to be added to sandbox for other users to enjoy.

First, commit your changes to your fork.

!!! warning
    BE SURE YOU DO NOT COMMIT FILES CONTAINING SECRETS LIKE API KEYS OR TOKENS.

This will involve adding the files you changed or added and doing a git commit and git push.

This is standard git stuff, and again, with all respect, if you don't know these git basics you probably shouldn't be creating a role right now.

Back at github.com, create a pull request against the "master" branch of the sandbox repo.

You do this by switching to your feature branch in your repo and clicking "Pull request" at the top where it says something like: "This branch is 2 commits ahead of sandbox:master."

This is a request for the Saltbox team to "pull" your changes into their repo.

If there are special instructions or details that your role needs, add them to the pull request comments. If needed, create a doc page [which will be its own pull request] for the role.

!!! warning
    BE SURE YOU DO NOT COMMIT FILES CONTAINING SECRETS LIKE API KEYS OR TOKENS.

Your pull request will be reviewed eventually, and may generate comments or change requests.

You can address those change requests by making further commits to your feature branch; they will automatically be added to this pull request.

Eventually, if deemed a good or just reasonable fit, your pull request will be accepted and it will appear in the source sandbox repo.
