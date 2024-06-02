import cv2
import os

class_dict = ["pedestrian",
    "rider",
    "car",
    "truck",
    "bus",
    "train",
    "motorcycle",
    "bicycle",
    "traffic light",
    "traffic sign"]

# example jpg: images/train/0a0a0b1a-7c39d841.jpg
path = input("images/val/.jpg oder images/train/.jpg\n")
image = cv2.imread(path)

# determine path of label
head, descriptionfile = os.path.split(path)
descriptionfile = descriptionfile[:-4] + ".txt"
txtpath = "labels" + head[6:] + f"/{descriptionfile}"

with open(txtpath) as f:
    for line in f:
        label, x_center, y_center, width, height = line.split(" ")
        x_center = float(x_center)
        y_center = float(y_center)
        width = float(width)
        height = float(height)
        x1 = int((x_center - width/2)*1280) 
        x2 = int((x_center + width/2)*1280)
        y1 = int((y_center - height/2)*720)
        y2 = int((y_center + height/2)*720)
    
        cv2.rectangle(image, (x1,y1),(x2,y2), (0,255,0),1)
        cv2.putText(image, class_dict[int(label)], (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

cv2.imshow(f"{path}", image)
cv2.waitKey(0)

