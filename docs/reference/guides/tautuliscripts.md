# Introduction

This is a quick guide to installing and configuring a Tautulli custom script. It will teach you how to download and configure a Tautulli custom script that drops Plex video streams transcoding from a 4K source.

## Install the script

Access your Saltbox server as your normal non-root user.

We'll be installing the [Killstream.py script](https://github.com/blacktwin/JBOPS/tree/master/killstream) from the [JBOPS](https://github.com/blacktwin/JBOPS) script collection.

### Download the script using curl

```shell
cd /opt/scripts/tautulli/
curl -O https://raw.githubusercontent.com/blacktwin/JBOPS/master/killstream/kill_stream.py
chmod a+x kill_stream.py
```

### Verify that the script was downloaded successfully with

```shell
ls -la kill_stream.py
```

## Configure Tautulli Notification Agent

Enter Tautulli settings and find the **Notification Agents** link on the left side menu.\
Click **Add a new notification agent** and scroll down to **Script** in the selection dialog.

### Configuration panel

Enter `/scripts/tautulli/` in the script folder and exit the text input field.

Select the script named `./kill_stream.py` in the Script File drop-down.\
_Check your previous steps or bug someone on discord if the script is not listed._

Enter `Terminate 4K transcodes` or something of your own choice in the description field.

#### Triggers panel

Put a checkmark in `Playback Start` and `Transcode Decision Change`

#### Notifications Conditions panel

Condition {1}: `Video Decision` - `is` - `transcode`

Condition {2}: `Library Name` - `contains` - `4K`

Note: adjust the library name if your 4K libraries does not contain the name **4K**.

#### Arguments panel

Under Playback Start enter the following:

```text
--jbop stream --username {username} --sessionId {session_id} --killMessage 'Transcoding is not allowed from the 4K libraries.'
```

Under Transcode Decision Change enter the following:

```text
--jbop stream --username {username} --sessionId {session_id} --killMessage 'Transcoding is not allowed from the 4K libraries.'
```

### Finishing up

Click the **Save** button to save the new notification agent.

You can test the agent by attempting to play a 4K movie through the Plex web app and downgrade the quality to 2Mbit. It will be transcoding for about 5-10 seconds, after which you should get the stream kill message.

There is a list of when a notification agent is triggered in the **Notification logs** section of Tautulli logs.

### Credit goes to blacktwin

* [https://github.com/blacktwin/JBOPS](https://github.com/blacktwin/JBOPS)
