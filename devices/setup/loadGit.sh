#!/bin/bash

echo "Installing git"
sudo apt-get update
sudo apt-get install git

# Set the Git repository URL
repo_url="https://github.com/Programmierpraktikum-MVA/edgeAI.git"
# Set the destination directory
dest_dir1="$HOME/Documents/edgeAI"
dest_dir2="$HOME/Documents/yolo-weights"

# Check if the destination directory already exists
if [ -d "$dest_dir1" ]; then
    echo "Directory '$dest_dir1' already exists. Skipping clone."
    cd "$dest_dir1"
    git pull
    cd $HOME
else
    # Create the destination directory
    mkdir -p "$dest_dir1"

    # Clone the Git repository
    echo "Cloning repository to '$dest_dir1'..."
    git clone "$repo_url" "$dest_dir1"

    if [ $? -eq 0 ]; then
        echo "Repository cloned successfully."
    else
        echo "Failed to clone the repository."
    fi
fi

if [ -d "$dest_dir2" ]; then
    echo "Directory '$dest_dir2' already exists. Skipping clone."
    cd "$dest_dir2"
    git pull
    cd $HOME
else
    # Create the destination directory
    mkdir -p "$dest_dir2"
    echo "Cloning repository to '$dest_dir2'..."
    git clone --depth 1 https://github.com/squarra/yolo-weights.git "$dest_dir2"
    if [ $? -eq 0 ]; then
        echo "Repository cloned successfully."
    else
        echo "Failed to clone the repository."
    fi
fi


cp -r $dest_dir2/yolov8/best_ncnn_model/ $dest_dir1/yolov8/
cp $dest_dir2/short.mp4 $dest_dir1/yolov8/
#exit 0
