---
hide:
  - tags
tags:
  - cloudplow
  - config
---

# Cloudplow Config

NOTE: Everything here is specific to Google Drive.  If you are using Dropbox, there is nothing here that applies to you.

The default Cloudplow setup uploads to the `google` remote using a single account, which limits you to 750GB/day of upload.

To utilize rotating service accounts to upload more than this, you'll need to configure cloudplow to upload to the individual shared drives.

If you used the [scripted rclone method](rclone-manual.md), there is a script in the sb_gd repo that will make the required modifications to the cloudplow config.

NOTE: This script is assuming that your service account file are in `/opt/sa/all`, which is where the [scripted rclone method](rclone-manual.md) puts them.

The script is also assuming a totally stock Cloudplow `config.json` as it comes from the original saltbox install.  If you have added `remote`s or `uploader`s it will fail with an error.

This script is only useful if you have used the [scripted rclone method](rclone-manual.md).

AGAIN: This script is **only useful if you have used the [scripted rclone method](rclone-manual.md).**

This script is going to load the config from the last script in that process, and if it finds that config unmodified [specifically the prefix found in the config, which you create as part of that process] it will exit with a message to that effect.  There is no point in trying to circumvent this, since it is going to look for rclone remotes with specific names based on that prefix, which point at shared drives that it created with that prefix, etc.

### Important

You will have to have completed `sb install saltbox` before using this script.

1. Run the script

    ```shell
    cd /opt/sb_gd
    source sb_gd/bin/activate
    python sb_cp.py
    ```

    If that doesn't work, update to the latest version of the files from the repo with `git pull` and try again.

    If you see:
    ```
    There is no /opt/cloudplow/config.json here.
    ```
    You apparently ignored [this](#important) and have not completed the saltbox install, so cloudplow has not been installed, so its default config file in not present.  Complete the saltbox install then come back here.

2. Restart the cloudplow service:

    ```shell
    sudo systemctl restart cloudplow
    ```

3. Deactivate the virtual environment:

    ```shell
    deactivate
    ```

---

# Updating Cloudplow Config for additional shared drives

A backup of the stock `config.json` will be created as `config.json.old`; if you want to run this script a second time [perhaps you ran the previous script again and added some shared drives], run `cp config.json.old config.json` before running the script:

NOTE: This will overwrite the customized config.json, losing any changes you have made.  If the only changes you've made were via this script, that's totally safe.  If you've made other changes, they will be overwritten and you will have to repeat them

```shell
cd /opt/sb_gd
source sb_gd/bin/activate
cp /opt/cloudplow/config.json.old /opt/cloudplow/config.json
python sb_cp.py
sudo systemctl restart cloudplow
deactivate
```
