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

src_dir_img = 'images'
src_dir_anno = 'annotations'
dest_dir_train = 'train'
dest_dir_val = 'val'

def randomly_assign_files(train_ratio=0.8):
    image_files = [f for f in os.listdir(src_dir_img) if f.endswith('.png')]
    annotation_files = [f for f in os.listdir(src_dir_anno) if f.endswith('.xml')]
    image_files.sort()
    annotation_files.sort()
    os.makedirs(src_dir_img + '/' + dest_dir_train, exist_ok=True)
    os.makedirs(src_dir_img + '/' + dest_dir_val, exist_ok=True)
    os.makedirs(src_dir_anno + '/' + dest_dir_train, exist_ok=True)
    os.makedirs(src_dir_anno + '/' + dest_dir_val, exist_ok=True)

    for image_file, annotation_file in zip(image_files, annotation_files):
        rand_num = random.random()
        if rand_num < train_ratio:
            dest_dir = dest_dir_train
        else:
            dest_dir = dest_dir_val
        img_start_path = src_dir_img + '/' + image_file
        img_end_path = src_dir_img + '/' + dest_dir + '/' + image_file
        anno_start_path = src_dir_anno + '/' + annotation_file
        anno_end_path = src_dir_anno + '/' + dest_dir + '/' + annotation_file
        shutil.move(img_start_path, img_end_path)
        shutil.move(anno_start_path, anno_end_path)

        output_dir = 'labels' + '/' + dest_dir
        os.makedirs(output_dir, exist_ok=True)
        ano_file = anno_end_path
        filename = output_dir + '/' + os.path.splitext(os.path.basename(ano_file))[0] + '.txt'
        convert_xml_to_yolo(ano_file, filename)

def convert_xml_to_yolo(cur_xml_file, filename):
    tree = ET.parse(cur_xml_file)
    root = tree.getroot()

    size = root.find('size')
    img_width = int(size.find('width').text)
    img_height = int(size.find('height').text)

    with open(filename, "w") as f:
        for obj in root.findall('object'):
            label = obj.find('name').text
            class_id = class_dict[label]

            box = obj.find('bndbox')
            x1 = int(box.find('xmin').text) / img_width
            y1 = int(box.find('ymin').text) / img_height
            x2 = int(box.find('xmax').text) / img_width
            y2 = int(box.find('ymax').text) / img_height

            x_center = ((x1 + x2) / 2)
            y_center = ((y1 + y2) / 2)
            width = (x2 - x1)
            height = (y2 - y1)

            f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


if __name__ == "__main__":
    randomly_assign_files()
