# Bazarr

## Settings to limit API calls

All settings are documented in the [official docs](https://wiki.bazarr.media) - though most of the time the impact on Saltbox setups needs to be inferred.
Especially useful: [:octicons-link-16: Performance Tuning](https://wiki.bazarr.media/Additional-Configuration/Performance-Tuning/)

### Some settings of note - AS OF 22ND OCTOBER 2023 - MIGHT BE OUTDATED IF YOU READ THIS LATER

- `Settings` => `Subtitles` => `Performance / Optimization` Disable `Use Embedded Subtitles` Embedded subtitles are subtitles that are in the video container (mkv, mp4, etc) Bazarr needs to look inside the video container to know which subtitles are in it, causing issues with API Limits 

- `Settings` => `Languages` => `Embedded Tracks Language` Disable `Deep analyze media file to get audio tracks language.`

- `Settings` => `Subtitles` => `Performance / Optimization` Enable `Skip video file hash calculation` - (Possibly depending on the cloud backend) it seems to trigger a full read by multiple API calls instead of just getting the hash

- `Settings` => `Subtitles` => `Post-Processing` Disable `Automatic Subtitles Synchronization` - This one hurts quite a bit to disable, but if you are downloading multiple subtitles (like you just downloaded multiple series and they got pushed to the cloud by cloudplow before Bazarr pulled subs; or subs got released for a whole series en block, etc.) it will trigger Bazarr to download and analyze a whole bunch of files possibly triggering tens of thousands of API-calls.
