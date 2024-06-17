import json
import os
import shutil
import sys

class_dict = {
    0: "car",
    1: "person",
    2: "van",
    3: "rider",
    4: "truck",
    6: "tram",
    7: "personsitting",
}


def convert_to_yolo(file, dest_dir, classes):
    with open(f"annotations/{file}", "r") as f:
        lines = f.readlines()

    with open(f"labels/{dest_dir}/{file}", "w") as f:
        for line in lines:
            parts = line.split()
            kitti_id = int(parts[0])
            if kitti_id not in class_dict:
                continue

            class_name = class_dict.get(kitti_id)
            class_id = classes[class_name]
            f.write(f"{class_id} " + " ".join(parts[1:]) + "\n")


def main(classes, train_ratio=0.8):
    images = os.listdir("images")
    split_index = int(len(images) * train_ratio)

    train_images = images[:split_index]
    val_images = images[split_index:]

    os.makedirs("images/train", exist_ok=True)
    os.makedirs("images/val", exist_ok=True)
    os.makedirs("labels/train", exist_ok=True)
    os.makedirs("labels/val", exist_ok=True)

    for image in train_images:
        shutil.move(f"images/{image}", f"images/train/{image}")
        convert_to_yolo(image.replace(".png", ".txt"), "train", classes)

    for image in val_images:
        shutil.move(f"images/{image}", f"images/val/{image}")
        convert_to_yolo(image.replace(".png", ".txt"), "val", classes)


if __name__ == "__main__":
    json_file = sys.argv[1] if sys.argv[1] else "../unified1.json"
    with open(json_file) as f:
        classes = json.load(f)
    main(classes)
