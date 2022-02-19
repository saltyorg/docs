# Unifi Controller

## What is it?

[Unifi Controller](https://www.ui.com/download/unifi/){: target=_blank rel="noopener noreferrer" } software is a powerful, enterprise wireless software engine ideal for high-density client deployments requiring low latency and high uptime performance.


| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://www.ui.com/download/unifi/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/linuxserver/docker-unifi-controller/blob/master/README.md){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/linuxserver/docker-unifi-controller){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/linuxserver/unifi-controller){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-unifi

```

### 2. URL

- To access Unifi Controller, visit `https://unifi._yourdomain.com_`

### 3. Setup

  1. Visit the Unifi Controller site at `https://unifi._yourdomain.com_`

  2. For Unifi to adopt other devices, e.g. an Access Point, it is required to change the inform IP address. Because Unifi runs inside Docker by default it uses an IP address not accessible by other devices. To change this go to Settings > System Settings > Controller Configuration and set the Controller Hostname/IP to a hostname or IP address accessible by your devices. Additionally the checkbox "Override inform host with controller hostname/IP" has to be checked, so that devices can connect to the controller during adoption (devices use the inform-endpoint during adoption).

  In order to manually adopt a device take these steps:

  ```
  ssh ubnt@$AP-IP
  set-inform http://$address:8080/inform
  ```

  The default device password is `ubnt`. `$address` is the IP address of the host you are running this container on and `$AP-IP` is the Access Point IP address.

  When using a Security Gateway (router) it could be that network connected devices are unable to obtain an ip address. This can be fixed by setting "DHCP Gateway IP", under Settings > Networks > network_name, to a correct (and accessible) ip address.


- [:octicons-link-16: Documentation](https://github.com/linuxserver/docker-unifi-controller/blob/master/README.md){: .header-icons target=_blank rel="noopener noreferrer" }

!!! Note
      📢 The default setup only publish the 8080 tcp port, which is the bare minimum to allow communication between your network equipment and Unifi Controller.
      Depending on your requirements, you may need additional ports according to the [:octicons-link-16: Documentation](https://github.com/linuxserver/docker-unifi-controller#parameters) .

      The recommended way to customize these parameters is to use the [inventory](https://docs.saltbox.dev/saltbox/inventory/) :
      You should edit `/srv/git/saltbox/inventories/host_vars/localhost.yml` and add the following section:

      ```
      ### Open Specified Ports for the specified container ###
      ##### Unifi Ports for aditional services #####
      unifi_docker_ports_custom:
        - "3478:3478/udp" #Unifi STUN port
        - "10001:10001/udp" #Required for AP discovery
        - "8080:8080/tcp" #Required for device communication
        - "1900:1900/udp" #Required for Make controller discoverable on L2 network option
        - "8843:8843/tcp" #Unifi guest portal HTTPS redirect port
        - "8880:8880/tcp" #Unifi guest portal HTTP redirect port
        - "6789:6789/tcp" #For mobile throughput test
        - "5514:5514/udp" #Remote syslog port
      ```
