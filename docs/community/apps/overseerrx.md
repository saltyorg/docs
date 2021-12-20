# Overseerr**X**

## What is it?

[Overseerr**X**](APPHOMEPAGE){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [Overseerr](../../apps/overseerr.md).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://overseerr.dev/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://docs.overseerr.dev/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/sct/overseerr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/sctx/overseerr){: .header-icons target=_blank rel="noopener noreferrer" }|


### 1. Installation

``` shell

sb install cm-overseerrx

```

### 2. URL

- To access Overseerr**X**, visit `https://overseerrx._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the Overseerr**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

    ``` { .yaml }
        overseerrx:
          roles:
            - 1080
            - 4k
    ```

3. Run the Saltbox installer to generate your **X** instances of Overseerr.

      ``` { .shell }

          sb install cm-overseerrx

      ```

- For app specific instructions refer to the parent role,
     - [Overseerr](../../apps/overseerr.md)<Br/>
     - and the overseerr upstream documentation <BR/>
     - [:octicons-link-16: Documentation: Overseerr Docs](https://docs.overseerr.dev/){: .header-icons target=_blank rel="noopener noreferrer" }
