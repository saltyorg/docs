# Danger Zone :material-sign-caution:

Override patterns that may compromise the security or stability of your setup and fall **outside our support** scope. Proceed at your own risk.

## Authelia App Bypass

Some users may not want the additional layer of security that Authelia provides. An override is available to disable the middleware on a per-app basis:

!!! danger "Before continuing, ensure that fallback measures are in place to prevent unauthorized access to any of your apps."

```yaml
### Authelia App Bypass ###
xROLE_NAMEx_traefik_sso_middleware: ""
```

To determine which apps are included in Authelia by default, you can run this command:

```shell
grep -Ril '_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"' /srv/git/saltbox/roles /opt/sandbox/roles | awk 'BEGIN{RS="roles/"; FS="/defaults"}NF>1{print $1}' | sort -u
```

Should you wish to enable Authelia on an application that did not previously use it you do something similar as above but use a different value to enable it:

```yaml
xROLE_NAMEx_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
```

It should be noted that we take care of whitelisting any API endpoints when enabling Authelia for you so ask on the discord if you have trouble with enabling Authelia on an application that needs to have its API whitelisted and the below example isn't enough.

```yaml
xROLE_NAMEx_traefik_api_enabled: true
xROLE_NAMEx_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"
```

## Authorize with App Credentials

__Inject an Authorization header - Traefik performs basic auth with the backend app__

This will allow you to keep basic auth enabled within apps while avoiding the hassle of entering the credentials manually. The authorization header is only inserted if the request is authorized through the SSO middleware (Authelia) and is not applied to the API endpoint(s).

You can use [this tool](https://www.blitter.se/utils/basic-authentication-header-generator/) to generate the header contents based on your credentials.

```yaml
xROLE_NAMEx_docker_labels_custom:
  traefik.http.middlewares.appAuth.headers.customrequestheaders.Authorization: "Basic <base64 header>"
xROLE_NAMEx_traefik_middleware_custom: "appAuth"
```

## Plex Shared Data

=== "2 instances"

    ```yaml
    #### Shared metadata between all Plex instances ####
    plex2_docker_volumes_custom:
      - "{{ plex_paths_application_support_location }}/Media:/config/Library/Application Support/Plex Media Server/Media:ro"
      - "{{ plex_paths_application_support_location }}/Metadata:/config/Library/Application Support/Plex Media Server/Metadata:ro"
    ```

=== "Many instances (option A)"

    ```yaml
    #### Shared metadata between all Plex instances ####
    plex_shared_data:
      - "{{ plex_paths_application_support_location }}/Media:/config/Library/Application Support/Plex Media Server/Media:ro"
      - "{{ plex_paths_application_support_location }}/Metadata:/config/Library/Application Support/Plex Media Server/Metadata:ro"

    plex2_docker_volumes_custom: "{{ plex_shared_data }}"
    plex3_docker_volumes_custom: "{{ plex_shared_data }}"
    # .. additional lines for additional instances
    ```

=== "Many instances (option B)"

    ```yaml
    #### Shared metadata between all Plex instances ####
    plex_role_docker_volumes_custom:
      - "{{ plex_paths_application_support_location }}/Media:/config/Library/Application Support/Plex Media Server/Media:ro"
      - "{{ plex_paths_application_support_location }}/Metadata:/config/Library/Application Support/Plex Media Server/Metadata:ro"
    plex_docker_volumes_custom: [] # (1)! You can add mounts to this but don't remove it, or the base instance will lose write permissions to its metadata directories.
    ```
    
    1.  You can add other mounts to this but do not remove it.
        
        Clears the base instance of its own shares, so it retains write permissions to those directories.
