# Citypersons Dataset

Download the `leftImg8bit_trainvaltest.zip` file from https://www.cityscapes-dataset.com/downloads/ and extract the images to this directory. Also download the `anno_train.mat` and `anno_val.mat` files from https://github.com/CharlesShang/Detectron-PYTORCH/tree/master/data/citypersons/annotations.

After extracting, the directory structure NEEDS to look like this, before we can proceed.

```
citypersons
├── annotations
│   ├── anno_train.mat
│   └── anno_val.mat
├── images
│   ├── test
│   ├── train
│   └── val
├── README.md
└── convert.py
```

You can now run the `convert.py` script to create the correct directory structure and YOLO labels in order to train with ultralytics.

## Annotation info

More info here: https://github.com/CharlesShang/Detectron-PYTORCH/tree/master/data/citypersons/annotations

**data structure:** in each cell, there are three fields: `cityname, im_name, bbs`

**bounding box annotation format:** `class_label, x1,y1,w,h, instance_id, x1_vis, y1_vis, w_vis, h_vis`

**class label definition:**

0 -> ignore regions (fake humans, e.g. people on posters, reflections etc.)
1 -> pedestrians
2 -> riders
3 -> sitting persons
4 -> other persons with unusual postures
5 -> group of people

**boxes:**

- visible boxes [x1_vis, y1_vis, w_vis, h_vis] are automatically generated from segmentation masks
- (x1,y1) is the upper left corner
- if class_label==1 or 2
  [x1,y1,w,h] is a well-aligned bounding box to the full body
- else
  [x1,y1,w,h] = [x1_vis, y1_vis, w_vis, h_vis];