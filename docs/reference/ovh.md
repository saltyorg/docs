---
hide:
  - tags
tags:
  - OVH
  - hardware transcoding
---

# Enabling hardware transcoding on OVH

The required system-level changes are performed automatically on Hetzner machines; OVH requires some manual effort.

1. Make sure it actually has one of the motherboards that can use the iGPU (that isn't the case always)
2. manually tweak the nomodeset in grub.

## Verify motherboard capabilities

Verification method TBD

Symptom: display shows as `UNCLAIMED`:
```
sudo lshw -c video
  *-display UNCLAIMED
       description: Display controller
       product: HD Graphics 630
       vendor: Intel Corporation
       physical id: 2
       bus info: pci@0000:00:02.0
       version: 04
       width: 64 bits
       clock: 33MHz
       capabilities: pciexpress msi pm bus_master cap_list
       configuration: latency=0
       resources: memory:a1000000-a1ffffff memory:90000000-9fffffff ioport:5000(size=64)
  *-display UNCLAIMED
       description: VGA compatible controller
       product: MGA G200e [Pilot] ServerEngines (SEP1)
       vendor: Matrox Electronics Systems Ltd.
       physical id: 0
       bus info: pci@0000:04:00.0
       version: 05
       width: 32 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list
       configuration: latency=0
       resources: memory:a0000000-a0ffffff memory:a2800000-a2803fff memory:a2000000-a27fffff memory:a2810000-a281ffff
  *-graphics
       product: EFI VGA
       physical id: 2
       logical name: /dev/fb0
       capabilities: fb
       configuration: depth=32 resolution=1024,768
```

```
lsmod | grep i915
i915                 3104768  0
ttm                    86016  1 i915
drm_kms_helper        311296  1 i915
cec                    61440  2 drm_kms_helper,i915
drm                   622592  3 drm_kms_helper,i915,ttm
i2c_algo_bit           16384  2 igb,i915
video                  65536  1 i915
```

## tweak the nomodeset in grub

OVH's default grub config looks like this:
```
> cat /etc/default/grub

# This file is based on /usr/share/grub/default/grub, some settings
# have been changed by OVHcloud.
# If you change this file, run 'update-grub' afterwards to update
# /boot/grub/grub.cfg.
# For full documentation of the options in this file, see:
#   info -f grub -n 'Simple configuration'

GRUB_DEFAULT=0
GRUB_TIMEOUT_STYLE=hidden
GRUB_TIMEOUT=0
GRUB_DISTRIBUTOR=lsb_release -i -s 2> /dev/null || echo Debian
GRUB_CMDLINE_LINUX_DEFAULT=""
GRUB_CMDLINE_LINUX="nomodeset iommu=pt console=tty0 console=ttyS0,115200n8"

# Uncomment to enable BadRAM filtering, modify to suit your needs
# This works with Linux (no patch required) and with any kernel that obtains
# the memory map information from GRUB (GNU Mach, kernel of FreeBSD ...)
#GRUB_BADRAM="0x01234567,0xfefefefe,0x89abcdef,0xefefefef"

# Uncomment to disable graphical terminal (grub-pc only)
#GRUB_TERMINAL=console

# The resolution used on graphical terminal
# note that you can use only modes which your graphic card supports via VBE
# you can see them in real GRUB with the command `vbeinfo'
#GRUB_GFXMODE=640x480

# Uncomment if you don't want GRUB to pass "root=UUID=xxx" parameter to Linux
#GRUB_DISABLE_LINUX_UUID=true

# Uncomment to disable generation of recovery mode menu entries
#GRUB_DISABLE_RECOVERY="true"

# Uncomment to get a beep at grub start
#GRUB_INIT_TUNE="480 440 1"
```

Change this line:

```
GRUB_CMDLINE_LINUX="nomodeset iommu=pt console=tty0 console=ttyS0,115200n8"
```

to:

```
GRUB_CMDLINE_LINUX=""
```

Save the file and run:

```
sudo update-grub
```

then reboot:

```
sudo reboot
```

After doing this, the display controller should no longer appear as `UNCLAIMED`:

```
$ sudo lshw -c video
  *-display
       description: Display controller
       product: HD Graphics 630
       vendor: Intel Corporation
       physical id: 2
       bus info: pci@0000:00:02.0
       version: 04
       width: 64 bits
       clock: 33MHz
       capabilities: pciexpress msi pm bus_master cap_list
       configuration: driver=i915 latency=0
       resources: irq:158 memory:a1000000-a1ffffff memory:90000000-9fffffff ioport:5000(size=64)
  *-display
       description: VGA compatible controller
       product: MGA G200e [Pilot] ServerEngines (SEP1)
       vendor: Matrox Electronics Systems Ltd.
       physical id: 0
       bus info: pci@0000:04:00.0
       logical name: /dev/fb0
       version: 05
       width: 32 bits
       clock: 33MHz
       capabilities: pm pciexpress msi vga_controller bus_master cap_list rom fb
       configuration: depth=32 driver=mgag200 latency=0 resolution=1024,768
       resources: irq:17 memory:a0000000-a0ffffff memory:a2800000-a2803fff memory:a2000000-a27fffff memory:a2810000-a281ffff
```

And once you rerun the plex tag with intel enabled, HW transcoding should be available.
