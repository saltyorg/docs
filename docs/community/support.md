---
status: draft
---

# Support

Saltbox support is provided exclusively via our [Discord server](https://discord.gg/ugfKXpFND8).

## Where to Post

-   For officially supported Saltbox topics, create a thread in [#support-saltbox](https://discord.com/channels/853755447970758686/1020063740936335451).
-   For topics not directly related to Saltbox, create a thread in [#support-non-saltbox](https://discord.com/channels/853755447970758686/1108457911530819654).

    Hardware and home networking considerations typically go here. Specific software issues are more likely to be resolved through their official support platforms and outside Saltbox.

-   Please avoid posting support requests in other channels.

## Sharing Information

!!! warning "Do not share sensitive information!"
       
    Carefully review any output for personal information (domain names, public IP addresses, credentials...) and sanitize it before sharing.

Always provide detailed context and relevant logs. This can include but is not limited to:

-   Your hosting specifics:

    -   Location: on-site (home?) or off-site (Hetzner? OVH?)
    -   Environment: bare-metal or VM (Proxmox? Unraid?)
    -   Media storage: direct-attached (internal drive? USB?) or remote (Rclone? CIFS?)

-   What you have tried: `sb update`, `sb install ...`, `docker restart ...`, etc.
-   Saltbox logs in `/srv/git/Saltbox/`, Traefik logs in `/opt/traefik`
-   Output of `sb docker ps`, `sb docker logs`, `docker inspect ...`, `sb logs`
-   Your [Inventory](../saltbox/inventory/index.md) content, output of `sb diag`
-   Output of `curl http://traefik:8080/api/http/routers/xROLE_NAMEx@docker` with the problem app
-   Output of `dig`, `curl`, `ping` with the problem FQDN
-   Output of `lsblk`, `lspci`, `free -h`, `df -h`, `sudo lshw`, `uname -a`, `history | tail -100`

Please do not cherry-pick snippets that you believe are more relevant than others. We require the complete picture.

**Note:** If your text exceeds the Discord character limit, use [PrivateBin][1] or attach a text file.

[1]: https://privatebin.net "Please set the expiration to the longest duration available, and do not check *Burn after reading*."

## Best Practices

-   **Check Announcements:** Always review [#announcements](https://discord.com/channels/853755447970758686/905480112949051402) for recent developments. Broad issues requiring user intervention are usually covered there.
-   **Threads:** Always create a dedicated thread for your support request to keep discussions organized.
-   **Beware the [XY problem](https://xyproblem.info)**: Present the core problem and mention everything you tried to overcome it, but leave out the self-diagnosis.
-   **No Screenshots of Text:** Please do not use screenshots for terminal output—copy and paste the text instead, inside a [code fence](#code-fences) if appropriate.
-   **Error Screens:** For issues like HTTP errors (404, 500, SSL certificate...), please avoid posting a screenshot of your web browser. Instead, paste the output of a command-line HTTP client such as `curl` with the problem URL. Screenshots in general are not welcome in support requests.

## Code Fences

When sharing a command, log, or error message, use a code fence to escape native Discord formatting.

-   **Syntax:** The backtick is used for code fences.

    ![Backtick Key](../images/support/qwerty-backtick.svg)

-   **Single-line:** For short inline content, wrap with a single backtick ++grave++: `` `your inline content` ``
-   **Multi-line:** For longer content, wrap with triple backticks ++grave+grave+grave++:

    ````markdown
    ```
    your
    multi-line
    content
    ```
    ````

-   **Language:** For syntax highlighting, add a language identifier by the opening triple backticks.

    ````markdown title="YAML example"
    ```yaml
    your: ["syntax-highlighted", "content"]
    ```
    ````
