import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, "..", ".."))

from utils.dataset_utils import split_data

anno_dir = os.path.join(current_dir, "annotations")
imgs_dir = os.path.join(current_dir, "images")
lbls_dir = os.path.join(current_dir, "labels")

class_dict = {
    0: 0,  # car
    1: 1,  # person
    2: 2,  # van
    3: 3,  # cyclist
    4: 4,  # truck
    6: 5,  # tram
    7: 1,  # person
}


def convert():
    if not os.path.isdir(anno_dir):
        print("Make sure you rename the labels directory to annotations")
        return

    split_data(imgs_dir)
    split_data(anno_dir)

    for split in ["train", "val"]:
        src_dir = os.path.join(anno_dir, split)
        dst_dir = os.path.join(lbls_dir, split)
        os.makedirs(dst_dir, exist_ok=True)

        for file in os.listdir(src_dir):
            with open(os.path.join(src_dir, file), "r") as f:
                lines = f.readlines()
            with open(os.path.join(dst_dir, file), "w") as f:
                for line in lines:
                    parts = line.split()
                    kitti_id = int(parts[0])
                    if kitti_id not in class_dict:
                        continue
                    f.write(f"{class_dict[kitti_id]} " + " ".join(parts[1:]) + "\n")


if __name__ == "__main__":
    convert()
