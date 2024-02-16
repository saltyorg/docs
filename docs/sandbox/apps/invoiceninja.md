# Invoice Ninja v5

## What is it?

[InvoiceNinja](https://www.invoiceninja.com/) is a self-hosted accounting system with ability to Quote & Invoice Clients, Time Billable-Tasks, Track Expenses, Get Paid.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.invoiceninja.com/){: .header-icons } | [:octicons-link-16: Docs](https://invoiceninja.github.io/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/invoiceninja/invoiceninja/tree/v5-stable){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/invoiceninja/invoiceninja/){: .header-icons }|

### 1. Installation

Ideally you should set a unique app key in settings.yml.
Generate the key using:

``` shell
docker run --rm -it invoiceninja/invoiceninja php artisan key:generate --show
```

insert this in the invoiceninja.app_key setting in `/opt/sandbox/settings.yml`

``` shell

sb install sandbox-invoiceninja

```

### 2. URL

- To access Invoice Ninja, visit `https://invoiceninja._yourdomain.com_`

### 3. Log in

Enter email, and password from accounts.yml setting.

- [:octicons-link-16: Documentation: Invoice Ninja Docs](https://invoiceninja.github.io/){: .header-icons }
