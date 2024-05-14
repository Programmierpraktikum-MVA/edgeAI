import argparse

def main(dataset, num_epochs):
    from ultralytics import YOLO

    if dataset == "deepdrive":
        data_dir = "configs/berkeley-deepdrive.yaml"
    elif dataset == "roadsigns":
        data_dir = "configs/roadsigns.yaml"
    elif dataset == "citypersons":
        data_dir = "configs/citypersons.yaml"

    model = YOLO("yolov8n.pt")
    model.train(data=data_dir, epochs=num_epochs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a YOLO model on a given dataset.")
    parser.add_argument("dataset", choices=["deepdrive", "roadsigns", "citypersons"], help="The dataset to train on")
    parser.add_argument("-e", "--epochs", type=int, default=1, help="The number of epochs to train for")

    args = parser.parse_args()

    main(args.dataset, args.epochs)
