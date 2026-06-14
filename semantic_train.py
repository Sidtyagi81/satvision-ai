import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from semantic_dataset import SemanticDataset
from semantic_model import SemanticUNet

# ================= DEVICE =================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print(f"\n🚀 Device: {device}\n")

# ================= DATASET =================

dataset = SemanticDataset(
    "second/second_dataset/SECOND_train_set"
)

print(f"📂 Dataset Size: {len(dataset)} samples")

loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)

print(f"📦 Batches per Epoch: {len(loader)}\n")

# ================= MODEL =================

model = SemanticUNet(
    num_classes=3
).to(device)

# ================= LOSS =================

criterion = nn.CrossEntropyLoss()

# ================= OPTIMIZER =================

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=1e-4
)

# ================= TRAIN =================

epochs = 10

print("🔥 Training Started...\n")

for epoch in range(epochs):

    model.train()

    running_loss = 0

    print(
        f"\n========== Epoch {epoch+1}/{epochs} =========="
    )

    for batch_idx, (images, label1, label2) in enumerate(loader):

        images = images.to(device)

        label2 = label2.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(
            outputs,
            label2
        )

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        if batch_idx % 50 == 0:

            percent = (
                batch_idx / len(loader)
            ) * 100

            print(
                f"Epoch {epoch+1} | "
                f"Batch {batch_idx}/{len(loader)} "
                f"({percent:.1f}%) | "
                f"Loss: {loss.item():.4f}"
            )

    avg_loss = running_loss / len(loader)

    print(
        f"\n✅ Epoch [{epoch+1}/{epochs}] "
        f"Completed | Avg Loss: {avg_loss:.4f}"
    )

# ================= SAVE =================

torch.save(
    model.state_dict(),
    "semantic_model.pth"
)

print("\n🎉 Training Finished!")
print("💾 Model saved as semantic_model.pth")