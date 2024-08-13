#!/bin/bash

echo "Updating Pi"

yes | sudo apt-get update
yes | sudo apt-get install nala
yes | sudo nala upgrade

echo "Update complete"