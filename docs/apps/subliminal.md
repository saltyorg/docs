---
icon: material/desktop-classic
hide:
  - tags
tags:
  - subliminal
  - subtitles
  - media
saltbox_automation:
  app_links:
    - name: Manual
      url: https://subliminal.readthedocs.io
      type: documentation
    - name: Releases
      url:
      type: github
    - name: Community
      url: https://discord.gg/kXW6sWte9N
      type: discord
  project_description:
    name: Subliminal
    summary: |-
      a Python library and command-line tool to search and download subtitles for your videos.
    link: https://github.com/Diaoul/subliminal
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Subliminal

## Overview

[Subliminal](https://github.com/Diaoul/subliminal) is a Python library and command-line tool to search and download subtitles for your videos.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://subliminal.readthedocs.io){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/kXW6sWte9N){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install subliminal
```

## Usage

Subliminal is available as a command-line tool after installation.

Download subtitles for a video:

```shell
subliminal download -l en /path/to/video.mkv
```

Download for an entire directory:

```shell
subliminal download -l en /path/to/media/
```

Common options: `-l` (language), `-s` (single best match), `-f` (force), `--age` (filter by age).
