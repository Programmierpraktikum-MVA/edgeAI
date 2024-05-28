import argparse
import os

def main(data_path, num_epochs, use_wandb):
    from ultralytics import YOLOv10
    model = YOLOv10("yolov10n.pt")
    
    if use_wandb:
        import wandb
        from wandb.integration.ultralytics import add_wandb_callback
        add_wandb_callback(model, enable_model_checkpointing=True)
    
    model.train(data=data_path, epochs=num_epochs)
    
    if use_wandb:
        wandb.finish()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a YOLO model on a given dataset.")
    parser.add_argument("data_path", help="Path to the configuration YAML file.")
    args = parser.parse_args()

    num_epochs = os.getenv('EPOCHS', 1)
    use_wandb = os.getenv('WANDB', False)
    main(args.data_path, num_epochs, use_wandb)
