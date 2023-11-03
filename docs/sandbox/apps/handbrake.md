# HandBrake

## What is it?

[HandBrake](https://handbrake.fr/) is a tool for converting video from nearly any format to a selection of modern, widely supported codecs.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://handbrake.fr/){: .header-icons } | [:octicons-link-16: Docs](https://handbrake.fr/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/HandBrake/HandBrake){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/handbrake){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-handbrake

```

### 2. URL

- To access HandBrake, visit `https://handbrake._yourdomain.com_`

### 3. Setup

1. Edit the HandBrake section in [sandbox `settings.yml`:](../settings.md) and enter your desired password. Please note that it MUST be less than eight characters.

    ``` { .yaml }
    handbrake:
      handbrake_pass: saltbox
    ```

2. Run the role install command

    ``` { .shell }

    sb install sandbox-handbrake

    ```

3. Access HandBrake `https://handbrake._yourdomain.com_`

4. See the HandBrake documentation for usage:
      - [:octicons-link-16: Documentation](https://handbrake.fr/docs){: .header-icons }

!!! Tip
      This container has an automatic video converter built in, see the [container documentation here](https://github.com/jlesage/docker-handbrake#automatic-video-conversion){: .header-icons }.
