# Requestrr**X**

## What is it?

[RequestrrX](https://github.com/darkalfx/requestrr){: target=_blank rel="noopener noreferrer" } is an [arr**X** role](arrx.md) for [Requestrr](../../sandbox/apps/requestrr.md).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/darkalfx/requestrr){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/darkalfx/requestrr/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/darkalfx/requestrr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/hotio/requestrr){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-requestrrx

```

### 2. URL

- To access Requestrr**X**, visit `https://requestrrx._yourdomain.com_`

### 3. Setup

1. Read through the general [arr**X** role instructions](arrx.md).

2. Add your **X** instance names to the Requestrr**X** section in [saltbox `settings.yml`:](../settings.md) using a list format as below.

    ``` { .yaml }
        requestrrx:
          roles:
            - 1080
            - 4k
    ```

3. Run the Saltbox installer to generate your **X** instances of requestrr.

      ``` { .shell }

          sb install sandbox-requestrrx

      ```

- For app specific instructions refer to the parent role,
     - [requestrr](../../sandbox/apps/requestrr.md)<Br/>
     - and the requestrr upstream documentation <BR/>
       [:octicons-link-16: Documentation](https://github.com/darkalfx/requestrr/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
