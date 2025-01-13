# Hoarder

[Meilisearch](https://www.meilisearch.com/) Meilisearch is an AI powered search tool.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Home](https://www.meilisearch.com/){ .md-button .md-button--stretch }

[:material-git: GitHub Repo](https://github.com/meilisearch/meilisearch){ .md-button .md-button--stretch }

</div>

This role is not externally exposed by default.

## Configuration

Use the ```sb inventory``` system to set any environment variables that are desired.

See [Meilisearch Environment Variables](https://www.meilisearch.com/docs/learn/self_hosted/configure_meilisearch_at_launch#environment) for supported variables

If not following the Hoarder role instructions:

One key needs to be generated and stored in your ```/opt/sandbox/settings.yaml``` generate with ```openssl rand -base64 36```

Store in the following

```yml
meilisearch:
  meili_master_key: $$$
```

## Deployment

``` shell
sb install sandbox-meilisearch
```

## Usage

Port 7700 is open to the container by default. Also analytics are disabled by default.

Visit `https://www.meilisearch.com/docs`.
