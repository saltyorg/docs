# Creating an rclone remote for Dropbox

This article describes how to create an rclone remote for Dropbox

## Prerequisites

To go through this process, you will need the following:

   1. App Key/App Secret from two applications you create at Dropbox. The process is described [here](https://rclone.org/dropbox/#get-your-own-dropbox-app-id).  You want two because you will probably want separate remotes for mount and upload.

You will need rclone and a web browser installed on a machine local to you [this machine needs a GUI].

## Walkthrough

1. Run the following command:

    ```shell
    rclone config
    ```

2. Type `n` for "New remote" and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    $ rclone config
    2022/02/26 15:29:40 NOTICE: Config file "/Users/geezer/.config/rclone/rclone.conf" not found - using defaults
    No remotes found - make a new one
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    ```

3. For "name", type in the name of your choice and and press <kbd class="platform-all">Enter</kbd>. [This name is arbitrary, aside from rclone's limitations on name; we're using `dropbox` in this example]

    ```shell
    n/s/q> n
    name> dropbox
    ```

4. For "Type of storage", type in `dropbox`, or the corresponding number, and press <kbd class="platform-all">Enter</kbd>.  Note that this list is constantly changing, will be much longer, and the numbers won't match what's shown here.  **Read what's on the screen.**

    ```shell
    Option Storage.
    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value.
    1 / 1Fichier
      \ "fichier"
    2 / Alias for an existing remote
      \ "alias"
     ...
    12 / Compress a remote
       \ (compress)
    13 / Dropbox
       \ (dropbox)
    14 / Encrypt/Decrypt a remote
       \ (crypt)
     ...
    48 / Zoho
       \ (zoho)
    49 / premiumize.me
       \ (premiumizeme)
    50 / seafile
       \ (seafile)
    Storage> dropbox
    ```

5. App Key and App Secret:

    Enter the App Key and App Secret from one of your applications when prompted.

    ```shell
    Storage> dropbox
    Option client_id.
    OAuth Client Id.
    Leave blank normally.
    Enter a value. Press Enter to leave empty.
    client_id> JOHNNYJOEYDEEDEE
    Option client_secret.
    OAuth Client Secret.
    Leave blank normally.
    Enter a value. Press Enter to leave empty.
    client_secret> OZZYTONYGEEZERBILL
    ```

6. For "Edit advanced config", type `n` and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Edit advanced config?
    y) Yes
    n) No (default)
    y/n> n
    ```

7. For "Use auto config?", type `n` for "...remote or headless machine" and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine

    y) Yes (default)
    n) No
    y/n> n
    ```

8. In the next section, follow the instructions on your local machine.

    ```shell
    Option config_token.
    For this to work, you will need rclone available on a machine that has
    a web browser available.
    For more help and alternate methods see: https://rclone.org/remote_setup/
    Execute the following on the machine with the web browser (same rclone
    version recommended):
     rclone authorize "dropbox" "eyJjbGllbnRfaWQiOiI2OTUx...cGUiOiJkcml2ZSJ9"
    Then paste the result.
    Enter a value.
    config_token>
    ```

9. If asked to login, use the Dropbox account you want to store your data in.

    [](../../images/rclone-remote/dropbox-login.png)

10. Give access by clicking "Allow".

    [](../../images/rclone-remote/dropbox-permission.png)

11. The browser should report success.

12. And a token should show up in the terminal on your local computer:

    ```text
    2023/05/19 16:59:57 NOTICE: Waiting for code...
    2023/05/19 18:07:33 NOTICE: Got code
    Paste the following into your remote machine --->
    ROGERPETEJOHNKEITH
    <---End paste
    ```

13. Paste the token at the rclone prompt and press Enter.

    ```text
    Enter a value.
    config_token>  ROGERPETEJOHNKEITH
    ```

14. Confirm that the remote details look OK, type `y` and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Configuration complete.
    Options:
    - type: dropbox
    - client_id: JOHNNYJOEYDEEDEE
    - client_secret: OZZYTONYGEEZERBILL
    - token: {"access_token":"sl.Beujz-1fB...PTCTBbPOGhTs","token_type":"bearer","refresh_token":"Fu9...EYpRr","expiry":"2023-05-19T22:07:34.356998-05:00"}
    Keep this "dropbox" remote?
    y) Yes this is OK (default)
    e) Edit this remote
    d) Delete this remote
    y/e/d> y
    ```

15. repeat steps 1-14 with your second App ID/App Secret, if you have one.  Give this one an appropriate name like `dropbox-upload`.  Letters are free, don't be stingy with them.

16. If you plan to use encryption, set up two more remotes, again for the mount and uploading.  If you don't plan to use encryption, skip to step XX.

17. Type `n` for "New remote" and press <kbd class="platform-all">Enter</kbd>.

18. For "name", type in the name of your first dropbox remote with `-crypt` appended, like `dropbox-crypt` and and press <kbd class="platform-all">Enter</kbd>. [This name is arbitrary, of course, but since you're going through a saltbox tutorial saltbox opinions should be expected.]

    ```shell
    Enter name for new remote.
    name> dropbox-crypt
    ```

19. For "Type of storage", type in `crypt`, or the corresponding number, and press <kbd class="platform-all">Enter</kbd>.
    
    ```shell
    Option Storage.
    Type of storage to configure.
    Choose a number from below, or type in your own value.
     1 / 1Fichier
       \ (fichier)
    ...
    13 / Dropbox
       \ (dropbox)
    14 / Encrypt/Decrypt a remote
       \ (crypt)
    15 / Enterprise File Fabric
       \ (filefabric)
    ...
    50 / seafile
       \ (seafile)
    Storage> crypt

20. For "Option remote", type in the name of your dropbox remote plus `:encrypt` and press <kbd class="platform-all">Enter</kbd>.
    
    ```shell
    Option remote.
    Remote to encrypt/decrypt.
    Normally should contain a ':' and a path, e.g. "myremote:path/to/dir",
    "myremote:bucket" or maybe "myremote:" (not recommended).
    Enter a value.
    remote> dropbox:encrypt
    ```

21. repeat steps 17-20 with your `dropbox-upload` remote, if you have one.

22. To exit, type `q` and press <kbd class="platform-all">Enter</kbd>.

    ```shell
    Current remotes:

    Name                 Type
    ====                 ====
    dropbox              dropbox
    dropbox-upload       dropbox
    dropbox-crypt        crypt
    dropbox-upload-crypt crypt

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q
    ```
