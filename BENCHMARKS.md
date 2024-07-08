# Some benchmarks for the project

We differentiate between two kinds of benchmarks, [Inference Performance](#inference-performance) and [Model Accuracy](#model-accuracy).

## Inference Performance

Here we tried to optimize the inference time on edge devices, specifically Raspberry PI 3, Raspberry PI 3 and NVIDIA Jetson Nano.

- **Format:** Converting the models to formats which are better for edge devices significantly increases the model performance
- **Device:** The device used for inference.
    - Raspi 4: Raspberry Pi 4B, 4GB Ram
    - Raspi 3: Raspberry Pi 3, 1GB Ram
    - Jetson Nano: NVIDIA Jetson Nano
- **Parameters:** The format type of the parameters. We tried quatizing to float16 but there were no improvements
- **Inference time:** Tested on the `short.mp4` video from the [TUBCloud](https://tubcloud.tu-berlin.de/s/jPT5SxQHcMNBxoW)

| Format   | Device      | Parameters | Inference Time (per frame) |
| -------- | ----------- | ---------- |--------------------------- |
| PyTorch  | Raspi 4     | float32    | 1180ms                     |
| NCNN     | Raspi 4     | float32    | 380ms                      |
| NCNN     | Jetson Nano | float32    | 250ms                      |
| NCNN     | Raspi 3     | float32    | 1000ms                     |
| NCNN     | Raspi 4     | float16    | 400ms                      |
| OpenVino | Raspi 4     | float32    | 450ms                      |
| ONNX     | Raspi 4     | float32    | 500ms                      |

## Model Accuracy

The goal here was to see the differences between training a model using centralized and federated learning. The metric we chose to evaluate the model is map50.

**map50** stands for mean Average Precision at 50% Intersection over Union (IoU).

### Centralized

The reference training run was created using

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

for dataset in ["deepdrive", "citypersons", "kitti", "roadsigns"]:
    model.train(data=f"datasets/{dataset}/config.yaml", epochs=5)
```

We trained a model for 5 epochs sequentially on each dataset starting from a pretrained yolo model provided by Ultralytics. The run took about 90 minutes on a NVIDIA RTX 2060.

| Checkpoint        | map50 |
| ----------------- | ----- |
| After deepdrive   | 0.39  |
| After citypersons | 0.52  | 
| After kitti       | 0.74  |
| After roadsigns   | 0.79  |

We see a constant increase in the mean average precision scrore after each training run. By increasing the numbe of epochs or doing multiple rounds of sequentially training on each dataset, we could probably increase the precision by some factor.

### Federated

Using the `federated.py` script we trained these models.

**3 rounds, 1 epoch**

| Checkpoint     | map50 |
| -------------- | ----- |
| After 1 round  | tbd   |
| After 2 rounds | tbd   | 
| After 3 rounds | tbd   |

**2 rounds, 3 epochs**

| Checkpoint     | map50 |
| -------------- | ----- |
| After 1 round  | tbd   |
| After 2 rounds | tbd   |