# Kitti Dataset Object Detection 2D

Download the "data_object_image2" subdirectory from the 'kitti dataset' https://www.kaggle.com/datasets/klemenko/kitti-dataset?select=data_object_image_2 
!The download should only be 11+Gb, we do not need to download the entire dataset (24GB). Then download 'kitti-yolo-labels' from https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format. Extract the folders `data_object_image2/training/image_2` and `kitti-yolo-labels/labels` into this directiory.

Make sure you have this directory structure.

```
kitti
├── annotations/
│   └── 000000.txt
├── images/
│   └── 000000.png
├── config.yaml
├── convert.py
└── README.md
```

Now run the `convert.py` script to create the correct directory structure and YOLO labels in order to train with ultralytics.

## Size

| Dataset | Images | Size | 
| ------- | ------ | ---- |
| Images  | 7481   | 6.2GB | 

## Annotation info

The annotations/labels are already in yolo format\
For each object within the picture, the ...txt File has one row with the following syntax\
object-class, x_center, y_center, width, height\
\
Note: coordinates are already normalized

More info/reference here: https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format/data?select=labels


**Data structure:** 
Each png-file in images has a corresponding YOLO format txt file in labels
(images/train/000000.png for labels/train/000000.txt)


**Classes for objects:**

| ID | Class         | 
| -- | ------------- |
| 0  | car           |
| 1  | pedestrian    |
| 2  | van           |
| 3  | cyclist       |
| 4  | truck         |
| 5  | misc          |
| 6  | tram          |
| 7  | personsitting |
