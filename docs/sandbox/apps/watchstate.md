# WatchState

This tool's primary goal is to sync your backends' play states without relying on third party services. Out of the box, it supports Jellyfin, Plex and Emby media servers.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Docs](https://github.com/ArabCoders/watchstate/blob/master/FAQ.md){ .md-button .md-button--stretch }

[:material-github: GitHub Repo](https://github.com/ArabCoders/watchstate){ .md-button .md-button--stretch }

[:material-cube: GitHub Packages](https://github.com/arabcoders/watchstate/pkgs/container/watchstate){ .md-button .md-button--stretch }

</div>

---

## Configuration

If needed, set environment variables[<sup>:octicons-link-external-16:</sup>][envs] by creating a `/opt/watchstate/config/.env` file and adding the appropriate lines, before deployment.

!!! tip inline end "[Multiple Instances](../../reference/multiple-instances.md) Capable"

## Deployment

``` shell
sb install sandbox-watchstate
```

## Usage

To get a list of available commands, run:

```shell
docker exec -it watchstate console list
```

### <span class="icon-indent-right"></span> Web

Your webhook URL[<sup>:octicons-link-external-16:</sup>][webhooks]:

=== "Plex / Emby"

    ```
    https://watchstate._yourdomain.com_/?apikey=[WEBHOOK_TOKEN]
    ```

=== "Jellyfin"

    ```
    https://watchstate._yourdomain.com_
    ```

=== "Plex / Emby (internal)"

    ```
    http://watchstate:8080/?apikey=[WEBHOOK_TOKEN]
    ```

=== "Jellyfin (internal)"

    ```
    http://watchstate:8080
    ```

[envs]: https://github.com/ArabCoders/watchstate/blob/master/FAQ.md#environment-variables "Head to the environment variables breakdown section of the project documentation"

[webhooks]: https://github.com/ArabCoders/watchstate/blob/master/FAQ.md#how-to-add-webhooks "Head to the webhook usage section of the project documentation"
