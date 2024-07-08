import torch


def main():
    if torch.cuda.is_available():
        print(f"CUDA is available. Your GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA is not available. Please check your installation.")


if __name__ == "__main__":
    main()
