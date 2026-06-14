import os
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt

from semantic_model import SemanticUNet

# ================= DEVICE =================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ================= MODEL =================

model = SemanticUNet(
    num_classes=3
)

model.load_state_dict(
    torch.load(
        "semantic_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()

print("✅ Model Loaded")

# ================= IMAGE PATHS =================

root = "second/second_dataset/SECOND_train_set"

file_name = sorted(
    os.listdir(
        os.path.join(root, "im1")
    )
)[0]

img1_path = os.path.join(
    root,
    "im1",
    file_name
)

img2_path = os.path.join(
    root,
    "im2",
    file_name
)

# ================= TRANSFORM =================

transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

# ================= LOAD IMAGES =================

img1 = Image.open(
    img1_path
).convert("RGB")

img2 = Image.open(
    img2_path
).convert("RGB")

img1_tensor = transform(img1)
img2_tensor = transform(img2)

image_pair = torch.cat(
    [img1_tensor, img2_tensor],
    dim=0
).unsqueeze(0)

image_pair = image_pair.to(device)

# ================= PREDICTION =================

with torch.no_grad():

    output = model(
        image_pair
    )

prediction = torch.argmax(
    output,
    dim=1
).squeeze().cpu().numpy()

print("Prediction Shape:", prediction.shape)

# ================= SAVE =================

plt.imshow(
    prediction,
    cmap="viridis"
)

plt.colorbar()

plt.title(
    "Semantic Prediction"
)

plt.savefig(
    "prediction.png"
)

plt.show()

print("✅ Saved prediction.png")