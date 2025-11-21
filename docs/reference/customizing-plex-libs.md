---
hide:
  - tags
tags:
  - library
  - custom
---

# Customizing Plex Libraries

!!! important
    This guide was written before Dropbox was a popular choice; all the concepts here apply to Dropbox as well. Nothing here is Google-specific, though all the examples use Google Drive.

!!! info
    This guide was written before the default shared drive setup started adding different shared drives for more media types, so chances are you may not need to do much here as the default system already looks like Scenario 2.

    As of this writing the default shared drives setup creates 7 shared drives, each with its own media type directory already in place.

    Current default directory structure [each on its own shared drive]

    ```text
    Media
    ├── Anime
    ├── Books
    ├── Movies
    ├── Movies-4K
    ├── Music
    ├── TV
    └── TV-4K
    ```

    You can point Plex libraries at those existing directories, and use those directories as root dirs in the *arrs, whether you create multiple instances or not.

    If you ran the optional cloudplow script as part of that process, the cloudplow mods discussed below are done for you.

    The concepts discussed here may still be useful if you did not use that process.

## Basics

In the default Saltbox install, there are only two main Plex libraries: one for Movies and one for TV Shows.

The idea being that all movies are to be placed within the `/Media/Movies` folder in your cloud storage. and all TV shows under `/Media/TV`.

   ```text
   Media
   ├── Movies
   ├── Music
   └── TV
   ```

![](https://i.imgur.com/kwnNjni.png)

If you would like to have custom libraries in Plex, you may do so with this guide.

But regardless of whatever scenario you choose below, the media folders will ALWAYS be located within the `Media` folder (`/Media/` on Google Drive and `/mnt/unionfs/Media/` on the server).

_Note: This guide discusses the setup in terms of movies. You can of course do the same with TV shows using the same concepts with your `Media/TV` directory and Sonarr, but to keep this document simple we're not covering both cases since they're just about identical._

## Scenarios

- Adding folders (i.e. libraries) directly under `Media/Movies/` (or `Media/TV/`) (i.e. the standard paths) &rightarrow; [Scenario 1](#scenario-1). This is the recommended option.

- Adding folders (i.e. libraries) directly under `Media/` &rightarrow; [Scenario 2](#scenario-2).

## Example

Here is an example library setup, which is based on [Scenario 1](#scenario-1).

 ```text
 Media
 ├── Movies
 │   ├── Movies
 │   ├── Movies-4K
 │   ├── Movies-Anime
 │   └── Movies-Kids
 ├── Music
 └── TV
     ├── TV
     └── TV-4K
 ```

- The general location movies in this example is `/Movies/Movies`.

  _Note: This can be called anything else, such as `/Movies/Movies-Main` or `/Movies/Movies-All`._

- `/Movies/Movies-Kids/` folder is for family rated, animated films.

- `/Movies/Movies-Anime/` folder is for Japanese, animated films.

## Scenario 1

Movie libraries under `/Media/Movies`.

This setup is recommended over Scenario 2 as it is somewhat user-friendly and requires a lot less setup.

Example:

```text
Media
├── Movies
│   ├── Movies
│   ├── Movies-4K
│   ├── Movies-Anime
│   ├── Movies-Foreign
│   └── Movies-Kids
├── Music
└── TV
```

### 1. Create Folders in Google Drive

Let's say you wanted to have separate movie libraries for:

- General Movies
- 4K Movies
- Anime Movies
- Foreign Movies
- Movies for Kids

You would first have to create these folders within the `/Media/Movies` path in Google Drive.

However, the root folder of `/Media/Movies` will NOT contain anything but these folders.

_Note: Remember, folders are case sensitive in Google Drive and in Linux (e.g. `4K` and `4k` are 2 different folders)._

For our example, we will create the following folders in Google Drive:

- `/Media/Movies/Movies`*
- `/Media/Movies/Movies-4K`
- `/Media/Movies/Movies-Anime`
- `/Media/Movies/Movies-Foreign`
- `/Media/Movies/Movies-Kids`

*_Note: This can be called anything else, such as `/Media/Movies/Movies-Main` or `/Media/Movies/Movies-All`._

Screenshots:

  ![](https://i.imgur.com/kwnNjni.png)

  ![](https://i.imgur.com/VG5zT7y.png)

### 2. Add Libraries to Plex

You will add each of these folders as separate libraries within Plex (see [[example|Install: Plex-Media-Server#adding-the-movie-library]]). You may name these libraries as whatever you want.

The folders will be located under `/mnt/unionfs/Media/Movies` folder within Plex (see [[Paths|Basics: Saltbox Paths#plex]]).

In our example, this will be:

- `/mnt/unionfs/Media/Movies/Movies`*
- `/mnt/unionfs/Media/Movies/Movies-4K`
- `/mnt/unionfs/Media/Movies/Movies-Anime`
- `/mnt/unionfs/Media/Movies/Movies-Foreign`
- `/mnt/unionfs/Media/Movies/Movies-Kids`

*_Note: This can be called anything else, such as `/mnt/unionfs/Media/Movies-Main` or `/mnt/unionfs/Media/Movies-All`._

### 3. Modify Cloudplow Config

_Note 1: For Mediabox / Feederbox setups, this will be done on the Feederbox._

_Note 2: This is the default setting and may be skipped if you haven't changed it before._

1. On the server's shell, run the following command:

    ```shell
    nano /opt/cloudplow/config.json
    ```

1. Set the following for `remove_empty_dir_depth`:

   ```json
   "remove_empty_dir_depth": 2,
   ```

1. <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd> to save.

1. Restart Cloudplow: `sudo systemctl restart cloudplow`.

### 4. Change Root Paths in Radarr

Set your Movie Paths in [[Radarr|Install: Radarr#8-adding-the-movies-path]] to reflect the new sub-dirs (e.g. `/mnt/unionfs/Media/Movies/3D`).

### 6. Misc

***

## Scenario 2

Movie libraries under `/Media`.

This setup is not recommended as it requires more config setup than Scenario 1. It also the changing of Sonarr/Radarr root paths and updating of those root paths for existing movies.

Example:

```text
Media
├── Movies
├── Movies-4K
├── Movies-Anime
├── Movies-Foreign
├── Movies-Kids
├── Music
└── TV
```

### 1. Create Folders in Google Drive

Let's say you wanted to have separate movie libraries for:

- General Movies
- 4K Movies
- Anime Movies
- Foreign Movies
- Movies for Kids

You would first have to create these folders within the `/Media/` path in Google Drive.

However, the root folder of `/Media/` will NOT contain anything but these folders (and Music and TV folders).

_Note: Remember, folders are case sensitive in Google Drive and in Linux (e.g. `4K` and `4k` are 2 different folders)._

For our example, we will create the following folders in Google Drive:

- `/Media/Movies`*
- `/Media/Movies-4K`
- `/Media/Movies-Anime`
- `/Media/Movies-Foreign`
- `/Media/Movies-Kids`

*_Note: This can be called anything else, such as `/Media/Movies-Main` or `/Media/Movies-All`._

Screenshot:

![](https://i.imgur.com/2MlgwFc.png)

## 2. Add Libraries to Plex

You will add each of these folders as separate libraries within Plex (see [[example|Install: Plex-Media-Server#adding-the-movie-library]]). You may name these libraries as whatever you want.

The folders will be located under `/mnt/unionfs/Media` folder within Plex (see [[Paths|Basics: Saltbox Paths#plex]]).

In our example, this will be:

- `/mnt/unionfs/Media/Movies`*
- `/mnt/unionfs/Media/Movies-4K`
- `/mnt/unionfs/Media/Movies-Anime`
- `/mnt/unionfs/Media/Movies-Foreign`
- `/mnt/unionfs/Media/Movies-Kids`

*_Note: This can be called anything else, such as `/mnt/unionfs/Media/Movies-Main` or `/mnt/unionfs/Media/Movies-All`._

## 3. Modify Plex Autoscan Config

_Note: For Mediabox / Feederbox setups, this will be done on the Mediabox._

1. On the server's shell, run the following command:

    ```shell
    nano /opt/plex_autoscan/config/config.json
    ```

1. Scroll down to the `SERVER_PATH_MAPPINGS` section.

    1. Under this section, you will need to add library paths (as seen from within Plex) with the corresponding `/mnt/unionfs/Media/` path.

        The format will look like:

        ```text
        "/data/<folder>": [                <----- Plex Library Path
          "/mnt/unionfs/Media/<folder>",   <----- Incoming folder path from webhooks (e.g. Radarr root path)
          "My Drive/Media/<folder>/"       <----- Incoming folder path from Google Drive Monitoring (optional)
        ],
        ```

       Note: Make sure the folder paths are within quotes (e.g. `"/data/Movies/"`) and there is a comma (`,`) after the close bracket (`]`) - all except the last one (see example below).

    1. After the changes, the section will now look similar to this:

        ```json
        "SERVER_PATH_MAPPINGS": {
          "/data/Movies/": [
            "/mnt/unionfs/Media/Movies/",
            "My Drive/Media/Movies/"
          ],
          "/data/Movies-4K/": [
            "/mnt/unionfs/Media/Movies-4K/",
            "My Drive/Media/Movies-4K/"
          ],
          "/data/Movies-Anime/": [
            "/mnt/unionfs/Media/Movies-Anime/",
            "My Drive/Media/Movies-Anime/"
          ],
          "/data/Movies-Foreign/": [
            "/mnt/unionfs/Media/Movies-Foreign/",
            "My Drive/Media/Movies-Foreign/"
          ],
          "/data/Movies-Kids/": [
            "/mnt/unionfs/Media/Movies-Kids/",
            "My Drive/Media/Movies-Kids/"
          ],
          "/data/TV/": [
            "/tv/",
            "/mnt/unionfs/Media/TV/"
            "My Drive/Media/TV/"
          ],
          "/data/Music/": [
            "/music/",
            "/mnt/unionfs/Media/Music/",
            "My Drive/Media/Music/"
          ]
        },
        ```

        Note: There may be paths such as `"My Drive/Media/Movies/"` filled in for [[Google Drive monitoring|Plex Autoscan Extras#google-drive-monitoring]]. If you are not planning on using this feature of Plex Autoscan, you can simply ignore them. If you do want to use it, you will then need to tweak the folders to match your Google Drive folder paths. See [[Plex Autoscan Extras|Plex Autoscan Extras#google-drive-monitoring]] for more info.

1. <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd> to save.

1. Restart Plex Autoscan: `sudo systemctl restart plex_autoscan`

## 4. Modify Cloudplow Config

_Note: For Mediabox / Feederbox setups, this will be done on the Feederbox._

1. On the server's shell, run the following command:

    ```shell
    nano /opt/cloudplow/config.json
    ```

1. Set the following for `remove_empty_dir_depth`:

   ```json
   "remove_empty_dir_depth": 1,
   ```

1. <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd> to save.

1. Restart Cloudplow: `sudo systemctl restart cloudplow`.

## 5. Change Root Paths in Radarr

Set your Movie Paths in [[Radarr|Install: Radarr#8-adding-the-movies-path]] to reflect the new sub-dirs (e.g. `/mnt/unionfs/Media/Movies-3D`).
