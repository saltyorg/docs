# Sarotate

## What is it?

[sarotate](https://github.com/saltydk/SARotate){: target=_blank rel="noopener noreferrer" } is for rotating Google Service Accounts to spread the API load in an attempt to avoid Rclone mount file access problems with heavy API traffic.

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
  sleeptime: 
  rc_port: 
  rc_user: 
  rc_pass: 
  apprise:
  ```

- [:octicons-link-16: Documentation: Sarotate Docs](https://github.com/saltydk/SARotate){: .header-icons target=_blank rel="noopener noreferrer" }
