# Bazarr**X**

## What is it?

[bazarr**X**](APPHOMEPAGE){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [bazarr](../../community/apps/bazarr.md).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://www.bazarr.media/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://wiki.bazarr.media/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/hotio/bazarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/hotio/bazarr){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-bazarrx

```

### 2. URL

- To access bazarr**X**, visit `https://bazarrx._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the bazarr**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

   ``` { .yaml }
    bazarrx:
      roles:
        - 1080webdl
        - 1080remux
   ```

- For app specific instructions refer to the parent role,
     - [bazarr](../../community/apps/bazarr.md)<Br/>
     - and the upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://wiki.bazarr.media/){: .header-icons target=_blank rel="noopener noreferrer" }
