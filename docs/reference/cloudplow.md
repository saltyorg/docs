# Example Cloudplow configs

## Cloudplow with Default Config

This is the default config; it contains a single remote/uploader pair.  This set uploads everything from `/mnt/local/Media` to `google:/Media` once there is 200GB in `/mnt/local/Media`.

<details>
<summary>Example config.json (click to expand)</summary><br />

```json
{
    "core": {
        "dry_run": false,
 "rclone_config_path": "/home/seed/.config/rclone/rclone.conf"
    },
    "hidden": {},
    "notifications": {
    },
    "remotes": {
        "google": {
            "hidden_remote": "google:",
            "rclone_excludes": [
                "**partial~",
                "**_HIDDEN~",
                ".unionfs/**",
                ".unionfs-fuse/**"
            ],
            "rclone_extras": {
                "--checkers": 16,
                "--drive-chunk-size": "64M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1
            },
            "rclone_sleeps": {
                "Failed to copy: googleapi: Error 403: User rate limit exceeded": {
                    "count": 5,
                    "sleep": 25,
                    "timeout": 3600
                }
            },
            "remove_empty_dir_depth": 2,
            "sync_remote": "google:/Media",
            "upload_folder": "/mnt/local/Media",
            "upload_remote": "google:/Media"
        }
    },
    "syncer": {
    },
    "uploader": {
        "google": {
            "check_interval": 30,
            "exclude_open_files": true,
            "max_size_gb": 200,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": [
                "downloads/*"
            ]
        }
    }
}
```

</details>

## Cloudplow with Multiple Remotes

A couple points:

- Uploader tasks run sequentially (vs in parallel)
- Each `uploader` task needs a separate `remote`. You can't have two “uploaders” referencing one “remote”.

<details>
<summary>Example config.json (click to expand)</summary><br />

```json
{
    "core": {
        "dry_run": false,
        "rclone_binary_path": "/usr/bin/rclone",
        "rclone_config_path": "/home/seed/.config/rclone/rclone.conf"
    },
    "hidden": {},
    "notifications": {
        "Pushover": {
            "app_token": "xxxxx",
            "priority": 0,
            "service": "pushover",
            "user_token": "xxxxx"
        }
    },
    "nzbget": {
        "enabled": false,
        "url": "https://user:password@nzbget.domain.com"
    },
    "plex": {
        "enabled": false,
        "max_streams_before_throttle": 1,
        "poll_interval": 30,
        "rclone": {
            "throttle_speeds": {
                "1": "50M",
                "2": "40M",
                "3": "30M",
                "4": "20M",
                "5": "10M"
            },
            "url": "http://localhost:7949"
        },
        "token": "xxxxxx",
        "url": "https://plex.domain.com",
        "verbose_notifications": false
    },
    "remotes": {
        "google": {
            "hidden_remote": "google:",
            "rclone_excludes": [
                "**partial~",
                "**_HIDDEN~",
                ".unionfs/**",
                ".unionfs-fuse/**"
            ],
            "rclone_extras": {
                "--checkers": 8,
                "--drive-chunk-size": "128M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1
            },
            "rclone_sleeps": {
                "Failed to copy: googleapi: Error 403: User rate limit exceeded": {
                    "count": 5,
                    "sleep": 6,
                    "timeout": 7200
                }
            },
            "rclone_command": "copy",
            "remove_empty_dir_depth": 1,
            "upload_folder": "/mnt/local/Media/",
            "upload_remote": "google:/Media/"
        },
        "dropbox": {
            "hidden_remote": "dropbox:",
            "rclone_excludes": [
                "**partial~",
                "**_HIDDEN~",
                ".unionfs/**",
                ".unionfs-fuse/**"
            ],
            "rclone_extras": {
                "--checkers": 8,
                "--dropbox-chunk-size": "128M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1
            },
            "rclone_sleeps": {
            },
            "rclone_command": "move",
            "remove_empty_dir_depth": 1,
            "upload_folder": "/mnt/local/Media/",
            "upload_remote": "dropbox:/Media/"
        }
    },
    "syncer": {},
    "uploader": {
        "google": {
            "check_interval": 30,
            "exclude_open_files": true,
            "max_size_gb": 100,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": [
                "downloads/*"
            ]
        },
        "dropbox": {
            "check_interval": 30,
            "exclude_open_files": true,
            "max_size_gb": 50,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": []
        }
    }
}
```

</details>

## Cloudplow with Multiple Folders

This config uploads everything from `/mnt/local/Media` to `google:/Media` [triggered at 100GB] and  everything in `/mnt/local/downloads/torrents/qbittorrent/completed/` to `google:/Downloads/` [triggered at 50GB].

<details>
<summary>Example config.json (click to expand)</summary><br />

```json
{
    "core": {
        "dry_run": false,
        "rclone_binary_path": "/usr/bin/rclone",
        "rclone_config_path": "/home/seed/.config/rclone/rclone.conf"
    },
    "hidden": {},
    "notifications": {
        "Pushover": {
            "app_token": "xxxxx",
            "priority": 0,
            "service": "pushover",
            "user_token": "xxxxx"
        }
    },
    "nzbget": {
        "enabled": false,
        "url": "https://user:password@nzbget.domain.com"
    },
    "plex": {
        "enabled": false,
        "max_streams_before_throttle": 1,
        "poll_interval": 30,
        "rclone": {
            "throttle_speeds": {
                "1": "50M",
                "2": "40M",
                "3": "30M",
                "4": "20M",
                "5": "10M"
            },
            "url": "http://localhost:7949"
        },
        "token": "xxxxxx",
        "url": "https://plex.domain.com",
        "verbose_notifications": false
    },
    "remotes": {
        "media_to_google": {
            "hidden_remote": "google:",
            "rclone_excludes": [
                "**partial~",
                "**_HIDDEN~",
                ".unionfs/**",
                ".unionfs-fuse/**"
            ],
            "rclone_extras": {
                "--checkers": 8,
                "--drive-chunk-size": "128M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1
            },
            "rclone_sleeps": {
                "Failed to copy: googleapi: Error 403: User rate limit exceeded": {
                    "count": 5,
                    "sleep": 6,
                    "timeout": 7200
                }
            },
            "remove_empty_dir_depth": 1,
            "upload_folder": "/mnt/local/Media/",
            "upload_remote": "google:/Media/"
        },
        "downloads_to_google": {
            "hidden_remote": "",
            "rclone_excludes": [
                "**partial~",
                "**_HIDDEN~",
                ".unionfs/**",
                ".unionfs-fuse/**"
            ],
            "rclone_extras": {
                "--checkers": 8,
                "--drive-chunk-size": "128M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1
            },
            "rclone_sleeps": {
                "Failed to copy: googleapi: Error 403: User rate limit exceeded": {
                    "count": 5,
                    "sleep": 25,
                    "timeout": 7200
                }
            },
            "remove_empty_dir_depth": 1,
            "upload_folder": "/mnt/local/downloads/torrents/qbittorrent/completed/",
            "upload_remote": "google:/Downloads/"
        }
    },
    "syncer": {},
    "uploader": {
        "media_to_google": {
            "check_interval": 30,
            "exclude_open_files": true,
            "max_size_gb": 100,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": [
                "downloads/*"
            ]
        },
        "downloads_to_google": {
            "check_interval": 30,
            "exclude_open_files": true,
            "max_size_gb": 50,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": []
        }
    }
}
```

</details>

## Cloudplow with Notifications Enabled

This is the default config with Pushover notifications configured.

<details>
<summary>Example config.json (click to expand)</summary><br />

```json
{
    "core": {
        "dry_run": false,
 "rclone_config_path": "/home/seed/.config/rclone/rclone.conf"
    },
    "hidden": {},
    "notifications": {
        "Pushover": {
            "app_token": "XXXXXXXXXXX",
            "service": "pushover",
            "user_token": "XXXXXXXXXXXX",
            "priority": 0
        }
    },
    "remotes": {
        "google": {
            "hidden_remote": "google:",
            "rclone_excludes": [
                "**partial~",
                "**_HIDDEN~",
                ".unionfs/**",
                ".unionfs-fuse/**"
            ],
            "rclone_extras": {
                "--checkers": 16,
                "--drive-chunk-size": "64M",
                "--stats": "60s",
                "--transfers": 8,
                "--verbose": 1
            },
            "rclone_sleeps": {
                "Failed to copy: googleapi: Error 403: User rate limit exceeded": {
                    "count": 5,
                    "sleep": 25,
                    "timeout": 3600
                }
            },
            "remove_empty_dir_depth": 2,
            "sync_remote": "google:/Media",
            "upload_folder": "/mnt/local/Media",
            "upload_remote": "google:/Media"
        }
    },
    "syncer": {
    },
    "uploader": {
        "google": {
            "check_interval": 30,
            "exclude_open_files": true,
            "max_size_gb": 200,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": [
                "downloads/*"
            ]
        }
    }
}
```

</details>
