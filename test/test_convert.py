import os
import unittest

class TestLabels(unittest.TestCase):
    def check_labels(self, dataset_name):
        for sub_dir in ["train", "val"]:
            img_path = os.path.join(f"datasets/{dataset_name}/images", sub_dir)
            lbl_path = os.path.join(f"datasets/{dataset_name}/labels", sub_dir)
            
            images = [f for f in os.listdir(img_path) if any(f.endswith(ext) for ext in [".png", ".jpg"])]
            labels = [f[:-3] + 'txt' for f in images]
            
            for label in labels:
                label_file = os.path.join(lbl_path, label)
                self.assertTrue(os.path.exists(label_file), f"Label {label} does not exist in {lbl_path}.")
                self.check_label_format(label_file)
    
    def check_label_format(self, label_file):
        with open(label_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                self.assertEqual(len(parts), 5, f"Invalid label format in {label_file}: {line.strip()}")
                class_label = int(parts[0])
                self.assertTrue(0 <= class_label <= 16, f"Invalid class label in {label_file}: {class_label}")
                for num in parts[1:]:
                    float_num = float(num)
                    self.assertTrue(0 <= float_num <= 1, f"Invalid number format in {label_file}: {float_num}")

    def test_roadsigns_labels(self):
        self.check_labels("roadsigns")

if __name__ == "__main__":
    unittest.main()
