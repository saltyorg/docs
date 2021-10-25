# OmbiX

## What is it?

[OmbiX](https://ombi.io){: target=_blank rel="noopener noreferrer" } is an [arrX role](../../community/apps/arrx.md) for [Ombi](../../apps/ombi.md).

[Ombi](https://ombi.io/){: target=_blank rel="noopener noreferrer" } is a self-hosted web application that automatically gives your shared Plex or Emby users the ability to request content by themselves!

## Project Information

- [:material-home: Ombi ](https://ombi.io/){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://docs.ombi.app/guides/installation/){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/Ombi-app/Ombi){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/hotio/ombi){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-ombix

```

### 2. URL

- To access OmbiX, visit `https://OmbiX._yourdomain.com_`

### 3. Setup

1. Read through the general [arrX role instructions](../../community/apps/arrx.md).

2. Add your X instance names to the OmbiX section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

   ``` { .yaml }
    ombix:
      roles:
        - 4k
        - anime
   ```

- For app specific instructions refer to the parent role,
     - [Ombi](../../apps/ombi.md)<Br/>
     - and the upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://docs.ombi.app/guides/installation/){: .header-icons target=_blank rel="noopener noreferrer" }
