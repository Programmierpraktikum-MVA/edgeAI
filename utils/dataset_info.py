import argparse
import os
from collections import defaultdict

def main(dataset):
    num_train = len(os.listdir(f"{dataset}/images/train"))
    num_val = len(os.listdir(f"{dataset}/images/val"))
    print("Train images:", num_train)
    print("Val images:", num_val)

    label_counts = defaultdict(int)
    for txt_file in os.listdir(f"{dataset}/labels/train"):
        with open(f"{dataset}/labels/train/{txt_file}", 'r') as file:
            for line in file:
                label = line.split()[0]
                label_counts[label] += 1

    for label, count in sorted(label_counts.items()):
        print(f"{label}: {count}")

    size = 0
    for dirpath, _, filenames in os.walk(f"{dataset}/images"):
        for f in filenames:
            size += os.path.getsize(f"{dirpath}/{f}")
    print("Size:", size, "bytes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", type=str, help="Path to the dataset directory")
    args = parser.parse_args()
    main(args.data_path)
