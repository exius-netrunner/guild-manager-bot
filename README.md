**Upload Steps:**

1. Upload the files to the /home/guild-manager folder on ubuntu live server
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