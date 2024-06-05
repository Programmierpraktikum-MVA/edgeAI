from flwr.server.strategy import FedAvg
from flwr.server import start_server
from flwr.client import NumPyClient, start_client
from ultralytics import YOLO

class FlowerClient(fl.client.NumPyClient):
    def __init__(self):
        self.model = YOLO("yolov10n.pt")

    def get_parameters(self, config):
        return self.model.get_parameters()

    def set_parameters(self, parameters):
        self.model.set_parameters(parameters)

    def fit(self, parameters, config):
        self.set_parameters(parameters)

        self.model.train()

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)

        loss, accuracy = self.model.evaluate()

        return loss, len(dataset), {"loss": loss}


def _get_parameters(model):
    return [val.cpu().numpy() for _, val in model.state_dict().items()]


def _set_parameters(model, parameters):
    params_dict = zip(model.state_dict().keys(), parameters)
    state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
    model.load_state_dict(state_dict, strict=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Flower")
    parser.add_argument(
        "--partition-id",
        type=int,
        choices=range(0, 10),
        required=True,
        help="Specifies the artificial data partition",
    )
    args = parser.parse_args()
    partition_id = args.partition_id

    # Model and data
    model = mnist.LitAutoEncoder()
    train_loader, val_loader, test_loader = mnist.load_data(partition_id)

    # Flower client
    client = FlowerClient(model, train_loader, val_loader, test_loader).to_client()
    fl.client.start_client(server_address="127.0.0.1:8080", client=client)


if __name__ == "__main__":
    main()