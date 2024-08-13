#!/bin/bash

echo "Running model..."

source base/bin/activate
cd $HOME/Documents/edgeAI/

#python3 train.py -e 3 datasets/roadsigns/config.yaml
yolo export model=runs/detect/train/weights/best.pt format=ncnn
python3 app.py runs/detect/train/weights/best.pt mittel_1.mp4

echo "Model run complete!#python3 train.py -e 3 datasets/roadsigns/config.yaml"