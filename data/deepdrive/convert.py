import json
import os
from tqdm import tqdm

class_dict = {
    "pedestrian": 0,
    "rider": 1,
    "car": 2,
    "truck": 3,
    "bus": 4,
    "train": 5,
    "motorcycle": 6,
    "bicycle": 7,
    "traffic light": 8,
    "traffic sign": 9,
}

image_width = 1280
image_height = 720


def process_dataset(label_type):
    json_file = f"annotations/det_20/det_{label_type}.json"
    output_path = f"labels/{label_type}"

    with open(json_file) as f:
        data = json.load(f)
    print(f"Converting {len(data)} {label_type} labels to YOLO format in {output_path}")

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for item in tqdm(data):
        filename = os.path.splitext(item["name"])[0] + ".txt"
        output_file = os.path.join(output_path, filename)

        if "labels" not in item:
            continue

        with open(output_file, "w") as f:
            for obj in item["labels"]:
                category = obj["category"]
                if category not in class_dict:
                    continue

                box2d = obj["box2d"]
                x1 = box2d["x1"] / image_width
                y1 = box2d["y1"] / image_height
                x2 = box2d["x2"] / image_width
                y2 = box2d["y2"] / image_height

                class_id = class_dict[category]
                x_center = (x1 + x2) / 2
                y_center = (y1 + y2) / 2
                width = x2 - x1
                height = y2 - y1

                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


if __name__ == "__main__":
    process_dataset("train")
    process_dataset("val")
