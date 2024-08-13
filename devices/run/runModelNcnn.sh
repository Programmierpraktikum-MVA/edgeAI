#!/bin/bash

echo "Running model..."

source base/bin/activate
cd $HOME/Documents/edgeAI/yolov8/

python3 app.py best_ncnn_model/ short.mp4

echo "Model run complete!"