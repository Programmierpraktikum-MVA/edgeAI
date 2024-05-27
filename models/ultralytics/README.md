# Using the ultralytics library

**[Official documentation](https://docs.ultralytics.com/models/)**

If you want to finetune a YOLOv8 model or earlier YOLO models, simply use the `train.py` script and change the line `model = YOLO("yolov8n.pt")` into the pretrained model weights that you actually want. This can be either a local file or one that ultralytics feature by default. Provide a configuration file for the dataset you want to train on. We provided some in the `configs` directory. Here is an example usage of running the script. You can use the `-e` flag to specify the number of epochs you want to train (default is 1).

```sh
python3 train.py configs/deepdrive.yaml
```

## YOLOv10

For YOLOv10 there are a couple more steps:

1. Download the pretrained weights from [here](https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10n.pt)

2. Install the necessary dependencies for YOLOv10

    ```sh
    pip install git+https://github.com/THU-MIG/yolov10.git
    ```

3. Change the following lines in the `train.py` script

    ```python
    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")
    ```

    into

    ```python
    from ultralytics import YOLOv10
    model = YOLOv10("yolov10n.pt")
    ```

4. Now you can run the script as specified above
