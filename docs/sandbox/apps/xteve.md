# xTeVe


## What is it?

[xTeVe](https://github.com/xteve-project/xTeVe){: target=_blank rel="noopener noreferrer" } is a M3U proxy server for Plex, Emby and any client and provider which supports the .TS and .M3U8 (HLS) streaming formats.

xTeVe emulates a SiliconDust HDHomeRun OTA tuner, which allows it to expose IPTV style channels to software, which would not normally support it. This Docker image includes the following packages and features:

- xTeVe v2.1 (Linux) x86 64 bit

- Latest Guide2go (Linux) x86 64 bit (Schedules Direct XMLTV grabber)

- Zap2XML Support (Perl based zap2it / TVguide.com XMLTV grabber)

- Bash, Perl & crond Support

- VLC & ffmpeg Support

- Automated XMLTV Guide Lineups & Cron’s


| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://github.com/xteve-project/xTeVe){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/xteve-project/xTeVe-Documentation/blob/master/en/configuration.md){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/xteve-project/xTeVe){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/dnsforge/xteve){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-xteve

```

### 2. URL

- To access xTeVe, visit `https://ROLENAME._yourdomain.com_`

### 3. Setup

- Access xTeVe web GUI, visit `https://ROLENAME._yourdomain.com_`

- Run through the Configuration Wizard.

- [:octicons-link-16: Documentation](https://github.com/xteve-project/xTeVe-Documentation/blob/master/en/configuration.md){: .header-icons target=_blank rel="noopener noreferrer" }
