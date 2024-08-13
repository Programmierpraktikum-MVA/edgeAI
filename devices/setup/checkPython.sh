#!/bin/bash

# Check Python 3 installation
python3 --version
if [ $? -eq 0 ]; then
    echo "Python 3 is installed and working."
else
    echo "Python 3 is not installed or not working."
    exit 1
fi

# Check if project.yaml file exists
if [ -f "project.yaml" ]; then
    echo "project.yaml file found."
else
    echo "project.yaml file not found."
    exit 1
fi

# Install required packages from project.yaml
echo "Installing required packages from project.yaml..."
pip3.12 install -r project.yaml
if [ $? -eq 0 ]; then
    echo "All required packages installed successfully."
else
    echo "Failed to install required packages."
    exit 1
fi

echo "All checks passed."
