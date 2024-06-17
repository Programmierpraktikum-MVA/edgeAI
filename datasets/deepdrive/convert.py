import json
import os
from tqdm import tqdm

class_dict = {
    "car": "car",
    "pedestrian": "person",
    "rider": "rider",
    "truck": "truck",
    "bus": "bus",
    "train": "train",
    "motorcycle": "motorcycle",
    "bicycle": "bicycle",
    "traffic light": "trafficlight",
    "traffic sign": "trafficsign",
}

image_width = 1280
image_height = 720

with open("../classes.json") as f:
    classes = json.load(f)


def convert_to_yolo(data_type):
    with open(f"annotations/det_{data_type}.json") as f:
        data = json.load(f)

    os.makedirs(f"labels/{data_type}", exist_ok=True)

    for item in tqdm(data, desc=f"Generating labels for {data_type} annotations"):
        if "labels" not in item:
            continue

        
        txt_file = f"labels/{data_type}/{item['name'].replace('.jpg', '.txt')}"
        with open(txt_file, "w") as f:
            for obj in item["labels"]:
                category = obj["category"]
                if category not in class_dict:
                    continue

                box2d = obj["box2d"]
                x1 = box2d["x1"] / image_width
                y1 = box2d["y1"] / image_height
                x2 = box2d["x2"] / image_width
                y2 = box2d["y2"] / image_height

                class_name = class_dict[category]
                class_id = classes[class_name]
                x_center = (x1 + x2) / 2
                y_center = (y1 + y2) / 2
                width = x2 - x1
                height = y2 - y1

                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


if __name__ == "__main__":
    convert_to_yolo("train")
    convert_to_yolo("val")
