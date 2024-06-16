import os
import cv2
import scipy.io
import shutil
from tqdm import tqdm

class_dict = {
    1: 1,
    2: 3,
    3: 7,
}


def move_images(data_type):
    subdirs = [d for d in os.listdir(f"images/{data_type}") if os.path.isdir(f"images/{data_type}/{d}")]

    for subdir in subdirs:
        subdir_path = f"images/{data_type}/{subdir}"
        for file in os.listdir(subdir_path):
            shutil.move(f"{subdir_path}/{file}", f"images/{data_type}")
        os.rmdir(subdir_path)


def convert_to_yolo(data_type):
    data = scipy.io.loadmat(f"annotations/anno_{data_type}.mat")
    annotations = data[f"anno_{data_type}_aligned"][0]
    im_names = [item["im_name"][0][0][0] for item in annotations]
    bboxes = [item["bbs"][0][0] for item in annotations]

    os.makedirs(f"labels/{data_type}", exist_ok=True)

    for idx, im_name in enumerate(tqdm(im_names, desc=f"Generating labels for {data_type} annotations")):
        image_path = f"images/{data_type}/{im_name}"
        image = cv2.imread(image_path)
        im_height, im_width, _ = image.shape

        txt_file = f"labels/{data_type}/{im_name.replace('.png', '.txt')}"
        with open(txt_file, "w") as f:
            for bbox in bboxes[idx]:
                class_id, x1, y1, w, h = bbox[:5]
                if class_id not in class_dict:
                    continue

                x_center = (x1 + w / 2) / im_width
                y_center = (y1 + h / 2) / im_height
                box_width = w / im_width
                box_height = h / im_height
                class_id = class_dict[class_id]
                f.write(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")


if __name__ == "__main__":
    for data_type in ["train", "val"]:
        move_images(data_type)
        convert_to_yolo(data_type)
    move_images("test")
