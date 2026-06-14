import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm
from model import UNet
from dataset import ChangeDetectionDataset


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_dataset = ChangeDetectionDataset("train")

train_loader = DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True
)

model = UNet().to(device)

criterion = nn.BCELoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

epochs = 10

print("Training Started...")

for epoch in range(epochs):

    model.train()

    epoch_loss = 0

    progress_bar = tqdm(
        train_loader,
        desc=f"Epoch {epoch+1}/{epochs}"
    )

    for images, masks in progress_bar:

        images = images.to(device)
        masks = masks.to(device)

        outputs = model(images)

        loss = criterion(outputs, masks)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        epoch_loss += loss.item()

        progress_bar.set_postfix(
            loss=loss.item()
        )

    print(
        f"Epoch [{epoch+1}/{epochs}] "
        f"Loss: {epoch_loss:.4f}"
    )

torch.save(
    model.state_dict(),
    "saved_models/model.pth"
)

print("Model Saved Successfully")