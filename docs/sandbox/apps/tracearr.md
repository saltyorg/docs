---
icon: material/docker
hide:
  - tags
tags:
  - tracearr
  - monitoring
  - statistics
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.tracearr.com
      type: documentation
      purpose: manual
    - name: Releases
      url: https://github.com/connorgallopo/Tracearr/pkgs/container/tracearr
      type: github
      purpose: release
    - name: Community
      url: https://discord.gg/a7n3sFd2Yw
      type: discord
      purpose: community
  project_description:
    name: Tracearr
    summary: |-
      a monitoring platform for Plex, Jellyfin, and Emby that tracks active streams, playback history, and account sharing.
    link: https://tracearr.com
    categories:
      - Accessories > For Media Server > Monitoring
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-tracearr
```

## Usage

Visit <https://tracearr.iYOUR_DOMAIN_NAMEi>.

The first account created becomes the owner. Add media servers by their container address, for example `http://plex:32400` or `http://jellyfin:8096`.

To require a code before that first account can be created, set one in `/srv/git/saltbox/inventories/host_vars/localhost.yml` before deploying:

```yaml
tracearr_role_docker_envs_custom:
  CLAIM_CODE: "your-code"
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
