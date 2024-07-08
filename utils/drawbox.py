import argparse
import cv2

class_dict = {
    0: "Car",
    1: "Pedestrian",
    2: "Van",
    3: "Rider",
    4: "Truck",
    5: "Misc",
    6: "Tram",
    7: "Person sitting",
    8: "Bus",
    9: "Train",
    10: "Motorcycle",
    11: "Bicycle",
    12: "Traffic light",
    13: "Traffic sign",
    14: "Stop sign",
    15: "Speedlimit sign",
    16: "Crosswalk",
}


def main(image_path):
    label_path = (image_path.replace("images", "labels").replace(".png", ".txt").replace(".jpg", ".txt"))

    image = cv2.imread(image_path)

    with open(label_path, "r") as file:
        labels = file.readlines()

    height, width, _ = image.shape

    for label in labels:
        parts = label.strip().split()
        label = class_dict[int(parts[0])]
        x_center = float(parts[1])
        y_center = float(parts[2])
        bbox_width = float(parts[3])
        bbox_height = float(parts[4])

        x_center_abs = int(x_center * width)
        y_center_abs = int(y_center * height)
        bbox_width_abs = int(bbox_width * width)
        bbox_height_abs = int(bbox_height * height)

        x1 = int(x_center_abs - bbox_width_abs / 2)
        y1 = int(y_center_abs - bbox_height_abs / 2)
        x2 = int(x_center_abs + bbox_width_abs / 2)
        y2 = int(y_center_abs + bbox_height_abs / 2)

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Image with Bounding Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display images with bounding boxes and labels")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    args = parser.parse_args()
    main(args.image_path)
