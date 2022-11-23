# Absolute Series Scanner and HAMA role for anime

## What is it?

[asshama](https://github.com/ZeroQI/Absolute-Series-Scanner){: target=_blank rel="noopener noreferrer" } will install the [Absolute Series Scanner (ASS)](https://github.com/ZeroQI/Absolute-Series-Scanner){: target=_blank rel="noopener noreferrer" } and the [HTTP Anidb Metadata Agent (HAMA)](https://github.com/ZeroQI/Hama.bundle){: target=_blank rel="noopener noreferrer" }.

HAMA is a plex agent specifically for anime and its various challenges. It is recommended to use the HAMA agent with the Absolute Series Scanner (ASS). Hama agent features include: -

* Both Movies and Series Agent
* AniDB ID to TVDB/TMDB ID matching (with studio and episode mapping list) with ScudLee's xml mapping file
* Posters from TVDB (assign a poster to each anidb id in anidb to tvdb mapping file to avoid poster duplicates)
* TVDB episode screenshots
* Episode summary (in English only) courtesy of TVDB through ScudLee's XML episode mappings
* Uses studio from mapping file then AniDB (as often missing from AniDB)
* Search part entirely local through AniDB HTML API database file anime-titles.xml
* Separate language order selection for the series name and episode titles in Agent Settings (Supports Kanji characters in folders, filenames, titles)
* Warnings in html report files (no poster available, episode summary empty, TVDB id not in mapping file) to allow the community to update more easily the mapping XML or TVDB, list of missing episodes
* Collection mapping from ScudLee's movie collection ammended with AniDB RelatedAnime field
* Unique posters by using the anidbid rank in the mapping to rotate the posters
* when a serie is not found in AniDB, search TVDB and TMDB automatically
* Trakt scrobbling supports Hama guids

## Project Information

- [:material-home: Absolute Series Scanner (A.S.S.)](https://github.com/ZeroQI/Absolute-Series-Scanner){: target=_blank rel="noopener noreferrer" }
- [:material-home: HTTP Anidb Metadata Agent (HAMA)](https://github.com/ZeroQI/Hama.bundle){: target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install asshama

```

### 3. Setup

- [:octicons-link-16: Documentation](https://github.com/ZeroQI/Hama.bundle){: .header-icons target=_blank rel="noopener noreferrer" }
