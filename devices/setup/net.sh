#!/bin/bash

SSID="longuspetrus"
PSK="12345678"
CONFIG_DIR="/etc/NetworkManager/system-connections"
NEW_UUID=$(uuidgen)
CONFIG_FILE="${CONFIG_DIR}/${SSID}.nmconnection"

# Check if the SSID already exists
SSID_EXISTS=$(grep -rl "ssid=${SSID}" ${CONFIG_DIR})

if [ -z "$SSID_EXISTS" ]; then
    # Create a new configuration file for the Wi-Fi network
    echo "[connection]
id=${SSID}
uuid=${NEW_UUID}
type=wifi
[wifi]
mode=infrastructure
ssid=${SSID}
hidden=false
[ipv4]
method=auto
[ipv6]
addr-gen-mode=default
method=auto
[proxy]
[wifi-security]
key-mgmt=wpa-psk
psk=${PSK}" | sudo tee "${CONFIG_FILE}"

    # Set appropriate permissions for the new configuration file
    sudo chmod 600 "${CONFIG_FILE}"

    # Restart the NetworkManager service
    sudo service NetworkManager restart

    echo "Wi-Fi network ${SSID} added and NetworkManager restarted."
else
    echo "Wi-Fi network ${SSID} already exists."
fi
