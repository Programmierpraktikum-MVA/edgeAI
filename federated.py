from typing import List, OrderedDict, Optional
import os

import flwr
import numpy as np
import torch
from ultralytics import YOLO

NUM_ROUNDS = 3
EPOCHS = 3
SAVE_DIR="saved_models"

os.environ["YOLO_VERBOSE"] = "false"
base_model = YOLO(model="runs/detect/train/weights/best.pt")
datasets = ["citypersons", "deepdrive", "kitti", "roadsigns"]

strategy = flwr.server.strategy.FedAvg(save_dir=SAVE_DIR)
client_resources = {"num_cpus": 1, "num_gpus": 1.0}


def set_parameters(model, parameters: List[np.ndarray]):
    params_dict = zip(model.state_dict().keys(), parameters)
    state_dict = OrderedDict({k: torch.Tensor(v) for k, v in params_dict})
    model.load_state_dict(state_dict, strict=True)


def get_parameters(model) -> List[np.ndarray]:
    return [val.cpu().numpy() for _, val in model.state_dict().items()]


class YOLOClient(flwr.client.NumPyClient):
    def __init__(self, model, dataset):
        self.model = model
        self.config_path = f"datasets/{dataset}/config.yaml"
        self.train_size = len(os.listdir(f"datasets/{dataset}/images/train"))

    def get_parameters(self, config):
        return get_parameters(self.model)

    def fit(self, parameters, config):
        set_parameters(self.model, parameters)
        self.model.train(data=self.config_path, epochs=EPOCHS)
        return get_parameters(self.model), self.train_size, {}

    def evaluate(self, parameters, config):
        set_parameters(self.model, parameters)
        metrics = self.model.val(data=self.config_path)
        accuracy = metrics.box.map
        loss = 1 - accuracy
        return loss, self.train_size, {"accuracy": accuracy}


def client_fn(node_id: int, partition_id: Optional[int]) -> YOLOClient:
    model = base_model
    dataset = datasets[partition_id]
    return YOLOClient(model, dataset).to_client()

flwr.simulation.start_simulation(
    client_fn=client_fn,
    num_clients=len(datasets),
    config=flwr.server.ServerConfig(num_rounds=NUM_ROUNDS),
    strategy=strategy,
    client_resources=client_resources,
)
