#!/bin/bash

echo "Running model..."
source base311/bin/activate
cd $HOME/Documents/edgeAI/yolov8/

# Iterate over each video in the videos directory
for video in videos/videos-self-recorded/*; do
    # Run the model on each video with a timeout of 5 minutes
    timeout 5m python3 app.py runs/detect/train/weights/best.pt "$video" > jetson_bestPt_"$video".txt
    
    # Check if the process completed successfully
    if [ $? -eq 124 ]; then
        echo "Processing of $video timed out."
    else
        echo "Processing of $video completed."
    fi
done

echo "Model run complete!"
