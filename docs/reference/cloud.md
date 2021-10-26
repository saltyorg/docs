# Cloud Storage
## Provider

Saltbox can be set up to use any cloud storage provider that [Rclone](https://rclone.org/) supports. However, Google Drive via [G-Suite Business](https://gsuite.google.com/pricing.html) is the popular choice among users.  Some of the components are designed expressly for Google Drive, like the Google Drive monitoring in plex-autoscan and the service-account rotation in cloudplow.

It is advised that you do NOT use a educational GSuite account or any GSuite account you may buy on the secondary market [eBay and the like], unless you are aware of and planning for the likelihood that it disappears one day.

## Basics

Out of the box, Saltbox stores the media unencrypted in cloud storage utilizing an Rclone VFS mount to access it. If you prefer your data is stored encrypted, you will need to do some tweaking to the Rclone config.  At this type those tweaks are not documented here.

Media will be stored in `Movies` and `TV` folders, all within a `Media` folder in root (i.e. `/Media`). <a href="#note1" id="note1ref"><sup>[1]</sup></a>  

Saltbox is opinionated about this `/Media/<type>` file structure; changing it is not trivial.

## Setup

```
Media
├── Movies
├── Music
└── TV
```

- Example from Google Drive:

  ![](../images/google-drive-filesystem.png)

If you have media in other folders, you can simply move them into these folders via the Cloud Storage Provider's web site.

Note 1: For Google Drive, you can use the [Shift-Z trick](https://www.labnol.org/internet/add-files-multiple-drive-folders/28715/) to "symlink" folders here. 

Note 2: All the paths/folders mentioned here, and elsewhere, are **CASE SENSITIVE** (see  [[Saltbox Paths|Basics: Saltbox Paths]]).

## Google "My Drive" vs. "Shared Drives"

Google provides two "types" of storage in  a GSuite account: "My Drive" and "Shared Drives".

Shared Drives provide advantages for our purposes over My Drive, while My Drive offers no advantages over Shared Drives.

The primary advantage of Shared Drives is that access to them can be controlled via Service accounts, which allows credential rotation to increase upload limits and reduce likelihood of usage-based server-side bans.

Some newer related utilities [like the Golang "Autoscan" replacement for plex-autoscan] have features that work exclusively with Shared Drives.

The primary disadvantage ot Shared Drives is that they have a fixed limit of 400,000 files.  For this reason one common strategy is to create separate Shared Drives for each media type.

For those reasons, this documentation will discuss ONLY Shared Drives.

As a note, if you are unable to create Shared Drives in the Google Drive Web UI, that's a sign that you have the wrong type of Google Drive account.

  ![](../images/google-drive-acct.png)

---
 <sub> <a id="note1" href="#note1ref"><sup>1</sup></a> If you would like to customize your Plex libraries beyond what is listed above, see [Customizing Plex Libraries](../reference/customizing-plex-libs.md).</sub>
