# Goplaxt

## What is it?

[Goplaxt](https://github.com/XanderStrike/goplaxt){: target=_blank rel="noopener noreferrer" } scrobbles Plex plays to Trakt with ease!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://github.com/XanderStrike/goplaxt){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/XanderStrike/goplaxt){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/XanderStrike/goplaxt){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/xanderstrike/goplaxt){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-goplaxt

```

### 2. URL

- To access Goplaxt, visit `https://goplaxt._yourdomain.com_`

### 3. Setup

1. Create an API application through Trakt [here](https://trakt.tv/oauth/applications). The Redirect URI should be your goplaxt.domain + `/authorize`, so it reads as: `https://goplaxt.domain.com/authorize`.

2. Edit the Goplaxt section in [saltbox `settings.yml`:](../settings.md) substituting your own `ID` and `secret`.

    ``` { .yaml }
    goplaxt:
      trakt_id: IDHERE
      trakt_secret: SECRETHERE
    ```

3. Run the role install command

    ``` { .shell }

    sb install sandbox-goplaxt

    ```

4. Visit the goplaxt site at `https://goplaxt.domain.com`. <br />
    Enter your `Plex Username` then `Authorize`, and add the Webhook in `Plex Settings`. <br />
    Make sure under your server `Settings > Network` that Webhooks is `enabled`.

- [:octicons-link-16: Documentation](https://github.com/XanderStrike/goplaxt){: .header-icons target=_blank rel="noopener noreferrer" }
