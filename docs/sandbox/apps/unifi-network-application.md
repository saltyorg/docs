# Unifi Network Application

## What is it?

[Unifi Network Application](https://www.ui.com/download/unifi/) software is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.ui.com/download/unifi/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/linuxserver/docker-unifi-network-application/blob/main/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/linuxserver/docker-unifi-network-application){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/unifi-network-application){: .header-icons }|

!!! Warning
    This role is a replacement for the previous Unifi Controller role. This is not an in-place replacement. In order to migrate, you must perform a full backup from the Unifi web interface, and restore from that backup when running the setup wizard in a fresh instance of the Unifi Network Application.

### 1. Installation

``` shell

sb install sandbox-unifi-network-application

```

### 2. URL

- To access Unifi Network Application, visit `https://unifi._yourdomain.com_`

### 3. Setup

  1. Visit the Unifi Network Application site at `https://unifi._yourdomain.com_`

  2. For Unifi to adopt other devices, e.g. an Access Point, it is required to change the inform IP address. Because Unifi runs inside Docker by default it uses an IP address not accessible by other devices. To change this go to Settings > System Settings > Controller Configuration and set the Controller Hostname/IP to a hostname or IP address accessible by your devices. Additionally the checkbox "Override inform host with controller hostname/IP" has to be checked, so that devices can connect to the controller during adoption (devices use the inform-endpoint during adoption).

  In order to manually adopt a device take these steps:

  ```shell
  ssh ubnt@$AP-IP
  set-inform http://$address:8080/inform
  ```

  The default device password is `ubnt`. `$address` is the IP address of the host you are running this container on and `$AP-IP` is the Access Point IP address.

  When using a Security Gateway (router) it could be that network connected devices are unable to obtain an ip address. This can be fixed by setting "DHCP Gateway IP", under Settings > Networks > network_name, to a correct (and accessible) ip address.

- [:octicons-link-16: Documentation](https://github.com/linuxserver/docker-unifi-network-application/blob/master/README.md){: .header-icons }

!!! Note
      📢 The default setup only publish the 8080 tcp port, which is the bare minimum to allow communication between your network equipment and Unifi Network Application.
      Depending on your requirements, you may need additional ports according to the [:octicons-link-16: Documentation](https://github.com/linuxserver/docker-unifi-network-application#parameters) .

      The recommended way to customize these parameters is to use the [inventory](../../saltbox/inventory/index.md).

      Edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section:

      ```
      ### Open Specified Ports for the specified container ###
      ##### Unifi Ports for aditional services #####
      unifi_network_application_docker_ports_custom:
        - "1900:1900/udp" #Required for Make controller discoverable on L2 network option
        - "8843:8843/tcp" #Unifi guest portal HTTPS redirect port
        - "8880:8880/tcp" #Unifi guest portal HTTP redirect port
        - "6789:6789/tcp" #For mobile throughput test
        - "5514:5514/udp" #Remote syslog port
      ```
