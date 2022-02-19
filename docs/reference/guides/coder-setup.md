# Using coder for editing

Coder is a version of VS Code that runs on your server.  It's friendlier than something like `nano`, and you can use it anywhere you can get at your domain.

## install coder

```
sb install sandbox-coder
```

By default, coder will be available at [https://coder.yourdomain.tld].

   ![](../../images/coder-setup/01-login.png)

The password is the one you set in `accounts.yml`

   ![](../../images/coder-setup/02-screen.png)

VSCode will by default be pointing to `/home/coder`, and on first startup you'll be presented with a checklist of "getting started" items.

If you've never used VSCode before, take a few minutes to go through the fundamentals tutorial.

You can change the default theme if you wish.  I'm going to choose the dark theme.

   ![](../../images/coder-setup/03-dark-mode-home-dir.png)

Probably, you want to edit config files for the apps, which are in `/opt`.

The host `/opt` dir is mounted into the container as `/host_opt/`.

Choose `File -> Open Folder...` from the hamburger menu on the upper left:

   ![](../../images/coder-setup/04-file-open-folder.png)

Navigate to `/host_opt/`, click the arrow:

   ![](../../images/coder-setup/05-host-opt.png)

and you should be presented with your `/opt` directory.  Most of the things you will want to edit are here.

   ![](../../images/coder-setup/06-host-opt.png)

I suggest you install a few extensions:

Click on the Extensions icon on the left, then type the name of the extension into the search box, and click the "install" button.

   ![](../../images/coder-setup/07-extensions.png)

Python:

   ![](../../images/coder-setup/08-python.png)

Rainbow-indent:

   ![](../../images/coder-setup/09-rainbow.png)

Redhat YAML:

   ![](../../images/coder-setup/10-yaml.png)

Better TOML:

   ![](../../images/coder-setup/11-toml.png)

Those are just suggestions; install others if you prefer.

Now, with these extensions installed, you should have syntax highlighting and indentation coloring for:

TOML

   ![](../../images/coder-setup/12-toml-sample.png)

YAML

   ![](../../images/coder-setup/13-yaml-sample.png)

JSON

   ![](../../images/coder-setup/14-json-sample.png)
