import os
import sys
import xml.etree.ElementTree as ET

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, "..", ".."))

from utils.dataset_utils import split_data

anno_dir = os.path.join(current_dir, "annotations")
imgs_dir = os.path.join(current_dir, "images")
lbls_dir = os.path.join(current_dir, "labels")

class_dict = {
    "trafficlight": 10,
    "stop": 11,
    "speedlimit": 11,
    "crosswalk": 11,
}


def convert():
    split_data(imgs_dir)
    split_data(anno_dir)

    for split in ["train", "val"]:
        src_dir = os.path.join(anno_dir, split)
        dst_dir = os.path.join(lbls_dir, split)
        os.makedirs(dst_dir, exist_ok=True)

        for file in os.listdir(src_dir):
            tree = ET.parse(os.path.join(src_dir, file))
            root = tree.getroot()

            size = root.find("size")
            img_width = int(size.find("width").text)
            img_height = int(size.find("height").text)

            with open(os.path.join(dst_dir, file.replace("xml", "txt")), "w") as f:
                for obj in root.findall("object"):
                    roadsigns_label = obj.find("name").text
                    class_id = class_dict[roadsigns_label]

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
    convert()
