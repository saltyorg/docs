---
show:
  - footer.previous
  - footer.next
hide:
  - tags
tags:
  - customize
  - install
  - inventory
  - override
---

# Inventory

The inventory system offers a centralized approach to customizing roles, allowing manipulation of variables without directly editing the roles themselves. This ensures persistent configurations while avoiding conflicts during git merge operations.

## Overriding Variables

Enter your new values in:

```
/srv/git/saltbox/inventories/host_vars/localhost.yml
```

!!! tip "Quick Shell Access"

    ```shell
    sb edit inventory
    ```

Changes take effect after deploying the affected role(s) using the `install` command.

## Finding Available Variables

Variables that can be used for customization within the Inventory are listed under ***Role Defaults*** at the end of role documentations.

<div class="sb-cta" markdown>

Find a role by using search or browsing the indexes:

<div markdown>

[Browse Apps](../../apps/index.md){ .md-button }

[Browse Modules](../../reference/modules/index.md){ .md-button }

</div>

</div>

## Data Types

Inventory syntax follows [YAML specifications](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html). You will encounter five data types in the defaults:

| Data Type       | Token          | Syntax Template                                                                  | Saltbox Example                                                                                                                   |
|-----------------|----------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| boolean         | `true`/`false` | <pre><code>bool_key: true</code></pre>                                           | <pre><code>use_cloudplow: false</code></pre>                                                                                      |
| integer         |                | <pre><code>int_key: 123</code></pre>                                             | <pre><code>emby_role_config_cache_size: 2048</code></pre>                                                                         |
| string          | `""`           | <pre><code>str_key: "value"</code></pre>                                         | <pre><code>global_themepark_theme: "overseerr"</code></pre>                                                                       |
| <br/>list       | <br/>`[]`      | <pre><code>list_key:<br/>  - item0<br/>  - "item1"</code></pre>                  | <pre><code>gluetun_docker_networks_alias_custom:<br/>  - "plex"<br/>  - "plex2"</code></pre>                                      |
| <br/>dictionary | <br/>`{}`      | <pre><code>dict_key:<br/>  STR_KEY: "value"<br/>  BOOL_KEY: "false"</code></pre> | <pre><code>kometasw_docker_envs_custom:<br/>  KOMETA_RUN_COLLECTIONS: "Star Wars"<br/>  KOMETA_DELETE_LABELS: "true"</code></pre> |

## Override Scope

When deploying [multiple instances](../../reference/multiple-instances.md), you can apply a configuration across all instances or to a specified instance. This is achieved by shaping the variable name as follows:

<div class="grid" markdown>

<div markdown>

:material-cards-playing: **Role-level** (default)

```yaml
xROLE_NAMEx_role_setting_enabled: false # (1)!
```

1.  Variable name unchanged (default when no instances are defined)

:material-arrow-right-bottom-bold: Applies to all instances of the role

</div>

<div markdown>

:material-cards-playing-diamond: **Instance-level**

```yaml
dROLE_NAMEdxINSTANCE_SUFFIXx_setting_enabled: true # (1)!
```

1.  -   `_role` segment removed
    -   instance name can be the role name (`xROLE_NAMEx`) or prefixed with it (`dROLE_NAMEdxINSTANCE_SUFFIXx`)

:material-arrow-right-bottom-bold: Applies to the specified instance

</div>

</div>

When both forms of the variable are used in the Inventory, the instance-level value takes precedence.

## Demo

Let's explore two example use cases for customizing roles using variables in the Saltbox Inventory.

### Replacing a Default Value

A common use for overrides will be specifying the version of the Docker image to be used. Let's see how that's done by navigating to [Sonarr: Role Defaults](../../apps/sonarr.md#role-defaults) and in the ***Docker*** tab, scrolling down to:

???+ variable string "`sonarr_role_docker_image_tag`"

    === "Role-level"

        ```yaml
        # Type: string
        sonarr_role_docker_image_tag: "release"
        ```

    === "Instance-level"

        ```yaml
        # Type: string
        sonarr2_docker_image_tag: "release"
        ```

Given this default value, Saltbox will use `ghcr.io/hotio/sonarr:release` as the Sonarr Docker image.

Opting to switch to "nightly" versions across all Sonarr instances, we can add the following line to `localhost.yml`:

```yaml
sonarr_role_docker_image_tag: "nightly"
```

This will cause Saltbox to use the `ghcr.io/hotio/sonarr:nightly` Docker image, overriding the default: `release`. When we update Saltbox, our tag change to `nightly` will remain in effect.

### Adding an Item to a List

A common use for lists is to specify extra Docker mappings or flags. Let's examine how to give our [code-server](../../sandbox/apps/code_server.md#role-defaults) container access to more locations on the host. In the ***Docker*** section, we find:

??? variable list "`code_server_role_docker_volumes_default`"

    ```yaml
    # Type: list
    code_server_role_docker_volumes_default:
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/project:/home/coder/project"
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.config:/home/coder/.config"
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.local:/home/coder/.local"
      - "{{ server_appdata_path }}:/host_opt"
    ```

???+variable list "`code_server_role_docker_volumes_custom`"

    ```yaml
    # Type: list
    code_server_role_docker_volumes_custom: []
    ```

Note the list syntax. Since we want the container to preserve existing volumes, the `_docker_volumes_default` list should not be overridden. Instead, we use the `_docker_volumes_custom` list.

To expose additional host locations (in this case, `/srv` and our home directory), we can add custom volumes to the list using the following syntax in the Inventory:

```yaml
code_server_role_docker_volumes_custom:
  - "/srv:/host_srv"
  - "/home:/host_home"
```

The container will then be created with the new volumes included, and the target locations will be accessible to code-server at `/host_srv` and `/host_home`.
