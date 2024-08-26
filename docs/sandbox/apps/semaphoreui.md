# SemaphoreUI

## What is it?

[Semaphore UI](https://github.com/semaphoreui/semaphore) is a modern UI for Ansible, Terraform, OpenTofu and Pulumi. It lets you easily run Ansible playbooks, get notifications about fails, control access to deployment system.

If your project has grown and deploying from the terminal is no longer for you then Semaphore UI is what you need.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://semaphoreui.com){: .header-icons } | [:octicons-link-16: Docs](https://docs.semaphoreui.com/user-guide/projects){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/semaphoreui/semaphore?tab=readme-ov-file){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/semaphoreui/semaphore){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-semaphoreui

```

### 2. URL

- To access the Syncthing dashboard, visit `https://semaphoreui._yourdomain.com_`

### 3. Setup

### 4. Additional Settings

The default installation utilises a seperate postgres database. There is an option for this package to utilise mariadb / mysql but this isnt what this guide will be based on.

To enable email notifications, set these [inventory](../saltbox/inventory/index.md) entries to your desired values:

``` yaml title="Semaphoreui Email Settings"

SEMAPHORE_EMAIL_ALERT: "true" # (1)!
SEMAPHORE_EMAIL_SENDER: ""  # (2)!
SEMAPHORE_EMAIL_HOST: "localhost"  # (3)!¿˘˘˘˘˘˘˘˘˘¿¿˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘˘
SEMAPHORE_EMAIL_PORT: "25"  # (4)!¿˘˘˘˘˘˘
SEMAPHORE_EMAIL_USERNAME: ""  # (5)!
SEMAPHORE_EMAIL_PASSWORD: ""  # (6)!
SEMAPHORE_EMAIL_SECURE: ""  # (7)!
```

1. Flag which enables email alerts. Can be `true` or '`false`.
2. The email address you want to send to. Replace `""` with the email address you want to send to
3. Replace `localhost` with your email host. IE: `smtp-relay.gmail.com`
4. Replace `25` with your email port. IE: `587`
5. Replace `""` with your email username if necessary.
6. Replace `""` with your email password if necessary.
7. Use `SSL` or `TLS` for communication with the SMTP server. Can be `true` or '`false`.

``` yaml title="Semaphoreui Telgram Settings"

SEMAPHORE_TELEGRAM_ALERT: ""  # (1)!
SEMAPHORE_TELEGRAM_CHAT: ""  # (2)!
SEMAPHORE_TELEGRAM_TOKEN: ""  # (3)!
```

1. Flag which enables telegram alerts. Can be `true` or '`false`.
2. The chat id of which you want to send the message to
3. Your Telegram bot token

``` yaml title="Semaphoreui Telgram Settings"

SEMAPHORE_SLACK_ALERT: ""  # (1)!
SEMAPHORE_SLACK_URL: ""  # (2)!
```

1. Flag which enables telegram alerts. Can be `true` or '`false`.
2. Your slack URL

Redeploy the Semaphoreui role to apply any of the above changes.
