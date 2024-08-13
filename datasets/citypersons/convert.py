import os
import cv2
import scipy.io
import shutil
from tqdm import tqdm

class_dict = {
    1: 1,  # person
    2: 3,  # rider
    3: 1,  # sitting person
    4: 1,  # other persons with unusual postures
}


def move_images(split):
    subdirs = [d for d in os.listdir(f"images/{split}") if os.path.isdir(f"images/{split}/{d}")]

    for subdir in subdirs:
        subdir_path = f"images/{split}/{subdir}"
        for file in os.listdir(subdir_path):
            shutil.move(f"{subdir_path}/{file}", f"images/{split}")
        os.rmdir(subdir_path)


def convert(split):
    data = scipy.io.loadmat(f"annotations/anno_{split}.mat")
    annotations = data[f"anno_{split}_aligned"][0]
    im_names = [item["im_name"][0][0][0] for item in annotations]
    bboxes = [item["bbs"][0][0] for item in annotations]

    os.makedirs(f"labels/{split}", exist_ok=True)

    for idx, im_name in enumerate(tqdm(im_names, desc=f"Generating labels for {split} annotations")):
        image_path = f"images/{split}/{im_name}"
        image = cv2.imread(image_path)
        im_height, im_width, _ = image.shape

        txt_file = f"labels/{split}/{im_name.replace('.png', '.txt')}"
        with open(txt_file, "w") as f:
            for bbox in bboxes[idx]:
                citypersons_id, x1, y1, w, h = bbox[:5]
                if citypersons_id not in class_dict:
                    continue
                class_id = class_dict[citypersons_id]
                x_center = (x1 + w / 2) / im_width
                y_center = (y1 + h / 2) / im_height
                box_width = w / im_width
                box_height = h / im_height
                f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")


if __name__ == "__main__":
    for split in ["train", "val"]:
        move_images(split)
        convert(split)
    move_images("test")
