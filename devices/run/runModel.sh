#!/bin/bash

# Usage: ./runModel.sh <device_name> [timeout] <video_folder>
# or
#   ssh user@ip 'bash -s' < runModel.sh <device_name> [timeout] <video_folder>
#   scp user@ip:~/Documents/edgeAI local_dest

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <device_name> [timeout] <video_folder>"
    exit 1
fi

DEVICE_NAME=$1
TIMEOUT=${2:-5m}
VIDEO_FOLDER=${3:-$2}

if [ ! -d "$VIDEO_FOLDER" ]; then
    echo "Error: Folder $VIDEO_FOLDER does not exist."
    exit 1
fi

echo "Running model on device $DEVICE_NAME with timeout $TIMEOUT..."
source base311/bin/activate
cd $HOME/Documents/edgeAI/

for VIDEO_FILE in "$VIDEO_FOLDER"/*.mp4; 
do
    VIDEO_BASENAME=$(basename "$VIDEO_FILE" .mp4)
    
    # Run the model
    timeout "$TIMEOUT" python3 app.py runs/detect/train/weights/best.pt "$VIDEO_FILE" > "${DEVICE_NAME}_bestPt_${VIDEO_BASENAME}.txt"
done

echo "Model run complete!"
