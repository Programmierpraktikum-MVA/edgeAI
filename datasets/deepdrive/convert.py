import json
import os
from tqdm import tqdm

class_dict = {
    "car": 0,
    "pedestrian": 1,
    "rider": 3,
    "truck": 4,
    "bus": 6,
    "train": 7,
    "motorcycle": 8,
    "bicycle": 9,
    "traffic light": 10,
    "traffic sign": 11,
}

image_width = 1280
image_height = 720


def convert(split):
    output_path = f"labels/{split}"

    with open(f"annotations/det_{split}.json") as f:
        data = json.load(f)

    os.makedirs(output_path, exist_ok=True)

    for item in tqdm(data, desc=f"Generating labels for {split} annotations"):
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
    convert("train")
    convert("val")
