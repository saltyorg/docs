# Sarotate

## What is it?

[Sarotate](https://github.com/saltydk/SARotate){: target=_blank rel="noopener noreferrer" } is for rotating Google Service Accounts to spread the API load in an attempt to avoid Rclone mount file access problems with heavy API traffic.

Parses the specified Service Account files and automatically identifies the projects that they are a part of and rotates between projects where possible to spread API usage across projects.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/saltydk/SARotate){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/saltydk/SARotate#configuration){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/saltydk/SARotate){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-sarotate

```

### 2. Usage

- After installing the role, add your SA path to the settings file in `/opt/sandbox/settings.yml`

- Example

  ``` { .yaml}
  sarotate: 
  remotes: ["google"]
  sa_path: "/opt/sa/all" # Change this as needed
  sleeptime: # Optional. Default is 300
  rc_port: # Default is localhost:5572
  rc_user: # Optional. Default is blank
  rc_pass: # Optional. Default is blank
  apprise: # Optional. Add an apprise url if it suits you

  ```

**remotes:** if you have a different union in your rclone.conf (typically located @ `/home/user/.config/rclone/`) you will want to supply that name here. The saltbox default is google.

**sa_path:** supply the path to your service accounts. Saltbox default is `/opt/sa/all`

Heres a short example of the `config.yaml` in `/opt/sarotate/`.

```yaml

rclone:
  sleeptime: 300

remotes:
  '/opt/sa/all':
    random_header-TV:
      address: localhost:5572
      user:
      pass:
    random_header-Anime:
      address: localhost:5572
      user:
      pass:

notification:
  errors_only: y
  apprise:
    - ''

```

- [:octicons-link-16: Documentation: Sarotate Docs](https://github.com/saltydk/SARotate){: .header-icons target=_blank rel="noopener noreferrer" }
