import os
import xml.etree.ElementTree as ET

def convert_annotations(set_type):
    annotations_dir = os.path.join("annotations", set_type)
    labels_dir = os.path.join("labels", set_type)

    if not os.path.exists(labels_dir):
        os.makedirs(labels_dir)

    class_dict = {
        "trafficlight": 0,
        "stop": 1,
        "speedlimit": 2,
        "crosswalk": 3
    }

    for xml_file in os.listdir(annotations_dir):
        tree = ET.parse(os.path.join(annotations_dir, xml_file))
        root = tree.getroot()

        width = int(root.find(".//width").text)
        height = int(root.find(".//height").text)

        with open(os.path.join(labels_dir, xml_file.replace(".xml", ".txt")), "w") as txt_file:
            for obj in root.findall(".//object"):
                class_name = obj.find(".//name").text
                class_id = class_dict[class_name]
                xmin = int(obj.find(".//xmin").text)
                ymin = int(obj.find(".//ymin").text)
                xmax = int(obj.find(".//xmax").text)
                ymax = int(obj.find(".//ymax").text)

                x_center = (xmin + xmax) / (2 * width)
                y_center = (ymin + ymax) / (2 * height)
                box_width = (xmax - xmin) / width
                box_height = (ymax - ymin) / height

                txt_file.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")

if __name__ == "__main__":
    convert_annotations("train")
    convert_annotations("val")
