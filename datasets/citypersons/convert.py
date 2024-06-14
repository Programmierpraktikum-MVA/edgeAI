import os
import cv2
import scipy.io
import shutil
from tqdm import tqdm

# unify class_ids with other datasets
unified_classes = {
    1: 1,  # Pedestrian remains 1
    2: 3,  # Rider becomes 3
    3: 7,  # Sitting person becomes 7
}

"""
Script to set up the right image directory structure and generate Yolo Labels for training
"""


# convert annotations to YOLO format and returns the array of annotations
def convert_to_yolo(annotations, image_width, image_height):
    yolo_annotations = []
    for bbox in annotations:
        class_label, x1, y1, w, h, instance_id, x1_vis, y1_vis, w_vis, h_vis = bbox
        # # Use visible bounding box if class_label is not 1 or 2

        if w <= 0 or h <= 0:
            print(
                f"Warning: Invalid bounding box dimensions (w={w}, h={h}) for class_label={class_label}. Skipping."
            )
            continue

        # Normalize bounding box coordinates
        x_center = (x1 + w / 2) / image_width
        y_center = (y1 + h / 2) / image_height
        normalized_w = w / image_width
        normalized_h = h / image_height

        class_label = int(class_label)
        # map classes to unified classes
        class_id = unified_classes.get(class_label)
        if class_id is None:
            continue  # Skip this bbox if class ID is not mapped

        # Append annotation in YOLO format: class_id x_center y_center normalized_w normalized_h
        yolo_annotations.append(
            f"{class_id} {x_center} {y_center} {normalized_w} {normalized_h}"
        )
    return yolo_annotations


# write YOLO annotations array to a text file
def write_yolo_annotations_file(yolo_annotations, file_path):
    with open(file_path, "w") as file:
        for annotation in yolo_annotations:
            file.write(f"{annotation}\n")


"""
process the given dataset and write all the annotations into yolo format
@param anno_file - path to the respective annotations.mat file
@param image_folder - path to the image_folder (leftImg8bit/train or leftImg8bit/val)
@param label-folder - path to the folder where the labels will be stored (labels/train or labels/val)
"""


def process_dataset(anno_file, image_folder, label_folder):

    data = scipy.io.loadmat(anno_file)
    annotations = (
        data["anno_train_aligned"][0]
        if "train" in anno_file
        else data["anno_val_aligned"][0]
    )  # check which subfolder we are creating the dataset for

    city_names = [item["cityname"][0][0][0] for item in annotations]
    image_names = [item["im_name"][0][0][0] for item in annotations]
    bboxes = [item["bbs"][0][0] for item in annotations]

    # create new folder, if not alrdy existent
    os.makedirs(label_folder, exist_ok=True)

    # iterate over all images
    for idx, image_name in enumerate(
        tqdm(image_names, desc=f"Generating labels for {anno_file}")
    ):
        # TODO modify if we already moved the folders over add alternative image_path
        image_path = os.path.join(image_folder, city_names[idx], image_name)

        # read image to get img_height, img_width which are not in the mat file :(
        image = cv2.imread(image_path)
        if image is None:
            print(f"Warning: could not read image {image_path}. Skipping.")
            continue
        image_height, image_width = image.shape[:2]

        # create annotations
        yolo_annotations = convert_to_yolo(bboxes[idx], image_width, image_height)

        # create file_path to store annotations at
        yolo_annotation_file_path = os.path.join(
            label_folder, f"{os.path.splitext(image_name)[0]}.txt"
        )
        write_yolo_annotations_file(yolo_annotations, yolo_annotation_file_path)


def move_images(src_dir, dest_dir):
    """
    Moves images from the source directory to the destination directory.

    Args:
        src_dir (str): Path to the source directory.
        dest_dir (str): Path to the destination directory.
    """

    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    folders = os.listdir(src_dir)
    # Walk through the source directory
    for folder in tqdm(folders, desc="Processing folders"):
        if not folder.startswith("."):  # Exclude hidden files
            folderpath = os.path.join(src_dir, folder)
            print(f"Moving images of folder: {folderpath}")
            for file in os.listdir(folderpath):

                # Construct source file path
                src_file_path = os.path.join(folderpath, file)
                # Construct destination file path
                dest_file_path = os.path.join(dest_dir, file)

                print(dest_file_path)
                # Move file
                shutil.move(src_file_path, dest_file_path)


# read yolo annotations from txt file
def read_yolo_annotations_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    annotations = []
    for line in lines:
        annotations.append(line.strip().split())
    return annotations


# Function to draw bounding boxes on an image
def draw_bounding_boxes(image, annotations, image_width, image_height):
    for annotation in annotations:
        class_id, x_center, y_center, w, h = map(float, annotation)
        x_center *= image_width
        y_center *= image_height
        w *= image_width
        h *= image_height
        x1 = int(x_center - w / 2)
        y1 = int(y_center - h / 2)
        x2 = int(x_center + w / 2)
        y2 = int(y_center + h / 2)
        # Draw rectangle with class label
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            image,
            str(int(class_id)),
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
        )
    return image


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    image_base_path = os.path.join(script_dir, "leftImg8bit")

    # Define the paths to rename tubingen folder for consistency with .mat file
    old_folder_path = os.path.join(image_base_path, "train/tubingen")
    new_folder_path = os.path.join(image_base_path, "train/tuebingen")

    # Rename the folder
    try:
        os.rename(old_folder_path, new_folder_path)
        print("renamed train/tubingen folder to train/tuebingen successfully!")
    except FileNotFoundError:
        print(
            "Folder already renamed to tuebingen? Check if train folder contains tuebingen instead of tubingen"
        )

    # specify path to path to .mat files and the new labels folder
    annotations_base_path = os.path.join(script_dir, "annotations")
    labels_base_path = os.path.join(script_dir, "labels")

    # Process train and validation datasets
    try:
        process_dataset(
            os.path.join(annotations_base_path, "anno_train.mat"),
            os.path.join(image_base_path, "train"),
            os.path.join(labels_base_path, "train"),
        )
        process_dataset(
            os.path.join(annotations_base_path, "anno_val.mat"),
            os.path.join(image_base_path, "val"),
            os.path.join(labels_base_path, "val"),
        )
        print("YOLO annotations files created !")
    except Exception as e:
        print(e)

    print("Moving onto file relocation ...")

    # Define the source and destination directories
    current_img_dir = os.path.join(script_dir, "leftImg8bit")
    new_img_dir = os.path.join(script_dir, "images")

    src_test = os.path.join(current_img_dir, "test")
    src_train = os.path.join(current_img_dir, "train")
    src_val = os.path.join(current_img_dir, "val")

    dest_test = os.path.join(new_img_dir, "test")
    dest_train = os.path.join(new_img_dir, "train")
    dest_val = os.path.join(new_img_dir, "val")

    # Create destination directories if they don't exist
    os.makedirs(dest_test, exist_ok=True)
    os.makedirs(dest_train, exist_ok=True)
    os.makedirs(dest_val, exist_ok=True)

    # Move the images
    try:
        move_images(src_test, dest_test)
        move_images(src_train, dest_train)
        move_images(src_val, dest_val)
        print("Images have been relocated")
    except Exception as e:
        print(e)

    """
    You can test whether relocation and label generation worked by drawing bbox on a single image with the following snippet
    """
    # # Define paths

    # image_path = os.path.join(script_dir, "images/train/aachen_000005_000019_leftImg8bit.png")
    # label_path = os.path.join(script_dir, "labels/train/aachen_000005_000019_leftImg8bit.txt")

    # # Read image
    # image = cv2.imread(image_path)
    # if image is None:
    #     print(f"Error: could not read image {image_path}")
    # else:
    #     image_height, image_width = image.shape[:2]

    #     # Read YOLO annotations
    #     yolo_annotations = read_yolo_annotations_file(label_path)
    #     if not yolo_annotations:
    #         print(f"Error: no annotations found in {label_path}")
    #     else:
    #         # Draw bounding boxes on the image
    #         image_with_bboxes = draw_bounding_boxes(image, yolo_annotations, image_width, image_height)

    #         # Display the image
    #         cv2.imshow("Image with Bounding Boxes", image_with_bboxes)
    #         cv2.waitKey(0)
    #         cv2.destroyAllWindows()

    #         # Optionally, save the image with bounding boxes
    #         output_path = "output_image_with_bboxes.png"
    #         cv2.imwrite(output_path, image_with_bboxes)
    #         print(f"Image with bounding boxes saved to {output_path}")
