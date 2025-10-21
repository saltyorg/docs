---
hide:
  - tags
tags:
  - autoscan
---

# Autoscan

## What is it?

[Autoscan](https://github.com/Cloudbox/autoscan) replaces the default Plex, Emby, and Jellyfin behaviour for picking up file changes on the file system. Autoscan integrates with Sonarr, Radarr, Lidarr and Google Shared Drives to fetch changes in near real-time without relying on the file system.

Autoscan is a rewrite of the original Plex Autoscan written in the Go language. In addition, this rewrite introduces a more modular approach and should be easy to extend in the future.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Cloudbox/autoscan){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Cloudbox/autoscan){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Cloudbox/autoscan){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/cloudb0x/autoscan){: .header-icons } |

## Setup

The Plex API is known to have trouble when scanning items into empty libraries.  You should add at least one item to each Plex library and perform a manual scan as a first step.  If you don't do this, things may not get scanned into Plex in response to autoscan's requests.

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
    - url: https://plex.DOMAIN.TLD # plex
      token: YOUR_PLEX_TOKEN
```

Then edit the anchors section:

```yaml
anchors:
  - /mnt/unionfs/mounted.bin
```

To reflect your own configuration.

YOU PROBABLY NEED TO CREATE THIS FILE OR FILES YOURSELF.  The regular saltbox install does not do it for you.

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
To create one of these files on *each distinct element* of cloud storage.  If you're using Dropbox, there is just one.  If you have eleven OneDrive mounts, you need to create eleven of these.

Do this on each rclone remote that you have *mounted*. For example, if you're using box.com and have three remotes [`box_remote`, `box_crypt`, `chunker_remote`], run this command on the last one, `chunker_remote`, since that';s the remote that you are mounting.

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
Autoscan uses these to determine if your cloud storage is mounted and visible; if autoscan can't see these files, no scans will be sent to Plex since doing so would empty your library as Plex removed all the files it can no longer see [assuming that "empty trash on scan" is enabled].
<br />
<br />
There's nothing special about the contents of these files; autoscan just needs to see that they exist.  Typically they are empty.
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
Strictly speaking, no, not with the way saltbox sets up the mounts.  All those shared drives are part of a union remote, and the union remote is mounted, so there's really no possibility that some of those files would be present but not others.  Any one of them is probably sufficient.
<br />
<br />
However, there's no reason *not* to include them all as you can grab the list with a single command and a copy-paste.  You save a few keystrokes by not including all of them [you don't have to copy-paste `  - ` in front of those few lines], but in thinking about it at all you've spent the same amount of time.  Reading this question and answer have taken more time than it would have taken to include all of them as a belt-and-suspenders measure.
<br />
<br />
</details>

<details>
<summary>Is there something magic about the name `mounted.bin`?</summary>
<br />
<br />
No.  These files can be named whatever you want.  If you don't like `mounted.bin` and woudl rather use `black.sabbath` or whatever, go ahead.  Autoscan is just going to verify that the file you specify exists so autoscan knows it is safe to send scans to Plex.
<br />
<br />
</details>

You will set up the webhooks for radarr/sonarr/lidarr as part of their setup, so they aren't discussed here

### Manual Scan URL

The manual scan URL will be https://autoscan.YOUR_DOMAIN/triggers/manual.  Usage is described in the autoscan docs linked below.

### A-Train

Autoscan can monitor **Google Drive** changes via a trigger called "Bernard".  The code behind Bernard can sometimes get out of sync with the state of Google Drive and miss things, so now we are using A-Train.

**IMPORTANT**:
You only need to set this up if you are planning to add media to **Google Drive** directly, *outside* the usual Radarr/Sonarr channels, or if you are monitoring a Shared Drive where new media appears outside those channels.  If you are not planning to do that, you can skip this portion of the setup.

**IMPORTANT**:
A-Train does not support anything other than **Google Drive**, as it uses the Google Drive API to do its work.

"A-Train" is a rewrite of the Bernard concepts, and is currently available as a second docker image as part of Sandbox.  It will likely be integrated into autoscan at some point in the future.

!!! warning
    A-Train supports **only** *unencrypted* Google Shared Drives authenticated via Service Accounts.  It *does not* support encrypted drives, My Drive, or authentication via Client ID/Secret or other means.

Enter the names of the remotes you want to monitor in the [sandbox settings.yml](../sandbox/settings.md). The Remotes can be either drive remotes or union remotes. You may use ```rclone listremotes``` to get your drive remotes.

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

Copy one of your service account files from its current location to `/opt/a-train/account.json`.  Remember to rename your service account file to "`account.json`".

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

- [:octicons-link-16: Documentation](https://github.com/Cloudbox/autoscan){: .header-icons }

## Next

Are you setting Saltbox up for the first time?  Continue to [Sonarr](sonarr.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `autoscan_instances`.

    === "Role-level Override"

        Applies to all instances of autoscan:

        ```yaml
        autoscan_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `autoscan2`):

        ```yaml
        autoscan2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `autoscan_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `autoscan_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`autoscan_instances`"

        ```yaml
        # Type: list
        autoscan_instances: ["autoscan"]
        ```

        !!! example

            ```yaml
            # Type: list
            autoscan_instances: ["autoscan", "autoscan2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`autoscan_role_paths_folder`"

            ```yaml
            # Type: string
            autoscan_role_paths_folder: "{{ autoscan_name }}"
            ```

        ??? variable string "`autoscan_role_paths_location`"

            ```yaml
            # Type: string
            autoscan_role_paths_location: "{{ server_appdata_path }}/{{ autoscan_role_paths_folder }}"
            ```

        ??? variable string "`autoscan_role_paths_config_location`"

            ```yaml
            # Type: string
            autoscan_role_paths_config_location: "{{ autoscan_role_paths_location }}/config.yml"
            ```

    === "Instance-level"

        ??? variable string "`autoscan2_paths_folder`"

            ```yaml
            # Type: string
            autoscan2_paths_folder: "{{ autoscan_name }}"
            ```

        ??? variable string "`autoscan2_paths_location`"

            ```yaml
            # Type: string
            autoscan2_paths_location: "{{ server_appdata_path }}/{{ autoscan_role_paths_folder }}"
            ```

        ??? variable string "`autoscan2_paths_config_location`"

            ```yaml
            # Type: string
            autoscan2_paths_config_location: "{{ autoscan_role_paths_location }}/config.yml"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`autoscan_role_web_subdomain`"

            ```yaml
            # Type: string
            autoscan_role_web_subdomain: "{{ autoscan_name }}"
            ```

        ??? variable string "`autoscan_role_web_domain`"

            ```yaml
            # Type: string
            autoscan_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`autoscan_role_web_port`"

            ```yaml
            # Type: string
            autoscan_role_web_port: "3030"
            ```

        ??? variable string "`autoscan_role_web_url`"

            ```yaml
            # Type: string
            autoscan_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='autoscan') + '.' + lookup('role_var', '_web_domain', role='autoscan')
                                    if (lookup('role_var', '_web_subdomain', role='autoscan') | length > 0)
                                    else lookup('role_var', '_web_domain', role='autoscan')) }}"
            ```

    === "Instance-level"

        ??? variable string "`autoscan2_web_subdomain`"

            ```yaml
            # Type: string
            autoscan2_web_subdomain: "{{ autoscan_name }}"
            ```

        ??? variable string "`autoscan2_web_domain`"

            ```yaml
            # Type: string
            autoscan2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`autoscan2_web_port`"

            ```yaml
            # Type: string
            autoscan2_web_port: "3030"
            ```

        ??? variable string "`autoscan2_web_url`"

            ```yaml
            # Type: string
            autoscan2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='autoscan') + '.' + lookup('role_var', '_web_domain', role='autoscan')
                                if (lookup('role_var', '_web_subdomain', role='autoscan') | length > 0)
                                else lookup('role_var', '_web_domain', role='autoscan')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`autoscan_role_dns_record`"

            ```yaml
            # Type: string
            autoscan_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='autoscan') }}"
            ```

        ??? variable string "`autoscan_role_dns_zone`"

            ```yaml
            # Type: string
            autoscan_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='autoscan') }}"
            ```

        ??? variable bool "`autoscan_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`autoscan2_dns_record`"

            ```yaml
            # Type: string
            autoscan2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='autoscan') }}"
            ```

        ??? variable string "`autoscan2_dns_zone`"

            ```yaml
            # Type: string
            autoscan2_dns_zone: "{{ lookup('role_var', '_web_domain', role='autoscan') }}"
            ```

        ??? variable bool "`autoscan2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`autoscan_role_traefik_regex_middleware_string`"

            ```yaml
            # Type: string
            autoscan_role_traefik_regex_middleware_string: ",{{ autoscan_name }}-replacepathregex"
            ```

        ??? variable string "`autoscan_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            autoscan_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`autoscan_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            autoscan_role_traefik_middleware_default: "{{ traefik_default_middleware + autoscan_role_traefik_regex_middleware_string }}"
            ```

        ??? variable string "`autoscan_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            autoscan_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`autoscan_role_traefik_certresolver`"

            ```yaml
            # Type: string
            autoscan_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`autoscan_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_traefik_enabled: true
            ```

        ??? variable bool "`autoscan_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_traefik_api_enabled: false
            ```

        ??? variable string "`autoscan_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            autoscan_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`autoscan2_traefik_regex_middleware_string`"

            ```yaml
            # Type: string
            autoscan2_traefik_regex_middleware_string: ",{{ autoscan_name }}-replacepathregex"
            ```

        ??? variable string "`autoscan2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            autoscan2_traefik_sso_middleware: ""
            ```

        ??? variable string "`autoscan2_traefik_middleware_default`"

            ```yaml
            # Type: string
            autoscan2_traefik_middleware_default: "{{ traefik_default_middleware + autoscan_role_traefik_regex_middleware_string }}"
            ```

        ??? variable string "`autoscan2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            autoscan2_traefik_middleware_custom: ""
            ```

        ??? variable string "`autoscan2_traefik_certresolver`"

            ```yaml
            # Type: string
            autoscan2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`autoscan2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_traefik_enabled: true
            ```

        ??? variable bool "`autoscan2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_traefik_api_enabled: false
            ```

        ??? variable string "`autoscan2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            autoscan2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`autoscan_role_docker_container`"

            ```yaml
            # Type: string
            autoscan_role_docker_container: "{{ autoscan_name }}"
            ```

        ##### Image

        ??? variable bool "`autoscan_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_image_pull: true
            ```

        ??? variable string "`autoscan_role_docker_image_repo`"

            ```yaml
            # Type: string
            autoscan_role_docker_image_repo: "saltydk/autoscan"
            ```

        ??? variable string "`autoscan_role_docker_image_tag`"

            ```yaml
            # Type: string
            autoscan_role_docker_image_tag: "latest"
            ```

        ??? variable string "`autoscan_role_docker_image`"

            ```yaml
            # Type: string
            autoscan_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='autoscan') }}:{{ lookup('role_var', '_docker_image_tag', role='autoscan') }}"
            ```

        ##### Envs

        ??? variable dict "`autoscan_role_docker_envs_default`"

            ```yaml
            # Type: dict
            autoscan_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`autoscan_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            autoscan_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`autoscan_role_docker_volumes_default`"

            ```yaml
            # Type: list
            autoscan_role_docker_volumes_default: 
              - "{{ autoscan_role_paths_location }}:/config"
            ```

        ??? variable list "`autoscan_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            autoscan_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable list "`autoscan_role_docker_labels_default`"

            ```yaml
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

        ??? variable dict "`autoscan_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            autoscan_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`autoscan_role_docker_hostname`"

            ```yaml
            # Type: string
            autoscan_role_docker_hostname: "{{ autoscan_name }}"
            ```

        ##### Networks

        ??? variable string "`autoscan_role_docker_networks_alias`"

            ```yaml
            # Type: string
            autoscan_role_docker_networks_alias: "{{ autoscan_name }}"
            ```

        ??? variable list "`autoscan_role_docker_networks_default`"

            ```yaml
            # Type: list
            autoscan_role_docker_networks_default: []
            ```

        ??? variable list "`autoscan_role_docker_networks_custom`"

            ```yaml
            # Type: list
            autoscan_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`autoscan_role_docker_restart_policy`"

            ```yaml
            # Type: string
            autoscan_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`autoscan_role_docker_state`"

            ```yaml
            # Type: string
            autoscan_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`autoscan2_docker_container`"

            ```yaml
            # Type: string
            autoscan2_docker_container: "{{ autoscan_name }}"
            ```

        ##### Image

        ??? variable bool "`autoscan2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_image_pull: true
            ```

        ??? variable string "`autoscan2_docker_image_repo`"

            ```yaml
            # Type: string
            autoscan2_docker_image_repo: "saltydk/autoscan"
            ```

        ??? variable string "`autoscan2_docker_image_tag`"

            ```yaml
            # Type: string
            autoscan2_docker_image_tag: "latest"
            ```

        ??? variable string "`autoscan2_docker_image`"

            ```yaml
            # Type: string
            autoscan2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='autoscan') }}:{{ lookup('role_var', '_docker_image_tag', role='autoscan') }}"
            ```

        ##### Envs

        ??? variable dict "`autoscan2_docker_envs_default`"

            ```yaml
            # Type: dict
            autoscan2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`autoscan2_docker_envs_custom`"

            ```yaml
            # Type: dict
            autoscan2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`autoscan2_docker_volumes_default`"

            ```yaml
            # Type: list
            autoscan2_docker_volumes_default: 
              - "{{ autoscan_role_paths_location }}:/config"
            ```

        ??? variable list "`autoscan2_docker_volumes_custom`"

            ```yaml
            # Type: list
            autoscan2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable list "`autoscan2_docker_labels_default`"

            ```yaml
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

        ??? variable dict "`autoscan2_docker_labels_custom`"

            ```yaml
            # Type: dict
            autoscan2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`autoscan2_docker_hostname`"

            ```yaml
            # Type: string
            autoscan2_docker_hostname: "{{ autoscan_name }}"
            ```

        ##### Networks

        ??? variable string "`autoscan2_docker_networks_alias`"

            ```yaml
            # Type: string
            autoscan2_docker_networks_alias: "{{ autoscan_name }}"
            ```

        ??? variable list "`autoscan2_docker_networks_default`"

            ```yaml
            # Type: list
            autoscan2_docker_networks_default: []
            ```

        ??? variable list "`autoscan2_docker_networks_custom`"

            ```yaml
            # Type: list
            autoscan2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`autoscan2_docker_restart_policy`"

            ```yaml
            # Type: string
            autoscan2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`autoscan2_docker_state`"

            ```yaml
            # Type: string
            autoscan2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`autoscan_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            autoscan_role_docker_blkio_weight:
            ```

        ??? variable int "`autoscan_role_docker_cpu_period`"

            ```yaml
            # Type: int
            autoscan_role_docker_cpu_period:
            ```

        ??? variable int "`autoscan_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            autoscan_role_docker_cpu_quota:
            ```

        ??? variable int "`autoscan_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            autoscan_role_docker_cpu_shares:
            ```

        ??? variable string "`autoscan_role_docker_cpus`"

            ```yaml
            # Type: string
            autoscan_role_docker_cpus:
            ```

        ??? variable string "`autoscan_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            autoscan_role_docker_cpuset_cpus:
            ```

        ??? variable string "`autoscan_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            autoscan_role_docker_cpuset_mems:
            ```

        ??? variable string "`autoscan_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            autoscan_role_docker_kernel_memory:
            ```

        ??? variable string "`autoscan_role_docker_memory`"

            ```yaml
            # Type: string
            autoscan_role_docker_memory:
            ```

        ??? variable string "`autoscan_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            autoscan_role_docker_memory_reservation:
            ```

        ??? variable string "`autoscan_role_docker_memory_swap`"

            ```yaml
            # Type: string
            autoscan_role_docker_memory_swap:
            ```

        ??? variable int "`autoscan_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            autoscan_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`autoscan_role_docker_cap_drop`"

            ```yaml
            # Type: list
            autoscan_role_docker_cap_drop:
            ```

        ??? variable list "`autoscan_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            autoscan_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`autoscan_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            autoscan_role_docker_device_read_bps:
            ```

        ??? variable list "`autoscan_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            autoscan_role_docker_device_read_iops:
            ```

        ??? variable list "`autoscan_role_docker_device_requests`"

            ```yaml
            # Type: list
            autoscan_role_docker_device_requests:
            ```

        ??? variable list "`autoscan_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            autoscan_role_docker_device_write_bps:
            ```

        ??? variable list "`autoscan_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            autoscan_role_docker_device_write_iops:
            ```

        ??? variable list "`autoscan_role_docker_devices`"

            ```yaml
            # Type: list
            autoscan_role_docker_devices:
            ```

        ??? variable string "`autoscan_role_docker_devices_default`"

            ```yaml
            # Type: string
            autoscan_role_docker_devices_default:
            ```

        ??? variable bool "`autoscan_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_privileged:
            ```

        ??? variable list "`autoscan_role_docker_security_opts`"

            ```yaml
            # Type: list
            autoscan_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`autoscan_role_docker_dns_opts`"

            ```yaml
            # Type: list
            autoscan_role_docker_dns_opts:
            ```

        ??? variable list "`autoscan_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            autoscan_role_docker_dns_search_domains:
            ```

        ??? variable list "`autoscan_role_docker_dns_servers`"

            ```yaml
            # Type: list
            autoscan_role_docker_dns_servers:
            ```

        ??? variable dict "`autoscan_role_docker_hosts`"

            ```yaml
            # Type: dict
            autoscan_role_docker_hosts:
            ```

        ??? variable string "`autoscan_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            autoscan_role_docker_hosts_use_common:
            ```

        ??? variable string "`autoscan_role_docker_network_mode`"

            ```yaml
            # Type: string
            autoscan_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`autoscan_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_keep_volumes:
            ```

        ??? variable list "`autoscan_role_docker_mounts`"

            ```yaml
            # Type: list
            autoscan_role_docker_mounts:
            ```

        ??? variable string "`autoscan_role_docker_volume_driver`"

            ```yaml
            # Type: string
            autoscan_role_docker_volume_driver:
            ```

        ??? variable list "`autoscan_role_docker_volumes_from`"

            ```yaml
            # Type: list
            autoscan_role_docker_volumes_from:
            ```

        ??? variable string "`autoscan_role_docker_volumes_global`"

            ```yaml
            # Type: string
            autoscan_role_docker_volumes_global:
            ```

        ??? variable string "`autoscan_role_docker_working_dir`"

            ```yaml
            # Type: string
            autoscan_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`autoscan_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            autoscan_role_docker_healthcheck:
            ```

        ??? variable bool "`autoscan_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_init:
            ```

        ??? variable string "`autoscan_role_docker_log_driver`"

            ```yaml
            # Type: string
            autoscan_role_docker_log_driver:
            ```

        ??? variable dict "`autoscan_role_docker_log_options`"

            ```yaml
            # Type: dict
            autoscan_role_docker_log_options:
            ```

        ??? variable bool "`autoscan_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`autoscan_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_auto_remove:
            ```

        ??? variable list "`autoscan_role_docker_capabilities`"

            ```yaml
            # Type: list
            autoscan_role_docker_capabilities:
            ```

        ??? variable string "`autoscan_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            autoscan_role_docker_cgroup_parent:
            ```

        ??? variable string "`autoscan_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            autoscan_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`autoscan_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_cleanup:
            ```

        ??? variable list "`autoscan_role_docker_commands`"

            ```yaml
            # Type: list
            autoscan_role_docker_commands:
            ```

        ??? variable string "`autoscan_role_docker_create_timeout`"

            ```yaml
            # Type: string
            autoscan_role_docker_create_timeout:
            ```

        ??? variable string "`autoscan_role_docker_domainname`"

            ```yaml
            # Type: string
            autoscan_role_docker_domainname:
            ```

        ??? variable string "`autoscan_role_docker_entrypoint`"

            ```yaml
            # Type: string
            autoscan_role_docker_entrypoint:
            ```

        ??? variable string "`autoscan_role_docker_env_file`"

            ```yaml
            # Type: string
            autoscan_role_docker_env_file:
            ```

        ??? variable list "`autoscan_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            autoscan_role_docker_exposed_ports:
            ```

        ??? variable string "`autoscan_role_docker_force_kill`"

            ```yaml
            # Type: string
            autoscan_role_docker_force_kill:
            ```

        ??? variable list "`autoscan_role_docker_groups`"

            ```yaml
            # Type: list
            autoscan_role_docker_groups:
            ```

        ??? variable int "`autoscan_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            autoscan_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`autoscan_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            autoscan_role_docker_ipc_mode:
            ```

        ??? variable string "`autoscan_role_docker_kill_signal`"

            ```yaml
            # Type: string
            autoscan_role_docker_kill_signal:
            ```

        ??? variable string "`autoscan_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            autoscan_role_docker_labels_use_common:
            ```

        ??? variable list "`autoscan_role_docker_links`"

            ```yaml
            # Type: list
            autoscan_role_docker_links:
            ```

        ??? variable bool "`autoscan_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_oom_killer:
            ```

        ??? variable int "`autoscan_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            autoscan_role_docker_oom_score_adj:
            ```

        ??? variable bool "`autoscan_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_paused:
            ```

        ??? variable string "`autoscan_role_docker_pid_mode`"

            ```yaml
            # Type: string
            autoscan_role_docker_pid_mode:
            ```

        ??? variable list "`autoscan_role_docker_ports`"

            ```yaml
            # Type: list
            autoscan_role_docker_ports:
            ```

        ??? variable bool "`autoscan_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_read_only:
            ```

        ??? variable bool "`autoscan_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            autoscan_role_docker_recreate:
            ```

        ??? variable int "`autoscan_role_docker_restart_retries`"

            ```yaml
            # Type: int
            autoscan_role_docker_restart_retries:
            ```

        ??? variable string "`autoscan_role_docker_runtime`"

            ```yaml
            # Type: string
            autoscan_role_docker_runtime:
            ```

        ??? variable string "`autoscan_role_docker_shm_size`"

            ```yaml
            # Type: string
            autoscan_role_docker_shm_size:
            ```

        ??? variable int "`autoscan_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            autoscan_role_docker_stop_timeout:
            ```

        ??? variable dict "`autoscan_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            autoscan_role_docker_storage_opts:
            ```

        ??? variable list "`autoscan_role_docker_sysctls`"

            ```yaml
            # Type: list
            autoscan_role_docker_sysctls:
            ```

        ??? variable list "`autoscan_role_docker_tmpfs`"

            ```yaml
            # Type: list
            autoscan_role_docker_tmpfs:
            ```

        ??? variable list "`autoscan_role_docker_ulimits`"

            ```yaml
            # Type: list
            autoscan_role_docker_ulimits:
            ```

        ??? variable string "`autoscan_role_docker_user`"

            ```yaml
            # Type: string
            autoscan_role_docker_user:
            ```

        ??? variable string "`autoscan_role_docker_userns_mode`"

            ```yaml
            # Type: string
            autoscan_role_docker_userns_mode:
            ```

        ??? variable string "`autoscan_role_docker_uts`"

            ```yaml
            # Type: string
            autoscan_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`autoscan2_docker_blkio_weight`"

            ```yaml
            # Type: int
            autoscan2_docker_blkio_weight:
            ```

        ??? variable int "`autoscan2_docker_cpu_period`"

            ```yaml
            # Type: int
            autoscan2_docker_cpu_period:
            ```

        ??? variable int "`autoscan2_docker_cpu_quota`"

            ```yaml
            # Type: int
            autoscan2_docker_cpu_quota:
            ```

        ??? variable int "`autoscan2_docker_cpu_shares`"

            ```yaml
            # Type: int
            autoscan2_docker_cpu_shares:
            ```

        ??? variable string "`autoscan2_docker_cpus`"

            ```yaml
            # Type: string
            autoscan2_docker_cpus:
            ```

        ??? variable string "`autoscan2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            autoscan2_docker_cpuset_cpus:
            ```

        ??? variable string "`autoscan2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            autoscan2_docker_cpuset_mems:
            ```

        ??? variable string "`autoscan2_docker_kernel_memory`"

            ```yaml
            # Type: string
            autoscan2_docker_kernel_memory:
            ```

        ??? variable string "`autoscan2_docker_memory`"

            ```yaml
            # Type: string
            autoscan2_docker_memory:
            ```

        ??? variable string "`autoscan2_docker_memory_reservation`"

            ```yaml
            # Type: string
            autoscan2_docker_memory_reservation:
            ```

        ??? variable string "`autoscan2_docker_memory_swap`"

            ```yaml
            # Type: string
            autoscan2_docker_memory_swap:
            ```

        ??? variable int "`autoscan2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            autoscan2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`autoscan2_docker_cap_drop`"

            ```yaml
            # Type: list
            autoscan2_docker_cap_drop:
            ```

        ??? variable list "`autoscan2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            autoscan2_docker_device_cgroup_rules:
            ```

        ??? variable list "`autoscan2_docker_device_read_bps`"

            ```yaml
            # Type: list
            autoscan2_docker_device_read_bps:
            ```

        ??? variable list "`autoscan2_docker_device_read_iops`"

            ```yaml
            # Type: list
            autoscan2_docker_device_read_iops:
            ```

        ??? variable list "`autoscan2_docker_device_requests`"

            ```yaml
            # Type: list
            autoscan2_docker_device_requests:
            ```

        ??? variable list "`autoscan2_docker_device_write_bps`"

            ```yaml
            # Type: list
            autoscan2_docker_device_write_bps:
            ```

        ??? variable list "`autoscan2_docker_device_write_iops`"

            ```yaml
            # Type: list
            autoscan2_docker_device_write_iops:
            ```

        ??? variable list "`autoscan2_docker_devices`"

            ```yaml
            # Type: list
            autoscan2_docker_devices:
            ```

        ??? variable string "`autoscan2_docker_devices_default`"

            ```yaml
            # Type: string
            autoscan2_docker_devices_default:
            ```

        ??? variable bool "`autoscan2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_privileged:
            ```

        ??? variable list "`autoscan2_docker_security_opts`"

            ```yaml
            # Type: list
            autoscan2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`autoscan2_docker_dns_opts`"

            ```yaml
            # Type: list
            autoscan2_docker_dns_opts:
            ```

        ??? variable list "`autoscan2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            autoscan2_docker_dns_search_domains:
            ```

        ??? variable list "`autoscan2_docker_dns_servers`"

            ```yaml
            # Type: list
            autoscan2_docker_dns_servers:
            ```

        ??? variable dict "`autoscan2_docker_hosts`"

            ```yaml
            # Type: dict
            autoscan2_docker_hosts:
            ```

        ??? variable string "`autoscan2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            autoscan2_docker_hosts_use_common:
            ```

        ??? variable string "`autoscan2_docker_network_mode`"

            ```yaml
            # Type: string
            autoscan2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`autoscan2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_keep_volumes:
            ```

        ??? variable list "`autoscan2_docker_mounts`"

            ```yaml
            # Type: list
            autoscan2_docker_mounts:
            ```

        ??? variable string "`autoscan2_docker_volume_driver`"

            ```yaml
            # Type: string
            autoscan2_docker_volume_driver:
            ```

        ??? variable list "`autoscan2_docker_volumes_from`"

            ```yaml
            # Type: list
            autoscan2_docker_volumes_from:
            ```

        ??? variable string "`autoscan2_docker_volumes_global`"

            ```yaml
            # Type: string
            autoscan2_docker_volumes_global:
            ```

        ??? variable string "`autoscan2_docker_working_dir`"

            ```yaml
            # Type: string
            autoscan2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`autoscan2_docker_healthcheck`"

            ```yaml
            # Type: dict
            autoscan2_docker_healthcheck:
            ```

        ??? variable bool "`autoscan2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_init:
            ```

        ??? variable string "`autoscan2_docker_log_driver`"

            ```yaml
            # Type: string
            autoscan2_docker_log_driver:
            ```

        ??? variable dict "`autoscan2_docker_log_options`"

            ```yaml
            # Type: dict
            autoscan2_docker_log_options:
            ```

        ??? variable bool "`autoscan2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`autoscan2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_auto_remove:
            ```

        ??? variable list "`autoscan2_docker_capabilities`"

            ```yaml
            # Type: list
            autoscan2_docker_capabilities:
            ```

        ??? variable string "`autoscan2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            autoscan2_docker_cgroup_parent:
            ```

        ??? variable string "`autoscan2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            autoscan2_docker_cgroupns_mode:
            ```

        ??? variable bool "`autoscan2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_cleanup:
            ```

        ??? variable list "`autoscan2_docker_commands`"

            ```yaml
            # Type: list
            autoscan2_docker_commands:
            ```

        ??? variable string "`autoscan2_docker_create_timeout`"

            ```yaml
            # Type: string
            autoscan2_docker_create_timeout:
            ```

        ??? variable string "`autoscan2_docker_domainname`"

            ```yaml
            # Type: string
            autoscan2_docker_domainname:
            ```

        ??? variable string "`autoscan2_docker_entrypoint`"

            ```yaml
            # Type: string
            autoscan2_docker_entrypoint:
            ```

        ??? variable string "`autoscan2_docker_env_file`"

            ```yaml
            # Type: string
            autoscan2_docker_env_file:
            ```

        ??? variable list "`autoscan2_docker_exposed_ports`"

            ```yaml
            # Type: list
            autoscan2_docker_exposed_ports:
            ```

        ??? variable string "`autoscan2_docker_force_kill`"

            ```yaml
            # Type: string
            autoscan2_docker_force_kill:
            ```

        ??? variable list "`autoscan2_docker_groups`"

            ```yaml
            # Type: list
            autoscan2_docker_groups:
            ```

        ??? variable int "`autoscan2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            autoscan2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`autoscan2_docker_ipc_mode`"

            ```yaml
            # Type: string
            autoscan2_docker_ipc_mode:
            ```

        ??? variable string "`autoscan2_docker_kill_signal`"

            ```yaml
            # Type: string
            autoscan2_docker_kill_signal:
            ```

        ??? variable string "`autoscan2_docker_labels_use_common`"

            ```yaml
            # Type: string
            autoscan2_docker_labels_use_common:
            ```

        ??? variable list "`autoscan2_docker_links`"

            ```yaml
            # Type: list
            autoscan2_docker_links:
            ```

        ??? variable bool "`autoscan2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_oom_killer:
            ```

        ??? variable int "`autoscan2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            autoscan2_docker_oom_score_adj:
            ```

        ??? variable bool "`autoscan2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_paused:
            ```

        ??? variable string "`autoscan2_docker_pid_mode`"

            ```yaml
            # Type: string
            autoscan2_docker_pid_mode:
            ```

        ??? variable list "`autoscan2_docker_ports`"

            ```yaml
            # Type: list
            autoscan2_docker_ports:
            ```

        ??? variable bool "`autoscan2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_read_only:
            ```

        ??? variable bool "`autoscan2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            autoscan2_docker_recreate:
            ```

        ??? variable int "`autoscan2_docker_restart_retries`"

            ```yaml
            # Type: int
            autoscan2_docker_restart_retries:
            ```

        ??? variable string "`autoscan2_docker_runtime`"

            ```yaml
            # Type: string
            autoscan2_docker_runtime:
            ```

        ??? variable string "`autoscan2_docker_shm_size`"

            ```yaml
            # Type: string
            autoscan2_docker_shm_size:
            ```

        ??? variable int "`autoscan2_docker_stop_timeout`"

            ```yaml
            # Type: int
            autoscan2_docker_stop_timeout:
            ```

        ??? variable dict "`autoscan2_docker_storage_opts`"

            ```yaml
            # Type: dict
            autoscan2_docker_storage_opts:
            ```

        ??? variable list "`autoscan2_docker_sysctls`"

            ```yaml
            # Type: list
            autoscan2_docker_sysctls:
            ```

        ??? variable list "`autoscan2_docker_tmpfs`"

            ```yaml
            # Type: list
            autoscan2_docker_tmpfs:
            ```

        ??? variable list "`autoscan2_docker_ulimits`"

            ```yaml
            # Type: list
            autoscan2_docker_ulimits:
            ```

        ??? variable string "`autoscan2_docker_user`"

            ```yaml
            # Type: string
            autoscan2_docker_user:
            ```

        ??? variable string "`autoscan2_docker_userns_mode`"

            ```yaml
            # Type: string
            autoscan2_docker_userns_mode:
            ```

        ??? variable string "`autoscan2_docker_uts`"

            ```yaml
            # Type: string
            autoscan2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`autoscan_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            autoscan_role_autoheal_enabled: true
            ```

        ??? variable string "`autoscan_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            autoscan_role_depends_on: ""
            ```

        ??? variable string "`autoscan_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            autoscan_role_depends_on_delay: "0"
            ```

        ??? variable string "`autoscan_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            autoscan_role_depends_on_healthchecks:
            ```

        ??? variable bool "`autoscan_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            autoscan_role_diun_enabled: true
            ```

        ??? variable bool "`autoscan_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            autoscan_role_dns_enabled: true
            ```

        ??? variable bool "`autoscan_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            autoscan_role_docker_controller: true
            ```

        ??? variable bool "`autoscan_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            autoscan_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`autoscan_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            autoscan_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`autoscan_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            autoscan_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`autoscan_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            autoscan_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`autoscan_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            autoscan_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`autoscan_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            autoscan_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`autoscan_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            autoscan_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`autoscan_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            autoscan_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                autoscan_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "autoscan2.{{ user.domain }}"
                  - "autoscan.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`autoscan_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            autoscan_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                autoscan_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoscan2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`autoscan_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            autoscan_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `autoscan2`):

        ??? variable bool "`autoscan2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            autoscan2_autoheal_enabled: true
            ```

        ??? variable string "`autoscan2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            autoscan2_depends_on: ""
            ```

        ??? variable string "`autoscan2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            autoscan2_depends_on_delay: "0"
            ```

        ??? variable string "`autoscan2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            autoscan2_depends_on_healthchecks:
            ```

        ??? variable bool "`autoscan2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            autoscan2_diun_enabled: true
            ```

        ??? variable bool "`autoscan2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            autoscan2_dns_enabled: true
            ```

        ??? variable bool "`autoscan2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            autoscan2_docker_controller: true
            ```

        ??? variable bool "`autoscan2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            autoscan2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`autoscan2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            autoscan2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`autoscan2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            autoscan2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`autoscan2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            autoscan2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`autoscan2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            autoscan2_traefik_robot_enabled: true
            ```

        ??? variable bool "`autoscan2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            autoscan2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`autoscan2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            autoscan2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`autoscan2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            autoscan2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                autoscan2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "autoscan2.{{ user.domain }}"
                  - "autoscan.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`autoscan2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            autoscan2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                autoscan2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoscan2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`autoscan2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            autoscan2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->