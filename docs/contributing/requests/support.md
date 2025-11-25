---
status: draft
---

# Support

Saltbox support is provided exclusively via our [Discord server](https://discord.gg/ugfKXpFND8).

## Where to Post

-   For officially supported Saltbox matters, create a thread in [:fontawesome-brands-discord: #support-saltbox](https://discord.com/channels/853755447970758686/1020063740936335451).
-   For topics not directly related to Saltbox, create a thread in [:fontawesome-brands-discord: #support-non-saltbox](https://discord.com/channels/853755447970758686/1108457911530819654).

    Hardware and home networking considerations typically go here. For specific software issues, you are more likely to receive efficient help by contacting the software's support team through their official platform (Discord, forums, GitHub, etc.)

-   Please avoid posting support requests in other channels.

## Sharing Information

Always provide detailed context and relevant logs. This can include but is not limited to:

!!! warning "Do not share sensitive information!"
       
    Carefully review any output for personal information (such as domain names, IPs, or credentials) and sanitize it before sharing.

-   Your hosting specifics:

    -   On-site (e.g., home) or off-site (specify provider: e.g., Hetzner)?
    -   Bare metal or VM (specify hypervisor: e.g., Proxmox)?
    -   Direct-attached (e.g., SATA, USB) or remote (e.g., rclone, cifs) storage?

-   What you have tried so far (`sb update`, `sb install ...`, `docker restart ...`, etc.)
-   Output of `sb diag`, `sb logs`, `sb docker ps`, `sb docker logs`, `docker inspect ...`
-   Your [Inventory](../../saltbox/inventory/index.md) content
-   Traefik logs in `/opt/traefik`
-   Output of `dig`, `curl`, `ping` with the problem FQDN
-   Output of `curl http://traefik:8080/api/http/routers/xROLE_NAMEx@docker` with the problem app
-   Output of `lsblk`, `lspci`, `free -h`, `df -h`, `sudo lshw`, `uname -a`

**Large Data:** If your text exceeds the Discord character limit, upload it to [PrivateBin](https://privatebin.net/) or attach a text file.

## Best Practices

-   **Check Announcements:** Always review [:fontawesome-brands-discord: #announcements](https://discord.com/channels/853755447970758686/905480112949051402) for recent troubleshooting steps and updates. Many transient issues requiring user intervention are addressed there.
-   **Threads:** Always create a dedicated thread for your support request to keep discussions organized.
-   **No Screenshots of Text:** Please do not use screenshots for terminal output—copy and paste the text instead, inside a code fence if necessary.
-   **Error Reporting:** For issues like HTTP errors (404, 500, SSL certificate...), pleaste avoid posting a screenshot of your web browser. Instead, paste the output of a command such as `curl` with the problem URL.

## Code Fences

When sharing commands, logs, or error messages, use code fences for clarity.

-   **Backtick Key:** The backtick ++grave++ is used for code fences.

    ![Backtick Key](https://www.computerhope.com/cdn/keyboard/tilde.jpg)

-   **Single-line:** For short inline content, wrap with a single backtick: `` `your inline content` ``
-   **Multi-line:** For longer content, wrap with triple backticks ++grave+grave+grave++:

    ````markdown
    ```
    your
    multi-line
    content
    ```
    ````

-   **Language Identifier:** For syntax highlighting, add a language identifier by the opening triple backticks.

    ````markdown title="YAML example"
    ```yaml
    your: ["syntax-highlighted", "content"]
    ```
    ````
