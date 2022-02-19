##  Options in accounts.yml

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
        - Leave this blank to run without the reverse proxy and access the apps via IP:PORT

    - `email`: E-mail address.

        - This is used for the Let's Encrypt SSL certificates.
        - It does not have to be an email address at the domain above.
        - This parameter is **required** if you're using the reverse proxy.

- `cloudflare`: Cloudflare Account
    - `email`: E-mail address used for the Cloudflare account.

    - `api`: [Global API Key](domain.md#cloudflare-api-key).

    - This parameter is optional.

    - Default is blank.

    - Fill this in to have Saltbox add subdomains on Cloudflare, automatically; leave it blank, to have all Cloudflare related functions disabled.

    - Note: if you are using a subdomain, like WHATEVER.DOMAIN.TLD, as your domain above, leave these blank. The Cloudflare automation does not work in that case and the install will stop with an error.

- `plex`: Plex.tv account credentials.

    - This will be used to:
        - claim the Plex server under your username, and
        - generate Plex Access Tokens for apps such as Plex Autoscan, etc.

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

    - This will be used to send out messages during certain tasks (e.g. backup).
    - This parameter is not nested like the others in this file.
    - This parameter is optional.

---

##  Options in settings.yml

**Note:** Having `{{user}}` in the path tells Ansible to fill in the username, automatically. You do not need to fill in your actual username.

---

- `downloads`: Where downloads go.

    - `nzbs`: Path for Usenet app downloads.

      - Default is `/mnt/unionfs/downloads/nzbs`.

       - Example: With the default path, NZBGet downloads would go to `/mnt/unionfs/downloads/nzbs/nzbget/completed` and SABnzbd downloads would go to `/mnt/unionfs/downloads/nzbs/sabnzbd/complete`.

    - `torrents`: Path for BitTorrent app downloads.

        - Default is `/mnt/unionfs/downloads/torrents`.

       - Example: With the default path, ruTorrent downloads would go to `/mnt/unionfs/downloads/torrents/rutorrent/completed`.

- `transcodes`: Path of temporary transcoding files.

    - Default is `"/mnt/local/transcodes"`.

    - Note: It is recommended to **not** use `/tmp` or `/dev/shm` as a transcode location because the paths are cleared on reboots, causing Docker to create the folder as root and Plex transcoder to crash. Another reason why not to: [https://forums.plex.tv/discussion/comment/1502936/#Comment_1502936](https://forums.plex.tv/discussion/comment/1502936/#Comment_1502936).

- `rclone`: Rclone options.

    - `version`: Rclone version that is installed by Saltbox.

        - Choices are `latest` (or `current`), `beta`, or a specific version number (e.g. `1.42`).

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

##  Options in adv_settings.yml

---

- `system`: Various system-level settings.

    - `timezone`: Timezone to use on the server.

        - Default is `auto`, which will pick the timezone based on geolocation of the server.

        - Enter a "TZ database name" as shown in [this table](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  For example, "America/Costa_Rica".

        - `timedatectl list-timezones` at your server's command prompt will also list the options.

- `dns`: DNS-related settings.

    - `enabled`: Controls whether subdomains are created at Cloudflare

        - Default is `yes`.

    - `proxied`: Controls whether Cloudflare records should be "proxied" or "DNS only".

        - Default is `no`.

    - `ipv6`: Enable/disable ipv6 configuration.

        - Default is `no`.

    - `zerossl`: Controls whether zerossl is used.

        - Default is `no`.

- `traefik`: traefik-related settings.

    - `tls`: Use TLS.

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

        - Default is `rclone_vfs`.

    - `feeder`: Should a feeder mount be created?

        - Default is `no`.

- `gpu`: GPU settings.

    - `intel`: Should system be set up for Intel GPU?

        - Default is `yes`.

    - `nvidia`: Should system be set up for NVidia GPU?

        - Default is `no`.


---

##  Password considerations

These are a YAML files, and values you enter here are subject to YAML file format rules.  If you use special characters in your password, wrap the password in quotes [or escape the characters correctly, if you are familiar with that concept].  It would be easiest to avoid using quote characters themselves within your password.

For example:

  - `pass: MyP4s5w0rd1s4w350m3`
  - `pass: "!@#$%^&*"`
  - `pass: multiple words work fine unquoted`
  - `pass: "or quote them to be safe"`


