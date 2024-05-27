import argparse

def main(model_path):
    from ultralytics import YOLO
    model = YOLO(model_path)
    model.predict("https://ultralytics.com/images/bus.jpg", save=True, imgsz=320, conf=0.5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a prediction on an image")
    parser.add_argument("model_path", help="Path to the model weights file.")
    args = parser.parse_args()
    main(args.model_path)
