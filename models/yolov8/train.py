import argparse
from multiprocessing import freeze_support

from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_path', type=str, help='Path to the data configuration file')
    parser.add_argument('--epochs', type=int, default=1, help='Number of epochs to train')
    args = parser.parse_args()

    model = YOLO('yolov8n.pt')
    model.train(data=args.data_path, epochs=args.epochs)

if __name__ == '__main__':
    freeze_support()
    main()
