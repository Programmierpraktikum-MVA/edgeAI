import os
import shutil


def split_data(train_ratio=0.9):
    annotation_files = [
        f
        for f in os.listdir("annotations")
        if os.path.isfile(os.path.join("annotations", f))
    ]
    total_files = len(annotation_files)
    train_size = int(total_files * train_ratio)
    val_size = total_files - train_size

    print(f"Total files: {total_files}")
    print(f"Train files: {train_size}")
    print(f"Val files: {val_size}")

    os.makedirs("annotations/train", exist_ok=True)
    os.makedirs("annotations/val", exist_ok=True)
    os.makedirs("images/train", exist_ok=True)
    os.makedirs("images/val", exist_ok=True)

    # Move annotation files
    for i, file in enumerate(annotation_files):
        if i < train_size:
            shutil.move(
                os.path.join("annotations", file),
                os.path.join("annotations/train", file),
            )
        else:
            shutil.move(
                os.path.join("annotations", file),
                os.path.join("annotations/val", file),
            )

    # Move corresponding image files
    for subdir in ["train", "val"]:
        for file in os.listdir(os.path.join(f"annotations/{subdir}")):
            image_file = file.split(".")[0] + ".png"
            shutil.move(
                os.path.join("images", image_file),
                os.path.join(f"images/{subdir}", image_file),
            )

    print("Files have been moved to train and val directories.")


if __name__ == "__main__":
    split_data()
