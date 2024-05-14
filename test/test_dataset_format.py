import unittest
import os


class TestYOLODatasetFormat(unittest.TestCase):
    def check_dataset_format(self, dataset_path):
        """
        Helper function to check dataset format.
        Assumes images are in dataset_path/images/{train,val} and annotations are in dataset_path/labels/{test,val}.
        """
        for subdir in ["train", "val"]:
            images_path = os.path.join(dataset_path, "images", subdir)
            labels_path = os.path.join(dataset_path, "labels", subdir)

            self.assertTrue(
                os.path.exists(images_path),
                f"Images directory does not exist: {images_path}",
            )
            self.assertTrue(
                os.path.exists(labels_path),
                f"Labels directory does not exist: {labels_path}",
            )

            image_files = {
                file
                for file in os.listdir(images_path)
                if file.endswith((".jpg", ".png"))
            }
            label_files = {
                file.replace(".txt", "")
                for file in os.listdir(labels_path)
                if file.endswith(".txt")
            }

            image_files_no_ext = {os.path.splitext(file)[0] for file in image_files}

            for label in label_files:
                self.assertIn(
                    label,
                    image_files_no_ext,
                    f"No corresponding image found for label {label} in {subdir} subdirectory",
                )

            for label_file in label_files:
                with open(os.path.join(labels_path, label_file + ".txt"), "r") as file:
                    for line in file:
                        elements = line.strip().split()
                        self.assertEqual(
                            len(elements),
                            5,
                            "Each line in label file must have 5 elements.",
                        )

                        class_id = int(elements[0])
                        x_center, y_center, width, height = map(float, elements[1:])

                        self.assertGreaterEqual(
                            class_id, 0, "Class ID must be a non-negative integer."
                        )
                        # self.assertLess(class_id, num_classes, f"Class ID must be less than the number of classes ({num_classes}).")

                        self.assertTrue(
                            0 <= x_center <= 1 and 0 <= y_center <= 1,
                            "Center coordinates must be normalized.",
                        )
                        self.assertTrue(
                            0 < width <= 1 and 0 < height <= 1,
                            "Width and height must be normalized and positive.",
                        )

    def test_citypersons(self):
        dataset_path = "data/citypersons"
        self.check_dataset_format(dataset_path)

    def test_deepdrive(self):
        dataset_path = "data/deepdrive"
        self.check_dataset_format(dataset_path)

    def test_roadsigns(self):
        dataset_path = "data/roadsigns"
        self.check_dataset_format(dataset_path)


if __name__ == "__main__":
    unittest.main()
