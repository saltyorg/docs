# Autoscan rewrites

These rewrites seem to cause a lot of consternation.

This article will attempt to clear them up.

## Why are rewrites needed in autoscan?

Basically, autoscan rewrites are a way to convert a path as one thing [typically an app like Sonarr] sees it to a path where another thing [typically an app like Plex] sees it.

The source of the scan [Sonarr, for example] sees a thing at one path, and the target of scan [Plex, for example] may see the same file at a different path. Autoscan uses "rewrites" to convert the source path to the target path.

## Do I always need rewrites?

No.

If Sonarr and Plex both see an episode at `/mnt/unionfs/Media/TV/SomeShow/Season 01/SomeShow S01E01.mkv`, then no rewrite is needed.

If you are setting up saltbox from scratch and use our recommended paths, your autoscan config needs no rewrites for Sonarr/Radarr/Lidarr [a-train or inotify triggers probably still need rewrites].

Rewrites *are* needed when:
```
/the/path/where/the/trigger/sees/files
```
and 
```
/the/path/where/the/target/sees/files
```
are different.

Sonarr has a root directory:

![](images/autoscan-01-sonarr-root.png)

This directory might be internal to the container, as this one is.

Shows are stored in that root:

![](images/autoscan-02-sonarr-show.png)

As are episodes, of course:

![](images/autoscan-03-sonarr-episode.png)

This episode path is what Sonarr is going to send to Autoscan.

Similarly, a Plex library has a root path:

![](images/autoscan-04-plex-library.png)

And things in that library are relative to that root:

![](images/autoscan-05-plex-episode.png)

Those two paths are different, so Autoscan needs a rewrite to change this path:
```
/tv/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
```
to this path:
```
/data/TV/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
```
so Plex can see it.

## What happens during a scan:

Sonarr tells Autoscan:

> "Here's a new thing at `/tv/#killerpost (2016)/Season 1/#killerpost - S01E01.mkv`, tell your friends."

Autoscan first needs to figure out which library to tell Plex about, since it's going to say:

> "Please scan this folder: `/tv/#killerpost (2016)/Season 1/`; it's in library something-or-other."

So Autoscan looks for a Plex library that has `/tv/` as one of its root directories. If it finds that to be library ID 12, it tells Plex:

> "Please scan this folder: `/tv/#killerpost (2016)/Season 1/`; it's in library **12**."

Howver, in our example above, the Plex library is pointed at `/data/TV`, so Autoscan won't be able to find the target library [there isn't one with `/tv/` as one of its root dirs], so Autoscan will report:

```
No target libraries found error="/tv/#killerpost (2016)/Season 1/: failed determining libraries" target=plex url=https://plex.xYOUR_DOMAIN_NAMEx/
```

This problem is what rewrites are used to solve.

## Example rewrite process:

One way to do this is shown in [Autoscan's README](https://github.com/Cloudbox/autoscan#full-config-file):

```
  sonarr:
    - name: sonarr
      priority: 2

      rewrite:
        - from: /tv/
          to: /mnt/unionfs/Media/TV/

targets:
  plex:
    - url: https://plex.xYOUR_DOMAIN_NAMEx
      token: XXXX
      rewrite:
        - from: /mnt/unionfs/Media/
          to: /data/
```

Sonarr sends a path to Autoscan, which uses this rewrite:
```
      rewrite:
        - from: /tv/
          to: /mnt/unionfs/Media/TV/
```
to make this change:
```
                  /tv/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
|||||||||||||||||||||
/mnt/unionfs/Media/TV/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
```
then queues the scan.

Later, when Autoscan goes to send the scan to Plex, it uses this rewrite:
```
      rewrite:
        - from: /mnt/unionfs/Media/
          to: /data/
```
to make this change:
```
/mnt/unionfs/Media/TV/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
||||||||||||||||||
             /data/TV/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
```
so it matches what Plex expects.

Using this method might be useful if you have multiple targets:
```
targets:
  plex:
    - url: https://plex.xYOUR_DOMAIN_NAMEx
      token: XXXX
      rewrite:
        - from: /mnt/unionfs/Media/
          to: /plex/sees/files/here/
  emby:
    - url: https://emby.xYOUR_DOMAIN_NAMEx
      token: XXXX
      rewrite:
        - from: /mnt/unionfs/Media/
          to: /emby/sees/files/here/
```
so that the local `/mnt/unionfs/Media/` path is used as a common interchange.

You could also do this with a single rewrite as:
```
  sonarr:
    - name: sonarr
      priority: 2

      rewrite:
        - from: /tv/
          to: /data/TV/

targets:
  plex:
    - url: https://plex.xYOUR_DOMAIN_NAMEx
      token: XXXX
```

The Sonarr rewrite goes straight to the final path required by Plex:
```
     /tv/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
||||||||
/data/TV/#killerpost (2016) (tvdb-307250)/Season 1/#killerpost - S01E01 (tvdb-307250) Payne Potter [HDTV-720p x264 AC3 5.1]-W4F.mkv
```
and Plex accepts the path as is.

Of course, that works best when there's only a single target. 
