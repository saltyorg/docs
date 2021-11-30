THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

## What is it?

[NZBGet](https://nzbget.net/) (by Andrey Prygunkov aka hugbug) is a very efficient, cross-platform usenet downloader.

## Project Information

- [:material-home: NZBGet ](https://nzbget.net){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://nzbget.net/documentation){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/nzbget/nzbget){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/hotio/nzbget){: .header-icons target=_blank rel="noopener noreferrer" }

## 1. Accessing NZBGet

- To access NZBGet, visit https://nzbget._yourdomain.com_

## 2. Settings


### Paths

- Download paths have already been specified, no need to change those.

### News-Servers

- Add your [[news servers|Prerequisites: Usenet vs BitTorrent#i-usenet]].

### Security

- Login settings are preset out of the box (`user` / `passwd` as set in [[accounts.yml|Install: accounts.yml]]).

### Download Queue

- Disk Space

  - By default, minimum disk space is set at _100000_ (i.e. 100GB). When space goes lower than this, NZBGet will pause the queue. If you have a smaller hard drive, you will need to lower this setting. 

### Connection

- DailyQuota

  - Recommend you set this to `750000` (i.e. 750GB), to coincide with the Google Drive daily upload limit.  


## 3. Extensions

- Location on server: `/opt/scripts/nzb`. 

- Location within NZBGet: `/scripts/nzb`.
