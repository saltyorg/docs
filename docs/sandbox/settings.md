# The Settings File

The configuration file for Saltbox Sandbox settings is called settings.yml and is located at `/opt/sandbox/settings.yml`

settings.yml

``` { .yaml .annotate }
---
example:  # (1)
  roles:
    - podcasts
    - poetry
notifiarr:  # (2)
  api_key: "api-key-from-notifiarr.com"
unifi:  # (3)
  port: 8080
```

1. Example role, provide a list of "examples's"
    For each listed item an Example instance will be created and the item set to the subdomain.

2. Notifiarr
    Add your notifiarr api key here.

3. Unifi
