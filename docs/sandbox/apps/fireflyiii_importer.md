# Firefly III Data Importer

[TOC]

## What is it?

[Firefly III](https://www.firefly-iii.org) is a (self-hosted) manager for your personal finances. The data importer is built to help you import transactions into Firefly III. It is separated from Firefly III for security and maintenance reasons.

The data importer does not connect to your bank directly. Instead, it uses Nordigen and SaltEdge to connect to over 6000 banks worldwide. These services are free for Firefly III users, but require registration. Keep in mind these services have their own privacy and data usage policies.

The data importer can import CSV files you've downloaded from your bank.

You can run the data importer once, for a bulk import. You can also run it regularly to keep up with new transactions.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.firefly-iii.org/explanation/data-importer/about/introduction/){: .header-icons } | [:octicons-link-16: Docs](https://docs.firefly-iii.org/explanation/data-importer/about/introduction/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/firefly-iii/data-importer){: .header-icons } | [:material-docker: Docker](hhttps://docs.firefly-iii.org/how-to/data-importer/installation/docker/){: .header-icons }|

## 1. Installation

``` shell
sb install sandbox-fireflyiii_importer
```

## 2. URL

- To access the Firefly III Data Importer, visit `https://fireflyiii_importer._yourdomain.com_`

## 3. Setup

### 3.1 Connection To Firefly III
The Required variables that should be defined in [inventory](../../saltbox/inventory/index.md):

To authenticate the Data Importer to Firefly III you require to use either:

- [Access Token](#311-access-token)
- [~~Client ID~~](#312-client-id) ***Not Had Luck Getting This Working***

#### 3.1.1 Access Token

``` yaml title="Firefly III Data Importer Access Token Settings"
fireflyiii_importer_docker_envs_custom:
  - FIREFLY_III_ACCESS_TOKEN: ""  # (1)!
```

1. Your access token from your instance of Firefly III | Options | Profile | OAuth | Personal Access Tokens | Create New Token.

#### 3.1.2 Client ID

``` yaml title="Firefly III Data Importer Client ID Settings"
fireflyiii_importer_docker_envs_custom:
  - FIREFLY_III_CLIENT_ID: "1"  # (1)!
```

1. Your client id from your instance of Firefly III | Options | Profile | OAuth | OAuth Clients | Create New Client.
> Note: Your require to leave Confidential unticked

## 4. Additional Settings

> **Note: For all available settings please refer to the Firefly III Data Importer [example env](https://raw.githubusercontent.com/firefly-iii/docker/main/docker-compose-importer.yml)**

### 4.1 Email Notifications
To enable email notifications, set the following [inventory](../../saltbox/inventory/index.md) entries to your desired values:

``` yaml title="Firefly III Data Importer Email Settings"
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

Redeploy the Firefly III Importer Role role to apply the above changes.