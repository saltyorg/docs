# LinuxGSM

## What is it?

[LinuxGSM](https://linuxgsm.com) is a command-line tool for quick and simple deployment and management of Linux dedicated game servers. It aims to make the process of managing game servers hassle-free. With LinuxGSM, we can avoid spending hours trying to configure and manage game servers. It provides a streamlined and efficient solution for setting up and maintaining dedicated game servers on Linux.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://linuxgsm.com){: .header-icons } | [:octicons-link-16: Docs](https://docs.linuxgsm.com){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/GameServerManagers/LinuxGSM){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gameservermanagers/gameserver){: .header-icons }|

### 1. Installation

To add instances, add the following to the inventory. See these instructions on inventory [here](../../saltbox/inventory/index.md).

``` yaml title="Inventory"

lgsm_instances: ["lgsm_valheim", "lgsm_rust"] # (1)!
lgsm_valheim_docker_image_tag: "vh" # (2)!
lgsm_valheim_docker_ports_defaults: ["2456:2456/udp","2457:2457/udp"] # (3)!
lgsm_rust_docker_ports_defaults: ["28015:28015/udp","28017:28017/udp","28082:28082/udp"] # (4)!

```

1. Example setting image tag to correct shortcode from <https://github.com/GameServerManagers/LinuxGSM/blob/master/lgsm/data/serverlist.csv> using lgsm_shortcode will automatically pull the correct image tag
2. This is the valheim server shortcode
3. ports for valheim need to be exposed. Notice that rust is the image tag for the rust server. This means we don't have to specify it here.
4. The ports for the rust server need to be exposed as well.

Then run:

``` shell

sb install sandbox-lgsm

```

This will start the installation of LinuxGSM using the specified image tag per instance, which allows for the installation and management of multiple game servers.

### 2. Setup

LinuxGSM config files are the configuration files used by the game server to store various game server settings, such as the server name, maximum players, map cycle, etc. These settings can be edited to customise a game server. Different game server configs can use different syntax and work slightly differently, but all do the same basic job of editing a game server settings.

The configs for the lgsm servers are in `/opt/CONTAINERNAME/config-lgsm/LGSMSERVERNAME/`
For our valheim example the config would be `/opt/lgsm_valheim/config-lgsm/vhserver/vhserver.cfg` which is the lgsm instance config for that server.

`/opt/lgsm_valheim/config-lgsm/vhserver/common.cfg` works as well. Can read more [here](https://docs.linuxgsm.com/configuration/game-server-config)

Any actual game server configs will be in the `/opt/CONTAINERNAME/serverfiles/` and are all dependant on the game server installed.

### 3. Join Server

In your game, connect to your ip and default ports for the server. Make sure you set the UDP and TCP for the ports correctly. If everything was setup correctly the game should connect to the server.

- [:octicons-link-16: Documentation: LGSM Docs](https://docs.linuxgsm.com/configuration/game-server-config){: .header-icons }
