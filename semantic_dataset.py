import os
import torch
import numpy as np
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


def rgb_to_class(mask):

    class_mask = np.zeros(
        (mask.shape[0], mask.shape[1]),
        dtype=np.int64
    )

    class_mask[
        np.all(mask == [0, 128, 0], axis=-1)
    ] = 0

    class_mask[
        np.all(mask == [128, 128, 128], axis=-1)
    ] = 1

    class_mask[
        np.all(mask == [255, 255, 255], axis=-1)
    ] = 2

    return class_mask


class SemanticDataset(Dataset):

    def __init__(self, root_dir):

        self.root_dir = root_dir

        self.im1_dir = os.path.join(
            root_dir,
            "im1"
        )

        self.im2_dir = os.path.join(
            root_dir,
            "im2"
        )

        self.label1_dir = os.path.join(
            root_dir,
            "label1"
        )

        self.label2_dir = os.path.join(
            root_dir,
            "label2"
        )

        self.images = sorted(
            os.listdir(self.im1_dir)
        )

        self.transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor()
        ])

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):

        file_name = self.images[idx]

        # ---------- Images ----------

        img1 = Image.open(
            os.path.join(
                self.im1_dir,
                file_name
            )
        ).convert("RGB")

        img2 = Image.open(
            os.path.join(
                self.im2_dir,
                file_name
            )
        ).convert("RGB")

        img1 = img1.resize(
            (256, 256),
            Image.BILINEAR
        )

        img2 = img2.resize(
            (256, 256),
            Image.BILINEAR
        )

        img1 = self.transform(img1)
        img2 = self.transform(img2)

        # ---------- Labels ----------

        label1 = Image.open(
            os.path.join(
                self.label1_dir,
                file_name
            )
        ).convert("RGB")

        label2 = Image.open(
            os.path.join(
                self.label2_dir,
                file_name
            )
        ).convert("RGB")

        label1 = label1.resize(
            (256, 256),
            Image.NEAREST
        )

        label2 = label2.resize(
            (256, 256),
            Image.NEAREST
        )

        label1 = rgb_to_class(
            np.array(label1)
        )

        label2 = rgb_to_class(
            np.array(label2)
        )

        label1 = torch.tensor(
            label1,
            dtype=torch.long
        )

        label2 = torch.tensor(
            label2,
            dtype=torch.long
        )

        # ---------- Concatenate Images ----------

        image_pair = torch.cat(
            [img1, img2],
            dim=0
        )

        return (
            image_pair,
            label1,
            label2
        )