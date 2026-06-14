import numpy as np
from semantic_dataset import SemanticDataset

dataset = SemanticDataset(
    "second/second_dataset/SECOND_train_set"
)

print("Samples:", len(dataset))

image_pair, label1, label2 = dataset[0]

print(image_pair.shape)
print(label1.shape)
print(label2.shape)

print(np.unique(label1.numpy())[:20])