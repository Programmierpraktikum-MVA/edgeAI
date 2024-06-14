import os
import shutil
import random
import tqdm


src_dir_img = "images"
src_dir_anno = "annotations"

dest_dir_anno = "labels"
dest_dir_train = "train"
dest_dir_val = "val"
dest_dir_test = "test"


def main(train_ratio=0.8):
    image_files = [f for f in os.listdir(src_dir_img) if f.endswith(".png")]
    annotation_files = [f for f in os.listdir(src_dir_anno) if f.endswith(".txt")]
    image_files.sort()
    annotation_files.sort()

    os.makedirs(src_dir_img + "/" + dest_dir_train, exist_ok=True)
    os.makedirs(src_dir_img + "/" + dest_dir_val, exist_ok=True)

    os.makedirs(dest_dir_anno + "/" + dest_dir_train, exist_ok=True)
    os.makedirs(dest_dir_anno + "/" + dest_dir_val, exist_ok=True)

    for image_file, annotation_file in tqdm(zip(image_files, annotation_files)):
        dest_dir = dest_dir_train if random.random() < train_ratio else dest_dir_val

        img_start_path = src_dir_img + "/" + image_file
        img_end_path = src_dir_img + "/" + dest_dir + "/" + image_file
        anno_start_path = src_dir_anno + "/" + annotation_file
        anno_end_path = dest_dir_anno + "/" + dest_dir + "/" + annotation_file

        shutil.move(img_start_path, img_end_path)
        shutil.move(anno_start_path, anno_end_path)


if __name__ == "__main__":
    main()
