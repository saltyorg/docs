Here are two ways of obtaining a Plex Access Token for your Plex account.

## Saltbox Role

You will need your Plex credentials filled in `~/saltbox/accounts.yml`. If you already do, skip steps 2-4.

1. Go to the Saltbox folder:

   ```bash
   cd ~/saltbox/
   ```

1. Open the file for editing:

   - For encrypted `accounts.yml`:

     ```bash
     ansible-vault edit accounts.yml
     ```

   - For plain text `accounts.yml`:

     ```bash
     nano accounts.yml
     ```

1. Fill in your Plex credentials:

   ```yml
   plex:
     user:
     pass:
   ```

1. Save and exit: <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd>.

1. Run the following command:

   ```
   sb install plex_auth_token
   ```

1. You will be shown your Plex Access Token in the log:

   ```
   TASK [plex_auth_token : Display Plex Auth Token] 
   ***********************************************************************************
   Tuesday 29 January 2019  21:08:33 +0100 (0:00:00.104)       0:00:13.905 *******
   ok: [localhost] => {
       "msg": "Your Plex Auth Token is: XXXXXXXXXXXXXXXX"
   }
   ```

## Script


1. On the server's shell, run the following command<a href="#note1" id="note1ref"><sup>[1]</sup></a>:

   ```bash
   /opt/scripts/plex/plex_token.sh
   ```
   
1. You will be prompted to enter your Plex login and then presented with the Plex Access Token (under `Your X_PLEX_TOKEN:`)


## 

---

<sub> <a id="note1" href="#note1ref"><sup>1</sup></a> Credit: https://github.com/wernight</sub><br>
