---
icon: material/desktop-classic
title: Plex DupeFinder
hide:
  - tags
tags:
  - plex-dupefinder
  - plex
  - cleanup
saltbox_automation:
  sections:
    inventory: false
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url:
      type: releases
    - name: Community
      url:
      type: community
  project_description:
    name: Plex DupeFinder
    summary: |
      a Python script designed to identify duplicate versions of media—such as TV episodes and movies—within a Plex library and remove the lowest-rated versions based on a customizable scoring system, leaving only a single, high-quality file.
    link: https://github.com/l3uddz/plex_dupefinder
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Plex DupeFinder

## Overview

[Plex DupeFinder](https://github.com/l3uddz/plex_dupefinder) is a Python script designed to identify duplicate versions of media—such as TV episodes and movies—within a Plex library and remove the lowest-rated versions based on a customizable scoring system, leaving only a single, high-quality file.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! note

    📢 You will need to have `allow media deletion: enabled` ticked. See the [Plex configuration instructions](https://github.com/l3uddz/plex_dupefinder#plex)

## Deployment

```shell
sb install sandbox-plex-dupefinder
```

## Usage

```shell
plex_dupefinder
```
