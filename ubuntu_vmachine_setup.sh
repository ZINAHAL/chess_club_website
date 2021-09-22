#!/bin/bash

# If there is a command failure, stop running future commands, and exit
set -e

# ssh root@ip_address
# Root
apt-get update && apt-get upgrade --noinput

# Setting a hostname for the virtual machine
hostnamectl set-hostname chessServer
# ***
# Open /etc/hosts file and add [vm_ip_address  hostname]


# Creating a new user
adduser zinahal 
# Allowing a user to run root commands by using sudo
adduser zinahal sudo


# ssh zinahal@ip_address
# zinahal

