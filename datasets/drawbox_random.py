import cv2
import os
import sys
import random


# List of all available datasets. Edit the list to reduce the randomness or to test the labels of a certain dataset.

datasets = ["deepdrive", "citypersons", "kitti", "roadsigns"]


image_folders = ["val", "train"]



if __name__ == "__main__":
    chosen_dataset = random.choice(datasets)
    chosen_folder = random.choice(image_folders)
    
    imagepath = chosen_dataset + "/images/" + chosen_folder

    image = random.choice(os.listdir(fr"{imagepath}"))

    imagepath = imagepath + f"/{image}"

    labelpath = chosen_dataset + "/labels/" + f"{chosen_folder}/" + image[:-3] + "txt"
    image = cv2.imread(imagepath)
    img_height, img_width, _  = image.shape
    print(imagepath)
    print(labelpath)
    with open(labelpath) as f:
        for line in f:
            label, x_center, y_center, width, height = line.split(" ")
            x_center = float(x_center)
            y_center = float(y_center)
            width = float(width)
            height = float(height)
            x1 = int((x_center - width/2)*img_width) 
            x2 = int((x_center + width/2)*img_width)
            y1 = int((y_center - height/2)*img_height)
            y2 = int((y_center + height/2)*img_height)
        
            cv2.rectangle(image, (x1,y1),(x2,y2), (0,255,0),1)
            cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 1)
        
    cv2.imshow(f"{imagepath}", image)
    cv2.waitKey(0)
