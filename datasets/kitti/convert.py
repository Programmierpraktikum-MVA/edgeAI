import os
import shutil


def main(train_ratio=0.8):
    images = os.listdir("images")
    split_index = int(len(images) * train_ratio)

    train_images = images[:split_index]
    val_images = images[split_index:]

    os.makedirs("images/train", exist_ok=True)
    os.makedirs("images/val", exist_ok=True)
    os.makedirs("labels/train", exist_ok=True)
    os.makedirs("labels/val", exist_ok=True)

    for image in train_images:
        shutil.move(f"images/{image}", f"images/train/{image}")
        label = image.replace(".png", ".txt")
        shutil.move(f"labels/{label}", f"labels/train/{label}")

    for image in val_images:
        shutil.move(f"images/{image}", f"images/val/{image}")
        label = image.replace(".png", ".txt")
        shutil.move(f"labels/{label}", f"labels/val/{label}")


if __name__ == "__main__":
    main()
