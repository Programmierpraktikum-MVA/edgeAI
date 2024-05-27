import argparse

def main(data_path, num_epochs):
    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")
    model.train(data=data_path, epochs=num_epochs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a YOLO model on a given dataset.")
    parser.add_argument("data_path", help="Path to the configuration YAML file.")
    parser.add_argument("-e", "--epochs", type=int, default=1, help="Number of epochs to train the model for (default is 1).")
    args = parser.parse_args()
    main(args.data_path, args.epochs)
