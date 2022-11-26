# Ombi**X**

## What is it?

[Ombi**X**](https://ombi.io){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](arrx.md) for [Ombi](../../sandbox/apps/ombi.md).

[Ombi](https://ombi.io/){: target=_blank rel="noopener noreferrer" } is a self-hosted web application that automatically gives your shared Plex or Emby users the ability to request content by themselves!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://ombi.io/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://docs.ombi.app/guides/installation/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Ombi-app/Ombi){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/hotio/ombi){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-ombix

```

### 2. URL

- To access Ombi**X**, visit `https://OmbiX._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](arrx.md).

2. Add your **X** instance names to the Ombi**X** section in [saltbox `settings.yml`:](../settings.md) using a list format as below.

   ``` { .yaml }
    ombix:
      roles:
        - 4k
        - anime
   ```

- For app specific instructions refer to the parent role,
  - [Ombi](../../sandbox/apps/ombi.md)<Br/>
  - and the upstream documentation <BR/>
       [:octicons-link-16: Documentation](https://docs.ombi.app/guides/installation/){: .header-icons target=_blank rel="noopener noreferrer" }
