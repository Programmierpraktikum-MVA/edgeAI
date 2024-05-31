import argparse

parser = argparse.ArgumentParser(description="Train a YOLOv8 model on a given dataset.")
parser.add_argument("data_path", help="Path to the configuration YAML file.")
parser.add_argument("-e", "--epochs", type=int, default=1, help="Number of epochs to train the model for (default is 1).")
args = parser.parse_args()

from ultralytics import YOLOv10
model = YOLOv10("yolov10n.pt")
model.train(data=args.data_path, epochs=args.epochs)
model.export(format="onnx")
model.export(format="ncnn")
model.export(format="openvino")
