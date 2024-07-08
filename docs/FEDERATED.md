# Using the Flower Framework for Federated Learning

**[Flower Framework Website](https://flower.ai/)**

Training a model using federated learning can be done with the provided `federated.py` script. Simply follow these steps to correctly set up everything.

## Install dependencies

For easier use and integration of the Flower Framework with Ultralytics (our YOLO deep learning library), we've created a fork of flower and added model saving at the end of each round.

```sh
pip install ultralytics
pip install -e git+https://github.com/squarra/flower.git#egg=flwr[simulation]
```

**Important note:** If you see pip throwing some weird errors regarding version conflicts this is likely because a core dependency of Flower (Ray) is not ready for Python3.12 yet. **Make sure to use Python3.11 or older for Flower**

## Configuration

- **NUM_ROUNDS**: The number of rounds for federated learning
- **EPOCHS**: The number of epochs each client trains for in one federated learning round.
- **SAVE_DIR**: The directory in which the global model parameters should be saved after each round.
- **base_model**: The base model to be used for federated learning. This must be a model that has been trained on one of the provided datasets for at least one epoch ([how to do training](../README.md#training)).
- **datasets**: The datasets you want to use for federated learning. Each dataset will be put on one individual client.
- **strategy**: We recommend leaving it as is.
- **client_ressources**: The ressources each client gets. Flower will try to parralelize training as much as possible. When specifying `num_gpus: 1 / len(datasets)` for example, Flower will allocate a part of the GPU to each client and run the clients concurrently. This can lead to out-of-memory errors easily though so we recommend giving one whole GPU to each client. This effectively gets rid of the concurrency but will stabilize training time.

## Training

Once you are happy with your configuration you can run the script:

```sh
python3 federated.py
```

If you want to have all the logs from Ultralytics, simply comment out the line `os.environ["YOLO_VERBOSE"] = "false"`.

## Exporting

During training the global model parameters will be saved to SAVE_DIR as a numpy file at the end of each round. You can then create a .pt file from those saved parameters by running the `utils/export_federated.py` file:

```sh
python3 export.py ../runs/detect/train/weights/best.pt ../saved_models/round1.npz
```

or simply running this python code:

```python
from typing import List, OrderedDict
import numpy as np
import torch
from ultralytics import YOLO

def set_parameters(model, parameters: List[np.ndarray]):
    params_dict = zip(model.state_dict().keys(), parameters)
    state_dict = OrderedDict({k: torch.Tensor(v) for k, v in params_dict})
    model.load_state_dict(state_dict, strict=True)

model = YOLO("runs/detect/train/weights/best.pt")
params = np.load("<SAVE_DIR>/round1.npz", allow_pickle=True)
list_of_ndarrays = []
for key in params.files:
    list_of_ndarrays.append(params[key])
set_parameters(model, list_of_ndarrays)
model.save()
```

This will create a `saved_model.pt` file which you can then further use to [export to different formats](../README.md#export).

**Important note:** Again, please specify a model based off of a finetuned model and not only `YOLO("yolov8n.pt)`. Ideally use the same base model as in the `federated.py` script.