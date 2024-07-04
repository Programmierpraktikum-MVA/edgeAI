import argparse
import json
import os
import shutil

# you might change this
PATH_TO_JSON = '/annotations/det_20/det_train.json'
IMAGE_DIR = '/deepdrive/images/'
LABEL_DIR = '/deepdrive/labels/'
OUTPUT_DIR = 'datasets/subset1/'


# weather = ["clear", "overcast", "snowy", "rainy", "foggy", "partly_cloudy", "undefined"]
# scene = ["residential", "highway", "city street", "parking lot", "gas stations", "tunnel"]
# tod = ["dawn/dusk", "daytime", "night"]

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data


def filter_dataset(data, weather, scene, time_of_day):
    # convert underscore to space ; e.g. partly_cloudy -> partly cloudy
    if (weather is not None):
        weather = [x.replace("_", " ")  for x in weather]
    if (scene is not None):
        scene = [x.replace("_", " ")  for x in scene]
    if (time_of_day is not None):
        time_of_day = [x.replace("_", " ")  for x in time_of_day]
    
    filtered_data = []
    # add images that meet input criteria
    for item in data:
        if  (not weather or item['attributes']['weather'] in weather) and \
            (not scene or item['attributes']['scene'] in scene) and \
            (not time_of_day or item['attributes']['timeofday'] in time_of_day):
            filtered_data.append(item)
    return filtered_data


def create_new_dirs(json_name):
    # Create base directories images and labels
    basedir_img = os.path.join(OUTPUT_DIR, 'images')
    os.makedirs(basedir_img, exist_ok=True)
    basedir_labels = os.path.join(OUTPUT_DIR, 'labels')
    os.makedirs(basedir_labels, exist_ok=True)

    # create /images/val or /images/train based on json
    subdir = ''
    if (os.path.basename(json_name) == 'det_train.json'):
        subdir = 'train'
    elif (os.path.basename(json_name) == 'det_val.json'):
        subdir = 'val'
    img_path = os.path.join(basedir_img, subdir)
    labels_path = os.path.join(basedir_labels, subdir)
    os.makedirs(img_path, exist_ok=True)
    os.makedirs(labels_path, exist_ok=True)

    return img_path, labels_path, subdir


def copy_files(filtered_data, img_path, label_path, subdir):
    for item in filtered_data:
        filename = item['name']
        txt_name = filename.replace('jpg', 'txt')
        # original paths
        og_img_path = os.path.join(IMAGE_DIR, subdir, item['name'])
        og_label_path = os.path.join(LABEL_DIR, subdir, txt_name)

        # destination paths
        output_img_path = os.path.join(img_path, item['name'])
        output_label_path = os.path.join(label_path, txt_name)

        # copy files
        shutil.copy(og_img_path, output_img_path)
        shutil.copy(og_label_path, output_label_path)
    

def main():
    parser = argparse.ArgumentParser(description="Create Subset of Deepdrive based on (multiple) tags")
    parser.add_argument('-w', '--weather', nargs='+', help="Weather conditions to filter by (e.g.: clear foggy party_cloudy)")
    parser.add_argument('-s', '--scene', nargs='+', help="Scenes to filter by (e.g.: residential highway)")
    parser.add_argument('-t', '--time_of_day', nargs='+', help="Time of day to filter by (e.g.: daytime)")

    args = parser.parse_args()

    if (os.path.basename(PATH_TO_JSON) != "det_val.json" and os.path.basename(PATH_TO_JSON) != "det_train.json"):
        print("invalid json")
        return
    
    data = load_json(PATH_TO_JSON)

    filtered_data = filter_dataset(data, args.weather, args.scene, args.time_of_day)

    img_path, labels_path, subdir = create_new_dirs(PATH_TO_JSON)
    
    copy_files(filtered_data, img_path, labels_path, subdir)
    return
    

if __name__ == "__main__":
    main()