**Default Setup:**

By default, the setup script assumes you're using a root account, to update this make the following changes:

1. user=root [Change root to your user - Line 46]
2. HOME='/home/root' [Change root to your user - Line 47]
3. Save the file

**Upload Steps:**

1. From root account, upload the files to a folder called /home/guild-manager on ubuntu live server
2. Run chmod +x server-setup.sh
3. Run ./server-setup.sh

**Script Steps:**

1. Installs Python 3.12
2. Installs pip3 globally
3. Installs Supervisor [Process Manager]
4. Installs the bot requirements
5. Creates a Supervisor configuration script
6. Sets it and the bot to run at start up
7. Starts the bot
