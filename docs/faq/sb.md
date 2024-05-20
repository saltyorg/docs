---
hide:
  - tags
tags:
  - cloudflare
---

# sb

---

## My sb commands suddenly return the following output:
```
Relaunching with previous arguments.
/srv/git/sb/sb: 1: version: not found
/srv/git/sb/sb: 2: oid: not found
size: '6743896': No such file
```

Fix is to reinstall sb using the following command:
```shell
curl -sL https://raw.githubusercontent.com/saltyorg/sb/master/sb_reinstall.sh | sudo -H bash
```

This change was announced on [discord](https://discord.com/channels/853755447970758686/905480112949051402/1241994889667936339).
