import json
import os
import shutil
import xml.etree.ElementTree as ET

class_dict = {
    "trafficlight": "trafficlight",
    "stop": "stop",
    "speedlimit": "speedlimit",
    "crosswalk": "crosswalk",
}

with open("../classes.json") as f:
    classes = json.load(f)


def main(train_ratio=0.8):
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
        convert_to_yolo(image.replace(".png", ".xml"), "train")

    for image in val_images:
        shutil.move(f"images/{image}", f"images/val/{image}")
        convert_to_yolo(image.replace(".png", ".xml"), "val")


def convert_to_yolo(xml_file, dest_dir):
    tree = ET.parse(f"annotations/{xml_file}")
    root = tree.getroot()

    size = root.find("size")
    img_width = int(size.find("width").text)
    img_height = int(size.find("height").text)

    txt_file = f"labels/{dest_dir}/{xml_file.replace('.xml', '.txt')}"

    with open(txt_file, "w") as f:
        for obj in root.findall("object"):
            label = obj.find("name").text
            class_name = class_dict[label]
            class_id = classes[class_name]

            box = obj.find("bndbox")
            x1 = int(box.find("xmin").text) / img_width
            y1 = int(box.find("ymin").text) / img_height
            x2 = int(box.find("xmax").text) / img_width
            y2 = int(box.find("ymax").text) / img_height

            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            box_width = x2 - x1
            box_height = y2 - y1

            f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")


if __name__ == "__main__":
    main()
