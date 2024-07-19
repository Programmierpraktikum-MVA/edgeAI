import os
import shutil


def split_data(path, ratio=0.8):
    if not os.path.isdir(path):
        print("Please provide a directory and not a file")
        return
    if not os.path.isabs(path):
        print("Please provide an absolute path")
        return
    if os.listdir(path) == ["val", "train"]:
        print(f"Already split the datasets for {path}")
        return

    train_dir = os.path.join(path, "train")
    val_dir = os.path.join(path, "val")

    files = sorted(os.listdir(path))
    split_index = int(len(files) * ratio)

    train_files = files[:split_index]
    val_files = files[split_index:]

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    for file in train_files:
        shutil.move(os.path.join(path, file), train_dir)

    for file in val_files:
        shutil.move(os.path.join(path, file), val_dir)
