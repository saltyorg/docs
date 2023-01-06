## Saltbox vs. Cloudbox

Saltbox started out as a branch in Cloudbox while salty was maintaining Cloudbox for about a year and a half so there is a massive carryover from the develop branch of Cloudbox.

The main reason it became its own project was due to Cloudbox project owners not feeling comfortable handing over the reins despite them more or less having become disinterested in maintaining their project.

There isn't a maintained list of differences as the improvements have happened slowly over time as people request features or functionality changes which have been added when it made sense.

In terms of functionality the high points are

- Validated Ubuntu 20.04 and 22.04 support (Saltbox will try to support newer releases quicker than Cloudbox has) which is useful in terms of hardware acceleration support with newer CPUs.
- Support for IPv6 within the docker container network using NAT since we still want to keep things behind the reverse proxy.
- Inventory system for simpler, upgrade-protected customization
- Authelia single sign-on
- Choice of SSL provider [Let's Encrypt or ZeroSSL]
- ability to use a subdomain rather than a TLD (`rolename.subdomain.domain.tld` rather than `rolename.domain.tld`)
- Generalized support for multiple app instances [replacement for the "ArrX" system]
- Ongoing maintenance and active development
- largely automated system to set up shared drives and service accounts for the user [for Cloudbox users, this is the "tip 44" setup].
