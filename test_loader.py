from semantic_dataset import SemanticDataset
from torch.utils.data import DataLoader

dataset = SemanticDataset(
    "second/second_dataset/SECOND_train_set"
)

loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)

images, label1, label2 = next(iter(loader))

print(images.shape)
print(label1.shape)
print(label2.shape)