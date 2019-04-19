#!/bin/bash

# Add repositories
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo add-apt-repository ppa:dawidd0811/neofetch
sudo add-apt-repository ppa:otto-kesselgulasch/gimp

sudo apt update && sudo apt upgrade -y


# Install Apps
sudo apt install linux-headers-$(uname -r) build-essential dkms
sudo apt install ubuntu-restricted-extras
sudo apt install software-properties-common apt-transport-https wget code neofetch gufw synaptic gimp darktable


# Update Config Files

cp .bashrc .bashrc_bak
echo 'neofetch' >> .bashrc




# TEMP Install Visio Studio Code

# TEMP Install Neofetch

# TEMP Install GUFW

# TEMP Install Synaptic

# TEMP Install pre VM Tools

# TEMP Install  ubuntu restricted

# TEMP Install gimp

# TEMP Install Darktable






