#!/bin/sh

PATH_TO_JSON_LABELFILE=/home/mika/edgeAI/data/deepdrive/annotations/det_20/det_val.json
PATH_TO_IMAGES_DIRECTORY=/home/mika/edgeAI/data/deepdrive/images/val
PATH_TO_OUTPUT_BBOX_DIRECTORY=./val-bboxes_clear2snowy/

python3 ~/joliGEN/scripts/bdd100k_to_joligen.py\
    --json-label-file $PATH_TO_JSON_LABELFILE\
    --path-to-imgs $PATH_TO_IMAGES_DIRECTORY\
    --bbox-out-dir $PATH_TO_OUTPUT_BBOX_DIRECTORY\
    --weather

mkdir -p clear2snowy
mkdir -p clear2snowy/trainA
mkdir -p clear2snowy/trainB

mv bdd100k_clear.txt clear2snowy/trainA/paths.txt
mv bdd100k_snowy.txt clear2snowy/trainB/paths.txt

mkdir -p other_segments
mv bdd100k_*.txt other_segments/