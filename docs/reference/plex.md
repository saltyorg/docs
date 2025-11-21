---
hide:
  - tags
tags:
  - plex
  - emby
---

# Plex or Emby Account

## Plex

You'll need a free [Plex account](https://www.plex.tv/sign-up/) for the setup, if you don't already have one.

It's easiest if you have a Plex account *even if you're not planning to use Plex*. The default `saltbox` install assumes that you are using Plex, and without a Plex account in the settings, it will fail in various ways as it tries to install Plex and then things that depend on Plex. This can be worked around[^1], and may change in the future, but for now the simplest route is to sign up for that free account, and then disable Plex after install if you don't want to use it.

[^1]: Basically, run the `core` tag instead of the `saltbox` tag, then run the tags for the apps you want individually.

## Emby

You can use [Emby](https://emby.media/) in lieu of Plex (admonitions above about needing a Plex account for install still apply).

Sign up for a free Emby Connect account at <https://emby.media/connect.html>, if you don't already have one.

You'll need to install Emby manually after the initial install is complete.
