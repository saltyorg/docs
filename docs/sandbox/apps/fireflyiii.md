# Firefly III

[TOC]

## What is it?

[Firefly III](https://www.firefly-iii.org) is a (self-hosted) manager for your personal finances. It can help you keep track of your expenses and income, so you can spend less and save more. Firefly III supports the use of budgets, categories and tags. Using a bunch of external tools, you can import data. It also has many neat financial reports available.

Firefly III should give you insight into and control over your finances. Money should be useful, not scary. You should be able to see where it is going, to feel your expenses and to... wow, I'm going overboard with this aren't I?

But you get the idea: this is your money. These are your expenses. Stop them from controlling you.

If your project has grown and deploying from the terminal is no longer for you then Semaphore UI is what you need.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.firefly-iii.org){: .header-icons } | [:octicons-link-16: Docs](https://docs.firefly-iii.org/?mtm_campaign=firefly-iii-org&mtm_kwd=top-link){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/firefly-iii/firefly-iii/){: .header-icons } | [:material-docker: Docker](https://docs.firefly-iii.org/how-to/firefly-iii/installation/docker/){: .header-icons }|

## 1. Installation

``` shell

sb install sandbox-fireflyiii

```

## 2. URL

- To access the Firefly III, visit `https://fireflyiii._yourdomain.com_`

## 3. Setup

## 4. Additional Settings

- The default installation utilises a seperate postgres database.
- This will install the fireflyiii core container and install the mariadb database
  - > **Note: It can be installed using postgresql and mysql**
- It will by default enable webhooks

> **Note: For all available settings please refer to the Firefly III [example env](https://raw.githubusercontent.com/firefly-iii/firefly-iii/main/.env.example)**

#### 4.1 Email Notifications
To enable email notifications, set the following [inventory](../../saltbox/inventory/index.md) entries to your desired values:

``` yaml title="Firefly III Email Settings"

MAIL_MAILER: "log"  # (1)!
MAIL_HOST: "localhost"  # (2)!
MAIL_PORT: "25"  # (3)!
MAIL_FROM: "fireflyiii@domain.com"  # (4)!
MAIL_USERNAME: ""  # (5)!
MAIL_PASSWORD: ""  # (6)!
MAIN_ENCRYPTION: ""  # (7)!
```

1. The MAIL_MAILER-setting indicates the system that is used for mailing. Firefly III supports the following mail systems: smtp, sendmail, mailgun, mandrill, sparkpost and log. [Here](https://docs.firefly-iii.org/how-to/firefly-iii/advanced/notifications/#email) is an explanation about each MAIL_MAILER option
2. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
4. Replace `25` with your email port. IE: `587`
3. The email address you want to send to. Replace `""` with the email address you want to send to
5. Replace `""` with your email username if necessary.
6. Replace `""` with your email password if necessary.
7. Use `SSL` or `TLS` for communication with the SMTP server. Can be `true` or '`false`.

### 4.2 Firefly III Authentication
By default this utilises the authelia authentication and utilises its own authentication mechanism

This can be changed to do 1 of the following:

- [Remove Authelia authentication (Not Recommended)](#421-remove-authelia-authentication-not-recommended)
- ~~Remove Firefly III built-in authentication~~ ***Not Understood***

#### 4.2.1 Remove Authelia Authentication (Not Recommended)

``` yaml title="Firefly III Remove Authelia"

fireflyiii_traefik_sso_middleware: ""
```

Redeploy the Firefly III role to apply the above changes.