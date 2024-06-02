# Street View Dataset
This dataset does **not** contain Google Street View images, but rather images taken from traffic cameras in turkish cities. There also a few other images of trucks or cars alone. \
This dataset provides more road images with different angles, especially from above, which our other datasets don't have.

## Download
Download the dataset from [roboflow](https://universe.roboflow.com/fsmvu/street-view-gdogo) in desired format and extract the .zip in this directory.
Your directory structure should then look like this if exported to YOLOv8 format:

```
.
├── valid
│   ├── labels
│   └── images
├── train
│   ├── labels
│   └── images
├── test
│   ├── labels
│   └── images
├── data.yaml
├── README.roboflow.txt
├── README.dataset.txt
└── README.md
```

## Size
|            | **train** | **valid** | **test** | **$\sum$** |
|:----------:|:---------:|:---------:|:--------:|:-------:|
| **images** |    7566   |    805    |    322   |   8693  |

For YOLOv8 export, the total size is 727 MB.

## Classes

bicycle, bus, car, motorbike, person, truck