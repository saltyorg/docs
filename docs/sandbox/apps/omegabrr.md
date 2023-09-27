# Omegabrr

[Omegabrr](https://autobrr.com/filters/omegabrr) is a companion app to [Autobrr](../../apps/autobrr.md). It transforms items monitored by 'arrs or imported from lists into autobrr filters.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Docs](https://autobrr.com/filters/omegabrr#configuration){ .md-button .md-button--stretch }

[:material-github: GitHub Repo](https://github.com/autobrr/omegabrr){ .md-button .md-button--stretch }

[:material-cube: GitHub Packages](https://github.com/autobrr/omegabrr/pkgs/container/omegabrr){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-omegabrr
```

## Configuration

Upon fresh deployment, `/opt/omegabrr/config.yaml` is generated and pre-filled with your new API token and your internal PVR connection info, but missing an Autobrr API key which you must provide.

Add your filter IDs—separated with a comma and space—inside the square brackets within their appropriate PVR block.

!!! example ""
    ```yaml hl_lines="5"
        - name: radarr
          type: radarr
          host: http://radarr:7878
          apikey: 8713a440703d9e23b689cfe47967694e
          filters: [9, 10, 99, 100] 
    ```

Restart the Docker container for the changes to take effect.

## Usage

To get a list of available commands, run:

```shell
docker exec -it omegabrr omegabrr
```

### <span class="icon-indent-right"></span> Web

Your webhook URL[<sup>:octicons-link-external-16:</sup>][service]:

=== "FQDN"

    ```
    https://omegabrr._yourdomain.com_/api/webhook/trigger
    ```

=== "Internal"

    ```
    http://omegabrr:7441/api/webhook/trigger
    ```

[service]: https://autobrr.com/filters/omegabrr#service "Head to the webhook usage section of the project documentation"