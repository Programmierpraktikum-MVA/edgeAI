import os
import random
from ultralytics import YOLO

num_predictions = 5
model = "roadsigns"
run_number = ""

model_path = f"runs/detect/train{run_number}/weights/best.pt"

if model == "roadsigns":
    dataset_path = f"../data/{model}/images/train/"
else:
    dataset_path = f"../data/{model}/images/test/"

os.makedirs("predictions", exist_ok=True)
model = YOLO(model_path)

all_images = [f for f in os.listdir(dataset_path) if f.endswith('.png') or f.endswith('.jpg')]
if len(all_images) < num_predictions:
    print(f"Warning: Only {len(all_images)} images available, less than the requested {num_predictions}. Reducing the number to available images.")
    num_predictions = len(all_images)
selected_images = random.sample(all_images, num_predictions)
image_paths = [os.path.join(dataset_path, img) for img in selected_images]

results = model(image_paths)

for index, result in enumerate(results):
    result.show()
    result.save(filename=f"predictions/{model}-{index}.jpg")
