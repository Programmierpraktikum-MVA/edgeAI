# Using the ultralytics library

**[Official documentation](https://docs.ultralytics.com/)**

## Training

If you want to finetune a YOLOv8 model or earlier YOLO models, simply use the `train.py` script and change the
line `model = YOLO("yolov8n.pt")` into the pretrained model weights that you actually want. This can either be a local
file or one that ultralytics [features by default](https://docs.ultralytics.com/models/). Run the `train.py` script
providing a configuration file for the dataset you want to train on.

```sh
python3 train.py ../../data/kitti/config.yaml
```

You can also specify the number of epochs to train for by passing it as an argument to the `--epochs` or `-e` flag (
default is 1).

```sh
python3 train.py -e 3 ../../data/kitti/config.yaml
```

**Important note:** When running the script for the first time, ultralytics will complain about a missing dataset path.
Go to the ultralytics config directory (linux default is /home/<user>/.config/Ultralytics) and open the `settings.yaml`
file. Change the `datasets_dir` to point to the `data` directory in the root of this project (
e.g. `/home/<user>/edgeAI/data`).

**Other import note:** When running the `train.py` script for the first time, ultralytics will download the [ncnn](https://github.com/Tencent/ncnn) dependency. This takes a very long time (about 15mins average). Ncnn is used to convert the weights into a format which has better performance on edge devices. If you don't plan to run the model on edge devices, you can remove the `model.export(format="ncnn")` line from the script.

## Inference

The `app.py` script sets up a simple flask server that streams images to a port. I guess there are much better ways to
do this but this is very simple and works. Provide a path to the model you want to use and the video source, usually a
video file. The example video used here can be downloaded
from [here](https://raw.githubusercontent.com/intel-iot-devkit/sample-videos/master/person-bicycle-car-detection.mp4)

```sh
python3 app.py runs/detect/train/weights/best.pt person-bicycle-car-detection.mp4
```

If you want to use your **webcam** as input, simply pass `0` as video source.

```sh
python3 app.py runs/detect/train/weights/best.pt 0
```
