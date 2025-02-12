import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# all resources path => e:\ML-Bootcamp-Practical\CNN\CNN vs Deformable CNN\resources

# current_direcrory = os.chdir(os.path.dirname(os.path.abspath(__file__)))

image = cv2.imread(r'e:\ML-Bootcamp-Practical\CNN\CNN vs Deformable CNN\resources\9919.png')
if image is None:
    print("Error: Image not loaded. Check the file path.")
else:
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Displaying using Matplotlib
    plt.imshow(image_gray, cmap='gray')
    plt.axis('off')  # Hides the axes for better visualization
    plt.title("Gray scaled image")
    plt.show()
