from PIL import Image
import numpy as np
import os

path = "second/second_dataset/SECOND_train_set/label1"

file = sorted(os.listdir(path))[0]

img = Image.open(
    os.path.join(path, file)
)

arr = np.array(img)

colors = np.unique(
    arr.reshape(-1, 3),
    axis=0
)

print("Number of colors:", len(colors))
print(colors[:20])