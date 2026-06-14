import torch
from torch.utils.data import DataLoader
from semantic_dataset import SemanticDataset
from semantic_model import SemanticUNet

# ================= DEVICE =================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Device:", device)

# ================= DATASET =================

dataset = SemanticDataset(
    "second/second_dataset/SECOND_train_set"
)

loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=False
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

# ================= METRICS =================

correct_pixels = 0
total_pixels = 0

with torch.no_grad():

    for images, label1, label2 in loader:

        images = images.to(device)
        label2 = label2.to(device)

        outputs = model(images)

        predictions = torch.argmax(
            outputs,
            dim=1
        )

        correct_pixels += (
            predictions == label2
        ).sum().item()

        total_pixels += label2.numel()

accuracy = (
    correct_pixels /
    total_pixels
) * 100

print("\n📊 Evaluation Results")
print(f"Pixel Accuracy: {accuracy:.2f}%")