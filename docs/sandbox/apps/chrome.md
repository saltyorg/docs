# Chrome

Headless container running Google Chrome. Useful for testing, filling out forms, web crawling, getting webpage screenshots, etc.

This was created for use with Hoarder which calls for a specific version (123)

<div class="grid sb-buttons" style="grid-template-columns: repeat(2, 1fr);" markdown data-search-exclude>

[:material-bookshelf: Github Repo](https://github.com/jlandure/alpine-chrome/blob/master/Dockerfile){ .md-button .md-button--stretch }

[:material-git: Google Artifact](https://console.cloud.google.com/artifacts/docker/zenika-hub/us/gcr.io/alpine-chrome/sha256:e38563d4475a3d791e986500a2e4125c9afd13798067138881cf770b1f6f3980){ .md-button .md-button--stretch }

</div>

This role is not exposed by default.

## Deployment

```shell
sb install sandbox-chrome
```

## Usage

The docker commands are set to the following by default. Port 9222 is open to the container by default.

```yml
  - --no-sandbox
  - --disable-gpu
  - --disable-dev-shm-usage
  - --remote-debugging-address=0.0.0.0
  - --remote-debugging-port=9222
  - --hide-scrollbars
```
