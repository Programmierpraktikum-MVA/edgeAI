# Roadsign Dataset

Download the 'archive.zip' file from https://www.kaggle.com/datasets/andrewmvd/road-sign-detection and extract the folder into this directiory. 

Make sure you have this directory structure:
    
```
roadsigns
├── annotations/
│   └── road0.xml
├── images/
│   └── road0.png
├── config.yaml
├── convert.py
└── README.md
```

Now run the `convert.py` script to create the correct directory structure and YOLO labels in order to train with ultralytics.

## Annotation info

More info/reference here: https://www.kaggle.com/datasets/andrewmvd/road-sign-detections

**Data structure:** 
Each .png image has a corresponding .xml file (road0.png has road0.xml)
Each "object" within the xml file corresponds to a bbox : 

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

- trafficlight
- stop
- speedlimit
- crosswalk
