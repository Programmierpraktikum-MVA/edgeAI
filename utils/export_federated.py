import argparse
from typing import List, OrderedDict
import numpy as np
import torch


def set_parameters(model, parameters: List[np.ndarray]):
    params_dict = zip(model.state_dict().keys(), parameters)
    state_dict = OrderedDict({k: torch.Tensor(v) for k, v in params_dict})
    model.load_state_dict(state_dict, strict=True)


def main(base_model, parameter_file):
    from ultralytics import YOLO

    model = YOLO(base_model)
    params = np.load(parameter_file, allow_pickle=True)
    list_of_ndarrays = []
    for key in params.files:
        list_of_ndarrays.append(params[key])
    set_parameters(model, list_of_ndarrays)
    model.save()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("base_model", type=str, help="Path to the pretrained model .pt file (e.g. runs/detect/train/weights/best.pt)")
    parser.add_argument("parameter_file", type=str, help="Path to the parameter npz file (e.g. saved_models/round1.npz)")
    args = parser.parse_args()

    main(args.base_model, args.parameter_file)
