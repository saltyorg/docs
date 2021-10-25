# APPNAME**X**

## What is it?

[APPNAME**X**](APPHOMEPAGE){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [APPNAME](../../community/apps/OGAPP.md).

## Project Information

- [:material-home: APPNAME ](APPHOMEPAGE){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](DOCSLINK){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](GITHUBLINK){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](DOCKERLINK){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-ROLENAME

```

### 2. URL

- To access APPNAME**X**, visit `https://ROLENAME._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the APPNAME**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

    ``` { .yaml }
        ROLENAME:
          roles:
            - 1080webdl
            - 1080remux
    ```

3. Run the Saltbox installer to generate your **X** instances of OGAPP.

      ``` { .shell }

          sb install cm-ROLENAME

      ```

- For app specific instructions refer to the parent role,
     - [OGAPP](../../community/apps/OGAPP.md)<Br/>
     - and the OGAPP upstream documentation <BR/>
       [:octicons-link-16: Documentation ](DOCSLINK){: .header-icons target=_blank rel="noopener noreferrer" }
