import cv2
import torch
import numpy as np
from model import UNet
from utils import create_overlay

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = UNet().to(device)

model.load_state_dict(
    torch.load("saved_models/model.pth", map_location=device)
)

model.eval()

before = cv2.imread("before.png")
after = cv2.imread("after.png")

before_resized = cv2.resize(before, (256, 256))
after_resized = cv2.resize(after, (256, 256))

before_norm = before_resized / 255.0
after_norm = after_resized / 255.0

combined = np.concatenate([before_norm, after_norm], axis=2)

combined = np.transpose(combined, (2, 0, 1))

input_tensor = torch.tensor(
    combined,
    dtype=torch.float32
).unsqueeze(0).to(device)

with torch.no_grad():

    prediction = model(input_tensor)

mask = prediction.squeeze().cpu().numpy()

binary_mask = (mask > 0.5).astype(np.uint8)

overlay = create_overlay(before_resized, binary_mask)

cv2.imwrite("predicted_mask.png", binary_mask * 255)
cv2.imwrite("overlay.png", overlay)

print("Prediction Saved")