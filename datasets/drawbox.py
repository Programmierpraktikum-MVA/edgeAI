import cv2
import os
import sys
import xml.etree.ElementTree as ET


# example jpg: images/train/0a0a0b1a-7c39d841.jpg
path = sys.argv[1]


def drawtxt(path, split_path):
    image = cv2.imread(path)
    img_height, img_width, _  = image.shape
    dataset = split_path[0]
    
# determine path of label
    txtpath_prefix = f"labels/{split_path[-2]}" if dataset in ["deepdrive", "citypersons"] else "annotations"
    _, descriptionfile = os.path.split(path)
    descriptionfile = descriptionfile[:-4] + ".txt"
    txtpath = os.path.join(dataset + f"/{txtpath_prefix}" +  f"/{descriptionfile}")
    print(txtpath)
    with open(txtpath) as f:
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
        
    cv2.imshow(f"{path}", image)
    cv2.waitKey(0)


def drawxml(path, dataset):
    image = cv2.imread(path)
    img_height, img_width, _  = image.shape
    _, descriptionfile = os.path.split(path)
    descriptionfile = descriptionfile[:-4] + ".xml"
    xmlpath = "roadsigns/annotations/" + f"{descriptionfile}"
    print(xmlpath)

    tree = ET.parse(xmlpath)
    root = tree.getroot()
    bounding_boxes = []
    for obj in root.findall('object'):
        label = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        bounding_boxes.append((label, xmin, ymin, xmax, ymax))
    
    for bbox in bounding_boxes:
        bbox_label, xmin, ymin, xmax, ymax = bbox
        cv2.rectangle(image, (xmin,ymin), (xmax, ymax), (0,255,0),1)
        cv2.putText(image, bbox_label, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 1)
    cv2.imshow(f"{path}", image)
    cv2.waitKey(0)
    



if __name__ == "__main__":
    path = sys.argv[1]
    try:
        f = open(path)
    except FileNotFoundError:
        print("Couldn't find the path. Please make sure that your terminal is in the data directory and all the datasets are structured like specified in their respective README.md.")
        sys.exit(1)
    f.close()

    split_path = os.path.normpath(path).split(os.sep)
    dataset = split_path[0]
    
    if dataset in ["deepdrive", "kitti", "citypersons"]:
        drawtxt(path, split_path)
    elif dataset == "roadsigns":
        drawxml(path, split_path)
    