#!/bin/bash

# Update package lists
sudo apt update

# Install required dependencies for adding new repositories
sudo apt install -y software-properties-common

# Add the repository for Python 3.12
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# Install Python 3.12
sudo apt install -y python3.12 python3.12-dev python3.12-venv

# Ensure pip3 is installed
echo "Checking if pip3 is installed..."
if ! command -v pip3 &>/dev/null; then
    echo "pip3 not found. Installing pip3 for Python 3.12..."
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.12 get-pip.py --break-system-packages
    rm get-pip.py
else
    echo "pip3 is already installed."
fi

# Install Supervisor
sudo apt install -y supervisor

# Install dependencies from requirements.txt
pip3 install -r requirements.txt --break-system-packages

# Output success message
echo "Installation complete and requirements are installed."

# Create the Supervisor configuration file for the bot
SUPERVISOR_CONF="/etc/supervisor/conf.d/bot.conf"

sudo bash -c "cat > $SUPERVISOR_CONF" <<EOF
[program:bot]
command=/usr/bin/python3 /home/guild-manager/bot.py
autostart=true
autorestart=true
stderr_logfile=/var/log/bot.err.log
stdout_logfile=/var/log/bot.out.log
user=root
environment=PATH='/usr/bin:/bin',HOME='/home/root'
EOF

# Reload Supervisor to apply the new configuration
sudo supervisorctl reread
sudo supervisorctl update

# Start the bot using Supervisor
sudo supervisorctl start bot

# Ensure Supervisor starts on boot
sudo systemctl enable supervisor

# Output success message
echo "Supervisor configuration for bot created at $SUPERVISOR_CONF and bot started."
