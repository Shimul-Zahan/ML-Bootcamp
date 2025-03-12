import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import torch
from torchvision import transforms
from PIL import Image
import torch.nn as nn
import torch.nn.functional as F

# TODO 1 : Image Preprocessing
# image_path = r'E:\ML-Bootcamp-Practical\CNNs Indepth\resources\download.jpg'
image_path = r'E:\ML-Bootcamp-Practical\CNNs Indepth\resources\IMG_4117.JPG'
image = Image.open(image_path)
print(image, 'here is the image array')


transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    # transforms.RandomVerticalFlip()
])

image_tensor = transforms(image)
print(image_tensor.shape)  # torch.Size([3, 128, 128])
image_tensor = transforms(image).unsqueeze(0)
print(image_tensor) # torch.Size([b=1, c=3, h=128, w=128])

# this is only for image representation
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
'''
    plt.imshow(image)
    plt.title("Loaded Image")
    plt.axis("off")
    plt.show()

    print(f"Image Tensor Shape: {image_tensor.shape}")  # Should be [1, 3, 128, 128]
'''

# TODO 2: Here is we build or write out model structure code using PyTorch
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        
        '''
            class Conv2d(
                in_channels: int,
                out_channels: int,
                kernel_size: _size_2_t,
                stride: _size_2_t = 1,
                padding: _size_2_t | str = 0,
                dilation: _size_2_t = 1,
                groups: int = 1,
                bias: bool = True,
                padding_mode: str = "zeros",
                device: Any | None = None,
                dtype: Any | None = None
            )
            
            class MaxPool2d(
                kernel_size: _size_any_t,
                stride: _size_any_t | None = None,
                padding: _size_any_t = 0,
                dilation: _size_any_t = 1,
                return_indices: bool = False,
                ceil_mode: bool = False
            )
        '''
        
        # define the layers
        # Layer 1
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        # Layer 2
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=164, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        
        # fully connected layer.
        # A fully connected (linear) layer that takes the flattened output of the previous layers (64 * 7 * 7) and maps it to 1000 neurons.
        self.fc1 = nn.Linear(64 * 7 * 7, 1000)  # flatten the output from layer 2 
        # fully connected layer that maps the 1000 neurons to 10 output classes
        self.fc2 = nn.Linear(1000, 2)
        
        
    def forword(self, x):
        # Pass the input through the layers
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        # second layer
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)
        
        # flatten the layer
        x = x.view(-1, 64 * 7 * 7)
        
        # Pass the flattened tensor through fully connected layers
        x = self.fc1(x)
        x = self.fc2(x)

        return x