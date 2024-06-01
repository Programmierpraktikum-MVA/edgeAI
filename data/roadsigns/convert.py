import os
import xml.etree.ElementTree as ET

class_dict = {
    "trafficlight": 12,
    "stop": 14,
    "speedlimit": 15,
    "crosswalk": 16,
}

image_width = 1280
image_height = 720


def convert_xml_to_yolo(cur_xml_file, img_width, img_height, filename):
    tree = ET.parse(cur_xml_file)
    root = tree.getroot()

    with open(filename, "w") as f:
        for obj in root.findall('object'):
            label = obj.find('name').text
            class_id = class_dict[label]

            box = obj.find('bndbox')
            x1 = int(box.find('xmin').text)
            y1 = int(box.find('ymin').text)
            x2 = int(box.find('xmax').text)
            y2 = int(box.find('ymax').text)

            x_center = ((x1 + x2) / 2) / img_width
            y_center = ((y1 + y2) / 2) / img_height
            width = (x2 - x1) / img_width
            height = (y2 - y1) / img_height

            f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


if __name__ == "__main__":
    xml_dir = 'annotations'

    output_dir = 'labels'
    os.makedirs(output_dir, exist_ok=True)

    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith('.xml'):
            # Construct the full file paths
            xml_path = os.path.join(xml_dir, xml_file)
            output_path = os.path.join(output_dir, os.path.splitext(xml_file)[0] + '.txt')

            # Convert the XML file to YOLO format
            convert_xml_to_yolo(xml_path, image_width, image_height, output_path)
