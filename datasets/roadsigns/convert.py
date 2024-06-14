import os
import shutil
import random
import xml.etree.ElementTree as ET

class_dict = {
    "trafficlight": 12,
    "stop": 14,
    "speedlimit": 15,
    "crosswalk": 16,
}


def main(train_ratio=0.8):
    images = sorted([f for f in os.listdir("images") if f.endswith(".png")])
    annotations = sorted([f for f in os.listdir("annotations") if f.endswith(".xml")])

    os.makedirs("images/train", exist_ok=True)
    os.makedirs("images/val", exist_ok=True)
    os.makedirs("labels/train", exist_ok=True)
    os.makedirs("labels/val", exist_ok=True)

    for image, annotation in zip(images, annotations):
        dest_dir = "train" if random.random() < train_ratio else "val"
        shutil.move(f"images/{image}", f"images/{dest_dir}/{image}")
        convert_xml_to_yolo(annotation, dest_dir)


def convert_xml_to_yolo(xml_file, dest_dir):
    tree = ET.parse(f"annotations/{xml_file}")
    root = tree.getroot()

    size = root.find("size")
    img_width = int(size.find("width").text)
    img_height = int(size.find("height").text)

    txt_file = f"labels/{dest_dir}/{xml_file.replace('.xml', '.txt')}"

    with open(txt_file, "w") as f:
        for obj in root.findall("object"):
            label = obj.find("name").text
            class_id = class_dict[label]

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
