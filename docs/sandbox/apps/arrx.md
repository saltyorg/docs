# Multiple container instances (Cloudbox legacy style)

Read through this entire page, even if you are only installing one of the apps.

NOTE:
This functionality is being moved to a more generalized and customizable [multiple instances](../../reference/multiple-instances.md) system.  As roles are transitioned, they will be removed from the table below.

## Background

There are a number of roles in the saltbox Sandbox repo which can be used to create multiple instances of an application.  Some of these include:

| Role          | Description                         |
| ------------- | ----------------------------------- |
| alternatarrx  | Alternate Name Management           |
| ombix         | Request management                  |
| requestrrx    | Discord request bot                 |
| rfloodx       | Torrent client                      |
| transmissionx | Torrent client                      |

They're all named something*X* because they allow creation of *X* number of *something*.

They are all configured in the same way.

In general terms, you'll enter the instances you want into the [sandbox `settings.yml`:](../settings.md)

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
ombix:
  roles:
    - ""
    - bing
    - bang
    - boing
```

Running the Saltbox Sandbox `ombix` tag would produce:

| entry         | Container  | Config dir       | Subdomain                  | Note                         |
| ------------- | ---------- | ---------------- | -------------------------- | ---------------------------- |
| ""            | ombi       | `/opt/ombi`      | ombi.YOURDOMAIN.TLD        | Replaces the stock container |
| bing          | ombibing   | `/opt/ombibing`  | ombibing.YOURDOMAIN.TLD    |                              |
| bang          | ombibang   | `/opt/ombibang`  | ombibang.YOURDOMAIN.TLD    |                              |
| boing         | ombiboing  | `/opt/ombiboing` | ombiboing.YOURDOMAIN.TLD   |                              |

NOTE: the names have to be compliant with both domain names and docker names, so no funny business. Do not use anything but a-z and 0-9, no spaces, no commas, no colons, no dash, no exclamation marks, no nothing!

The names, within the constraints above, are completely arbitrary.  There is nothing magic about the example configs [1080webdl, 1080remux] given below.  They represent some common use cases, but you can use whatever names you wish, as in the "bing, bang, boing" examples above.

You will need to configure these new containers just as you did the stock containers.  One change; if applicable, **be sure each one gets a unique download category**, so that each instance imports only those downloads meant for it.

Also, you probably want to put some thought into the directory and library structure you want to use.  See ["Customizing Plex Libraries"](https://github.com/Cloudbox/Cloudbox/wiki/Customizing-Plex-Libraries){: target=_blank rel="noopener noreferrer" }.

## Overwriting the stock container

The example above shows a `""` config entry.  For those apps which are also found in the stock saltbox install, this will *overwrite* the existing container.  Then, when you rerun the saltbox tag, this container will get overwritten by the stock one again.  You probably don't want that.

For one thing, these "arrX" roles *may* be based on different images than the stock images.

You probably want to overwrite your existing role with this one; that will ensure that all your instances of Bazarr are based on the same image and get updated in the same way.  It's up to you, though, how you want to manage them.

### If you want to use this to overwrite your existing Bazarr/etc container

1. Include a `""` entry in the config:

   ```yaml
    bazarrx:
      roles:
        - ""
        - bing
        - bang
        - boing
   ```

2. Run the role as described below.

```bash
  sb install cm-bazarrx
```

3. Add the stock tag to the `[skip]` section in `"/srv/git/saltbox/ansible.cfg"`:

```text

   [tags]
   skip = bazarr,whatever,whatever

```

That will ensure that the stock `bazarr` tag doesn't overwrite the container you are creating here.

When you want to update Bazarr, you'll run the Saltbox Sandbox `bazarrx` tag instead.

The same thing holds for every `arrX` variant discussed here.

### If you **DO NOT** want to overwrite your existing Bazarr/etc container

1. Make sure there IS NOT a `""` entry in the config:

   ```yaml
   bazarrx:
     roles:
       - bing
       - bang
       - boing

   ```

That's all.  Your existing `bazarr` container will not be touched.

Again, the same thing holds for every `arrX` variant discussed here.

## Examples: multiple Bazarr containers

1. Edit [`settings.yml`](../settings.md) and change the bazarrx roles to what you want:

   <details>
     <summary>I want to add a BING [4K, kids, German, whatever] version and leave my existing container untouched.</summary>
     <br />

   ```yaml
   bazarrx:
     roles:
       - BING
   ```

   </details>

   <details>
     <summary>I want to add BING and BANG versions and leave my existing container untouched.</summary>
     <br />

   ```yaml
   bazarrx:
     roles:
       - BING
       - BANG
   ```

   </details>

   <details>
     <summary>I want to replace my existing version and add BANG and BOING versions.</summary>
     <br />

   ```yaml
   bazarrx:
     roles:
       - ""
       - BANG
       - BOING
   ```

   **Refer to the notes above about overwriting the default container.**

   </details>

1. Run the bazarrx role as a normal Saltbox Sandbox role.

   ```bash
   sb install cm-bazarrx
   ```

Remember that all those names are arbitrary and purely cosmetic for your own use.  There is nothing that ties `readarr-romance.YOURDOMAIN.TLD` to romance literature aside from the configuration that you are going to give it.
