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

    try:
        model = YOLOv10("yolov10n.pt")
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
        return


    print("Starting training...")
    try:
        model.train(data=args.data_path, epochs=args.epochs)
        print("Training completed successfully.")
    except Exception as e:
        print(f"Error during training: {e}")
        return

    try:
        model.export(format="onnx")
        print("Model exported to ONNX format.")
        model.export(format="ncnn")
        print("Model exported to NCNN format.")
        model.export(format="openvino")
        print("Model exported to OpenVINO format.")
    except Exception as e:
        print(f"Error exporting model: {e}")

if __name__ == '__main__':
    freeze_support()
    main()
