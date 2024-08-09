---
hide:
  - tags
tags:
  - oauth
  - oidc
  - idp
---

# IDP/OIDC Configuration

To configure Authentik as an IDP (Identity Provider) or OIDC (OpenID Connect) provider, follow these steps:

Click on the `Admin Interface` button in the top right corner.

Locate the `Applications` tab on the left panel and click on it.

Near the center of the screen select the blue `Create With Wizard` button.

- Below you will see the `Create Application` screen.

    ![Create Application](../../images/authentik/authentik-create-application-screenshot.png)

On the next screen select the `Oauth2/OIDC` option. (This will be the first option)

In this example, on the `Configure OAuth2/OpenId Provider` screen, only the required fields will be filled.

- Below you will see the `Configure OAuth2` screen.

    ![Configure Oauth2](../../images/authentik/authentik-configure-oauth2.png)

Under the `Protocol Settings` section, fill in the following fields:

- `Client ID`: `immich` (This can be anything you want, and is auto filled in. You can change it if you want)
- `Client Secret`: Its probably best to leave this as is, but you can change it if you want.
- `Redirect URI/Origins`:
  - `https://immich.your_domain.com/auth/login`
  - `https://immich.your_domain.com/user-settings`
  - `app.immich:/`

## OIDC Configuration Example

In the screenshot below, you can see how the [Immich](../../sandbox/apps/immich.md) application is configured to use Authentik as an OIDC provider.

![Authentik Oauth Example](../../images/authentik/authentik-oauth-example.png)

The only other field you need to concern yourself with is the `Mobile Redirect URI`, which is (in this case/example) `https://immich.your_domain.com/api/oauth/mobile-redirect`.
