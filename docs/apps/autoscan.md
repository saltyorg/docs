---
icon: material/docker
status: outdated
hide:
  - tags
tags:
  - autoscan
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/saltydk/autoscan/blob/master/README.md#overview
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/saltydk/autoscan/tags
      type: docker
    - name: Community
      url: https://discord.gg/ugfKXpFND8
      type: discord
  project_description:
    name: Autoscan
    summary: |
      the official Saltbox continuation of *Cloudbox/autoscan*, an open-source tool designed to automatically trigger media scans in media servers like Plex, Emby, and Jellyfin when new content is added.
    link: https://github.com/saltydk/autoscan
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Autoscan

## Overview

[Autoscan](https://github.com/saltydk/autoscan) is the official Saltbox continuation of *Cloudbox/autoscan*, an open-source tool designed to automatically trigger media scans in media servers like Plex, Emby, and Jellyfin when new content is added.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/saltydk/autoscan/blob/master/README.md#overview){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/saltydk/autoscan/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/ugfKXpFND8){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install autoscan
```

## Usage

Manual scan URL: <https://autoscan.iYOUR_DOMAIN_NAMEi/triggers/manual>.

## Basics

The Plex API is known to have trouble when scanning items into empty libraries. You should add at least one item to each Plex library and perform a manual scan as a first step. If you don't do this, things may not get scanned into Plex in response to autoscan's requests.

The Saltbox Autoscan role will attempt to partially configure your autoscan config file located at `/opt/autoscan/config.yml`. You should refer to the documentation and adjust this file as suits your own needs. The config generated is very minimal. [a-train](https://github.com/m-rots/a-train/pkgs/container/a-train) is now replacing the bernard trigger.

The generated config file will look something like this:

```yaml
# <- processor ->

# Override the minimum age before a scan request is sent to the target (Default 10m):
minimum-age: 10m

# Override the delay between processed scans (Default 5s):
scan-delay: 5s

# Set anchor files for remote storage. If these are missing no scans will be sent to the target to avoid files being trashed when a mount fails
anchors:
  - /mnt/unionfs/mounted.bin

# <- triggers ->

# Optionally, protect your webhooks with authentication
authentication:
  username: USERNAME_FROM_SETTINGS
  password: PASSWORD_FROM_SETTINGS

# Port for Autoscan webhooks to listen on
port: 3030

triggers:
  a-train:
      priority: 5
      rewrite: # Global rewrites
        - from: ^/Media/
          to: /mnt/unionfs/Media/

  inotify:
    - priority: 0

      # Filter with regular expressions
      include:
        - ^/mnt/unionfs/Media/
      exclude:
        - '\.(srt|pdf)$'

      # rewrite inotify path to unified filesystem
      rewrite:
        - from: ^/mnt/local/Media/
          to: /mnt/unionfs/Media/

      # Local filesystem paths to monitor
      paths:
        - path: /mnt/local/Media

  sonarr:
    - name: sonarr # /triggers/sonarr
      priority: 2

  radarr:
    - name: radarr # /triggers/radarr
      priority: 2

  lidarr:
    - name: lidarr # /triggers/lidarr
      priority: 1

# <- targets ->

targets:
  plex:
    - url: https://plex.xYOUR_DOMAIN_NAMEx # plex
      token: YOUR_PLEX_TOKEN
```

Then edit the anchors section:

```yaml
anchors:
  - /mnt/unionfs/mounted.bin
```

To reflect your own configuration.

YOU PROBABLY NEED TO CREATE THIS FILE OR FILES YOURSELF. The regular saltbox install does not do it for you.

If you went through the OPTIONAL google-drive rclone setup process, these files *did* get created for you, and you'll need to enter something like:

```yaml
anchors:
  - /mnt/unionfs/bvoiwepopz-movies_mounted.bin
  - /mnt/unionfs/bvoiwepopz-tv_mounted.bin
  - /mnt/unionfs/bvoiwepopz-music_mounted.bin
  - /mnt/unionfs/bvoiwepopz-anime_mounted.bin
...
```

You should enter the entire list of bin files that were created by the automated script here.

If you didn't go through that process, use:

```
rclone touch NAME_OF_CLOUD_REMOTE:mounted.bin
```

To create one of these files on *each distinct element* of cloud storage. If you're using Dropbox, there is just one. If you have eleven OneDrive mounts, you need to create eleven of these.

Do this on each rclone remote that you have *mounted*. For example, if you're using box.com and have three remotes (`box_remote`, `box_crypt`, `chunker_remote`), run this command on the last one, `chunker_remote`, since that';s the remote that you are mounting.

Once you've done that, verify that they show up in the union mount with:

```
ls /mnt/unionfs/*.bin
```

then enter that list of files into the autoscan config as shown.

Everything else should be ready to go for standard usage.

<details>
<summary>What are those mount files?</summary>
<br />
<br />
Autoscan uses these to determine if your cloud storage is mounted and visible; if autoscan can't see these files, no scans will be sent to Plex since doing so would empty your library as Plex removed all the files it can no longer see (assuming that "empty trash on scan" is enabled).
<br />
<br />
There's nothing special about the contents of these files; autoscan just needs to see that they exist. Typically they are empty.
<br />
<br />
If you went through the saltbox rclone setup, these files got created for you.
<br />
<br />
</details>

<details>
<summary>Do I really need to include all seven or eight or however many?</summary>
<br />
<br />
Strictly speaking, no, not with the way saltbox sets up the mounts. All those shared drives are part of a union remote, and the union remote is mounted, so there's really no possibility that some of those files would be present but not others. Any one of them is probably sufficient.
<br />
<br />
However, there's no reason *not* to include them all as you can grab the list with a single command and a copy-paste. You save a few keystrokes by not including all of them (you don't have to copy-paste `  - ` in front of those few lines), but in thinking about it at all you've spent the same amount of time. Reading this question and answer have taken more time than it would have taken to include all of them as a belt-and-suspenders measure.
<br />
<br />
</details>

<details>
<summary>Is there something magic about the name `mounted.bin`?</summary>
<br />
<br />
No. These files can be named whatever you want. If you don't like `mounted.bin` and woudl rather use `black.sabbath` or whatever, go ahead. Autoscan is just going to verify that the file you specify exists so autoscan knows it is safe to send scans to Plex.
<br />
<br />
</details>

You will set up the webhooks for radarr/sonarr/lidarr as part of their setup, so they aren't discussed here

### A-Train

Autoscan can monitor **Google Drive** changes via a trigger called "Bernard". The code behind Bernard can sometimes get out of sync with the state of Google Drive and miss things, so now we are using A-Train.

**IMPORTANT**:
You only need to set this up if you are planning to add media to **Google Drive** directly, *outside* the usual Radarr/Sonarr channels, or if you are monitoring a Shared Drive where new media appears outside those channels. If you are not planning to do that, you can skip this portion of the setup.

**IMPORTANT**:
A-Train does not support anything other than **Google Drive**, as it uses the Google Drive API to do its work.

"A-Train" is a rewrite of the Bernard concepts, and is currently available as a second docker image as part of Sandbox. It will likely be integrated into autoscan at some point in the future.

!!! warning
    A-Train supports **only** *unencrypted* Google Shared Drives authenticated via Service Accounts. It *does not* support encrypted drives, My Drive, or authentication via Client ID/Secret or other means.

Enter the names of the remotes you want to monitor in the Inventory. The Remotes can be either drive remotes or union remotes. You may use `rclone listremotes` to get your drive remotes.

Example:

```yaml
a_train:
  remotes: ["bvoiwepopz-Movies", "bvoiwepopz-TV"]
```

or

```yaml
a_train:
  remotes: ["google"]
```

Run the a-train tag to create the container:

```shell
sb install sandbox-a-train
```

Copy one of your service account files from its current location to `/opt/a-train/account.json`. Remember to rename your service account file to "`account.json`".

Example:

```shell
cp /opt/sa/all/160.json /opt/a-train/account.json
```

Run the autoscan tag to rebuild the container:

```shell
sb install autoscan
```

Run the a-train tag to rebuild the container:

```shell
sb install sandbox-a-train
```

### Bernard

**IMPORTANT**:
Bernard does not support anything other than **Google Drive**, as it uses the Google Drive API to do its work.

If for some reason you still wanted to use Bernard, it would look like this:

```yaml
triggers:
  bernard:
    - account: /config/sa.json # Path inside the container where your SA is located
      cron: "*/5 * * * *" # every five minutes (the "" are important)
      priority: 0
      drives:
        - id: drive_id #Friendly title
      # Rewrite gdrive to the local filesystem
      rewrite:
        - from: ^/Media/
          to: /mnt/unionfs/Media/
      # Filter with regular expressions
      include:
        - ^/mnt/unionfs/Media/
      exclude:
        - '\.srt$'
```

Further documentation:

- [A-Train Docker page](https://github.com/users/m-rots/packages/container/package/a-train)

- [A-Train initial documentation](https://gist.github.com/m-rots/f345fd2cfc44585266b620feb9fbd612)

## Next

<div class="sb-cta" markdown>

Are you Setting Saltbox up for the first time?

<div markdown>

[**Continue to SABnzbd**:material-forward:](sabnzbd.md){ .md-button }

</div>

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override level"><input type="checkbox" name="scope" hidden/></label>

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `autoscan_instances`.**

    !!! example "Example override"

        === "Role-level"

            ```yaml
            autoscan_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of autoscan

        === "Instance-level"

            ```yaml
            autoscan2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named autoscan2

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `autoscan_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `autoscan_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`autoscan_instances`"

        ```yaml
        # Type: list
        autoscan_instances: ["autoscan"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            autoscan_instances: ["autoscan", "autoscan2"]
            ```

=== "Web"

    ??? variable string "`autoscan_role_web_subdomain`{ .sb-show-on-unchecked }`autoscan2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_web_subdomain: "{{ autoscan_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_web_subdomain: "{{ autoscan_name }}"
        ```

    ??? variable string "`autoscan_role_web_domain`{ .sb-show-on-unchecked }`autoscan2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`autoscan_role_web_port`{ .sb-show-on-unchecked }`autoscan2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_web_port: "3030"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_web_port: "3030"
        ```

    ??? variable string "`autoscan_role_web_url`{ .sb-show-on-unchecked }`autoscan2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='autoscan') + '.' + lookup('role_var', '_web_domain', role='autoscan')
                                if (lookup('role_var', '_web_subdomain', role='autoscan') | length > 0)
                                else lookup('role_var', '_web_domain', role='autoscan')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='autoscan') + '.' + lookup('role_var', '_web_domain', role='autoscan')
                            if (lookup('role_var', '_web_subdomain', role='autoscan') | length > 0)
                            else lookup('role_var', '_web_domain', role='autoscan')) }}"
        ```

=== "DNS"

    ??? variable string "`autoscan_role_dns_record`{ .sb-show-on-unchecked }`autoscan2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='autoscan') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='autoscan') }}"
        ```

    ??? variable string "`autoscan_role_dns_zone`{ .sb-show-on-unchecked }`autoscan2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='autoscan') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_dns_zone: "{{ lookup('role_var', '_web_domain', role='autoscan') }}"
        ```

    ??? variable bool "`autoscan_role_dns_proxy`{ .sb-show-on-unchecked }`autoscan2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`autoscan_role_traefik_regex_middleware_string`{ .sb-show-on-unchecked }`autoscan2_traefik_regex_middleware_string`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_regex_middleware_string: ",{{ autoscan_name }}-replacepathregex"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_regex_middleware_string: ",{{ autoscan_name }}-replacepathregex"
        ```

    ??? variable string "`autoscan_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`autoscan2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_sso_middleware: ""
        ```

    ??? variable string "`autoscan_role_traefik_middleware_default`{ .sb-show-on-unchecked }`autoscan2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_middleware_default: "{{ traefik_default_middleware + autoscan_role_traefik_regex_middleware_string }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_middleware_default: "{{ traefik_default_middleware + autoscan_role_traefik_regex_middleware_string }}"
        ```

    ??? variable string "`autoscan_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`autoscan2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_middleware_custom: ""
        ```

    ??? variable string "`autoscan_role_traefik_certresolver`{ .sb-show-on-unchecked }`autoscan2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`autoscan_role_traefik_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_traefik_enabled: true
        ```

    ??? variable bool "`autoscan_role_traefik_api_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_traefik_api_enabled: false
        ```

    ??? variable string "`autoscan_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`autoscan2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`autoscan_role_docker_container`{ .sb-show-on-unchecked }`autoscan2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_container: "{{ autoscan_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_container: "{{ autoscan_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`autoscan_role_docker_image_pull`{ .sb-show-on-unchecked }`autoscan2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_image_pull: true
        ```

    ??? variable string "`autoscan_role_docker_image_repo`{ .sb-show-on-unchecked }`autoscan2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_image_repo: "saltydk/autoscan"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_image_repo: "saltydk/autoscan"
        ```

    ??? variable string "`autoscan_role_docker_image_tag`{ .sb-show-on-unchecked }`autoscan2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_image_tag: "latest"
        ```

    ??? variable string "`autoscan_role_docker_image`{ .sb-show-on-unchecked }`autoscan2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='autoscan') }}:{{ lookup('role_var', '_docker_image_tag', role='autoscan') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='autoscan') }}:{{ lookup('role_var', '_docker_image_tag', role='autoscan') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`autoscan_role_docker_envs_default`{ .sb-show-on-unchecked }`autoscan2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        autoscan_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        autoscan2_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`autoscan_role_docker_envs_custom`{ .sb-show-on-unchecked }`autoscan2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        autoscan_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        autoscan2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`autoscan_role_docker_volumes_default`{ .sb-show-on-unchecked }`autoscan2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_volumes_default:
          - "{{ autoscan_role_paths_location }}:/config"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_volumes_default:
          - "{{ autoscan_role_paths_location }}:/config"
        ```

    ??? variable list "`autoscan_role_docker_volumes_custom`{ .sb-show-on-unchecked }`autoscan2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable list "`autoscan_role_docker_labels_default`{ .sb-show-on-unchecked }`autoscan2_docker_labels_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_labels_default:
          - '{ "traefik.http.middlewares.{{ traefik_router }}-replacepathregex.replacepathregex.regex": "^/$" }'
          - '{ "traefik.http.middlewares.{{ traefik_router }}-replacepathregex.replacepathregex.replacement": "/triggers/manual" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.entrypoints": "{{ traefik_entrypoint_websecure }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.service": "{{ traefik_router }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.rule": "Host(`{{ traefik_host }}`) && PathPrefix(`/triggers`)" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.priority": "{{ lookup("role_var", "_traefik_priority", role="autoscan", default="40") }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="autoscan", default=traefik_default_certresolver) }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.middlewares": "{{ traefik_middleware | regex_replace(autoscan_role_traefik_regex_middleware_string) }}" }'
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_labels_default:
          - '{ "traefik.http.middlewares.{{ traefik_router }}-replacepathregex.replacepathregex.regex": "^/$" }'
          - '{ "traefik.http.middlewares.{{ traefik_router }}-replacepathregex.replacepathregex.replacement": "/triggers/manual" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.entrypoints": "{{ traefik_entrypoint_websecure }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.service": "{{ traefik_router }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.rule": "Host(`{{ traefik_host }}`) && PathPrefix(`/triggers`)" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.priority": "{{ lookup("role_var", "_traefik_priority", role="autoscan", default="40") }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="autoscan", default=traefik_default_certresolver) }}" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ traefik_router }}-triggers.middlewares": "{{ traefik_middleware | regex_replace(autoscan_role_traefik_regex_middleware_string) }}" }'
        ```

    ??? variable dict "`autoscan_role_docker_labels_custom`{ .sb-show-on-unchecked }`autoscan2_docker_labels_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        autoscan_role_docker_labels_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        autoscan2_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`autoscan_role_docker_hostname`{ .sb-show-on-unchecked }`autoscan2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_hostname: "{{ autoscan_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_hostname: "{{ autoscan_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`autoscan_role_docker_networks_alias`{ .sb-show-on-unchecked }`autoscan2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_networks_alias: "{{ autoscan_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_networks_alias: "{{ autoscan_name }}"
        ```

    ??? variable list "`autoscan_role_docker_networks_default`{ .sb-show-on-unchecked }`autoscan2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_networks_default: []
        ```

    ??? variable list "`autoscan_role_docker_networks_custom`{ .sb-show-on-unchecked }`autoscan2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`autoscan_role_docker_restart_policy`{ .sb-show-on-unchecked }`autoscan2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`autoscan_role_docker_state`{ .sb-show-on-unchecked }`autoscan2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`autoscan_role_docker_blkio_weight`{ .sb-show-on-unchecked }`autoscan2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_blkio_weight:
        ```

    ??? variable int "`autoscan_role_docker_cpu_period`{ .sb-show-on-unchecked }`autoscan2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_cpu_period:
        ```

    ??? variable int "`autoscan_role_docker_cpu_quota`{ .sb-show-on-unchecked }`autoscan2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_cpu_quota:
        ```

    ??? variable int "`autoscan_role_docker_cpu_shares`{ .sb-show-on-unchecked }`autoscan2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_cpu_shares:
        ```

    ??? variable string "`autoscan_role_docker_cpus`{ .sb-show-on-unchecked }`autoscan2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_cpus:
        ```

    ??? variable string "`autoscan_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`autoscan2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_cpuset_cpus:
        ```

    ??? variable string "`autoscan_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`autoscan2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_cpuset_mems:
        ```

    ??? variable string "`autoscan_role_docker_kernel_memory`{ .sb-show-on-unchecked }`autoscan2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_kernel_memory:
        ```

    ??? variable string "`autoscan_role_docker_memory`{ .sb-show-on-unchecked }`autoscan2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_memory:
        ```

    ??? variable string "`autoscan_role_docker_memory_reservation`{ .sb-show-on-unchecked }`autoscan2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_memory_reservation:
        ```

    ??? variable string "`autoscan_role_docker_memory_swap`{ .sb-show-on-unchecked }`autoscan2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_memory_swap:
        ```

    ??? variable int "`autoscan_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`autoscan2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_memory_swappiness:
        ```

    ??? variable string "`autoscan_role_docker_shm_size`{ .sb-show-on-unchecked }`autoscan2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`autoscan_role_docker_cap_drop`{ .sb-show-on-unchecked }`autoscan2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_cap_drop:
        ```

    ??? variable string "`autoscan_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`autoscan2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_cgroupns_mode:
        ```

    ??? variable list "`autoscan_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`autoscan2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_device_cgroup_rules:
        ```

    ??? variable list "`autoscan_role_docker_device_read_bps`{ .sb-show-on-unchecked }`autoscan2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_device_read_bps:
        ```

    ??? variable list "`autoscan_role_docker_device_read_iops`{ .sb-show-on-unchecked }`autoscan2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_device_read_iops:
        ```

    ??? variable list "`autoscan_role_docker_device_requests`{ .sb-show-on-unchecked }`autoscan2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_device_requests:
        ```

    ??? variable list "`autoscan_role_docker_device_write_bps`{ .sb-show-on-unchecked }`autoscan2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_device_write_bps:
        ```

    ??? variable list "`autoscan_role_docker_device_write_iops`{ .sb-show-on-unchecked }`autoscan2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_device_write_iops:
        ```

    ??? variable list "`autoscan_role_docker_devices`{ .sb-show-on-unchecked }`autoscan2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_devices:
        ```

    ??? variable string "`autoscan_role_docker_devices_default`{ .sb-show-on-unchecked }`autoscan2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_devices_default:
        ```

    ??? variable list "`autoscan_role_docker_groups`{ .sb-show-on-unchecked }`autoscan2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_groups:
        ```

    ??? variable bool "`autoscan_role_docker_privileged`{ .sb-show-on-unchecked }`autoscan2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_privileged:
        ```

    ??? variable list "`autoscan_role_docker_security_opts`{ .sb-show-on-unchecked }`autoscan2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_security_opts:
        ```

    ??? variable string "`autoscan_role_docker_user`{ .sb-show-on-unchecked }`autoscan2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_user:
        ```

    ??? variable string "`autoscan_role_docker_userns_mode`{ .sb-show-on-unchecked }`autoscan2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`autoscan_role_docker_dns_opts`{ .sb-show-on-unchecked }`autoscan2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_dns_opts:
        ```

    ??? variable list "`autoscan_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`autoscan2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_dns_search_domains:
        ```

    ??? variable list "`autoscan_role_docker_dns_servers`{ .sb-show-on-unchecked }`autoscan2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_dns_servers:
        ```

    ??? variable string "`autoscan_role_docker_domainname`{ .sb-show-on-unchecked }`autoscan2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_domainname:
        ```

    ??? variable list "`autoscan_role_docker_exposed_ports`{ .sb-show-on-unchecked }`autoscan2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_exposed_ports:
        ```

    ??? variable dict "`autoscan_role_docker_hosts`{ .sb-show-on-unchecked }`autoscan2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        autoscan_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        autoscan2_docker_hosts:
        ```

    ??? variable bool "`autoscan_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`autoscan2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_hosts_use_common:
        ```

    ??? variable string "`autoscan_role_docker_ipc_mode`{ .sb-show-on-unchecked }`autoscan2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_ipc_mode:
        ```

    ??? variable list "`autoscan_role_docker_links`{ .sb-show-on-unchecked }`autoscan2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_links:
        ```

    ??? variable string "`autoscan_role_docker_network_mode`{ .sb-show-on-unchecked }`autoscan2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_network_mode:
        ```

    ??? variable string "`autoscan_role_docker_pid_mode`{ .sb-show-on-unchecked }`autoscan2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_pid_mode:
        ```

    ??? variable list "`autoscan_role_docker_ports`{ .sb-show-on-unchecked }`autoscan2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_ports:
        ```

    ??? variable string "`autoscan_role_docker_uts`{ .sb-show-on-unchecked }`autoscan2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`autoscan_role_docker_keep_volumes`{ .sb-show-on-unchecked }`autoscan2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_keep_volumes:
        ```

    ??? variable list "`autoscan_role_docker_mounts`{ .sb-show-on-unchecked }`autoscan2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_mounts:
        ```

    ??? variable dict "`autoscan_role_docker_storage_opts`{ .sb-show-on-unchecked }`autoscan2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        autoscan_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        autoscan2_docker_storage_opts:
        ```

    ??? variable list "`autoscan_role_docker_tmpfs`{ .sb-show-on-unchecked }`autoscan2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_tmpfs:
        ```

    ??? variable string "`autoscan_role_docker_volume_driver`{ .sb-show-on-unchecked }`autoscan2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_volume_driver:
        ```

    ??? variable list "`autoscan_role_docker_volumes_from`{ .sb-show-on-unchecked }`autoscan2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_volumes_from:
        ```

    ??? variable bool "`autoscan_role_docker_volumes_global`{ .sb-show-on-unchecked }`autoscan2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_volumes_global:
        ```

    ??? variable string "`autoscan_role_docker_working_dir`{ .sb-show-on-unchecked }`autoscan2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`autoscan_role_docker_auto_remove`{ .sb-show-on-unchecked }`autoscan2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_auto_remove:
        ```

    ??? variable bool "`autoscan_role_docker_cleanup`{ .sb-show-on-unchecked }`autoscan2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_cleanup:
        ```

    ??? variable string "`autoscan_role_docker_force_kill`{ .sb-show-on-unchecked }`autoscan2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_force_kill:
        ```

    ??? variable dict "`autoscan_role_docker_healthcheck`{ .sb-show-on-unchecked }`autoscan2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        autoscan_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        autoscan2_docker_healthcheck:
        ```

    ??? variable int "`autoscan_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`autoscan2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`autoscan_role_docker_init`{ .sb-show-on-unchecked }`autoscan2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_init:
        ```

    ??? variable string "`autoscan_role_docker_kill_signal`{ .sb-show-on-unchecked }`autoscan2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_kill_signal:
        ```

    ??? variable string "`autoscan_role_docker_log_driver`{ .sb-show-on-unchecked }`autoscan2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_log_driver:
        ```

    ??? variable dict "`autoscan_role_docker_log_options`{ .sb-show-on-unchecked }`autoscan2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        autoscan_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        autoscan2_docker_log_options:
        ```

    ??? variable bool "`autoscan_role_docker_oom_killer`{ .sb-show-on-unchecked }`autoscan2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_oom_killer:
        ```

    ??? variable int "`autoscan_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`autoscan2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_oom_score_adj:
        ```

    ??? variable bool "`autoscan_role_docker_output_logs`{ .sb-show-on-unchecked }`autoscan2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_output_logs:
        ```

    ??? variable bool "`autoscan_role_docker_paused`{ .sb-show-on-unchecked }`autoscan2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_paused:
        ```

    ??? variable bool "`autoscan_role_docker_recreate`{ .sb-show-on-unchecked }`autoscan2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_recreate:
        ```

    ??? variable int "`autoscan_role_docker_restart_retries`{ .sb-show-on-unchecked }`autoscan2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_restart_retries:
        ```

    ??? variable int "`autoscan_role_docker_stop_timeout`{ .sb-show-on-unchecked }`autoscan2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`autoscan_role_docker_capabilities`{ .sb-show-on-unchecked }`autoscan2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_capabilities:
        ```

    ??? variable string "`autoscan_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`autoscan2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_cgroup_parent:
        ```

    ??? variable list "`autoscan_role_docker_commands`{ .sb-show-on-unchecked }`autoscan2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_commands:
        ```

    ??? variable int "`autoscan_role_docker_create_timeout`{ .sb-show-on-unchecked }`autoscan2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        autoscan_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        autoscan2_docker_create_timeout:
        ```

    ??? variable string "`autoscan_role_docker_entrypoint`{ .sb-show-on-unchecked }`autoscan2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_entrypoint:
        ```

    ??? variable string "`autoscan_role_docker_env_file`{ .sb-show-on-unchecked }`autoscan2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_env_file:
        ```

    ??? variable bool "`autoscan_role_docker_labels_use_common`{ .sb-show-on-unchecked }`autoscan2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_labels_use_common:
        ```

    ??? variable bool "`autoscan_role_docker_read_only`{ .sb-show-on-unchecked }`autoscan2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_read_only:
        ```

    ??? variable string "`autoscan_role_docker_runtime`{ .sb-show-on-unchecked }`autoscan2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_runtime:
        ```

    ??? variable list "`autoscan_role_docker_sysctls`{ .sb-show-on-unchecked }`autoscan2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_sysctls:
        ```

    ??? variable list "`autoscan_role_docker_ulimits`{ .sb-show-on-unchecked }`autoscan2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        autoscan_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        autoscan2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`autoscan_role_autoheal_enabled`{ .sb-show-on-unchecked }`autoscan2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        autoscan_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        autoscan2_autoheal_enabled: true
        ```

    ??? variable string "`autoscan_role_depends_on`{ .sb-show-on-unchecked }`autoscan2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        autoscan_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        autoscan2_depends_on: ""
        ```

    ??? variable string "`autoscan_role_depends_on_delay`{ .sb-show-on-unchecked }`autoscan2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        autoscan_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        autoscan2_depends_on_delay: "0"
        ```

    ??? variable string "`autoscan_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`autoscan2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        autoscan_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        autoscan2_depends_on_healthchecks:
        ```

    ??? variable bool "`autoscan_role_diun_enabled`{ .sb-show-on-unchecked }`autoscan2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        autoscan_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        autoscan2_diun_enabled: true
        ```

    ??? variable bool "`autoscan_role_dns_enabled`{ .sb-show-on-unchecked }`autoscan2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        autoscan_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        autoscan2_dns_enabled: true
        ```

    ??? variable bool "`autoscan_role_docker_controller`{ .sb-show-on-unchecked }`autoscan2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        autoscan_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        autoscan2_docker_controller: true
        ```

    ??? variable string "`autoscan_role_docker_image_repo`{ .sb-show-on-unchecked }`autoscan2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_image_repo:
        ```

    ??? variable string "`autoscan_role_docker_image_tag`{ .sb-show-on-unchecked }`autoscan2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_docker_image_tag:
        ```

    ??? variable bool "`autoscan_role_docker_volumes_download`{ .sb-show-on-unchecked }`autoscan2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_docker_volumes_download:
        ```

    ??? variable string "`autoscan_role_themepark_addons`{ .sb-show-on-unchecked }`autoscan2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_themepark_addons:
        ```

    ??? variable string "`autoscan_role_themepark_app`{ .sb-show-on-unchecked }`autoscan2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_themepark_app:
        ```

    ??? variable string "`autoscan_role_themepark_theme`{ .sb-show-on-unchecked }`autoscan2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_themepark_theme:
        ```

    ??? variable dict "`autoscan_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`autoscan2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        autoscan_role_traefik_api_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        autoscan2_traefik_api_endpoint:
        ```

    ??? variable string "`autoscan_role_traefik_api_middleware`{ .sb-show-on-unchecked }`autoscan2_traefik_api_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_api_middleware:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_api_middleware:
        ```

    ??? variable string "`autoscan_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`autoscan2_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_api_middleware_http:
        ```

    ??? variable bool "`autoscan_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        autoscan2_traefik_autodetect_enabled: false
        ```

    ??? variable string "`autoscan_role_traefik_certresolver`{ .sb-show-on-unchecked }`autoscan2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_certresolver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_certresolver:
        ```

    ??? variable bool "`autoscan_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        autoscan2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`autoscan_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        autoscan2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`autoscan_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        autoscan2_traefik_gzip_enabled: false
        ```

    ??? variable string "`autoscan_role_traefik_middleware_http`{ .sb-show-on-unchecked }`autoscan2_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_middleware_http:
        ```

    ??? variable bool "`autoscan_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`autoscan2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`autoscan_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`autoscan2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        autoscan_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        autoscan2_traefik_middleware_http_insecure:
        ```

    ??? variable string "`autoscan_role_traefik_priority`{ .sb-show-on-unchecked }`autoscan2_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_traefik_priority:
        ```

    ??? variable bool "`autoscan_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        autoscan2_traefik_robot_enabled: true
        ```

    ??? variable bool "`autoscan_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        autoscan_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        autoscan2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`autoscan_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`autoscan2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        autoscan_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        autoscan2_traefik_wildcard_enabled: true
        ```

    ??? variable string "`autoscan_role_web_domain`{ .sb-show-on-unchecked }`autoscan2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_web_domain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_web_domain:
        ```

    ??? variable list "`autoscan_role_web_fqdn_override`{ .sb-show-on-unchecked }`autoscan2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        autoscan_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        autoscan2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            autoscan_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "autoscan2.{{ user.domain }}"
              - "autoscan.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            autoscan2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "autoscan2.{{ user.domain }}"
              - "autoscan.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`autoscan_role_web_host_override`{ .sb-show-on-unchecked }`autoscan2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        autoscan_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        autoscan2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            autoscan_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoscan2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            autoscan2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoscan2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`autoscan_role_web_http_port`{ .sb-show-on-unchecked }`autoscan2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        autoscan_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        autoscan2_web_http_port:
        ```

    ??? variable string "`autoscan_role_web_http_scheme`{ .sb-show-on-unchecked }`autoscan2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        autoscan_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        autoscan2_web_http_scheme:
        ```

    ??? variable dict "`autoscan_role_web_http_serverstransport`{ .sb-show-on-unchecked }`autoscan2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        autoscan_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        autoscan2_web_http_serverstransport:
        ```

    ??? variable string "`autoscan_role_web_scheme`{ .sb-show-on-unchecked }`autoscan2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        autoscan_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        autoscan2_web_scheme:
        ```

    ??? variable dict "`autoscan_role_web_serverstransport`{ .sb-show-on-unchecked }`autoscan2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        autoscan_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        autoscan2_web_serverstransport:
        ```

    ??? variable string "`autoscan_role_web_subdomain`{ .sb-show-on-unchecked }`autoscan2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        autoscan_role_web_subdomain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        autoscan2_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->