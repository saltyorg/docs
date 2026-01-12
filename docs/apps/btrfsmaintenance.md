---
icon: material/play
title: BTRFS Maintenance
hide:
  - tags
tags:
  - btrfs
  - btrfsmaintenance
saltbox_automation:
  sections:
    inventory: false
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://github.com/kdave/btrfsmaintenance/tags
      type: github
    - name: Community
      url:
      type: community
  project_description:
    name: BTRFS Maintenance
    summary: |
      a set of scripts designed to automate key maintenance tasks for the BTRFS filesystem, including scrubbing, balancing, trimming, and defragmentation.
    link: https://github.com/kdave/btrfsmaintenance
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# BTRFS Maintenance

## Overview

[BTRFS Maintenance](https://github.com/kdave/btrfsmaintenance) is a set of scripts designed to automate key maintenance tasks for the BTRFS filesystem, including scrubbing, balancing, trimming, and defragmentation.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/kdave/btrfsmaintenance/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install btrfsmaintenance
```
