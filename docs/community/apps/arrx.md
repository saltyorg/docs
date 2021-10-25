# arr**X**

## Create multiple (Sonarr / Radarr / Bazarr / etc.) containers

Read through this entire page, even if you are only installing one of the apps.

## Background

There are a number of roles in the saltbox community repo which can be used to create multiple instances of an application.  Some of these include:

| Role          | Description                         |
| ------------- | ----------------------------------- |
| alternatrrx   | Sonarr alternative title management |
| bazarrx       | Subtitle downloading                |
| delugex       | Torrent client                      |
| lidarrx       | Music management                    |
| ombix         | Request management                  |
| qbittorrentx  | Torrent client                      |
| radarrx       | Movie management                    |
| readarrx      | Ebook management                    |
| requestrrx    | Discord request bot                 |
| rfloodx       | Torrent client                      |
| sonarrx       | TV management                       |
| tautullix     | Plex stats, data, actions           |
| transmissionx | Torrent client                      |

They're all named something*X* because they allow creation of *X* number of *something*.

They are all configured in the same way.

In general terms, you'll enter the instances you want into the [community `settings.yml`:](../../community/settings.md)

```yaml
appnamex:
  roles:
    - ""
    - bing
    - bang
    - boing
```

That will create:<br/>

- appname
- appnamebing
- appnamebang
- appnameboing

as docker containers, subdomain, and data directories in `/opt`.

For example, with this configuration:

```yaml
sonarrx:
  roles:
    - ""
    - bing
    - bang
    - boing
```

Running the saltbox community `sonarrx` tag would produce:

| entry         | Container    | Config dir         | Subdomain                    | Note                         |
| ------------- | ------------ | ------------------ | ---------------------------- | ---------------------------- |
| ""            | sonarr       | `/opt/sonarr`      | sonarr.YOURDOMAIN.TLD        | Replaces the stock container |
| bing          | sonarrbing   | `/opt/sonarrbing`  | sonarrbing.YOURDOMAIN.TLD    |                              |
| bang          | sonarrbang   | `/opt/sonarrbang`  | sonarrbang.YOURDOMAIN.TLD    |                              |
| boing         | sonarrboing  | `/opt/sonarrboing` | sonarrboing.YOURDOMAIN.TLD   |                              |

NOTE: the names have to be compliant with both domain names and docker names, so no funny business. Do not use anything but a-z and 0-9, no spaces, no commas, no colons, no dash, no exclamation marks, no nothing!

The names, within the constraints above, are completely arbitrary.  There is nothing magic about the example configs [1080webdl, 1080remux] given below.  They represent some common use cases, but you can use whatever names you wish, as in the "bing, bang, boing" examples above.

You will need to configure these new containers just as you did the stock containers.  One change; **be sure each one gets a unique download category**, so that each instance imports only those downloads meant for it.

Also, you probably want to put some thought into the directory and library structure you want to use.  See ["Customizing Plex Libraries"](https://github.com/Cloudbox/Cloudbox/wiki/Customizing-Plex-Libraries){: target=_blank rel="noopener noreferrer" }.

## Overwriting the stock container

The example above shows a `""` config entry.  For those apps which are also found in the stock saltbox install, this will *overwrite* the existing container.  Then, when you rerun the saltbox tag, this container will get overwritten by the stock one again.  You probably don't want that.

For one thing, these "arrX" roles _may_ be based on different images than the stock images.  For example, for a while the `radarrx` role installed Radarr v3 while the stock role installed v2.  You should pick one: use this role to replace the stock one, or not.

You probably want to overwrite your existing role with this one; that will ensure that all your instances of Sonarr are based on the same image and get updated in the same way.  It's up to you, though, how you want to manage them.

### If you want to use this to overwrite your existing Sonarr/Radarr/etc container:

1. Include a `""` entry in the config:
   ```yaml
    sonarrx:
      roles:
        - ""
        - bing
        - bang
        - boing
   ```
2. Run the role as described below.
   ```bash
  sb install cm-sonarrx
   ```
3. Add the stock tag to the `[skip]` section in `"/srv/git/saltbox/ansible.cfg"`:
   ```
   [tags]
   skip = sonarr,whatever,whatever
   ```

That will ensure that the stock `sonarr` tag doesn't overwrite the container you are creating here.

When you want to update Sonarr, you'll run the Saltbox Community `sonarrx` tag instead.

The same thing holds for every `arrX` variant discussed here.

### If you **DO NOT** want to overwrite your existing Sonarr/Radarr/etc container:

1. Make sure there IS NOT a `""` entry in the config:
   ```yaml
   sonarrx:
     roles:
       - bing
       - bang
       - boing

   ```

That's all.  Your existing `sonarr` container will not be touched.

Again, the same thing holds for every `arrX` variant discussed here.

## Create multiple Sonarr v3 containers

1. Edit [`settings.yml`](../../community/settings.md) and change the sonarrx roles to what you want:

   <details>
     <summary>I want to add a 4K version and leave my existing container untouched.</summary>
     <br />

   ```yaml
   sonarrx:
     roles:
       - 4k
   ```
   </details>

   <details>
     <summary>I want to add webdl and remux versions and leave my existing container untouched.</summary>
     <br />

   ```yaml
   sonarrx:
     roles:
       - 1080webdl
       - 1080remux
   ```
   </details>

   <details>
     <summary>I want to replace my existing version and add reality and kids versions.</summary>
     <br />

   ```yaml
   sonarrx:
     roles:
       - ""
       - reality
       - kids
   ```
   **Refer to the notes above about overwriting the default container.**

   </details>

1. Run the sonarrx role as a normal saltbox community role.

   ```bash
   sb install cm-sonarrx
   ```

Remember that all those names are arbitrary and purely cosmetic for your own use.  There is nothing that ties `sonarrreality.YOURDOMAIN.TLD` to reality TV aside from the configuration that you are going to give it.
