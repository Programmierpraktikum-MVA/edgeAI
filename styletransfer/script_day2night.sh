#!/bin/sh

PATH_TO_JSON_LABELFILE=/home/mika/edgeAI/data/deepdrive/annotations/det_20/det_val.json
PATH_TO_IMAGES_DIRECTORY=/home/mika/edgeAI/data/deepdrive/images/val
PATH_TO_OUTPUT_BBOX_DIRECTORY=./val-bboxes_day2night/

python3 ~/joliGEN/scripts/bdd100k_to_joligen.py\
    --json-label-file $PATH_TO_JSON_LABELFILE\
    --path-to-imgs $PATH_TO_IMAGES_DIRECTORY\
    --bbox-out-dir $PATH_TO_OUTPUT_BBOX_DIRECTORY\
    --time-of-day

mkdir -p day2night
mkdir -p day2night/trainA
mkdir -p day2night/trainB

mv bdd100k_daytime.txt day2night/trainA/paths.txt
mv bdd100k_night.txt day2night/trainB/paths.txt

mkdir -p other_segments
mv bdd100k_*.txt other_segments/