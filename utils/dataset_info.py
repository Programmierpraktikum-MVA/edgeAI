import argparse
import os
from collections import defaultdict

class_dict = {
    0: "car",
    1: "person",
    2: "van",
    3: "rider",
    4: "truck",
    5: "tram",
    6: "bus",
    7: "train",
    8: "motorcycle",
    9: "bicycle",
    10: "traffic light",
    11: "street sign",
}

def main(dataset):
    num_train = len(os.listdir(f"{dataset}/images/train"))
    num_val = len(os.listdir(f"{dataset}/images/val"))
    
    print("\nDataset Summary")
    print("================")
    print(f"Train images: {num_train}")
    print(f"Validation images: {num_val}")
    
    print("\nLabel Counts")
    print("============")

    label_counts = defaultdict(int)
    for txt_file in os.listdir(f"{dataset}/labels/train"):
        with open(f"{dataset}/labels/train/{txt_file}", "r") as file:
            for line in file:
                class_id = int(line.split()[0])
                class_name = class_dict[class_id]
                label_counts[class_name] += 1

    for label, count in sorted(label_counts.items()):
        print(f"{label}: {count}")

    size = 0
    for dirpath, _, filenames in os.walk(f"{dataset}/images"):
        for f in filenames:
            size += os.path.getsize(f"{dirpath}/{f}")

    print("\nDataset Size")
    print("============")
    print(f"Total size: {size / (1024 ** 2):.2f} MB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", type=str, help="Path to the dataset directory")
    args = parser.parse_args()
    main(args.data_path)
