[NZBGet](https://nzbget.net/) (by Andrey Prygunkov aka hugbug) is a very efficient, cross-platform usenet downloader.

![](https://nzbget.net/images/Web-Interface-01-Downloads.png)

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
