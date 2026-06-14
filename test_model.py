import torch
from semantic_model import SemanticUNet

model = SemanticUNet(
    num_classes=3
)

x = torch.randn(
    4,
    6,
    256,
    256
)

y = model(x)

print(y.shape)