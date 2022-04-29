# Invoice Ninja v5

## What is it?

[InvoiceNinja](https://www.invoiceninja.com/){: target=_blank rel="noopener noreferrer" } is a self-hosted accounting system with ability to Quote & Invoice Clients, Time Billable-Tasks, Track Expenses, Get Paid


- [:material-home: Project home ](https://github.com/invoiceninja/invoiceninja/tree/v5-stable){: .header-icons target=_blank rel="noopener noreferrer" } 
- [:octicons-link-16: Support Forum](https://forum.invoiceninja.com/){: .header-icons target=_blank rel="noopener noreferrer" } 
- [:material-docker: Docker ](https://hub.docker.com/r/invoiceninja/invoiceninja/){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation


Ideally you should set a unique app key in settings.yml. 
Generate the key using:
``` shell
docker run --rm -it invoiceninja/invoiceninja php artisan key:generate --show
```
insert this in the invoiceninka.app_key setting in settings.yml

``` shell

sb install sandbox-invoiceninja

```

### 2. URL

- To access Invoice Ninja, visit `https://invoiceninja._yourdomain.com_`

### 3. Log in.

Enter email, and password from accounts.yml setting.
