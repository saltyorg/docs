---
icon: material/desktop-classic
title: ctop
hide:
  - tags
tags:
  - ctop
  - monitoring
  - docker
saltbox_automation:
  sections:
    inventory: false
  app_links:
    - name: Manual
      url: https://github.com/bcicen/ctop/blob/master/README.md#usage
      type: documentation
    - name: Releases
      url: https://github.com/bcicen/ctop/tags
      type: github
    - name: Community
      url:
      type: community
  project_description:
    name: ctop
    summary: |-
      a command-line, top-like tool for monitoring Linux containers in real-time.
    link: https://ctop.sh
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# ctop

## Overview

[ctop](https://ctop.sh) is a command-line, top-like tool for monitoring Linux containers in real-time.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/bcicen/ctop/blob/master/README.md#usage){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/bcicen/ctop/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install ctop
```

## Usage

```shell
ctop
```
