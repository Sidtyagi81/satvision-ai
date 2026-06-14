import os
import cv2
import torch
import numpy as np
from torch.utils.data import Dataset

class ChangeDetectionDataset(Dataset):

    def __init__(self, root_dir):

        self.a_dir = os.path.join(root_dir, "A")
        self.b_dir = os.path.join(root_dir, "B")
        self.label_dir = os.path.join(root_dir, "label")

        self.images = os.listdir(self.a_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):

        img_name = self.images[index]

        img_a_path = os.path.join(self.a_dir, img_name)
        img_b_path = os.path.join(self.b_dir, img_name)
        label_path = os.path.join(self.label_dir, img_name)

        img_a = cv2.imread(img_a_path)
        img_b = cv2.imread(img_b_path)
        label = cv2.imread(label_path, 0)

        img_a = cv2.resize(img_a, (256, 256))
        img_b = cv2.resize(img_b, (256, 256))
        label = cv2.resize(label, (256, 256))

        img_a = img_a / 255.0
        img_b = img_b / 255.0
        label = label / 255.0

        combined = np.concatenate([img_a, img_b], axis=2)

        combined = np.transpose(combined, (2, 0, 1))

        label = np.expand_dims(label, axis=0)

        return (
            torch.tensor(combined, dtype=torch.float32),
            torch.tensor(label, dtype=torch.float32)
        )