# ArchiveBox

## What is it?

[ArchiveBox](https://github.com/ArchiveBox/ArchiveBox){: target=_blank rel="noopener noreferrer" } is a powerful, self-hosted internet archiving solution to collect, save, and view sites you want to preserve offline.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/ArchiveBox/ArchiveBox){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/ArchiveBox/ArchiveBox/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/ArchiveBox/ArchiveBox){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/archivebox/archivebox){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-archivebox

```

### 2. URL

- To access ArchiveBox, visit `https://archivebox._yourdomain.com_`

### 3. Setup

Initial setup guide thanks to `erisheaded` on CB discord.

1. Run tag:

    ``` { .shell }
    sb install sandbox-archivebox
    ```

2. Connect to container:

   ``` { .shell }
   docker exec -it archivebox /bin/bash
   ```

   - NOTE: (This drops you in the /data folder. DO NOT switch to /data/archive directory)
3. Switch to `archivebox` user for config:

   ``` { .shell }
   su archivebox
   ```

4. Initialize with setup to create a web admin:

   ``` { .shell }
   archivebox init --setup
   ```

5. Enter username, email, and password
6. Load URL and test login

By default, your new installation has a publicly accessible web index, snapshots, and archive addition access. You may not want this for a host of security reasons, so it's recommended to review the [ArchiveBox Security Overview](https://docs.archivebox.io/en/latest/Security-Overview.html){: .header-icons target=_blank rel="noopener noreferrer" } and tailoring these settings to your preference when setting up.
