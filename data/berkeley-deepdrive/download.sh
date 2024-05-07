#!/bin/bash

set -euo pipefail

base_url="https://dl.cv.ethz.ch/bdd100k/data/"
temp_dir="tmp"

download_data() {
    local type=$1
    local dataset=$2
    local zip_file zip_dir output_dir

    if [ "$type" == "dataset" ]; then
        zip_dir="bdd100k/images/100k/$dataset/"
        zip_file="100k_images_$dataset.zip"
        output_dir="../images/"
    elif [ "$type" == "labels" ]; then
        zip_dir="bdd100k/labels/$dataset"
        zip_file="bdd100k_${dataset}_labels_trainval.zip"
        output_dir="../annotations/"
    else
        echo "Invalid type specified."
        return 1
    fi

    if [ -d "$output_dir/$dataset" ] && [ "$(ls -A "$output_dir/$dataset")" ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') INFO: $output_dir$dataset is not empty. Assuming $type already exists and skipping download."
        return 0
    fi

    echo "$(date '+%Y-%m-%d %H:%M:%S') INFO: Starting download for $zip_file"
    if wget -c -q --show-progress --timeout=20 --tries=3 "$base_url$zip_file"; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') INFO: Unzipping $zip_file"
        if unzip -q "$zip_file"; then
            mkdir -p "$output_dir"
            mv "$zip_dir" "$output_dir"
            echo "$(date '+%Y-%m-%d %H:%M:%S') INFO: Successfully downloaded and extracted $zip_file"
        else
            echo "$(date '+%Y-%m-%d %H:%M:%S') ERROR: Failed to unzip $zip_file."
            return 1
        fi
    else
        echo "$(date '+%Y-%m-%d %H:%M:%S') ERROR: Failed to download $type."
        return 1
    fi
}

for cmd in wget unzip; do
    command -v "$cmd" >/dev/null 2>&1 || { echo >&2 "$cmd is required but not installed. Aborting."; exit 1; }
done

mkdir -p "$temp_dir"
cd "$temp_dir"

download_data "dataset" "train"
download_data "dataset" "val"
download_data "dataset" "test"
download_data "labels" "det_20"

echo "$(date '+%Y-%m-%d %H:%M:%S') INFO: Cleaning up temporary ressources."
cd ..
rm -rf "$temp_dir"
