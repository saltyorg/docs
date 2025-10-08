---
hide:
  - tags
---

# Saltbox CLI
<!-- termynal -->

```console
$ sb -h
Saltbox CLI

Usage:
  sb [command]

Available Commands:
  bench            Runs bench.sh benchmark
  branch           Change the branch used by Saltbox
  branch-sandbox   Change the branch used by Sandbox
  diag             Runs Saltbox diagnostics role
  docker           Manage Docker containers managed by Saltbox
  edit             Edit Saltbox configuration files
  fact             Manage Saltbox configuration facts
  help             Help about any command
  install          Runs Ansible playbooks with specified tags
  inventory        Manage Saltbox inventory
  list             List available Saltbox, Sandbox or Saltbox-mod tags
  logs             Display logs of managed systemd services
  motd             Display system information
  reinstall-facts  Reinstall the Rust saltbox.fact file
  reinstall-python Reinstall the deadsnakes Python version used by Saltbox and related Ansible virtual environment
  reinstall-venv   Reinstall the Ansible virtual environment
  self-update      Update Saltbox CLI
  update           Update Saltbox & Sandbox
  validate-config  Validate Saltbox configuration files
  validate-config2 Validate Saltbox configuration files using YAML schemas
  version          Print Saltbox CLI version

Flags:
  -h, --help   help for sb

Use "sb [command] --help" for more information about a command.

```