import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# Step 1: Generate synthetic data (2D, non-linearly separable)
X, y = datasets.make_circles(n_samples=100, factor=0.5, noise=0.1)

# Define gamma values for the different SVM models
gamma_values = [0.1, 1, 10]

# Step 2: Create subplots for each gamma value
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Step 3: Train an SVM classifier with the RBF kernel and varying gamma
for i, gamma in enumerate(gamma_values):
    # Train SVM model with a specific gamma value
    svm = SVC(kernel='rbf', gamma=gamma)
    svm.fit(X, y)
    
    # Define meshgrid for plotting decision boundaries
    h = 0.02  # Step size in the mesh grid
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # Predict class for each point in the mesh grid
    Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plotting the decision boundary
    axes[i].contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.Paired)

    # Plotting the data points and support vectors
    axes[i].scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', s=50, cmap=plt.cm.Paired)
    axes[i].scatter(svm.support_vectors_[:, 0], svm.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k', marker='x')

    axes[i].set_title(f"SVM with RBF Kernel (gamma={gamma})")
    axes[i].set_xlabel('Feature 1')
    axes[i].set_ylabel('Feature 2')

# Step 4: Display the plot
plt.tight_layout()
plt.show()
