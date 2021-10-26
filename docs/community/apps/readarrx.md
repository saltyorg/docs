# Readarr**X**

## What is it?

[ReadarrX](http://readarr.com/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [Readarr](../../community/apps/readarr.md).

## Project Information

- [:material-home: Readarr ](http://readarr.com/){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://wiki.servarr.com/en/readarr){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/Readarr/Readarr){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/hotio/readarr){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-readarrx

```

### 2. URL

- To access Readarr**X**, visit `https://readarrx._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the Readarr**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

    ``` { .yaml }
        readarrx:
          roles:
            - ebooks
            - audiobooks
    ```

3. Run the Saltbox installer to generate your **X** instances of readarr.

      ``` { .shell }

          sb install cm-readarrx

      ```

- For app specific instructions refer to the parent role,
     - [Readarr](../../community/apps/readarr.md)<Br/>
     - and the Readarr upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://wiki.servarr.com/en/readarr){: .header-icons target=_blank rel="noopener noreferrer" }
