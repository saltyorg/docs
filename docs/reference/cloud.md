---
hide:
  - tags
tags:
  - cloud
  - storage
---

# Cloud Storage

## Provider

If you want to forego cloud storage and put your media on something like your own NAS, there are some notes [here](local-storage.md).

Saltbox can be set up to use any cloud storage provider that [Rclone](https://rclone.org/) supports. Google Drive via [G-Suite Business](https://gsuite.google.com/pricing.html) has historically been the preferred choice among users, but with recent changes to the Google offering (Dropbox)[https://www.dropbox.com/] has now become a primary choice. Some of the components are designed expressly for Google Drive, like the A-Train Google Drive monitoring in autoscan and the service-account rotation in cloudplow.

This documentation has not yet been fully updated to cover Dropbox specifics or idiosyncrasies.

We advise that you do NOT use a educational account or any account or drive access plan you may buy on the secondary market (eBay and the like) or get free from some random website, unless you are aware of and planning for the likelihood that it disappears without warning one day.

Note that rclone offering support for a storage backend does not mean that backend is suitable for the Saltbox use case. The only backends that see any significant testing and use are Google Drive and Dropbox.

## Basics

Media will be stored in `Movies` and `TV` folders, all within a `Media` folder in root (i.e. `/Media`). <a href="#note1" id="note1ref"><sup>[1]</sup></a>

Saltbox is opinionated about this `/Media/<type>` file structure; changing it is not trivial.

## Setup

```text
Media
├── Movies
├── Music
└── TV
```

- Example from Google Drive:

  ![](../images/google-drive-filesystem.png)

If you have media in other folders, you can simply move them into these folders via the Cloud Storage Provider's web site.

Note 1: For Google Drive, you can use the [Shift-Z trick](https://www.labnol.org/internet/add-files-multiple-drive-folders/28715/) to "symlink" folders here.

Note 2: All the paths/folders mentioned here, and elsewhere, are **CASE SENSITIVE** (see [Saltbox Paths](../saltbox/basics/paths.md)).

## Dropbox "personal folder" vs "shared folders"

Dropbox has both "personal folders" and "shared folders".

An rclone remote without a trailing slash shows your personal folder:
```
> rclone lsd dropbox-saltbox:
          -1 2023-06-26 10:26:58        -1 in-my-personal-folder
```

With a trailing slash shows the "shared folders":
```
> rclone lsd dropbox-saltbox:/
          -1 2023-06-26 10:21:03        -1 Content
          -1 2023-06-26 10:21:03        -1 USERNAME
          -1 2023-06-26 10:21:03        -1 USERNAME@email.tld
          -1 2023-06-26 10:21:03        -1 crypt
          -1 2023-06-26 10:21:03        -1 slash-dir
```

`USERNAME@email.tld` is my personal folder, as shown here:
```
> rclone lsd dropbox-saltbox:/USERNAME@email.tld
          -1 2023-06-26 10:26:58        -1 in-my-personal-folder
```

It's mostly up to you which you use, just keep the differences in mind.

The reasons why one would choose one or the other will be added here at some point.

NOTE: This is a changepoint from Google Drive, where that leading slash doesn't change anything:

```
> rclone mkdir google-saltbox:bing
> rclone lsd google-saltbox:
          -1 2023-06-26 10:41:45        -1 bing
> rclone lsd google-saltbox:/
          -1 2023-06-26 10:41:45        -1 bing
```

## Google "My Drive" vs. "Shared Drives"

Google provides two "types" of storage in a GSuite account: "My Drive" and "Shared Drives".

Shared Drives provide advantages for our purposes over My Drive, while My Drive offers no advantages over Shared Drives.

The primary advantage of Shared Drives is that access to them can be controlled via Service accounts, which allows credential rotation to increase upload limits and reduce likelihood of usage-based server-side bans.

Some newer related utilities (like the Golang "Autoscan" replacement for plex-autoscan) have features that work exclusively with Shared Drives.

The primary disadvantage of Shared Drives is that they have a fixed limit of 400,000 files. For this reason one common strategy is to create separate Shared Drives for each media type.

For those reasons, this documentation will discuss ONLY Shared Drives.

However, if your data is currently on My Drive and you want to keep it there, Saltbox works fine with that as well. Rather than littering the docs with "If you're using My Drive to this, Shared drives do that" decision points, we standardized on Shared Drives. You'll just need to skip some stuff that refers to shared drives.

As a note, if you are unable to create Shared Drives in the Google Drive Web UI, that's a sign that you have the wrong type of Google Drive account.

  ![](../images/google-drive-acct.png)

## Running Saltbox without cloud storage

While the typical use case for Saltbox includes cloud storage, nothing prevents using it without cloud storage.

If, in `settings.yml`, you leave the rclone remote name blank, neither `cloudplow` nor the rclone_vfs mount will be configured. Your media will be imported to `/mnt/local` and stay there. You can mount whatever storage you wish to use at `/mnt/local`.

Alternatively, you can configure an rclone remote pointing at your primary storage (named "google"), then install normally. Everything would then work as it typically does, except that cloudplow would move media from the local system to your NAS or whatever. Perhaps that would allow downloads and imports to go faster.

---
 <sub> <a id="note1" href="#note1ref"><sup>1</sup></a> If you would like to customize your Plex libraries beyond what is listed above, see [Customizing Plex Libraries](../reference/customizing-plex-libs.md).</sub>
