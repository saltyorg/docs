---
hide:
  - tags
---

# Saltbox CLI

<!-- BEGIN SALTBOX MANAGED CLI SECTION -->
<!-- This section is managed by scripts/update-sb-help.py - DO NOT EDIT MANUALLY -->
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
    help [command]                    Help about any command
    install [tags] [--flags]          Runs Ansible playbooks with specified tags
    list [query] [--flags]            List available Saltbox, Sandbox or Saltbox-mod tags
    logs                              Display logs of managed systemd services
    motd [--flags]                    Display system information
    reinstall-facts [--flags]         Reinstall the Rust saltbox.fact file
    reinstall-python [--flags]        Reinstall the Python version used by Saltbox and related Ansible virtual environment using uv
    reinstall-venv [--flags]          Reinstall the Ansible virtual environment
    self-update [--flags]             Update Saltbox CLI
    update [--flags]                  Update Saltbox & Sandbox
    validate-config [--flags]         Validate Saltbox configuration files
    version                           Print Saltbox CLI version
         
  FLAGS  
         
    -h --help                         Help for sb
    -v --version                      Version for sb
```

<!-- END SALTBOX MANAGED CLI SECTION -->