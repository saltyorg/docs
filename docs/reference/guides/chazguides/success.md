# Did my Saltbox install succeed?

If you started with the first install [step](../../../saltbox/install/install.md)

And went through the first five steps, completely and without seeing any errors, it should be.

Perhaps you skipped some of those 5 required steps.  If so, why?  Go back to the beginning and start again.

Perhaps you ignored some errors.  If so, why?  Go back to the beginning and start again.

The install is complete when you get to the end of [this step](../../../saltbox/install/install.md#install-saltbox) with no errors.

It’s not complete until then.

What does success look like?

After running the Saltbox install command:

```text
~$ sb install saltbox
```

A lot of logging information will scroll by.

Eventually, it will stop, and if successful, will display something like this:

TODO: REPLACE WITH SALTBOX VERSION

```text
PLAY RECAP ************************************************************************************
localhost               : ok=713  changed=180  unreachable=0 failed=0

Tuesday 14 April 2020  11:31:47 -0500 (0:00:00.040)    0:13:22.200 *********
===============================================================================
docker : Start docker service -----------------------------------------------------...- 121.63s
docker : Wait for 30 seconds before commencing ------------------------------------...- 30.65s
iperf3 : Build and install iperf3 -------------------------------------------------...- 17.04s
system : APT | APT upgrade --------------------------------------------------------...- 16.82s
plex : Extra | Stop Plex Container ------------------------------------------------...- 11.39s
plex : Create and start container -------------------------------------------------...- 11.30s
remote : Rclone VFS | Start 'rclone_vfs.service' ----------------------------------...- 11.03s
qbittorrent : Settings | Wait for 10 seconds before stopping qbittorrent container --...- 10.43s
ombi : Create and start container -------------------------------------------------...- 9.39s
docker : Stop docker service ------------------------------------------------------...- 8.48s
system : sysctl | Tuning ----------------------------------------------------------...- 7.49s
nodejs : Install nodejs -----------------------------------------------------------...- 7.37s
plexpy : Create and start container -----------------------------------------------...- 7.03s
jackett : Create and start container ----------------------------------------------...- 6.78s
nzbhydra2 : Create and start container --------------------------------------------...- 6.22s
nodejs : Update npm ---------------------------------------------------------------...- 6.12s
remote : Rclone VFS | "Wait for 5 seconds" ----------------------------------------...- 5.42s
sanity_check : Get all available TAGS ---------------------------------------------...- 5.08s
sonarr : Create and start container -----------------------------------------------...- 4.96s
lidarr : Create and start container -----------------------------------------------...- 4.88s
chaz@oberon:~/saltbox$

Note this part: it’s even color-coded:
PLAY RECAP ************************************************************************************
localhost               : ok=713  changed=180  unreachable=0 failed=0

No red there.

Emphasizing what you want to see:
ok=713   changed=180   unreachable=0   failed=0

Zero failures.

If you are not left at a prompt like this after running the saltbox install, chances are an error occurred during the install, and typically that error is shown at the end here.

If you come to the discord asking for help, this log will be the first thing we ask you for.

Once more for emphasis:
If you come to the discord asking for help, this log will be the first thing we ask you for.
What does an error look like?


For example, if I enter a bad domain in my accounts.yml:

---
user:
  name: REDACTED
  pass: REDACTED
  domain: bing.bang.boing
  email: REDACTED
...

It runs for a bit and stops here:

TASK [pre_tasks : Add Subdomain | Cloudflare: Add 'saltbox' subdomain to 'bing.bang.boing'] *********************************************************************************
Tuesday 14 April 2020  11:53:29 -0500 (0:00:00.142)    0:00:52.680 *********
fatal: [localhost]: FAILED! => {"changed": false, "msg": "No zone found with name bing.bang.boing"}

PLAY RECAP **********************************************************************
localhost               : ok=131  changed=3 unreachable=0 failed=1

Tuesday 14 April 2020  11:53:30 -0500 (0:00:00.779)    0:00:53.460 *********
===============================================================================
sanity_check : Get all available TAGS ---------------------------------------------------------------------------------...- 5.02s
Gathering Facts ---------------------------------------------------------------------------------...- 1.51s
...
TRIMMED FOR SPACE
...
settings : Copy | Check if 'ansible.cfg' exists ---------------------------------------------------------------------------------...- 0.35s
chaz@oberon:~/saltbox$

Lots of red there, showing exactly what went wrong.

Or, If I set the cloudflare email in the config to a bad value:

...
cloudflare:
  email: bing@bang.boing
  api: REDACTED
...


TASK [pre_tasks : Add Subdomain | Cloudflare: Add 'saltbox' subdomain to 'DOMAIN.TLD'] ********************************************************************************************
Tuesday 14 April 2020  11:56:54 -0500 (0:00:00.224)    0:00:52.892 *********
fatal: [localhost]: FAILED! => {"changed": false, "msg": "API request not authenticated; Status: 403; Method: GET: Call: /zones?name=DOMAIN.TLD; Error details: code: 9103, error: Unknown X-Auth-Key or X-Auth-Email; "}

PLAY RECAP *********************************************************************************
localhost               : ok=131  changed=2 unreachable=0 failed=1

Tuesday 14 April 2020  11:56:55 -0500 (0:00:00.686)    0:00:53.579 *********
===============================================================================
sanity_check : Get all available TAGS ---------------------------------------------------------------------------------...- 5.06s
Gathering Facts ---------------------------------------------------------------------------------...- 1.52s
...
TRIMMED FOR SPACE
...

settings : Start | Check to see if yyq is installed ---------------------------------------------------------------------------------...- 0.35s
chaz@oberon:~/saltbox$

Again, lots of red there, showing exactly what went wrong.

Typically, all errors will be displayed in that manner.

Maybe docker didn’t get installed, maybe your Plex credentials are bad, maybe some network issue prevented the install from grabbing a thing from github, etc.

Whatever it is will be displayed in that install log, and no one can say anything more than “I’m sorry it didn’t work” if this output is not provided.

If you come to the discord asking for help, this log will be the first thing we ask you for.

Once more for emphasis:
If you come to the discord asking for help, this log will be the first thing we ask you for.
What now?
Is DNS configured?
If you entered your cloudflare credentials into the settings, the install should have created subdomains at cloudflare for you.

You can verify this with the ping utility:

(nothing special about my choice of ombi here)

You should see something like:

chaz@oberon:~/saltbox$ ping ombi.YOURDOMAIN.TLD
PING ombi.YOURDOMAIN.TLD (111.222.333.444): 56 data bytes
64 bytes from 111.222.333.444: icmp_seq=0 ttl=48 time=114.425 ms

That IP address should be the IP address of the server.  If this is a home server, it should be your external IP.

If instead you should see something like:

chaz@oberon:~/saltbox$ ping ombi.YOURDOMAIN.TLD
ping: cannot resolve ombi.YOURDOMAIN.TLD: Unknown host

...then you need to fix your DNS setup.  Either enter valid Cloudflare credentials in the settings, OR, if you are not using Cloudflare, go set up the required subdomains manually at your DNS provider.
Are the containers running?
The install should leave you with all the docker containers  set up and running.

Verify this with docker ps

(The display here has been edited for readability and space)

chaz@oberon:~/saltbox$ docker ps
CONTAINER ID   IMAGE                                   CREATED          STATUS
99c552628534   hotio/lidarr                            27 minutes ago   Up 27 minutes
fae88a0e46d1   hotio/radarr                            27 minutes ago   Up 27 minutes
a5858358c3f8   hotio/sonarr:phantom                    27 minutes ago   Up 27 minutes
84e39d15fbdd   hotio/nzbhydra2                         27 minutes ago   Up 27 minutes
a579ca009eb2   hotio/jackett                           27 minutes ago   Up 27 minutes
a1d387692b30   hotio/nzbget                            28 minutes ago   Up 28 minutes
c4b5b3a73aeb   organizrtools/organizr-v2:plex          29 minutes ago   Up 29 minutes
974f5bc87364   portainer/portainer                     29 minutes ago   Up 29 minutes
7ac30109104c   hotio/ombi                              29 minutes ago   Up 29 minutes
0cb9c230f5f1   tautulli/tautulli:nightly               30 minutes ago   Up 30 minutes
bed4af6dc439   cloudb0x/plex:latest                    31 minutes ago   Up 30 minutes
18b10e11029a   jrcs/letsencrypt-nginx-proxy-companion  31 minutes ago   Up 31 minutes
51b214fdf273   jwilder/nginx-proxy                     31 minutes ago   Up 31 minutes
```

That’s the list of containers installed by the default setup at the time of writing.

There should be no way for the install to complete without errors, but leave no containers running.
Is the proxy running?

You can verify the proxy with curl:

(nothing special about my choice of ombi here)

```text
chaz@oberon:~/saltbox$ curl http://ombi.DOMAIN.TLD | head -n 20
  % Total % Received % Xferd  Average Speed   Time Time  Time  Current
                              Dload  Upload   Total   Spent Left  Speed
100   169  100   169 0  0  12071   0 --:--:-- --:--:-- --:--:-- 12071
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.17.6</center>
</body>
</html>
```

That’s expected, it’s the standard saltbox behavior where the non-secure URL forwards to the secure URL.

Tell curl to follow the redirect by adding -L:

You're ready to start the application setup in the wiki.
