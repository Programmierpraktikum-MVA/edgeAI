# Berkeley DeepDrive Dataset

On Linux systems, you can use the `download.sh` script to download the dataset and labels and set up the directory structure as required. You can also manually download the `bdd100k_det_20_labels_trainval.zip`, `100k_images_test.zip`, `100k_images_train.zip` and `100k_images_val.zip` files from https://dl.cv.ethz.ch/bdd100k/data/ and extract the images to this directory. Make sure your directory structure looks like this after extracting:

```
deepdrive
├── annotations
│   ├── det_train.json
│   └── det_val.json
├── images
│   ├── test
│   ├── train
│   └── val
├── config.yaml
├── convert.py
├── download.sh
└── README.md
```

You can now run the `convert.py` script to create the correct directory structure and YOLO labels in order to train with ultralytics.

## Size

| Dataset | Images | Size | Zip  |
| ------- | ------ | ---- | ---- |
| Train   | 70000  | 4.2G | 3.7G |
| Val     | 10000  | 601M | 542M |
| Test    | 20000  | 1.2G | 1.1G |
| Total   | 100000 | 6.0G | 5.3G |

## Annotations

The keys can be easily looked up in the json file. For each cell, the important attributes are:

- `name`: the image file name
- `labels[].category`: the label as full name (e.g "traffic light")
- `labels[].box2d`: x1, y1, x2, y2 as pixel value coordinates (e.g. 1125.902264)

**Some remarks:**

- Some items don't have labels for some reasen, thus the try-except block.
- In the demo we don't use the whole float number, we convert that to an int. 
- The categories `trailer`, `other vehicle` and `other person` are not officially listed [here](https://wandb.ai/av-datasets/av-dataset/reports/The-Berkeley-Deep-Drive-BDD110K-Dataset--VmlldzoyNjI0MDk5#road-object-detection). You can use `show_img_for_category()` to get some idea for what these classes are used.

Notice: to close the image in the notebook, press any key.

## Links

- https://wandb.ai/av-datasets/av-dataset/reports/The-Berkeley-Deep-Drive-BDD110K-Dataset--VmlldzoyNjI0MDk5
- https://bair.berkeley.edu/blog/2018/05/30/bdd/
