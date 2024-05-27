import argparse

def main(data_path, num_epochs, wandb):
    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")
    
    if wandb:
        import wandb
        from wandb.integration.ultralytics import add_wandb_callback
        add_wandb_callback(model, enable_model_checkpointing=True)
    
    model.train(data=data_path, epochs=num_epochs)
    
    if wandb:
        wandb.finish()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a YOLO model on a given dataset.")
    parser.add_argument("data_path", help="Path to the configuration YAML file.")
    parser.add_argument("-e", "--epochs", type=int, default=1, help="Number of epochs to train the model for (default is 1).")
    parser.add_argument("--wandb", help="Flag to enable tracking with wandb")
    args = parser.parse_args()
    main(args.data_path, args.epochs, args.wandb)
