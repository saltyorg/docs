

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:0 orderedList:1 -->

1. [Intro](#1-intro)
2. [URL](#2-url)
3. [Setup](#3-setup)
4. [API](#4-api-key)

<!-- /TOC -->

## 1. Intro


[NZBHydra2](https://github.com/theotherp/nzbhydra2), by _TheOtherP_, is a meta search tool for NZB indexers. It provides easy access to a number of NZB indexers. You can search all your indexers from one place and use it as indexer source for tools like Sonarr or CouchPotato.


![](https://i.imgur.com/gjciEYd.png)

---

Three Ways to setup NZB indexers with Sonarr/Radarr/Lidarr: 

1) Skip this page and add all your NZB Indexers directly into Sonarr/Radarr/Lidarr. Benefit from the seeing indexer sources during manual lookups in Sonarr/Radarr/Lidarr. This method is also useful when diagnosing issues with indexers during failed searches;

2) Add all your NZB Indexers directly into Sonarr/Radarr/Lidarr, but also add them in NZBHydra2, so it could be used a tool for manual downloads; or

3) Add all your NZB indexers in NZBHydra2 and then just add the one NZBHydra2 "indexer" into Sonarr/Radarr/Lidarr. This is the most popular choice among users.




---

To Setup NZBHydra2, follow the steps below.



## 2. URL

- URL to access NZBHydra2, visit https://nzbhydra2._yourdomain.com_.

## 3. Setup

Enter setup by clicking on "Config" at the top.

### Main

- Under 'Security', click the icon next to the 'API key *' field to generate an API key. Click 'Save'.

### Authorization

- Login settings are preset out of the box (`user` / `passwd` as set in [[accounts.yml|Install: Settings]]).

### Migration

 <details>
 <summary> You can migrate your previous NZBHydra 1 config by entering in the following: (click to expand)</summary> 
  <br />
  <img src="https://i.imgur.com/CneRSWw.png" alt="NZBHydra1 Migration"> 
 </details>

### Indexers

- Add your indexers. Click "Save".

### Downloaders

- NZBGet settings are preset out of the box. 




## 4. API Key

To find the NZBHydra2 API Key, go to "Config" --> "Main". This will be used later in [[Sonarr|Install: Sonarr#nzbhydra2]] and [[Radarr|Install: Radarr#nzbhydra2]].