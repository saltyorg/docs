# Styled Error Pages

## What is this?

If this flag is set in the `adv_settings.yml`:

```yaml
  error_pages: yes
```

Common error pages can be displayed with some consistent styling, based on [this system](https://github.com/tarampampam/error-pages).

## What themes are available?

There are initially seven "themes" available, which are stored in `/opt/error_pages`:

```text
cats  ghost  hacker-terminal  l7-dark  l7-light  noise  shuffle
```

Samples of the themed pages can be viewed [here](https://tarampampam.github.io/error-pages/)

## How do I change the theme?

The default theme is `l7-dark`.

Changing the theme can be done via the [inventory](../saltbox/inventory/index.md):

```yaml
error_pages_template: "hacker-terminal"
```

## How do I enable the error pages?

Enable error pages per role by adding the following to the [inventory](../saltbox/inventory/index.md) as desired:

```yaml
rolename_traefik_error_pages_enabled: true
```

`rolename` is, of course, the name of the role, as:

```yaml
sonarr_traefik_error_pages_enabled: true
```

These error pages do not work with every app; do your own a/b testing to verify that nothing unexpected results.

You can find the Saltbox roles that are known to NOT work with:

```bash
grep -Ril "_traefik_error_pages_enabled: false" /srv/git/saltbox/roles | cut -d/ -f6 | sort -u
```

You can find the Sandbox roles that are known to NOT work with:

```bash
grep -Ril "_traefik_error_pages_enabled: false" /opt/sandbox/roles | cut -d/ -f5 | sort -u
```

## Can I create a theme?

Duplicate one of the directories in `/opt/error_pages` and make your changes.
