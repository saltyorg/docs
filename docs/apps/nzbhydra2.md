THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

# What is it?

[NZBHydra2](https://github.com/theotherp/nzbhydra2), by _TheOtherP_, is a meta search tool for NZB indexers. It provides easy access to a number of NZB indexers. You can search all your indexers from one place and use it as indexer source for tools like Sonarr or CouchPotato.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| :material-home: Project home | [:octicons-link-16: Docs](https://github.com/theotherp/nzbhydra2/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/theotherp/nzbhydra2){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/hotio/nzbhydra2){: .header-icons target=_blank rel="noopener noreferrer" }|

Three Ways to setup NZB indexers with Sonarr/Radarr/Lidarr:

1. Skip this page and add all your NZB Indexers directly into Sonarr/Radarr/Lidarr. Benefit from the seeing indexer sources during manual lookups in Sonarr/Radarr/Lidarr. This method is also useful when diagnosing issues with indexers during failed searches;

2. Add all your NZB Indexers directly into Sonarr/Radarr/Lidarr, but also add them in NZBHydra2, so it could be used a tool for manual downloads; or

3. Add all your NZB indexers in NZBHydra2 and then just add the one NZBHydra2 "indexer" into Sonarr/Radarr/Lidarr. This is the most popular choice among users.

---

To Setup NZBHydra2, follow the steps below.

## 2. URL

- URL to access NZBHydra2, visit `https://nzbhydra2._yourdomain.com_`

## 3. Setup

Enter setup by clicking on "Config" at the top.

### Main

- Under 'Security', click the icon next to the 'API key *' field to generate an API key. Click 'Save'.

### Authorization

- Login settings are preset out of the box (`user` / `passwd` as set in [accounts.yml](../reference/accounts.md)).

### Indexers

- Add your indexers. Click "Save".

### Downloaders

- NZBGet settings are preset out of the box.

## 4. API Key

To find the NZBHydra2 API Key, go to "Config" --> "Main". This will be used later in [Sonarr](sonarr.md) and [Radarr](radarr.md).

## 5. Next

Are you setting Saltbox up for the first time?  Continue to [Jackett](jackett.md).
