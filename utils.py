import cv2
import numpy as np

def create_overlay(image, mask):

    overlay = image.copy()

    red_mask = np.zeros_like(image)
    red_mask[:, :, 2] = 255

    mask = (mask > 0.5).astype(np.uint8)

    overlay = np.where(
        mask[:, :, None],
        cv2.addWeighted(image, 0.7, red_mask, 0.3, 0),
        image
    )

    return overlay