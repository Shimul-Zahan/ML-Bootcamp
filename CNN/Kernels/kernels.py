import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread(r'e:\ML-Bootcamp-Practical\CNN\CNN vs Deformable CNN\resources\9919.png')

if image is None:
    print("Error: Image not loaded. Check the file path.")
else:
    # Convert the image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 1. Identity Kernel (No change)
    identity_kernel = np.array([[0, 0, 0],
                                [0, 1, 0],
                                [0, 0, 0]])
    identity = cv2.filter2D(image_gray, -1, identity_kernel)

    # 2. Sobel Edge Detection Kernel (Horizontal edges)
    sobel_kernel_x = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])
    sobel_x = cv2.filter2D(image_gray, -1, sobel_kernel_x)

    # 3. Gaussian Blur Kernel
    gaussian_kernel = np.array([[1/16, 1/8, 1/16],
                                [1/8, 1/4, 1/8],
                                [1/16, 1/8, 1/16]])
    gaussian_blur = cv2.filter2D(image_gray, -1, gaussian_kernel)

    # 4. Sharpening Kernel
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    sharpened = cv2.filter2D(image_gray, -1, sharpening_kernel)

    # 5. Embossing Kernel
    emboss_kernel = np.array([[-2, -1, 0],
                              [-1, 1, 1],
                              [0, 1, 2]])
    embossed = cv2.filter2D(image_gray, -1, emboss_kernel)

    # Displaying all images using Matplotlib
    titles = ['Original', 'Identity', 'Sobel (X)', 'Gaussian Blur', 'Sharpened', 'Embossed']
    images = [image_gray, identity, sobel_x, gaussian_blur, sharpened, embossed]

    plt.figure(figsize=(12, 6))
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()
