# Kitti Dataset Object Detection 2D

Kitti object detection dataset with 2D bounding boxes




## Directory setup
1. Download the "data_object_image2" subdirectory from the 'kitti dataset' https://www.kaggle.com/datasets/klemenko/kitti-dataset?select=data_object_image_2 
!The download should only be 11+Gb; we do not need to download the entire dataset (24GB).
2. Download 'kitti-yolo-labels' from https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format.
3. Extract the folders `data_object_image2/training/image_2` and `kitti-yolo-labels/labels` into this directory.
4. Rename the folder `data_object_image2/training/image_2` to `images`.
5. Rename the `kitti-yolo-labels/labels` folder to `annotations`.
6. Run convert.py to generate the train/val/test split (70%/15%/15%).
7. Feel free to delete the empty `annotations` folder now.




In the end, your directory structure should look like this:

  
    ├── images/
    │    └── train/
    │         └── yyy.png
    │     └── val/
    │         └── zzz.png
    ├── labels/
    │     └── train/
    │         └── yyy.txt
    │     └── val/
    │         └── zzz.txt
    ├── config.yaml
    ├── convert.py
    ├── main.ipynb
    └── README.md

Note that "kitti-yolo-labels" only has annotations for the train images within "data_object_image2".
## Size
| Dataset | Images | Size | 
| ------- | ------ | ---- |
| Images  | 7481    | 6.2GB | 


## Annotations

The annotations/labels are already in Yolo format.\
For each object within the picture, the ...txt file has one row with the following syntax:\
object-class, x_center, y_center, width, height\
\
Note: coordinates are already normalized.

More info and references are here: https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format/data?select=labels


**Data structure:** 
Each png-file in images has a corresponding YOLO format txt file in the labels folder.\
(images/train/000000.png for labels/train/000000.txt)


**Classes for objects:**

'Car': 0,\
 'Pedestrian': 1,\
 'Van': 2,\
 'Cyclist': 3,\
 'Truck': 4,\
 'Misc': 5,\
 'Tram': 6,\
 'Person_sitting': 7