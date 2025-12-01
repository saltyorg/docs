---
status: draft
---

# Development

Interested in creating a new role for Sandbox? We welcome your contributions!

!!! info "Repository Philosophy"

    Sandbox is not a free-for-all; it accepts a broad range of apps, prefereably within the media acquisition and delivery ecosystem. New or experimental apps land in Sandbox and may move to Saltbox if relevant, stable, and maintained.

## Contributing to Sandbox

!!! tip

    If you just want to install a container into the Saltbox system without creating a role, see [this article](../../advanced/your-own-containers.md).  
    Starting here helps you learn what is needed for a role.

To change an existing role (e.g., update the docker image), use the [inventory system](../../saltbox/inventory/index.md).

### Preparatory Work

1. Fork the Sandbox repo.
2. Clone your fork (ideally on a Saltbox machine for easier testing):

    ```shell
    git clone https://github.com/YOURNAMEHERE/Sandbox.git sandbox
    cd sandbox
    git pull
    git checkout -b my-cool-role
    ```

### Creating a Role

- Use an existing role as a starting point (choose one similar to your needs):
    ```shell
    cp -R roles/bookstack roles/my-cool-role
    ```
- At minimum, edit:
    - `roles/my-cool-role/defaults/main.yml` — contains details like docker image, name, subdomain, etc.
    - `roles/my-cool-role/tasks/main.yml` — drives the install process.
    - `sandbox.yml` — provides valid tags for the Ansible install system.

    If the contents of these files are not self-explanatory, reconsider creating a role for now.

#### Required Headers

Add a header to both `main.yml` files:

```text
#########################################################################
# Title:            Sandbox: my-cool-role                               #
# Author(s):        your-name, salty                                    #
# URL:              https://github.com/saltyorg/Sandbox                 #
# --                                                                    #
#########################################################################
#                   GNU General Public License v3.0                     #
#########################################################################
---
```

#### Other Files

- If needed, edit:
    - `defaults/settings.yml.default` — prototype settings for your role.
    - `templates/my-cool-role.j2` — for config/service files generated at install.

### Testing

!!! warning

    BE SURE TO TEST YOUR ROLE. Run it on fresh installs, reinstalls, and ask others to test.

### Creating the Pull Request

1. Commit your changes to your fork.
2. **Do not commit files containing secrets like API keys or tokens.**
3. Push your branch and open a pull request against the master branch on GitHub.
4. Add any special instructions or documentation as needed.

!!! warning

    Do not commit files containing secrets like API keys or tokens.  
    Basic git knowledge is expected; if unfamiliar, reconsider creating a role for now.

Your pull request will be reviewed and may generate comments or change requests.  
Address those by updating your branch; changes will be added to the pull request.  
If accepted, your role will appear in the Sandbox repo.

## Need Help?

For questions or assistance, join our [Discord](https://discord.gg/ugfKXpFND8).
