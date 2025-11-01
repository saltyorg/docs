---
hide:
  - tags
tags:
  - subliminal
  - subtitles
  - media
---

# Subliminal

## Overview

[Subliminal](https://github.com/Diaoul/subliminal) is a Python library and command-line tool to search and download subtitles for your videos. It supports multiple subtitle providers and languages, making it easy to find and download subtitles for your media collection.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Diaoul/subliminal){: .header-icons } | [:octicons-link-16: Docs](https://subliminal.readthedocs.io/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Diaoul/subliminal){: .header-icons } |

### 1. Installation

``` shell

sb install subliminal

```

### 2. Setup

Subliminal is available as a command-line tool after installation.

Download subtitles for a video:

``` shell
subliminal download -l en /path/to/video.mkv
```

Download for an entire directory:

``` shell
subliminal download -l en /path/to/media/
```

Common options: `-l` (language), `-s` (single best match), `-f` (force), `--age` (filter by age).

- [:octicons-link-16: Documentation: Subliminal Docs](https://subliminal.readthedocs.io/){: .header-icons }
