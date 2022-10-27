# Cherry

## What is it?

[Cherry](https://cherry.haishan.me/){: target=_blank rel="noopener noreferrer" } is a bookmark service that is open source.

- The code of Cherry service and the browser extension are all available on GitHub.

- It's self-hostable. Your data in in your own hands. Using SQLite, management and backup is a breeze.

- It has a simple UI. But you got all the features you want for a bookmark service. Tags, groups, full text search and browser extensions.

!!!info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://cherry.haishan.me/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://cherry.haishan.me/docs/intro){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/haishanh/cherry){: .header-icons target=_blank rel="noopener noreferrer" } |

### 1. Installation

``` shell

sb install sandbox-cherry

```

### 2. URL

- To access Cherry, visit `https://cherry._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

!!!note
    To create an additional user, use Cherry cli: `docker exec cherry cherry create-user <email> <password>`

- [:octicons-link-16: Documentation: Cherry Docs](https://cherry.haishan.me/docs/intro){: .header-icons target=_blank rel="noopener noreferrer" }
