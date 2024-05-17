## Using joliGENs day2night / clear2snowy on bdd

First, we will have to clone the joliGEN repository and afterwards work in it, linking our dataset into the scripts.

```
cd ...
git clone https://github.com/jolibrain/joliGEN.git
cd joliGEN
pip install -r requirements.txt --upgrade
```

Then move the scripts into the joliGEN directory

```
mv or cp script_clear2snowy.sh script_day2night.sh testing.sh training.sh ../../joligen
```

Your folder structure should then look like this
```
├── /edgeAI
│   ├── /data
│   │   ├── /deepdrive
│   │   └── ...
│   ├── /styletransfer
│   │   └── ...
│   └── ...
└── /joliGEN
    └── script_clear2snowy
    └── script_day2night.sh
    └── testing.sh
    └── training.sh
    └── ...
```
Make sure you have the bdd dataset downloaded as described [here](../data/deepdrive/README.md).

# day2night
### Preparation
Modify paths in script `script_day2night.sh` and run from joligen directory. Now the joligen directory should have 3 new subdirectories: day2night, other_segments and val-bboxesdaynight \
The script has seperated the paths of daytime images into `/day2night/trainA` and of nighttime into `/day2night/trainB`. The paths to other time-of-day's is stored in `/other_segments`. `/val-bboxes_day2night` contains the val boxes, same as in `deepdrive/labels/val`.

### Training

Modify paths in script `training_day2night.sh` and run. For further details visit [https://www.joligen.com/doc/tutorial_styletransfer_bdd100k.html](https://www.joligen.com/doc/tutorial_styletransfer_bdd100k.html).

### Inference

Modify and run the script `testing.sh`. This creates a nighttime image from the input image you specify.

# clear2snowy
### Preparation
This is the same as in **day2night** but with the sript `scrip_day2night.sh`. `/clear2snowy/trainA` contains the paths to clear weather images and trainB of snowy weather. `/othersegments` contains other weather image paths.

### Training
This can also be done as in **day2night** but there is also a pretrained model for bdd100k from joliGEN.

```
wget https://www.joligen.com/models/clear2snowy_bdd100k.zip
unzip clear2snowy_bdd100k.zip -d checkpoints
rm clear2snowy_bdd100k.zip
```

### Inference
You can modify and use the same script `testing.sh`. 