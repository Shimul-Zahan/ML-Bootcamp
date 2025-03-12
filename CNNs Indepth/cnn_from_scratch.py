import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import torch
from torchvision import transforms
from PIL import Image

# image_path = r'E:\ML-Bootcamp-Practical\CNNs Indepth\resources\download.jpg'
image_path = r'E:\ML-Bootcamp-Practical\CNNs Indepth\resources\IMG_4117.JPG'
image = Image.open(image_path)
print(image, 'here is the image array')


transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.RandomVerticalFlip()
])

image_tensor = transforms(image)
print(image_tensor.shape)  # torch.Size([3, 128, 128])
image_tensor = transforms(image).unsqueeze(0)
print(image_tensor) # torch.Size([b=1, c=3, h=128, w=128])

# this is for image representation
'''
    transformed_image = image_tensor.permute(1, 2, 0)
    transformed_image = transformed_image.numpy()
    transformed_image = transformed_image.clip(0, 1)


    # Plot the image using matplotlib
    plt.imshow(transformed_image)
    plt.axis('off')  # Turn off the axis
    plt.show()
'''
# Show the image
plt.imshow(image)
plt.title("Loaded Image")
plt.axis("off")
plt.show()

print(f"Image Tensor Shape: {image_tensor.shape}")  # Should be [1, 3, 128, 128]