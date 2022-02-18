## Installing Saltbox on a home server

Prerequisites:

 - Domain

 - Static IP OR Dynamic DNS configured

 - Router supports port forwarding

 - ISP supports you running servers on ports 80 and 443.  Some ISPs don’t allow or actively block this.

 - Router supports hairpin NAT [or NAT loopback]
   Saltbox assumes that you are accessing apps via subdomains like “radarr.mydomain.com” rather than ip and port like 192.168.1.25:7878.
   Without “hairpin NAT”, a request to “radarr.mydomain.com” from inside the network will not find its way to the proxy which does that routing.

NOTE: None of this initial setup is Saltbox-specific. If you want to run a server on a machine behind your router and connect to it using a domain name, whether Saltbox sets it up or something else, you’ll need to do these very same things.

### Domain:

You need a domain.  They’re cheap or even free.

You can find cheap ones here:  https://tld-list.com/
There are a variety of places that provide free domains.  Here’s one offered with no endorsement [It was the first google result for “free domain”]: https://www.freenom.com/en/freeandpaiddomains.html

Configure the DNS at your registrar to point your domain at your home external IP address.

You can find that using something like: https://whatismyipaddress.com/

You will need to configure “dynamic DNS” to make sure that domain keeps pointing to your home IP, which is subject to change, most likely.

Probably your router has this available.  If not, there’s a Dynamic DNS Client role available in saltbox you can install.  If you use Cloudflare for DNS, the ddns client configuration will be automatically done when you run the role.

The saltbox role is ddclient, and you run it like any other saltbox role:

```
sb install ddclient
```

You’ll do this AFTER you’ve installed saltbox.

### Machine:

I installed Ubuntu server 20.04 on the machine, accepting all defaults except:
I enabled OpenSSH and imported my SSH keys from github
That’s all.

Since I installed Ubuntu on my own hardware, the first user I created is a member of the sudoers group.  I’ll be running the install as that user from the start rather than starting as root like you would on a remote server.

## Router:

You need some ports forwarded to that machine on your router.  Explaining how to do that for any arbitrary router is out of scope, but I’ll show you where it is on my Netgear.

A remote server like one at Hetzner is just exposed to the open internet, so when you connect to that server on port 123, you’re connecting directly to that specific machine.  Your home network doesn’t work like that.  Your ISP gives you a single IP address, and your router translates all traffic in and out of your network to make sure it gets to the correct place.  Thas means that when a connection from the outside comes in, it is connecting to the router, not any individual machine.  You need to set up port forwarding so that when you try to connect to Radarr, for example, your router knows to send this request to the machine where you’ve installed Radarr.

There are two parts to what you need to do:
GIve your server an unchanging local IP address
Forward requests from the outside on relevant ports to that IP address.

The first is required because typically your router will be able to configure port forwarding to an IP address, so you don’t want the IP of your server changing.  Typically, on your router, everything gets an IP assigned automagically by the router’s DHCP server, so the IP address of a specific thing might change.  Depending on how your network is set up, it may be unlikely, but it’s a possibility nonetheless, so we’re going to make sure it doesn’t happen by telling the router “Always give this machine the IP address 1.2.3.4”.

On my Netgear, they call this “Address Reservation” and it’s found under “LAN Setup”:


I scroll to the end of that list, click “Add”, then choose a device and type in the address I want that thing to have.

The server I’m installing Saltbox on is “oberon”, and I’ve assigned it 192.168.1.5.





Next, port forwarding:


You can see here that I’ve set it such that outside requests to port 80, 443, 2205, and 3468 get forwarded on to the IP we just assigned to the saltbox server.
Depending on the applications you end up installing, you may need to forward other ports.  That example covers the reverse proxy, ssh, and Plex-Autoscan.

If your ISP does not allow you to do this, STOP NOW.  You won’t be able to run saltbox at home.

At this point, you should be able to SSH to that machine using your domain.

ssh YOU@YOUR_DOMAIN -p 2207

That should work just like:


ssh YOU@192.168.X.Y

If it doesn’t, verify all the port-forwarding details.

You should also be able to connect to a web server running on that machine.

Verify this part is working by installing apache on your server:
sudo apt install apache2

Then open a web browser and go to your domain [http://yourdomain.tld] . Maybe use your phone with wifi off to make sure the request is coming from outside your house.

If you see the default apache page, you’re set to go.



Once verified, remove apache:
sudo apt remove apache2

With that done, we can move on to the install.


IF THAT DOESN’T WORK, DON’T CONTINUE UNTIL IT DOES.  Verify your port forwarding setup and try again.  Verify that your ISP allows this.

From this point on there is nothing special about the install process on this home server as opposed to a remote server.  I’m just following the wiki.

I ran the first (“Combined”) dependency/repo script on this page:
https://github.com/Saltbox/Saltbox/wiki/Install%3A-Dependencies-%28Master-Branch%29

That ran for a while, and ended here:


In my accounts.yml, I’m entering an existing account on the ubuntu machine:

---
user:
  name: chaz
  pass: REDACTED
  domain: domain.tld
  email: chaz@chazlarson.com
plex:
  user: REDACTED
  pass: REDACTED
cloudflare:
  email: REDACTED
  api: REDACTED
pushover:
  app_token:
  user_key:
  priority:
apprise:

I entered my cloudflare credentials because DNS for the domain I’m using is set up there, so the saltbox install is going to create the subdomains for me.

I made no changes to settings.yml.



Run the preinstall:
sudo ansible-playbook saltbox.yml --tags preinstall

In my case there were no kernel updates required, so the preinstall didn’t reboot:


I am already logged in as the user I specified in accounts.yml, so I didn’t have to log out of the root account and log back in as chaz.  If you specified a new account that the preinstall created, you need to log out and log in as that account.

I then set up rclone remote as usual.

Next, I ran saltbox setup:


sudo ansible-playbook saltbox.yml --tags saltbox

In my case the setup ran through without problems the first time:


PLAY RECAP ************************************************************************************
localhost              	: ok=713  changed=180  unreachable=0	failed=0

Tuesday 14 April 2020  11:31:47 -0500 (0:00:00.040)   	0:13:22.200 *********
===============================================================================
docker : Start docker service -----------------------------------------------------...- 121.63s
docker : Wait for 30 seconds before commencing ------------------------------------...- 30.65s
iperf3 : Build and install iperf3 -------------------------------------------------...- 17.04s
system : APT | APT upgrade --------------------------------------------------------...- 16.82s
plex : Extra | Stop Plex Container ------------------------------------------------...- 11.39s
plex : Create and start container -------------------------------------------------...- 11.30s
remote : Rclone VFS | Start 'rclone_vfs.service' ----------------------------------...- 11.03s
rutorrent : Settings | Wait for 10 seconds before stopping rutorrent container ----...- 10.43s
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


Now I did one last log out and back in so I could access the docker command.

At this point, everything is running and I’m ready to go through the application setup.

