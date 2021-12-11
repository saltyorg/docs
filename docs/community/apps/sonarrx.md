# Sonarr**X**

## What is it?

[Sonarr**X**](https://sonarr.tv/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [Sonarr](../../apps/sonarr.md).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://sonarr.tv/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://wiki.servarr.com/Sonarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/sonarr/sonarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/hotio/sonarr){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-sonarrx

```

### 2. URL

- To access Sonarr**X**, visit `https://sonarrx._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the Sonarr**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

    ``` { .yaml }
        sonarrx:
          roles:
            - 1080webdl
            - documentary
    ```

3. Run the Saltbox installer to generate your **X** instances of sonarr.

      ``` { .shell }

          sb install cm-sonarrx

      ```

- For app specific instructions refer to the parent role,
     - [sonarr](../../apps/sonarr.md)<Br/>
     - and the sonarr upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://wiki.servarr.com/Sonarr){: .header-icons target=_blank rel="noopener noreferrer" }
