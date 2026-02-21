---
hide:
  - tags
tags:
  - cli
  - compose
  - container
  - custom
  - docker
  - generate
---

# Adding your own containers to Saltbox

Use this guide to extend your setup beyond the stock catalog. While arbitrary deployments fall outside our support scope, we offer resources to facilitate their integration with the Saltbox ecosystem.

## [Docker Compose](https://docs.docker.com/reference/cli/docker/compose)

Recommended for GUI applications and web services.

<div class="sb-cta" markdown>

<div markdown>

Generate and deploy a Compose file with Traefik publishing:

</div>

<div markdown>

[Traefik Template](../reference/modules/traefik_template.md){ .md-button }

</div>

</div>

## [Docker CLI](https://docs.docker.com/reference/cli/docker/container/run)

Recommended for command‑line utilities where a container is invoked ad hoc or on a schedule.

While such containers can be run via Compose, you may prefer to avoid the extra files. Optionally, register them as functions in your shell environment, so they can be called in their native, host-level form.

=== "`~/.bashrc` `~/.zshrc`"

    ```shell
    xCUSTOM_APP_NAMEx() {
      docker run --rm -it \
        DOCKER/IMAGE:TAG "$@"
    }
    ```

=== "Saltbox Inventory"

    ??? variable string "`shell_bash_bashrc_block_custom`"

        ```yaml
        shell_bash_bashrc_block_custom: |

          xCUSTOM_APP_NAMEx() {
            docker run --rm -it \
              DOCKER/IMAGE:TAG "$@"
          }
        ```

    ??? variable string "`shell_zsh_zshrc_block_custom`"

        ```yaml
        shell_zsh_zshrc_block_custom: |

          xCUSTOM_APP_NAMEx() {
            docker run --rm -it \
              DOCKER/IMAGE:TAG "$@"
          }
        ```

Then call from your regular shell with a command such as `xCUSTOM_APP_NAMEx --help`.

!!! example

    === "`~/.bashrc` `~/.zshrc`"

        ```shell
        yt-dlp() {
          docker run --rm -it \
            -v "$(pwd)":/downloads:rw \
            -u $(id -u):$(id -g) \
            ghcr.io/jauderho/yt-dlp:latest "$@"
        }
        ```

        ```shell
        speedtest() {
          docker run --rm -it \
            gists/speedtest-cli "$@"
        }
        ```

    === "Saltbox Inventory"

        ??? variable string "`shell_bash_bashrc_block_custom`"

            ```yaml
            shell_bash_bashrc_block_custom: |

              yt-dlp() {
                docker run --rm -it \
                  -v "$(pwd)":/downloads:rw \
                  -u $(id -u):$(id -g) \
                ghcr.io/jauderho/yt-dlp:latest "$@"
              }

              speedtest() {
                docker run --rm -it \
                  gists/speedtest-cli "$@"
              }
            ```

        ??? variable string "`shell_zsh_zshrc_block_custom`"

            ```yaml
            shell_zsh_zshrc_block_custom: |

              yt-dlp() {
                docker run --rm -it \
                  -v "$(pwd)":/downloads:rw \
                  -u $(id -u):$(id -g) \
                ghcr.io/jauderho/yt-dlp:latest "$@"
              }

              speedtest() {
                docker run --rm -it \
                  gists/speedtest-cli "$@"
              }
            ```

    Call using `yt-dlp` and `speedtest` commands.

## [Ansible Roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html)

Recommended when you need more automation and are comfortable working with [YAML:octicons-link-external-16:{ .md-icon--sm }](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html) and [Jinja2:octicons-link-external-16:{ .md-icon--sm }](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html).

<div class="sb-cta" markdown>

<div markdown>

Develop and maintain your own Saltbox-compatible roles in a dedicated playbook codespace:

</div>

<div markdown>

[:fontawesome-brands-github:**saltbox_mod**](https://github.com/saltyorg/saltbox_mod){ .md-button }

</div>

</div>
