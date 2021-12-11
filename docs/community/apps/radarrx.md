# Radarr**X**

## What is it?

[Radarr**X**](https://radarr.video/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [Radarr](../../apps/radarr.md).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://radarr.video/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://wiki.servarr.com/radarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/Radarr/Radarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/hotio/radarr){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-radarrx

```

### 2. URL

- To access Radarr**X**, visit `https://radarr_X._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the Radarr**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

    ``` { .yaml }
        radarrx:
          roles:
            - 1080webdl
            - 1080remux
    ```

3. Run the Saltbox installer to generate your **X** instances of radarr.

      ``` { .shell }

          sb install cm-radarrx

      ```

- For app specific instructions refer to the parent role,
     - [Radarr](../../apps/radarr.md)<Br/>
     - and the Radarr upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://wiki.servarr.com/radarr){: .header-icons target=_blank rel="noopener noreferrer" }
