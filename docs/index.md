---
extra_stylesheets:
  - stylesheets/index.css
hide:
  - toc
  - navigation
---

<section markdown>

# Saltbox

[![GitHub Org's stars](https://img.shields.io/github/stars/saltyorg?style=flat&logo=github)](https://github.com/saltyorg/Saltbox/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/saltyorg/saltbox?style=flat&logo=github)](https://github.com/saltyorg/saltbox/commits)
[![License](https://img.shields.io/github/license/saltyorg/saltbox?style=flat&logo=github)](https://github.com/saltyorg/Saltbox/blob/master/LICENSE.md)
[![Discord](https://img.shields.io/discord/853755447970758686?style=flat&logo=discord&logoColor=white)](https://discord.gg/ugfKXpFND8)
{ style="text-align:center;" }

[Learn more](saltbox/basics/basics.md){ .md-button .md-button--primary }
[Install](saltbox/prerequisites/prerequisites.md){ .md-button .md-button--primary }
[Get help](community/support.md){ .md-button .md-button--primary }
[Help out](community/index.md){ .md-button .md-button--primary }

---
<!-- BEGIN SALTBOX MANAGED CLI SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
<!-- termynal -->

```console
$ sb --help
Saltbox CLI                                                                                                           
         
  USAGE  
         
    sb [command] [--flags]  
            
  COMMANDS  
            
    bench                             Runs bench.sh benchmark
    branch [branch_name]              Change the branch used by Saltbox
    branch-sandbox [branch_name]      Change the branch used by Sandbox
    diag                              Runs Saltbox diagnostics role
    docker [command]                  Manage Docker containers managed by Saltbox
    edit [command]                    Edit Saltbox configuration files
    fact [role] [instance] [--flags]  Manage Saltbox configuration facts
    install [tags] [--flags]          Runs Ansible playbooks with specified tags
    list [query] [--flags]            List available Saltbox, Sandbox or Saltbox-mod tags
    logs                              Display logs of managed systemd services
    motd [--flags]                    Display system information
    reinstall-facts [--flags]         Reinstall the Rust saltbox.fact file
    reinstall-python [--flags]        Reinstall the Python version used by Saltbox and related Ansible virtual environment using uv
    reinstall-venv [--flags]          Reinstall the Ansible virtual environment
    update [--flags]                  Update Saltbox & Sandbox
    validate-config [--flags]         Validate Saltbox configuration files
    version                           Print Saltbox CLI version
         
  FLAGS  
         
    -h --help                         Help for sb
```

<!-- END SALTBOX MANAGED CLI SECTION -->
### Powered by { style="text-align:center;" }

<div class="grid brands" markdown>

[![Traefik](images/brands/traefik.svg#only-light)](#powered-by)

[![Traefik](images/brands/traefik-dark.svg#only-dark)](#powered-by)

[![Ansible](images/brands/ansible.svg#only-light)](#powered-by)

[![Ansible](images/brands/ansible-dark.svg#only-dark)](#powered-by)

[![Docker](images/brands/docker.svg)](#powered-by)

[![Go](images/brands/go.svg)](#powered-by)

[![Python](images/brands/python.svg)](#powered-by)

[![Ubuntu](images/brands/ubuntu.svg#only-light)](#powered-by)

[![Ubuntu](images/brands/ubuntu-dark.svg#only-dark)](#powered-by)

</div>

</section>
