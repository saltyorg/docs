# UniFi Network Controller

# **NOT INTEGRATED - MAKE SANDBOX REQUEST IF WANTED**

## What is it?

[UniFi Network Controller ](https://www.ui.com/){: target=_blank rel="noopener noreferrer" } is a wireless network management
software solution from Ubiquiti Networks™. It allows you to manage multiple wireless networks using a web browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://www.ui.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](http://documentation.ubnt.com/UniFi){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://hub.docker.com/r/linuxserver/unifi-controller){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/linuxserver/unifi-controller){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-unifi

```

### 2. URL

- To access UniFi Network Controller , visit `https://unifi._yourdomain.com_`

### 3. Setup

1. If you do not wish to use port `8080` then edit your desired UniFi informer port into the UniFi section in [community `settings.yml`:](../../community/settings.md) .

   ``` { .yaml }
    unifi:
      port: 8080
   ```

2. Run the installer role:

    ``` { .shell }

    sb install cm-unifi

    ```

3. Work out how to do the setup then come back here and write the rest of the instructions to help other users.

4. For now, I think...
      1. The webui is at `https://unifi._yourdomain.com_`, setup with the first run wizard.

      2. For Unifi to adopt other devices, e.g. an Access Point, it is required to change the inform IP address. Because Unifi runs inside Docker by default it uses an IP address not accessible by other devices. To change this go to `Settings > System Settings > Controller Configuration` and set the `Controller Hostname/IP` to a hostname or IP address accessible by your devices, probably https://unifi._yourdomain.com_. Additionally the checkbox `"Override inform host with controller hostname/IP"` has to be checked, so that devices can connect to the controller during adoption (devices use the inform-endpoint during adoption).

      3. In order to manually adopt a device take these steps:

        ```
          ssh ubnt@$AP-IP
          set-inform https://$address:8080/inform
        ```
          The default device password is `ubnt`. `$address` is the IP address of the host you are running this container on and `$AP-IP` is the Access Point IP address.


- [:octicons-link-16: Documentation](http://documentation.ubnt.com/UniFi){: .header-icons target=_blank rel="noopener noreferrer" }
