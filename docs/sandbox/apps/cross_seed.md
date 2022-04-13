# Cross-seed

## What is it?

[FlareSolverr](https://github.com/mmgoodnow/cross-seed){: target=_blank rel="noopener noreferrer" }  is an app designed to help you download torrents that you can cross seed based on your existing torrents. Cross-seed can inject the torrents it finds directly into your torrent client. Currently the supported clients are qBittorrent and rTorrent. If your client isn't supported, cross-seed will download a bunch of torrent files to a folder you specify. 

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://github.com/mmgoodnow/cross-seed){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/mmgoodnow/cross-seed){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/mmgoodnow/cross-seed){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/mmgoodnow/cross-seed){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-cross-seed

```

### 2. Setup
#### Config.js
- Locate the _config.js.sample_ file in your apps `/opt/` dir. 
- Ignore Jackett sections
- Optionally add tracker IDs. 
- Define `excludeRecentSearch:` is recommended. ie `excludeRecentSearch: 10080`
- Fill in the appropriate info for your setup. 
#### Prowlarr
- In the first tab `Indexers`, click the `(i)` on the right of the indexer. 
- Copy the `Torznab Url`, then append `?apikey=YOUR_PROWLARR_API_KEY`
- Place this in `config.js.sample` by `torznab: []` ie ["paste", "paste"],


- [:octicons-link-16: Documentation](https://github.com/mmgoodnow/cross-seed){: .header-icons target=_blank rel="noopener noreferrer" }
