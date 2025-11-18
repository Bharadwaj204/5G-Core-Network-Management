#!/bin/bash

# Open5GS Installation Script for Ubuntu
# This script installs Open5GS and its dependencies on Ubuntu 22.04

echo "Starting Open5GS installation..."

# Update package list
sudo apt update

# Install required packages
sudo apt install -y software-properties-common

# Add Open5GS repository
sudo add-apt-repository -y ppa:open5gs/latest

# Update package list again
sudo apt update

# Install Open5GS
sudo apt install -y open5gs

# Install MongoDB (required for Open5GS)
sudo apt install -y mongodb

echo "Open5GS installation completed!"