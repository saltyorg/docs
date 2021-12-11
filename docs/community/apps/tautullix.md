# Tautulli**X**

## What is it?

[Tautulli**X**](https://tautulli.com/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [Tautulli](../../apps/tautulli.md).

[Tautulli](https://tautulli.com/){: target=_blank rel="noopener noreferrer" } is a 3rd party application that you can run alongside your Plex Media Server to monitor activity and track various statistics. Most importantly, these statistics include what has been watched, who watched it, when and where they watched it, and how it was watched. The only thing missing is "why they watched it", but who am I to question your 42 plays of Frozen. All statistics are presented in a nice and clean interface with many tables and graphs, which makes it easy to brag about your server to everyone else.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://tautulli.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/Tautulli/Tautulli/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/tautulli/tautulli){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/hotio/tautulli){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-tautullix

```

### 2. URL

- To access Tautulli**X**, visit `https://tautulliX._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the Tautulli**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

    ``` { .yaml }
        tautullix:
          roles:
            tautulli: plex
            tautulli2: plex2
    ```

3. Run the Saltbox installer to generate your **X** instances of tautulli.

      ``` { .shell }

          sb install cm-tautullix

      ```

- For app specific instructions refer to the parent role,
     - [tautulli](../../apps/tautulli.md)<Br/>
     - and the tautulli upstream documentation <BR/>
       [:octicons-link-16: Documentation ](https://github.com/Tautulli/Tautulli/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
