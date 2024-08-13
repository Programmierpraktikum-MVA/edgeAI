#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP_address> <password>"
    exit 1
fi

ip_address="$1"
password="$2"

ssh -o StrictHostKeyChecking=no user@"$ip_address" << EOF
echo "$password" | sudo -S ls
EOF
