# Setting Up the Project on Windows

If you are a Windows user and want to try out our project, follow the steps outlined to ensure it
runs smoothly without errors.

**YouTube Tutorial:** Watch this
helpful [YouTube video](https://www.youtube.com/watch?v=r7Am-ZGMef8&ab_channel=SL7Tech) which provides a detailed
guide.

**Text Guide:** Another helpful source
in [Text](https://medium.com/analytics-vidhya/installing-cuda-and-cudnn-on-windows-d44b8e9876b5) form.


## 1. Download the required Software

Before getting started, ensure you have the necessary software installed:

- **PyTorch:** Visit the [PyTorch website](https://pytorch.org/get-started/locally/) to get the correct version number
  of CUDA and a pip install command.

- **Visual Studio:** Download the latest version of Visual Studio
  from [here](https://visualstudio.microsoft.com/de/vs/older-downloads/).

- **CUDA Toolkit:** Choose the CUDA version compatible with PyTorch from the NVIDIA
  website's [CUDA Toolkit Archive](https://developer.nvidia.com/cuda-toolkit-archive).

- **cuDNN:** Select the appropriate cuDNN version corresponding to your chosen CUDA version from
  the [cuDNN Archive](https://developer.nvidia.com/rdp/cudnn-archive).

## 2. Installation

Follow the installation instructions provided with each software package to complete the setup process.

- **Extracting cuDNN Files:** Extract the cuDNN zip file. You'll need to move some files from the cuDNN directory to
  specific subfolders within the CUDA directory. This process is explained in detail in the YouTube video mentioned
  above, starting from minute 08:40. Refer to the video for a step-by-step walkthrough.
- **Execute the command from the PyTorch website:** It should look something like this:
    ```bash
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
  ```

To verify that everything is set up correctly, run a test script:

1. **Run the script:** Execute the script by running the following command in your terminal:

    ```bash
    python test.py
    ```

   If you see the name of your NVIDIA GPU printed, it means the installation was successful. If CUDA is not available,
   please check your installation steps.
