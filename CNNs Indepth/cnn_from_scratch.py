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

def visualization_each_layer_output(tensor, title = 'image'):
    image = tensor.squeeze(0).permute(1, 2, 0).numpy()
    image = np.clip(image, 0, 1)
    plt.imshow(image)
    plt.title(title)
    plt.show()



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
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        # Layer 2
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        
        # fully connected layer.
        # A fully connected (linear) layer that takes the flattened output of the previous layers (64 * 7 * 7) and maps it to 1000 neurons.
        self.fc1 = nn.Linear(64 * 56 * 56, 1000)  # flatten the output from layer 2 
        # fully connected layer that maps the 1000 neurons to 10 output classes
        self.fc2 = nn.Linear(1000, 1)
        
        
    def forward(self, x):
        
        visualization_each_layer_output(x, title='original image')
        
        # Pass the input through the layers
        x = self.conv1(x)
        print(f'After Conv1: {x.shape}')  # Output after Conv1
        self.show_feature_maps(x, title='Conv1 Feature Maps')
        
        x = self.relu1(x)
        print(f'After Conv1: {x.shape}')  # Output after Conv1
        self.show_feature_maps(x, title='Conv1 Feature Maps')
        
        x = self.pool1(x)
        print(f'After Conv1: {x.shape}')  # Output after Conv1
        self.show_feature_maps(x, title='Conv1 Feature Maps')
        
        
        # second layer
        x = self.conv2(x)
        print(f'After Conv1: {x.shape}')  # Output after Conv1
        self.show_feature_maps(x, title='Conv1 Feature Maps')
        
        x = self.relu2(x)
        print(f'After Conv1: {x.shape}')  # Output after Conv1
        self.show_feature_maps(x, title='Conv1 Feature Maps')
        
        x = self.pool2(x)
        print(f'After Conv1: {x.shape}')  # Output after Conv1
        self.show_feature_maps(x, title='Conv1 Feature Maps')
        
        # flatten the layer
        x = x.view(-1, 64 * 56 * 56)
        print(f'After Flatten: {x.shape}')
        
        # Pass the flattened tensor through fully connected layers
        x = self.fc1(x)
        print(f'After FC1: {x.shape}')
        x = self.fc2(x)
        print(f'After FC2: {x.shape}')

        return x
    
    def show_feature_maps(self, feature_map, title):
        
        """ Helper function to display feature maps """
        # feature_maps is a tensor of shape [batch_size, num_channels, height, width]
        
        num_channels = feature_map.shape[1]
        fig, axes = plt.subplots(1, num_channels, figsize =(num_channels * 2, 2))
        for i in range(num_channels):
            axes[i].imshow(feature_map[0, i].detach().cpu().numpy(), cmap='gray')
            axes[i].axis('off')
        plt.suptitle(title)
        plt.show()
    
# TODO 3: Train the model
def train(image_tensor):
    model = SimpleCNN()
    target = torch.tensor([1])   # class 1
    # Loss function (CrossEntropyLoss) and Optimizer (Adam)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001
    )
    epochs = 1
    for epoch in range(epochs):
        model.train()
        
        optimizer.zero_grad()
        
        # Forward pass
        output = model(image_tensor)
        print(f'Output: {output.shape}')  # Final output shape
        
        # compute the loss
        loss = criterion(output, target)
        print(f'Loss: {loss.item()}')
        
        # Backward pass (gradient computation)
        loss.backward()
        
        # Optimizer step
        optimizer.step()
        
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')


if __name__=="__main__":
    train(image_tensor)