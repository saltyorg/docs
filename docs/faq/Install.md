
# Install

IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## Ansible Tags

### Multiple Tags

Run multiple tags together by separating them with commas, no spaces. Quotes are optional. Order is not important.

Use this to install containers or roles that are not included in "default" install types.  

Example:

```shell
sb install core,emby,sonarr,radarr,nzbget,nzbhydra2
```

## Error while fetching server API version

Full error message:

```text
Error Connecting:  Error while fetching server API version: Timeout value connect was Timeout(connect=60, read=60, total=None), but it must be an int or float.
```

Run `sudo pip install requests==2.10.0` and retry.

## 403 Client Error: Forbidden: endpoint with name \<container name\> already exists in network \<network name\>

Example:

```text
fatal: [localhost]: FAILED! => {"changed": false, "failed": true, "msg": "Error starting container 6fb60d4cdabe938986042e06ef482012a1d85a66a099d861f08062d8262c2ef7: 403 Client Error: Forbidden (\"{\"message\":\"endpoint with name jackett already exists in network bridge\"}\")"}
    to retry, use: --limit @/home/seed/saltbox/saltbox.retry
PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=1
```

You have a remnant of the container in the Docker's network.

You can verify with the command below (replace `<network name>` and `<container name>` is replaced with the network name and container name mentioned in the error, respectively):

```shell
docker inspect network <network name> | grep <container name>
```

To remove the remnant, run this command and try again:

```shell
docker network disconnect -f <network name> <container name>
```

## 500 Server Error: Internal Server Error: driver failed programming external connectivity on endpoint \<container name\> bind for 0.0.0.0:\<port number\> failed: port is already allocated

```shell
sudo service docker stop
sudo service docker start
```

## Updating Saltbox

Follow the appropriate steps from [this page](../saltbox/basics/update.md)
