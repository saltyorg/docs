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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        autoscan_instances: ["autoscan"]

        ```

    === "Example"

        ```yaml
        # Type: list
        autoscan_instances: ["autoscan", "autoscan2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        autoscan_role_paths_folder: "{{ autoscan_name }}"

        # Type: string
        autoscan_role_paths_location: "{{ server_appdata_path }}/{{ autoscan_role_paths_folder }}"

        # Type: string
        autoscan_role_paths_config_location: "{{ autoscan_role_paths_location }}/config.yml"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        autoscan2_paths_folder: "{{ autoscan_name }}"

        # Type: string
        autoscan2_paths_location: "{{ server_appdata_path }}/{{ autoscan_role_paths_folder }}"

        # Type: string
        autoscan2_paths_config_location: "{{ autoscan_role_paths_location }}/config.yml"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        autoscan_role_web_subdomain: "{{ autoscan_name }}"

        # Type: string
        autoscan_role_web_domain: "{{ user.domain }}"

        # Type: string
        autoscan_role_web_port: "3030"

        # Type: string
        autoscan_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='autoscan') + '.' + lookup('role_var', '_web_domain', role='autoscan')
                                if (lookup('role_var', '_web_subdomain', role='autoscan') | length > 0)
                                else lookup('role_var', '_web_domain', role='autoscan')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        autoscan2_web_subdomain: "{{ autoscan_name }}"

        # Type: string
        autoscan2_web_domain: "{{ user.domain }}"

        # Type: string
        autoscan2_web_port: "3030"

        # Type: string
        autoscan2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='autoscan') + '.' + lookup('role_var', '_web_domain', role='autoscan')
                            if (lookup('role_var', '_web_subdomain', role='autoscan') | length > 0)
                            else lookup('role_var', '_web_domain', role='autoscan')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        autoscan_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='autoscan') }}"

        # Type: string
        autoscan_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='autoscan') }}"

        # Type: bool (true/false)
        autoscan_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        autoscan2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='autoscan') }}"

        # Type: string
        autoscan2_dns_zone: "{{ lookup('role_var', '_web_domain', role='autoscan') }}"

        # Type: bool (true/false)
        autoscan2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        autoscan_role_traefik_regex_middleware_string: ",{{ autoscan_name }}-replacepathregex"

        # Type: string
        autoscan_role_traefik_sso_middleware: ""

        # Type: string
        autoscan_role_traefik_middleware_default: "{{ traefik_default_middleware + autoscan_role_traefik_regex_middleware_string }}"

        # Type: string
        autoscan_role_traefik_middleware_custom: ""

        # Type: string
        autoscan_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        autoscan_role_traefik_enabled: true

        # Type: bool (true/false)
        autoscan_role_traefik_api_enabled: false

        # Type: string
        autoscan_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        autoscan2_traefik_regex_middleware_string: ",{{ autoscan_name }}-replacepathregex"

        # Type: string
        autoscan2_traefik_sso_middleware: ""

        # Type: string
        autoscan2_traefik_middleware_default: "{{ traefik_default_middleware + autoscan_role_traefik_regex_middleware_string }}"

        # Type: string
        autoscan2_traefik_middleware_custom: ""

        # Type: string
        autoscan2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        autoscan2_traefik_enabled: true

        # Type: bool (true/false)
        autoscan2_traefik_api_enabled: false

        # Type: string
        autoscan2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        autoscan_role_docker_container: "{{ autoscan_name }}"

        # Image
        # Type: bool (true/false)
        autoscan_role_docker_image_pull: true

        # Type: string
        autoscan_role_docker_image_repo: "saltydk/autoscan"

        # Type: string
        autoscan_role_docker_image_tag: "latest"

        # Type: string
        autoscan_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='autoscan') }}:{{ lookup('role_var', '_docker_image_tag', role='autoscan') }}"

        # Envs
        # Type: dict
        autoscan_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"

        # Type: dict
        autoscan_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        autoscan_role_docker_volumes_default: 
          - "{{ autoscan_role_paths_location }}:/config"

        # Type: list
        autoscan_role_docker_volumes_custom: []

        # Labels
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

        # Type: dict
        autoscan_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        autoscan_role_docker_hostname: "{{ autoscan_name }}"

        # Networks
        # Type: string
        autoscan_role_docker_networks_alias: "{{ autoscan_name }}"

        # Type: list
        autoscan_role_docker_networks_default: []

        # Type: list
        autoscan_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        autoscan_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        autoscan_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        autoscan_role_docker_blkio_weight:

        # Type: int
        autoscan_role_docker_cpu_period:

        # Type: int
        autoscan_role_docker_cpu_quota:

        # Type: int
        autoscan_role_docker_cpu_shares:

        # Type: string
        autoscan_role_docker_cpus:

        # Type: string
        autoscan_role_docker_cpuset_cpus:

        # Type: string
        autoscan_role_docker_cpuset_mems:

        # Type: string
        autoscan_role_docker_kernel_memory:

        # Type: string
        autoscan_role_docker_memory:

        # Type: string
        autoscan_role_docker_memory_reservation:

        # Type: string
        autoscan_role_docker_memory_swap:

        # Type: int
        autoscan_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        autoscan_role_docker_cap_drop:

        # Type: list
        autoscan_role_docker_device_cgroup_rules:

        # Type: list
        autoscan_role_docker_device_read_bps:

        # Type: list
        autoscan_role_docker_device_read_iops:

        # Type: list
        autoscan_role_docker_device_requests:

        # Type: list
        autoscan_role_docker_device_write_bps:

        # Type: list
        autoscan_role_docker_device_write_iops:

        # Type: list
        autoscan_role_docker_devices:

        # Type: string
        autoscan_role_docker_devices_default:

        # Type: bool (true/false)
        autoscan_role_docker_privileged:

        # Type: list
        autoscan_role_docker_security_opts:

        # Networking
        # Type: list
        autoscan_role_docker_dns_opts:

        # Type: list
        autoscan_role_docker_dns_search_domains:

        # Type: list
        autoscan_role_docker_dns_servers:

        # Type: dict
        autoscan_role_docker_hosts:

        # Type: string
        autoscan_role_docker_hosts_use_common:

        # Type: string
        autoscan_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        autoscan_role_docker_keep_volumes:

        # Type: list
        autoscan_role_docker_mounts:

        # Type: string
        autoscan_role_docker_volume_driver:

        # Type: list
        autoscan_role_docker_volumes_from:

        # Type: string
        autoscan_role_docker_volumes_global:

        # Type: string
        autoscan_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        autoscan_role_docker_healthcheck:

        # Type: bool (true/false)
        autoscan_role_docker_init:

        # Type: string
        autoscan_role_docker_log_driver:

        # Type: dict
        autoscan_role_docker_log_options:

        # Type: bool (true/false)
        autoscan_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        autoscan_role_docker_auto_remove:

        # Type: list
        autoscan_role_docker_capabilities:

        # Type: string
        autoscan_role_docker_cgroup_parent:

        # Type: string
        autoscan_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        autoscan_role_docker_cleanup:

        # Type: list
        autoscan_role_docker_commands:

        # Type: string
        autoscan_role_docker_create_timeout:

        # Type: string
        autoscan_role_docker_domainname:

        # Type: string
        autoscan_role_docker_entrypoint:

        # Type: string
        autoscan_role_docker_env_file:

        # Type: list
        autoscan_role_docker_exposed_ports:

        # Type: string
        autoscan_role_docker_force_kill:

        # Type: list
        autoscan_role_docker_groups:

        # Type: int
        autoscan_role_docker_healthy_wait_timeout:

        # Type: string
        autoscan_role_docker_ipc_mode:

        # Type: string
        autoscan_role_docker_kill_signal:

        # Type: string
        autoscan_role_docker_labels_use_common:

        # Type: list
        autoscan_role_docker_links:

        # Type: bool (true/false)
        autoscan_role_docker_oom_killer:

        # Type: int
        autoscan_role_docker_oom_score_adj:

        # Type: bool (true/false)
        autoscan_role_docker_paused:

        # Type: string
        autoscan_role_docker_pid_mode:

        # Type: list
        autoscan_role_docker_ports:

        # Type: bool (true/false)
        autoscan_role_docker_read_only:

        # Type: bool (true/false)
        autoscan_role_docker_recreate:

        # Type: int
        autoscan_role_docker_restart_retries:

        # Type: string
        autoscan_role_docker_runtime:

        # Type: string
        autoscan_role_docker_shm_size:

        # Type: int
        autoscan_role_docker_stop_timeout:

        # Type: dict
        autoscan_role_docker_storage_opts:

        # Type: list
        autoscan_role_docker_sysctls:

        # Type: list
        autoscan_role_docker_tmpfs:

        # Type: list
        autoscan_role_docker_ulimits:

        # Type: string
        autoscan_role_docker_user:

        # Type: string
        autoscan_role_docker_userns_mode:

        # Type: string
        autoscan_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        autoscan2_docker_container: "{{ autoscan_name }}"

        # Image
        # Type: bool (true/false)
        autoscan2_docker_image_pull: true

        # Type: string
        autoscan2_docker_image_repo: "saltydk/autoscan"

        # Type: string
        autoscan2_docker_image_tag: "latest"

        # Type: string
        autoscan2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='autoscan') }}:{{ lookup('role_var', '_docker_image_tag', role='autoscan') }}"

        # Envs
        # Type: dict
        autoscan2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"

        # Type: dict
        autoscan2_docker_envs_custom: {}

        # Volumes
        # Type: list
        autoscan2_docker_volumes_default: 
          - "{{ autoscan_role_paths_location }}:/config"

        # Type: list
        autoscan2_docker_volumes_custom: []

        # Labels
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

        # Type: dict
        autoscan2_docker_labels_custom: {}

        # Hostname
        # Type: string
        autoscan2_docker_hostname: "{{ autoscan_name }}"

        # Networks
        # Type: string
        autoscan2_docker_networks_alias: "{{ autoscan_name }}"

        # Type: list
        autoscan2_docker_networks_default: []

        # Type: list
        autoscan2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        autoscan2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        autoscan2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        autoscan2_docker_blkio_weight:
        # Type: int
        autoscan2_docker_cpu_period:
        # Type: int
        autoscan2_docker_cpu_quota:
        # Type: int
        autoscan2_docker_cpu_shares:
        # Type: string
        autoscan2_docker_cpus:
        # Type: string
        autoscan2_docker_cpuset_cpus:
        # Type: string
        autoscan2_docker_cpuset_mems:
        # Type: string
        autoscan2_docker_kernel_memory:
        # Type: string
        autoscan2_docker_memory:
        # Type: string
        autoscan2_docker_memory_reservation:
        # Type: string
        autoscan2_docker_memory_swap:
        # Type: int
        autoscan2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        autoscan2_docker_cap_drop:
        # Type: list
        autoscan2_docker_device_cgroup_rules:
        # Type: list
        autoscan2_docker_device_read_bps:
        # Type: list
        autoscan2_docker_device_read_iops:
        # Type: list
        autoscan2_docker_device_requests:
        # Type: list
        autoscan2_docker_device_write_bps:
        # Type: list
        autoscan2_docker_device_write_iops:
        # Type: list
        autoscan2_docker_devices:
        # Type: string
        autoscan2_docker_devices_default:
        # Type: bool (true/false)
        autoscan2_docker_privileged:
        # Type: list
        autoscan2_docker_security_opts:

        # Networking
        # Type: list
        autoscan2_docker_dns_opts:
        # Type: list
        autoscan2_docker_dns_search_domains:
        # Type: list
        autoscan2_docker_dns_servers:
        # Type: dict
        autoscan2_docker_hosts:
        # Type: string
        autoscan2_docker_hosts_use_common:
        # Type: string
        autoscan2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        autoscan2_docker_keep_volumes:
        # Type: list
        autoscan2_docker_mounts:
        # Type: string
        autoscan2_docker_volume_driver:
        # Type: list
        autoscan2_docker_volumes_from:
        # Type: string
        autoscan2_docker_volumes_global:
        # Type: string
        autoscan2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        autoscan2_docker_healthcheck:
        # Type: bool (true/false)
        autoscan2_docker_init:
        # Type: string
        autoscan2_docker_log_driver:
        # Type: dict
        autoscan2_docker_log_options:
        # Type: bool (true/false)
        autoscan2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        autoscan2_docker_auto_remove:
        # Type: list
        autoscan2_docker_capabilities:
        # Type: string
        autoscan2_docker_cgroup_parent:
        # Type: string
        autoscan2_docker_cgroupns_mode:
        # Type: bool (true/false)
        autoscan2_docker_cleanup:
        # Type: list
        autoscan2_docker_commands:
        # Type: string
        autoscan2_docker_create_timeout:
        # Type: string
        autoscan2_docker_domainname:
        # Type: string
        autoscan2_docker_entrypoint:
        # Type: string
        autoscan2_docker_env_file:
        # Type: list
        autoscan2_docker_exposed_ports:
        # Type: string
        autoscan2_docker_force_kill:
        # Type: list
        autoscan2_docker_groups:
        # Type: int
        autoscan2_docker_healthy_wait_timeout:
        # Type: string
        autoscan2_docker_ipc_mode:
        # Type: string
        autoscan2_docker_kill_signal:
        # Type: string
        autoscan2_docker_labels_use_common:
        # Type: list
        autoscan2_docker_links:
        # Type: bool (true/false)
        autoscan2_docker_oom_killer:
        # Type: int
        autoscan2_docker_oom_score_adj:
        # Type: bool (true/false)
        autoscan2_docker_paused:
        # Type: string
        autoscan2_docker_pid_mode:
        # Type: list
        autoscan2_docker_ports:
        # Type: bool (true/false)
        autoscan2_docker_read_only:
        # Type: bool (true/false)
        autoscan2_docker_recreate:
        # Type: int
        autoscan2_docker_restart_retries:
        # Type: string
        autoscan2_docker_runtime:
        # Type: string
        autoscan2_docker_shm_size:
        # Type: int
        autoscan2_docker_stop_timeout:
        # Type: dict
        autoscan2_docker_storage_opts:
        # Type: list
        autoscan2_docker_sysctls:
        # Type: list
        autoscan2_docker_tmpfs:
        # Type: list
        autoscan2_docker_ulimits:
        # Type: string
        autoscan2_docker_user:
        # Type: string
        autoscan2_docker_userns_mode:
        # Type: string
        autoscan2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        autoscan_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        autoscan_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        autoscan_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        autoscan_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        autoscan_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        autoscan_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        autoscan_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        autoscan_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        autoscan_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        autoscan_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        autoscan_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        autoscan_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        autoscan_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            autoscan_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "autoscan2.{{ user.domain }}"
              - "autoscan.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            autoscan_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoscan2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

    === "Instance-level"

        Override for a specific instance (e.g., `autoscan2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        autoscan2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        autoscan2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        autoscan2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        autoscan2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        autoscan2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        autoscan2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        autoscan2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        autoscan2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        autoscan2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        autoscan2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        autoscan2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        autoscan2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        autoscan2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        autoscan2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        autoscan2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        autoscan2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        autoscan2_web_scheme:

        ```

        1.  Example:

            ```yaml
            autoscan2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "autoscan2.{{ user.domain }}"
              - "autoscan.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            autoscan2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoscan2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Sonarr](sonarr.md).
