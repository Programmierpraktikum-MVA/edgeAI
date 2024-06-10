import argparse
from multiprocessing import freeze_support

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_path', type=str, help='Path to the data configuration file')
    parser.add_argument('--epochs', type=int, default=1, help='Number of epochs to train')
    args = parser.parse_args()

    print(f"Data path: {args.data_path}")
    print(f"Number of epochs: {args.epochs}")

    from ultralytics import YOLOv10

    model = YOLOv10("yolov10n.pt")
    model.train(data=args.data_path, epochs=args.epochs)
    model.export(format="onnx")
    model.export(format="ncnn")
    model.export(format="openvino")


if __name__ == '__main__':
    freeze_support()
    main()
