# Inventory

Advanced use cases that would normally require editing roles can now be handled through the inventory system instead. 

Any variables defined in `/srv/git/saltbox/role_name/defaults/main.yml` are intended to be changeable by the user. This implementation avoids git merge conflicts when updating Saltbox.

Should you require additional functionality then by all means create an issue on the [main repository](https://github.com/saltyorg/Saltbox/) and we'll look at accommodating it.

Overrides are done in this file `"/srv/git/saltbox/inventories/host_vars/localhost.yml"` which does not exist by default.

Changing Sonarr/Radarr image tags:
``` yaml
radarr_docker_image_tag: nightly
sonarr_docker_image_tag: nightly
```
Which would override the docker image tags used when deploying the containers.