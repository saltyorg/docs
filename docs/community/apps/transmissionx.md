# Transmission**X**

## What is it?

[Transmission**X**](https://transmissionbt.com/){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](../../community/apps/arrx.md) for [Transmission](../../community/apps/transmission.md).

[Transmission](https://transmissionbt.com/){: target=_blank rel="noopener noreferrer" } is a fast, easy, and free BitTorrent client.

## Project Information

- [:material-home: Transmission ](https://transmissionbt.com/){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://github.com/transmission/transmission/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/transmission/transmission){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/linuxserver/transmission){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install cm-transmissionx

```

### 2. URL

- To access Transmission**X**, visit `https://transmissionx._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](../../community/apps/arrx.md).

2. Add your **X** instance names to the Transmission**X** section in [community `settings.yml`:](../../community/settings.md) using a list format as below.

    ``` { .yaml }
        transmissionx:
          roles:
            - reality
            - games
    ```

3. Run the Saltbox installer to generate your **X** instances of transmission.

      ``` { .shell }

          sb install cm-transmissionx

      ```

- For app specific instructions refer to the parent role,
     - [transmission](../../community/apps/transmission.md)<Br/>
     - and the transmission upstream documentation <BR/>
       [:octicons-link-16: Documentation ](DOCSLINK){: .header-icons target=_blank rel="noopener noreferrer" }
