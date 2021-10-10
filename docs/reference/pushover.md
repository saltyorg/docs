## What is Pushover?

[Pushover](https://pushover.net/faq) is service that enables you to receive instant push notifications on your phone/tablet/PC from a variety of sources. With Cloudbox, you can have notifications sent with many different events.

Screenshots:

 - Mobile device (Pushover app):

   ![](https://i.imgur.com/lTdXcNU.png)



 - PC (Pullover client):

   ![](https://i.imgur.com/2A12nIe.png)






## Pushover Setup

Listed below are the things you'll need from Pushover's site.

1. [Pushover](https://pushover.net/login) account

1. Pushover license(s)

    - Pushover has 3 separate licenses for the different device types: Android, iOS, or PC. The cost for the license is a one-time fee of $4.99. You'll need one for the type of device you want to receive notifications on.  See their [FAQ](https://pushover.net/faq#overview-fees) for more info.

1. A [Pushover Device Client](https://pushover.net/clients)

    - [Android](https://pushover.net/clients/android)

    - [iOS](https://pushover.net/clients/ios)

    - Desktop PC:

        - [Pullover](https://github.com/cgrossde/Pullover) (free, open source, multi platform client, and my personal favorite).

        - Browser Desktop Notifications (i.e. Chrome, Firefox, Safari).

1. Your User Key

    - Once you're signed in, click the Pushover logo at the top left to take you there.

1. Application API Token (one per app)

    - Pushover -> Your Applications -> [Create an Application/API Token](https://pushover.net/apps/build)

    - Fill in:

        - Name (app/task name)

        - Type (Application or Script)

        - Description (optional)

        - URL (optional)

        - Icon (optional)

    - Click "Create Application".


## Cloudbox Backup

To have Pushover send you alerts every time a Cloudbox backup task starts and finishes, follow to steps below.

1. Create a Pushover application for "Cloudbox Backup" (see Step 5 [[here](#pushover-setup).

   _Tip: If you have a Mediabox/Feederbox setup, you can create 2 different applications within Pushover specify "Mediabox Backup" and "Feederbox Backup" as their names._
 

2. Open the `accounts.yml` file.

   - For encrypted `accounts.yml`:

     ```bash
     ansible-vault edit accounts.yml
     ```

   - For plain text `accounts.yml`:

     ```bash
     nano accounts.yml
     ```


3. Type in your Pushover User Key and the Application Token (from Step #1) under "pushover" (without quotes).

   ```yaml
   pushover:
     app_token:
     user_key:
     priority
   ```

4. <kbd class="platform-all">Ctrl+X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd> to save.


## Cloudplow

Cloudplow can send notifications when it:

- starts an upload task.
- is put into a ban sleep.
- is restored after a ban sleep.
- completes an upload task.


![](https://i.imgur.com/LeIt8BC.png)


To setup notifications, follow the steps below:

1. Create a Pushover application for "Cloudplow" (see Step 5 [here](#pushover-setup).

2. Edit the Cloudplow config.json file:

    ```
    nano /opt/cloudplow/config.json
    ```

3. Add the following notification section and type in your Pushover User Key and the Application Token (from Step #1) within the quotes (""). Take a look at an example of this [here](../reference/cloudplow.md#cloudplow-with-notifications-enabled).

   ```json
   "notifications": {
       "Pushover": {
           "app_token": "XXXXXXXXXXX",
           "service": "pushover",
           "user_token": "XXXXXXXXXXXX",
           "priority": 0
        }
    },
   ```

4. <kbd class="platform-all">Ctrl+X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd> to save.

5. Restart CP after changes: `sudo systemctl restart cloudplow`.


## Overseerr

TODO: Write this

## Tautulli

Pushover can send you notifications whenever an event occurs with Plex (e.g. someone starts watching something,  new media is added, etc)

1. Create a Pushover application for "Tautulli" (see Step 5 [here](#pushover-setup).

2. Enable notifications: [[Tautulli|Install: Tautulli#1-accessing-plexpy]] -> Settings -> Notification Agents -> Click the gray "bell" icon next to "Pushover" -> and select when you want to be alerted -> Click "close". The "bell" icon will turn yellow. 

3. Add in your Pushover info: Click the "gear" icon next to "Pushover" -> Type in your Pushover User Key and the Application Token (you can click the "Test Notification" to check if it's working ok) -> Click "Save".



## Sonarr and Radarr

You can also have Sonarr and Radarr also send out alerts via Pushover when new media is added.