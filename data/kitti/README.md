# Kitti Dataset Object Detection 2D

Kitti object detection dataset with 2d bounding boxes




## Directory setup
1. Download the "data_object_image2" subdirectory from the 'kitti dataset' https://www.kaggle.com/datasets/klemenko/kitti-dataset?select=data_object_image_2 
2. Download 'kitti-yolo-labels' from https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format 
3. Extract the folders "data_object_image2/training/image_2" and "kitti-yolo-labels/labels" into this directiory
4. Rename the folder "data_object_image2/training/image_2" to "images" 
5. Rename the "kitti-yolo-labels/labels" folder to "annotations"





In the end your directory structure should look like the following

    ├── annotations/
    │   └── 000000.txt
    ├── images/
    │   └── 000000.png
    ├── .gitignore
    ├── classes.json
    ├── main.ipynb
    └── README.md

!Note the "kitti-yolo-labels" only has annotations for the train images within "data_object_image2"
## Size
| Dataset | Images | Size | 
| ------- | ------ | ---- |
| Images  | 7481    | 6.2GB | 


## Annotations

The annotations/labels are already in yolo format\
For each object within the picture, the ...txt File has one row with the following syntax\
object-class, x_center, y_center, width, height\
\
Note: coordinates are already normalized

More info/reference here: https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format/data?select=labels


**Data structure:** 
Each png-file in data_object_image_2/training/image_2 has a corresponding YOLO format txt file in kitti-dataset-yolo-format/labels
(000000.png <-> 000000.txt)


**Classes for objects:**

'Car': 0,\
 'Pedestrian': 1,\
 'Van': 2,\
 'Cyclist': 3,\
 'Truck': 4,\
 'Misc': 5,\
 'Tram': 6,\
 'Person_sitting': 7


