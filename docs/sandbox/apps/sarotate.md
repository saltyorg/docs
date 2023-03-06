# Sarotate

## What is it?

[Sarotate](https://github.com/saltydk/SARotate){: target=_blank rel="noopener noreferrer" } is for rotating Google Service Accounts to spread the API load in an attempt to avoid Rclone mount file access problems with heavy API traffic.

Parses the specified Service Account files and automatically identifies the projects that they are a part of and rotates between projects where possible to spread API usage across projects.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/saltydk/SARotate){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/saltydk/SARotate#configuration){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/saltydk/SARotate){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

- Before installing the role, add your SA path to the settings file in `/opt/sandbox/settings.yml` and supply the remotes or union in your rclone.conf file.

- Example

  ``` { .yaml}
  ...
  sarotate: 
    remotes: ["your_remote", "your_remote2", "your_union"]
    sa_path: "/opt/sa/all" # Change this as needed
    sleeptime: # Optional. Default is 300
    rc_port: # Default is localhost:5572
    rc_user: # Optional. Default is blank
    rc_pass: # Optional. Default is blank
    apprise: # Optional. Add an apprise url if it suits you
  ...
  ```

**remotes:** This will take individual drives, or a union remote, like `google`. Sarotate will  resolve the backend remotes for building the config from `/home/user/.config/rclone/`. You will want to supply that name here. If you don't use a union, list all of the remotes individually here instead, formatted like it is above.

**sa_path:** Supply the path to the directory holding your service accounts. Our automated shared drive script uses `/opt/sa/all`.

Run the tag and install the service.

``` shell

sb install sandbox-sarotate

```

To check the status of the service, you can run:

```shell

sudo systemctl status sarotate.service

```

You can also follow the logs with:

```shell

tail -f /opt/sarotate/sarotate.log

```

- [:octicons-link-16: Documentation: Sarotate Docs](https://github.com/saltydk/SARotate){: .header-icons target=_blank rel="noopener noreferrer" }
