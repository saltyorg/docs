---
hide:
  - tags
tags:
  - accounts
  - settings
  - advanced
---

# Accounts and Settings

!!! warning
    This is a reference discussing an aspect of the [install process](../saltbox/install/install.md#step-2-configuration).
    If you are looking for the steps to follow to install, they are [here](../saltbox/install/install.md).

On this page, we break down the options available in the following files:

- `/srv/git/saltbox/accounts.yml`
- `/srv/git/saltbox/settings.yml`
- `/srv/git/saltbox/adv_settings.yml`

IMPORTANT: If you make changes to values in these files, you will have to run the relevant role[s] to make them take effect. For example, if you change traefik-related settings, you will need to rerun the traefik tag for them to take effect. The only thing that looks at these settings files is the Ansible script.

## Options in accounts.yml

**Note**: There must always be a space between the key and the value in YAML files. `key: value` NOT `key:value`

Each tab shows a "section" in the file.

=== "apprise"
    ```yaml
    apprise:
    ```

    `apprise` - Apprise notification URL

    This parameter is optional.
    Information about constructing the URL can be found [here](https://github.com/caronc/apprise#supported-notifications).
    This will be used to send out messages during certain tasks (e.g. backup).

    This parameter is not nested:

    ```yaml
    apprise: somescheme://something_else_here/perhaps_a_token
    ```

    not

    ```yaml
    apprise:
      somescheme://something_else_here/perhaps_a_token
    ```

=== "cloudflare"
    ```yaml
    cloudflare:
      email:
      api:
    ```

    `email`: E-mail address used for the Cloudflare account.

    `api`: [Global API Key](domain.md#get-a-free-cloudflare-api-key).

    These parameters are optional.
    Default is blank.
    Fill this in to have Saltbox add subdomains on Cloudflare, automatically; leave it blank, to have all Cloudflare related functions disabled.
    Cloudflare does not support all top-level domains though its API. Refer to [this page](https://support.cloudflare.com/hc/en-us/articles/360020296512-DNS-Troubleshooting-FAQ#h_84167303211544035341531). As of 2022/11/03:  "DNS API cannot be used for domains with .cf, .ga, .gq, .ml, or .tk TLDs."

=== "dockerhub"
    ```yaml
    dockerhub:
      user:
      token:
    ```

    `user` - Docker Hub username.

    `token` - Docker Hub access token.

    Note that this is a Docker Hub *token*, not your Docker Hub password. You create one of these in the security tab of your account settings at dockerhub, and it will look something like: `dckr_pat_EZ-YVvzrb_OzZyToNyGeEzErBiLl`

    This parameter is optional.
    Entering Dockerhub credentials increases the number of images one can pull.

=== "user"
    ```yaml
    ---
    user:
      name: seed
      pass: password1234
      domain: xYOUR_DOMAIN_NAMEx
      email: your@email.com
      ssh_key:
    ```

    `name`: User name for the server.

    This parameter is **required**.
    If user account with this name does not already exist, it will be created during install.
    Also used to create first-time logins for various apps.
    Default is `seed`.

    `pass`: Password for the user account and for misc apps.

    This parameter is **required**. Minimum 12 characters.
    Sets password for the server's user account when creating a new account. This will not change the password of an existing account.
    Also used to create first-time logins for NZBGet, qbittorrent, NZBHydra2, and potentially other apps.
    Don't leave it blank, even if you are planning to use SSH keys to connect to your box. This user and password are used to set up authentication for some applications in this repo and Sandbox, and a blank password may cause trouble there.
    Don't leave it as `password1234`.
    See the [password considerations](#password-considerations) below.
    [Relevant XKCD](https://xkcd.com/936/)

    `domain`: Domain name for the Saltbox server.

    This parameter is **required**.
    If you don't have one, see [here](domain.md).
    This should be the domain "below" the saltbox subdomains. For example, if you want to access Sonarr at "sonarr.xYOUR_DOMAIN_NAMEx", enter "xYOUR_DOMAIN_NAMEx". If you want "sonarr.foo.xYOUR_DOMAIN_NAMEx", enter "foo.xYOUR_DOMAIN_NAMEx".

    `email`: E-mail address.

    This parameter is **required** if you're using the reverse proxy.
    This is used for the Let's Encrypt SSL certificates.
    It does not have to be an email address at the domain above.

    `ssh_key`: SSH Key

    This parameter is optional.
    This is used to provision a SSH key in your user's `authorized_keys` file
    This parameter accepts either the public key or a GitHub url (i.e. [https://github.com/charlie.keys](https://github.com/charlie.keys)) which will pull the keys you have added to your GitHub account.

---

## Options in settings.yml

**Note:** Having `{{ user }}` in the path tells Ansible to fill in the username, automatically. You do not need to fill in your actual username.

**Note**: There must always be a space between the key and the value in YAML files. `key: value` NOT `key:value`

Each tab shows a "section" in the file.

=== "authelia"
    ```yaml
    authelia:
      master: yes
      subdomain: login
    ```

    `master` - Is this the master machine in a split feeder/media setup?

    `subdomain` - subdomain for the Authelia login page

    Default is `login`.

=== "downloads"
    ```yaml
    ---
    downloads: /mnt/unionfs/downloads
    ```

    `downloads`: Where downloads go.

    Default is `/mnt/unionfs/downloads`.

=== "rclone"
    ```yaml
    rclone:
      enabled: yes
      remotes:
        - remote: google
          settings:
            enable_refresh: no
            mount: yes
            template: google
            union: yes
            upload: yes
            upload_from: /mnt/local/Media
            vfs_cache:
              enabled: no
              max_age: 504h
              size: 50G
      version: latest
    ```

    `enabled`: Use this to toggle Rclone related deployments like mounts and cloudplow.

    `remotes`: This variable takes a list of dictionaries formatted like the example. Add as many remotes as you wish, like this:

    ```yaml
    rclone:
      enabled: yes
      remotes:
        - remote: google
          settings:
            mount: yes
            template: google
          ...
        - remote: dropbox
          settings:
            mount: no
            template: dropbox
          ...
        - remote: minio
          settings:
            mount: yes
            template: /opt/mount-templates/custom/myminio.j2
          ...
    ```

    `remotes/remote`: The name of the rclone remote for this mount. You can also specify a path to use for the remote. `remote: "google:Media"` or `remote: "my-sftp:/path/to/my/files"`  Quotes are important.

    `remotes/settings/enable_refresh`: Toggles whether this remote required a refresh service to look for new files [for example, an `sftp` remote].

    `remotes/settings/mount`: Toggles whether you want this remote mounted in the file system.

    `remotes/settings/template`: The name of the template you want to use for the mount. Currently Saltbox supports 4 options: `google`, `dropbox`, `sftp` and a path to a file ("/opt/mount-templates/remote.j2") containing either jinja2 template or an actual copy of a systemd service file. A [community repo](https://github.com/saltyorg/mount-templates) is maintained of user submitted mount options which can be referenced via path (i.e. `/opt/mount-templates/generic.j2`.) We recommend saving your own custom templates/services in `/opt/mount-templates/custom` to ensure they are backed up and not subject to being overwritten by the repo.

    `remotes/settings/union`: Toggles whether you want to add this remote mount to `/mnt/unionfs`. This requires that `mount` be enabled.

    `remotes/settings/upload`: Toggles whether you intend to upload to this remote using Cloudplow.

    `remotes/settings/upload_from`: The local path Cloudplow will use to upload from if the remote was upload enabled.

    `remotes/settings/vfs_cache/enabled`: Toggle for using Rclone VFS file cache.

    `remotes/settings/vfs_cache/max_age`: Defines the max age of files in the cache.

    `remotes/settings/vfs_cache/size`: Defines the max size of the cache. The cache can grow above this value in actual usage (polls the cache once a minute) so leave some headroom when using this.

    `version`: Rclone version that is installed by Saltbox.
    Choices are `latest`, `current`, `beta`, or a specific version number (e.g. `1.42`).
    Default is `latest`.

=== "shell"
    ```yaml
    shell: bash
    ```

    `shell`: Type of shell to use.

    Choices are `bash` or `zsh`.
    Default is `bash`.

=== "transcodes"
    ```yaml
    transcodes: /mnt/local/transcodes
    ```

    `transcodes`: Path of temporary transcoding files.

    Default is `"/mnt/local/transcodes"`.

    Note: It is recommended to **not** use `/tmp` or `/dev/shm` as a transcode location because the paths are cleared on reboots, causing Docker to create the folder as root and Plex transcoder to crash. Another reason why not to: [https://forums.plex.tv/discussion/comment/1502936/#Comment_1502936](https://forums.plex.tv/discussion/comment/1502936/#Comment_1502936).

---

## Options in adv_settings.yml

**Note**: There must always be a space between the key and the value in YAML files. `key: value` NOT `key:value`

Each tab shows a "section" in the file.

=== "dns"
    ```yaml
    dns:
      ipv4: yes
      ipv6: no
      proxied: no
    ```

    `ipv4`: Enable/disable IPv4 configuration.

    Default is `yes`.

    `ipv6`: Enable/disable IPv6 configuration.

    Default is `no`.

    `proxied` - Controls whether Cloudflare records should be "proxied" or "DNS only".

    Default is `no`.

    This is a global flag; if you want to override this for individual apps you can do so in the inventory.

=== "docker"
    ```yaml
    docker:
      json_driver: no
    ```

    `json_driver` - make docker logs available as JSON

=== "gpu"
    ```yaml
    gpu:
      intel: yes
    ```

    `intel`: Should system be set up for Intel GPU?

    Default is `yes`.

=== "mounts"
    ```yaml
    mounts:
      ipv4_only: no
    ```

    `ipv4_only`: Should Rclone use IPv4 only?

    Default is `no`.

=== "system"
    ```yaml
    ---
    system:
      timezone: auto
    ```

    `timezone`: Timezone to use on the server.

    Default is `auto`, which will pick the timezone based on geolocation of the server.
    Enter a "TZ database name" as shown in [this table](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). For example, "America/Costa_Rica".
    `timedatectl list-timezones` at your server's command prompt will also list the options.

=== "traefik"
    ```yaml
    traefik:
      cert:
        http_validation: no
        zerossl: no
      error_pages: no
      hsts: no
      metrics: no
      provider: cloudflare
      subdomains:
        dash: dash
        metrics: metrics
      tracing: no
    ```

    `cert.http_validation`: Use HTTP (HTTP-01) certificate validation method.
    Required if not using Cloudflare.

    Default is `no`.

    `cert.zerossl`: Use ZeroSSL instead of Let's Encrypt for generation of certificates.

    Default is `no`.

    `error_pages`: enable styled error pages.

    Default is `no`.
    See [here](../advanced/styled-error-pages.md) for configuration details.

    `hsts`: enable [HSTS](https://developer.mozilla.org/en-US/docs/Glossary/HSTS).

    Default is `no`.

    `metrics`: enable metrics subdomain.

    Default is `no`.

    `provider`: DNS provider.

    Default is `cloudflare`.

    `subdomain.dash`: traefik dashboard subdomain.

    Default is `dash`.

    `subdomain.metrics`: traefik metrics subdomain.

    Default is `metrics`.

    `tracing`: Enable tracing.

    Default is `no`.

---

## Password considerations

Your chosen password must have a minimum of 12 characters.

These are a YAML files, and values you enter here are subject to YAML file format rules. If you use special characters in your password, wrap the password in quotes [or escape the characters correctly, if you are familiar with that concept]. It would be easiest to avoid using quote characters themselves within your password.

For example:

- `pass: MyP4s5w0rd1s4w350m3`
- `pass: "!@#$%^&*"(){`
- `pass: multiple words work fine unquoted`
- `pass: "or quote them to be safe"`
