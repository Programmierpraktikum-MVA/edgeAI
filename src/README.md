# How to train a model

This README provides instructions on how to start a training run using the `main.py` script. This script is designed to train a YOLO (You Only Look Once) model on two different datasets: Berkeley DeepDrive and Road Signs.

## Requirements

Before you start, ensure you have the following:

1. Python 3.x installed on your system.
2. The `ultralytics` library installed. You can install it using pip:
   ```sh
   pip install ultralytics
   ```

## Usage

To start a training run, follow these steps:

1. Open a terminal.

2. Navigate to the directory containing the `main.py` script.

3. Run the script using the following command:
   ```sh
   python main.py [dataset] -e [epochs]
   ```
   Replace `[dataset]` with the name of the dataset you want to train on. The options are `deepdrive` for Berkeley DeepDrive and `roadsigns` for Road Signs.

   Replace `[epochs]` with the number of epochs you want to train for. This is optional and defaults to 1 if not provided.

Here is an example:

- To train on the Berkeley DeepDrive dataset for 10 epochs:
  ```
  python main.py deepdrive -e 10
  ```

After running the script, the model will start training. The training results and the trained model will be saved in the script's directory.

## What the Script Does

The `main.py` script does the following:

1. Loads a pretrained YOLO model.
2. Trains the model on the specified dataset for the specified number of epochs.
3. Evaluates the model's performance on the validation set.
4. Makes a prediction on an image.
5. Exports the model to ONNX format.
