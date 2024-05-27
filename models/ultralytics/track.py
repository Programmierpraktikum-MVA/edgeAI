import argparse

def main(model_path):
    from ultralytics import YOLO
    model = YOLO(model_path)
    model.track("person-bicycle-car-detection.mp4", save=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use ultralytics tracking functionality")
    parser.add_argument("model_path", help="Path to the model weights file.")
    args = parser.parse_args()
    main(args.model_path)
