---
hide:
  - tags
tags:
  - misc
  - faq
---

# Misc

IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## Backup/Restore NextcloudDB

DB data is stored in /opt/mariadb and backed up along with Saltbox Backup.

However, you can separately make a backup of the DB into a single `nextcloud_backup.sql` file, by running the following command.

```shell
docker exec mariadb /usr/bin/mysqldump -u root --password=password321 nextcloud  > nextcloud_backup.sql
```

And restoring it back:

```shell
cat nextcloud_backup.sql | docker exec -i mariadb /usr/bin/mysql -u root --password=password321 nextcloud

```

## JSON Format Errors

Python or script errors mentioning an issue with the config file is usually due to an invalid JSON format in the file.

Examples:

```python
Traceback (most recent call last):
  File "scan.py", line 52, in <module>
    conf.load()
  File "/opt/plex_autoscan/config.py", line 157, in load
    cfg = self.upgrade(json.load(fp))
  File "/usr/lib/python2.7/json/__init__.py", line 291, in load
    **kw)
  File "/usr/lib/python2.7/json/__init__.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python2.7/json/decoder.py", line 364, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python2.7/json/decoder.py", line 380, in raw_decode
    obj, end = self.scan_once(s, idx)
ValueError: Expecting , delimiter: line 20 column 2 (char 672)
```

```python
Traceback (most recent call last):
  File "/opt/plex_autoscan/scan.py", line 52, in <module>
    conf.load()
  File "/opt/plex_autoscan/config.py", line 157, in load
    cfg = self.upgrade(json.load(fp))
  File "/usr/lib/python2.7/json/init.py", line 291, in load
    **kw)
  File "/usr/lib/python2.7/json/init.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python2.7/json/decoder.py", line 364, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python2.7/json/decoder.py", line 382, in raw_decode
    raise ValueError("No JSON object could be decoded")
ValueError: No JSON object could be decoded
```

```python
Traceback (most recent call last):
  File "/usr/local/bin/cloudplow", line 60, in <module>
    conf.load()
  File "/opt/cloudplow/utils/config.py", line 227, in load
    cfg, upgraded = self.upgrade_settings(json.load(fp))
  File "/usr/lib/python3.5/json/__init__.py", line 268, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.5/json/__init__.py", line 319, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.5/json/decoder.py", line 339, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.5/json/decoder.py", line 355, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 46 column 13 (char 1354)
```

Fixes:

1. Paste the JSON file at [jsonformatter.curiousconcept.com](https://jsonformatter.curiousconcept.com/) and click `process`. This will tell you what the issue is and fix it for you.

   or

2. Run:

   ```shell
   jq '.' config.json
   ```

   If there are no issues, it will simply print out the full JSON file.

   If there is an issue, a msg will display the location of the issue:

   ```text
   parse error: Expected separator between values at line 7, column 10
   ```
