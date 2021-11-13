
---
IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## Stuck on "Waiting for running upload to finish before proceeding..."

If the activity log is stuck on:

```
2018-06-03 13:44:59,659 - INFO       - cloudplow            - do_upload                      - Waiting for running upload to finish before proceeding...
```

This means that an upload task was prematurely canceled and it left lock file(s) to prevent another upload.

To fix this, run this command:

```
rm -rf /opt/cloudplow/locks/*
```

or

```
sudo systemctl restart cloudplow
```

