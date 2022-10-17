All the apps are installed and configured, but here are some things you want to set up or do that aren't done automatically:

1. Harden your SSH server.  There are some tips [here](https://linuxhandbook.com/ssh-hardening-tips/), but three simple actions to take are:

    1. [Change the default SSH port](https://linuxhandbook.com/change-ssh-port/) from 22 to something else.

    1. [Disable password login](https://linuxhandbook.com/ssh-disable-password-authentication/) and use only SSH keys to authenticate.

    1. Disable root login.

    The above tips can be implemented via [adv_settings.yml](../../reference/accounts.md#options-in-adv_settingsyml).

2. Set up [scheduled backups](../backup/backup.md). **There is no backup enabled automatically**, so unless you explicitly set them up, you will be disappointed to find that you don't have a backup when something goes wrong.

3. Take some time to verify disk space usage for the apps.

    You need local disk space for stuff between download completion and cloudplow moving things into the cloud.  If you don't, for example, set cloudplow's upload thresholds and Nzbget's "stop downloading" disk space threshold to meaningful values for your situation, you can get into a situation where cloudplow's not uploading because that threshold hasn't been met and nzbget has stopped because its threshold has been met and everything grinds to a halt.  Alternatively, nzbget just keeps going and runs your disk out of space.

    You also need a bunch of disk space for the [scheduled backups](../backup/backup.md) that you just set up to succeed, so be sure to take that into account.

    Another common "hidden" disk space consumer is unfinished or unimported downloads.  If NZBGet downloads something and Radarr can't tell what movie it is, it will just sit consuming disk space.  There is a script you can set up to keep this stuff cleaned up in the [user crontab examples](../../advanced/user-crontab-examples.md).

4. Spend some time working with the system before you start customizing.  A **lot** of problems are seen when new users rush ahead to install All The Things and customize the system without understanding how things work.  Slow down.  Learn how the thing works, and then make changes in a controlled manner.

    None of these apps or scripts are sentient, so if they are not doing what you expect, it's almost certainly a configuration problem.

5. Take time to go through some Youtube or other tutorials about:

    1. JSON

        Many config files are written in JSON, so you need to have a grounding in how JSON works before editing them.  You should know how to edit within the structure of a JSON file, and how to validate a JSON file to figure out how you've broken it.

        1. [first "json tutorial" result; no endorsement](https://www.tutorialspoint.com/json/index.htm)

        2. [online JSON validator](https://jsonlint.com)

    2. YAML

        Many config files are written in YAML, so you need to have a grounding in how YAML works before editing them.

        1. [first "yaml tutorial" result; no endorsement](https://www.tutorialspoint.com/yaml/index.htm)

        2. [online YAML validator](http://www.yamllint.com/)

    3. Docker

        Nearly everything is running as a Docker container, so it's helpful to have at least a nodding familiarity with how that works.

        1. [first "docker tutorial" result; no endorsement](https://www.docker.com/101-tutorial)

Next, let's discuss how [updates](../basics/update.md) are done.
