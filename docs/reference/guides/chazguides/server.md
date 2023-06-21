# Can I run Saltbox on this server?

Yes.

Wait, no.

Um, maybe.  Try it and see.

The answer to this question depends on a whole bunch of things, including but not limited to:

- CPU
- Memory
- Storage type
- Format of media
- Location of server
- Location of clients
- Type of clients
- Number of simultaneous streams
- Transcoding or not
- Expectations of clients
- Random nonsense

## Server Hardware

For example, at time of writing the author had a Hetzner EX42-NVME in Helsinki.  Nearly all users were in the Minneapolis area on Comcast cable.  One user in Utah, one in Brisbane, Australia.  No 4K media.  The box was an AIO; usenet downloading happened on that box as well as streaming and no throttles were in place to slow NZBget or Cloudplow while Plex was streaming.

For the most part, this box met requirements during its tenure.  All author's streaming happened over a 1G fiber line to an AppleTV.  Most other active streamers used Plex Web, Roku, or a Smart TV Plex app.  The guy in Brisbane had trouble streaming due to his local ISP [Telstra], but streaming worked great from a Gold Coast hotel.

However, another fellow, who lives blocks away from the author, got one of these same servers and found it unusable for his target usage.  Maybe that was a config issue [didn't seem to be], but it illustrates that there is no "one-size-fits-all" answer.

Ultimately, there’s not really a sure way to answer this question.

Plex’ article on the topic is [here](https://support.plex.tv/articles/200375666-plex-media-server-requirements/).

## Plex Metadata

Plex saves metadata [posters, etc] for all your media; that gets stored in `/opt/plex` and as your library grows so does that directory.  Required disk space therefore grows over time.  This directory can be quite large.

For example:

Here Plex has 9640 movies and 137140 TV episodes.  Radarr is tracking 11608 movies and Sonarr 3070 series.

[These displays are produced by `ncdu` a command-line tool that shows disk usage; they're showing the content of the /opt directory]

```text
ncdu 1.14.1 ~ Use the arrow keys to navigate, press ? for help
--- /opt -------------------------------------------------------
   78.3 GiB [##########] /plex
   10.0 GiB [#         ] /radarr
    4.2 GiB [          ] /sonarr
```

Here Plex contains a lot more than that.

```text
ncdu 1.12 ~ Use the arrow keys to navigate, press ? for help
--- /opt -------------------------------------------------------
  274.5 GiB [##########] /plex
    7.4 GiB [          ] /tautulli
```

## Plex transcoding

Ideally, all your clients would Direct Play everything; in that case the server is just shoveling bits out as fast as it can and you don’t need any CPU power.  In practice, some transcoding will be happening.

There are two types of video transcoding; hardware or software.  Software video transcoding is CPU intensive, but higher-quality.  Hardware video transcoding doesn’t burden your CPU [so it’s free to continue extracting rar files or something], but it’s typically lower quality.  Depending on the specific CPU, dramatically lower quality.

Some Intel CPUs support hardware video transcoding, a smaller subset of AMD processors support hardware video transcoding, so if you want hardware video transcoding you probably want Intel [assuming you’re not using a separate GPU on a video card to do it].

Audio transcoding is always done by the CPU, but is generally far less resource-intensive.

But that’s just Plex.

## Context Acquisition

You’re looking to run Saltbox, so chances are you’re downloading via Usenet or torrents, so there are other concerns.

### Usenet

Usenet is all about speed of disk access as things are unrar’ed.  An SSD should be considered required, and NVME highly recommended.  In practical terms, you should have at least 300GB of space available for downloading and extracting.  That’s a general idea; sure you can make do with less, but it may be tight.  The author's first cloud server had a 160GB disk, and it was very tight.

### Torrents

If you’re downloading torrents from private servers, you probably need to seed things for some minimal amount of time; so multiple TBs of disk space are a plus.

## Client Peering to the Server

Depending on where you are in the world, peering to cloud servers will be different.  If you’re in the US, Hetzner’s German data centers are typically pretty good, but YMMV.

If you want a server in the US for that reason, it will probably be more expensive.

And so on.

So, the only way to answer this question is:

Maybe; try it and see.

The other way this question is posed is:

## What is the cheapest VPS or dedi on which I can run saltbox?

That question cannot be answered in any meaningful sense other than the requirements laid out in the docs.

Saltbox itself and the apps it installs do not have particularly great hardware requirements to *run*.  Some docker containers, a couple services.  You can *install* Saltbox on a tiny little Digital Ocean instance or the like.

The apps obviously have higher requirements if you want them to actually *do* anything, so whether a given box will work for *you* is entirely down to what *you’re* going to do with it.

Refer to the previous section.

Again, the only way to answer this question is:

Maybe; try it and see.
