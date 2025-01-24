# Hoarder

[Hoarder](https://hoarder.app/) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Docs](https://docs.hoarder.app/){ .md-button .md-button--stretch }

[:material-git: GitHub Repo](https://github.com/hoarder-app/hoarder){ .md-button .md-button--stretch }

</div>

## Configuration

Use the ```sb inventory``` system to set any environment variables that are desired such as OpenAI API keys, downloading videos, document size limits, etc

See [Hoarder Configuration](https://docs.hoarder.app/configuration) for supported variables

## Deployment

``` shell
sb install sandbox-hoarder
```

## Usage

Visit `https://hoarder.app/`.
