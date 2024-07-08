# Citypersons Dataset

## Download and Setup of Datasets

Download the `leftImg8bit_trainvaltest.zip` file from https://www.cityscapes-dataset.com/downloads/ and extract the
images to this directory.
Also download the `anno_train.mat` and `anno_val.mat` files
from https://github.com/CharlesShang/Detectron-PYTORCH/tree/master/data/citypersons/annotations.

After extracting, the directory structure NEEDS to look like this, before we can proceed.

    .
    ├── annotations
        ├── anno_train.mat
        ├── anno_val.mat
    ├── leftImg8bit
        ├── test
        ├── train
        ├── val
    ├── git.ignore
    ├── main.ipynb
    ├── README.md
    └── setup.py

Now follow the following steps to restructure the folder and create yolo labels for the images

1. Run `setup.py` to move all images into a centralized `images ` folder, without subdirectories for each city the
   labels are also created.

Feel free to delete the `annotations` and (empty )`leftImg8bit` folder

The resulting structure after running `setup.py` should look like this:

    .
    ├── images
        ├── test
            ...
        ├── train
            ├── aachen_000000_000019_leftImg8bit.png
            ...
        ├── val
            ├── frankfurt_000000_000294_leftImg8bit.txt
            ...
    ├── labels
        ├── train
            ├── aachen_000000_000019_leftImg8bit.txt
        ├── val
            ├── frankfurt_000000_000294_leftImg8bit.txt
    ├── git.ignore
    ├── main.ipynb
    ├── README.md
    └── setup.py

## Old Annotations (not in Yolo format)

The original .mat annotations have the following format
More info here: https://github.com/CharlesShang/Detectron-PYTORCH/tree/master/data/citypersons/annotations

**data structure:** in each cell, there are three fields: `cityname, im_name, bbs`

**bounding box annotation format:** `class_label, x1,y1,w,h, instance_id, x1_vis, y1_vis, w_vis, h_vis`

**class label definition:**

0. ignore regions (fake humans, e.g. people on posters, reflections etc.)
1. pedestrians
2. riders
3. sitting persons
4. other persons with unusual postures
5. group of people

**boxes:**

- visible boxes [x1_vis, y1_vis, w_vis, h_vis] are automatically generated from segmentation masks
- (x1,y1) is the upper left corner
- if class_label==1 or 2
  [x1,y1,w,h] is a well-aligned bounding box to the full body
- else
  [x1,y1,w,h] = [x1_vis, y1_vis, w_vis, h_vis];

## New Annotations (yolo format)

A corresponding txt file for each image

**yolo format**
in each line we have 1 bbox with the following syntax

{class_id} {x_center} {y_center} {normalized_width} {normalized_height
}

**class label definition:**
3 Distinct Labels

pedestrian 1,\
rider 3, \
sitting person 7 


