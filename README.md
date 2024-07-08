# Computer vision on edge devices

If you are on **Windows**, make sure you've set up your system as specified [here](docs/WINDOWS.md).

## Set up

Before getting started, we recommend you delete any [Ultralytics](https://docs.ultralytics.com/) configuration file that may already be on your system.

**Linux:**

```sh
rm -rf ~/.config/Ultralytics/
```

**Windows:**

In most cases, the config can be found somewhere in `$env:USERPROFILE\AppData`.

## Training

We've provided four datasets that you can use out of the box to train a model. Just make sure you follow the steps in the respective README files and convert the annotations into the YOLO format using the respective `convert.py` script. If so, you can simply start a training run on one dataset like this:

```sh
python3 train.py datasets/roadsigns/config.yaml
```

You can also specify the number of epochs to train for by passing it as an argument to the `--epochs` or `-e` flag (default is 1).

```sh
python3 train.py -e 3 datasets/roadsigns/config.yaml
```

## Export

For better inference performance on edge devices, you will want to export your model to [ncnn](https://github.com/Tencent/ncnn) format. We recommend using the [Ultraltics CLI](https://docs.ultralytics.com/usage/cli/) for that.

```sh
yolo export model=runs/detect/train/weights/best.pt format=ncnn
```

**Important note:** When exporting to ncnn for the first time, Ultralytics will download the ncnn dependency. This takes a very long time (about 15 minutes average).

## Inference

The `app.py` script sets up a simple flask server that streams images to a port. Provide a path to the model you want to use and the video source, usually a video file. The example video used here can be downloaded from [here](https://tubcloud.tu-berlin.de/s/GPLWJp8EpEoEt43)

```sh
python3 app.py runs/detect/train/weights/best.pt mittel_1.mp4
```

If you want to use your **webcam** as input, simply pass `0` as a video source.
