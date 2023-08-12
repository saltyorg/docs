# Transmission**X**

## What is it?

[Transmission**X**](https://transmissionbt.com/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](arrx.md) for [Transmission](../../sandbox/apps/transmission.md).

[Transmission](https://transmissionbt.com/){: target=_blank rel="noopener noreferrer" } is a fast, easy, and free BitTorrent client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://transmissionbt.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/transmission/transmission/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/transmission/transmission){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/transmission){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-transmissionx

```

### 2. URL

- To access Transmission**X**, visit `https://transmissionx._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](arrx.md).

2. Add your **X** instance names to the Transmission**X** section in [saltbox `settings.yml`:](../settings.md) using a list format as below.

    ``` { .yaml }
        transmissionx:
          roles:
            - reality
            - games
    ```

3. Run the Saltbox installer to generate your **X** instances of transmission.

      ``` { .shell }

          sb install sandbox-transmissionx

      ```

- For app specific instructions refer to the parent role,
  - [transmission](../../sandbox/apps/transmission.md)<Br/>
  - and the transmission upstream documentation <BR/>
       [:octicons-link-16: Documentation](https://github.com/transmission/transmission/blob/main/docs/README.md){: .header-icons target=_blank rel="noopener noreferrer" }
