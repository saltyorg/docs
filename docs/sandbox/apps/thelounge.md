# The Lounge

## What is it?

[The Lounge](https://thelounge.chat/){: target=_blank rel="noopener noreferrer" } is a self hosted web IRC client. In private mode, The Lounge acts like a bouncer and a client combined, in order to offer an experience similar to other modern chat applications outside the IRC world. Users can then access and resume their session without being disconnected from their channels.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: The Lounge](https://thelounge.chat/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://thelounge.chat/docs){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/thelounge/thelounge ){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker: ](https://docs.linuxserver.io/images/docker-thelounge){: .header-icons target=_blank rel="noopener noreferrer" } |

### 1. Installation

``` shell

sb install sandbox-thelounge

```

### 2. URL

- To access The Lounge, visit `https://thelounge._yourdomain.com_`

### 3. Setup

- When the application first runs, it will populate its /config
- Stop the container
- Now from the host, edit /config/config.js, wherever you've mapped it
- In most cases you want the value public: false to allow named users only
- Setting the two prefetch values to true improves usability, but uses more storage
- Once you have the configuration you want, save it and start the container again
- For each user, run the command

      ``` shell
        docker exec -it thelounge s6-setuidgid abc thelounge add <user>
      ```
  - You will be prompted to enter a password that will not be echoed.
  - Saving logs to disk is the default, this consumes more space but allows scrollback.
- To log in to the application, browse to `https://thelounge._yourdomain.com_`
- You should now be prompted for a username and password on the webinterface.
- Once logged in, you can add an IRC network. Some defaults are preset for Freenode.

### ZNC

To connect to **[znc](../../sandbox/apps/znc.md)**, you need to have a **[znc](../../sandbox/apps/znc.md)** server running. A guide to using The Lounge with ZNC can be found [here](https://thelounge.chat/docs/guides/znc)

- In this image we have a ZNC network defined.

![ZNC network Screenshot](../../sandbox/images/znc_network.png)

- To add this network to The Lounge, give it a Name, it does not have to match the ZNC network settings.
- For the Server, use `znc` and set the port to `6502`
- For the Password, enter your `ZNC user password`
- Uncheck `Use secure connection (TLS)
- In the User Preferences section enter your Nick - I would recommend the same Nick as that set in ZNC.
- For the user name enter the `<ZNC username>/<ZNC_Network_Name>`.
- For Real Name, enter your desired `<real_name>` it does not need to match ZNC
- Save the network, and it should connect to ZNC.

![The Lounge network Screenshot](../../sandbox/images/lounge_network.png)

- [:octicons-link-16: Documentation: The Lounge Docs](https://thelounge.chat/docs){: .header-icons target=_blank rel="noopener noreferrer" }
