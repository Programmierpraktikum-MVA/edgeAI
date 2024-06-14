import argparse


def main(data, epochs):
    from ultralytics import YOLO

    model = YOLO("yolov8n.pt")
    model.train(data=data, epochs=epochs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_path", type=str, help="Path to the data configuration file")
    parser.add_argument("-e", "--epochs", type=int, default=1, help="Number of epochs to train the model for (default is 1).")
    args = parser.parse_args()
    main(args.data_path, args.epochs)
