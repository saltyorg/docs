# Installation

!!! warning
    This is a reference discussing an aspect of the [install process](../saltbox/install/install.md#install).
    If you are looking for the steps to follow to install, they are [here](../saltbox/install/install.md).

## Install Saltbox

=== "Saltbox"
    ```shell
    sb install saltbox

    ```

=== "Mediabox"
    ```shell
    sb install mediabox

    ```

=== "Feederbox"
    ```shell
    sb install feederbox

    ```

=== "Core"
    ```shell
    sb install core

    ```

A lot of logging information will scroll by.

Eventually, it will stop, and if successful, will display something like this:

    ```text
    PLAY RECAP ************************************************************************************
    localhost               : ok=713  changed=180  unreachable=0 failed=0
    ```

Note the `failed=0`.

If you don't see that, scroll up and the actual error should not be far away.
