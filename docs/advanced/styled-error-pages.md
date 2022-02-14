# Styled Error Pages

## What is this?

If this flag is set in the `adv_settings.yml`:

```
  error_pages: yes
```

All common error pages will be displayed with some consistent styling, based on [this system](https://github.com/tarampampam/error-pages).

## What themes are available?

There are initially seven "themes" available, which are stored in `/opt/error_pages`:

```
cats  ghost  hacker-terminal  l7-dark  l7-light  noise  shuffle
```
Samples of the themed pages can be viewed [here](https://tarampampam.github.io/error-pages/)


## How do I change the theme?

The default theme is `l7-dark`.

Changing the theme can be done via the [inventory](../saltbox/inventory/index.md):

```
error_pages_template: "hack-terminal"
```

## Can I create a theme?

Duplicate one of the directories in `/opt/error_pages` and make your changes.
