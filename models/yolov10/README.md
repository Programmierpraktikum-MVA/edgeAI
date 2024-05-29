# Using YOLOv10

**[YOLOv10 Repository](https://github.com/THU-MIG/yolov10.git)**

YOLOv10 just recently came out and is not officially supported by the ultralytics library yet. The authors provide a custom implementation so you can use YOLOv10 in the usual ultralytics way. Simply pip install the library from source and you are good to go.

```sh
pip install git+https://github.com/THU-MIG/yolov10.git
```

The authors also provide a pretrained YOLOv10n model. You can download it from [here](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt)

## Training

Run the `train.py` script providing a configuration file for the dataset you want to train on.

```sh
python3 train.py ../../data/deepdrive/config.yaml
```

You can also specify the number of epochs to train for by passing it as an argument to the `--epochs` or `-e` flag (default is 1).

```sh
python3 train.py -e 3 ../../data/deepdrive/config.yaml
```

**Important note:** When running the script for the first time, ultralytics will complain about a missing dataset path. Go to the ultralytics config directory (linux default is /home/<user>/.config/Ultralytics) and open the `settings.yaml` file. Change the `datasets_dir` to point to the `data` directory in the root of this project (e.g. `/home/<user>/edgeAI/data`).

## Inference

The `app.py` script sets up a simple flask server that streams images to a port. I guess there are much better ways to do this but this is very simple and works. Provide a path to the model you want to use and the video source, usually a video file. The example video used here can be downloaded from [here](https://raw.githubusercontent.com/intel-iot-devkit/sample-videos/master/person-bicycle-car-detection.mp4)

```sh
python3 app.py runs/detect/train/weights/best.pt person-bicycle-car-detection.mp4
```

If you want want to use your **webcam** as input, simply pass `0` as video source.

```sh
python3 app.py runs/detect/train/weights/best.pt 0
```
