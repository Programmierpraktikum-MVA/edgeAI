# Using the ultralytics library

**[Official documentation](https://docs.ultralytics.com/)**

## Training

If you want to finetune a YOLOv8 model or earlier YOLO models, simply use the `train.py` script and change the
line `model = YOLO("yolov8n.pt")` into the pretrained model weights that you actually want. This can either be a local
file or one that ultralytics [features by default](https://docs.ultralytics.com/models/). If you want to use one of our
data sets, follow the instructions in the README.md of the respective data set. In these files you will find everything
important such as the folder structure and the conversion of the annotations. The conversion is important because it
converts the annotations into labels that the Yolo model can use, so if you want to use your own data set, make sure
that
the labels are in the correct format. Run the `train.py` script providing a configuration file for the dataset you want
to train on. Example:

```sh
python3 train.py ../../data/roadsigns/config.yaml
```

You can also specify the number of epochs to train for by passing it as an argument to the `--epochs` or `-e` flag (
default is 1). Simply put, the more epochs the training goes through, the better the model gets at interpreting the
data.

```sh
python3 train.py --epochs 3 ../../data/roadsigns/config.yaml
```

**Important note:** When running the script for the first time, ultralytics will complain about a missing dataset path.
Go to the ultralytics config directory (linux default is /home/<user>/.config/Ultralytics) and open the `settings.yaml`
file. Change the `datasets_dir` to point to the `data` directory in the root of this project (
e.g. `/home/<user>/edgeAI/data`).

**Other import note:** When running the `train.py` script for the first time, ultralytics will download
the [ncnn](https://github.com/Tencent/ncnn) dependency. This takes a very long time (about 15mins average). Ncnn is used
to convert the weights into a format which has better performance on edge devices. If you don't plan to run the model on
edge devices, you can remove the `model.export(format="ncnn")` line from the script.

**Other import note:** If you want to run the train.py via Windows you have to specify in the config.yaml and the paths
Example: path: ..\roadsigns -> C:\Users\%user%\Documents\GitHub\edgeAI\data\roadsigns

## Inference

The `app.py` script sets up a simple flask server that streams images to a port. I guess there are much better ways to
do this but this is very simple and works. Provide a path to the model you want to use and the video source, usually a
video file. The example video used here can be downloaded
from [here](https://raw.githubusercontent.com/intel-iot-devkit/sample-videos/master/person-bicycle-car-detection.mp4)

```sh
python3 app.py runs/detect/train/weights/best.pt person-bicycle-car-detection.mp4
```

If you want to use your **webcam** as input, simply pass `0` as video source.
In the Test.py is a short test to see if your webcam is recognized

```sh
python3 app.py runs/detect/train/weights/best.pt 0
```

0. Car
1. Pedestrian
2. Van
3. Cyclist/rider
4. Truck
5. misc (pretty sure it isn't used anywhere but just in case)
6. Tram
7. Person sitting
8. bus
9. train
10. motorcycle
11. bicycle
12. traffic light
13. traffic sign
14. stop sign
15. speedlimit sign
16. crosswalk