---
hide:
  - tags
tags:
  - wishlist
  - gift
  - list
---

# Wishlist

## What is it?

[Wishlist](https://github.com/cmintey/wishlist) is a sharable wishlist for your friends and family

Wishlist is a self-hosted wishlist application that you can share with your friends and family. You no longer have to wonder what to get your parents for the holidays, simply check their wishlist and claim any available item. With a simple user interface, even the grandparents can get involved!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/cmintey/wishlist){: .header-icons } | [:octicons-link-16: Docs](https://github.com/cmintey/wishlist){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/cmintey/wishlist){: .header-icons } | [:material-docker: Docker](ghcr.io/cmintey/wishlist){: .header-icons }|

!!! warning This is not behind Authelia by default since Wishlist has its own authentication and allows configuration for public lists

### 1. Installation

``` shell
sb install sandbox-wishlist

```

### 2. URL

- To access Wishlist, visit `https://wishlist._yourdomain.com_`

### 3. Usage

Make sure to log in after Installation to configure the admin account.

The uploads and database files will be stored in `/opt/wishlist/`

See the [Wishlist GitHub](https://github.com/cmintey/wishlist) for more usage information.
