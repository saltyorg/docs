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

        - This is a YAML file, and values you can enter here are subject to YAML file format rules.  If you use special characters in your password, wrap the password in quotes [or escape the characters correctly, if you are familiar with that concept].  It would be easiest to avoid using quote characters themselves within your password.

        - For example:

            - `pass: MyP4s5w0rd1s4w350m3`
            - `pass: "!@#$%^&*"`
            - `pass: multiple words work fine unquoted`
            - `pass: "or quote them to be safe"`

    - `domain`: Domain name for the Saltbox server. 

        - If you don't have one, see [[here|Prerequisites: Domain Name]].
        - This should be the domain "below" the saltbox subdomains.  For example, if you want to access Sonarr at "sonarr.domain.tld", enter "domain.tld".  If you want "sonarr.foo.domain.tld", enter "foo.domain.tld".
        - This parameter is **required**.

    - `email`: E-mail address. 

        - This is used for the Let's Encrypt SSL certificates.
        - It does not have to be an email address at the domain above.
        - This parameter is **required**.

- `cloudflare`: Cloudflare Account
    - `email`: E-mail address used for the Cloudflare account. 

    - `api`: [[API Token|Prerequisites: Cloudflare]]. 

    - This parameter is optional. 

    - Default is blank.

    - Fill this in to have Saltbox add subdomains on Cloudflare, automatically; leave it blank, to have all Cloudflare related functions disabled.

    - Note: if you are using a subdomain, like WHATEVER.DOMAIN.TLD, as your domain above, leave these blank. The Cloudflare automation does not work in that case and the install will stop with an error.

- `plex`: Plex.tv account credentials. 

    - This will be used to:
        - claim the Plex server under your username, and
        - generate Plex Access Tokens for apps such as Plex Autoscan, etc. 

    - `user` - Plex username or email address on the profile.

    - `pass` - Plex password.

    - `tfa` - "yes" or "no" depending on whether you want to use the two-factor authentication [TFA] compatible Plex connection system.

    - This parameter is required. 

    - Note: The "tfa" setting controls whether Saltbox uses the newer authentication method or not; this newer method is *required* for use with TFA, but will work evern with it off; it's the "Open an URL, log into Plex, grant access to this app" workflow you may be familiar with from other contexts.

    - If you use the `tfa` workflow, a random client ID and a Plex Access Token will be stored in `/opt/saltbox/plex.ini` for later use.

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

       - Example: With the default path, NZBGet downloads would go to `/mnt/unionfs/downloads/nzbs/nzbget/completed`, where as, SABnzbd downloads would go to `/mnt/unionfs/downloads/nzbs/sabnzbd/complete`.

    - `torrents`: Path for BitTorrent app downloads. 

        - Default is `/mnt/unionfs/downloads/torrents`.

       - Example: With the default path, ruTorrent downloads would go to `/mnt/unionfs/downloads/torrents/rutorrent/completed`.

- `plex`: Plex options.

    - `tag`: Determines what version of Plex to install. 


        - Options are `public`, `beta`, or [[version tag|https://hub.docker.com/r/cloudb0x/plex/tags]] (e.g. `"1.12.3.4973-215c28d86"`). TODO CHANGE THIS LIST TO REFLECT ACTIVE IMAGE

        - Default is `public`.

        - Notes:

            - Note 1: The `public` tag restricts this check to public versions only, where as, `beta` tag will fetch beta versions. If the server is not logged in or you do not have an active [Plex Pass](https://www.plex.tv/features/plex-pass/) on your Plex account, the `beta` tag will only install the publicly available versions only. 

            - Note 2: Hardware Transcoding requires an  active [Plex Pass](https://www.plex.tv/features/plex-pass/). This can be enabled on either the `public` or `beta` tagged versions. 

            - Note 3: If you decide to change the tags later, you will need to update Plex by running the Saltbox install command with the "plex" tag (i.e. `sb install plex`).

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


