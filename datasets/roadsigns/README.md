# Roadsign Dataset

Download the 'archive.zip' file from https://www.kaggle.com/datasets/andrewmvd/road-sign-detection and extract the folder into this directory.
Afterwards, the directory structure should look like this:
    
```
roadsigns
├── annotations/
│   └── road0.xml
├── images/
│   └── road0.png
├── config.yaml
├── convert.py
├── main.ipynb
└── README.md
```

## Annotations

More information and references are here: https://www.kaggle.com/datasets/andrewmvd/road-sign-detections

**Data structure:** 
Each .png image has a corresponding .xml file (road0.png has road0.xml).
Each "object" within the xml file corresponds to a bbox: 

**Bounding Box Annotation Format:**
Example road0.xml

```xml
<object>
    <name>trafficlight</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <occluded>0</occluded>
    <difficult>0</difficult>
    <bndbox>
        <xmin>98</xmin>
        <ymin>62</ymin>
        <xmax>208</xmax>
        <ymax>232</ymax>
    </bndbox>
</object>
```

**More info for BBoxes:**
- (xmin,ymin) is the upper left corner

**4 classes for objects:**

1. Traffic Light (name = trafficlight)
2. Stop (name = stop)
3. Speedlimit (name = speedlimit)
4. Crosswalk (name = crosswalk)

## Convert to Yolo-Format

Run convert.py. The structure before using convert.py should be equal to the one mentioned in the Roadsigns Dataset, it will shuffle the images and annotations into train and val folders, and afterwards create label files
in yolo format.

The structure should look like this after running convert.py:

```
roadsigns
├── annotations/
│   ├── train
│   │   └── roadX.xml
│   └── val
│       └── roadY.xml
├── images/
│   ├── train
│   │   └── roadX.png
│   └── val
│       └── roadY.png
├── labels/
│   ├── train
│   │   └── roadX.txt
│   └── val
│       └── roadY.txt
├── config.yaml
├── convert.py
├── main.ipynb
└── README.md
```
