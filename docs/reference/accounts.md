# Accounts and Settings

!!! warning
    This is a reference discussing an aspect of the [install process](../../saltbox/install/install/#configuration).
    If you are looking for the steps to follow to install, they are [here](../../saltbox/install/install).

On this page, we break down the options available in the following files:

- `/srv/git/saltbox/accounts.yml`
- `/srv/git/saltbox/settings.yml`
- `/srv/git/saltbox/adv_settings.yml`

## Options in accounts.yml

**Note**: There must always be a space betwen the key and the value in YAML files.  `key: value` NOT `key:value`

---

- `user`: User information.

    - `name`: User name for the server.

        - If user account with this name does not already exist, it will be created during install.
        - Also used to create first-time logins for NZBGet, ruTorrent, NZBHydra2, and potentially other apps.
        - Default is `seed`.
        - This parameter is **required**.

    - `pass`: Password for the user account and for misc apps.

        - Sets password for the server's user account when creating a new account. This will not change the password of an existing account.
        - Also used to create first-time logins for NZBGet, ruTorrent, NZBHydra2, and potentially other apps.
        - This parameter is **required**.
        - Don't leave it blank. Even if you are planning to use SSH keys to connect to your box.  This user and password are used to set up authentication for some applications in this repo and Community, and a blank password may cause trouble there.

        - [Relevant XKCD](https://xkcd.com/936/)

        - See the [password considerations](#password-considerations) below.

    - `domain`: Domain name for the Saltbox server.

        - If you don't have one, see [here](domain.md).

        - This should be the domain "below" the saltbox subdomains.  For example, if you want to access Sonarr at "sonarr.domain.tld", enter "domain.tld".  If you want "sonarr.foo.domain.tld", enter "foo.domain.tld".

    - `email`: E-mail address.

        - This is used for the Let's Encrypt SSL certificates.
        - It does not have to be an email address at the domain above.
        - This parameter is **required** if you're using the reverse proxy.

    - `ssh_key`: SSH Key

        - This parameter is optional
        - This is used to provision a SSH key in your user's `authorized_keys` file
        - This parameter accepts either the public key or a GitHub url (i.e. [https://github.com/charlie.keys](https://github.com/charlie.keys)) which will pull the keys you have added to your GitHub account.

- `cloudflare`: Cloudflare Account

    - `email`: E-mail address used for the Cloudflare account.

    - `api`: [Global API Key](domain.md#cloudflare-api-key).

        - This parameter is optional.

        - Default is blank.

        - Fill this in to have Saltbox add subdomains on Cloudflare, automatically; leave it blank, to have all Cloudflare related functions disabled.

        - Note: if you are using a subdomain, like WHATEVER.DOMAIN.TLD, as your domain above, leave these blank. The Cloudflare automation does not work in that case and the install will stop with an error.

        - Cloudflare does not support all top-level domains though its API.  Refer to [this page](https://support.cloudflare.com/hc/en-us/articles/360020296512-DNS-Troubleshooting-FAQ#h_84167303211544035341531).  As of 2022/11/03:  "DNS API cannot be used for domains with .cf, .ga, .gq, .ml, or .tk TLDs."

- `plex`: Plex.tv account credentials.

    - This will be used to:

        - claim the Plex server under your username, and

        - generate Plex Access Tokens for apps such as Autoscan, etc.

    - `user` - Plex username or email address on the profile.

    - `pass` - Plex password. See the [password considerations](#password-considerations) below.

    - `tfa` - "yes" or "no" depending on whether you want to use the two-factor authentication [TFA] compatible Plex connection system.

    - This parameter is required.

    - Note: The "tfa" setting controls whether Saltbox uses the newer authentication method or not; this newer method is *required* for use with TFA, but will work even with it off; it's the "Open an URL, log into Plex, grant access to this app" workflow you may be familiar with from other contexts.

    - If you use the `tfa` workflow, a random client ID and a Plex Access Token will be stored in `/opt/saltbox/plex.ini` for later use.  Consider securing this file if you are running Saltbox on a shared machine.

- `dockerhub`: DockerHub account credentials.

    - Entering Dockerhub credentials increases the number of images one can pull

    - `user` - Docker Hub username.

    - `token` - Docker Hub access token.

- `apprise`: apprise url.

    - Information about constructing the URL can be found [here](https://github.com/caronc/apprise#supported-notifications).

    - This will be used to send out messages during certain tasks (e.g. backup).

    - This parameter is not nested like the others in this file.

    ```yaml

    apprise: somescheme://something_else_here/perhaps_a_token

    ```

    not

    ```yaml

    apprise:
      somescheme://something_else_here/perhaps_a_token

    ```

    - This parameter is optional.

---

## Options in settings.yml

**Note:** Having `{{user}}` in the path tells Ansible to fill in the username, automatically. You do not need to fill in your actual username.

**Note**: There must always be a space betwen the key and the value in YAML files.  `key: value` NOT `key:value`

---

- `downloads`: Where downloads go.

    - Default is `/mnt/unionfs/downloads`.

- `transcodes`: Path of temporary transcoding files.

    - Default is `"/mnt/local/transcodes"`.

    - Note: It is recommended to **not** use `/tmp` or `/dev/shm` as a transcode location because the paths are cleared on reboots, causing Docker to create the folder as root and Plex transcoder to crash. Another reason why not to: [https://forums.plex.tv/discussion/comment/1502936/#Comment_1502936](https://forums.plex.tv/discussion/comment/1502936/#Comment_1502936).

- `rclone`: Rclone options.

    - `version`: Rclone version that is installed by Saltbox.

        - Choices are `latest`, `current`, `beta`, or a specific version number (e.g. `1.42`).

        - Default is `latest`.

    - `remote`: Rclone remote that Saltbox will use to setup Rclone VFS mount and Cloudplow.

        - Default is `google`.

        - Can be left blank to run without cloud storage].

- `shell`: Type of shell to use.

    - Choices are `bash` or `zsh`.

    - Default is `bash`.

- `authelia`: Authelia options.

    - `subdomain`: subdomain for the Authelia login page

        - Default is `login`.

---

## Options in adv_settings.yml

**Note**: There must always be a space betwen the key and the value in YAML files.  `key: value` NOT `key:value`

---

- `system`: Various system-level settings.

    - `timezone`: Timezone to use on the server.

        - Default is `auto`, which will pick the timezone based on geolocation of the server.

        - Enter a "TZ database name" as shown in [this table](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  For example, "America/Costa_Rica".

        - `timedatectl list-timezones` at your server's command prompt will also list the options.

- `dns`: DNS-related settings.

    - `proxied`: Controls whether Cloudflare records should be "proxied" or "DNS only".

        - Default is `no`.

    - `ipv6`: Enable/disable ipv6 configuration.

        - Default is `no`.

  - `zerossl`: Controls whether zerossl is used.

     - Default is `no`.

- `traefik`: traefik-related settings.

    - `tls`: Use TLS (ALPN-01) certificate validation method.

        - Default is `no`.

    - `http`: Use HTTP (HTTP-01) certificate validation method.

        - Default is `no`.

    - `metrics`: enable metrics subdomain.

        - Default is `no`.

    - `tracing`: Enable tracing.

        - Default is `no`.

    - `hsts`: enable hsts.

        - Default is `no`.

    - `provider`: DNS provider.

        - Default is `cloudflare`.

    - `subdomains`: traefik subdomains.

        - `dash`: traefik dashboard subdomain.

            - Default is `dash`.

        - `metrics`: traefik metrics subdomain.

            - Default is `metrics`.

        - `jaeger`: traefik jaeger subdomain.

            - Default is `jaeger`.

    - `error_pages`: enable styled error pages.

        - Default is `no`.

        - see [here](../advanced/styled-error-pages.md) for configuration details.

- `mounts`: cloud storage mount settings.

    - `remote`: What type of remote to use.

        - Default is `rclone_vfs`. Options are `rclone_vfs` and `rclone_vfs_cache`. If selecting `rclone_vfs_cache` it is recommended to review the [rclone documentation](https://rclone.org/commands/rclone_mount/#vfs-file-caching) and review the `rclone_vfs_cache_max_size`, `rclone_vfs_cache_max_age` and (optionally) `rclone_vfs_cache_max_dir` variables for any configuration required.via the inventory system.

    - `feeder`: Should a feeder mount be created?

        - Default is `no`.

- `gpu`: GPU settings.

    - `intel`: Should system be set up for Intel GPU?

        - Default is `yes`.

    - `nvidia`: Should system be set up for NVidia GPU?

        - Default is `no`.

---

## Password considerations

These are a YAML files, and values you enter here are subject to YAML file format rules.  If you use special characters in your password, wrap the password in quotes [or escape the characters correctly, if you are familiar with that concept].  It would be easiest to avoid using quote characters themselves within your password.

For example:

- `pass: MyP4s5w0rd1s4w350m3`
- `pass: "!@#$%^&*"`
- `pass: multiple words work fine unquoted`
- `pass: "or quote them to be safe"`
