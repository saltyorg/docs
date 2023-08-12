# Creating an encrypted rclone remote

This article describes how to create an encrypted rclone remote

## Prerequisites

To go through this process, you will need the following:

   1. rclone installed on your saltbox machine [which means the preinstall has been run]
   2. the backing rclone remote pointing to your cloud storage must be created and working

When I say "backing remote" here I am referring to the rclone remote that points directly at your cloud storage, like [`google`](rclone-remote.md) or [`dropbox`](rclone-remote-dropbox.md) or whatever.  This article uses `dropbox`, but that should be considered a placeholder for the name of *your* cloud-storage rclone remote.

## Walkthrough

First, create a directory on the backing remote at which to point the crypt remote.  This is especially important for Dropbox, where paths starting with a `/` have special meaning.

1. Create the `encrypt` directory on the backing remote:

    === "I want to use my personal folder"

        ```shell
        rclone mkdir dropbox:encrypt

        ```

    === "I want to use a team folder"

        ```shell
        rclone mkdir dropbox:/encrypt

        ```

    **MAKE NOTE OF THIS; YOU WILL NEED IT LATER**

1. Verify that the directory is there, if you wish:

    ```
    rclone lsd dropbox:
    ```

    Display should look something like this:
    ```
          -1 2023-05-22 17:07:58        -1 encrypt
    ```

Now move on to creating the actual crypt remote.

1. Run the following command:

    ```
    rclone config
    ```

2. Type `n` for "New remote" and press <kbd class="platform-all">Enter</kbd>.

3. For "name", type in the name of your backing remote with `-crypt` appended, like `dropbox-crypt` and and press <kbd class="platform-all">Enter</kbd>. [This name is arbitrary, of course, but since you're going through a saltbox tutorial saltbox opinions should be expected here.]

    ```
    Enter name for new remote.
    name> dropbox-crypt
    ```

4. For "Type of storage", type in `crypt`, or the corresponding number, and press <kbd class="platform-all">Enter</kbd>.  Note that this list is constantly changing, will be much longer, and the numbers won't match what's shown here.  **Read what's on the screen.**

    ```
    Option Storage.
    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value.
    1 / 1Fichier
      \ "fichier"
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
    ```

5. For "Option remote", type in the name of your backing remote plus `:encrypt` and press <kbd class="platform-all">Enter</kbd>.

    === "I am using my personal folder"

        ```shell
        Option remote.
        Remote to encrypt/decrypt.
        Normally should contain a ':' and a path, e.g. "myremote:path/to/dir",
        "myremote:bucket" or maybe "myremote:" (not recommended).
        Enter a value.
        remote> dropbox:encrypt
        ```

    === "I want to use a team folder"

        ```shell
        Option remote.
        Remote to encrypt/decrypt.
        Normally should contain a ':' and a path, e.g. "myremote:path/to/dir",
        "myremote:bucket" or maybe "myremote:" (not recommended).
        Enter a value.
        remote> dropbox:/encrypt
        ```

    This is the directory on the cloud storage that will contain the encrypted data.

    **NOTE: THIS IS THE DIRECTORY ON THE BACKING REMOTE YOU CREATED A MOMENT AGO**

7. Press <kbd class="platform-all">Enter</kbd> to select the defaults for the next two settings:

    ```
    Option filename_encryption.
    How to encrypt the filenames.
    Choose a number from below, or type in your own string value.
    Press Enter for the default (standard).
    / Encrypt the filenames.
    1 | See the docs for the details.
    \ (standard)
    2 / Very simple filename obfuscation.
    \ (obfuscate)
    / Don't encrypt the file names.
    3 | Adds a ".bin" extension only.
    \ (off)
    filename_encryption>

    Option directory_name_encryption.
    Option to either encrypt directory names or leave them intact.
    NB If filename_encryption is "off" then this option will do nothing.
    Choose a number from below, or type in your own boolean value (true or false).
    Press Enter for the default (true).
    1 / Encrypt directory names.
    \ (true)
    2 / Don't encrypt directory names, leave them intact.
    \ (false)
    directory_name_encryption>
    ```

8. You're now going to choose two passwords; you can make them up yourself or let rclone generate them for you.  Here we are going to let rclone choose them, but follow the prompts as suits your requirements.

    ```
    Option password.
    Password or pass phrase for encryption.
    Choose an alternative below.
    y) Yes, type in my own password
    g) Generate random password
    y/g> g
    Password strength in bits.
    64 is just about memorable
    128 is secure
    1024 is the maximum
    Bits> 128
    Your password is: GsgEchLQllKRKmi-6BuA6w
    Use this password? Please note that an obscured version of this
    password (and not the password itself) will be stored under your
    configuration file, so keep this generated password in a safe place.
    y) Yes (default)
    n) No
    y/n> y

    Option password2.
    Password or pass phrase for salt.
    Optional but recommended.
    Should be different to the previous password.
    Choose an alternative below. Press Enter for the default (n).
    y) Yes, type in my own password
    g) Generate random password
    n) No, leave this optional password blank (default)
    y/g/n> g
    Password strength in bits.
    64 is just about memorable
    128 is secure
    1024 is the maximum
    Bits> 128
    Your password is: NsGyJb78XwW1OJwtcakHNw
    Use this password? Please note that an obscured version of this
    password (and not the password itself) will be stored under your
    configuration file, so keep this generated password in a safe place.
    y) Yes (default)
    n) No
    y/n> y
    ```
    *Make a note of those two passwords in a safe place*; this is the only time they wil be displayed.

9. Answer `y` and press <kbd class="platform-all">Enter</kbd> to enter advanced config:

    ```
    Edit advanced config?
    y) Yes
    n) No (default)
    y/n> y
    ```

10. Press <kbd class="platform-all">Enter</kbd> to accept the defaults on the first two options:

    ```
    Option server_side_across_configs.
    Allow server-side operations (e.g. copy) to work across different crypt configs.
    Normally this option is not what you want, but if you have two crypts
    pointing to the same backend you can use it.
    This can be used, for example, to change file name encryption type
    without re-uploading all the data. Just make two crypt backends
    pointing to two different directories with the single changed
    parameter and use rclone move to move the files between the crypt
    remotes.
    Enter a boolean value (true or false). Press Enter for the default (false).
    server_side_across_configs>

    Option no_data_encryption.
    Option to either encrypt file data or leave it unencrypted.
    Choose a number from below, or type in your own boolean value (true or false).
    Press Enter for the default (false).
    1 / Don't encrypt file data, leave it unencrypted.
    \ (true)
    2 / Encrypt file data.
    \ (false)
    no_data_encryption>
    ```

11. Answer `base32768` and press <kbd class="platform-all">Enter</kbd> when asked about filename encoding:

    ```
    Option filename_encoding.
    How to encode the encrypted filename to text string.
    This option could help with shortening the encrypted filename. The
    suitable option would depend on the way your remote count the filename
    length and if it's case sensitive.
    Choose a number from below, or type in your own string value.
    Press Enter for the default (base32).
    1 / Encode using base32. Suitable for all remote.
    \ (base32)
    2 / Encode using base64. Suitable for case sensitive remote.
    \ (base64)
    / Encode using base32768. Suitable if your remote counts UTF-16 or
    3 | Unicode codepoint instead of UTF-8 byte length. (Eg. Onedrive)
    \ (base32768)
    filename_encoding> base32768
    ```

12. answer `n` and press <kbd class="platform-all">Enter</kbd> *this* time when asked about advanced options:

    ```
    Edit advanced config?
    y) Yes
    n) No (default)
    y/n>
    ```

13. Review the remote configuration then answer `y` and press <kbd class="platform-all">Enter</kbd> if it looks like you expect:

    ```
    Configuration complete.
    Options:
    - type: crypt
    - remote: dropbox:encrypt
    - password: *** ENCRYPTED ***
    - password2: *** ENCRYPTED ***
    - filename_encoding: base32768
    Keep this "dropbox-crypt" remote?
    y) Yes this is OK (default)
    e) Edit this remote
    d) Delete this remote
    y/e/d> y
    ```

14. To exit, type `q` and press <kbd class="platform-all">Enter</kbd>.

    ```
    Current remotes:

    Name                 Type
    ====                 ====
    dropbox              dropbox
    dropbox-crypt        crypt

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q
    ```


15. repeat steps 2-15 with any other remotes you wish to apply encryption to.  

    **IMPORTANT**: If you are creating multiple remotes to access the same files [like one for upload and one for mount], use the same passwords with all of them.

The name of this remote [`dropbox-crypt` in this case] is what you should enter in the saltbox rclone settings as you proceed with the install.
